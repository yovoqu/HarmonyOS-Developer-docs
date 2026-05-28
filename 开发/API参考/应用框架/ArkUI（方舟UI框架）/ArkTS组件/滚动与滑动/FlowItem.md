# FlowItem

更新时间：2026-05-18 03:44:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flowitem
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

瀑布流组件[WaterFlow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow)的子组件，用来展示瀑布流具体item。
 
> [!NOTE]
> 该组件从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。 仅支持作为 WaterFlow 组件的子组件使用。 在滑动场景中，由于FlowItem及其子组件的频繁创建与销毁，建议将FlowItem中的组件封装为自定义组件，并使用@Reusable装饰器进行修饰，以增强组件的复用能力，从而减少ArkUI框架内部重复创建和销毁节点的开销。最佳实践请参考 优化瀑布流加载慢丢帧问题-组件复用 。

  

#### 子组件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

支持单个子组件。
 
  

#### 接口

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

FlowItem()
 
使用该接口来创建瀑布流子组件。
 
**元服务API：** 从API version 11开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
  

#### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

无
 
  

#### 示例

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

详见[瀑布流组件示例](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow#示例)。
