# 识别平面语义（C/C++）

更新时间：2026-08-14 11:17:56

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-get-semantics

本章节给出了关键开发步骤，完整代码可以参考[示例代码](https://gitcode.com/harmonyos_samples/arengine_-sample-code_-clientdemo_cpp)。


#### 约束与限制

从5.0.0(12)开始，识别平面语义能力支持部分Phone、部分Tablet设备。请参考[硬件要求](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-preparations#硬件要求)判断设备是否支持平面语义及物体语义特性（[ARENGINE_FEATURE_TYPE_SEMANTIC](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#arengine_featuretype)）。



#### 引入AR Engine

开发者可参考管理AR会话章节的[引入AR Engine](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-arsession#引入ar-engine)。



#### 创建AR会话

创建AR会话并配置为平面语义识别模式。

```text
CHECK(HMS_AREngine_ARSession_Create(nullptr, nullptr, &mArSession));

AREngine_ARConfig *arConfig = nullptr;
CHECK(HMS_AREngine_ARConfig_Create(mArSession, &arConfig));
// ...
SetSemanticDenseMode(params.semanticDenseMode, mArSession, arConfig);
AREngine_ARSemanticDenseMode outSemanticDenseMode = ARENGINE_SEMANTIC_DENSE_MODE_DISABLED;
HMS_AREngine_ARConfig_GetSemanticDenseMode(mArSession, arConfig, &outSemanticDenseMode);
CHECK(HMS_AREngine_ARSession_Configure(mArSession, arConfig));
```



#### 检测环境中的平面

进行平面语义识别之前，需要先检测环境中的平面。开发者可以参考[检测环境中的平面](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-get-plane)完成平面检测过程，并获取环境中的平面数量。当存在平面时，就可以继续下面的步骤。



#### 初始化平面语义标签

创建并初始化平面语义标签label，用于描述平面的语义。

```text
AREngine_ARSemanticPlaneLabel planeLabel = ARENGINE_PLANE_UNKNOWN;
```

平面语义标签定义为枚举类型，包括12种枚举值（1种未知类型+11种平面类型）。 参考[AREngine_ARSemanticPlaneLabel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#arengine_arsemanticplanelabel)



#### 识别平面类型

调用[HMS_AREngine_ARPlane_GetLabel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#hms_arengine_arplane_getlabel)函数，获取平面类型，结果存放在label中。平面的获取可以参考[获取平面实例](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-get-plane#获取平面实例)。

```text
HMS_AREngine_ARPlane_GetLabel(arSession, arPlane, &planeLabel);
```
