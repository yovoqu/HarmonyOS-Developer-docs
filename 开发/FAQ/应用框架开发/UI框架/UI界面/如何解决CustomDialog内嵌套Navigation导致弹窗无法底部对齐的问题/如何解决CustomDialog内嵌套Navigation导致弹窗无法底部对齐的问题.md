# 如何解决CustomDialog内嵌套Navigation导致弹窗无法底部对齐的问题

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1483

#### 问题现象

当CustomDialog内部嵌套Navigation容器时，弹窗设置底部显示alignment: DialogAlignment.Bottom时失效，问题代码如下：
 
```text
@CustomDialog
export struct MyDialog {
  controller: CustomDialogController;

  build() {
    Navigation() {
      Column() {
        Text('我是弹窗')
          .margin({ top: 20 });
      }
      .width('100%')
      .height(200)
      .backgroundColor(Color.White);
    };
  }
}

@Entry
@Component
struct Dialog {
  myDiaController: CustomDialogController = new CustomDialogController({
    builder: MyDialog({}),
    customStyle: true, <em>// 弹窗容器样式是否自定义</em>
    autoCancel: false,<em> // 是否允许点击遮障层退出</em>
    alignment: DialogAlignment.Bottom,<em> // 弹窗在竖直方向上的对齐，底部对齐失效</em>
  });

  onPageShow(): void {
    this.myDiaController.open();
  }

  build() {
  }
}
```
 
问题现象如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/YRrTLS4DS5-d91dlPxK3Ig/zh-cn_image_0000002658845073.png?HW-CC-KV=V1&HW-CC-Date=20260811T005713Z&HW-CC-Expire=86400&HW-CC-Sign=6BF78959CE4630202D5AFB48A7FB8FEE49C96D7324DCDC490AFC2961232487FD)

 
 

#### 背景知识

[CustomDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-custom-dialog-box)：是一种常见的自定义弹窗方式，当其内部嵌套[Navigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation)容器时，Navigation容器在不设置高度的情况下会默认撑满屏幕，而Navigation内部默认至上而下显示，所以导致弹窗的底部显示命令在显示效果上没有生效。
 
 

#### 解决方案

- 由于Navigation在不设置高度时，默认撑满整个手机屏幕，导致嵌套Navigation的弹窗也是全屏显示，从而导致DialogAlignment.Bottom从体验上未生效。实际逻辑是弹窗已经是全屏显示，弹窗底部对齐后依旧是全屏显示。
- 为Navigation容器设置高度限制（本示例设置300vp），并设置背景颜色为蓝色后，可以发现弹窗为底部对齐效果：
```text
@CustomDialog
export struct MyDialog {
  controller: CustomDialogController;
  pathStack: NavPathStack = new NavPathStack();

  build() {
 <em>   // 弹窗内使用Navigation可实现弹窗内路由跳转，从而更换弹窗内显示的页面</em>
    Navigation(this.pathStack) {
      Column() {
        Text('我是弹窗')
          .margin({ top: 20 });
      }
      .width('100%')
      .height(200)
      .backgroundColor(Color.White);
    }
    .height(300)
    .backgroundColor('#0a59f7');
  }
}

@Entry
@Component
struct DialogDemo {
  myDialogController: CustomDialogController = new CustomDialogController({
    builder: MyDialog({}),
    customStyle: true, <em>// 弹窗容器样式是否自定义</em>
    autoCancel: false,<em> // 是否允许点击遮障层退出</em>
    alignment: DialogAlignment.Bottom,<em> // 弹窗在竖直方向上的对齐，底部对齐失效</em>
  });

  onPageShow(): void {
    this.myDialogController.open();
  }

  build() {
  }
}
```


 
实现效果如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/ILKGvnkxR1mSVz1AUFN56Q/zh-cn_image_0000002628765700.png?HW-CC-KV=V1&HW-CC-Date=20260811T005713Z&HW-CC-Expire=86400&HW-CC-Sign=1FF3278A2539A3FAE08F35C4FD49826C80065C239C6DD0C49BDB30CF2622BDFE)

 
上图中弹窗为白色与蓝色部分（其中白色是弹窗中子组件背景色，蓝色是弹窗背景色），弹窗底部对齐。
 
 

#### 总结

多数情况下，父容器的大小在未设置尺寸限制的情况下默认自适应子组件大小，所以，该思维惯性会陷入一个误区：默认Navigation容器未设置尺寸时会自适应其子组件Column的高度200vp，从而默认弹窗高度是200vp、底部对齐命令未生效。而实际上，部分容器在未设置尺寸限制时会默认全屏显示，例如Navigation、Tabs等。
