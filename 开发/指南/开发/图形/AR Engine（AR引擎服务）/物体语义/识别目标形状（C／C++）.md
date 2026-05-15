# 识别目标形状（C/C++）

更新时间：2026-04-24 08:10:21

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-get-plane-shape

## 约束与限制

识别目标形状能力支持部分Phone、部分Tablet设备。请参考[硬件要求](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-preparations#硬件要求)判断设备是否支持运动跟踪及平面识别特性（[ARENGINE_FEATURE_TYPE_SEMANTIC](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#arengine_featuretype)）。

## 引入AR Engine

开发者可参考管理AR会话章节的[引入AR Engine](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-arsession#引入ar-engine)。

## 创建AR会话

创建AR会话并配置为目标形状识别模式。
```text
AREngine_ARSession *arSession = nullptr;
// 创建AR会话。
HMS_AREngine_ARSession_Create(nullptr, nullptr, &arSession);
AREngine_ARConfig *arConfig = nullptr;
// 创建AR会话配置器。
HMS_AREngine_ARConfig_Create(arSession, &arConfig);
// 设置语义识别模式为目标形状识别。
HMS_AREngine_ARConfig_SetSemanticMode(arSession, arConfig, ARENGINE_SEMANTIC_MODE_TARGET);
// 配置器设置给AR会话。
HMS_AREngine_ARSession_Configure(arSession, arConfig);
```


## 创建可跟踪对象列表

创建一个可跟踪对象列表targetList，用于存放AR Engine运行过程中检测到的所有可跟踪对象。
```text
AREngine_ARTrackableList *targetList = nullptr;
HMS_AREngine_ARTrackableList_Create(arSession, &targetList);
```


## 获取当前环境中的可跟踪对象

调用[HMS_AREngine_ARSession_GetAllTrackables](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#hms_arengine_arsession_getalltrackables)函数，检测当前环境中的所有可跟踪对象，并将结果存放在targetList中。
```text
HMS_AREngine_ARSession_GetAllTrackables(arSession, ARENGINE_TRACKABLE_TARGET, targetList);
```


## 获取可跟踪对象数量

调用[HMS_AREngine_ARTrackableList_GetSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#hms_arengine_artrackablelist_getsize)函数获取当前可跟踪对象数量，结果存放在targetSize中。
```text
int32_t targetSize = 0;
HMS_AREngine_ARTrackableList_GetSize(arSession, targetList, &targetSize);
```

当targetSize等于0时，代表当前环境中无可跟踪对象。 当targetSize等于1时，代表当前环境中仅存在1个可跟踪对象。 当targetSize大于1时，代表当前环境中存在多个可跟踪对象。

## 遍历并识别物体形状

当环境中存在一个或多个可跟踪对象时，依次遍历targetList中所有可跟踪对象进行目标形状识别。
```text
for (int i = 0; i              对于第i个对象，创建并获取对象实例。
```text
AREngine_ARTrackable *target = nullptr;
HMS_AREngine_ARTrackableList_AcquireItem(arSession, targetList, i, &target);
```

             获取该实例跟踪状态，仅当跟踪状态为[ARENGINE_TRACKING_STATE_TRACKING](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#arengine_artrackingstate)时，才可进行形状识别。
```text
AREngine_ARTrackingState outTrackingState;
HMS_AREngine_ARTrackable_GetTrackingState(arSession, target, &outTrackingState);

if (AREngine_ARTrackingState::ARENGINE_TRACKING_STATE_TRACKING != outTrackingState) {
continue;
}
```

             获取该实例目标形状，识别结果存放在label中。
```text
AREngine_ARTargetShapeLabel label = ARENGINE_TARGET_SHAPE_UNKNOWN;
HMS_AREngine_ARTarget_GetShapeType(arSession, reinterpret_cast(target), &label);
```

       其中，[AREngine_ARTargetShapeLabel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#arengine_artargetshapelabel)为枚举类型，描述了目标物体形状。

## 销毁可跟踪对象列表


```text
HMS_AREngine_ARTrackableList_Destroy(targetList);
```
