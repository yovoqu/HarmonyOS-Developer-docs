# @BuilderParam装饰器：引用@Builder函数

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-builderparam-dynamic
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

@BuilderParam用于装饰指向[@Builder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-builder-dynamic)函数的变量，使自定义组件能够接收外部传入的@Builder函数，实现UI内容的自定义渲染。适用于需要将父组件的UI构建逻辑传递给子组件、实现组件内容动态定制的场景。

开发指南参考：[@BuilderParam装饰器：引用@Builder函数](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builderparam)。

> [!NOTE]
> 该装饰器从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。



#### @BuilderParam

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

const BuilderParam: PropertyDecorator

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**示例：**

```text
@Component
struct Child {
  @Builder
  customBuilder() {
  }

  // 使用@BuilderParam装饰器声明一个指向@Builder函数的变量
  // 类型为无参无返回值的函数，默认值为子组件内部的customBuilder
  @BuilderParam customBuilderParam: () => void = this.customBuilder;

  build() {
    Column() {
      // 调用@BuilderParam引用的构建函数来渲染UI
      this.customBuilderParam()
    }
  }
}

@Entry
@Component
struct Parent {
  @Builder
  componentBuilder() {
    Text(`Parent builder`)
  }

  build() {
    Column() {
      // 创建子组件Child，将父组件的componentBuilder传入customBuilderParam
      Child({ customBuilderParam: this.componentBuilder })
    }
  }
}
```
