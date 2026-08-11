# 如何取消Swiper指示器的默认边距

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1598

#### 问题现象

使用Swiper组件的DotIndicator构建导航指示器，并将导航点底部相对于Swiper的位置属性bottom设置为0，该指示器无法完全贴底，具体演示如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/gY1_0Kd0S9SCwibdxzO7HQ/zh-cn_image_0000002628613328.png?HW-CC-KV=V1&HW-CC-Date=20260811T005805Z&HW-CC-Expire=86400&HW-CC-Sign=E9FFBC1466E5DF6E0B94F220083C24086EB608F26844FFA1D8332E2E822B5C8C)

 
上下左右存在留白，如何实现可以去除内边距的导航指示器效果？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/sRlkmNzxS1qFXPhPJ1mItg/zh-cn_image_0000002658972541.gif?HW-CC-KV=V1&HW-CC-Date=20260811T005805Z&HW-CC-Expire=86400&HW-CC-Sign=D38DF628CAE7A3F86D739B6E5BB71A70C107DC6137A2CBC11D04A541A79BDB3F)

 
 

#### 背景知识

- [DotIndicator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#dotindicator10)构造圆点指示器的样式，继承自API10中[Indicator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#indicator10)。由于导航点有默认交互区域，交互区域高度为32vp，所以无法让显示部分完全贴底。在API19中提供了新的[bottom](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#bottom19)接口，可以忽略指示器的默认高度实现去除内边距的效果。
- 在API15中将Swiper中的指示器单独分割，新增了导航与切换组件[Indicator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-swiper-components-indicator)，同时也在Swiper内新增了API15的[indicator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#indicator15)属性，可以实现Indicator组件绑定Swiper内的Indicator属性，也可以单独使用Indicator组件。
- [Stack](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-stack-layout)是HarmonyOS提供的一种堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。

 
 

#### 解决方案

- **方案一：采用API19的bottom接口。**通过bottom接口，可以实现指示器与底部间距为0。实现方式详见：[示例9](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#示例9演示导航点space与bottom)。
- **方案二：自定义Indicator。**当前DotIndicator的规格固定存在内边距，无法满足问题需求。可以通过以下步骤实现无内边距的导航指示器效果：

1. 在Stack组件中创建Swiper轮播组件与导航点Column组件。
2. 使用[LazyForEach](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-rendering-control-lazyforeach)循环渲染Column组件，并设置合适的高度和外边距，例如在Stack组件内设置[alignContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-stack#aligncontent)参数为[Alignment](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#alignment).Bottom，表示底部对齐，也可以采用[位置设置](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-location)的方式，直接指定指示器位置。
3. 将index的值与currentIndex作比较，当两者相同时，改变Column的宽度与颜色，以此实现导航点效果。
 
具体参考代码如下所示：
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">SwiperExample </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">swiperController</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">SwiperController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">SwiperController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">arr</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">'1'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'2'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'3'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'4'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'5'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'6'</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">currentIndex</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">5 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">alignContent</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Alignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bottom </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Swiper</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">swiperController</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">ForEach</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">arr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'90%'</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">200</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(0xAFEEEE)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textAlign</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">TextAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">30</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">item</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">cachedCount</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">indicator</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">currentIndex </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

        <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">ForEach</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">arr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">()</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">currentIndex </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">index </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(255,0,0);">15 </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">5</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">5</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">5</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">currentIndex </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">index </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Gray </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">White</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">item</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
 
方案二运行效果图如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/LEYIs8L2Q9WSGFE-0abQtA/zh-cn_image_0000002658852587.png?HW-CC-KV=V1&HW-CC-Date=20260811T005805Z&HW-CC-Expire=86400&HW-CC-Sign=AB8B2F1ADF7E13D8ECA0D248A5085FBD61DE8C1FBC176A10C5215A49DDFE9650)

 
- **方案三：采用API15中Indicator组件。**Indicator组件采用的依旧是Swiper中的默认指示器样式，一样有32vp的交互高度限制，不过该组件将Swiper与指示器单独分割，可以通过Column组件单独封装指示器，再通过clip属性裁剪，控制Indicator组件高度，其它的与方案二类似采用Stack组件封装。

  具体参考代码如下所示：

  
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">DotIndicatorDemo </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">indicatorController</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">IndicatorComponentController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">IndicatorComponentController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">swiperController</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">SwiperController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">SwiperController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">list</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">'1'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'2'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'3'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'4'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'5'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'6'</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">alignContent</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Alignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bottom </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Swiper</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">swiperController</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">ForEach</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">list</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'90%'</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">200</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(0xAFEEEE)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textAlign</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">TextAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">30</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">item</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">cachedCount</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">indicator</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">indicatorController</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">IndicatorComponent</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">indicatorController</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">style</span><span style="color: rgb(0,0,255);">(</span>
            new <span style="color: rgb(0,0,255);">DotIndicator</span><span style="color: rgb(0,0,255);">()</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">itemWidth</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">10</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">itemHeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">10</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectedItemWidth</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectedItemHeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">10</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">color</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">White</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectedColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Gray</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(0,0,255);">          )</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">25</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">clip</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 方案三运行效果图如下：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/x2em69MFQGSUELXeUw1X2w/zh-cn_image_0000002628773228.png?HW-CC-KV=V1&HW-CC-Date=20260811T005805Z&HW-CC-Expire=86400&HW-CC-Sign=9ED201A7D3D09B4497B7CBBCEFCE2BF5A0D151D6AD01CBA7F99B6B6C3B3AD6B2)


 
> [!NOTE]
> 若方案三指示器背景为透明，不使用clip裁剪也可。同时若背景颜色为透明，也可采用margin属性，设置底部为负值达成类似消除内边距的效果。

 
 

#### 常见FAQ

Q：如何实现Swiper指示器居左下角显示？
 
A：可以直接方案二采用位置设置的方式对自定义指示器位置进行定位，或采用自带指示器通过方案一，方案三消除内边距再进行左下角对齐。
 
Q：如何修改Swiper指示器自带样式圆点的颜色？
 
A：DotIndicator中.color设置未选中的圆点颜色，.selectedColor属性设置选中的圆点颜色。
 
Q：如何实现Swiper指示器显示在Swiper外侧？
 
A：方案二、方案三去掉Stack层叠组件替换为Column组件，默认从上往下排列即可。
 
 

#### 总结
 
| 方案 | 位置 | 样式 | 简易程度 |
| --- | --- | --- | --- |
| 方案一 | Swiper内部 | 自带默认样式。 | 简单。 |
| 方案二 | 任意位置 | 多种自定义样式。 | 根据自定义样式的复杂程度攀升。 |
| 方案三 | 任意位置 | 自带默认样式基础上可以增加指示器背景颜色等通用属性（在绑定Swiper组件的情况下height/width等部分通用属性及自身部分属性暂不生效）。 | 一般。 |
