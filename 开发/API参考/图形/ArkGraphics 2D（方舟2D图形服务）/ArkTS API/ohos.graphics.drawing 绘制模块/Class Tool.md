# Class (Tool)

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-tool
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

本模块定义的工具类，仅提供静态的方法，主要完成其他模块和[common2D](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-graphics-common2d)中定义的数据结构的转换功能等操作。


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```ts
import { drawing } from '@kit.ArkGraphics2D';
```


## makeColorFromResourceColor15+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static makeColorFromResourceColor(resourceColor: ResourceColor): common2D.Color

将ResourceColor类型的值转换为common2D.Color对象。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resourceColor | [ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor) | 是 | ResourceColor格式的颜色值（支持所有的4种输入，示例中提供13个示例输入）。其中第4种类型[Resource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resource)只接受\$r('belonging.type.name')构造方法，需要确保该资源在main/resources/base/element目录下已定义(app支持color、string和integer，sys只支持color)。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| [common2D.Color](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-graphics-common2d#color) | 转换后的common2D.Color颜色对象，若转换失败则返回空指针。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |


**示例：**


```ts
import { drawing, common2D } from '@kit.ArkGraphics2D';

// Color
let color1: common2D.Color = drawing.Tool.makeColorFromResourceColor(
  Color.Blue,
);

// Number
let color2: common2D.Color = drawing.Tool.makeColorFromResourceColor(0xffc0cb);
let color3: common2D.Color =
  drawing.Tool.makeColorFromResourceColor(0x11ffa500);

// String
let color4: common2D.Color = drawing.Tool.makeColorFromResourceColor('#ff0000');
let color5: common2D.Color =
  drawing.Tool.makeColorFromResourceColor('#110000ff');
let color6: common2D.Color = drawing.Tool.makeColorFromResourceColor('#00f');
let color7: common2D.Color = drawing.Tool.makeColorFromResourceColor('#100f');
let color8: common2D.Color =
  drawing.Tool.makeColorFromResourceColor('rgb(255, 100, 255)');
let color9: common2D.Color = drawing.Tool.makeColorFromResourceColor(
  'rgba(255, 100, 255, 0.5)',
);

// Resource
let color10: common2D.Color = drawing.Tool.makeColorFromResourceColor(
  $r('sys.color.ohos_id_color_secondary'),
);

// Use color
let brush = new drawing.Brush();
brush.setColor(color1);
```
