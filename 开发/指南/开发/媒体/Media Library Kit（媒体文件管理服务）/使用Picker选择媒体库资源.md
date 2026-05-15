# 使用Picker选择媒体库资源

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoaccesshelper-photoviewpicker

当用户需要分享图片、视频等文件时，开发者可以通过特定接口拉起系统图库，让用户自行选择待分享的资源，完成分享。此接口本身无需申请权限，目前适用于界面UIAbility，使用窗口组件触发。具体使用方式如下：

Media Library Kit提供图片和视频的管理能力，当需要读取和保存音频文件时，请使用[AudioViewPicker（音频选择器对象）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-picker#audioviewpicker)。


以下示例以图片选择为例，媒体文件类型请参见[PhotoViewMIMETypes](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-e#photoviewmimetypes)。


```text
photoSelectOptions.maxSelectNumber = 5;
photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE;
photoSelectOptions.isPhotoTakingSupported = true;
```


## 指定URI读取文件数据

待界面从图库返回后，再通过一个类似按钮的组件去调用其他函数，使用[fileIo.openSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileioopensync)接口，通过[媒体文件uri](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro#媒体文件uri)打开这个文件得到fd。这里需要注意接口权限参数是fileIo.OpenMode.READ_ONLY。
```text
try {
  const file = fileIo.openSync(uri, fileIo.OpenMode.READ_ONLY);
  console.info('file fd: ' + file.fd);
  return { fd: file.fd, file: file };
} catch (error) {
  console.error('openSync failed with err: ' + error);
  return null;
}
```

通过fd使用[fileIo.readSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#readsync)接口读取这个文件内的数据，读取完成后关闭fd。
```text
try {
  const buffer = new ArrayBuffer(bufferSize);
  const readLen = fileIo.readSync(fileObj.fd, buffer);
  console.info('readSync data to file succeed and buffer size is:' + readLen);
  return { data: buffer, length: readLen };
} catch (error) {
  console.error('readSync failed with err: ' + error);
  return null;
}
```


## 指定URI获取图片或视频资源

媒体库支持Picker选择[媒体文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-file-uri-intro#媒体文件uri)URI后，根据指定URI获取图片或视频资源，下面以查询指定URI为'file://media/Photo/1/IMG_datetime_0001/displayName.jpg'为例。 定义媒体资源处理器[MediaAssetDataHandler](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-mediaassetdatahandler)，系统在资源准备就绪时向应用回调onDataPrepared。
```text
export class MediaAssetDataHandler implements photoAccessHelper.MediaAssetDataHandler {
  private callback?: MediaDataHandlerCallback;

  constructor(callback?: MediaDataHandlerCallback) {
    this.callback = callback;
  }

  // 使用箭头函数确保this引用不会丢失
  onDataPrepared = (data: ArrayBuffer) => {
    if (data === undefined) {
      console.error('Error occurred when preparing data');
      return;
    }
    console.info('on image data prepared');
    // 现在this始终指向MediaAssetDataHandler实例
    if (this.callback) {
      this.callback(data);
    }
  };
}
```

使用[getAssets](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper#getassets-1)接口获取要访问的资产，并通过[requestImageData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-mediaassetmanager#requestimagedata11)获取对应资源。
![](assets/使用Picker选择媒体库资源/file-20260514131557575-0.png)
出于对用户隐私安全的保护，对媒体资源EXIF中的地理位置和拍摄参数信息做了去隐私化处理。如果需要获取被去隐私化的EXIF信息，需要[申请相册管理模块权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoaccesshelper-preparation#申请相册管理模块功能相关权限)'ohos.permission.MEDIA_LOCATION'。
```text
static async getMediaResourceByUri(uri: string, context: common.Context, callback?: MediaDataHandlerCallback)
: Promise {
  try {
    // 创建PhotoAccessHelper实例
    const phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);

    // 创建查询条件
    const predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    predicates.equalTo(photoAccessHelper.PhotoKeys.URI, uri);

    // 设置查询选项
    const fetchOptions: photoAccessHelper.FetchOptions = {
      fetchColumns: [photoAccessHelper.PhotoKeys.TITLE],
      predicates: predicates
    };

    // 查询资产
    const fetchResult: photoAccessHelper.FetchResult =
      await phAccessHelper.getAssets(fetchOptions);

    const photoAsset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    if (photoAsset) {
      console.info('getAssets photoAsset.uri : ' + photoAsset.uri);
      // 获取标题属性
      console.info('title : ' + photoAsset.get(photoAccessHelper.PhotoKeys.TITLE));

      // 设置请求选项
      const requestOptions: photoAccessHelper.RequestOptions = {
        deliveryMode: photoAccessHelper.DeliveryMode.HIGH_QUALITY_MODE,
      };

      // 请求图片数据
      await photoAccessHelper.MediaAssetManager.requestImageData(
        context, photoAsset, requestOptions, new MediaAssetDataHandler(callback));

      console.info('requestImageData successfully');
    } else {
      console.error('No asset found for URI: ' + uri);
    }

    // 关闭查询结果
    fetchResult.close();
  } catch (err) {
    console.error('getMediaResourceByUri failed with err: ' + err);
  }
}
```
