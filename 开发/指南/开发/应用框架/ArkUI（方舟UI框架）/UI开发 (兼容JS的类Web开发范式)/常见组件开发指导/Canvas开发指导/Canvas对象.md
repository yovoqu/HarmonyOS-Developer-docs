# Canvas对象

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-canvas

Canvas组件提供画布，用于自定义绘制图形。具体用法请参考[CanvasRenderingContext2D对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-canvasrenderingcontext2d)。


##### 创建Canvas组件

在pages/index目录下的hml文件中创建一个Canvas组件。

```text
<!-- xxx.hml -->
<div class="container">
  <canvas></canvas>
</div>
```

```text
/* xxx.css */
.container {
    width: 100%;
    height: 100%;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: #F1F3F5;
}

canvas {
    background-color: #00ff73;
}
```


![](assets/Canvas对象/file-20260514130757521-0.png)


> [!NOTE]
> Canvas组件默认背景色与父组件的背景色一致。 Canvas默认宽高为width: 300px，height: 150px。




##### 添加样式

Canvas组件设置宽（width）、高（height）、背景色（background-color）及边框样式（border）。

```text
<!-- xxx.hml -->
<div class="container">
  <canvas></canvas>
</div>
```

```text
/* xxx.css */
.container {
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: #F1F3F5;
    width: 100%;
    height: 100%;
}

canvas {
    width: 500px;
    height: 500px;
    background-color: #fdfdfd;
    border: 5px solid red;
}
```


![](assets/Canvas对象/file-20260514130757521-2.gif)




##### 添加事件

Canvas添加长按事件，长按后可获取Canvas组件的dataUrl值（toDataURL方法返回的图片信息），打印在下方文本区域内。

> [!NOTE]
> promptAction相关接口参考 弹窗 。


```text
<!-- xxx.hml -->
<div class="container">
    <canvas ref="canvas1" onlongpress="getUrl"></canvas>
    <text>dataURL</text>
    <text class="content">{{ dataURL }}</text>
</div>
```

```text
/* xxx.css */
.container {
    width: 100%;
    height: 100%;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: #F1F3F5;
}

canvas {
    width: 500px;
    height: 500px;
    background-color: #fdfdfd;
    border: 5px solid red;
    margin-bottom: 50px;
}

.content {
    border: 5px solid blue;
    padding: 10px;
    width: 90%;
    height: 400px;
    overflow: scroll;
}
```

```text
// xxx.js
import promptAction from '@ohos.promptAction';

export default {
    data: {
        dataURL: null,
    },
    onShow() {
        let el = this.$refs.canvas1;
        let ctx = el.getContext("2d");
        ctx.strokeRect(100, 100, 300, 300);
    },
    getUrl() {
        let el = this.$refs.canvas1
        let dataUrl = el.toDataURL()
        this.dataURL = dataUrl;
        promptAction.showToast({ duration: 2000, message: "long press,get dataURL" })
    }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/giAoqG0ASSumE4X_KjxG6A/zh-cn_image_0000002611754135.gif?HW-CC-KV=V1&HW-CC-Date=20260528T014753Z&HW-CC-Expire=86400&HW-CC-Sign=D15C8D6DB7080AB6B52718F2D06DDFE6A39E4AA69F4A24A8747B8C313DCA5CD3)


> [!NOTE]
> 画布不支持在onInit和onReady中进行创建。
