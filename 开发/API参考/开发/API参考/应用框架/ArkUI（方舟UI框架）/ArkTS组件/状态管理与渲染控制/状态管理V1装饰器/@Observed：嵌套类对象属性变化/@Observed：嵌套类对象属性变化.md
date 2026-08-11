# @Observed：嵌套类对象属性变化

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management-observed
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

@Observed是类装饰器，用于[状态管理V1](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-overview#状态管理v1)中，观察嵌套类对象的属性变化。

开发指南参考：[@Observed装饰器和@ObjectLink装饰器：嵌套类对象属性变化](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-observed-and-objectlink)。

> [!NOTE]
> 从API version 7开始，支持该装饰器。



#### @Observed

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

const Observed: ClassDecorator

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```text
// 使用@Observed类装饰器，使Info类的属性变化可被ArkUI框架观察
@Observed
class Info {
  name: string;
  constructor(name: string) {
    this.name = name;
  }
}

@Entry
@Component
struct Index {
  @State info: Info = new Info('Tom');
  build() {
    Column() {
      Text(`name: ${this.info.name}`)
    }
  }
}
```
