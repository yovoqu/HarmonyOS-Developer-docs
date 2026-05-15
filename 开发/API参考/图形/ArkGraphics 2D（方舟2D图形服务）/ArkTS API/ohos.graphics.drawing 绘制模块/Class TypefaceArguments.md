# Class (TypefaceArguments)

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-typefacearguments
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

提供字体属性配置的结构体。


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```ts
import { drawing } from '@kit.ArkGraphics2D';
```


## constructor20+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

constructor()

字体属性的构造函数。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**示例：**


```ts
import { drawing } from '@kit.ArkGraphics2D';
let typeFaceArgument = new drawing.TypefaceArguments();
```


## addVariation20+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

addVariation(axis: string, value: number)

给字体属性设置字重值。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| axis | string | 是 | 字体属性对象可变维度字重的标签'wght'。具体是否支持的该标签取决于加载的字体文件。请打开对应的字体文件具体查看支持的属性。 |
| value | number | 是 | 字体属性对象可变维度字重的标签'wght'对应的属性值，需要在字体文件支持的范围内，否则不会生效。如果属性值小于支持的最小值，则默认和最小值一致。如果属性值大于支持的最大值，则默认和最大值效果一致。请打开对应的字体文件具体查看支持的属性值。 |


**错误码：**

以下错误码的详细介绍请参见[图形绘制与显示错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-drawing)。


| 错误码ID | 错误信息 |
| --- | --- |
| 25900001 | Parameter error.Possible causes: Incorrect parameter range. |


**示例：**


```ts
import { drawing } from '@kit.ArkGraphics2D';

let typeFaceArgument = new drawing.TypefaceArguments();
typeFaceArgument.addVariation('wght', 10);
```
