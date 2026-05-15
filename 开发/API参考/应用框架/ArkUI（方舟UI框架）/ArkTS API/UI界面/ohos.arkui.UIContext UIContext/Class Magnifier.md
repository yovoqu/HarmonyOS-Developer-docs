# Class (Magnifier)

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-magnifier
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

提供控制放大镜的显示与隐藏的能力，放大镜会对组件内容进行放大显示，便于查看组件细节。


## bind
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

bind(id: string): void

绑定放大镜与指定id的组件。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 组件id，可通过通用属性[id](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-component-id#id)或[key](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-component-id#key12)设置。当组件id为空字符串或未找到匹配id的组件时，不显示放大镜。 |


**示例：**

该示例通过监听onTouch事件控制放大镜对图片进行放大显示。


```ts
import { Magnifier } from '@kit.ArkUI';

@Entry
@Component
struct MagnifierExample {
  private magnifier: Magnifier = this.getUIContext().getMagnifier();

  build() {
    Column() {
      // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.startIcon'))
      .draggable(false)
      .width(200)
      .height(200)
      .margin(50)
      .id('image')
      .onTouch((event?: TouchEvent) => {
        if (event && event.sourceTool === SourceTool.Finger) {
          if (event.type === TouchType.Down) {
            this.magnifier.bind('image')
          } else if (event.type === TouchType.Move) {
            let x = event.touches[0].x
            let y = event.touches[0].y
            this.magnifier.show(x, y)
          } else if (event.type === TouchType.Up) {
            this.magnifier.unbind()
          } else if (event.type === TouchType.Cancel) {
            this.magnifier.unbind()
          }
        }
      })
    }
  }
}
```

![](assets/Class%20Magnifier/file-20260514163832732-0.png)


## show
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

show(x: number, y: number): void

设置放大镜显示的组件内容相对于组件左上角的位置，设置成功后放大镜会对以该坐标点为中心的区域内容进行放大显示。


> [!NOTE]
> 当与放大镜绑定的组件自身内容发生变化时，放大镜显示内容不会自动更新，需要主动调用show接口对放大镜显示内容进行更新。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 放大镜显示的组件内容相对组件水平方向坐标，单位为vp。当坐标值大于组件宽度或小于0时不显示放大镜；将值设为undefined时保持放大镜的当前显示状态。 |
| y | number | 是 | 放大镜显示的组件内容相对组件垂直方向坐标，单位为vp。当坐标值大于组件高度或小于0时不显示放大镜；将值设为undefined时保持放大镜的当前显示状态。 |


**示例：**

请参考[bind](#bind)示例。


## unbind
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

unbind(): void

解除放大镜与当前组件的绑定。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

请参考[bind](#bind)示例。
