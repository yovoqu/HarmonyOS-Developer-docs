# Image对象

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-image
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

> [!NOTE]
> 从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

 
图片对象。
  

##### 属性
 
| 属性 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| src | string | - | 是 | 图片资源的路径。 |
| width | &lt;length&gt; | 0px | 否 | 图片的宽度。 |
| height | &lt;length&gt; | 0px | 否 | 图片的高度。 |
| onload | Function | - | 否 | 图片加载成功后触发该事件，无参数。 |
| onerror | Function | - | 否 | 图片加载失败后触发该事件，无参数。 |
 
 
  

##### 示例

```text
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; "></canvas>
</div>
```
 
```text
// xxx.js
export default {
    onShow() {
        const el = this.$refs.canvas;
        var ctx = el.getContext('2d');
        var img = new Image();
        // 图片路径建议放在common目录下
        img.src = 'common/images/example.jpg';
        img.onload = function () {
            console.log('Image load success');
            ctx.drawImage(img, 0, 0, 360, 250);
        };
        img.onerror = function () {
            console.error('Image load fail');
        };
    }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/Gf957t1BSDyaG3gTHeUVvg/zh-cn_image_0000002611836201.png?HW-CC-KV=V1&HW-CC-Date=20260528T013803Z&HW-CC-Expire=86400&HW-CC-Sign=F7995C6E0C73E1BD17F2B23B874EE150091C2114C482AD8643A865AFC17ACD7E)
