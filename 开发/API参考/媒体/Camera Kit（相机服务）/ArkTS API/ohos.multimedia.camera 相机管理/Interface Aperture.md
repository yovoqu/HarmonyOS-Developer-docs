# Interface (Aperture)

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-aperture
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

Aperture继承自[ApertureQuery](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-aperturequery)。
 
物理光圈对象。
 
> [!NOTE]
> 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 本Interface首批接口从API version 24开始支持。

  

##### 导入模块

```text
import { camera } from '@kit.CameraKit';
```
 
  

##### getPhysicalAperture24+

getPhysicalAperture(): number
 
获取当前物理光圈值。
 
**元服务API：** 从API version 24开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Multimedia.Camera.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| number | 当前物理光圈值。 |
 
 
**错误码：**
 
以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 7400102 | Operation not allowed, the inputDevice or the session is abnormal. |
| 7400103 | Session not config. |
 
 
**示例：**
 
```text
import { BusinessError } from '@kit.BasicServicesKit';

function getPhysicalAperture(photoSession: camera.PhotoSession): number {
  let aperture = 0.0;
  try {
    aperture = photoSession.getPhysicalAperture();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getPhysicalAperture call failed. error code: ${err.code}`);
  }
  return aperture;
}
```
 
  

##### setPhysicalAperture24+

setPhysicalAperture(aperture: number): void
 
设置物理光圈值。
 
**元服务API：** 从API version 24开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Multimedia.Camera.Core
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| aperture | number | 是 | 物理光圈值。 |
 
 
**错误码：**
 
以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 7400102 | Operation not allowed, the inputDevice or the session is abnormal. |
| 7400103 | Session not config. |
 
 
**示例：**
 
```text
import { BusinessError } from '@kit.BasicServicesKit';

function setPhysicalAperture(photoSession: camera.PhotoSession, aperture: number): void {
  try {
    photoSession.setPhysicalAperture(aperture);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The setPhysicalAperture call failed. error code: ${err.code}`);
  }
}
```
