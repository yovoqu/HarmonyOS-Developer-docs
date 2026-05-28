# select

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-select
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

下拉选择按钮，可使用下拉菜单展示并选择内容。
 
> [!NOTE]
> 从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

  

#### 子组件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

支持<[option](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-option)>。
 
  

#### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-attributes)。
 
  

#### 样式

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

除支持[通用样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-styles)外，还支持如下样式：
  
| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| font-family | string | 否 | 字体样式列表，用逗号分隔。列表中第一个系统中存在的字体样式或者通过自定义字体指定的字体样式，会被选中作为当前文本的字体样式。 默认值：sans-serif |
 
 
  

#### 事件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

除支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-events)外，还支持如下事件：
  
| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | {newValue: newValue} | 选择下拉选项后触发该事件，返回值为一个对象，其中newValue为选中项option的value值。 |
 
 
> [!NOTE]
> select组件不支持click事件。

 
  

#### 方法

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

支持[通用方法](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-methods)。
 
  

#### 示例

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
<!-- xxx.hml -->
<div class="container">
    <select>
        <option for="{{ array }}" value="{{ $item.value }}">
            {{ $item.name }}
        </option>
    </select>
</div>
```
 
```text
/* xxx.css */
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
}
```
 
```text
// xxx.js
export default {
    data: {
        array: [
            {
                "value": "下拉选项0", "name": "选项0"
            },
            {
                "value": "下拉选项1", "name": "选项1"
            },
            {
                "value": "下拉选项2", "name": "选项2"
            },
            {
                "value": "下拉选项3", "name": "选项3"
            },
        ]
    }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/2Juny6TQQlymA4y2algCng/zh-cn_image_0000002611756279.png?HW-CC-KV=V1&HW-CC-Date=20260528T025436Z&HW-CC-Expire=86400&HW-CC-Sign=4C7A28115E3C5C66C58ABCD9450C04F746A81BAA891ABCC0E7047CE82B765031)
