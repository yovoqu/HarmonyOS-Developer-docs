# image开发指导

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-images

image是图片组件，用来渲染展示图片。具体用法请参考[image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-image)组件。


## 创建image组件

在pages/index目录下的hml文件中创建一个image组件。
```text


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
```

![](assets/image开发指导/file-20260514130750000-0.png)

## 设置image样式

通过设置width、height和object-fit属性定义图片的宽、高和缩放样式。
```text


```


```text
/* xxx.css */
.container {
  width: 100%;
  height: 100%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color:#F1F3F5;
}
image{
  width: 80%;
  height: 500px;
  border: 5px solid saddlebrown;
  border-radius: 20px;
  object-fit: contain;
  match-text-direction:true;
}
```

![](assets/image开发指导/file-20260514130750000-1.png)

## 加载图片

图片成功加载时触发complete事件，返回加载的图源尺寸。加载失败则触发error事件，打印图片加载失败。
```text


```


```text
/* xxx.css */
.container{
  width: 100%;
  height: 100%;
  flex-direction: column;
  justify-content: center;
  align-self: center;
  background-color: #F1F3F5;
}
.container div{
  margin-left: 10%;
  width: 80%;
  height: 300px;
  margin-bottom: 40px;
}
```


```text
// index.js
import promptAction from '@ohos.promptAction';
export default {
  imageComplete(i,e){
    promptAction.showToast({
      message: "image "+i+"'s width"+ e.width+"----image "+i+"'s height"+e.height,
      duration: 3000,
    })
  },
  imageError(i,e){
    setTimeout(()=>{
      promptAction.showToast({
        message: "Failed to load image "+i+".",
        duration: 3000,
      })
    },3000)
  }
}
```

![](assets/image开发指导/file-20260514130750000-2.gif)

## 场景示例

在本场景中，开发者长按图片后将慢慢隐藏图片，当完全隐藏后再重新显示原始图片。定时器setInterval每隔一段时间改变图片透明度,实现慢慢隐藏的效果，当透明度为0时清除定时器，设置透明度为1。
```text


      Touch and hold the image


```


```text
/* xxx.css */
.page-container {
  width: 100%;
  height: 100%;
  flex-direction:column;
  align-self: center;
  justify-content: center;
  background-color:#F1F3F5;
  background-color: #F1F3F5;
}
.content{
  flex-direction:column;
}
.image-container {
  width: 100%;
  height: 300px;
  align-items: center;
  justify-content: center;
}
.text-container {
  margin-top:50px;
  width: 100%;
  height: 60px;
  flex-direction: row;
  justify-content: space-between;
}
.testimage {
  width: 100%;  height: 400px;
  object-fit: scale-down;
  border-radius: 20px;
}
```


```text
// index.js
import promptAction from '@ohos.promptAction';
export default {
  data: {
    testuri: 'common/images/bg-tv.jpg',
    imageopacity:1,
    timer: null
  },
  changeopacity: function () {
    promptAction.showToast({
      message: 'Touch and hold the image.'
    })
    var opval = this.imageopacity * 20
    clearInterval(this.timer);
    this.timer = setInterval(()=>{
      opval--;
      this.imageopacity = opval / 20
      if (opval===0) {
        clearInterval(this.timer)
        this.imageopacity = 1
      }
    },100);
  }
}
```

![](assets/image开发指导/file-20260514130750000-3.gif)
