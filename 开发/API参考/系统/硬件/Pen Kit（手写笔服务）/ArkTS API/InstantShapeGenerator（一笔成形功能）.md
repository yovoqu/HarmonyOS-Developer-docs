# InstantShapeGenerator（一笔成形功能）

更新时间：2026-05-19 09:13:51

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-instantsshapegenerator
**支持设备：** Phone | PC/2in1 | Tablet

一笔成形的功能入口类。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.Stylus.Handwrite
 
**起始版本：** 5.0.0(12)
  

#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet

```text
import { InstantShapeGenerator, ShapeInfo } from '@kit.Penkit';
```
 
本模块提供以下类或接口，支持获取一笔成形的图像。
  
| 名称 | 类型 | 说明 |
| --- | --- | --- |
| ShapeInfo | ShapeInfo | 一笔成形识别结果对象，包含识别的图像的基本信息。 |
 
 
本模块提供以下方法。
  
| 方法名称 | 说明 |
| --- | --- |
| processTouchEvent | 传递触摸事件。 |
| getPathFromString | 从给定的形状字符串中提取形状信息。 |
| notifyAreaChange | 通知控件大小变化。 |
| setPauseTime | 设置触发识别的暂停时间，单位：ms。 |
| release | 销毁识别工具。 |
| onShapeRecognized | 注册识别完成时的回调方法。使用callback异步回调。 |
 
 
  

#### ShapeInfo

**支持设备：** Phone | PC/2in1 | Tablet

一笔成形识别结果对象，包含识别的图像的基本信息。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.Stylus.Handwrite
 
**起始版本：** 5.0.0(12)
 
**参数**：
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| shapePath | Path2D | 否 | 否 | 图形对象。 |
| shapeString | string | 否 | 否 | 图形信息，可以用于保存的。 |
| shapeType | number | 否 | 否 | 图形类型。 - 未知类型（识别失败）- 0 - 直线 - 1 - 圆（椭圆）- 2 - 折线 - 3 - 矩形 - 6 - 平行四边形 - 7 - 菱形 - 9 - 等腰三角形 - 10 - 等边三角形 - 11 - 五角星形 - 12 - 正五边形 - 13 - 抛物线形 - 14 - 直线单向箭头（箭头指向起点） - 15 - 直线单向箭头（箭头指向终点）- 16 - 直线双向箭头 - 17 - 抛物线单向箭头（箭头指向起点） - 18 - 抛物线单向箭头（箭头指向终点） - 19 - 抛物线双向箭头 - 20 |
 
 
**示例：**
 
```text
private shapeInfo : ShapeInfo = {
shapePath: '',
shapeString: '',
shapeType: 0
}
```
 
  

#### processTouchEvent

**支持设备：** Phone | PC/2in1 | Tablet

processTouchEvent(event: TouchEvent): void
 
传递触摸事件。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.Stylus.Handwrite
 
**起始版本：** 5.0.0(12)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | TouchEvent | 是 | 当前触摸点事件。 |
 
 
**错误码**：
 
以下错误码的详细介绍请参见[ArkTS API 错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-error-code)。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 1010410001 | internal recognition engine has been released. |
 
 
**示例：**
 
```text
instantShapeGenerator: InstantShapeGenerator = new InstantShapeGenerator();
// 画布
@Builder
Canvas() {
  Stack()
    .width('100%')
    .height('100%')
    .onTouch((event: TouchEvent) => {
      this.instantShapeGenerator?.processTouchEvent(event);
    })
}
```
 
  

#### getPathFromString

**支持设备：** Phone | PC/2in1 | Tablet

getPathFromString(shapeString: string, penSize: number): Path2D
 
从给定的形状字符串中提取形状信息，并使用该信息生成Path2D对象。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.Stylus.Handwrite
 
**起始版本：** 5.0.0(12)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| shapeString | string | 是 | 形状字符串。无取值范围限制。 |
| penSize | number | 是 | 用于绘制结果形状的笔宽。某些形状结果会根据此值而变化，例如箭头。单位：画布宽度的千分之一。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Path2D | 形状信息生成的Path2D对象。 |
 
 
**错误码**：
 
以下错误码的详细介绍请参见[ArkTS API 错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-error-code)。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 1010410001 | internal recognition engine has been released. |
 
 
**示例：**
 
```text
// 通过回调方法获取识别结果
private shapeInfoCallback(shapeInfo: ShapeInfo) {
  this.drawPath = this.instantShapeGenerator?.getPathFromString(shapeInfo.shapeString, this.penWidth);
}
```
 
  

#### notifyAreaChange

**支持设备：** Phone | PC/2in1 | Tablet

notifyAreaChange(width: number, height: number): void
 
通知组件大小更改。形状的大小（例如圆的半径）根据组件尺寸而变化。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.Stylus.Handwrite
 
**起始版本：** 5.0.0(12)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 组件变更后的宽度。单位：vp。 |
| height | number | 是 | 组件变更后的高度。单位：vp。 |
 
 
**错误码**：
 
以下错误码的详细介绍请参见[ArkTS API 错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-error-code)。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 1010410001 | internal recognition engine has been released. |
 
 
**示例：**
 
```text
// 画布
@Builder Canvas() {
  Stack()
    .width('100%')
    .height('100%')
    .onAreaChange((oldValue, newValue) => {
    this.instantShapeGenerator?.notifyAreaChange(Number(newValue.width), Number(newValue.height));
  })
}
```
 
  

#### setPauseTime

**支持设备：** Phone | PC/2in1 | Tablet

setPauseTime(time: number): void
 
设置触发识别的暂停时间。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.Stylus.Handwrite
 
**起始版本：** 5.0.0(12)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| time | number | 是 | 触发识别的暂停时间。 单位：ms。 |
 
 
**错误码**：
 
以下错误码的详细介绍请参见[ArkTS API 错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-error-code)。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 1010410001 | internal recognition engine has been released. |
 
 
**示例：**
 
```text
aboutToAppear() {
  console.info('InstantShapeGenerator aboutToAppear')
  try {
    this.instantShapeGenerator?.setPauseTime(280);
  } catch (error) {
    console.error('setPauseTime failed: ', error);
  }
}
```
 
  

#### release

**支持设备：** Phone | PC/2in1 | Tablet

release(): void
 
销毁一笔成形工具。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.Stylus.Handwrite
 
**起始版本：** 5.0.0(12)
 
**示例：**
 
```text
aboutToDisappear(){
  console.info('InstantShapeGenerator aboutToDisappear');
  this.instantShapeGenerator?.release();
}
```
 
  

#### onShapeRecognized

**支持设备：** Phone | PC/2in1 | Tablet

onShapeRecognized(callback: Callback&lt;ShapeInfo&gt;): [InstantShapeGenerator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-instantsshapegenerator)
 
注册识别完成时的回调方法。使用callback异步回调。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.Stylus.Handwrite
 
**起始版本：** 5.0.0(12)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;ShapeInfo&gt; | 是 | 回调函数，返回一笔成形识别结果对象，包含识别的图像的基本信息。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| InstantShapeGenerator | 一笔成形工具方法类实例。 |
 
 
**示例：**
 
```text
// 通过回调方法获取识别结果
private shapeInfoCallback(shapeInfo: ShapeInfo) {
  this.shapeInfo = shapeInfo;
}

aboutToAppear() {
  console.info('InstantShapeGenerator aboutToAppear')
  this.instantShapeGenerator?.onShapeRecognized(this.shapeInfoCallback)
}
```
