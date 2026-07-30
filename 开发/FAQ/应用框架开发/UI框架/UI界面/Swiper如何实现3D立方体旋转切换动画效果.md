# Swiper如何实现3D立方体旋转切换动画效果

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-919

#### 问题现象

通常Swiper组件，提供平面滑动轮播显示的效果，如何通过Swiper组件实现对子组件3D立方体旋转切换动画效果？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/97ClRHuASkWB4B2kH_GkUQ/zh-cn_image_0000002628400290.gif?HW-CC-KV=V1&HW-CC-Date=20260701T041143Z&HW-CC-Expire=86400&HW-CC-Sign=0E8A6FD2AE27CC28051A8392EF6429AE599DFB07E5C2087C759A4A70685992AC)

 
 

#### 背景知识

- [Swiper组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper)：滑块视图容器组件，它提供了子组件滑动轮播显示的能力。
- [customContentTransition属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#customcontenttransition12)：用于实现自定义的过渡动画效果，该属性允许开发者通过回调函数动态控制轮播切换过程中的动画细节，特别是可结合进度参数进行精细化动画控制。
- [rotate属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-transformation#rotate)：主要用于设置组件的旋转，可使组件在以组件左上角为坐标原点的坐标系中进行旋转。其中，（x，y，z）指定一个矢量，作为旋转轴。旋转轴和旋转中心点都基于坐标系设定，组件发生位移时，坐标系不会随之移动。默认值：在x、y、z都不指定时，x、y、z的默认值分别为0、0、1。指定了x、y、z任何一个值时，x、y、z中未指定的值默认为0。

 
 

#### 解决方案
1. 给Swiper组件内的子组件设置旋转属性rotate。
```text
Stack() {
  this.swiperItemSlotParam(item);
}
<em>// </em><em>设置组件旋转</em>
.rotate({
  x: 0,
  y: 1,
  z: 0,
  angle: this.angleList[index],
  centerX: this.centerXList[index],
  centerY: '50%',
  centerZ: 0,
  perspective: 0
});
```

2. 给Swiper组件设置页面切换动画属性customContentTransition，在页面切换时逐帧触发回调，在回调中设置子组件的rotate属性值。
```text
<em>// </em><em>自定义Swiper页面切换动画</em>
.customContentTransition({
 <em> // 页面移除视窗时超时1000ms下渲染树</em>
  timeout: 1000,
  transition: (proxy: SwiperContentTransitionProxy) => {
   <em> // 旋转角度</em>
    let angle = 0;
    console.info('proxy.position===>' + proxy.position);
    console.info('proxy.index===>' + proxy.index);
   <em> // position为index页面相对于selectedIndex对应页面的起始位置的移动比例，向左移动减小，向右移动增加。</em>
    if (proxy.position < 0 && proxy.position > -1) {
     <em> // 当前页向左滑出或上一页向右滑入</em>
      angle = proxy.position * 90;
   <em>   // 设置index页面的旋转中心轴为右侧边缘</em>
      this.centerXList[proxy.index] = '100%';
    } else if (proxy.position > 0 && proxy.position < 1) {
    <em>  // 当前页向右滑出或下一页向左滑入</em>
      angle = proxy.position * 90;
     <em> // 设置index页面的旋转中心轴为左侧边缘</em>
      this.centerXList[proxy.index] = '0%';
    } else {
   <em>   // position小于-1时表示向左完全滑出区域，大于1时表示向右完全滑出区域，重置角度</em>
      angle = 0;
    }
  <em>  // 修改index页的旋转角</em>
    this.angleList[proxy.index] = angle;
  }
});
```

 
完整示例参考如下：
 
```json
@Component
@Entry
export struct Swiper3D {
 <em> // Swiper数据</em>
  private swiperList: MySwiperItem[] =
    [new MySwiperItem('模块1', '#4B48F7'),
      new MySwiperItem('模块2', '#46B1E3'),
      new MySwiperItem('模块3', '#61CFBE')]
  ;

  build() {
    Column() {
     <em> // 轮播网格</em>
      Custom3DComponentPage({
        items: this.swiperList,
        swiperItemSlotParam: (item: MySwiperItem) => {
          this.mySwiperItem(item);
        }
      });
    };
  }

 <em> // 自定义3D立方体旋转轮播项UI内容</em>
  @Builder
  mySwiperItem(item: MySwiperItem) {
    Column() {
      Text(item.title).fontSize(24);
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
    .backgroundColor(item.colors);
  }
}

export class MySwiperItem {
 <em> // 标题</em>
  title: string;
 <em> // 颜色</em>
  colors: Color | string;

  constructor(title: string, colors: Color | string) {
    this.title = title;
    this.colors = colors;
  }
}

@Component
export struct Custom3DComponentPage {
  <em>// --------------------暴露外部属性----------------------------</em>
<em>  // 动画持续时间，默认500ms</em>
  duration: number = 500;
 <em> // 是否自动播放</em>
  autoPlay: boolean = false;
 <em> // 是否循环播放</em>
  loop: boolean = true;
 <em> // 轮播数据</em>
  items: ESObject[] = [];
 <em> // 轮播页插槽参数</em>
  @BuilderParam swiperItemSlotParam: (item: ESObject) => void;
 <em> // --------------------私有属性----------------------------</em>
<em>  // 当前项下标</em>
  @State currentIndex: number = 0;
  <em>// </em><em>旋转角度列表</em>
  @State angleList: number[] = [];
  <em>// 旋转中心点列表</em>
  @State centerXList: Array<number | string> = [];
  <em>// 轮播控制器</em>
  private swiperController: SwiperController = new SwiperController();

  build() {
    Swiper(this.swiperController) {
      ForEach(this.items, (item: ESObject, index: number) => {
        Stack() {
          this.swiperItemSlotParam(item);
        }
       <em> // 设置组件旋转</em>
        .rotate({
          x: 0,
          y: 1,
          z: 0,
          angle: this.angleList[index],
          centerX: this.centerXList[index],
          centerY: '50%',
          centerZ: 0,
          perspective: 0
        });

      }, ((item: ESObject, index: number) => `${JSON.stringify(item)}_${index}`));
    }
    .loop(this.loop)
    .autoPlay(this.autoPlay)
    .duration(this.duration)
    .onChange((index: number) => {
      this.currentIndex = index;
    })
   <em> // 自定义Swiper页面切换动画</em>
    .customContentTransition({
      <em>// 页面移除视窗时超时1000ms下渲染树</em>
      timeout: 1000,
      transition: (proxy: SwiperContentTransitionProxy) => {
    <em>    // 旋转角度</em>
        let angle = 0;
        console.info('proxy.position===>' + proxy.position);
        console.info('proxy.index===>' + proxy.index);
       <em> // position为index页面相对于selectedIndex对应页面的起始位置的移动比例，向左移动减小，向右移动增加。</em>
        if (proxy.position < 0 && proxy.position > -1) {
          <em>// </em><em>当前页向左滑出或上一页向右滑入</em>
          angle = proxy.position * 90;
        <em>  // 设置index页面的旋转中心轴为右侧边缘</em>
          this.centerXList[proxy.index] = '100%';
        } else if (proxy.position > 0 && proxy.position < 1) {
       <em>   // 当前页向右滑出或下一页向左滑入</em>
          angle = proxy.position * 90;
        <em>  // 设置index页面的旋转中心轴为左侧边缘</em>
          this.centerXList[proxy.index] = '0%';
        } else {
       <em>   // position小于-1时表示向左完全滑出区域，大于1时表示向右完全滑出区域，重置角度</em>
          angle = 0;
        }
       <em> // 修改index页的旋转角</em>
        this.angleList[proxy.index] = angle;
      }
    });
  }
}
```
