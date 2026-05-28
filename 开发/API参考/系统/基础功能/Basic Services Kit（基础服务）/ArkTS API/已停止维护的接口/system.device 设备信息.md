# @system.device (设备信息)

更新时间：2026-05-14 10:06:22

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-device
**支持设备：** Wearable | lite_wearable

本模块提供当前设备的信息。
 
> [!NOTE]
> 模块维护策略 - 对于Lite Wearable设备类型，该模块长期维护，正常使用。 - 对于支持该模块的其他设备类型，该模块从API Version 6开始不再维护，推荐使用新接口 @ohos.deviceInfo 进行设备信息查询。 本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

  

##### 导入模块

**支持设备：** Wearable | lite_wearable

```text
import device from '@system.device';
```
 
  

##### device.getInfo(deprecated)

**支持设备：** Wearable | lite_wearable

getInfo(options?: GetDeviceOptions): void
 
获取当前设备的信息。
 
> [!NOTE]
> 在首页的onShow生命周期之前不建议调用device.getInfo接口。

 
**系统能力：** SystemCapability.Startup.SystemInfo.Lite
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | GetDeviceOptions | 否 | 定义设备信息获取的参数选项。 |
 
 
**示例：**
 
ArkTS示例：
 
```text
export default class Page {
  getInfo() {
    interface DeviceData {
      brand: string;
    }

    try {
      device.getInfo({
        success: (data: DeviceData) => {
          console.info('Device information obtained successfully. Device brand:' + data.brand);
        },
        fail: (data: string, code: number) => {
          console.info('Failed to obtain device information. Error code:' + code + '; Error information: ' + data);
        },
      });
    } catch (error) {
      console.error('Device information API is not supported');
    }
  }
}
```
 
JS示例：
 
```xml
<div class="container">
    <text class="title">Device Information</text>
    <input type="button" value="Get Device Brand" class="button" onclick="getDeviceInfo"></input>
    <text class="info">{{brandInfo}}</text>
</div>
```
 
```text
/*xxx.css*/
.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    left: 0px;
    top: 0px;
    width: 100%;
    height: 100%;
}

.title {
    font-size: 40px;
    text-align: center;
    width: 100%;
    height: 80px;
    margin-bottom: 50px;
}

.button {
    font-size: 30px;
    text-align: center;
    width: 240px;
    height: 80px;
    margin: 20px;
}

.info {
    font-size: 28px;
    text-align: center;
    width: 100%;
    height: 60px;
    margin-top: 50px;
    color: #007dff;
}
```
 
```text
//xxx.js
import device from '@system.device';

export default {
    data: {
        brandInfo: 'Click the button to get device brand'
    },
    
    getDeviceInfo() {
        try {
            device.getInfo({
                success: (data) => {
                    console.info('Device information obtained successfully. Device brand:' + data.brand);
                    this.brandInfo = 'Device brand: ' + data.brand;
                },
                fail: (data, code) => {
                    console.info('Failed to obtain device information. Error code:' + code + '; Error information: ' + data);
                    this.brandInfo = 'Failed to obtain, error code: ' + code;
                },
            });
        } catch (error) {
            console.error('Device information API is not supported');
            this.brandInfo = 'Current device does not support this API';
        }
    }
}
```
 
  

##### GetDeviceOptions(deprecated)

**支持设备：** Wearable | lite_wearable

定义设备信息获取的参数选项。
 
**系统能力：** SystemCapability.Startup.SystemInfo.Lite
  
| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | (data: DeviceResponse) => void | 否 | 接口调用成功的回调函数。 data为成功返回的设备信息，具体参考DeviceResponse。 |
| fail | (data: any,code:number)=> void | 否 | 接口调用失败的回调函数。 code为失败返回的错误码。 code:200，表示返回结果中存在无法获得的信息。 |
| complete | () => void | 否 | 接口调用结束的回调函数。 |
 
 
  

##### DeviceResponse(deprecated)

**支持设备：** Wearable | lite_wearable

设备信息。
 
**系统能力：** SystemCapability.Startup.SystemInfo.Lite
  
| 名称 | 类型 | 说明 |
| --- | --- | --- |
| brand | string | 品牌。 |
| manufacturer | string | 生产商。 |
| model | string | 型号。 |
| product | string | 代号。 |
| language4+ | string | 系统语言。 |
| region4+ | string | 系统地区。 |
| windowWidth | number | 可使用的窗口宽度，单位px。 |
| windowHeight | number | 可使用的窗口高度，单位px。 |
| screenDensity4+ | number | 屏幕密度，单位dpi。 |
| screenShape4+ | string | 屏幕形状。可取值： - rect：方形屏； - circle：圆形屏。 |
| apiVersion4+ | number | 系统API版本号。 |
| deviceType4+ | string | 设备类型。 |
