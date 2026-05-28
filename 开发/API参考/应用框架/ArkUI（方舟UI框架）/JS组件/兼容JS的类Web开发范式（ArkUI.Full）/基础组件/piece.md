# piece

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-piece
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

一种块状的入口，可包含图片和文本，常用于展示收件人。例如，邮件收件人或信息收件人。
 
> [!NOTE]
> 从API version 5开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

  

#### 子组件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

无
 
  

#### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-attributes)外，还支持如下属性：
  
| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| content | string | 是 | 操作块文本内容。 |
| closable | boolean | 否 | 设置当前操作块是否显示删除图标，当显示删除图标时，点击删除图标会触发close事件。 true表示显示删除图标，false表示不显示删除图标。默认为false。 |
| icon | string | 否 | 操作块删除图标的url，支持本地路径。 |
 
 
  

#### 样式

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

支持[通用样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-styles)。
 
> [!NOTE]
> 文本和图片默认在整个piece组件中居中。

 
  

#### 事件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

除支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-events)外，还支持如下事件：
  
| 名称 | 参数 | 描述 |
| --- | --- | --- |
| close | - | 当piece组件点击删除图标触发，此时可以通过渲染属性if删除该组件。 |
 
 
  

#### 方法

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

支持[通用方法](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-methods)。
 
  

#### 示例

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
<!-- xxx.hml-->
<div class="container" >
  <piece if="{{first}}" content="example"></piece>
  <piece if="{{second}}" content="example" closable="true" onclose="closeSecond"></piece>
</div>
```
 
```text
/* xxx.css */
.container {
  width: 100%;
  height: 100%;
  align-items: center;
  justify-content: center;
}
```
 
```text
// xxx.js
export default {
  data: {
    first: true,
    second: true
  },
  closeSecond(e) {
    this.second = false;
  }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/Y1cCUVJpRpqPsnclqDWnfw/zh-cn_image_0000002581276420.gif?HW-CC-KV=V1&HW-CC-Date=20260528T025436Z&HW-CC-Expire=86400&HW-CC-Sign=318EC4341FE88ECB2F42BA8EE34667F30C1F870BDA872A31CEF4E2FAF40B49FE)
