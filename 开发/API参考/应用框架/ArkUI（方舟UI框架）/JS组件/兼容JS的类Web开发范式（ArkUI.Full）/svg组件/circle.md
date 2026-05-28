# circle

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-circle
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

> [!NOTE]
> 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

 
圆形形状。
  

##### 权限列表

无
 
  

##### 子组件

支持[animate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animate)、[animateMotion](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animatemotion)、[animateTransform](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animatetransform)。
 
  

##### 属性

支持Svg组件[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-common-attributes)和以下属性。
  
| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| id | string | - | 否 | 组件的唯一标识。 |
| cx | &lt;length&gt;\|&lt;percentage&gt; | 0 | 否 | 设置圆心的x轴坐标。支持属性动画。 |
| cy | &lt;length&gt;\|&lt;percentage&gt; | 0 | 否 | 设置圆心的y轴坐标。支持属性动画。 |
| r | &lt;length&gt;\|&lt;percentage&gt; | 0 | 否 | 设置圆的半径。支持属性动画。 |
 
 
  

##### 示例

```text
<!-- xxx.hml -->
<div class="container">
  <svg fill="white" width="400" height="400">
    <circle cx="60" cy="200" r="50" stroke-width="4" fill="red" stroke="blue"></circle>
    <circle cx="180" cy="200" r="50" stroke-width="10" stroke="red" stroke-dasharray="10 5" stroke-dashoffset="3"></circle>
  </svg>
</div>
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/PLfAb_0xThKMTmdAWgF6dQ/zh-cn_image_0000002581276464.png?HW-CC-KV=V1&HW-CC-Date=20260528T013809Z&HW-CC-Expire=86400&HW-CC-Sign=F6FA59599800F9654B654C0E8665791827FA576AF62856F6FE3C956D7CFDA39D)
