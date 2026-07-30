# Class (Magnifier)

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-magnifier
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

提供控制放大镜的显示与隐藏的能力，放大镜会对组件内容进行放大显示，便于查看组件细节。适用于非文本类组件（如图片）需要查看细节的场景。
 
> [!NOTE]
> 本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 本Class首批接口从API version 22开始支持。 以下API需先使用UIContext中的 getMagnifier() 方法获取Magnifier实例，再通过此实例调用对应方法。 与文本类组件自带的放大镜能力互不影响，文本类组件推荐使用自带的放大镜能力。

  

#### bind

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

bind(id: string): void
 
绑定放大镜与指定id的组件。
 
> [!NOTE]
> 使用前需先通过UIContext中的getMagnifier()方法获取Magnifier实例。

 
**元服务API：** 从API version 22开始，该接口支持在元服务中使用。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 组件id，可通过通用属性id或key设置。当组件id为空字符串或未找到匹配id的组件时，不显示放大镜。 |
 
 
**示例：**
 
该示例通过监听onTouch事件控制放大镜对图片进行放大显示。
 
```text
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
        .onTouch((event: TouchEvent) => {
          if (event && event.sourceTool === SourceTool.Finger) {
            if (event.type === TouchType.Down) {
              this.magnifier.bind('image');
            } else if (event.type === TouchType.Move) {
              let touchX = event.touches[0].x;
              let touchY = event.touches[0].y;
              this.magnifier.show(touchX, touchY);
            } else if (event.type === TouchType.Up) {
              this.magnifier.unbind();
            } else if (event.type === TouchType.Cancel) {
              this.magnifier.unbind();
            }
          }
        })
    }
  }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/3RHsMwpbRh2BDmfpp0G9Mw/zh-cn_image_0000002686087685.png?HW-CC-KV=V1&HW-CC-Date=20260730T071444Z&HW-CC-Expire=86400&HW-CC-Sign=C4605577083EDC09BDED5F5676203712BCCBF6E991CFDB830E898BA99325686C)

 
  

#### show

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

show(x: number, y: number): void
 
设置放大镜显示的组件内容相对于组件左上角的位置，设置成功后放大镜会对以该坐标点为中心的区域内容进行放大显示。
 
> [!NOTE]
> 使用前需先通过UIContext中的getMagnifier()方法获取Magnifier实例。 调用此方法前，需先调用 bind 方法绑定目标组件。 当与放大镜绑定的组件自身内容发生变化时，放大镜显示内容不会自动更新，需要主动调用show接口对放大镜显示内容进行更新。

 
**元服务API：** 从API version 22开始，该接口支持在元服务中使用。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 放大镜显示的组件内容相对于组件左上角的水平方向坐标，单位为vp。当坐标值大于组件宽度或小于0时不显示放大镜；传入undefined时不生效，保持放大镜当前的显示状态。 |
| y | number | 是 | 放大镜显示的组件内容相对于组件左上角的垂直方向坐标，单位为vp。当坐标值大于组件高度或小于0时不显示放大镜；传入undefined时不生效，保持放大镜当前的显示状态。 |
 
 
**示例：**
 
请参考[bind](#bind)示例。
 
  

#### unbind

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

unbind(): void
 
解除放大镜与当前组件的绑定。使用前需先通过UIContext中的getMagnifier()方法获取Magnifier实例。
 
**元服务API：** 从API version 22开始，该接口支持在元服务中使用。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**示例：**
 
请参考[bind](#bind)示例。
