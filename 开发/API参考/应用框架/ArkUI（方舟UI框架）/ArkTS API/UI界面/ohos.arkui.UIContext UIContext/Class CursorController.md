# Class (CursorController)

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-cursorcontroller
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

提供光标样式设置的能力。


## restoreDefault12+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

restoreDefault(): void

恢复默认的光标样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

当光标移出绿框时，通过CursorController的restoreDefault方法恢复默认光标样式。


```ts
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

![](assets/Class%20CursorController/file-20260514163830948-0.gif)


## setCursor12+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setCursor(value: PointerStyle): void

更改当前的鼠标光标样式。


> [!NOTE]
> 该接口调用后不会立即生效，而是在下一帧改变鼠标光标样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PointerStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-t#pointerstyle12) | 是 | 光标样式。 |


**示例：**

当光标进入蓝框时，通过CursorController的setCursor方法修改光标样式为PointerStyle.WEST。


```ts
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

![](assets/Class%20CursorController/file-20260514163830948-1.gif)
