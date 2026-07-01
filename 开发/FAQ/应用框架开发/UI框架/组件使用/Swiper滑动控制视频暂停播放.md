# Swiper滑动控制视频暂停播放

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-755

#### 问题现象

Swiper里嵌套不同的视频，滑动Swiper时（比如从第一个Item滑动到第二个Item），如何让之前的Item暂停视频播放？
 
 

#### 背景知识

- [Video](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-media-components-video)组件视频播放后默认不会自动暂停，而是会继续播放，只有通过[VideoController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-media-components-video#videocontroller)的[pause](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-media-components-video#pause)方法可以暂停播放。另外还可以通过VideoController的[stop](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-media-components-video#stop)方法控制视频重新播放。
- [Swiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper)组件滑动时默认不会触发VideoController的pause方法，但是Swiper滑动时会触发[onChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#onchange)事件。

 
 

#### 解决方案

Swiper滑动时触发onChange事件，在onChange方法里调用VideoController的pause方法即可实现滑动过程控制视频暂停播放。
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">demoExample </span><span style="color: rgb(181,106,1);">{</span>
  private <span style="color: rgb(255,255,255);">controllerList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">VideoController</span><span style="color: rgb(255,0,170);">[] </span><span style="color: rgb(181,106,1);">=</span>
    <span style="color: rgb(255,0,170);">[</span>new <span style="color: rgb(0,0,255);">VideoController</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">, </span>new <span style="color: rgb(0,0,255);">VideoController</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">, </span>new <span style="color: rgb(0,0,255);">VideoController</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">, </span>new <span style="color: rgb(0,0,255);">VideoController</span><span style="color: rgb(255,0,170);">()]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">swiperIndex</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Swiper</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">ForEach</span><span style="color: rgb(255,0,170);">([</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">2</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">3</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(132,63,161);">第 </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">item </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">} </span><span style="color: rgb(132,63,161);">个组件页</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">White</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textAlign</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">TextAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">20</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">Video</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
          <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">此处</span><span style="color: rgb(128,128,128);">'www.xxx.com/yyy.mp4'</span><span style="color: rgb(128,128,128);">仅作为示例</span></em>
            <span style="color: rgb(255,255,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'www.xxx.com/yyy.mp4'</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controllerList</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(255,0,170);">]</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">objectFit</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">ImageFit</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Contain</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controls</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">autoPlay</span><span style="color: rgb(255,0,170);">(</span>false<span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loop</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">200</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loop</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Black</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onChange</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      const <span style="color: rgb(255,255,255);">preIndex </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">index </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(80,160,79);">0 </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(255,255,255);">index </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(80,160,79);">1 </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">3</span><span style="color: rgb(181,106,1);">;</span>
      const <span style="color: rgb(255,255,255);">nextIndex </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">index </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(80,160,79);">3 </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(255,255,255);">index </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(80,160,79);">1 </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controllerList</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(255,255,255);">preIndex</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pause</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controllerList</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(255,255,255);">nextIndex</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pause</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">swiperIndex </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
 

#### 常见FAQ

Q：如果要视频切回来之后重新播放，应该如何设置？
 
A：只需将上述样例代码中onChange方法里调用的pause()方法换成stop()即可。
 
> [!NOTE]
> 这里切回来之后显示的还是暂停时的那一帧内容，在点击播放时会重新播放。

 
Q：如果Video组件设置了预览图和视频路径，如何在视频播放暂停时如何由当前帧重置到预览图？
 
A：可使用Stack堆叠Image和Video，通过状态控制Image的显示/隐藏，实现暂停时展示预览图、播放时隐藏的效果。
