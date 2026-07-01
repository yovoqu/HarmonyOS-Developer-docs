# 调用closeCustomDialog关闭弹窗未触发aboutToDisappear生命周期回调

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-942

## 调用closeCustomDialog关闭弹窗未触发aboutToDisappear生命周期回调
 


##### 问题现象

通过uiContext.getPromptAction().openCustomDialog()打开弹窗时aboutToAppear()会触发，但是uiContext.getPromptAction().closeCustomDialog()关闭弹窗时aboutToDisappear()未触发。
 
问题代码示例参考如下：
 
- Index：
```text
@Entry
@Component
struct CustomDialogCloseDemo {
  @State setTimeOut: number = 0;

  build() {
    Row() {
      Column({ space: 20 }) {
        Button('打开自定义弹窗')
          .fontSize(20)
          .onClick(async () => {
            const uiContext = this.getUIContext();
            const componentContent = new ComponentContent(this.getUIContext(), wrapBuilder(customDialogBuilder));
            uiContext.getPromptAction().openCustomDialog(componentContent, {
              onWillDismiss: () => {
                uiContext.getPromptAction().closeCustomDialog(componentContent).then(() => {
                });
              }
            });
            this.setTimeOut = setTimeout(() => {
              uiContext.getPromptAction().closeCustomDialog(componentContent).then(() => {
              });
            }, 2000);
          });
      }
      .width('100%');
    }
    .height('100%');
  }
}
```

- customDialogComponent：
```text
@Builder
export function customDialogBuilder() {
  customDialogComponent();
}

@Component
struct customDialogComponent {
  aboutToAppear(): void {
    console.info('测试弹窗打开');
  }

  aboutToDisappear(): void {
    console.info('测试弹窗关闭');
  }

  build() {
    Column({ space: 30 }) {
      Text('弹窗页面')
        .fontColor(Color.White)
        .height('100%')
        .fontSize(30);
    }
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
    .height(150)
    .width('90%')
    .justifyContent(FlexAlign.SpaceBetween)
    .backgroundColor('rgba(148, 148, 148, 1.00)');
  }
}
```


 
 

##### 背景知识

[ComponentContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-componentcontent#componentcontent-1)创建的[openCustomDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-promptaction#opencustomdialog12)弹窗的关闭过程不涉及页面的销毁，弹窗关闭时不会执行[aboutToDisappear()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-lifecycle#abouttodisappear)方法。
 
 

##### 解决方案

如果想在弹窗关闭后触发弹窗的aboutToDisappear()生命周期函数，可以在promptAction.closeCustomDialog()的异步方法回调里，调用ComponentContent的[dispose()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-componentcontent#dispose)方法立即释放当前ComponentContent实例，解除节点之间的绑定关系即可触发aboutToDisappear()生命周期函数。
 
对index代码做如下修改：
 
```text
import { ComponentContent } from '@kit.ArkUI';
import { customDialogBuilder } from './customDialogComponent';

@Entry
@Component
struct CustomDialogCloseDemo {
  @State setTimeOut: number = 0;

  build() {
    Row() {
      Column({ space: 20 }) {
        Button('打开自定义弹窗')
          .fontSize(20)
          .onClick(async () => {
            const uiContext = this.getUIContext();
            const componentContent = new ComponentContent(this.getUIContext(), wrapBuilder(customDialogBuilder));
            uiContext.getPromptAction().openCustomDialog(componentContent, {
              onWillDismiss: () => {
                uiContext.getPromptAction().closeCustomDialog(componentContent).then(() => {
                  clearTimeout(this.setTimeOut);
                  componentContent.dispose();
                });
              }
            });
            this.setTimeOut = setTimeout(() => {
              uiContext.getPromptAction().closeCustomDialog(componentContent).then(() => {
                componentContent.dispose();
              });
            }, 2000);
          });
      }
      .width('100%');
    }
    .height('100%');
  }
}
```
 
实现效果如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/W1jMZWTMQ6S9rr3-jUIfTQ/zh-cn_image_0000002628401218.png?HW-CC-KV=V1&HW-CC-Date=20260701T025706Z&HW-CC-Expire=86400&HW-CC-Sign=414F63534974C2CB97458F0D75EFC99938BCA34F328A19034BB761934E6319B6)
