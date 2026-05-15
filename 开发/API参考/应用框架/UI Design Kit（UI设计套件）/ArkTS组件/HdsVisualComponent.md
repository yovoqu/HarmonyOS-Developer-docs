# HdsVisualComponent

更新时间：2026-04-29 07:35:50

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hds-visual-component
**支持设备：** Phone / PC/2in1 / Tablet / TV

HdsVisualComponent组件承载复杂视效实现，应用开发者通过HdsVisualComponent选择具体视效场景完成复杂视效的开发。

**起始版本：** 6.0.0(20)


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / TV


6.0.1(21)及之前版本：


```ts
import {
  HdsVisualComponent,
  HdsVisualComponentAttribute,
  HdsSceneController,
  HdsSceneType,
  hdsEffect,
} from '@kit.UIDesignKit';
```

6.0.2(22)及之后版本：


```ts
import {
  HdsVisualComponent,
  HdsSceneController,
  HdsSceneType,
  hdsEffect,
} from '@kit.UIDesignKit';
```


## 子组件
**支持设备：** Phone / PC/2in1 / Tablet / TV

无


## 接口
**支持设备：** Phone / PC/2in1 / Tablet / TV

HdsVisualComponent()

创建HdsVisualComponent通用视效组件。

**模型约束：** 此接口仅可在Stage模型下使用。

**卡片能力：** 从6.0.2(22)开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)


## 属性
**支持设备：** Phone / PC/2in1 / Tablet / TV

除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)，还支持以下属性：


### scene
**支持设备：** Phone / PC/2in1 / Tablet / TV

scene(sceneType: HdsSceneType, controller: HdsSceneController, callback?: HdsSceneFinishCallback, frameRateRange?: hdsEffect.ExpectedFrameRateRange)

设置视效场景

**模型约束：** 此接口仅可在Stage模型下使用。

**卡片能力：** 从6.0.2(22)开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sceneType | [HdsSceneType](#hdsscenetype) | 是 | 视效场景类型。 |
| controller | [HdsSceneController](#hdsscenecontroller) | 是 | 视效场景控制器。 |
| callback | [HdsSceneFinishCallback](#hdsscenefinishcallback) | 否 | 视效场景结束时触发的回调。 |
| frameRateRange | hdsEffect.[ExpectedFrameRateRange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdseffect#expectedframeraterange) | 否 | 视效场景帧率配置。 |


## 事件
**支持设备：** Phone / PC/2in1 / Tablet / TV

支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)。


## HdsSceneType
**支持设备：** Phone / PC/2in1 / Tablet / TV

视效场景。

**模型约束：** 此接口仅可在Stage模型下使用。

**卡片能力：** 从6.0.2(22)开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)


| 名称 | 值 | 说明 |
| --- | --- | --- |
| DUAL_EDGE_FLOW_LIGHT_WITH_BACKGROUND_MASK | 0 | 自带背景的双边流光。 说明：该场景在TV中无效果，在其他设备类型中可正常显示。 |


## HdsSceneFinishCallback
**支持设备：** Phone / PC/2in1 / Tablet / TV

type HdsSceneFinishCallback = () => void

场景视效结束回调函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**卡片能力：** 从6.0.2(22)开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)


## HdsSceneController
**支持设备：** Phone / PC/2in1 / Tablet / TV

场景控制器。

**模型约束：** 此接口仅可在Stage模型下使用。

**卡片能力：** 从6.0.2(22)开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)


### constructor
**支持设备：** Phone / PC/2in1 / Tablet / TV

constructor()

HdsSceneController的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**卡片能力：** 从6.0.2(22)开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)


### start
**支持设备：** Phone / PC/2in1 / Tablet / TV

start(): void

开始视效场景。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)


### pause
**支持设备：** Phone / PC/2in1 / Tablet / TV

pause(): void

暂停视效场景。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)


### resume
**支持设备：** Phone / PC/2in1 / Tablet / TV

resume(): void

恢复视效场景。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)


### stop
**支持设备：** Phone / PC/2in1 / Tablet / TV

stop(): void

停止视效场景。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)


### setSceneParams
**支持设备：** Phone / PC/2in1 / Tablet / TV

setSceneParams(params: SceneParams): HdsSceneController

设置场景参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [SceneParams](#sceneparams) | 是 | 场景参数。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| [HdsSceneController](#hdsscenecontroller) | 返回[HdsSceneController](#hdsscenecontroller)对象。 |


## SceneParams
**支持设备：** Phone / PC/2in1 / Tablet / TV

type SceneParams = DualEdgeFlowLightWithMaskParam

场景视效参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)


| 类型 | 说明 |
| --- | --- |
| [DualEdgeFlowLightWithMaskParam](#dualedgeflowlightwithmaskparam) | 双边边缘流光视效参数。 |


## DualEdgeFlowLightWithMaskParam
**支持设备：** Phone / PC/2in1 / Tablet / TV

双边边缘流光视效参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)


| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| backgroundMaskColors | Array&lt;[ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor)&gt; | 否 | 否 | 背景蒙层颜色数组。 |
| firstEdgeFlowLight | hdsEffect.[EdgeFlowLightParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdseffect#edgeflowlightparam) | 否 | 否 | 第一条流光参数配置。 |
| secondEdgeFlowLight | hdsEffect.[EdgeFlowLightParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdseffect#edgeflowlightparam) | 否 | 否 | 第二条流光参数配置。 |


## 示例
**支持设备：** Phone / PC/2in1 / Tablet / TV


```ts
// 从6.0.2(22)版本开始，无需手动导入HdsVisualComponentAttribute。具体请参考HdsVisualComponent的导入模块说明。
import { HdsVisualComponent, HdsVisualComponentAttribute, HdsSceneController, HdsSceneType } from '@kit.UIDesignKit';

@Entry
@Component
struct EdgeFlowLightVisualComponent {
  @State sceneController: HdsSceneController = new HdsSceneController()
  .setSceneParams({
    backgroundMaskColors: [Color.Green, Color.Red],
    firstEdgeFlowLight: {
      startPos: 0,
      endPos: 0.5,
      color: Color.Red
    },
    secondEdgeFlowLight: {
      startPos: 0,
      endPos: -0.5,
      color: Color.Green
    }
  })

  build() {
    Stack() {
      HdsVisualComponent()
      .scene(HdsSceneType.DUAL_EDGE_FLOW_LIGHT_WITH_BACKGROUND_MASK, this.sceneController, () => {
        console.info('Succeeded in finishing');
      })
      .width('100%')
      .height('50%')
    }
  }
}
```

![](assets/HdsVisualComponent/file-20260514164502910-0.gif)
