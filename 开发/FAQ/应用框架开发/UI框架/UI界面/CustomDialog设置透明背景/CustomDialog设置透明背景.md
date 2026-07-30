# CustomDialog设置透明背景

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1454

#### 问题现象

如何将自定义弹窗（CustomDialog）的背景设置为透明？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/xk5EXdzsQs-eLFaNpeeahw/zh-cn_image_0000002628764166.png?HW-CC-KV=V1&HW-CC-Date=20260730T072458Z&HW-CC-Expire=86400&HW-CC-Sign=B7EA555D4E2AE22C08F68C8C9B1303CB0A75882D8562254B9305B70C30C35E62)

 
 

#### 背景知识

自定义弹窗组件[CustomDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-custom-dialog-box)类能够显示弹窗，并且可以自定义弹窗的样式与内容，允许用户灵活地设置弹窗的样式，布局和交互行为。
 
 

#### 解决方案

CustomDialog设置透明背景的解决方案如下：
 
- **方案一**：将CustomDialog的backgroundColor设置为Color.Transparent，同时将backgroundBlurStyle设置为BlurStyle.NONE（若此项不设置则自定义弹窗的背景色为白色），两种属性配合使用实现透明背景效果。
```text
@CustomDialog
struct CustomDialogContent {
  controller: CustomDialogController;

  build() {
    Column() {
      Button('关闭').onClick(() => {
        this.controller.close();
      })
        .backgroundColor('#0a59f7');
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%');
  }
}

@Entry
@Component
struct Index {
  dialogController: CustomDialogController = new CustomDialogController({
    builder: CustomDialogContent(),
   <em> // 设置弹窗背景色为透明</em>
    backgroundColor: Color.Transparent,
    backgroundBlurStyle: BlurStyle.NONE
  });

  build() {
    Row() {
      Button('弹窗').onClick(() => {
        this.dialogController.open();
      })
        .backgroundColor('#0a59f7')
        .margin({ top: 100 });
    }
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
    .alignItems(VerticalAlign.Center)
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%')
    .backgroundColor(0xF1F3F5);
  }
}
```

- **方案二**：通过将CustomDialog的属性customStyle设置为true，就可以将弹窗容器样式的可自定义性关闭，此时的弹窗圆角为0，背景色为透明色。
```text
@CustomDialog
struct CustomDialogContent1 {
  controller: CustomDialogController;

  build() {
    Column() {
      Button('关闭').onClick(() => {
        this.controller.close();
      })
        .backgroundColor('#0a59f7');
    };
  }
}

@Entry
@Component
struct Index1 {
  dialogController: CustomDialogController = new CustomDialogController({
    builder: CustomDialogContent1(),
    customStyle: true, <em>// 设置弹窗背景色为透明</em>
  });

  build() {
    Row() {
      Button('弹窗').onClick(() => {
        this.dialogController.open();
      })
        .backgroundColor('#0a59f7') <em>// 按钮颜色</em>
        .margin({ top: 100 });
    }
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
    .alignItems(VerticalAlign.Center)
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%')
    .backgroundColor(0xF1F3F5); <em>// 主页面背景色</em>
  }
}
```

- **方案三**：在方案二的基础上，通过将isModal设置为false，将弹窗设置为非模态弹窗，而非模态窗口无蒙层，即可实现完全透明弹窗。
```text
@CustomDialog
struct CustomDialogContent2 {
  controller: CustomDialogController;

  build() {
    Column() {
      Button('关闭').onClick(() => {
        this.controller.close();
      })
        .backgroundColor('#0a59f7');
    };
  }
}

@Entry
@Component
struct Index2 {
  dialogController: CustomDialogController = new CustomDialogController({
    builder: CustomDialogContent2(),
    customStyle: true, <em>// 设置弹窗背景色为透明</em>
    isModal: false
  });

  build() {
    Row() {
      Button('弹窗').onClick(() => {
        this.dialogController.open();
      })
        .backgroundColor('#0a59f7')
        .margin({ top: 100 });
    }
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
    .alignItems(VerticalAlign.Center)
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%')
    .backgroundColor(0xF1F3F5);
  }
}
```


 
 

#### 常见FAQ

Q：如何修改自定义弹窗的背景色？同时怎么设定弹窗不点击遮罩就能消除？
 
A：可以使用自定义弹窗[CustomDialogControllerOptions对象说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-custom-dialog-box#customdialogcontrolleroptions对象说明)下的蒙层颜色属性maskColor修改弹窗背景色，是否允许点击遮障层退出属性autoCancel设定弹窗不点击遮罩就能消除。
 
Q：为什么使用maskColor:"0xB0000000"设置maskColor无效？
 
A：该写法不符合规范，因此失效，可通过maskColor:0xB0000000或maskColor:'#B0000000'这样的规范写法设置maskColor。
 
Q：为maskColor设置resource类型不生效。
 
A：maskColor当前只支持字符串颜色值，不支持\$r()资源引用。
 
 

#### 总结

方案一、二、三都是通过自定义[CustomDialogController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-custom-dialog-box#customdialogcontroller)类方法实现透明背景，但实现方法略有不同，因此应用场景也不同，常见场景如下表格：
  
| 方案 | 特点 | 适用场景 |
| --- | --- | --- |
| 方案一 | 弹窗背板填充和模糊材质固定。 | 消息提示、操作确认、图片预览。 |
| 方案二 | 不能自定义弹窗容器样式。 | 系统消息提示、应用权限请求、软件错误提示。 |
| 方案三 | 背景完全透明。 | 悬浮窗效果、评论弹窗。 |
