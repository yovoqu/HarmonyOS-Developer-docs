# Class (PhotoViewPicker)

更新时间：2026-07-21 07:44:23

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

图库选择器对象用于支持选择图片、视频等用户场景。使用前，需先创建PhotoViewPicker实例。

> [!NOTE]
> 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 如果需要重复拉起PhotoViewPicker，需要先通过NavDestination或跟随进程销毁前一个photoViewPicker。



#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```



#### select

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

select(option?: PhotoSelectOptions) : Promise&lt;PhotoSelectResult&gt;

通过选择模式拉起photoPicker界面，用户可以选择一个或多个图片/视频。使用Promise异步回调。传入可选参数PhotoSelectOptions对象，返回PhotoSelectResult对象。


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/OYhYP1Y3TbiNda3JVIn3Ew/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260723T012039Z&HW-CC-Expire=86400&HW-CC-Sign=60A9F1F35A803F3F2D91138359AF32633771375F15B4E1EB8D1BBC0579B01832)


此接口返回的PhotoSelectResult对象中的photoUris具有永久授权，可通过调用接口[photoAccessHelper.getAssets](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper#getassets)去使用。具体操作请参考[媒体文件URI的使用方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro#媒体文件uri的使用方式)。



**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| option | PhotoSelectOptions | 否 | photoPicker选择选项，若无此参数，则默认选择媒体文件类型为图片和视频类型，默认选择媒体文件数量的最大值为50。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;PhotoSelectResult&gt; | Promise对象。返回photoPicker选择后的结果集 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)、[文件管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement)和[媒体库错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-medialibrary)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 13900042 | Unknown error. |
| 23800151 | Scene parameters validate failed, possible causes:1. An illegal enumeration value was passed to PhotoSelectOptions.globalMovingPhotoState. Only MOVING_PHOTO_ENABLED and MOVING_PHOTO_DISABLED are supported for configuration; 2. An illegal enumeration value was passed to PhotoSelectOptions.assetCompatibleAbility. 适用版本：12 |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';

async function example01(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
    photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
    photoSelectOptions.maxSelectNumber = 5;
    let photoPicker = new photoAccessHelper.PhotoViewPicker();
    photoPicker.select(photoSelectOptions).then((photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
      console.info('PhotoViewPicker.select successfully, photoSelectResult uri: ' + JSON.stringify(photoSelectResult));
    }).catch((err: BusinessError) => {
      console.error(`PhotoViewPicker.select failed with err: ${err.code}, ${err.message}`);
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`PhotoViewPicker failed with err: ${err.code}, ${err.message}`);
  }
}
```



#### select

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

select(option: PhotoSelectOptions, callback: AsyncCallback&lt;PhotoSelectResult&gt;) : void

通过选择模式拉起photoPicker界面，用户可以选择一个或多个图片/视频。接口采用callback异步返回形式，传入参数PhotoSelectOptions对象，返回PhotoSelectResult对象。


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/-kZ1D8tOSYKHjp1FMoJ8ww/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260723T012039Z&HW-CC-Expire=86400&HW-CC-Sign=75A6FF6C76EA0C456381F8635DE447A5498EA5E8D4F348F1BD94E301178AF85C)


此接口返回的PhotoSelectResult对象中的photoUris具有永久授权，可通过调用接口[photoAccessHelper.getAssets](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper#getassets)去使用。具体操作请参考[媒体文件URI的使用方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro#媒体文件uri的使用方式)。



**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| option | PhotoSelectOptions | 是 | photoPicker选择选项。 |
| callback | AsyncCallback&lt;PhotoSelectResult&gt; | 是 | callback 返回photoPicker选择后的结果集。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)、[文件管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement)和[媒体库错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-medialibrary)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 13900042 | Unknown error. |
| 23800151 | Scene parameters validate failed, possible causes:1. An illegal enumeration value was passed to PhotoSelectOptions.globalMovingPhotoState. Only MOVING_PHOTO_ENABLED and MOVING_PHOTO_DISABLED are supported for configuration; |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';

async function example02(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
    photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
    photoSelectOptions.maxSelectNumber = 5;
    let photoPicker = new photoAccessHelper.PhotoViewPicker();
    photoPicker.select(photoSelectOptions, (err: BusinessError, photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
      if (err) {
        console.error(`PhotoViewPicker.select failed with err: ${err.code}, ${err.message}`);
        return;
      }
      console.info('PhotoViewPicker.select successfully, photoSelectResult uri: ' + JSON.stringify(photoSelectResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`PhotoViewPicker failed with err: ${err.code}, ${err.message}`);
  }
}
```



#### select

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

select(callback: AsyncCallback&lt;PhotoSelectResult&gt;) : void

通过选择模式拉起photoPicker界面，用户可以选择一个或多个图片/视频。接口采用callback异步返回形式，返回PhotoSelectResult对象。


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/ykpAqV1hSWScbSyg1GKxJQ/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260723T012039Z&HW-CC-Expire=86400&HW-CC-Sign=64B036C7DE269356D984F2D68EF50F2CB62870EDE5EA8EE94A9DC21B80964837)


此接口返回的PhotoSelectResult对象中的photoUris具有永久授权，可通过调用接口[photoAccessHelper.getAssets](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper#getassets)去使用。具体操作请参考[媒体文件URI的使用方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro#媒体文件uri的使用方式)。



**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;PhotoSelectResult&gt; | 是 | callback 返回photoPicker选择后的结果集。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[文件管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 13900042 | Unknown error. |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';

async function example03(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    let photoPicker = new photoAccessHelper.PhotoViewPicker();
    photoPicker.select((err: BusinessError, photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
      if (err) {
        console.error(`PhotoViewPicker.select failed with err: ${err.code}, ${err.message}`);
        return;
      }
      console.info('PhotoViewPicker.select successfully, photoSelectResult uri: ' + JSON.stringify(photoSelectResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`PhotoViewPicker failed with err: ${err.code}, ${err.message}`);
  }
}
```
