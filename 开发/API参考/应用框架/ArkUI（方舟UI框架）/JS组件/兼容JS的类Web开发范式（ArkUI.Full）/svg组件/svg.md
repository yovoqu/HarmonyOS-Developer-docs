# svg

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

基础容器，主要作为svg的根节点使用，也可以在svg中嵌套使用。
 
> [!NOTE]
> 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。 svg父组件或者svg组件需要定义宽高值，否则不进行绘制。

  

##### 权限列表

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

无
 
  

##### 子组件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

支持[svg](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg)、[rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-rect)、[circle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-circle)、[ellipse](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-ellipse)、[path](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-path)、[line](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-line)、[polygon](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-polygon)、[polyline](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-polyline)、[text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-text)、[animate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animate)、[animateTransform](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animatetransform)。
 
  

##### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

支持svg组件[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-common-attributes)和以下属性，设置的通用属性会传递给子组件。
  
| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| id | string | - | 否 | 组件的唯一标识。 |
| width | &lt;length&gt;\|&lt;percentage&gt; | - | 否 | 设置组件的宽度。 |
| height | &lt;length&gt;\|&lt;percentage&gt; | - | 否 | 设置组件的高度。 |
| x | &lt;length&gt;\|&lt;percentage&gt; | - | 否 | 设置当前svg的x轴坐标，根svg节点无效。 |
| y | &lt;length&gt;\|&lt;percentage&gt; | - | 否 | 设置当前svg的y轴坐标，根svg节点无效。 |
| viewBox | string | - | 否 | 设置当前svg的视口。支持的格式为<number number number number>，4个参数分别表示min-x, min-y, width and height，viewBox的宽高和svg的宽高不一致，会以中心对齐进行缩放。 |
 
 
  

##### 示例

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
<!-- xxx.hml -->
<div class="container">
  <svg width="400" height="400">
    <svg width="200" height="200" viewBox="0 0 100 100">
      <rect x="10" y="10" width="80" height="80" fill="#00FF00"></rect>
    </svg>
    <rect x="10" y="10" width="80" height="80" fill="red" ></rect>
    <svg x="0" y="0" width="200" height="200" viewBox="0 0 200 200">
      <rect x="10" y="10" width="80" height="80" fill="red"></rect>
    </svg>
    <svg x="0" y="0" width="200" height="200" viewBox="0 0 400 400">
      <rect x="10" y="10" width="80" height="80" fill="blue"></rect>
    </svg>
  </svg>
</div>
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/d_BWJnOSTSekzRqZ0T6wCw/zh-cn_image_0000002581436380.png?HW-CC-KV=V1&HW-CC-Date=20260528T024106Z&HW-CC-Expire=86400&HW-CC-Sign=8280A9CFCB28BE261B3C611DE3107D3EDAEFED77A05F7650464E5BDD22652ED4)
