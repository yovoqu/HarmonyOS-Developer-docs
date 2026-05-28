# rect

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-rect
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

> [!NOTE]
> 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

 
用于绘制矩形、圆角矩形。
  

##### 权限列表

无
 
  

##### 子组件

支持[animate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animate)、[animateMotion](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animatemotion)、[animateTransform](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animatetransform)。
 
  

##### 属性

支持Svg组件[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-common-attributes)和以下属性。
  
| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| id | string | - | 否 | 组件的唯一标识。 |
| width | &lt;length&gt;\|&lt;percentage&gt; | 0 | 否 | 设置矩形的宽度。支持属性动画。 |
| height | &lt;length&gt;\|&lt;percentage&gt; | 0 | 否 | 设置矩形的高度。支持属性动画。 |
| x | &lt;length&gt;\|&lt;percentage&gt; | 0 | 否 | 设置矩形左上角x轴坐标。支持属性动画。 |
| y | &lt;length&gt;\|&lt;percentage&gt; | 0 | 否 | 设置矩形左上角y轴坐标。支持属性动画。 |
| rx | &lt;length&gt;\|&lt;percentage&gt; | 0 | 否 | 设置矩形圆角x方向半径。支持属性动画。 |
| ry | &lt;length&gt;\|&lt;percentage&gt; | 0 | 否 | 设置矩形圆角y方向半径。支持属性动画。 |
 
 
  

##### 示例

```text
<!-- xxx.hml -->
<div class="container">
  <svg fill="white" width="400" height="400">
    <rect width="100" height="100" x="10" y="20" stroke-width="4" stroke="blue" id="rectId"></rect>
    <rect width="100" height="100" x="150" y="20" stroke-width="4" stroke="blue" rx="10" ry="10"></rect>
    <rect width="100" height="100" x="10" y="130" stroke-width="10" fill="red" stroke="blue" rx="10" ry="10"></rect>
    <rect width="100" height="100" x="150" y="130" stroke-width="10" stroke="red" rx="10" ry="10" stroke-dasharray="5 3" stroke-dashoffset="3"></rect>
    <rect width="100" height="100" x="20" y="270" stroke-width="4" stroke="blue" transform="rotate(-10)"></rect>
  </svg>
</div>
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/X9PZ-r9lSCO8RVIZXRdsdg/zh-cn_image_0000002611836211.png?HW-CC-KV=V1&HW-CC-Date=20260528T013810Z&HW-CC-Expire=86400&HW-CC-Sign=B85DD61F89D9E74694DEB801D1CB46921869D20457BD36E90E9FB32CBF16762B)
