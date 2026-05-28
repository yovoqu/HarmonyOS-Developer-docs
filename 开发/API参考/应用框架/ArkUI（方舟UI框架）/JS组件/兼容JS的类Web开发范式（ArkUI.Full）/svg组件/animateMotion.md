# animateMotion

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animatemotion
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

> [!NOTE]
> 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

 
路径动效。
  

##### 权限列表

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

无
 
  

##### 子组件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

不支持。
 
  

##### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

支持animate属性（values不生效）和以下表格中的属性。
  
| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| keyPoints | string | - | 是 | 一组关键帧的点位置，每帧的值为对象沿路径的距离比例。功能与animate属性中的values相同。 |
| path | string | - | 是 | 定义运动的路径，使用与path组件d属性相同的语法。 |
| rotate | [auto \| auto-reverse \| &lt;number&gt;] | auto | 否 | 设置动画对象的旋转方向。 |
