# Interface (ImagePacker)

更新时间：2026-05-19 09:13:51

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagepacker
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

ImagePacker类，用于图片压缩和编码。

在调用ImagePacker的方法前，需要先通过[image.createImagePacker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-f#imagecreateimagepacker)构建一个ImagePacker实例。

编码期间，请避免修改或释放作为输入的ImageSource/PixelMap/Picture对象，以免出现crash或其他未定义行为。

由于图片占用内存较大，所以当ImagePacker实例使用完成后，应主动调用[release](#release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

当前支持的格式有：jpeg、webp、png、heic12+、gif18+（不同硬件设备支持情况不同，可通过ImagePacker的supportedFormats属性查看）。

> [!NOTE]
> 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。



#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { image } from '@kit.ImageKit';
```



#### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| supportedFormats | Array&lt;string&gt; | 是 | 否 | 图片编码支持的格式，包括：jpeg、webp、png、heic12+、gif18+（不同硬件设备支持情况不同）。 |




#### packToData13+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

packToData(source: ImageSource, options: PackingOption): Promise&lt;ArrayBuffer&gt;

图片压缩或重新编码。使用Promise异步回调。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | ImageSource | 是 | 编码的ImageSource。 |
| options | PackingOption | 是 | 设置编码参数。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;ArrayBuffer&gt; | Promise对象，返回压缩或编码后的数据。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Image错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-image)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the parameter is invalid. |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980101 | The image data is abnormal. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| 62980113 | Unknown image format.The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 62980119 | Failed to encode the image. |
| 62980120 | Add pixelmap out of range. |
| 62980172 | Failed to encode icc. |
| 62980252 | Failed to create surface. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

async function PackToData(context : Context) {
  // 此处'test.jpg'仅作示例，请开发者自行替换，否则imageSource会创建失败导致后续无法正常执行。
  let filePath: string = context.filesDir + "/test.jpg";
  const imageSourceObj: image.ImageSource = image.createImageSource(filePath);
  let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 }
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  imagePackerObj.packToData(imageSourceObj, packOpts)
    .then((data: ArrayBuffer) => {
      console.info('Succeeded in packing the image.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to pack the image.code ${error.code},message is ${error.message}`);
    })
}
```



#### packToData13+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

packToData(source: PixelMap, options: PackingOption): Promise&lt;ArrayBuffer&gt;

图片压缩或重新编码。使用Promise异步回调。


![](assets/Interface%20ImagePacker/file-20260525092931772-002.png)


接口如果返回401错误码，表明参数异常，可能是PixelMap对象被提前释放了。需要调用方排查，在该方法调用结束后再释放PixelMap对象。



**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | PixelMap | 是 | 编码的PixelMap源。 |
| options | PackingOption | 是 | 设置编码参数。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;ArrayBuffer&gt; | Promise对象，返回压缩或编码后的数据。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Image错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-image)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the parameter is invalid. |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980101 | The image data is abnormal. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| 62980113 | Unknown image format.The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 62980119 | Failed to encode the image. |
| 62980120 | Add pixelmap out of range. |
| 62980172 | Failed to encode icc. |
| 62980252 | Failed to create surface. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

async function PackToData() {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
  let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 4, width: 6 } }
  image.createPixelMap(color, opts).then((pixelMap: image.PixelMap) => {
    let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 }
    const imagePackerObj: image.ImagePacker = image.createImagePacker();
    imagePackerObj.packToData(pixelMap, packOpts)
      .then((data: ArrayBuffer) => {
        console.info('Succeeded in packing the image.');
      }).catch((error: BusinessError) => {
      console.error(`Failed to pack the image.code ${error.code},message is ${error.message}`);
    })
  }).catch((error: BusinessError) => {
    console.error(`Failed to create PixelMap.code ${error.code},message is ${error.message}`);
  })
}
```



#### packing13+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

packing(picture: Picture, options: PackingOption): Promise&lt;ArrayBuffer&gt;

将图像压缩或重新编码。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| picture | Picture | 是 | 编码的Picture对象。 |
| options | PackingOption | 是 | 设置编码参数。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;ArrayBuffer&gt; | Promise对象，返回压缩或编码后的数据。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Image错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-image)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 7800301 | Encode failed. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

