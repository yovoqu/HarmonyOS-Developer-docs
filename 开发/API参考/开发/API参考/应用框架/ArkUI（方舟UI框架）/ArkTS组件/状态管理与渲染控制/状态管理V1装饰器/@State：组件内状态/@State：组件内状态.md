# @State：组件内状态

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management-state
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

@State用于[状态管理V1](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-overview#状态管理v1)，将自定义组件内的普通变量转变为状态变量，当状态变量变化时，触发组件内UI重新渲染。适用于需要在组件内管理可变状态的场景。

开发指南参考：[@State装饰器：组件内状态](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state)。

> [!NOTE]
> 从API version 7开始，支持该装饰器。



#### @State

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

const State: PropertyDecorator

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```text
@Entry
@Component
struct StateExample {
  @State count: number = 0; // 状态变量

  build() {
    Column() {
      Text(`${this.count}`)
    }
  }
}
```
