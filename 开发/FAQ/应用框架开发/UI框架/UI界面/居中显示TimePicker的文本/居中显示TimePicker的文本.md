# 居中显示TimePicker的文本

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-594

#### 问题现象

在使用TimePicker组件时，小时和分钟文本的默认间距及对齐方式如下图所示。请问如何调整设置以减小两者之间的间距并使文本居中显示？
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/-zQIfxFySgCp0u7HwknZpw/zh-cn_image_0000002658791799.png?HW-CC-KV=V1&HW-CC-Date=20260811T005721Z&HW-CC-Expire=86400&HW-CC-Sign=93368ED560E5A033D78F2FE9B9B7DA5FCE860F9E373A054A17ADCF7D52EDBBA1)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/eTeRSz-aQLacFjgo7vq7sA/zh-cn_image_0000002628552422.png?HW-CC-KV=V1&HW-CC-Date=20260811T005721Z&HW-CC-Expire=86400&HW-CC-Sign=5CAED80A909AE7963E308350F0E6A31042FCAC760447160E316566FB6138864E)

 
 

#### 背景知识

[TimePicker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-timepicker)为时间选择组件，可以根据指定参数创建选择器，支持选择小时及分钟。TimePicker除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)外，还支持设置[useMilitaryTime](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-timepicker#usemilitarytime)、[disappearTextStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-timepicker#disappeartextstyle10)、[textStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-timepicker#textstyle10)等属性。
 
 

#### 解决方案

可以考虑通过调整TimePicker组件的宽度，其中的小时和分钟会自适应调整占用宽度。用在两边加入水平分割线的方法来间接实现对文本间距的调整。
 
```json
@Entry
@Component
struct CenterAlignPage {
  private selectedTime: Date = new Date('2022-07-22T08:00:00');

  build() {
    Row() {
      Column() {
        // 加入水平分割线
        Text("")
          .width('35%')
          .height(0.2)
          .backgroundColor(('#A0A0A4')).margin({ top: 72 });
        Text("")
          .width('35%')
          .height(0.2)
          .backgroundColor(('#A0A0A4')).margin({ top: 56 });
      };

      TimePicker({
        selected: this.selectedTime,
      })
        .useMilitaryTime(true)
        .loop(true)
        .disappearTextStyle({
          color: Color.White,
          font: {
            size: 16,
            weight: FontWeight.Lighter
          }
        })
        .textStyle({
          font: {
            size: 18, weight: FontWeight.Normal
          }
        })
        .selectedTextStyle({
          font: {
            size: 20, weight: FontWeight.Bolder
          }
        })
        .onChange((value: TimePickerResult) => {
          this.selectedTime.setHours(value.hour, value.minute);
          console.info('select current date is: ', JSON.stringify(value));
        })
          // 调整TimePicker组件的宽度
        .width('30%');
      Column() {
        // 加入水平分割线
        Text("")
          .width('35%')
          .height(0.2)
          .backgroundColor(('#A0A0A4')).margin({ top: 72 });
        Text("")
          .width('35%')
          .height(0.2)
          .backgroundColor(('#A0A0A4')).margin({ top: 56 });
      };
    }.alignItems(VerticalAlign.Top)
    .height('100%');
  }
}
```
