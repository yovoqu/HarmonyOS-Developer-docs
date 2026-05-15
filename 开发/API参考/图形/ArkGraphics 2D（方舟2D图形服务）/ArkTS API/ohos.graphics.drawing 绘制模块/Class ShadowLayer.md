# Class (ShadowLayer)

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-shadowlayer
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

阴影层对象。


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```ts
import { drawing } from '@kit.ArkGraphics2D';
```


## create12+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static create(blurRadius: number, x: number, y: number, color: common2D.Color): ShadowLayer

创建阴影层对象。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blurRadius | number | 是 | 阴影的半径，必须为大于零的浮点数。 |
| x | number | 是 | x轴上的偏移点，该参数为浮点数。 |
| y | number | 是 | Y轴上的偏移点，该参数为浮点数。 |
| color | [common2D.Color](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-graphics-common2d#color) | 是 | ARGB格式的颜色，每个颜色通道的值是0到255之间的整数。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| [ShadowLayer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-shadowlayer) | 返回创建的阴影层对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed. |


**示例：**


```ts
import { RenderNode } from '@kit.ArkUI';
import { common2D, drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context: DrawContext) {
    const canvas = context.canvas;
    let color: common2D.Color = {
      alpha: 0xff,
      red: 0x00,
      green: 0xff,
      blue: 0x00,
    };
    let shadowLayer = drawing.ShadowLayer.create(3, -3, 3, color);
  }
}
```


## create18+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static create(blurRadius: number, x: number, y: number, color: common2D.Color | number): ShadowLayer

创建阴影层对象。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blurRadius | number | 是 | 阴影的半径，必须为大于零的浮点数。 |
| x | number | 是 | x轴上的偏移点，该参数为浮点数。 |
| y | number | 是 | Y轴上的偏移点，该参数为浮点数。 |
| color | [common2D.Color](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-graphics-common2d#color) \| number | 是 | 颜色，可以用16进制ARGB格式的无符号整数表示。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| [ShadowLayer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-shadowlayer) | 返回创建的阴影层对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed. |


**示例：**


```ts
import { RenderNode } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context: DrawContext) {
    const canvas = context.canvas;
    let shadowLayer = drawing.ShadowLayer.create(3, -3, 3, 0xff00ff00);
  }
}
```
