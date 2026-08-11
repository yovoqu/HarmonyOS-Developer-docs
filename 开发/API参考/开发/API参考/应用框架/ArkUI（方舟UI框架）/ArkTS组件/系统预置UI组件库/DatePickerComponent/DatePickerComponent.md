# DatePickerComponent

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-datepickercomponent
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

DatePickerComponent组件用于选择日期（年月日）和时间（时分秒）。

**起始版本：** 26.0.0


#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { DatePickerComponent, DatePickerComponentOptions, DisplayMode, DateMode, TimeFormat, DatePickerComponentResult } from '@kit.ArkUI';
```



#### 子组件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

无



#### DatePickerComponent

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

DatePickerComponent({ options: DatePickerComponentOptions })

定义日期时间选择器组件。

**起始版本：** 26.0.0

**装饰器类型：** @Component

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| options | DatePickerComponentOptions | 是 | @Prop | 定义日期时间选择器组件的选项。 |




#### DatePickerComponentOptions

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

DatePickerComponentOptions定义日期时间选择器组件的选项。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| displayMode | DisplayMode | 否 | 是 | 选择器的显示模式。 默认值：DisplayMode.DATE 说明： - DATE：仅显示日期，使用dateOptions，适用于只需要用户选择日期的场景，如生日选择、日程日期设置等。 - TIME：仅显示时间，使用timeOptions，适用于只需要用户选择时间的场景，如闹钟设置、提醒时间设置等。 - DATE_TIME：同时显示日期和时间，dateOptions与timeOptions同时生效，适用于需要用户同时选择日期和时间的场景，如日程安排、会议时间设置等。 |
| dateOptions | DateOptions | 否 | 是 | 日期选项。 |
| timeOptions | TimeOptions | 否 | 是 | 时间选项。 |




#### DisplayMode

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

DisplayMode枚举用于定义选择器的显示模式。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DATE | 0 | 仅显示日期。 |
| TIME | 1 | 仅显示时间。 |
| DATE_TIME | 2 | 同时显示日期和时间。 |




#### DateMode

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

DateMode枚举用于定义日期选择器的模式。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DATE | 0 | 日期显示三列：年、月、日。 |
| YEAR_AND_MONTH | 1 | 日期显示两列：年、月。 |
| MONTH_AND_DAY | 2 | 显示月、日二列。在此模式下，年份始终保持不变，取值为selected指定的年份；若selected未指定则取当前系统年份。当月份从12月变为1月时，年份不会增加；当月份从1月变为12月时，年份不会减少。当月份滚动导致日期超出有效范围时，日期会自动调整至该月最后一天。 |




#### TimeFormat

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

TimeFormat枚举用于定义时间选择器的格式。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HOUR_MINUTE | 0 | 显示时、分。 |
| HOUR_MINUTE_SECOND | 1 | 显示时、分、秒。 |




#### DatePickerComponentResult

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

DatePickerComponentResult定义日期时间选择器的选择结果，包含用户选择的年、月、日、时、分、秒信息，用于在onChange和onScrollStop回调中传递选择的具体日期时间值。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| year | number | 否 | 是 | 所选日期的年份。 |
| month | number | 否 | 是 | 所选日期的月份索引，从0开始，0表示1月，11表示12月。 |
| day | number | 否 | 是 | 所选日期的日。 |
| hour | number | 否 | 是 | 所选时间的小时部分。 |
| minute | number | 否 | 是 | 所选时间的分钟部分。 |
| second | number | 否 | 是 | 所选时间的秒部分。 |




#### CommonOptions

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

CommonOptions定义日期时间选择器的通用选项。

> [!TIP]
> Date构造函数参数顺序为：年、月索引（0-11）、日、时、分、秒。注意：年份参数需大于99或小于0以避免1900年代映射。 Date的使用请参考 TimePickerOptions ，需要注意的是，当需要设置1-99的年份日期时，不可使用new Date(1, 0, 1)写法，因为JavaScript的new Date(year, month, day)构造函数对1-99的年份有特殊处理，会自动加上1900，即变为1901年，因此此时推荐使用new Date('0001-01-01')写法。 DatePickerComponent的文本字号根据显示的总列数变化，当列数大于等于6列时，字号为14vp，其他情况下为16vp，当组件宽度过窄时，可能出现文本显示截断的情况。 参数缺省或者设置为undefined时，均保持默认值。 在 DateOptions 中设置start、end、selected时仅日期部分（年月日）设置生效，在 TimeOptions 中设置start、end、selected时仅时间部分（时分秒）设置生效。系统会根据配置的displayMode和对应的Options类型，自动过滤Date对象的相应部分并应用约束。


**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| start | Date | 否 | 是 | 选择器的起始日期或时间。 默认值：Date('1970-01-01T00:00:00') 取值范围：[Date('0001-01-01T00:00:00'), Date('9999-12-31T23:59:59')] 说明： 设置了start且为有效值的场景下，loop不生效。 |
| end | Date | 否 | 是 | 选择器的结束日期或时间。 默认值：Date('2100-12-31T23:59:59') 取值范围：[Date('0001-01-01T00:00:00'), Date('9999-12-31T23:59:59')] 说明： 设置了end且为有效值的场景下，loop不生效。 |
| selected | Date | 否 | 是 | 选中的日期或时间，设置后作为初始选中值显示。 默认值为当前系统日期或时间。 说明： 在DateMode.MONTH_AND_DAY模式下，仅month和day字段参与选择；年份取selected指定值，未指定时取当前系统年份，滚动过程中保持不变。 |
| loop | boolean | 否 | 是 | 设置是否启用循环模式。 - true：启用循环模式，支持滚动到边界时继续循环选择。 - false：不启用循环模式，滚动到边界时停止。 默认值：true 使用场景： 循环模式适用于需要连续滚动选择的场景，如快速浏览年月；非循环模式适用于需要明确边界范围的场景。 说明： 设置了start或end且为有效值的场景下，本参数不生效。 |
| onChange | Callback&lt;DatePickerComponentResult&gt; | 否 | 是 | 选择日期或时间后触发该回调。 |
| onScrollStop | Callback&lt;DatePickerComponentResult&gt; | 否 | 是 | 选择器项被选中且滚动停止时触发该回调。 |
| enableHapticFeedback | boolean | 否 | 是 | 设置是否启用触控反馈。 默认值：true - true：启用触控反馈，适用于需要增强用户交互体验的场景，如游戏、乐器类应用等。 - false：不启用触控反馈，适用于不需要触觉反馈或需要节省设备资源的场景。 说明： 1. 设置为true后，其生效情况取决于系统的硬件是否支持。 2. 启用触控反馈时，需要在工程的module.json5中配置requestPermissions字段以开启振动权限，配置如下： "requestPermissions": [{"name": "ohos.permission.VIBRATE"}] |


> [!NOTE]
> onChange在用户选择日期或时间时触发，用于响应用户的选择操作。 onScrollStop在滚动完全停止后触发，无论值是否变化都会返回当前选中项。 两者可根据需要同时使用或单独使用：onChange用于即时响应用户选择，onScrollStop用于获取滚动停止后的稳定结果。


**起始日期、结束日期和选中日期的异常情形说明：**

| 异常情形 | 对应结果 |
| --- | --- |
| 起始日期晚于结束日期，选中日期未设置。 | 起始日期、结束日期和选中日期都为默认值。 |
| 起始日期晚于结束日期，选中日期早于起始日期默认值。 | 起始日期、结束日期都为默认值，选中日期为起始日期默认值。 |
| 起始日期晚于结束日期，选中日期晚于结束日期默认值。 | 起始日期、结束日期都为默认值，选中日期为结束日期默认值。 |
| 起始日期晚于结束日期，选中日期在起始日期与结束日期默认值范围内。 | 起始日期、结束日期都为默认值，选中日期为设置的值。 |
| 选中日期早于起始日期。 | 选中日期为起始日期。 |
| 选中日期晚于结束日期。 | 选中日期为结束日期。 |
| 起始日期晚于当前系统日期，选中日期未设置。 | 选中日期为起始日期。 |
| 结束日期早于当前系统日期，选中日期未设置。 | 选中日期为结束日期。 |
| Date对象构造参数不符合规范或无效，如年份、月份、日期等参数超出有效范围，或传入无效字符串导致Invalid Date。 | 取默认值。 |
| 起始日期或结束日期早于取值范围最小值。 | 起始日期或结束日期取起始日期默认值。 |
| 起始日期或结束日期晚于取值范围最大值。 | 起始日期或结束日期取结束日期默认值。 |
| 起始日期与结束日期同时早于取值范围最小值。 | 起始日期与结束日期取系统有效范围最早日期。 |
| 起始日期与结束日期同时晚于取值范围最大值。 | 起始日期与结束日期取系统有效范围最晚日期。 |


**起始时间和结束时间的异常情形说明：**

| 异常情形 | 对应结果 |
| --- | --- |
| 起始时间晚于结束时间。 | 起始时间、结束时间都为默认值。 |
| 选中时间早于起始时间。 | 选中时间为起始时间。 |
| 选中时间晚于结束时间。 | 选中时间为结束时间。 |
| 起始时间晚于当前系统时间，选中时间未设置。 | 选中时间为起始时间。 |
| 结束时间早于当前系统时间，选中时间未设置。 | 选中时间为结束时间。 |
| Date对象构造参数不符合规范或无效，如小时、分钟、秒等参数超出有效范围，或传入无效字符串导致Invalid Date。 | 取默认值。 |




#### DateOptions

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

DateOptions定义日期选择器的选项。

继承于[CommonOptions](#commonoptions)。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| mode | DateMode | 否 | 是 | 定义日期选择器的模式。 默认值：DateMode.DATE |
| lunar | boolean | 否 | 是 | 指定是否显示为农历。 - true：显示为农历，适用于需要传统农历日期的场景，如传统节日、农历生日、农历纪念日等。 - false：不显示为农历，适用于使用公历日期的场景。 默认值：false 说明： 仅在简体中文和繁体中文语言环境下生效，其他语言环境下设置该属性无效果。 |




#### TimeOptions

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

TimeOptions定义时间选择器的选项。

继承于[CommonOptions](#commonoptions)。

> [!TIP]
> 若设置了start或end参数且为有效值，loop参数将不生效，具体请参考 CommonOptions 的参数说明。


**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| format | TimeFormat | 否 | 是 | 定义时间选择器的格式。 默认值：TimeFormat.HOUR_MINUTE |
| useMilitaryTime | boolean | 否 | 是 | 指定是否使用24小时制显示时间。 - true：时间以24小时制展示，适用于国际化应用、需要精确时间表达的专业场景（如医疗、交通、军事等）。 - false：时间以12小时制展示，适用于面向普通用户的日常应用场景，更符合用户的日常阅读习惯。 默认值：false |




#### 示例

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV



#### 示例1（日期选择器）

该示例通过设置[DatePickerComponentOptions](#datepickercomponentoptions)中的displayMode为DisplayMode.DATE，实现日期选择器。

从API版本26.0.0开始，新增[DatePickerComponentOptions](#datepickercomponentoptions)参数。

```text
import { DatePickerComponent, DisplayMode, DateMode } from '@kit.ArkUI';

