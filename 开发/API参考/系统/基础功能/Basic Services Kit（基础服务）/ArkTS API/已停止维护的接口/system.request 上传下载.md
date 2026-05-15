# @system.request (上传下载)

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-request
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

system.request部件主要给应用提供上传下载文件的基础能力。


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
import { Request } from '@kit.BasicServicesKit';
```


## request.upload(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

upload(options: UploadRequestOptions): void

上传文件，无返回值。

**系统能力**：SystemCapability.MiscServices.Upload


> [!NOTE]
> 从API version 3 开始支持，从API version 9 开始废弃，建议使用[request.uploadFile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-request#requestuploadfile9)替代。

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [UploadRequestOptions](#uploadrequestoptionsdeprecated) | 是 | 上传的配置信息。 |


**示例：**


```text
import  { Request, UploadRequestOptions, UploadResponse } from '@kit.BasicServicesKit';

let uploadRequestOptions: UploadRequestOptions = {
url: 'http://www.path.com',
method: 'POST',
files: [{
filename: "test",
name: "test",
uri: "internal://cache/test.jpg",
type: "jpg"
}],
data: [{
name: "name123",
value: "123"
}],
success: (data: UploadResponse) => {
console.info('Succeeded in uploading, code:' + JSON.stringify(data.code));
},
fail: (data: string, code: number) => {
console.info('Failed to upload, data: ' + data + 'code: ' + code);
},
complete: () => {
console.info('Upload complete');
}
}

try {
Request.upload(uploadRequestOptions);
console.info('Start Upload');
} catch (err) {
console.error('Failed to upload, err:' + err);
}
```


## UploadRequestOptions(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

**系统能力**：SystemCapability.MiscServices.Upload


> [!NOTE]
> 从API version 3 开始支持，从API version 9 开始废弃，建议使用[UploadConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-request#uploadconfig)替代。

**参数：**


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 上传服务器地址。 |
| data | Array&lt;[RequestData](#requestdatadeprecated)&gt; | 否 | 请求的表单数据。 |
| files | Array&lt;[RequestFile](#requestfiledeprecated)&gt; | 是 | 待上传文件列表。请使用multipart/form-data进行提交。 |
| header | Object | 否 | 请求头。 |
| method | string | 否 | 请求方法：POST、PUT。缺省POST。 |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |


**success参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [UploadResponse](#uploadresponsedeprecated) | 是 | 上传任务成功返回信息。 |


**fail参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | any | 是 | 上传任务失败返回header信息。 |
| code | number | 是 | 上传任务失败返回HTTP状态码。 |


## UploadResponse(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

**系统能力**：SystemCapability.MiscServices.Upload


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 服务器返回的HTTP状态码。 |
| data | string | 是 | 服务器返回的内容。根据返回头内容中的type决定该值的类型。 |
| headers | Object | 是 | 服务器返回的返回头内容。 |


## RequestFile(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

**系统能力**：SystemCapability.MiscServices.Upload


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filename | string | 否 | multipart 提交时，请求头中的文件名。 |
| name | string | 否 | multipart 提交时，表单项目的名称，缺省为file。 |
| uri | string | 是 | 文件的本地存储路径。 |
| type | string | 否 | 文件的内容类型，默认根据文件名或路径的后缀获取。 |


## RequestData(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

**系统能力**：SystemCapability.MiscServices.Upload


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 表示form 元素的名称。 |
| value | string | 是 | 表示form 元素的值。 |


## request.download(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

download(options: DownloadRequestOptions): void

下载文件，无返回值。

**系统能力**：SystemCapability.MiscServices.Download

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [DownloadRequestOptions](#downloadrequestoptionsdeprecated) | 是 | 下载的配置信息。 |


**示例：**


```text
import  { Request, DownloadResponse, DownloadRequestOptions } from '@kit.BasicServicesKit';

let downloadRequestOptions: DownloadRequestOptions = {
url: 'http://www.path.com',
filename: 'requestSystemTest',
header: "",
description: 'this is requestSystem download response',
success: (data: DownloadResponse) => {
console.info('Succeeded in downloading, code:' + JSON.stringify(data));
},
fail: (data: string, code: number) => {
console.info('Failed to download, data: ' + data + 'code: ' + code);
},
complete: () => {
console.info('Download complete');
}
}

try {
Request.download(downloadRequestOptions);
console.info('Start download');
} catch(err) {
console.error('Failed to download, err:' + err);
}
```


## DownloadRequestOptions(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

**系统能力**：SystemCapability.MiscServices.Download


> [!NOTE]
> 从API version 3 开始支持，从API version 9 开始废弃，建议使用[UploadConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-request#uploadconfig)替代。

**参数：**


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 资源地址。 |
| filename | string | 否 | 本次下载文件的名称。默认从本次请求或资源地址中获取。 |
| header | Object | 否 | 请求头。 |
| description | string | 否 | 资源地址的下载描述，默认为文件名称。 |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |


**success参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [DownloadResponse](#downloadresponsedeprecated) | 是 | 下载任务成功返回信息。 |


**fail参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | any | 是 | 下载任务失败返回header信息。 |
| code | number | 是 | 下载任务失败返回HTTP状态码。 |


## DownloadResponse(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

**系统能力**：SystemCapability.MiscServices.Download


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | string | 是 | 表示下载的token，获取下载状态的依据。 |


## request.onDownloadComplete(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

onDownloadComplete(options: OnDownloadCompleteOptions): void

获取下载任务状态，无返回值。

**系统能力**：SystemCapability.MiscServices.Download

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [OnDownloadCompleteOptions](#ondownloadcompleteoptionsdeprecated) | 是 | 监听下载任务的配置信息。 |


**示例：**


```text
import  { Request, OnDownloadCompleteOptions, OnDownloadCompleteResponse } from '@kit.BasicServicesKit';

let onDownloadCompleteOptions: OnDownloadCompleteOptions = {
token: 'token-index',
success: (data: OnDownloadCompleteResponse) => {
console.info('Succeeded in downloading, uri:' + JSON.stringify(data.uri));
},
fail: (data: string, code: number) => {
console.info('Failed to download, data: ' + data + 'code: ' + code);
},
complete: () => {
console.info('Download complete');
}
}

Request.onDownloadComplete(onDownloadCompleteOptions);
```


## OnDownloadCompleteOptions(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

**系统能力**：SystemCapability.MiscServices.Download


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | string | 是 | download 接口返回的结果 token。 |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |


**success参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [OnDownloadCompleteResponse](#ondownloadcompleteresponsedeprecated) | 是 | 下载任务成功返回信息。 |


**fail参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | any | 是 | 下载任务失败返回header信息。 |
| code | number | 是 | 下载任务失败返回HTTP状态码。 |


## OnDownloadCompleteResponse(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

**系统能力**：SystemCapability.MiscServices.Download


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示下载文件的uri。 |
