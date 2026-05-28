# @Env：环境变量

更新时间：2026-04-28 03:31:56

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-env-system-property
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

> [!NOTE]
> 本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。


开发者指南见：[@Env开发者指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-env-system-property)。


#### @Env

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

Env: EnvDecorator

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| Env | EnvDecorator | 环境变量装饰器。 |


**示例：**

```text
import { uiObserver } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  // @Env读取系统环境变量
  @Env(SystemProperties.BREAK_POINT) breakpoint: uiObserver.WindowSizeLayoutBreakpointInfo;

  build() {}
}
```



#### EnvDecorator

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

type EnvDecorator = (value: SystemProperties) => PropertyDecorator

定义@Env装饰器类型。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | SystemProperties | 是 | 环境变量属性名。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| PropertyDecorator | 属性装饰器。 |


**错误码：**

详细介绍请参见[环境变量错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-env)。

| 错误码ID | 错误信息 |
| --- | --- |
| 140000 | Invalid key for @Env |




#### SystemProperties

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义环境变量枚举值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BREAK_POINT | 'system.arkui.breakpoint' | @Env变量参数，通过@Env(SystemProperties.BREAK_POINT)可获取WindowSizeLayoutBreakpointInfo实例。 当该装饰器声明在@Component或@ComponentV2中时，用于获取当前自定义组件所在窗口的尺寸布局断点信息。 元服务API： 从API version 22开始，该接口支持在元服务中使用。 |
| WINDOW_SIZE23+ | 'system.window.size' | @Env变量参数，通过@Env(SystemProperties.WINDOW_SIZE)可获取SizeInVP实例。 当该装饰器声明在@Component或@ComponentV2中时，用于获取当前自定义组件所在窗口的大小信息，单位为vp。 模型约束：此接口仅可在Stage模型下使用。 |
| WINDOW_SIZE_PX23+ | 'system.window.size.px' | @Env变量参数，通过@Env(SystemProperties.WINDOW_SIZE_PX)可获取Size实例。 当该装饰器声明在@Component或@ComponentV2中时，用于获取当前自定义组件所在窗口的大小信息，单位为px。 模型约束：此接口仅可在Stage模型下使用。 |
| WINDOW_AVOID_AREA23+ | 'system.window.avoidarea' | @Env变量参数，通过@Env(SystemProperties.WINDOW_AVOID_AREA)可获取UIEnvWindowAvoidAreaInfoVP实例。 当该装饰器声明在@Component或@ComponentV2中时，用于获取当前自定义组件所在窗口的避让区域信息，单位为vp。 模型约束：此接口仅可在Stage模型下使用。 |
| WINDOW_AVOID_AREA_PX23+ | 'system.window.avoidarea.px' | @Env变量参数，通过@Env(SystemProperties.WINDOW_AVOID_AREA_PX)可获取UIEnvWindowAvoidAreaInfoPX实例。 当该装饰器声明在@Component或@ComponentV2中时，用于获取当前自定义组件所在窗口的避让区域信息，单位为px。 模型约束：此接口仅可在Stage模型下使用。 |
