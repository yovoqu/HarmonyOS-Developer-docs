# 检测环境中的平面（C/C++）

更新时间：2026-04-24 08:10:21

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-get-plane

## 概要

本章节给出了关键开发步骤，完整代码可以参考[示例代码](https://gitcode.com/harmonyos_samples/arengine_-sample-code_-clientdemo_cpp)。

## 约束与限制

检测环境平面能力支持部分Phone、部分Tablet设备。请参考[硬件要求](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-preparations#硬件要求)判断设备是否支持运动跟踪及平面识别特性（[ARENGINE_FEATURE_TYPE_SLAM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#arengine_featuretype)）。

## 引入AR Engine

开发者可参考管理AR会话章节的[引入AR Engine](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-arsession#引入ar-engine)。

## 创建ARSession

开发者可以参考[管理AR会话](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-arsession)创建ARSession。

## 创建平面对象列表

创建一个平面对象列表planeList，用于存放AR Engine运行过程中检测到的所有平面。
```text
AREngine_ARTrackableList *planeList = nullptr;
HMS_AREngine_ARTrackableList_Create(arSession, &planeList);
```

设置可跟踪对象类型为ARENGINE_TRACKABLE_PLANE。
```text
AREngine_ARTrackableType planeTrackedType = ARENGINE_TRACKABLE_PLANE;
```


## 识别当前环境中的平面

调用[HMS_AREngine_ARSession_GetAllTrackables](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#hms_arengine_arsession_getalltrackables)函数，检测当前环境中的所有平面，并将结果存放在planeList中。
```text
HMS_AREngine_ARSession_GetAllTrackables(arSession, planeTrackedType, planeList);
```


## 获取平面数量

调用[HMS_AREngine_ARTrackableList_GetSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#hms_arengine_artrackablelist_getsize)函数获取平面数量，结果存放在planeListSize中。
```text
int32_t planeListSize = 0;
HMS_AREngine_ARTrackableList_GetSize(arSession, planeList, &planeListSize);
```

在应用环境中，可能存在0个、1个或多个平面。 当planeListSize等于0时，表示当前环境中不存在平面。 当planeListSize等于1时，表示当前环境中仅存在1个平面。 当planeListSize大于1时，表示当前环境中存在多个平面。

## 获取平面实例

当存在1个或多个平面时，可以依次遍历planeList获取所有平面对象。
```text
for (int i = 0; i 对于第i个平面，创建并获取可跟踪对象，并将其转化为平面对象[AREngine_ARPlane](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#arengine_arplane)。
```text
AREngine_ARTrackable *arTrackable = nullptr;
HMS_AREngine_ARTrackableList_AcquireItem(arSession, planeList, i, &arTrackable);
AREngine_ARPlane *arPlane = reinterpret_cast(arTrackable);
```


> [!NOTE]
> AR Engine中，任何物体都被定义为可跟踪对象AREngine_ARTrackable。平面也是一种可跟踪对象，开发者可以通过类型转换reinterpret_cast将可跟踪对象AREngine_ARTrackable转化为平面对象AREngine_ARPlane。


## 销毁平面对象列表


```text
HMS_AREngine_ARTrackableList_Destroy(planeList);
```