@Entry
@Component
struct DatePickerExample {
  @State selectedYear: number = 2026
  @State selectedMonth: number = 0
  @State selectedDay: number = 1

  build() {
    Column() {
      DatePickerComponent({
        options: {
          displayMode: DisplayMode.DATE,
          dateOptions: {
            mode: DateMode.DATE,
            selected: new Date(this.selectedYear, this.selectedMonth, this.selectedDay),
            start: new Date('2020-03-01'),
            end: new Date('2030-10-31'),
            enableHapticFeedback: true,
            onChange: (result) => {
              console.info('Selected date: ' + (result.year ?? 0) + '-' + ((result.month ?? 0) + 1) + '-' + (result.day ?? 0));
              if (result.year !== undefined) {
                this.selectedYear = result.year
              }
              if (result.month !== undefined) {
                this.selectedMonth = result.month
              }
              if (result.day !== undefined) {
                this.selectedDay = result.day
              }
            },
            onScrollStop: (result) => {
              console.info('Scroll stop: ' + (result.year ?? 0) + '-' + ((result.month ?? 0) + 1) + '-' + (result.day ?? 0));
            }
          }
        }
      })
    }
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/VKONxXnvRBWcyzxjIQy9wg/zh-cn_image_0000002668303406.gif?HW-CC-KV=V1&HW-CC-Date=20260811T005506Z&HW-CC-Expire=86400&HW-CC-Sign=EFDC3E7C1C37B2AC76CFFB11AEACB8CD07B8D36124B959BC62CE6A0AA262B12E)




#### 示例2（时间选择器）

该示例通过设置[DatePickerComponentOptions](#datepickercomponentoptions)中的displayMode为DisplayMode.TIME，实现时间选择器。

从API版本26.0.0开始，新增[DatePickerComponentOptions](#datepickercomponentoptions)参数。

```text
import { DatePickerComponent, DisplayMode, TimeFormat } from '@kit.ArkUI';

@Entry
@Component
struct TimePickerExample {
  build() {
    Column() {
      DatePickerComponent({
        options: {
          displayMode: DisplayMode.TIME,
          timeOptions: {
            format: TimeFormat.HOUR_MINUTE,
            useMilitaryTime: true,
            enableHapticFeedback: true,
            onChange: (result) => {
              console.info('Selected time: ' + (result.hour ?? 0) + ':' + (result.minute ?? 0));
            },
            onScrollStop: (result) => {
              console.info('Scroll stop: ' + (result.hour ?? 0) + ':' + (result.minute ?? 0));
            }
          }
        }
      })
    }
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/mISfOFkPSZye8c0lhfflug/zh-cn_image_0000002668463280.gif?HW-CC-KV=V1&HW-CC-Date=20260811T005506Z&HW-CC-Expire=86400&HW-CC-Sign=C1707D56FBB7827BEF7E4DF19B6C26972D76F09EF5236B855558BC4BEF985FDA)




#### 示例3（日期时间选择器）

该示例通过设置[DatePickerComponentOptions](#datepickercomponentoptions)中的displayMode为DisplayMode.DATE_TIME，同时选择日期和时间。

从API版本26.0.0开始，新增[DatePickerComponentOptions](#datepickercomponentoptions)参数。

```json
import { DatePickerComponent, DisplayMode, DateMode, TimeFormat } from '@kit.ArkUI';

@Entry
@Component
struct DateTimePickerExample {
  build() {
    Column() {
      DatePickerComponent({
        options: {
          displayMode: DisplayMode.DATE_TIME,
          dateOptions: {
            mode: DateMode.DATE,
            lunar: false,
            enableHapticFeedback: true,
            onChange: (result) => {
              console.info('Selected: ' + JSON.stringify(result));
            },
            onScrollStop: (result) => {
              console.info('Scroll stop: ' + JSON.stringify(result));
            }
          },
          timeOptions: {
            format: TimeFormat.HOUR_MINUTE_SECOND,
            useMilitaryTime: false,
            onChange: (result) => {
              console.info('Selected: ' + JSON.stringify(result));
            },
            onScrollStop: (result) => {
              console.info('Scroll stop: ' + JSON.stringify(result));
            }
          }
        }
      })
    }
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/oEISd8JKTBu-LwWUcUdRAw/zh-cn_image_0000002698223161.gif?HW-CC-KV=V1&HW-CC-Date=20260811T005506Z&HW-CC-Expire=86400&HW-CC-Sign=A7773368EA6023916BFE9BEC170196B8FC941EA6D75691C90674B1B745A88261)




#### 示例4（关闭循环模式）

该示例通过设置[DateOptions](#dateoptions)中的loop为false，关闭选择器的循环滚动模式。

从API版本26.0.0开始，新增[DateOptions](#dateoptions)参数。

```text
import { DatePickerComponent, DisplayMode, DateMode } from '@kit.ArkUI';

@Entry
@Component
struct NoLoopPickerExample {
  build() {
    Column() {
      DatePickerComponent({
        options: {
          displayMode: DisplayMode.DATE,
          dateOptions: {
            mode: DateMode.DATE,
            selected: new Date(),
            start: new Date('2020-01-01'),
            end: new Date('2030-12-31'),
            loop: false,
            onChange: (result) => {
              console.info('Selected date: ' + (result.year ?? 0) + '-' + ((result.month ?? 0) + 1) + '-' + (result.day ?? 0));
            }
          }
        }
      })
    }
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/CI80H1pSR9yH6bI52DK9bA/zh-cn_image_0000002698143071.gif?HW-CC-KV=V1&HW-CC-Date=20260811T005506Z&HW-CC-Expire=86400&HW-CC-Sign=A641B554A8B6180DAC95F2AFBDBED1F537D6D65796F5617799C3CE41DC3F178C)
