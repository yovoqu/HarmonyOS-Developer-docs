# richtext

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-richtext
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


富文本组件，用于展示富文本信息。


## 权限列表
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

无


## 属性
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

仅支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-attributes)中的id、style和class属性。


## 样式
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

仅支持[通用样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-styles)中的display和visibility样式。


## 事件
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

除支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-events)外，还支持如下事件：


| 名称 | 参数 | 描述 |
| --- | --- | --- |
| start | - | 开始加载时触发。 |
| complete | - | 加载完成时触发。 |


## 方法
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

不支持。


## 示例
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
<!-- xxx.hml -->
<div style="flex-direction: column;width: 100%;">
<richtext @start="onLoadStart" @complete="onLoadEnd">{{content}}</richtext>
</div>
```


```text
// xxx.js
export default {
data: {
content: `
<div class="flex-direction: column; background-color: #ffffff; padding: 30px; margin-bottom: 30px;">
<style>h1{color: yellow;}</style>
<p class="item-title">h1</p>
<h1>文本测试(h1测试)</h1>
<p class="item-title">h2</p>
<h2>文本测试(h2测试)</h2>
</div>
`,
},
onLoadStart() {
console.error("start load rich text")
},
onLoadEnd() {
console.error("end load rich text")
}
}
```
