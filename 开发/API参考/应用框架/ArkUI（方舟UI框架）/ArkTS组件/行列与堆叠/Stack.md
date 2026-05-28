# Stack

更新时间：2026-04-28 03:31:56

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-stack
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。
 
> [!NOTE]
> 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。 通用属性 align 在该组件上支持镜像能力。

  

##### 子组件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

可以包含子组件。
 
  

##### 接口

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

Stack(options?: StackOptions)
 
堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。
 
> [!NOTE]
> 过多的组件嵌套会导致性能劣化。在部分场景中，直接使用组件属性或借助系统API的能力可以替代层叠容器的效果，减少了嵌套组件数进而优化性能。最佳实践请参考 组件嵌套优化-优先使用组件属性代替嵌套组件 。

 
**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。
 
**元服务API：** 从API version 11开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | StackOptions | 否 | 设置子组件在容器内的对齐方式。 |
 
 
  

##### StackOptions18+对象说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

设置堆叠容器的子组件对齐方式。
 
> [!NOTE]
> 为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

 
**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。
 
**元服务API：** 从API version 18开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| alignContent7+ | Alignment | 否 | 是 | 设置子组件在容器内的对齐方式。 默认值：Alignment.Center 非法值：按默认值处理。 卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
 
 
  

##### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)外，还支持以下属性：
 
  

##### alignContent

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

alignContent(value: Alignment)
 
设置子组件在容器内的对齐方式。该属性与[align](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-location#align)同时设置时，后设置的属性生效。该属性与接口的构造入参同时设置时，生效属性上的设置效果。
 
**元服务API：** 从API version 11开始，该接口支持在元服务中使用。
 
**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Alignment | 是 | 所有子组件在容器内的对齐方式。 默认值：Alignment.Center 非法值：按默认值处理。 |
 
 
  

##### 事件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)。
 
  

##### 示例

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

Stack的alignContent设置为Alignment.Bottom条件下子组件显示效果。
 
```ArkTS
// xxx.ets
@Entry
@Component
struct StackExample {
  build() {
    Stack({ alignContent: Alignment.Bottom }) {
      Text('First child, show in bottom').width('90%').height('100%').backgroundColor(0xd2cab3).align(Alignment.Top)
      Text('Second child, show in top').width('70%').height('60%').backgroundColor(0xc1cbac).align(Alignment.Top)
    }.width('100%').height(150).margin({ top: 5 })
  }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/wYcC1S8xQCOWPtLs8mu0SQ/zh-cn_image_0000002611755663.png?HW-CC-KV=V1&HW-CC-Date=20260528T024158Z&HW-CC-Expire=86400&HW-CC-Sign=4F4C99A2795326EDDF88CDC35D2241ED493AD5964CEB84B105C523188D89D056)
