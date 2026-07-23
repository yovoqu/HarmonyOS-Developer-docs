# router跳转时如何实现3D翻转动画效果

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1054

#### 问题现象

使用router跳转到其他页面时，如何实现自右向左的180度3D翻转的动画效果？
 
 

#### 背景知识

- [pageTransition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-page-transition-animation#pagetransitionenter)：当路由(router)进行切换时，可以通过在pageTransition函数中自定义页面入场和页面退场的转场动效。
- [rotate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-transformation#rotate)：可使组件在以组件左上角为坐标原点的坐标系中进行旋转。

 
 

#### 解决方案
1. 参照[禁用某页面的页面转场](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-page-transition-animation#禁用某页面的页面转场)以关闭路由跳转时的默认动画效果。
```text
pageTransition() {
  PageTransitionEnter({ type: RouteType.None, duration: 0 });
  PageTransitionExit({ type: RouteType.None, duration: 0 });
}
```

2. 在页面根节点绑定旋转属性以实现页面级视觉变换。
```text
.rotate({
  x: 0,
  y: 1,
  z: 0,
  angle: this.angle,
  centerX: '50%',
  centerY: '50%',
  centerZ: 0,
  perspective: 0
});
```

3. 通过帧动画实现旋转角度的连续变化效果。
```text
aboutToAppear(): void {
  this.result = this.getUIContext().createAnimator(this.options);
  this.result.onFrame = (value: number) => {
    this.angle = -value * 180;
  };
  this.result.onFinish = () => {
    this.getUIContext().getRouter().pushUrl({ url: 'pages/Index2' });
  };
}
```

 
完整代码参考如下：
 
```text
import { AnimatorOptions, AnimatorResult } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State angle: number = 1;
  @State result: AnimatorResult | undefined = undefined;
  private options: AnimatorOptions = {
    duration: 1200,
    easing: 'friction',
    delay: 0,
    fill: 'forwards',
    direction: 'normal',
    iterations: 1,
    begin: 0,
    end: 1
  };

  aboutToAppear(): void {
    this.result = this.getUIContext().createAnimator(this.options);
    this.result.onFrame = (value: number) => {
      this.angle = -value * 180;
    };
    this.result.onFinish = () => {
      this.getUIContext().getRouter().pushUrl({ url: 'pages/Index2' });
    };
  }


  build() {
    Stack() {
      Button('go to PageTwo')
        .onClick(() => {
          this.result?.play();
        });
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#f1f3f5')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
    .rotate({
      x: 0,
      y: 1,
      z: 0,
      angle: this.angle,
      centerX: '50%',
      centerY: '50%',
      centerZ: 0,
      perspective: 0
    });

  }

  pageTransition() {
    PageTransitionEnter({ type: RouteType.None, duration: 0 });
    PageTransitionExit({ type: RouteType.None, duration: 0 });
  }

}
```
 
```text
import { AnimatorOptions, AnimatorResult } from '@kit.ArkUI';

@Entry
@Component
struct Index2 {
  @State angle: number = 0;
  @State result: AnimatorResult | undefined = undefined;
  private options: AnimatorOptions = {
    duration: 1200,
    easing: 'friction',
    delay: 0,
    fill: 'forwards',
    direction: 'normal',
    iterations: 1,
    begin: 0,
    end: 1
  };

  aboutToAppear(): void {
    this.result = this.getUIContext().createAnimator(this.options);
    this.result.onFrame = (value: number) => {
      this.angle = value * 180;
    };
    this.result.onFinish = () => {
      this.getUIContext().getRouter().pushUrl({ url: 'pages/Index' });
    };
  }

  build() {
    Stack() {
      Button('PageTwo')
        .onClick(() => {
          this.result?.play();
        });
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#f1f3f5')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
    .rotate({
      x: 0,
      y: 1,
      z: 0,
      angle: this.angle,
      centerX: '50%',
      centerY: 0,
      centerZ: 0,
      perspective: 0
    });
  }

  pageTransition() {
    PageTransitionEnter({ type: RouteType.None, duration: 0 });
    PageTransitionExit({ type: RouteType.None, duration: 0 });
  }
}
```
 
实现效果如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/PHeFr6IjS5KewW9uR8s_LA/zh-cn_image_0000002658804833.png?HW-CC-KV=V1&HW-CC-Date=20260723T013225Z&HW-CC-Expire=86400&HW-CC-Sign=0265154CC9FD241563679C29B59957990B505C407B735A50506EBDD1EA513036)
