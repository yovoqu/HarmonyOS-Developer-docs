# @Prop：父子单向同步

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management-prop
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

@Prop用于[状态管理V1](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-overview#状态管理v1)，接收外部传入值，并与父组件建立单向同步关系。当父组件中[@State](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management-state)等装饰的状态变量发生变化时，会同步更新到子组件中对应的@Prop变量，触发子组件重新渲染。@Prop采用单向数据流机制，子组件对@Prop变量的修改仅在子组件内部生效，不会反向同步到父组件。适用于子组件需要响应父组件状态变化但不需要反向修改的场景。

开发指南参考：[@Prop装饰器：父子单向同步](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-prop)。

> [!NOTE]
> 从API version 7开始，支持该装饰器。



#### @Prop

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

const Prop: PropertyDecorator

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```text
@Component
struct Child {
  // 使用@Prop装饰器接收父组件传入的值，与父组件建立单向同步关系
  // 父组件数据变化会同步到子组件，但子组件修改不会同步回父组件
  @Prop message: string = 'Hi';

  build() {
    Column() {
      Text(this.message)
    }
  }
}

@Entry
@Component
struct Index {
  // 使用@State声明状态变量，作为@Prop的数据源
  @State message: string = 'Hello';

  build() {
    Column() {
      // 创建子组件Child，将message单向绑定到子组件的@Prop变量
      Child({ message: this.message })
    }
  }
}
```
