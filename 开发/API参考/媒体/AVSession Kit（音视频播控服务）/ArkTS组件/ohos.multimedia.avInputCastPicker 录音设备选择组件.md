# @ohos.multimedia.avInputCastPicker (录音设备选择组件)

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-multimedia-avinputcastpicker
**支持设备：** PC/2in1

本模块提供创建录音设备选择组件AVInputCastPicker的功能，提供录音设备发现连接的统一入口。

> [!NOTE]
> 本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 示例效果请以真机为准，当前DevEco Studio预览器无实际录音设备选择功能。



#### 导入模块

**支持设备：** PC/2in1

```text
import { AVInputCastPicker } from '@kit.AVSessionKit';
```



#### 属性

**支持设备：** PC/2in1

支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)。



#### AVInputCastPicker

**支持设备：** PC/2in1

```text
AVInputCastPicker({
  customPicker?: CustomBuilder;
  onStateChange?: OnPickerStateCallback;
})
```

录音设备选择组件，可用于切换音频输入设备。

该组件为自定义组件，开发者在使用前需要先了解[@Component](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-custom-components#component)。

**装饰器类型：** [@Component](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-custom-components#component)

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVInputCast

**参数：**

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| customPicker | CustomBuilder | 否 | @Prop | 自定义样式。建议应用自定义组件样式，可有效提升组件渲染性能。 |
| onStateChange | OnPickerStateCallback | 否 | - | 设备列表状态变更回调。 |




#### OnPickerStateCallback

**支持设备：** PC/2in1

type OnPickerStateCallback = (state: AVCastPickerState) => void

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVInputCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | AVCastPickerState | 是 | 设备列表状态。 |




#### 事件

**支持设备：** PC/2in1

支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)。



#### 示例

**支持设备：** PC/2in1

录音设备选择组件功能的示例说明参考如下。

```text
import { AVCastPickerState, AVInputCastPicker } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {

  @State pickerImage: ResourceStr = $r('app.media.layered_image'); // 自定义资源。

  private onStateChange(state: AVCastPickerState) {
    if (state == AVCastPickerState.STATE_APPEARING) {
      console.info('The picker starts showing.');
    } else if (state == AVCastPickerState.STATE_DISAPPEARING) {
      console.info('The picker finishes presenting.');
    }
  }

  @Builder
  customPickerBuilder() {
    Image(this.pickerImage)
      .width('100%')
      .height('100%')
      .fillColor(Color.Black)
  }

  build() {
    Row() {
      Column() {
        AVInputCastPicker({
          customPicker: () => this.customPickerBuilder(),
          onStateChange: this.onStateChange
        })
          .width('40vp')
          .height('40vp')
          .border({ width: 1, color: Color.Red })
      }.height('50%')
    }.width('50%')
  }
}
```
