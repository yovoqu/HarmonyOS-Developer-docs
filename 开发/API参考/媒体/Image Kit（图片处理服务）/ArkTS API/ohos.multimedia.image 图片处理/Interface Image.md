# Interface (Image)

更新时间：2026-05-19 09:13:51

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-image
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

Image类，供ImageReceiver和ImageCreator使用，用于传输图片对象，其实际内容由生产者决定。如相机预览流提供的Image对象存储了YUV数据、相机拍照提供的Image对象存储了JPEG文件。

调用[readNextImage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagereceiver#readnextimage9)和[readLatestImage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagereceiver#readlatestimage9)接口时会返回Image实例。

Image的属性仅支持在创建时初始化，后续无法再修改，且其属性不对图片内容产生实际影响，请以图片生产者写入的属性为准，即以向[ImageReceiver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagereceiver)发送图片数据的发送方实际写入的内容为准。

由于图片占用内存较大，所以当Image实例使用完成后，应主动调用[release](#release9)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

> [!NOTE]
> 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 本Interface首批接口从API version 9开始支持。



##### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { image } from '@kit.ImageKit';
```



##### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**系统能力：** SystemCapability.Multimedia.Image.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| clipRect9+ | Region | 否 | 否 | 要裁剪的图像区域。恒等于整个图像，不支持修改。 |
| size9+ | Size | 是 | 否 | 图像大小。 如果Image对象所存储的是相机预览流数据（YUV图像数据），那么获取到的size中的宽和高分别对应YUV图像的宽和高。 如果Image对象所存储的是相机拍照流数据（JPEG图像数据），由于已是编码后的文件，size中的宽等于JPEG文件大小，高等于1。 Image对象所存储的数据是预览流还是拍照流，取决于应用将receiver中的surfaceId通过createPreviewOutput接口还是createPhotoOutput接口传给相机。 相机预览与拍照最佳实践请参考双路预览(ArkTS)与拍照实践(ArkTS)。 |
| format9+ | number | 是 | 否 | 图像格式，参考OH_NativeBuffer_Format。 |
| timestamp12+ | number | 是 | 否 | 图像时间戳。时间戳以纳秒为单位，通常是单调递增的。时间戳的具体含义和基准取决于图像的生产者，在相机预览/拍照场景，生产者就是相机。来自不同生产者的图像的时间戳可能有不同的含义和基准，因此可能无法进行比较。如果要获取某张照片的生成时间，可以通过getImageProperty接口读取EXIF时间戳信息。 |
| colorSpace23+ | colorSpaceManager.ColorSpace | 是 | 否 | 图像色彩空间，色域枚举类型。 模型约束： 此接口仅可在Stage模型下使用。 |




##### getComponent9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getComponent(componentType: ComponentType, callback: AsyncCallback&lt;Component&gt;): void

根据图像的组件类型从图像中获取组件缓存。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| componentType | ComponentType | 是 | 图像的组件类型（目前仅支持ComponentType:JPEG，实际返回格式由生产者决定，如相机）。 |
| callback | AsyncCallback&lt;Component&gt; | 是 | 回调函数，当返回组件缓冲区成功，err为undefined，data为获取到的组件缓冲区；否则为错误对象。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

async function GetComponent(img : image.Image) {
  img.getComponent(image.ComponentType.JPEG, (err: BusinessError, component: image.Component) => {
    if (err) {
      console.error(`Failed to get the component.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in getting component.');
    }
  })
}
```



##### getComponent9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getComponent(componentType: ComponentType): Promise&lt;Component&gt;

根据图像的组件类型从图像中获取组件缓存。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| componentType | ComponentType | 是 | 图像的组件类型（目前仅支持ComponentType:JPEG，实际返回格式由生产者决定，如相机）。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Component&gt; | Promise对象，返回组件缓冲区。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

async function GetComponent(img : image.Image) {
  img.getComponent(image.ComponentType.JPEG).then((component: image.Component) => {
    console.info('Succeeded in getting component.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to get the component.code ${error.code},message is ${error.message}`);
  })
}
```



##### release9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

release(callback: AsyncCallback&lt;void&gt;): void

释放当前图像。使用callback异步回调。

在接收另一个图像前必须先释放对应资源。

由于图片占用内存较大，所以当Image实例使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数，当图像释放成功，err为undefined，否则为错误对象。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(img : image.Image) {
  img.release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release the image instance.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in releasing the image instance.');
    }
  })
}
```



##### release9+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

release(): Promise&lt;void&gt;

释放当前图像。使用Promise异步回调。

在接收另一个图像前必须先释放对应资源。

由于图片占用内存较大，所以当Image实例使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(img : image.Image) {
  img.release().then(() => {
    console.info('Succeeded in releasing the image instance.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to release the image instance.code ${error.code},message is ${error.message}`);
  })
}
```



##### getBufferData23+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getBufferData(): ImageBufferData | null

从图像中获取ImageBufferData。


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/kAZoh1WKQvirk5wb0NpNow/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260528T023950Z&HW-CC-Expire=86400&HW-CC-Sign=A7219E564A16364D079784F2CEA7C09ED4EC2620CAEA21BF001778659A6F613A)


ImageBufferData中的byteBuffer是对内部缓存的浅拷贝，当Image的生命周期结束时，便不能对byteBuffer做任何操作，否则会导致未定义行为。



**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ImageBufferData \| null | 获取封装图像数据缓冲区的结构体，获取不到时返回空值。 |


**示例：**

```text
function GetBufferData(img: image.Image) {
  const bufferData = img.getBufferData();
  if (bufferData == null) {
    console.error('Failed to get the bufferData: bufferData is null.');
    return;
  }
  console.info('Succeeded in getting bufferData.');
}
```



##### getMetadata23+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getMetadata(key: HdrMetadataKey): HdrMetadataValue | null

根据HDR元数据的类型从图像中获取HDR元数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | HdrMetadataKey | 是 | HDR元数据的关键字，可用于查询对应值。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| HdrMetadataValue \| null | 返回关键字对应的HDR元数据的值。如果图像没有HDR元数据，返回空值。 |


**错误码：**

以下错误码的详细介绍请参见[Image错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-image)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7600206 | Invalid parameter. |
| 7600302 | Memory copy failed. |


**示例：**

```text
async function GetMetadata(img : image.Image) {
  try {
    let staticMetadata = img.getMetadata(image.HdrMetadataKey.HDR_STATIC_METADATA);
    console.info(`getMetadata:${staticMetadata}`);
  } catch (err) {
    console.error('Failed to getMetadata.' + err);
  }
}
```
