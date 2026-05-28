# @ohos.file.storageStatistics (应用空间统计)

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-storage-statistics
**支持设备：** Phone | PC/2in1 | Tablet | TV

该模块提供空间查询相关的常用功能：包括对内外卡的空间查询、对应用分类数据统计的查询、对应用数据的查询等。

> [!NOTE]
> 本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。



#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
import { storageStatistics } from '@kit.CoreFileKit';
```



#### storageStatistics.getCurrentBundleStats9+

**支持设备：** Phone | PC/2in1 | Tablet | TV

getCurrentBundleStats(): Promise&lt;BundleStats&gt;

应用异步获取当前应用存储空间大小（单位为Byte），使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.StorageService.SpatialStatistics

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;BundleStats&gt; | Promise对象，返回指定卷上的应用存储空间大小（单位为Byte）。 |


**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid. Possible causes: Mandatory parameters are left unspecified. |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';
storageStatistics.getCurrentBundleStats().then((BundleStats: storageStatistics.BundleStats) => {
  console.info("getCurrentBundleStats successfully:" + JSON.stringify(BundleStats));
}).catch((err: BusinessError) => {
  console.error("getCurrentBundleStats failed with error:"+ JSON.stringify(err));
});
```



#### storageStatistics.getCurrentBundleStats9+

**支持设备：** Phone | PC/2in1 | Tablet | TV

getCurrentBundleStats(callback: AsyncCallback&lt;BundleStats&gt;): void

应用异步获取当前应用存储空间大小（单位为Byte），使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.StorageService.SpatialStatistics

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;BundleStats&gt; | 是 | 获取指定卷上的应用存储空间大小之后的回调。 |


**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid. Possible causes: Mandatory parameters are left unspecified. |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';
storageStatistics.getCurrentBundleStats((error: BusinessError, bundleStats: storageStatistics.BundleStats) => {
  if (error) {
    console.error("getCurrentBundleStats failed with error:" + JSON.stringify(error));
  } else {
    // do something
    console.info("getCurrentBundleStats successfully:" + JSON.stringify(bundleStats));
  }
});
```



#### storageStatistics.getTotalSize15+

**支持设备：** Phone | PC/2in1 | Tablet | TV

getTotalSize(): Promise&lt;number&gt;

获取内置存储的总空间大小（单位为Byte），使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.StorageService.SpatialStatistics

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | Promise对象，返回内置存储的总空间大小（单位为Byte）。 |


**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';
storageStatistics.getTotalSize().then((number: number) => {
  console.info("getTotalSize successfully:" + JSON.stringify(number));
}).catch((err: BusinessError) => {
  console.error("getTotalSize failed with error:"+ JSON.stringify(err));
});
```



#### storageStatistics.getTotalSize15+

**支持设备：** Phone | PC/2in1 | Tablet | TV

getTotalSize(callback: AsyncCallback&lt;number&gt;): void

获取内置存储的总空间大小（单位为Byte），使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.StorageService.SpatialStatistics

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;number&gt; | 是 | 获取内置存储的总空间大小之后的回调。 |


**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid. Possible causes: Mandatory parameters are left unspecified. |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';
storageStatistics.getTotalSize((error: BusinessError, number: number) => {
  if (error) {
    console.error("getTotalSize failed with error:" + JSON.stringify(error));
  } else {
    // do something
    console.info("getTotalSize successfully:" + number);
  }
});
```



#### storageStatistics.getTotalSizeSync15+

**支持设备：** Phone | PC/2in1 | Tablet | TV

getTotalSizeSync(): number

同步获取内置存储的总空间大小（单位为Byte）。

**系统能力**：SystemCapability.FileManagement.StorageService.SpatialStatistics

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回内置存储的总空间大小（单位为Byte）。 |


**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';
try {
  let number = storageStatistics.getTotalSizeSync();
  console.info("getTotalSizeSync successfully:" + JSON.stringify(number));
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error("getTotalSizeSync failed with error:" + JSON.stringify(error));
}
```



#### storageStatistics.getFreeSize15+

**支持设备：** Phone | PC/2in1 | Tablet | TV

getFreeSize(): Promise&lt;number&gt;

获取内置存储的可用空间大小（单位为Byte），使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.StorageService.SpatialStatistics

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | Promise对象，返回内置存储的可用空间大小（单位为Byte）。 |