async function Packing(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("test.jpg");
  let ops: image.SourceOptions = {
    sourceDensity: 98,
  }
  let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
  let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
  let pictureObj: image.Picture = image.createPicture(commodityPixelMap);
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  let funcName = "Packing";
  if (imagePackerObj != null) {
    let opts: image.PackingOption = {
      format: "image/jpeg",
      quality: 98,
      desiredDynamicRange: image.PackingDynamicRange.AUTO,
      needsPackProperties: true};
    await imagePackerObj.packing(pictureObj, opts).then((data: ArrayBuffer) => {
      console.info(funcName, 'Succeeded in packing the image.'+ data);
    }).catch((error: BusinessError) => {
      console.error(funcName, `Failed to pack the image.code ${error.code},message is ${error.message}`);
    });
  }
}
```



#### packToDataFromPixelmapSequence18+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

packToDataFromPixelmapSequence(pixelmapSequence: Array&lt;PixelMap&gt;, options: PackingOptionsForSequence): Promise&lt;ArrayBuffer&gt;

将多个PixelMap编码成GIF数据。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pixelmapSequence | Array&lt;PixelMap&gt; | 是 | 待编码的PixelMap序列。 |
| options | PackingOptionsForSequence | 是 | 动图编码参数。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;ArrayBuffer&gt; | Promise对象，返回编码后的数据。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Image错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-image)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 7800301 | Failed to encode image. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

async function PackToDataFromPixelmapSequence(context : Context) {
  const resourceMgr = context.resourceManager;
  // 此处'moving_test.gif'仅作示例，请开发者自行替换。否则imageSource会创建失败，导致后续无法正常执行。
  const fileData = await resourceMgr.getRawFileContent('moving_test.gif');
  const color = fileData.buffer as ArrayBuffer;
  let imageSource = image.createImageSource(color);
  let pixelMapList = await imageSource.createPixelMapList();
  let ops: image.PackingOptionsForSequence = {
    frameCount: 3,  // 指定GIF编码中的帧数为3。
    delayTimeList: [10, 10, 10],  // 指定GIF编码中3帧的延迟时间分别为100ms、100ms、100ms。
    disposalTypes: [3, 2, 3], // 指定GIF编码中3帧的帧过渡模式分别为3（恢复到之前的状态）、2（恢复背景色)、3(恢复到之前的状态)。
    loopCount: 0 // 指定GIF编码中循环次数为无限循环。
  };
  let packer = image.createImagePacker();
  packer.packToDataFromPixelmapSequence(pixelMapList, ops)
    .then((data: ArrayBuffer) => {
      console.info('Succeeded in packing.');
    }).catch((error: BusinessError) => {
    console.error('Failed to packing.');
  })
}
```



#### release

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

release(callback: AsyncCallback&lt;void&gt;): void

释放图片编码实例。使用callback异步回调。

由于图片占用内存较大，所以当ImagePacker实例使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数，当释放图片编码实例成功，err为undefined，否则为错误对象。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

