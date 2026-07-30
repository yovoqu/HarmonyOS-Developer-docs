# Toast是否支持设置字体大小和弹窗宽高等属性

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1436

#### 问题现象

Toast是否支持自定义设置字体大小和弹窗背板的宽高等属性？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/_vhMeuFsRzaetoR_unRN4g/zh-cn_image_0000002628763654.gif?HW-CC-KV=V1&HW-CC-Date=20260730T072451Z&HW-CC-Expire=86400&HW-CC-Sign=3788069EA6C59B13B8F149BD15088B9C6331C59C81A9B3AB9240074598FBDE9E)

 
 

#### 背景知识

- [即时反馈（Toast）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-toast)是一种临时性的消息提示框，用于向用户显示简短的操作反馈或状态信息。
- [不依赖UI组件的全局自定义弹出框](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-uicontext-custom-dialog)：在相对较复杂的应用场景中推荐使用UIContext中获取到的PromptAction对象提供的openCustomDialog接口来实现自定义弹出框。

 
 

#### 解决方案

[this.getUIContext().getPromptAction().openToast](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-promptaction#promptactionopentoast18)接口未提供设置字体大小和弹窗宽高等方法，可以使用this.getUIContext().getPromptAction().openCustomDialog打开自定义弹窗来实现定制化样式。方案如下：
 
- 使用[this.getUIContext().getPromptAction().openCustomDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-promptaction#opencustomdialog12)自定义弹窗，在相对较复杂的应用场景中推荐使用[全局自定义弹出框](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-uicontext-custom-dialog)的方式。
```text
let customDialogId: number = 0;

@Builder
function customDialogBuilder() {
  Column() {
   <em> // 可自定义文字大小及颜色</em>
    Text('自定义Toast').fontSize(20).fontColor('#fff');
  }
  .width('100%')
  .height('100%')
  .justifyContent(FlexAlign.Center)
  .alignItems(HorizontalAlign.Center);
}

@Entry
@Component
struct Index99 {
  @Builder
  customDialogComponent() {
    customDialogBuilder();
  }

  build() {
    Row() {
      Column() {
        Text('点击弹出Toast')
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            this.getUIContext().getPromptAction().openCustomDialog({
              builder: () => {
                this.customDialogComponent();
              },
          <em>    // 弹窗背景色</em>
              backgroundColor: 'rgba(0,0,0,0.8)',
              backgroundBlurStyle: BlurStyle.NONE,
              cornerRadius: 5,
              width: '50%',<em> </em><em>// 弹窗宽度</em>
              height: 50,<em> </em><em>// 弹窗高度</em>
              isModal: false,
              alignment: DialogAlignment.Center,
              offset: { dx: 0, dy: 100 }
            }).then((dialogId: number) => {
              customDialogId = dialogId;
              setTimeout(() => {
                this.getUIContext().getPromptAction().closeCustomDialog(customDialogId);
              }, 1500);
            });
          });
      }
      .width('100%');
    }
    .height('100%');
  }
}
```
