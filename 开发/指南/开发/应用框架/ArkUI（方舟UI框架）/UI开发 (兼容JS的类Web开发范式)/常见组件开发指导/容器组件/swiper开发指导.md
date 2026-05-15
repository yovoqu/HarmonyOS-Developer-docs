# swiper开发指导

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-swiper

swiper为滑动容器，提供切换显示子组件的能力。具体用法请参考[swiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-swiper)。


## 创建swiper组件

在pages/index目录下的hml文件中创建一个swiper组件。
```text


      item1


      item2


      item3


```


```text
/* xxx.css */
.container{
  width: 100%;
  height: 100%;
  flex-direction: column;
  background-color: #F1F3F5;
  align-items: center;
  justify-content: center;
  width: 100%;
}
swiper{
  height: 30%;
}
.item{
  width: 100%;
  height: 500px;
}
text{
  width: 100%;
  height: 100%;
  text-align: center;
  font-size: 50px;
  color: white;
}
```

![](assets/swiper开发指导/file-20260514130746556-0.gif)
> [!NOTE]
> swiper组件支持除之外的子组件。


## 添加属性

在swiper组件不开启循环播放（loop="false"）时添加自动播放属性（autoplay），设置自动播放时播放时间间隔（interval），页面会自动切换并停留在最后一个子组件页面。添加digital属性启用数字导航点，设置切换时为渐隐滑动效果（scrolleffect="fade"）。
```text


      item1


      item2


      item3


      item4


```


```text
/* xxx.css */
.container{
  width: 100%;
  height: 100%;
  flex-direction: column;
  background-color: #F1F3F5;
  align-items: center;
  justify-content: center;
}
swiper{
  height: 30%;
}
.item{
  width: 100%;
  height: 500px;
}
text{
  width: 100%;
  height: 100%;
  text-align: center;
  font-size: 50px;
  color: white;
}
```

![](assets/swiper开发指导/file-20260514130746556-1.gif)
> [!NOTE]
> 设置indicator（是否启用导航点指示器）属性为true时digital（是否启用数字导航点）属性才会生效。 swiper子组件的个数大于等于2时设置的loop属性才会生效。 scrolleffect属性仅在loop属性值为false时生效。


## 设置样式

设置swiper组件的宽高，导航点指示器的直径大小（indicator-size）、颜色（indicator-color）、相对位置（indicator-top）及选中时的颜色（indicator-selected-color）。
```text


            item1


            item2


            item3


```


```text
/* xxx.css */
.container{
  width: 100%;
  height: 100%;
  flex-direction: column;
  background-color: #F1F3F5;
  align-items: center;
  justify-content: center;
}
swiper{
  width:  500px;
  height: 500px;
  border-radius: 250px;
  indicator-color: white;
  indicator-selected-color: blue;
  indicator-size: 40px;
  indicator-top: 100px;
  overflow: hidden ;
}
.item{
  width: 100%;
  height: 500px;
}
text{
  width: 100%;
  text-align: center;
  margin-top: 150px;
  font-size: 50px;
  color: white;
}
```

![](assets/swiper开发指导/file-20260514130746556-2.gif)

## 绑定事件

创建两个text组件添加点击事件，当点击后就调用showPrevious（显示上一个子组件）或showNext（显示下一个子组件）方法。添加select组件下拉选择时触发change事件后调用swipeTo方法跳转到指定轮播页面。swiper组件绑定change（当前显示的组件索引变化时触发）和finish（切换动画结束时触发）事件。
```text


      item1


      item2


      item3


      item4


      Previous

          swipeTo 1
          swipeTo 2
          swipeTo 3
          swipeTo 4

    Next


```


```text
/* xxx.css */
.container{
  width: 100%;
  height: 100%;
  flex-direction: column;
  background-color: #F1F3F5;
  align-items: center;
  justify-content: center;
}
swiper{
  height: 30%;
}
.item{
  width: 100%;
  height: 500px;
}
text{
  width: 100%;
  height: 100%;
  text-align: center;
  font-size: 50px;
  color: white;
}
select{
  background-color: white;
  width: 250px;
  height: 80px;
}
.content{
  margin-top: 100px;
  justify-content: space-around;
}
.pnbtn{
  width: 200px;
  height: 80px;
  font-size: 30px;
}
```


```text
// xxx.js
import promptAction from '@ohos.promptAction';
export default{
  change(e){
    promptAction.showToast({duration:2000,message:"current index:"+e.index});
  },
  finish(){
    promptAction.showToast({duration:2000,message:"切换动作结束"});
  },
  selectChange(e){
    this.$element('swiper').swipeTo({index: Number(e.newValue)});
  },
  previous(){
    this.$element('swiper').showPrevious();
  },
  next(){
    this.$element('swiper').showNext();
  }
}
```

![](assets/swiper开发指导/file-20260514130746556-3.gif)

## 场景示例

本场景中使用swiper创建一个轮播图，在轮播图底部制作一个缩略图，点击缩略图后调用swipeTo方法切换到对应的轮播图。
```text


```


```text
/* xxx.css */
.container{
  flex-direction: column;
  background-color: #F1F3F5;
  align-items: center;
  justify-content: center;
  width: 100%;
}
swiper{
  width: 100%;
  height: 500px;
}
.item{
  width: 100%;
  height: 500px;
}
.content{
  margin-top: -120px;
  width: 70%;
  display: flex;
  justify-content: space-around;
  height: 100px;
}
.content_item{
  padding: 5px;
  transform: scale(0.5);
}
.activated{
  transform: scale(1);
  border: 1px solid #b20937ea;
}
```


```text
// xxx.js
export default {
  data:{
    index: 0,
    list:[
      {src: 'common/images/1.png'},
      {src: 'common/images/2.png'},
      {src: 'common/images/3.png'},
      {src: 'common/images/4.png'},]
    },
  imageTo(index){
    this.index = index;
    this.$element('swiper').swipeTo({index: index});
  },
  change(e){
    this.index = e.index;
  }
}
```

![](assets/swiper开发指导/file-20260514130746556-4.gif)
