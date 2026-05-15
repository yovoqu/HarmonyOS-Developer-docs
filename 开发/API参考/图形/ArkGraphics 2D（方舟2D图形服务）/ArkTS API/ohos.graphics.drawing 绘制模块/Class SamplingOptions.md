# Class (SamplingOptions)

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-samplingoptions
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

采样选项对象。


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```ts
import { drawing } from '@kit.ArkGraphics2D';
```


## constructor12+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

constructor()

构造一个新的采样选项对象，[FilterMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-e#filtermode12)的默认值为FILTER_MODE_NEAREST。

**系统能力：** SystemCapability.Graphics.Drawing

**示例：**


```ts
import { RenderNode } from '@kit.ArkUI';
import { common2D, drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context: DrawContext) {
    const canvas = context.canvas;
    const pen = new drawing.Pen();
    let samplingOptions = new drawing.SamplingOptions();
  }
}
```


## constructor12+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

constructor(filterMode: FilterMode)

构造一个新的采样选项对象。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filterMode | [FilterMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-e#filtermode12) | 是 | 过滤模式。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |


**示例：**


```ts
import { RenderNode } from '@kit.ArkUI';
import { common2D, drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context: DrawContext) {
    const canvas = context.canvas;
    let samplingOptions = new drawing.SamplingOptions(
      drawing.FilterMode.FILTER_MODE_NEAREST,
    );
  }
}
```
