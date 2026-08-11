# @Link：父子双向同步

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management-link
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

@Link用于[状态管理V1](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-overview#状态管理v1)，接收父组件传入的状态变量的引用，建立父子组件间的双向数据绑定。适用于需要在子组件中直接修改父组件状态、简化父子组件通信的场景。

开发指南参考：[@Link装饰器：父子双向同步](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-link)。

> [!NOTE]
> 从API version 7开始，支持该装饰器。



#### @Link

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

const Link: PropertyDecorator

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```text
@Component
struct Child {
  // 使用@Link装饰器声明双向绑定变量，与父组件数据源建立双向同步
  @Link msg: string;

  build() {
    Column() {
      Text(this.msg)
      Button('change')
        .onClick(() => {
          // 修改会同步到父组件
          this.msg += '~';
        })
    }
  }
}

@Entry
@Component
struct LinkExample {
  // 使用@State声明状态变量，作为@Link的数据源
  @State message: string = 'Hello';

  build() {
    Column() {
      // 创建子组件Child，通过@Link将message双向绑定到子组件的msg
      Child({ msg: this.message })
    }
  }
}
```
