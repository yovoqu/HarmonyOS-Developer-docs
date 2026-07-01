# 如何对SelectDialog的单选项进行增减

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1580

## 如何对SelectDialog的单选项进行增减
 


##### 问题现象

如图所示，[纯列表弹出框](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-dialog#示例2纯列表弹出框)提供如下的示意图，如何自定义单选项的数量，使得弹窗属性title的内容是从string数组foreach遍历获取？
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/xDuRdR7nSYSO52dOQrvIyQ/zh-cn_image_0000002658969515.png?HW-CC-KV=V1&HW-CC-Date=20260701T025701Z&HW-CC-Expire=86400&HW-CC-Sign=DEAC6941A51694AA53F681AC6C862ACC6CF1933E7C42FA449CDC8EC776A17427)

 
 

##### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/3Ejc15GRREKm7UL1o2Yk8A/zh-cn_image_0000002628610296.gif?HW-CC-KV=V1&HW-CC-Date=20260701T025701Z&HW-CC-Expire=86400&HW-CC-Sign=A7BCF2E88D0D91C00BAD43367CA792F7773426AE19B6CFF32DB6AA0AD8312B0F)

 
 

##### 背景知识

[SelectDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-dialog#selectdialog)：选择类弹出框，弹框中以列表或网格的形式提供可选的内容。
 
 

##### 解决方案

在aboutToAppear中使用for循环动态初始化SelectDialog的radioContent。
 
```text
import { SelectDialog } from '@kit.ArkUI';

@Entry
@Component
struct SelectDialogDemo {
  // title数组
  titleList: string[] = [];
  // SelectDialog的radioContent进行初始化
  radioContent: ArraySheetInfo> = [];
  // 设置默认选中radio的index
  radioIndex = 0;
  dialogControllerList: CustomDialogController = new CustomDialogController({
    builder: SelectDialog({
      title: '文本标题',
      selectedIndex: this.radioIndex,
      confirm: {
        value: '取消',
        action: () => {
        },
      },
      // 将初始化后的radioContent赋值给SelectDialog的radioContent属性
      radioContent: this.radioContent
    }),
  });

  build() {
    Row() {
      Stack() {
        Column() {
          Button('纯列表弹出框')
            .width(96)
            .height(40)
            .onClick(() => {
              this.titleList.push('文本');
              this.titleList.push('文本文本');
              this.titleList.push('文本文本文本');
              this.titleList.push('文本文本文本文本');
              this.titleList.push('文本文本文本文本文本');
              this.titleList.push('文本文本文本文本文本文本');

              // 赋值给radioContent
              this.titleList.forEach((value: string, index: number) => {
                let sheetInfo: SheetInfo = {
                  title: value,
                  action: () => {
                    this.radioIndex = index;
                  }
                };
                this.radioContent.push(sheetInfo);
              });
              this.dialogControllerList.open();
            });
        }.margin({ bottom: 300 });
      }
      .align(Alignment.Bottom)
      .width('100%')
      .height('100%');
    }
    .backgroundImageSize({ width: '100%', height: '100%' })
    .height('100%');
  }
}
```
