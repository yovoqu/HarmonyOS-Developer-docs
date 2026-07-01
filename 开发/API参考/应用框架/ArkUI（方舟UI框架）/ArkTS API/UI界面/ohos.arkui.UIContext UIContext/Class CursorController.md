# Class (CursorController)

更新时间：2026-06-13 03:51:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-cursorcontroller
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

提供光标样式设置的能力。

> [!NOTE]
> 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 本Class首批接口从API version 12开始支持。 本模块接口仅可在Stage模型下使用。 以下API需先使用UIContext中的 getCursorController() 方法获取CursorController实例，再通过此实例调用对应方法。



#### restoreDefault12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

restoreDefault(): void

恢复默认的光标样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

当光标移出绿框时，通过CursorController的restoreDefault方法恢复默认光标样式。

```text
import { pointer } from '@kit.InputKit';
import { UIContext, CursorController } from '@kit.ArkUI';

@Entry
@Component
struct CursorControlExample {
  @State text: string = '';
  cursorCustom: CursorController = this.getUIContext().getCursorController();

  build() {
    Column() {
      Row().height(200).width(200).backgroundColor(Color.Green).position({x: 150 ,y:70})
        .onHover((flag) => {
          if (flag) {
            this.cursorCustom.setCursor(pointer.PointerStyle.EAST);
          } else {
            console.info("restoreDefault");
            this.cursorCustom.restoreDefault();
          }
        })
    }.width('100%')
  }
}
```


![](assets/Class%20CursorController/file-20260514163830948-1.gif)




#### setCursor12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setCursor(value: PointerStyle): void

更改当前的鼠标光标样式。

> [!NOTE]
> 该接口调用后不会立即生效，而是在下一帧改变鼠标光标样式。


**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | PointerStyle | 是 | 光标样式。 |


**示例：**

当光标进入蓝框时，通过CursorController的setCursor方法修改光标样式为PointerStyle.WEST。

```text
import { pointer } from '@kit.InputKit';
import { UIContext, CursorController } from '@kit.ArkUI';

@Entry
@Component
struct CursorControlExample {
  @State text: string = '';
  cursorCustom: CursorController = this.getUIContext().getCursorController();

  build() {
    Column() {
      Row().height(200).width(200).backgroundColor(Color.Blue).position({x: 100 ,y:70})
        .onHover((flag) => {
          if (flag) {
            this.cursorCustom.setCursor(pointer.PointerStyle.WEST);
          } else {
            this.cursorCustom.restoreDefault();
          }
        })
    }.width('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/DLnrc2gvRASi0g2Ee8Au5g/zh-cn_image_0000002659101479.gif?HW-CC-KV=V1&HW-CC-Date=20260701T014312Z&HW-CC-Expire=86400&HW-CC-Sign=6A31F95748A12E563A72AF943EB9BD4A65D69EB64E11F8FDAC159A61890A8BCC)




#### setCustomCursor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setCustomCursor(value: image.PixelMap, focusX?: number, focusY?: number): void

设置自定义鼠标光标样式。

> [!NOTE]
> 该接口调用后不会立即生效，而是在下一帧改变鼠标光标样式。 仅支持设置静态图片，不支持设置动态图片。


**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | image.PixelMap | 是 | 自定义鼠标光标样式的像素图。最大尺寸为256*256px，超过该尺寸时，本次设置不会生效，鼠标光标保持当前样式不变。 |
| focusX | number | 否 | 自定义光标焦点的X坐标。以光标图片左上角为原点，向右为正方向。该焦点将在显示时与系统鼠标指针的屏幕坐标对齐，鼠标的点击、拖拽等操作均以此点为准。 默认值：0 单位：px 取值范围：[0, 图片宽度]，超出取值范围时按默认值处理。 |
| focusY | number | 否 | 自定义光标焦点的Y坐标。以光标图片左上角为原点，向下为正方向。结合focusX共同确定图像内代表实际交互位置的点。 默认值：0 单位：px 取值范围：[0, 图片高度]，超出取值范围时按默认值处理。 |


**示例：**

该示例通过调用[setCustomCursor](#setcustomcursor)接口，设置自定义鼠标光标样式。

从API版本26.0.0开始，新增setCustomCursor接口。

```text
import { image } from '@kit.ImageKit';
import { CursorController } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct CustomCursorExample {
  cursorController: CursorController = this.getUIContext().getCursorController();
  @State pixelMap: image.PixelMap | undefined = undefined;

  async loadPixelMapFromRawFile(): Promise<void> {
    try {
      // 1.获取资源管理器，添加空值检查
      const uiContext = this.getUIContext();
      if (!uiContext) {
        console.error('UIContext is undefined');
        return;
      }
      const context = uiContext.getHostContext();
      if (!context) {
        console.error('HostContext is undefined');
        return;
      }
      const resourceMgr = context.resourceManager;
      if (!resourceMgr) {
        console.error('ResourceManager is undefined');
        return;
      }
      // 2.读取rawfile中的图片文件
      const fileData: Uint8Array = await resourceMgr.getRawFileContent('cursor.png');
      const buffer = fileData.buffer.slice(0);
      // 3.创建ImageSource
      const imageSource = image.createImageSource(buffer);
      // 4.创建PixelMap（可以指定期望的尺寸）
      const pixelMap = await imageSource.createPixelMap({
        desiredSize: { width: 32, height: 32 }
      });
      this.pixelMap = pixelMap;
      console.info('Custom cursor loaded successfully');
    } catch (error) {
      let err = error as BusinessError;
      console.error(`Failed to load cursor: ${err.code}, ${err.message}`);
    }
  }

  build() {
    Column() {
      Button('load image')
        .width("40%")
        .height('7%')
        .fontSize('30vp')
        .margin(70)
        .backgroundColor(Color.Blue)
        .onClick(() => {
          // 点击按钮加载PixelMap
          this.loadPixelMapFromRawFile();
        })
      Row()
        .height(200)
        .width(200)
        .backgroundColor(Color.Blue)
        .onHover((isHover: boolean) => {
          if (isHover && this.pixelMap != undefined) {
            // 设置自定义鼠标光标样式，焦点位置设为(16, 16)，即光标中心
            this.cursorController.setCustomCursor(this.pixelMap, 16, 16);
          } else {
            this.cursorController.restoreDefault();
          }
        })
    }
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
    .width('100%')
    .height('100%')
  }

  aboutToDisappear(): void {
    // 释放PixelMap资源
    if (this.pixelMap) {
      this.pixelMap.release();
      this.pixelMap = undefined;
    }
    this.cursorController.restoreDefault();
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/w9AI1U3kReyIaiixEczO7Q/zh-cn_image_0000002628862130.gif?HW-CC-KV=V1&HW-CC-Date=20260701T014312Z&HW-CC-Expire=86400&HW-CC-Sign=6E6E25FA9C5253CCEAA39002F2BA7962B96E6E474AB918446409E46AA995BE94)