**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';
storageStatistics.getFreeSize().then((number: number) => {
  console.info("getFreeSize successfully:" + JSON.stringify(number));
}).catch((err: BusinessError) => {
  console.error("getFreeSize failed with error:" + JSON.stringify(err));
});
```



#### storageStatistics.getFreeSize15+

**支持设备：** Phone | PC/2in1 | Tablet | TV

getFreeSize(callback: AsyncCallback&lt;number&gt;): void

获取内置存储的可用空间大小（单位为Byte），使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.StorageService.SpatialStatistics

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;number&gt; | 是 | 获取内置存储的可用空间大小之后的回调。 |


**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid. Possible causes: Mandatory parameters are left unspecified. |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';
storageStatistics.getFreeSize((error: BusinessError, number: number) => {
  if (error) {
    console.error("getFreeSize failed with error:" + JSON.stringify(error));
  } else {
    // do something
    console.info("getFreeSize successfully:" + number);
  }
});
```



#### storageStatistics.getFreeSizeSync15+

**支持设备：** Phone | PC/2in1 | Tablet | TV

getFreeSizeSync(): number

同步获取内置存储的可用空间大小（单位为Byte）。

**系统能力**：SystemCapability.FileManagement.StorageService.SpatialStatistics

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回内置存储的可用空间大小（单位为Byte）。 |


**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |


**示例：**

```json
import { BusinessError } from '@kit.BasicServicesKit';
try {
  let number = storageStatistics.getFreeSizeSync();
  console.info("getFreeSizeSync successfully:" + JSON.stringify(number));
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error("getFreeSizeSync failed with error:" + JSON.stringify(error));
}
```



#### BundleStats9+

**支持设备：** Phone | PC/2in1 | Tablet | TV

**系统能力**：SystemCapability.FileManagement.StorageService.SpatialStatistics

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| appSize | number | 否 | 否 | 应用安装文件大小（单位为Byte）。 |
| cacheSize | number | 否 | 否 | 应用缓存文件大小（单位为Byte）。 |
| dataSize | number | 否 | 否 | 应用文件存储大小（除应用安装文件）（单位为Byte）。 |




#### storageStatistics.getTotalInodes24+

**支持设备：** Phone | PC/2in1 | Tablet | TV

getTotalInodes(): Promise&lt;number&gt;

获取文件系统的inode资源总量，仅支持查询系统数据分区。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.StorageService.SpatialStatistics

**模型约束**：此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | Promise对象，返回文件系统inode资源总量。 |


**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13600001 | IPC error. |
| 13600016 | Failed to query the inode information of the data partition. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

storageStatistics.getTotalInodes().then((totalInodes: number) => {
  console.info("getTotalInodes successfully: " + totalInodes);
}).catch((err: BusinessError) => {
  console.error(`getTotalInodes failed. Code: ${err.code}, Message: ${err.message}`);
});
```



#### storageStatistics.getFreeInodes24+

**支持设备：** Phone | PC/2in1 | Tablet | TV

getFreeInodes(): Promise&lt;number&gt;

获取文件系统的inode资源剩余量，仅支持查询系统数据分区。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.StorageService.SpatialStatistics

**模型约束**：此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | Promise对象，返回文件系统inode资源剩余量。 |


**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13600001 | IPC error. |
| 13600016 | Failed to query the inode information of the data partition. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

storageStatistics.getFreeInodes().then((freeInodes: number) => {
  console.info("getFreeInodes successfully: " + freeInodes);
}).catch((err: BusinessError) => {
  console.error(`getFreeInodes failed. Code: ${err.code}, Message: ${err.message}`);
});
```



#### storageStatistics.getCurrentBundleInodes24+

**支持设备：** Phone | PC/2in1 | Tablet | TV

getCurrentBundleInodes(): Promise&lt;number&gt;

获取当前应用的inode占用量，使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.StorageService.SpatialStatistics

**模型约束**：此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | Promise对象，返回当前应用的inode占用量。 |


**错误码：**

以下错误码的详细介绍请参见[文件管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13600001 | IPC error. |
| 13600002 | File system not supported. |
| 13600017 | Failed to query the inode information of the application. |


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

storageStatistics.getCurrentBundleInodes().then((curInodes: number) => {
  console.info("getCurrentBundleInodes successfully: " + curInodes);
}).catch((err: BusinessError) => {
  console.error(`getCurrentBundleInodes failed. Code: ${err.code}, Message: ${err.message}`);
});
```
