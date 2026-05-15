# @arkts.lang (ArkTS语言基础能力)

更新时间：2026-04-10 09:55:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkts-lang
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

本模块提供的ArkTS语言的基础类型定义。当前提供ISendable接口。


> [!NOTE]
> 本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
> 此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```ts
import { lang } from '@kit.ArkTS';
```


## lang.ISendable
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

是所有[Sendable](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#基础概念)类型（除null和undefined）的父类型。自身没有任何必须的方法和属性。

ArkTS中，ISendable类型的对象是Object类型的实例，遵循其基本特征，同时支持跨线程传递。

ISendable主要用在开发者自定义Sendable数据结构的场景中，ArkTS语言标准库中的容器类型（如[Array](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-array)、[Map](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-map)、[Set](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-set)等）隐式地继承并实现了ISendable。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**示例：**


```ts
// 构造一个用户自定义的Sendable数据结构
@Sendable
class CustomData implements lang.ISendable {
  data1: number;
  data2: string;
  constructor(data1: number, data2: string) {
    this.data1 = data1;
    this.data2 = data2;
  }
}
```
