# 居中显示TimePicker的文本

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-594

#### 问题现象

在使用TimePicker组件时，小时和分钟文本的默认间距及对齐方式如下图所示。请问如何调整设置以减小两者之间的间距并使文本居中显示？
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/-zQIfxFySgCp0u7HwknZpw/zh-cn_image_0000002658791799.png?HW-CC-KV=V1&HW-CC-Date=20260701T041218Z&HW-CC-Expire=86400&HW-CC-Sign=D34392F83A9045812D5C863BFC6C60D3F8A41061C6ED3176D9AA9B60703DF189)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/eTeRSz-aQLacFjgo7vq7sA/zh-cn_image_0000002628552422.png?HW-CC-KV=V1&HW-CC-Date=20260701T041218Z&HW-CC-Expire=86400&HW-CC-Sign=29531043FC29D1EEBE279910E92139484779AD2A5665C4F1B8D0E4E1BCE45773)

 
 

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
      <em>  // 加入水平分割线</em>
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
         <em> // 调整TimePicker组件的宽度</em>
        .width('30%');
      Column() {
       <em> // 加入水平分割线</em>
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
