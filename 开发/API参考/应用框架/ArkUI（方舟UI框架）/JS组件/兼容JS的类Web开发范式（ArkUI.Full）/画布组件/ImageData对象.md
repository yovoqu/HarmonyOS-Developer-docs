# ImageData对象

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-imagedata
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

> [!NOTE]
> 从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

 
ImageData对象可以存储[canvas组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-canvas)渲染的像素数据。
  

##### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 属性 | 类型 | 描述 |
| --- | --- | --- |
| width | number | 矩形区域实际像素宽度。 |
| height | number | 矩形区域实际像素高度。 |
| data | &lt;Uint8ClampedArray&gt; | 一维数组，保存了相应的颜色数据，数据值范围为0到255。 |
 
 
  

##### 示例

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
</div>
```
 
```text
// xxx.js
import promptAction from '@ohos.promptAction';
export default {
  onShow() {
    const el =this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.fillRect(0,0,200,200);
    var imageData = ctx.createImageData(1,1);
    promptAction.showToast({
      message:imageData,
      duration:5000
    })
  }
}
```