async function Release() {
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  imagePackerObj.release((err: BusinessError)=>{
    if (err) {
      console.error(`Failed to release image packaging.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in releasing image packaging.');
    }
  })
}
```



#### release

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

release(): Promise&lt;void&gt;

释放图片编码实例。使用Promise异步回调。

由于图片占用内存较大，所以当ImagePacker实例使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

async function Release() {
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  imagePackerObj.release().then(() => {
    console.info('Succeeded in releasing image packaging.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to release image packaging.code ${error.code},message is ${error.message}`);
  })
}
```



#### packToFile11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

packToFile(source: ImageSource, fd: number, options: PackingOption, callback: AsyncCallback&lt;void&gt;): void

指定编码参数，将ImageSource直接编码进文件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | ImageSource | 是 | 编码的ImageSource。 |
| fd | number | 是 | 文件描述符。取值范围为[0，65535]。 |
| options | PackingOption | 是 | 设置编码参数。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数，当编码进文件成功，err为undefined，否则为错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[Image错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-image)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980101 | The image data is abnormal. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| 62980113 | Unknown image format.The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 62980115 | Invalid input parameter. |
| 62980119 | Failed to encode the image. |
| 62980120 | Add pixelmap out of range. |
| 62980172 | Failed to encode icc. |
| 62980252 | Failed to create surface. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

async function PackToFile(context : Context) {
  // 此处'test.png'仅作示例，请开发者自行替换，否则imageSource会创建失败导致后续无法正常执行。
  const path: string = context.filesDir + "/test.png";
  const imageSourceObj: image.ImageSource = image.createImageSource(path);
  let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 };
  const filePath: string = context.filesDir + "/image_source.jpg";
  let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  imagePackerObj.packToFile(imageSourceObj, file.fd, packOpts, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to pack the image to file.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in packing the image to file.');
    }
  })
}
```



#### packToFile11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

packToFile (source: ImageSource, fd: number, options: PackingOption): Promise&lt;void&gt;

指定编码参数，将ImageSource直接编码进文件。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | ImageSource | 是 | 编码的ImageSource。 |
| fd | number | 是 | 文件描述符。取值范围为[0，65535]。 |
| options | PackingOption | 是 | 设置编码参数。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[Image错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-image)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980101 | The image data is abnormal. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| 62980113 | Unknown image format.The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 62980115 | Invalid input parameter. |
| 62980119 | Failed to encode the image. |
| 62980120 | Add pixelmap out of range. |
| 62980172 | Failed to encode icc. |
| 62980252 | Failed to create surface. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

async function PackToFile(context : Context) {
  // 此处'test.png'仅作示例，请开发者自行替换，否则imageSource会创建失败导致后续无法正常执行。
  const path: string = context.filesDir + "/test.png";
  const imageSourceObj: image.ImageSource = image.createImageSource(path);
  let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 };
  const filePath: string = context.filesDir + "/image_source.jpg";
  let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  imagePackerObj.packToFile(imageSourceObj, file.fd, packOpts).then(() => {
    console.info('Succeeded in packing the image to file.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to pack the image to file.code ${error.code},message is ${error.message}`);
  })
}
```



#### packToFile11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

packToFile (source: PixelMap, fd: number, options: PackingOption, callback: AsyncCallback&lt;void&gt;): void

指定编码参数，将PixelMap直接编码进文件。使用callback异步回调。


![](assets/Interface%20ImagePacker/file-20260525092931773-003.png)


接口如果返回62980115错误码，表明参数异常，可能是PixelMap对象被提前释放了。需要调用方排查，在该方法调用结束后再释放PixelMap对象。



**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | PixelMap | 是 | 编码的PixelMap资源。 |
| fd | number | 是 | 文件描述符。取值范围为[0，65535]。 |
| options | PackingOption | 是 | 设置编码参数。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数，当编码图片进文件成功，err为undefined，否则为错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[Image错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-image)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980101 | The image data is abnormal. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| 62980113 | Unknown image format.The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 62980115 | Invalid input parameter. |
| 62980119 | Failed to encode the image. |
| 62980120 | Add pixelmap out of range. |
| 62980172 | Failed to encode icc. |
| 62980252 | Failed to create surface. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

async function PackToFile(context : Context) {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
  let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 4, width: 6 } }
  const path: string = context.filesDir + "/pixel_map.jpg";
  image.createPixelMap(color, opts).then((pixelmap: image.PixelMap) => {
    let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 }
    let file = fileIo.openSync(path, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
    const imagePackerObj: image.ImagePacker = image.createImagePacker();
    imagePackerObj.packToFile(pixelmap, file.fd, packOpts, (err: BusinessError) => {
      if (err) {
        console.error(`Failed to pack the image to file.code ${err.code},message is ${err.message}`);
      } else {
        console.info('Succeeded in packing the image to file.');
      }
    })
  })
}
```



#### packToFile11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

packToFile (source: PixelMap, fd: number, options: PackingOption): Promise&lt;void&gt;

指定编码参数，将PixelMap直接编码进文件。使用Promise异步回调。


![](assets/Interface%20ImagePacker/file-20260525092931779-004.png)


接口如果返回62980115错误码，表明参数异常，可能是PixelMap对象被提前释放了。需要调用方排查，在该方法调用结束后再释放PixelMap对象。



**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | PixelMap | 是 | 编码的PixelMap资源。 |
| fd | number | 是 | 文件描述符。取值范围为[0，65535]。 |
| options | PackingOption | 是 | 设置编码参数。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[Image错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-image)。

| 错误码ID | 错误信息 |
| --- | --- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980101 | The image data is abnormal. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |
| 62980113 | Unknown image format.The image data provided is not in a recognized or supported format, or it may be corrupted. |
| 62980115 | Invalid input parameter. |
| 62980119 | Failed to encode the image. |
| 62980120 | Add pixelmap out of range. |
| 62980172 | Failed to encode icc. |
| 62980252 | Failed to create surface. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

async function PackToFile(context : Context) {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
  let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 4, width: 6 } }
  const path: string = context.filesDir + "/pixel_map.jpg";
  image.createPixelMap(color, opts).then((pixelmap: image.PixelMap) => {
    let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 }
    let file = fileIo.openSync(path, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
    const imagePackerObj: image.ImagePacker = image.createImagePacker();
    imagePackerObj.packToFile(pixelmap, file.fd, packOpts)
      .then(() => {
        console.info('Succeeded in packing the image to file.');
      }).catch((error: BusinessError) => {
      console.error(`Failed to pack the image to file.code ${error.code},message is ${error.message}`);
    })
  })
}
```



#### packToFile13+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

packToFile(picture: Picture, fd: number, options: PackingOption): Promise&lt;void&gt;

指定编码参数，将Picture直接编码进文件。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| picture | Picture | 是 | 编码的Picture资源。 |
| fd | number | 是 | 文件描述符。取值范围为[0，65535]。 |
| options | PackingOption | 是 | 设置编码参数。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Image错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-image)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 7800301 | Encode failed. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

async function PackToFile(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("test.jpg");
  let ops: image.SourceOptions = {
    sourceDensity: 98,
  }
  let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
  let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
  let pictureObj: image.Picture = image.createPicture(commodityPixelMap);

  let funcName = "PackToFile";
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  if (imagePackerObj != null) {
    const filePath: string = context.filesDir + "/test.jpg";
    let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
    let packOpts: image.PackingOption = {
      format: "image/jpeg",
      quality: 98,
      desiredDynamicRange: image.PackingDynamicRange.AUTO,
      needsPackProperties: true};
    await imagePackerObj.packToFile(pictureObj, file.fd, packOpts).then(() => {
      console.info(funcName, 'Succeeded in packing the image to file.');
    }).catch((error: BusinessError) => {
      console.error(funcName, `Failed to pack the image to file.code ${error.code},message is ${error.message}`);
    });
  }
}
```



#### packToFileFromPixelmapSequence18+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

packToFileFromPixelmapSequence(pixelmapSequence: Array&lt;PixelMap&gt;, fd: number, options: PackingOptionsForSequence): Promise&lt;void&gt;

指定编码参数，将多个PixelMap编码成GIF文件。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pixelmapSequence | Array&lt;PixelMap&gt; | 是 | 待编码的PixelMap序列。 |
| fd | number | 是 | 文件描述符。取值范围为[0，65535]。 |
| options | PackingOptionsForSequence | 是 | 动图编码参数。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Image错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-image)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 7800301 | Failed to encode image. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

async function PackToFile(context : Context) {
  const resourceMgr = context.resourceManager;
  // 此处'moving_test.gif'仅作示例，请开发者自行替换。否则imageSource会创建失败，导致后续无法正常执行。
  const fileData = await resourceMgr.getRawFileContent('moving_test.gif');
  const color = fileData.buffer;
  let imageSource = image.createImageSource(color);
  let pixelMapList = await imageSource.createPixelMapList();
  let path: string = context.cacheDir + '/result.gif';
  let file = fileIo.openSync(path, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
  let ops: image.PackingOptionsForSequence = {
    frameCount: 3,  // 指定GIF编码中的帧数为3。
    delayTimeList: [10, 10, 10],  // 指定GIF编码中3帧的延迟时间分别为100ms、100ms、100ms。
    disposalTypes: [3, 2, 3], // 指定GIF编码中3帧的帧过渡模式分别为3（恢复到之前的状态）、2（恢复背景色)、3(恢复到之前的状态)。
    loopCount: 0 // 指定GIF编码中循环次数为无限循环。
  };
  let packer = image.createImagePacker();
  packer.packToFileFromPixelmapSequence(pixelMapList, file.fd, ops)
    .then(() => {
      console.info('Succeeded in packToFileMultiFrames.');
    }).catch((error: BusinessError) => {
    console.error('Failed to packToFileMultiFrames.');
  })
}
```



#### packing(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

packing(source: ImageSource, option: PackingOption, callback: AsyncCallback&lt;ArrayBuffer&gt;): void

图片压缩或重新编码。使用callback异步回调。

> [!NOTE]
> 从API version 6开始支持，从API version 13开始废弃，建议使用 packToData 代替。


**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | ImageSource | 是 | 编码的ImageSource。 |
| option | PackingOption | 是 | 设置编码参数。 |
| callback | AsyncCallback&lt;ArrayBuffer&gt; | 是 | 回调函数，当图片编码成功，err为undefined，data为获取到的压缩或编码数据；否则为错误对象。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

async function Packing(context : Context) {
  // 此处'test.jpg'仅作示例，请开发者自行替换，否则imageSource会创建失败导致后续无法正常执行。
  let filePath: string = context.filesDir + "/test.jpg";
  const imageSourceObj: image.ImageSource = image.createImageSource(filePath);
  let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 };
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  imagePackerObj.packing(imageSourceObj, packOpts, (err: BusinessError, data: ArrayBuffer) => {
    if (err) {
      console.error(`Failed to pack the image.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in packing the image.');
    }
  })
}
```



#### packing(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

packing(source: ImageSource, option: PackingOption): Promise&lt;ArrayBuffer&gt;

图片压缩或重新编码。使用Promise异步回调。

> [!NOTE]
> 从API version 6开始支持，从API version 13开始废弃，建议使用 packToData 代替。


**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | ImageSource | 是 | 编码的ImageSource。 |
| option | PackingOption | 是 | 设置编码参数。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;ArrayBuffer&gt; | Promise对象，返回压缩或编码后的数据。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

async function Packing(context : Context) {
  // 此处'test.jpg'仅作示例，请开发者自行替换，否则imageSource会创建失败导致后续无法正常执行。
  let filePath: string = context.filesDir + "/test.jpg";
  const imageSourceObj: image.ImageSource = image.createImageSource(filePath);
  let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 }
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  imagePackerObj.packing(imageSourceObj, packOpts)
    .then((data: ArrayBuffer) => {
      console.info('Succeeded in packing the image.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to pack the image.code ${error.code},message is ${error.message}`);
    })
}
```



#### packing(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

packing(source: PixelMap, option: PackingOption, callback: AsyncCallback&lt;ArrayBuffer&gt;): void

图片压缩或重新编码。使用callback异步回调。

> [!NOTE]
> 从API version 8开始支持，从API version 13开始废弃，建议使用 packToData 代替。



![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/uQnB4kYhT5ebqdC9hXaszg/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260528T025326Z&HW-CC-Expire=86400&HW-CC-Sign=4C67CFDFF087F4BD74666F458D793448D74AD49A4A7BE283787A8057D7364B05)


接口如果返回"PixelMap mismatch"，表明参数异常，可能是PixelMap对象被提前释放了。需要调用方排查，在该方法调用结束后再释放PixelMap对象。



**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | PixelMap | 是 | 编码的PixelMap资源。 |
| option | PackingOption | 是 | 设置编码参数。 |
| callback | AsyncCallback&lt;ArrayBuffer&gt; | 是 | 回调函数，当图片编码成功，err为undefined，data为获取到的压缩或编码数据；否则为错误对象。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

async function Packing() {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
  let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 4, width: 6 } }
  image.createPixelMap(color, opts).then((pixelMap: image.PixelMap) => {
    let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 }
    const imagePackerObj: image.ImagePacker = image.createImagePacker();
    imagePackerObj.packing(pixelMap, packOpts, (err: BusinessError, data: ArrayBuffer) => {
      if (err) {
        console.error(`Failed to pack the image.code ${err.code},message is ${err.message}`);
      } else {
        console.info('Succeeded in packing the image.');
      }
    })
  }).catch((error: BusinessError) => {
    console.error(`Failed to create the PixelMap.code ${error.code},message is ${error.message}`);
  })
}
```



