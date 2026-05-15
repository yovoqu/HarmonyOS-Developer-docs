# Interface (ImageReceiver)

更新时间：2026-04-28 03:31:56

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagereceiver
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

ImageReceiver类，用于获取组件surface id、接收最新的图片和读取下一张图片以及释放ImageReceiver实例。ImageReceiver作为图片的接收方和消费者，其参数属性实际上不会对接收到的图片产生影响。图片属性的配置应在发送方和生产者上进行，如相机预览流[createPreviewOutput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-cameramanager#createpreviewoutput)。

在调用以下方法前需要先通过[image.createImageReceiver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-f#imagecreateimagereceiver11)创建ImageReceiver实例。

从API version 23开始，更推荐使用[image.createImageReceiver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-f#imagecreateimagereceiver23)，通过传入[ImageReceiverOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-i#imagereceiveroptions23)创建ImageReceiver实例。

由于图片占用内存较大，所以当ImageReceiver实例使用完成后，应主动调用[release](#release9)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```ts
import { image } from '@kit.ImageKit';
```


## 属性
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver


| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| size9+ | [Size](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-i#size) | 是 | 否 | 图片大小。该参数不会影响接收到的图片大小，实际返回大小由生产者决定，如相机。 |
| capacity9+ | number | 是 | 否 | 同时访问的图像数。该参数仅作为期望值，实际capacity由设备硬件决定。 |
| format9+ | [ImageFormat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-e#imageformat9) | 是 | 否 | 图像格式，取值为[ImageFormat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-e#imageformat9)常量（目前仅支持 ImageFormat:JPEG，实际返回格式由生产者决定，如相机）。 |


## getReceivingSurfaceId9+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getReceivingSurfaceId(callback: AsyncCallback<string>): void

用于获取一个surface id供Camera或其他组件使用。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;string&gt; | 是 | 回调函数，当获取surface id成功，err为undefined，data为获取到的surface id；否则为错误对象。 |


**示例:**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

async function GetReceivingSurfaceId(receiver: image.ImageReceiver) {
  receiver.getReceivingSurfaceId((err: BusinessError, id: string) => {
    if (err) {
      console.error(
        `Failed to get the ReceivingSurfaceId.code ${err.code},message is ${err.message}`,
      );
    } else {
      console.info('Succeeded in getting the ReceivingSurfaceId.');
    }
  });
}
```


## getReceivingSurfaceId9+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getReceivingSurfaceId(): Promise<string>

用于获取一个surface id供Camera或其他组件使用。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回surface id。 |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

async function GetReceivingSurfaceId(receiver: image.ImageReceiver) {
  receiver
    .getReceivingSurfaceId()
    .then((id: string) => {
      console.info('Succeeded in getting the ReceivingSurfaceId.');
    })
    .catch((error: BusinessError) => {
      console.error(
        `Failed to get the ReceivingSurfaceId.code ${error.code},message is ${error.message}`,
      );
    });
}
```


## readLatestImage9+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

readLatestImage(callback: AsyncCallback<Image>): void

从ImageReceiver读取最新的图片。使用callback异步回调。

![图片](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/p20dGBc8Quq3JSxrCmwYnA/caution_3.0-zh-cn.png?HW-CC-KV=V1&amp;HW-CC-Date=20260514T084900Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=79D76CCE1C62683683566CD0F2C54EBCB1E0CC899E0FB96F837E59C65E20BCBA)
此接口需要在[on](#on9)回调触发后调用，才能正常的接收到数据。且此接口返回的[Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-image)对象使用完毕后需要调用[release](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-image#release9)方法释放，释放后才可以继续接收新的数据。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;[Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-image)&gt; | 是 | 回调函数，当读取最新图片成功，err为undefined，data为获取到的最新图片；否则为错误对象。 |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

async function ReadLatestImage(receiver: image.ImageReceiver) {
  receiver.readLatestImage((err: BusinessError, img: image.Image) => {
    if (err) {
      console.error(
        `Failed to read the latest Image.code ${err.code},message is ${err.message}`,
      );
    } else {
      console.info('Succeeded in reading the latest Image.');
    }
  });
}
```


## readLatestImage9+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

readLatestImage(): Promise<Image>

从ImageReceiver读取最新的图片。使用Promise异步回调。

![图片](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/M00XSDETTH2emgHE3phiwg/caution_3.0-zh-cn.png?HW-CC-KV=V1&amp;HW-CC-Date=20260514T084900Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0D06451B0044A7EF4A9FBA0AF2E6D7C2E73BD8431E61F49CEB6A7D3CA2713CBB)
此接口需要在[on](#on9)回调触发后调用，才能正常的接收到数据。且此接口返回的[Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-image)对象使用完毕后需要调用[release](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-image#release9)方法释放，释放后才可以继续接收新的数据。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;[Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-image)&gt; | Promise对象，返回最新图片。 |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

async function ReadLatestImage(receiver: image.ImageReceiver) {
  receiver
    .readLatestImage()
    .then((img: image.Image) => {
      console.info('Succeeded in reading the latest Image.');
    })
    .catch((error: BusinessError) => {
      console.error(
        `Failed to read the latest Image.code ${error.code},message is ${error.message}`,
      );
    });
}
```


## readNextImage9+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

readNextImage(callback: AsyncCallback<Image>): void

从ImageReceiver读取下一张图片。使用callback异步回调。

![图片](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/Trv9-jlzSOy_d_RGNnXetQ/caution_3.0-zh-cn.png?HW-CC-KV=V1&amp;HW-CC-Date=20260514T084900Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=61B6F2586BAD1B9F6DC43A2AD26FF2FC3C204D22D6EE62D719A29B419DB9B7BE)
此接口需要在[on](#on9)回调触发后调用，才能正常的接收到数据。且此接口返回的[Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-image)对象使用完毕后需要调用[release](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-image#release9)方法释放，释放后才可以继续接收新的数据。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;[Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-image)&gt; | 是 | 回调函数，当获取下一张图片成功，err为undefined，data为获取到的下一张图片；否则为错误对象。 |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

async function ReadNextImage(receiver: image.ImageReceiver) {
  receiver.readNextImage((err: BusinessError, img: image.Image) => {
    if (err) {
      console.error(
        `Failed to read the next Image.code ${err.code},message is ${err.message}`,
      );
    } else {
      console.info('Succeeded in reading the next Image.');
    }
  });
}
```


## readNextImage9+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

readNextImage(): Promise<Image>

从ImageReceiver读取下一张图片。使用Promise异步回调。

![图片](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/agHfeL0mSg-ldtP-5-HDGg/caution_3.0-zh-cn.png?HW-CC-KV=V1&amp;HW-CC-Date=20260514T084900Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E63AC94655A7E86E18897684DFD37E54115F6248FC4B4B4E6D45177980A2979)
此接口需要在[on](#on9)回调触发后调用，才能正常的接收到数据。且此接口返回的[Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-image)对象使用完毕后需要调用[release](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-image#release9)方法释放，释放后才可以继续接收新的数据。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;[Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-image)&gt; | Promise对象，返回下一张图片。 |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

async function ReadNextImage(receiver: image.ImageReceiver) {
  receiver
    .readNextImage()
    .then((img: image.Image) => {
      console.info('Succeeded in reading the next Image.');
    })
    .catch((error: BusinessError) => {
      console.error(
        `Failed to read the next Image.code ${error.code},message is ${error.message}`,
      );
    });
}
```


## on9+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

on(type: 'imageArrival', callback: AsyncCallback<void>): void

接收图片时注册回调。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 注册事件的类型，固定为'imageArrival'，接收图片到达时触发。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数，当注册事件触发成功，err为undefined，否则为错误对象。 |


**示例：**


```ts
async function On(receiver: image.ImageReceiver) {
  receiver.on('imageArrival', () => {
    // 接收到图片，实现回调函数逻辑。
  });
}
```


## off13+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

off(type: 'imageArrival', callback?: AsyncCallback<void>): void

释放buffer时移除注册回调。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 注册事件的类型，固定为'imageArrival'，释放buffer时触发。 |
| callback | AsyncCallback&lt;void&gt; | 否 | 移除的回调函数。 |


**示例：**


```ts
async function Off(receiver: image.ImageReceiver) {
  let callbackFunc = () => {
    // 实现回调函数逻辑。
  };
  receiver.on('imageArrival', callbackFunc);
  receiver.off('imageArrival', callbackFunc);
}
```


## release9+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

release(callback: AsyncCallback<void>): void

释放ImageReceiver实例。使用callback异步回调。

由于图片占用内存较大，所以当ImageReceiver实例使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数，当释放ImageReceiver实例成功，err为undefined，否则为错误对象。 |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(receiver: image.ImageReceiver) {
  receiver.release((err: BusinessError) => {
    if (err) {
      console.error(
        `Failed to release the receiver.code ${err.code},message is ${err.message}`,
      );
    } else {
      console.info('Succeeded in releasing the receiver.');
    }
  });
}
```


## release9+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

release(): Promise<void>

释放ImageReceiver实例。使用Promise异步回调。

由于图片占用内存较大，所以当ImageReceiver实例使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(receiver: image.ImageReceiver) {
  receiver
    .release()
    .then(() => {
      console.info('Succeeded in releasing the receiver.');
    })
    .catch((error: BusinessError) => {
      console.error(
        `Failed to release the receiver.code ${error.code},message is ${error.message}`,
      );
    });
}
```
