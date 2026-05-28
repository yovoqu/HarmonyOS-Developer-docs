# Class (FontSizeAnimation)

更新时间：2026-05-18 03:44:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-fontsizeanimation
**支持设备：** Phone | PC/2in1 | Tablet | Wearable

##### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

```text
import { map } from '@kit.MapKit';
```
 
  

##### FontSizeAnimation

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

控制字体大小的动画类，继承[Animation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-animation)。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 4.1.0(11)
 
  

##### constructor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

constructor(fromSize: number, toSize: number)
 
创建一个控制字体大小的动画实例，通过指定起始字体大小和目标字体大小来初始化该动画。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 4.1.0(11)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fromSize | number | 是 | 起始的字体大小。取值范围：[0，100]，单位：px，异常值不处理。 |
| toSize | number | 是 | 目标的字体大小。取值范围：[0，100]，单位：px，异常值不处理。 |
 
 
**示例：**
 
```text
let animation: map.FontSizeAnimation = new map.FontSizeAnimation(5, 25);
```
