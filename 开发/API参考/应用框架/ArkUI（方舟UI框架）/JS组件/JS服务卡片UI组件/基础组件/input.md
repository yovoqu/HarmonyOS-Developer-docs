# input

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-basic-input
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

交互式组件，提供单选框功能。
 
> [!NOTE]
> 从API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

  

#### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-attributes)外，还支持如下属性：
  
| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| type | string | radio | 是 | input组件类型，当前仅支持radio类型： - "radio"：定义单选按钮，允许在多个拥有相同name值的选项中选中其中一个。 |
| checked | boolean | false | 否 | 当前组件是否选中，true表示选中，false表示未选中。 |
| name | string | - | 否 | input组件的名称。 |
| value | string | - | 否 | input组件的value值，类型为radio时必填且相同name值的选项该值唯一。 |
 
 
  

#### 样式

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

支持[通用样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-styles)。
 
  

#### 事件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | $event.checkedItem | radio单选框的checked状态发生变化时触发该事件，返回选中的组件value值。 |
| click | - | 点击动作触发该事件。 |
 
 
  

#### 示例

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
<!-- xxx.hml -->
<div class="content">
  <input type="radio" checked='true' name="radioSample" value="radio1" onchange="onRadioChange"></input>
  <input type="radio" checked='false' name="radioSample" value="radio2" onchange="onRadioChange"></input>
  <input type="radio" checked='false' name="radioSample" value="radio3" onchange="onRadioChange"></input>
</div>
```
 
```text
/* xxx.css */
.content{
  width: 100%;
  height: 200px;
  justify-content: center;
  align-items: center;
}
```
 
```json
{
  "actions": {
    "onRadioChange":{
      "action": "message",
      "params": {
        "checkedRadio": "$event.checkedItem"
      }
    }
  }
}
```
 
**4*4卡片**
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/YlfC4OL_SleuIXNDVouwuQ/zh-cn_image_0000002611756513.gif?HW-CC-KV=V1&HW-CC-Date=20260528T025429Z&HW-CC-Expire=86400&HW-CC-Sign=93401FB480BB8AE035A6D490A7971D5C5A453515A46D484B05CE0B08F9EA6577)
