# slider

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-slider
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

> [!NOTE]
> 从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

 
滑动条组件，用来快速调节设置值，如音量、亮度等。
  

##### 子组件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

不支持。
 
  

##### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-attributes)外，还支持以下属性：
  
| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| min | number | 0 | 否 | 滑动选择器的最小值。 |
| max | number | 100 | 否 | 滑动选择器的最大值。 |
| step | number | 1 | 否 | 每次滑动的步长。 |
| value | number | 0 | 否 | 滑动选择器的初始值。 |
| mode5+ | string | outset | 否 | 滑动条样式： - outset：滑块在滑杆上； - inset：滑块在滑杆内。 |
| showsteps5+ | boolean | false | 否 | 是否显示步长标识。true表示显示步长标识，false表示不显示步长标识。 |
| showtips5+ | boolean | false | 否 | 滑动时是否有气泡提示百分比。true表示有气泡提示百分比，false表示没有气泡提示百分比。 |
 
 
  

##### 样式

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

除支持[通用样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-styles)外，还支持如下样式：
  
| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| color | &lt;color&gt; | #19000000 | 否 | 滑动条的背景颜色。 |
| selected-color | &lt;color&gt; | #ff007dff | 否 | 滑动条的已选择颜色。 |
| block-color | &lt;color&gt; | #ffffff | 否 | 滑动条的滑块颜色。 |
 
 
  

##### 事件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

除支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-events)外，还支持如下事件：
  
| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | ChangeEvent | 选择值发生变化时触发该事件。 |
 
 
**表1** ChangeEvent
  
| 属性 | 类型 | 说明 |
| --- | --- | --- |
| value5+ | number | 当前slider的进度值。 |
| mode5+ | string | 当前change事件的类型，可选值为： - start：slider的值开始改变。 - move：slider的值跟随手指拖动中。 - end：slider的值结束改变。 - click：slider的值在点击进度条后改变。 |
 
 
  

##### 示例

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
<!-- xxx.hml -->
<div class="container">
    <slider min="0" max="100" value="{{ value }}" mode="outset" showtips="true"></slider>
    <slider class="slider" min="0" max="100" value="{{ value }}" step="20" mode="inset"  showtips="true"></slider>
    <slider class="slider" min="0" max="100" value="{{ value }}" showsteps="true" step="20" mode="inset"  showtips="false"></slider>
</div>
```
 
```text
/* xxx.css */
.container {
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.slider{
    margin-top: 100px;
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/X46Fyh7zQrec3mMGWQ9UTQ/zh-cn_image_0000002581436340.png?HW-CC-KV=V1&HW-CC-Date=20260528T024103Z&HW-CC-Expire=86400&HW-CC-Sign=586C090A1DD3F37F9B18787D5F0DD4AE27B5375F2B318490CA09B11D13DF4A32)
