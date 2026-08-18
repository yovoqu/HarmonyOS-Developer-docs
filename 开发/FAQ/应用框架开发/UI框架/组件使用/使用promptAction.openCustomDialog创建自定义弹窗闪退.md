# 使用promptAction.openCustomDialog创建自定义弹窗闪退

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1159

#### 问题现象

使用promptAction.openCustomDialog创建自定义弹窗，将全局Builder构建函数作为自定义弹窗内容构造器。弹窗弹出时应用闪退。错误日志为：
 
```text
Reason:TypeError Error name:TypeError Error message:Cannot read property observeComponentCreation2 of undefined
```
 
问题代码为：
 
```text
import { promptAction } from '@kit.ArkUI'


@Builder
function customDialogComponent() {
  Column() {
    Text('customDialogComponent')
  }
}


@Entry
@Component
struct Index {
  build() {
    Column() {
      Button('弹窗').onClick(() => {
        this.getUIContext().getPromptAction().openCustomDialog({
          builder: () => {
            customDialogComponent()
          },
          alignment: DialogAlignment.Center
        })
      })
    }
  }
}
```
 
 

#### 背景知识

ArkUI提供了一种轻量的UI元素复用机制[@Builder](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builder)，其内部UI结构固定，仅与使用方进行数据传递，开发者可以将重复使用的UI元素抽象成一个方法，在build方法里调用。
 
 

#### 解决方案

自定义构建函数@Builder可以在所属组件的build方法和其他自定义构建函数中调用，但不允许在组件外调用。因此，需要将自定义构建函数@Builder移至结构体内部，示例代码如下：
 
```text
@Entry
@Component
struct Index55 {
  private customDialogComponentId: number = 0;


  // 在结构体内构建定义函数
  @Builder
  customDialogComponent() {
    Column() {
      Text('温馨提示')
        .fontSize(25)
        .margin({ top: 10 });
      Text('请注意,一旦删除,该数据将从缓存中删除且不可恢复。请谨慎选择。')
        .padding({ left: 20, right: 20 });
      Row({ space: 50 }) {
        Button('确认').onClick(() => {
          try {
            this.getUIContext().getPromptAction().closeCustomDialog(this.customDialogComponentId);
          } catch (error) {
            let message = (error as BusinessError).message;
            let code = (error as BusinessError).code;
            console.error(`closeCustomDialog error code is ${code}, message is ${message}`);
          }
        });
        Button('取消').onClick(() => {
          try {
            this.getUIContext().getPromptAction().closeCustomDialog(this.customDialogComponentId);
          } catch (error) {
            let message = (error as BusinessError).message;
            let code = (error as BusinessError).code;
            console.error(`closeCustomDialog error code is ${code}, message is ${message}`);
          }
        });
      };
    }.height(200).padding(5).justifyContent(FlexAlign.SpaceAround);
  }


  build() {
    RelativeContainer() {
      Button('弹窗')
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.getUIContext().getPromptAction().openCustomDialog({
            builder: () => {
              this.customDialogComponent();
            },
            alignment: DialogAlignment.Center
          }).then((dialogId: number) => {
            this.customDialogComponentId = dialogId;
          });
        });
    }
    .width('100%')
    .height('100%');
  }
}
```
 
效果如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/9HNTyhVcSEW-Ho-fqhEsqw/zh-cn_image_0000002658929081.png?HW-CC-KV=V1&HW-CC-Date=20260701T041257Z&HW-CC-Expire=86400&HW-CC-Sign=9E06231D4E7C80EE425C84F058ECDCB4785A735FCF873CD52F8773E592EBE1C4)