#### packing(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

packing(source: PixelMap, option: PackingOption): Promise&lt;ArrayBuffer&gt;

图片压缩或重新编码。使用Promise异步回调。

> [!NOTE]
> 从API version 8开始支持，从API version 13开始废弃，建议使用 packToData 代替。



![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/zS5pVm0RQA655-8ER39DtA/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260528T025326Z&HW-CC-Expire=86400&HW-CC-Sign=9B88BEA57A4F4E851D5FBC8EC4A3B3382BF0F4B58881CB4E0D5D74DC3443F4A1)


接口如果返回"PixelMap mismatch"，表明参数异常，可能是PixelMap对象被提前释放了。需要调用方排查，在该方法调用结束后再释放PixelMap对象。



**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | PixelMap | 是 | 编码的PixelMap源。 |
| option | PackingOption | 是 | 设置编码参数。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;ArrayBuffer&gt; | Promise对象，返回压缩或编码后的数据。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

async function Packing() {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4。
  let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 4, width: 6 } }
  image.createPixelMap(color, opts).then((pixelMap: image.PixelMap) => {
    let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 }
    const imagePackerObj: image.ImagePacker = image.createImagePacker();
    imagePackerObj.packing(pixelMap, packOpts)
      .then((data: ArrayBuffer) => {
        console.info('Succeeded in packing the image.');
      }).catch((error: BusinessError) => {
      console.error(`Failed to pack the image.code ${error.code},message is ${error.message}`);
    })
  }).catch((error: BusinessError) => {
    console.error(`Failed to create PixelMap.code ${error.code},message is ${error.message}`);
  })
}
```
