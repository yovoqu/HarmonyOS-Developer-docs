# canvas组件

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-canvas
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

> [!NOTE]
> 从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

 
提供画布组件。用于自定义绘制图形。
  

##### 权限列表

无
 
  

##### 子组件

不支持。
 
  

##### 属性

支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-attributes)。
 
  

##### 样式

支持[通用样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-styles)。
 
  

##### 事件

支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-events)。
 
  

##### 方法

除支持[通用方法](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-methods)外，还支持如下方法：
 
  

##### getContext

getContext(type: '2d', options?: ContextAttrOptions): CanvasRenderingContext2D
 
获取canvas绘图上下文。不支持在onInit和onReady中进行调用。
 
**参数：**
  
| 参数名 | 参数类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| type | string | 是 | 设置为'2d'，返回值为2D绘制对象，该对象可用于在画布组件上绘制矩形、文本、图片等。 |
| options6+ | ContextAttrOptions | 否 | 当前仅支持配置是否开启抗锯齿功能，默认为关闭。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| CanvasRenderingContext2D | 用于在画布组件上绘制矩形、文本、图片等。 |
 
 
  

##### toDataURL6+

toDataURL(type?: string, quality?: number): string
 
生成一个包含图片展示的URL。
 
**参数：**
  
| 参数名 | 参数类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| type | string | 否 | 可选参数，用于指定图像格式，默认格式为image/png。 |
| quality | number | 否 | 在指定图片格式为image/jpeg或image/webp的情况下，可以从0到1的区间内选择图片的质量。如果超出取值范围，将会使用默认值0.92。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| string | 图像的URL地址。 |
 
 
  

##### ContextAttrOptions6+

用于配置Canvas渲染上下文属性的选项对象。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| antialias | boolean | 否 | 是 | 是否开启抗锯齿功能。 true表示开启抗锯齿功能；false表示不开启抗锯齿功能。 默认值：false |
 
 
  

##### 示例

```text
<!-- xxx.hml -->
<div style="margin: 100; flex-direction: column">
  <canvas ref="canvas1" style="width: 200px; height: 150px; background-color: rgb(213, 213, 213);"></canvas>
  <input type="button" style="width: 180px; height: 60px; margin: 13;" value="fillStyle" onclick="handleClick" />
</div>
```
 
```text
// xxx.js
export default {
  handleClick() {
    const el = this.$refs.canvas1;
    var dataURL = el.toDataURL();
    console.info(dataURL);
    // "data:image/png;base64,xxxxxxxx..."
  }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/XySHcTpjT56sKpVfEQ4kYQ/zh-cn_image_0000002581436344.png?HW-CC-KV=V1&HW-CC-Date=20260528T013804Z&HW-CC-Expire=86400&HW-CC-Sign=FF55D4845775558987DE52E88143E65437908350656A12B71873506DFB9C607D)
