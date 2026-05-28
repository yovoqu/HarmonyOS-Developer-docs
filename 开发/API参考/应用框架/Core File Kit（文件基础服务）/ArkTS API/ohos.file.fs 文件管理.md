# @ohos.file.fs (文件管理)

更新时间：2026-05-18 03:44:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

该模块为基础文件操作API，提供基础文件操作能力，包括文件基本管理、文件目录管理、文件信息统计、文件流式读写等常用功能。

> [!NOTE]
> 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。



#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { fileIo } from '@kit.CoreFileKit';
```



#### 使用说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

使用该功能模块对文件/目录进行操作前，需要先获取其应用沙箱路径，获取方式及其接口用法请参考：

```text
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let context = this.context;
    let pathDir = context.filesDir;
  }
}
```

获取沙箱路径的方式及其接口用法也可参考：[应用上下文Context-获取应用文件路径](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-context-stage#获取应用文件路径)。

将指向资源的字符串称为URI。对于只支持沙箱路径作为入参的接口，可以使用构造fileUri对象并获取其沙箱路径的属性的方式将URI转换为沙箱路径，然后使用文件接口。URI定义解及其转换方式请参考：[文件URI](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fileuri)。



#### fileIo.stat

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

stat(file: string | number): Promise&lt;Stat&gt;

获取文件或目录详细属性信息，使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string \| number | 是 | 文件或目录的应用沙箱路径path、URI或已打开的文件描述符fd。 说明：从API version 22开始，支持传入URI。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Stat&gt; | Promise对象。返回文件或目录的具体信息。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
fileIo.stat(filePath).then((stat: fileIo.Stat) => {
  console.info(`Succeeded in getting file info, the size of file is ${stat.size}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get file info. Code: ${err.code}, message: ${err.message}`);
});
```



#### fileIo.stat

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

stat(file: string | number, callback: AsyncCallback&lt;Stat&gt;): void

获取文件或目录的详细属性信息。使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string \| number | 是 | 文件或目录的应用沙箱路径path、URI或已打开的文件描述符fd。 说明：从API version 22开始，支持传入URI。 |
| callback | AsyncCallback&lt;Stat&gt; | 是 | 异步获取文件或目录的信息之后的回调。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

fileIo.stat(pathDir, (err: BusinessError, stat: fileIo.Stat) => {
  if (err) {
    console.error(`Failed to get file info. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting file info, the size of file is ${stat.size}`);
  }
});
```



#### fileIo.statSync

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

statSync(file: string | number): Stat

以同步方法获取文件或目录详细属性信息。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string \| number | 是 | 文件或目录的应用沙箱路径path、URI或已打开的文件描述符fd。 说明：从API version 22开始，支持传入URI。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Stat | 表示文件或目录的具体信息。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let stat = fileIo.statSync(pathDir);
console.info(`Succeeded in getting file info, the size of file is ${stat.size}`);
```



#### fileIo.access

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

access(path: string, mode?: AccessModeType): Promise&lt;boolean&gt;

检查文件或目录是否存在，或校验操作权限，使用promise异步回调。

校验读、写或读写权限不通过会抛出13900012（Permission denied）错误码。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件或目录应用沙箱路径。 |
| mode12+ | AccessModeType | 否 | 文件或目录校验的权限。不填该参数则默认校验文件是否存在。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回布尔值。返回true，表示文件存在；返回false，表示文件不存在。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
fileIo.access(filePath).then((res: boolean) => {
  if (res) {
    console.info(`Succeeded in checking file, file exists.`);
  } else {
    console.info(`Succeeded in checking file, file does not exist.`);
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to access. Code: ${err.code}, message: ${err.message}`);
});
```



#### fileIo.access12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

access(path: string, mode: AccessModeType, flag: AccessFlagType): Promise&lt;boolean&gt;

检查文件或目录是否在本地，或校验操作权限，使用promise异步回调。

校验读、写或读写权限不通过会抛出13900012（Permission denied）错误码。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件或目录应用沙箱路径。 |
| mode | AccessModeType | 是 | 文件或目录校验的权限。 |
| flag | AccessFlagType | 是 | 文件或目录校验的位置。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回布尔值。返回true，表示文件或目录在本地且校验权限存在；返回false，表示文件或目录不存在或者文件或目录在云端或其他分布式设备上。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
fileIo.access(filePath, fileIo.AccessModeType.EXIST, fileIo.AccessFlagType.LOCAL).then((res: boolean) => {
  if (res) {
    console.info(`Succeeded in checking file, file exists.`);
  } else {
    console.info(`Succeeded in checking file, file does not exist.`);
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to access. Code: ${err.code}, message: ${err.message}`);
});
```



#### fileIo.access

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

access(path: string, callback: AsyncCallback&lt;boolean&gt;): void

检查文件或目录是否存在。使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件或目录应用沙箱路径。 |
| callback | AsyncCallback&lt;boolean&gt; | 是 | 异步检查文件或目录是否存在的回调。如果存在，回调返回true；否则返回false。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
fileIo.access(filePath, (err: BusinessError, res: boolean) => {
  if (err) {
    console.error(`Failed to access. Code: ${err.code}, message: ${err.message}`);
  } else {
    if (res) {
      console.info(`Succeeded in checking file, file exists.`);
    } else {
      console.info(`Succeeded in checking file, file does not exist.`);
    }
  }
});
```



#### fileIo.accessSync

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

accessSync(path: string, mode?: AccessModeType): boolean

以同步方法检查文件或目录是否存在，或校验操作权限。

校验读、写或读写权限不通过会抛出13900012（Permission denied）错误码。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件或目录应用沙箱路径。 |
| mode12+ | AccessModeType | 否 | 文件或目录校验的权限。不填该参数则默认校验文件或目录是否存在。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true，表示文件存在；返回false，表示文件不存在。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
try {
  let res = fileIo.accessSync(filePath);
  if (res) {
    console.info(`Succeeded in checking file, file exists.`);
  } else {
    console.info(`Succeeded in checking file, file does not exist.`);
  }
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to accessSync. Code: ${err.code}, message: ${err.message}`);
}
```



#### fileIo.accessSync12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

accessSync(path: string, mode: AccessModeType, flag: AccessFlagType): boolean

以同步方法检查文件或目录是否在本地，或校验操作权限。

校验读、写或读写权限不通过会抛出13900012（Permission denied）错误码。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件应用沙箱路径。 |
| mode | AccessModeType | 是 | 文件或目录校验的权限。 |
| flag | AccessFlagType | 是 | 文件或目录校验的位置。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true，表示文件在本地且校验权限存在；返回false，表示文件不存在或者文件在云端或其他分布式设备上。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
try {
  let res = fileIo.accessSync(filePath, fileIo.AccessModeType.EXIST, fileIo.AccessFlagType.LOCAL);
  if (res) {
    console.info(`Succeeded in checking file, file exists.`);
  } else {
    console.info(`Succeeded in checking file, file does not exist.`);
  }
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to accessSync. Code: ${err.code}, message: ${err.message}`);
}
```



#### fileIo.close

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

close(file: number | File): Promise&lt;void&gt;

关闭文件或目录，使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | number \| File | 是 | 已打开的File对象或已打开的文件描述符fd。关闭后file对象或文件描述符fd不再具备实际意义，不可再用于进行读写等操作。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回值。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath);
fileIo.close(file).then(() => {
  console.info(`Succeeded in closing file.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to close file. Code: ${err.code}, message: ${err.message}`);
});
```



#### fileIo.close

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

close(file: number | File, callback: AsyncCallback&lt;void&gt;): void

关闭文件或目录。使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | number \| File | 是 | 已打开的File对象或已打开的文件描述符fd。关闭后file对象或文件描述符fd不再具备实际意义，不可再用于进行读写等操作。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 异步关闭文件或目录之后的回调。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath);
fileIo.close(file, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to close file. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in closing file.`);
  }
});
```



#### fileIo.closeSync

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

closeSync(file: number | File): void

以同步方法关闭文件或目录。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | number \| File | 是 | 已打开的File对象或已打开的文件描述符fd。关闭后file对象或文件描述符fd不再具备实际意义，不可再用于进行读写等操作。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath);
fileIo.closeSync(file);
```



#### fileIo.copy11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

copy(srcUri: string, destUri: string, options?: CopyOptions): Promise&lt;void&gt;

拷贝文件或目录，使用promise异步回调。

支持跨设备拷贝。强制覆盖拷贝。入参支持文件或目录URI。

跨端拷贝时，最多同时存在10个拷贝任务；单次拷贝的文件数量不得超过500个。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| srcUri | string | 是 | 待复制文件或目录的URI。 |
| destUri | string | 是 | 目标文件或目录的URI。 |
| options | CopyOptions | 否 | options中提供拷贝进度回调。不填该参数则无拷贝进度回调。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回值。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let srcDirPathLocal: string = pathDir + "/src";
let dstDirPathLocal: string = pathDir + "/dest";

let srcDirUriLocal: string = fileUri.getUriFromPath(srcDirPathLocal);
let dstDirUriLocal: string = fileUri.getUriFromPath(dstDirPathLocal);

let progressListener: fileIo.ProgressListener = (progress: fileIo.Progress) => {
  console.info(`progressSize: ${progress.processedSize}, totalSize: ${progress.totalSize}`);
};
let copyOption: fileIo.CopyOptions = {
  "progressListener" : progressListener
}
try {
  fileIo.copy(srcDirUriLocal, dstDirUriLocal, copyOption).then(()=>{
    console.info("Succeeded in copying.");
  }).catch((err: BusinessError)=>{
    console.error(`Failed to copy. Code: ${err.code}, message: ${err.message}`);
  })
} catch(err) {
  console.error(`Failed to copy.Code: ${err.code}, message: ${err.message}`);
}
```



#### fileIo.copy11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

copy(srcUri: string, destUri: string, callback: AsyncCallback&lt;void&gt;): void

拷贝文件或者目录。使用callback异步回调。

支持跨设备拷贝。强制覆盖拷贝。入参支持文件或目录URI。

跨端拷贝时，最多同时存在10个拷贝任务；单次拷贝的文件数量不得超过500个。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| srcUri | string | 是 | 待复制文件或目录的URI。 |
| destUri | string | 是 | 目标文件或目录的URI。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 异步拷贝之后的回调。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let srcDirPathLocal: string = pathDir + "/src";
let dstDirPathLocal: string = pathDir + "/dest";

let srcDirUriLocal: string = fileUri.getUriFromPath(srcDirPathLocal);
let dstDirUriLocal: string = fileUri.getUriFromPath(dstDirPathLocal);

try {
  fileIo.copy(srcDirUriLocal, dstDirUriLocal, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to copy. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info("Succeeded in copying.");
  })
} catch(err) {
  console.error(`Failed to copy. Code: ${err.code}, message: ${err.message}`);
}
```



#### fileIo.copy11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

copy(srcUri: string, destUri: string, options: CopyOptions, callback: AsyncCallback&lt;void&gt;): void

拷贝文件或者目录。使用callback异步回调。

支持跨设备拷贝。强制覆盖拷贝。入参支持文件或目录URI。

跨端拷贝时，最多同时存在10个拷贝任务；单次拷贝的文件数量不得超过500个。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| srcUri | string | 是 | 待复制文件或目录的URI。 |
| destUri | string | 是 | 目标文件或目录的URI。 |
| options | CopyOptions | 是 | 拷贝进度回调。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 异步拷贝之后的回调。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let srcDirPathLocal: string = pathDir + "/src";
let dstDirPathLocal: string = pathDir + "/dest";

let srcDirUriLocal: string = fileUri.getUriFromPath(srcDirPathLocal);
let dstDirUriLocal: string = fileUri.getUriFromPath(dstDirPathLocal);

try {
  let progressListener: fileIo.ProgressListener = (progress: fileIo.Progress) => {
    console.info(`progressSize: ${progress.processedSize}, totalSize: ${progress.totalSize}`);
  };
  let copyOption: fileIo.CopyOptions = {
    "progressListener" : progressListener
  }
  fileIo.copy(srcDirUriLocal, dstDirUriLocal, copyOption, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to copy. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info("Succeeded in copying.");
  })
} catch(err) {
  console.error(`Failed to copy. Code: ${err.code}, message: ${err.message}`);
}
```



#### fileIo.copyFile

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

copyFile(src: string | number, dest: string | number, mode?: number): Promise&lt;void&gt;

复制文件，使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string \| number | 是 | 待复制文件的路径或待复制文件的文件描述符。 |
| dest | string \| number | 是 | 目标文件路径或目标文件的文件描述符。 |
| mode | number | 否 | mode提供覆盖文件的选项，当前仅支持0，且默认为0。 0：完全覆盖目标文件，未覆盖部分将被裁切掉。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回值。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let srcPath = pathDir + "/srcDir/test.txt";
let dstPath = pathDir + "/dstDir/test.txt";
fileIo.copyFile(srcPath, dstPath, 0).then(() => {
  console.info(`Succeeded in copying file.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to copy file. Code: ${err.code}, message: ${err.message}`);
});
```



#### fileIo.copyFile

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

copyFile(src: string | number, dest: string | number, mode: number, callback: AsyncCallback&lt;void&gt;): void

复制文件，可设置覆盖文件的方式。使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string \| number | 是 | 待复制文件的路径或待复制文件的文件描述符。 |
| dest | string \| number | 是 | 目标文件路径或目标文件的文件描述符。 |
| mode | number | 是 | mode提供覆盖文件的选项，当前仅支持0，且默认为0。 0：完全覆盖目标文件，未覆盖部分将被裁切掉。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 异步复制文件之后的回调。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let srcPath = pathDir + "/srcDir/test.txt";
let dstPath = pathDir + "/dstDir/test.txt";
fileIo.copyFile(srcPath, dstPath, 0, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to copy file. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in copying file.`);
  }
});
```



#### fileIo.copyFile

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

copyFile(src: string | number, dest: string | number, callback: AsyncCallback&lt;void&gt;): void

复制文件，覆盖方式为完全覆盖目标文件，未覆盖部分将被裁切。使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string \| number | 是 | 待复制文件的路径或待复制文件的文件描述符。 |
| dest | string \| number | 是 | 目标文件路径或目标文件的文件描述符。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 异步复制文件之后的回调。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let srcPath = pathDir + "/srcDir/test.txt";
let dstPath = pathDir + "/dstDir/test.txt";
fileIo.copyFile(srcPath, dstPath, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to copy file. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in copying file.`);
  }
});
```



#### fileIo.copyFileSync

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

copyFileSync(src: string | number, dest: string | number, mode?: number): void

以同步方法复制文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string \| number | 是 | 待复制文件的路径或待复制文件的文件描述符。 |
| dest | string \| number | 是 | 目标文件路径或目标文件的文件描述符。 |
| mode | number | 否 | mode提供覆盖文件的选项，当前仅支持0，且默认为0。 0：完全覆盖目标文件，未覆盖部分将被裁切掉。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let srcPath = pathDir + "/srcDir/test.txt";
let dstPath = pathDir + "/dstDir/test.txt";
fileIo.copyFileSync(srcPath, dstPath);
```



#### fileIo.copyDir10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

copyDir(src: string, dest: string, mode?: number): Promise&lt;void&gt;

复制源目录至目标路径下，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 源目录的应用沙箱路径。 |
| dest | string | 是 | 目标目录的应用沙箱路径。 |
| mode | number | 否 | 复制模式，默认值为0。 - mode为0，文件级别抛异常。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则抛出异常。源目录下未冲突的文件全部拷贝至目标目录下，目标目录下未冲突文件将继续保留，且冲突文件信息将在抛出异常的data属性中以Array&lt;ConflictFiles&gt;形式提供。 - mode为1，文件级别强制覆盖。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则强制覆盖冲突目录下所有同名文件，未冲突文件将继续保留。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回值。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

// copy directory from srcPath to destPath
let srcPath = pathDir + "/srcDir/";
let destPath = pathDir + "/destDir/";
fileIo.copyDir(srcPath, destPath, 0).then(() => {
  console.info(`Succeeded in copying directory.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to copy directory. Code: ${err.code}, message: ${err.message}`);
});
```



#### fileIo.copyDir10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

copyDir(src: string, dest: string, mode: number, callback: AsyncCallback&lt;void&gt;): void

复制源目录至目标路径下，可设置复制模式。使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 源目录的应用沙箱路径。 |
| dest | string | 是 | 目标目录的应用沙箱路径。 |
| mode | number | 是 | 复制模式。 - mode为0，文件级别抛异常。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则抛出异常。源目录下未冲突的文件全部拷贝至目标目录下，目标目录下未冲突文件将继续保留。 - mode为1，文件级别强制覆盖。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则强制覆盖冲突目录下所有同名文件，未冲突文件将继续保留。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当复制目录成功，err为undefined，否则为错误对象。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

// copy directory from srcPath to destPath
let srcPath = pathDir + "/srcDir/";
let destPath = pathDir + "/destDir/";
fileIo.copyDir(srcPath, destPath, 0, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to copy directory. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in copying directory.`);
  }
});
```



#### fileIo.copyDir10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

copyDir(src: string, dest: string, mode: number, callback: AsyncCallback<void, Array&lt;ConflictFiles&gt;>): void

复制源目录至目标路径下，可设置复制模式。使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 源目录的应用沙箱路径。 |
| dest | string | 是 | 目标目录的应用沙箱路径。 |
| mode | number | 是 | 复制模式。 - mode为0，文件级别抛异常。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则抛出异常。源目录下未冲突的文件全部拷贝至目标目录下，目标目录下未冲突文件将继续保留，且冲突文件信息将在抛出异常的data属性中以Array&lt;ConflictFiles&gt;形式提供。 - mode为1，文件级别强制覆盖。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则强制覆盖冲突目录下所有同名文件，未冲突文件将继续保留。 |
| callback | AsyncCallback<void, Array&lt;ConflictFiles&gt;> | 是 | 异步复制目录之后的回调。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { ConflictFiles } from '@kit.CoreFileKit';

// copy directory from srcPath to destPath
let srcPath = pathDir + "/srcDir/";
let destPath = pathDir + "/destDir/";
fileIo.copyDir(srcPath, destPath, 0, (err: BusinessError<Array<ConflictFiles>>) => {
  if (err && err.code == 13900015 && err.data?.length !== undefined) {
    for (let i = 0; i < err.data.length; i++) {
      console.error(`Failed to copy directory, with conflicting files: ${err.data[i].srcFile} ${err.data[i].destFile}`);
    }
  } else if (err) {
    console.error(`Failed to copy directory. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in copying directory.`);
  }
});
```



#### fileIo.copyDir10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

copyDir(src: string, dest: string, callback: AsyncCallback&lt;void&gt;): void

复制源目录至目标路径下。使用callback异步回调。

如果目标目录下有与源目录名冲突的目录，且冲突目录下有同名文件，则抛出异常。源目录下未冲突的文件全部拷贝至目标目录下，目标目录下未冲突文件将继续保留。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 源目录的应用沙箱路径。 |
| dest | string | 是 | 目标目录的应用沙箱路径。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当复制目录成功，err为undefined，否则为错误对象。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

// copy directory from srcPath to destPath
let srcPath = pathDir + "/srcDir/";
let destPath = pathDir + "/destDir/";
fileIo.copyDir(srcPath, destPath, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to copy directory. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in copying directory.`);
  }
});
```



#### fileIo.copyDir10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

copyDir(src: string, dest: string, callback: AsyncCallback<void, Array&lt;ConflictFiles&gt;>): void

复制源目录至目标路径下。使用callback异步回调。

如果目标目录下有与源目录名冲突的目录，且冲突目录下有同名文件，则抛出异常。源目录下未冲突的文件全部拷贝至目标目录下，目标目录下未冲突文件将继续保留，且冲突文件信息将在抛出异常的data属性中以Array<[ConflictFiles](#conflictfiles10)>形式提供。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 源目录的应用沙箱路径。 |
| dest | string | 是 | 目标目录的应用沙箱路径。 |
| callback | AsyncCallback<void, Array&lt;ConflictFiles&gt;> | 是 | 异步复制目录之后的回调。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { ConflictFiles } from '@kit.CoreFileKit';

// copy directory from srcPath to destPath
let srcPath = pathDir + "/srcDir/";
let destPath = pathDir + "/destDir/";
fileIo.copyDir(srcPath, destPath, (err: BusinessError<Array<ConflictFiles>>) => {
  if (err && err.code == 13900015 && err.data?.length !== undefined) {
    for (let i = 0; i < err.data.length; i++) {
      console.error(`Failed to copy directory, with conflicting files: ${err.data[i].srcFile} ${err.data[i].destFile}`);
    }
  } else if (err) {
    console.error(`Failed to copy directory. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in copying directory.`);
  }
});
```



#### fileIo.copyDirSync10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

copyDirSync(src: string, dest: string, mode?: number): void

以同步方法复制源目录至目标路径下。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 源目录的应用沙箱路径。 |
| dest | string | 是 | 目标目录的应用沙箱路径。 |
| mode | number | 否 | 复制模式，默认值为0。 - mode为0，文件级别抛异常。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则抛出异常。源目录下未冲突的文件全部拷贝至目标目录下，目标目录下未冲突文件将继续保留，且冲突文件信息将在抛出异常的data属性中以Array&lt;ConflictFiles&gt;形式提供。 - mode为1，文件级别强制覆盖。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则强制覆盖冲突目录下所有同名文件，未冲突文件将继续保留。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

// copy directory from srcPath to destPath
let srcPath = pathDir + "/srcDir/";
let destPath = pathDir + "/destDir/";
try {
  fileIo.copyDirSync(srcPath, destPath, 0);
  console.info(`Succeeded in copying directory.`);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to copy directory. Code: ${err.code}, message: ${err.message}`);
}
```



#### fileIo.dup10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

dup(fd: number): File

复制文件描述符，并返回对应的File对象。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 文件描述符。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| File | 打开的File对象。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let filePath = pathDir + "/test.txt";
let file1 = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
let fd: number = file1.fd;
let file2 = fileIo.dup(fd);
console.info(`Succeeded in getting file name of the file2 is ${file2.name}`);
fileIo.closeSync(file1);
fileIo.closeSync(file2);
```



#### fileIo.connectDfs12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

connectDfs(networkId: string, listeners: DfsListeners): Promise&lt;void&gt;

业务调用connectDfs接口，触发建链。如果对端设备出现异常，业务执行回调DfsListeners内[onStatus](#onstatus12)通知应用。可参考[跨设备文件共享和访问](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/file-access-across-devices)文档进行开发。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| networkId | string | 是 | 设备的网络Id。通过distributedDeviceManager接口调用DeviceBasicInfo获得。 |
| listeners | DfsListeners | 是 | 分布式文件系统状态监听器。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回值。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { distributedDeviceManager } from '@kit.DistributedServiceKit';

let dmInstance = distributedDeviceManager.createDeviceManager("com.example.filesync");
let deviceInfoList: Array<distributedDeviceManager.DeviceBasicInfo> = dmInstance.getAvailableDeviceListSync();
if (deviceInfoList && deviceInfoList.length > 0) {
  console.info(`Succeeded in getting available device list.`);
  let networkId = deviceInfoList[0].networkId;
  let listeners: fileIo.DfsListeners = {
    onStatus(networkId, status) {
      console.info('onStatus');
    }
  };
  fileIo.connectDfs(networkId, listeners).then(() => {
    console.info("Succeeded in connecting dfs.");
  }).catch((err: BusinessError) => {
    console.error(`Failed to connectDfs. Code: ${err.code}, message: ${err.message}`);
  });
}
```



#### fileIo.disconnectDfs12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

disconnectDfs(networkId: string): Promise&lt;void&gt;

业务调用disconnectDfs接口，传入networkId参数，触发断链。可参考[跨设备文件共享和访问](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/file-access-across-devices)文档进行开发。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| networkId | string | 是 | 设备的网络Id。通过distributedDeviceManager接口调用DeviceBasicInfo获得。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回值。 |


**错误码：**

接口抛出错误码的详细介绍请参见[空间统计错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#空间统计错误码)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { distributedDeviceManager } from '@kit.DistributedServiceKit';

let dmInstance = distributedDeviceManager.createDeviceManager("com.example.filesync");
let deviceInfoList: Array<distributedDeviceManager.DeviceBasicInfo> = dmInstance.getAvailableDeviceListSync();
if (deviceInfoList && deviceInfoList.length > 0) {
  console.info(`Succeeded in getting available device list.`);
  let networkId = deviceInfoList[0].networkId;
  fileIo.disconnectDfs(networkId).then(() => {
    console.info("Succeeded in disconnecting dfs.");
  }).catch((err: BusinessError) => {
    console.error(`Failed to disconnect dfs. Code: ${err.code}, message: ${err.message}`);
  })
}
```



#### fileIo.setxattr12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setxattr(path: string, key: string, value: string): Promise&lt;void&gt;

设置文件或目录的扩展属性。使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件或目录的应用沙箱路径。 |
| key | string | 是 | 扩展属性的key。仅支持前缀为“user.”的字符串，且长度需小于256字节。 |
| value | string | 是 | 扩展属性的value。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回值。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let attrKey = "user.comment";
let attrValue = "Test file.";

fileIo.setxattr(filePath, attrKey, attrValue).then(() => {
  console.info(`Succeeded in setting extended attribute successfully.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to set extended attribute. Code: ${err.code}, message: ${err.message}`);
});
```



#### fileIo.setxattrSync12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setxattrSync(path: string, key: string, value: string): void

设置文件或目录的扩展属性。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件或目录的应用沙箱路径。 |
| key | string | 是 | 扩展属性的key。仅支持前缀为“user.”的字符串，且长度需小于256字节。 |
| value | string | 是 | 扩展属性的value。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let attrKey = "user.comment";
let attrValue = "Test file.";

try {
  fileIo.setxattrSync(filePath, attrKey, attrValue);
  console.info(`Succeeded in setting extended attribute successfully.`);
} catch (err) {
  console.error(`Failed to set extended attribute. Code: ${err.code}, message: ${err.message}`);
}
```



#### fileIo.getxattr12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getxattr(path: string, key: string): Promise&lt;string&gt;

获取文件或目录的扩展属性。使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件或目录的应用沙箱路径。 |
| key | string | 是 | 扩展属性的key。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise对象。返回扩展属性的value。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let attrKey = "user.comment";

fileIo.getxattr(filePath, attrKey).then((attrValue: string) => {
  console.info(`Succeeded in getting extended attribute, the value is: ${attrValue}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get extended attribute. Code: ${err.code}, message: ${err.message}`);
});
```



#### fileIo.getxattrSync12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getxattrSync(path: string, key: string): string

使用同步接口获取文件或目录的扩展属性。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件或目录的应用沙箱路径。 |
| key | string | 是 | 扩展属性的key。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回扩展属性的value。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let attrKey = "user.comment";

try {
  let attrValue = fileIo.getxattrSync(filePath, attrKey);
  console.info(`Succeeded in getting extended attribute, the value is: ${attrValue}`);
} catch (err) {
  console.error(`Failed to get extended attribute. Code: ${err.code}, message: ${err.message}`);
}
```



#### fileIo.mkdir

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

mkdir(path: string): Promise&lt;void&gt;

创建目录，使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目录的应用沙箱路径。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回值。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let dirPath = pathDir + "/testDir";
fileIo.mkdir(dirPath).then(() => {
  console.info(`Succeeded in making directory.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to make directory. Code: ${err.code}, message: ${err.message}`);
});
```



#### fileIo.mkdir11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

mkdir(path: string, recursion: boolean): Promise&lt;void&gt;

创建目录，使用promise异步回调。当recursion指定为true时，可递归创建目录。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目录的应用沙箱路径。 |
| recursion | boolean | 是 | 是否递归创建目录。recursion指定为true时，可递归创建目录。recursion指定为false时，仅可创建单层目录。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回值。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let dirPath = pathDir + "/testDir1/testDir2/testDir3";
fileIo.mkdir(dirPath, true).then(() => {
  console.info(`Succeeded in making directory.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to make directory. Code: ${err.code}, message: ${err.message}`);
});
```



#### fileIo.mkdir

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

mkdir(path: string, callback: AsyncCallback&lt;void&gt;): void

创建目录。使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目录的应用沙箱路径。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 异步创建目录操作完成之后的回调。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let dirPath = pathDir + "/testDir";
fileIo.mkdir(dirPath, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to make directory. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in making directory.`);
  }
});
```



#### fileIo.mkdir11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

mkdir(path: string, recursion: boolean, callback: AsyncCallback&lt;void&gt;): void

创建目录，当recursion指定为true，可递归创建目录。使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目录的应用沙箱路径。 |
| recursion | boolean | 是 | 是否递归创建目录。recursion指定为true时，可递归创建目录。recursion指定为false时，仅可创建单层目录。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 异步创建目录操作完成之后的回调。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let dirPath = pathDir + "/testDir1/testDir2/testDir3";
fileIo.mkdir(dirPath, true, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to make directory. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in making directory.`);
  }
});
```



#### fileIo.mkdirSync

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

mkdirSync(path: string): void

以同步方法创建目录。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目录的应用沙箱路径。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let dirPath = pathDir + "/testDir";
fileIo.mkdirSync(dirPath);
```



#### fileIo.mkdirSync11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

mkdirSync(path: string, recursion: boolean): void

以同步方法创建目录。当recursion指定为true，可递归创建目录。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目录的应用沙箱路径。 |
| recursion | boolean | 是 | 是否递归创建目录。recursion指定为true时，可递归创建目录。recursion指定为false时，仅可创建单层目录。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let dirPath = pathDir + "/testDir1/testDir2/testDir3";
fileIo.mkdirSync(dirPath, true);
```



#### fileIo.open

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

open(path: string, mode?: number): Promise&lt;File&gt;

打开文件或目录，使用promise异步回调。支持使用URI打开文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件或目录的应用沙箱路径或文件URI。 |
| mode | number | 否 | 打开文件或目录的OpenMode，必须指定如下选项中的一个，默认以只读方式打开： - OpenMode.READ_ONLY(0o0)：只读打开。 - OpenMode.WRITE_ONLY(0o1)：只写打开。 - OpenMode.READ_WRITE(0o2)：读写打开。 可以追加以下功能选项，以按位或的方式组合，默认情况下不追加任何额外选项。 - OpenMode.CREATE(0o100)：如果文件不存在，则创建文件。 - OpenMode.TRUNC(0o1000)：如果文件存在且文件具有写权限，则将其长度裁剪为零。 - OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到文件末尾。 - OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。 - OpenMode.DIR(0o200000)：如果path不指向目录，则出错。不允许附加写权限。 - OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。 - OpenMode.SYNC(0o4010000)：以同步IO方式打开文件。 - OpenMode.UNCACHE(0o10000000000)：读写文件不进行页缓存，从API版本26.0.0开始支持此选项。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;File&gt; | Promise对象。返回File对象。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
fileIo.open(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE).then((file: fileIo.File) => {
  console.info(`Succeeded in getting file fd: ${file.fd}`);
  fileIo.closeSync(file);
}).catch((err: BusinessError) => {
  console.error(`Failed to open file. Code: ${err.code}, message: ${err.message}`);
});
```



#### fileIo.open

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

open(path: string, mode: number, callback: AsyncCallback&lt;File&gt;): void

打开文件或目录，可设置打开文件的选项。使用callback异步回调。

支持使用URI打开文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件或目录的应用沙箱路径或URI。 |
| mode | number | 是 | 打开文件或目录的OpenMode，必须指定如下选项中的一个，默认以只读方式打开： - OpenMode.READ_ONLY(0o0)：只读打开。 - OpenMode.WRITE_ONLY(0o1)：只写打开。 - OpenMode.READ_WRITE(0o2)：读写打开。 给定如下功能选项，以按位或的方式追加，默认不给定任何额外选项： - OpenMode.CREATE(0o100)：若文件不存在，则创建文件。 - OpenMode.TRUNC(0o1000)：如果文件存在且文件具有写权限，则将其长度裁剪为零。 - OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到文件末尾。 - OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。 - OpenMode.DIR(0o200000)：如果path不指向目录，则出错。不允许附加写权限。 - OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。 - OpenMode.SYNC(0o4010000)：以同步IO的方式打开文件。 - OpenMode.UNCACHE(0o10000000000)：读写文件不进行页缓存，从API版本26.0.0开始支持此选项。 |
| callback | AsyncCallback&lt;File&gt; | 是 | 异步打开文件之后的回调。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
fileIo.open(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE, (err: BusinessError, file: fileIo.File) => {
  if (err) {
    console.error(`Failed to open. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting file fd: ${file.fd}`);
    fileIo.closeSync(file);
  }
});
```



#### fileIo.open

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

open(path: string, callback: AsyncCallback&lt;File&gt;): void

打开文件或目录，支持使用URI打开文件。使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件或目录的应用沙箱路径或URI。 |
| callback | AsyncCallback&lt;File&gt; | 是 | 异步打开文件之后的回调。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
fileIo.open(filePath, (err: BusinessError, file: fileIo.File) => {
  if (err) {
    console.error(`Failed to open. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting file fd: ${file.fd}`);
    fileIo.closeSync(file);
  }
});
```



#### fileIo.openSync

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

openSync(path: string, mode?: number): File

以同步方法打开文件或目录。支持使用URI打开文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 打开文件或目录的应用沙箱路径或URI。 |
| mode | number | 否 | 打开文件或目录的OpenMode，必须指定如下选项中的一个，默认以只读方式打开： - OpenMode.READ_ONLY(0o0)：只读打开。 - OpenMode.WRITE_ONLY(0o1)：只写打开。 - OpenMode.READ_WRITE(0o2)：读写打开。 给定如下功能选项，以按位或的方式追加，默认不给定任何额外选项： - OpenMode.CREATE(0o100)：若文件不存在，则创建文件。 - OpenMode.TRUNC(0o1000)：如果文件存在且文件具有写权限，则将其长度裁剪为零。 - OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到文件末尾。 - OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。 - OpenMode.DIR(0o200000)：如果path不指向目录，则出错。不允许附加写权限。 - OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。 - OpenMode.SYNC(0o4010000)：以同步IO的方式打开文件。 - OpenMode.UNCACHE(0o10000000000)：读写文件不进行页缓存，从API版本26.0.0开始支持此选项。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| File | 打开的File对象。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
console.info(`Succeeded in getting file fd: ${file.fd}`);
fileIo.closeSync(file);
```



#### fileIo.read

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

read(fd: number, buffer: ArrayBuffer, options?: ReadOptions): Promise&lt;number&gt;

读取文件数据，使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符。 |
| buffer | ArrayBuffer | 是 | 用于保存读取到的文件数据的缓冲区。 |
| options | ReadOptions | 否 | 支持如下选项： - offset，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。 - length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认缓冲区长度。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | Promise对象。返回实际读取的数据长度，单位为Byte。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
let arrayBuffer = new ArrayBuffer(4096);
fileIo.read(file.fd, arrayBuffer).then((readLen: number) => {
  let buf = buffer.from(arrayBuffer, 0, readLen);
  console.info(`Succeeded in reading file data. The content of file: ${buf.toString()}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to read file data. Code: ${err.code}, message: ${err.message}`);
}).finally(() => {
  fileIo.closeSync(file);
});
```



#### fileIo.read

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

read(fd: number, buffer: ArrayBuffer, callback: AsyncCallback&lt;number&gt;): void

从文件读取数据。使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符。 |
| buffer | ArrayBuffer | 是 | 用于保存读取到的文件数据的缓冲区。 |
| callback | AsyncCallback&lt;number&gt; | 是 | 异步读取数据之后的回调。返回实际读取的数据长度，单位为Byte。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
let arrayBuffer = new ArrayBuffer(4096);
fileIo.read(file.fd, arrayBuffer, (err: BusinessError, readLen: number) => {
  if (err) {
    console.error(`Failed to read. Code: ${err.code}, message: ${err.message}`);
  } else {
    let buf = buffer.from(arrayBuffer, 0, readLen);
    console.info(`Succeeded in reading file data. The content of file: ${buf.toString()}`);
  }
  fileIo.closeSync(file);
});
```



#### fileIo.read

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

read(fd: number, buffer: ArrayBuffer, options: ReadOptions, callback: AsyncCallback&lt;number&gt;): void

从文件读取数据，支持配置读取选项。使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符。 |
| buffer | ArrayBuffer | 是 | 用于保存读取到的文件数据的缓冲区。 |
| options | ReadOptions | 是 | 支持如下选项： - offset，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。 - length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认缓冲区长度。 |
| callback | AsyncCallback&lt;number&gt; | 是 | 回调函数，返回实际读取的数据长度，单位为Byte。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';
import { ReadOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
let arrayBuffer = new ArrayBuffer(4096);
let readOption: ReadOptions = {
  offset: 1,
  length: 5
};
fileIo.read(file.fd, arrayBuffer, readOption, (err: BusinessError, readLen: number) => {
  if (err) {
    console.error(`Failed to read. Code: ${err.code}, message: ${err.message}`);
  } else {
    let buf = buffer.from(arrayBuffer, 0, readLen);
    console.info(`Succeeded in reading file data. The content of file: ${buf.toString()}`);
  }
  fileIo.closeSync(file);
});
```



#### fileIo.readSync

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

readSync(fd: number, buffer: ArrayBuffer, options?: ReadOptions): number

以同步方法从文件读取数据。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符。 |
| buffer | ArrayBuffer | 是 | 用于保存读取到的文件数据的缓冲区。 |
| options | ReadOptions | 否 | 支持如下选项： - offset，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。 - length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认缓冲区长度。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回实际读取的数据长度，单位为Byte。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE);
let buf = new ArrayBuffer(4096);
fileIo.readSync(file.fd, buf);
fileIo.closeSync(file);
```



#### fileIo.rmdir

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

rmdir(path: string): Promise&lt;void&gt;

删除目录及其所有子目录和文件，使用promise异步回调。

> [!NOTE]
> 该接口支持删除单个文件，但不推荐使用此方法删除单个文件，推荐使用unlink接口删除单个文件。


**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目录的应用沙箱路径。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回值。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let dirPath = pathDir + "/testDir";
fileIo.rmdir(dirPath).then(() => {
  console.info(`Succeeded in removing directory.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to remove directory. Code: ${err.code}, message: ${err.message}`);
});
```



#### fileIo.rmdir

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

rmdir(path: string, callback: AsyncCallback&lt;void&gt;): void

删除目录及其所有子目录和文件。使用callback异步回调。

> [!NOTE]
> 该接口支持删除单个文件，但不推荐使用此方法删除单个文件，推荐使用unlink接口删除单个文件。


**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目录的应用沙箱路径。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 异步删除目录之后的回调。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let dirPath = pathDir + "/testDir";
fileIo.rmdir(dirPath, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to remove directory. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in removing directory.`);
  }
});
```



#### fileIo.rmdirSync

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

rmdirSync(path: string): void

以同步方法删除目录及其所有子目录和文件。

> [!NOTE]
> 该接口支持删除单个文件，但不推荐使用此方法删除单个文件，推荐使用unlinkSync接口删除单个文件。


**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目录的应用沙箱路径。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let dirPath = pathDir + "/testDir";
fileIo.rmdirSync(dirPath);
```



#### fileIo.unlink

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

unlink(path: string): Promise&lt;void&gt;

删除单个文件，使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件的应用沙箱路径。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回值。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
fileIo.unlink(filePath).then(() => {
  console.info(`Succeeded in removing file.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to remove file. Code: ${err.code}, message: ${err.message}`);
});
```



#### fileIo.unlink

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

unlink(path: string, callback: AsyncCallback&lt;void&gt;): void

删除文件。使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件的应用沙箱路径。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 异步删除文件之后的回调。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
fileIo.unlink(filePath, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to remove file. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in removing file.`);
  }
});
```



#### fileIo.unlinkSync

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

unlinkSync(path: string): void

以同步方法删除文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件的应用沙箱路径。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let filePath = pathDir + "/test.txt";
fileIo.unlinkSync(filePath);
```



#### fileIo.write

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

write(fd: number, buffer: ArrayBuffer | string, options?: WriteOptions): Promise&lt;number&gt;

将数据写入文件，使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符。 |
| buffer | ArrayBuffer \| string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | WriteOptions | 否 | 支持如下选项： - offset，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写入。 - length，number类型，表示期望写入数据的长度，单位为Byte。可选，默认缓冲区长度。 - encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。当前仅支持 'utf-8'。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | Promise对象。返回实际写入的数据长度，单位为Byte。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let str: string = "hello, world";
fileIo.write(file.fd, str).then((writeLen: number) => {
  console.info(`Succeeded in writing data to file, size is: ${writeLen}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to write data to file. Code: ${err.code}, message: ${err.message}`);
}).finally(() => {
  fileIo.closeSync(file);
});
```



#### fileIo.write

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

write(fd: number, buffer: ArrayBuffer | string, callback: AsyncCallback&lt;number&gt;): void

将数据写入文件。使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符。 |
| buffer | ArrayBuffer \| string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| callback | AsyncCallback&lt;number&gt; | 是 | 回调函数，返回实际写入的数据长度，单位为Byte。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let str: string = "hello, world";
fileIo.write(file.fd, str, (err: BusinessError, writeLen: number) => {
  if (err) {
    console.error(`Failed to write data to file. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in writing data to file, size is: ${writeLen}`);
  }
  fileIo.closeSync(file);
});
```



#### fileIo.write

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

write(fd: number, buffer: ArrayBuffer | string, options: WriteOptions, callback: AsyncCallback&lt;number&gt;): void

将数据写入文件，支持配置写入选项。使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符。 |
| buffer | ArrayBuffer \| string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | WriteOptions | 是 | 支持如下选项： - offset，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。 - length，number类型，表示期望写入数据的长度，单位为Byte。可选，默认缓冲区长度。 - encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。当前仅支持 'utf-8'。 |
| callback | AsyncCallback&lt;number&gt; | 是 | 回调函数，返回实际写入的数据长度，单位为Byte。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { WriteOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let str: string = "hello, world";
let writeOptions: WriteOptions = {
  offset: 1,
  length: 5
};
fileIo.write(file.fd, str, writeOptions, (err: BusinessError, writeLen: number) => {
  if (err) {
    console.error(`Failed to write data to file. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in writing data to file, size is: ${writeLen}`);
  }
  fileIo.closeSync(file);
});
```



#### fileIo.writeSync

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

writeSync(fd: number, buffer: ArrayBuffer | string, options?: WriteOptions): number

以同步方法将数据写入文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符。 |
| buffer | ArrayBuffer \| string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | WriteOptions | 否 | 支持如下选项： - offset，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。 - length，number类型，表示期望写入数据的长度，单位为Byte。可选，默认缓冲区长度。 - encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。当前仅支持 'utf-8'。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回实际写入的数据长度，单位为Byte。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let str: string = "hello, world";
let writeLen = fileIo.writeSync(file.fd, str);
console.info(`Succeeded in writing data to file, size is: ${writeLen}`);
fileIo.closeSync(file);
```



#### fileIo.truncate

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

truncate(file: string | number, len?: number): Promise&lt;void&gt;

截断文件，使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string \| number | 是 | 文件的应用沙箱路径或已打开的文件描述符fd。 |
| len | number | 否 | 文件截断后的长度，单位为Byte。默认为0。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回值。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let len: number = 5;
fileIo.truncate(filePath, len).then(() => {
  console.info(`Succeeded in truncating file.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to truncate file. Code: ${err.code}, message: ${err.message}`);
});
```



#### fileIo.truncate

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

truncate(file: string | number, callback: AsyncCallback&lt;void&gt;): void

截断文件。使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string \| number | 是 | 文件的应用沙箱路径或已打开的文件描述符fd。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当截断文件成功，err为undefined，否则为错误对象。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
fileIo.truncate(filePath, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to truncate. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in truncating.`);
  }
});
```



#### fileIo.truncate

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

truncate(file: string | number, len: number, callback: AsyncCallback&lt;void&gt;): void

截断文件，支持配置文件截断后的长度。使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string \| number | 是 | 文件的应用沙箱路径或已打开的文件描述符fd。 |
| len | number | 是 | 文件截断后的长度，单位为Byte。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当截断文件成功，err为undefined，否则为错误对象。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let len: number = 5;
fileIo.truncate(filePath, len, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to truncate. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in truncating.`);
  }
});
```



#### fileIo.truncateSync

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

truncateSync(file: string | number, len?: number): void

以同步方法截断文件内容。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string \| number | 是 | 文件的应用沙箱路径或已打开的文件描述符fd。 |
| len | number | 否 | 文件截断后的长度，单位为Byte。默认为0。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let filePath = pathDir + "/test.txt";
let len: number = 5;
fileIo.truncateSync(filePath, len);
```



#### fileIo.readLines11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

readLines(filePath: string, options?: Options): Promise&lt;ReaderIterator&gt;

逐行读取文件文本内容，只支持读取utf-8格式文件。使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filePath | string | 是 | 文件的应用沙箱路径。 |
| options | Options | 否 | 可选项。支持以下选项： - encoding，string类型，当数据是 string 类型时有效，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;ReaderIterator&gt; | Promise对象。返回文件读取迭代器。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { Options } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let options: Options = {
  encoding: 'utf-8'
};
fileIo.readLines(filePath, options).then((readerIterator: fileIo.ReaderIterator) => {
  for (let it = readerIterator.next(); !it.done; it = readerIterator.next()) {
    console.info(`Succeeded in reading lines, content: ${it.value}`);
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to read lines. Code: ${err.code}, message: ${err.message}`);
});
```



#### fileIo.readLines11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

readLines(filePath: string, callback: AsyncCallback&lt;ReaderIterator&gt;): void

逐行读取文件文本内容，只支持读取utf-8格式文件。使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filePath | string | 是 | 文件的应用沙箱路径。 |
| callback | AsyncCallback&lt;ReaderIterator&gt; | 是 | 回调函数，返回文件读取迭代器。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
fileIo.readLines(filePath, (err: BusinessError, readerIterator: fileIo.ReaderIterator) => {
  if (err) {
    console.error(`Failed to read lines. Code: ${err.code}, message: ${err.message}`);
  } else {
    for (let it = readerIterator.next(); !it.done; it = readerIterator.next()) {
      console.info(`Succeeded in reading lines, content: ${it.value}`);
    }
  }
});
```



#### fileIo.readLines11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

readLines(filePath: string, options: Options, callback: AsyncCallback&lt;ReaderIterator&gt;): void

逐行读取文件文本内容，可配置读取选项，只支持读取utf-8格式文件。使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filePath | string | 是 | 文件的应用沙箱路径。 |
| options | Options | 是 | 读取选项。支持以下选项： - encoding，string类型，当数据是 string 类型时有效，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。 |
| callback | AsyncCallback&lt;ReaderIterator&gt; | 是 | 回调函数，返回文件读取迭代器。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { Options } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let options: Options = {
  encoding: 'utf-8'
};
fileIo.readLines(filePath, options, (err: BusinessError, readerIterator: fileIo.ReaderIterator) => {
  if (err) {
    console.error(`Failed to read lines. Code: ${err.code}, message: ${err.message}`);
  } else {
    for (let it = readerIterator.next(); !it.done; it = readerIterator.next()) {
      console.info(`Succeeded in reading lines, content: ${it.value}`);
    }
  }
});
```



#### fileIo.readLinesSync11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

readLinesSync(filePath: string, options?: Options): ReaderIterator

以同步方式逐行读取文件的文本内容。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filePath | string | 是 | 文件的应用沙箱路径。 |
| options | Options | 否 | 可选项。支持以下选项： - encoding，string类型，当数据是 string 类型时有效，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| ReaderIterator | 返回文件读取迭代器。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { Options } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let options: Options = {
  encoding: 'utf-8'
};
let readerIterator = fileIo.readLinesSync(filePath, options);
for (let it = readerIterator.next(); !it.done; it = readerIterator.next()) {
  console.info(`Succeeded in reading lines, content: ${it.value}`);
}
```



#### ReaderIterator11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

文件读取迭代器。在调用ReaderIterator的方法前，需要先通过readLines方法（同步或异步）来构建一个ReaderIterator实例。



#### next11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

next(): ReaderIteratorResult

获取迭代器下一项内容。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ReaderIteratorResult | 文件读取迭代器返回结果。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

> [!NOTE]
> 如果ReaderIterator读取的当前行的编码方式不是'utf-8'，接口返回错误码13900037。


**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { Options } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let options: Options = {
  encoding: 'utf-8'
};
fileIo.readLines(filePath, options).then((readerIterator: fileIo.ReaderIterator) => {
  for (let it = readerIterator.next(); !it.done; it = readerIterator.next()) {
    console.info(`Succeeded in reading lines, content: ${it.value}`);
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to read lines. Code: ${err.code}, message: ${err.message}`);
});
```



#### ReaderIteratorResult11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

文件读取迭代器返回结果，支持ReaderIterator接口使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| done | boolean | 迭代器是否已完成迭代。true：已完成迭代；false：未完成迭代。 |
| value | string | 逐行读取的文件文本内容。 |




#### fileIo.readText

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

readText(filePath: string, options?: ReadTextOptions): Promise&lt;string&gt;

基于文本方式读取文件（即直接读取文件的文本内容），使用promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filePath | string | 是 | 文件的应用沙箱路径。 |
| options | ReadTextOptions | 否 | 支持如下选项： - offset，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读取。 - length，number类型，表示期望读取数据，单位为Byte。可选，默认文件长度。 - encoding，string类型，当数据是 string 类型时有效，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise对象。返回读取文件的内容。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
fileIo.readText(filePath).then((str: string) => {
  console.info(`Succeeded in reading text, text is: ${str}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to read text. Code: ${err.code}, message: ${err.message}`);
});
```



#### fileIo.readText

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

readText(filePath: string, callback: AsyncCallback&lt;string&gt;): void

基于文本方式读取文件内容。使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filePath | string | 是 | 文件的应用沙箱路径。 |
| callback | AsyncCallback&lt;string&gt; | 是 | 回调函数，返回读取文件的内容。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
fileIo.readText(filePath, (err: BusinessError, str: string) => {
  if (err) {
    console.error(`Failed to read text. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in reading text, text is: ${str}`);
  }
});
```



#### fileIo.readText

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

readText(filePath: string, options: ReadTextOptions, callback: AsyncCallback&lt;string&gt;): void

基于文本方式读取文件内容，支持配置读取选项。使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filePath | string | 是 | 文件的应用沙箱路径。 |
| options | ReadTextOptions | 是 | 支持如下选项： - offset，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读取。 - length，number类型，表示期望读取数据，单位为Byte。可选，默认文件长度。 - encoding，string类型，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。 |
| callback | AsyncCallback&lt;string&gt; | 是 | 回调函数，返回读取文件的内容。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { ReadTextOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let stat = fileIo.statSync(filePath);
let readTextOption: ReadTextOptions = {
    offset: 1,
    length: stat.size,
    encoding: 'utf-8'
};
fileIo.readText(filePath, readTextOption, (err: BusinessError, str: string) => {
  if (err) {
    console.error(`Failed to read text. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in reading text, text is: ${str}`);
  }
});
```



#### fileIo.readTextSync

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

readTextSync(filePath: string, options?: ReadTextOptions): string

以同步方法基于文本方式读取文件（即直接读取文件的文本内容）。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filePath | string | 是 | 文件的应用沙箱路径。 |
| options | ReadTextOptions | 否 | 支持如下选项： - offset，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读取。 - length，number类型，表示期望读取数据，单位为Byte。可选，默认文件长度。 - encoding，string类型，当数据是 string 类型时有效，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回读取文件的内容。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { ReadTextOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let readTextOptions: ReadTextOptions = {
  offset: 1,
  length: 0,
  encoding: 'utf-8'
};
let stat = fileIo.statSync(filePath);
readTextOptions.length = stat.size;
let str = fileIo.readTextSync(filePath, readTextOptions);
console.info(`Succeeded in reading text, text is: ${str}`);
```



#### fileIo.lstat

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

lstat(path: string): Promise&lt;Stat&gt;

获取符号链接文件信息，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件的应用沙箱路径path或URI。 说明：从API version 22开始，支持传入URI。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Stat&gt; | Promise对象。返回Stat对象，表示文件的具体信息，详情见Stat。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/linkToFile";
fileIo.lstat(filePath).then((stat: fileIo.Stat) => {
  console.info(`Succeeded in getting symbolic link info, the size of file is ${stat.size}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get symbolic link info. Code: ${err.code}, message: ${err.message}`);
});
```



#### fileIo.lstat

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

lstat(path: string, callback: AsyncCallback&lt;Stat&gt;): void

获取符号链接文件信息。使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件的应用沙箱路径path或URI。 说明：从API version 22开始，支持传入URI。 |
| callback | AsyncCallback&lt;Stat&gt; | 是 | 异步获取文件具体信息之后的回调。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/linkToFile";
fileIo.lstat(filePath, (err: BusinessError, stat: fileIo.Stat) => {
  if (err) {
    console.error(`Failed to get symbolic link info. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting symbolic link info, the size of file is ${stat.size}`);
  }
});
```



#### fileIo.lstatSync

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

lstatSync(path: string): Stat

以同步方法获取符号链接文件信息。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件的应用沙箱路径path或URI。 说明：从API version 22开始，支持传入URI。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Stat | 表示文件的具体信息。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let filePath = pathDir + "/linkToFile";
let fileStat = fileIo.lstatSync(filePath);
console.info(`Succeeded in getting symbolic link info, the size of file is ${fileStat.size}`);
```



#### fileIo.rename

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

rename(oldPath: string, newPath: string): Promise&lt;void&gt;

重命名文件或目录，使用promise异步回调。

> [!NOTE]
> 该接口不支持在分布式文件路径下操作。


**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| oldPath | string | 是 | 文件的应用沙箱原路径。 |
| newPath | string | 是 | 文件的应用沙箱新路径。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回值。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + "/new.txt";
fileIo.rename(srcFile, dstFile).then(() => {
  console.info(`Succeeded in renaming.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to rename. Code: ${err.code}, message: ${err.message}`);
});
```



#### fileIo.rename

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

rename(oldPath: string, newPath: string, callback: AsyncCallback&lt;void&gt;): void

重命名文件或目录。使用callback异步回调。

> [!NOTE]
> 该接口不支持在分布式文件路径下操作。


**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| oldPath | string | 是 | 文件的应用沙箱原路径。 |
| newPath | string | 是 | 文件的应用沙箱新路径。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 异步重命名文件之后的回调。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + "/new.txt";
fileIo.rename(srcFile, dstFile, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to rename. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in renaming.`);
  }
});
```



#### fileIo.renameSync

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

renameSync(oldPath: string, newPath: string): void

以同步方法重命名文件或目录。

> [!NOTE]
> 该接口不支持在分布式文件路径下操作。


**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| oldPath | string | 是 | 文件的应用沙箱原路径。 |
| newPath | string | 是 | 文件的应用沙箱新路径。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + "/new.txt";
fileIo.renameSync(srcFile, dstFile);
```



#### fileIo.fsync

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

fsync(fd: number): Promise&lt;void&gt;

将文件系统缓存数据写入磁盘，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回值。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath);
fileIo.fsync(file.fd).then(() => {
  console.info(`Succeeded in syncing data.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to sync data. Code: ${err.code}, message: ${err.message}`);
}).finally(() => {
  fileIo.closeSync(file);
});
```



#### fileIo.fsync

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

fsync(fd: number, callback: AsyncCallback&lt;void&gt;): void

将文件系统缓存数据写入磁盘。使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 异步将文件数据同步之后的回调。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath);
fileIo.fsync(file.fd, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to sync. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in syncing.`);
  }
  fileIo.closeSync(file);
});
```



#### fileIo.fsyncSync

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

fsyncSync(fd: number): void

以同步方法将文件系统缓存数据写入磁盘。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath);
fileIo.fsyncSync(file.fd);
fileIo.closeSync(file);
```



#### fileIo.fdatasync

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

fdatasync(fd: number): Promise&lt;void&gt;

实现文件内容数据同步，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回值。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath);
fileIo.fdatasync(file.fd).then(() => {
  console.info(`Succeeded in syncing data.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to sync data. Code: ${err.code}, message: ${err.message}`);
}).finally(() => {
  fileIo.closeSync(file);
});
```



#### fileIo.fdatasync

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

fdatasync(fd: number, callback: AsyncCallback&lt;void&gt;): void

实现文件内容数据同步。使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 异步将文件内容数据同步之后的回调。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath);
fileIo.fdatasync(file.fd, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to syncing data. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in syncing data.`);
  }
  fileIo.closeSync(file);
});
```



#### fileIo.fdatasyncSync

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

fdatasyncSync(fd: number): void

以同步方法实现文件内容的数据同步。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath);
fileIo.fdatasyncSync(file.fd);
fileIo.closeSync(file);
```



#### fileIo.symlink

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

symlink(target: string, srcPath: string): Promise&lt;void&gt;

基于文件路径创建符号链接，使用promise异步回调。

> [!NOTE]
> 从API version 11开始，不支持三方应用使用。


**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | string | 是 | 要链接的目标文件的应用沙箱路径。 |
| srcPath | string | 是 | 符号链接文件的应用沙箱路径。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回值。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + "/test";
fileIo.symlink(srcFile, dstFile).then(() => {
  console.info(`Succeeded in creating symbolic link.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to create symbolic link. Code: ${err.code}, message: ${err.message}`);
});
```



#### fileIo.symlink

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

symlink(target: string, srcPath: string, callback: AsyncCallback&lt;void&gt;): void

基于文件路径创建符号链接。使用callback异步回调。

> [!NOTE]
> 从API version 11开始，不支持三方应用使用。


**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | string | 是 | 要链接的目标文件的应用沙箱路径。 |
| srcPath | string | 是 | 符号链接文件的应用沙箱路径。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 异步创建符号链接信息之后的回调。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + "/test";
fileIo.symlink(srcFile, dstFile, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to create symbolic link. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in creating symbolic link.`);
  }
});
```



#### fileIo.symlinkSync

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

symlinkSync(target: string, srcPath: string): void

以同步的方法基于文件路径创建符号链接。

> [!NOTE]
> 从API version 11开始，不支持三方应用使用。


**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | string | 是 | 要链接的目标文件的应用沙箱路径。 |
| srcPath | string | 是 | 符号链接文件的应用沙箱路径。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + "/test";
fileIo.symlinkSync(srcFile, dstFile);
```



#### fileIo.listFile

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

listFile(path: string, options?: ListFileOptions): Promise<string[]>

默认列出当前目录下所有文件名和目录名。支持过滤。使用promise异步回调。

可通过配置ListFileOptions中recursion参数实现递归列出所有文件的相对路径，相对路径以“/”开头。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目录的应用沙箱路径。 |
| options | ListFileOptions | 否 | 文件过滤选项。默认不进行过滤。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string[]> | Promise对象。返回文件名数组，默认以'utf-8'编码。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { Filter, ListFileOptions } from '@kit.CoreFileKit';

let listFileOption: ListFileOptions = {
  recursion: false,
  listNum: 0,
  filter: {
    suffix: [".png", ".jpg", ".jpeg"],
    displayName: ["*abc", "efg*"],
    fileSizeOver: 1024
  }
}
fileIo.listFile(pathDir, listFileOption).then((filenames: Array<string>) => {
  console.info(`Succeeded in listing file.`);
  for (let i = 0; i < filenames.length; i++) {
    console.info(`Succeeded in listing file, file name: ${filenames[i]}`);
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to list file. Code: ${err.code}, message: ${err.message}`);
});
```



#### fileIo.listFile

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

listFile(path: string, callback: AsyncCallback<string[]>): void

默认列出当前目录下所有文件名和目录名。使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目录的应用沙箱路径。 |
| callback | AsyncCallback<string[]> | 是 | 异步列出文件名数组之后的回调，默认以'utf-8'编码。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

fileIo.listFile(pathDir, (err: BusinessError, filenames: Array<string>) => {
  if (err) {
    console.error(`Failed to list file. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in listing file.`);
    for (let i = 0; i < filenames.length; i++) {
      console.info(`Succeeded in listing file, file name: ${filenames[i]}`);
    }
  }
});
```



#### fileIo.listFile

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

listFile(path: string, options: ListFileOptions, callback: AsyncCallback<string[]>): void

默认列出当前目录下所有文件名和目录名。支持过滤。使用callback异步回调。

可通过配置ListFileOptions中recursion参数实现递归列出所有文件的相对路径，相对路径以“/”开头。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目录的应用沙箱路径。 |
| options | ListFileOptions | 是 | 文件过滤选项。 |
| callback | AsyncCallback<string[]> | 是 | 异步列出文件名数组之后的回调，默认以'utf-8'编码。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { Filter, ListFileOptions } from '@kit.CoreFileKit';

let listFileOption: ListFileOptions = {
  recursion: false,
  listNum: 0,
  filter: {
    suffix: [".png", ".jpg", ".jpeg"],
    displayName: ["*abc", "efg*"],
    fileSizeOver: 1024
  }
};
fileIo.listFile(pathDir, listFileOption, (err: BusinessError, filenames: Array<string>) => {
  if (err) {
    console.error(`Failed to list file. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in listing file.`);
    for (let i = 0; i < filenames.length; i++) {
      console.info(`Succeeded in listing file, file name: ${filenames[i]}`);
    }
  }
});
```



#### fileIo.listFileSync

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

listFileSync(path: string, options?: ListFileOptions): string[]

默认以同步方式列出当前目录下所有文件名和目录名。支持过滤。

可通过配置ListFileOptions中recursion参数实现递归列出所有文件的相对路径，相对路径以“/”开头。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目录的应用沙箱路径。 |
| options | ListFileOptions | 否 | 文件过滤选项。默认不进行过滤。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | 返回文件名数组，默认以'utf-8'编码。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { Filter, ListFileOptions} from '@kit.CoreFileKit';

let listFileOption: ListFileOptions = {
  recursion: false,
  listNum: 0,
  filter: {
    suffix: [".png", ".jpg", ".jpeg"],
    displayName: ["*abc", "efg*"],
    fileSizeOver: 1024
  }
};
let filenames = fileIo.listFileSync(pathDir, listFileOption);
console.info(`Succeeded in listing file.`);
for (let i = 0; i < filenames.length; i++) {
  console.info(`Succeeded in listing file, file name: ${filenames[i]}`);
}
```



#### fileIo.lseek11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

lseek(fd: number, offset: number, whence?: WhenceType): number

调整文件偏移指针位置。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 文件描述符。 |
| offset | number | 是 | 相对偏移位置，单位为Byte。 |
| whence | WhenceType | 否 | 偏移指针相对位置类型。不指定则默认为文件起始位置处。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前文件偏移指针位置（相对于文件头的偏移量，单位为Byte）。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
let offset = fileIo.lseek(file.fd, 5, fileIo.WhenceType.SEEK_SET);
console.info(`Succeeded in seeking, the current offset is at ${offset}`);
fileIo.closeSync(file);
```



#### fileIo.moveDir10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

moveDir(src: string, dest: string, mode?: number): Promise&lt;void&gt;

移动源目录至目标路径下，使用promise异步回调。

> [!NOTE]
> 该接口不支持在分布式文件路径下操作。


**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 源目录的应用沙箱路径。 |
| dest | string | 是 | 目标目录的应用沙箱路径。 |
| mode | number | 否 | 移动模式，默认值为0。 - mode为0，目录级别抛异常。若目标目录下存在与源目录名冲突的非空目录，则抛出异常。 - mode为1，文件级别抛异常。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则抛出异常。源目录下未冲突的文件全部移动至目标目录下，目标目录下未冲突文件将继续保留，且冲突文件信息将在抛出异常的data属性中以Array&lt;ConflictFiles&gt;形式提供。 - mode为2，文件级别强制覆盖。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则强制覆盖冲突目录下所有同名文件，未冲突文件将继续保留。 - mode为3，目录级别强制覆盖。移动源目录至目标目录下，目标目录下移动的目录内容与源目录完全一致。若目标目录下存在与源目录名冲突的目录，该目录下的所有原始文件将被删除。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回值。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let srcPath = pathDir + "/srcDir";
let destPath = pathDir + "/destDir";
fileIo.moveDir(srcPath, destPath, 1).then(() => {
  console.info(`Succeeded in moving directory.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to move directory. Code: ${err.code}, message: ${err.message}`);
});
```



#### fileIo.moveDir10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

moveDir(src: string, dest: string, mode: number, callback: AsyncCallback&lt;void&gt;): void

移动源目录至目标路径下，支持设置移动模式。使用callback异步回调。

> [!NOTE]
> 该接口不支持在分布式文件路径下操作。


**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 源目录的应用沙箱路径。 |
| dest | string | 是 | 目标目录的应用沙箱路径。 |
| mode | number | 是 | 移动模式。 - mode为0，目录级别抛异常。若目标目录下存在与源目录名冲突的目录，则抛出异常。 - mode为1，文件级别抛异常。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则抛出异常。源目录下未冲突的文件全部移动至目标目录下，目标目录下未冲突文件将继续保留。 - mode为2，文件级别强制覆盖。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则强制覆盖冲突目录下所有同名文件，未冲突文件将继续保留。 - mode为3，目录级别强制覆盖。移动源目录至目标目录下，目标目录下移动的目录内容与源目录完全一致。若目标目录下存在与源目录名冲突的目录，该目录下所有原始文件将被删除。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当移动目录成功，err为undefined，否则为错误对象。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let srcPath = pathDir + "/srcDir";
let destPath = pathDir + "/destDir";
fileIo.moveDir(srcPath, destPath, 1, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to move directory. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in moving directory.`);
  }
});
```



#### fileIo.moveDir10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

moveDir(src: string, dest: string, mode: number, callback: AsyncCallback<void, Array&lt;ConflictFiles&gt;>): void

移动源目录至目标路径下，支持设置移动模式。使用callback异步回调。

> [!NOTE]
> 该接口不支持在分布式文件路径下操作。


**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 源目录的应用沙箱路径。 |
| dest | string | 是 | 目标目录的应用沙箱路径。 |
| mode | number | 是 | 移动模式。 - mode为0，目录级别抛异常。若目标目录下存在与源目录名冲突的目录，则抛出异常。 - mode为1，文件级别抛异常。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则抛出异常。源目录下未冲突的文件全部移动至目标目录下，目标目录下未冲突文件将继续保留，且冲突文件信息将在抛出异常的data属性中以Array&lt;ConflictFiles&gt;形式提供。 - mode为2，文件级别强制覆盖。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则强制覆盖冲突目录下所有同名文件，未冲突文件将继续保留。 - mode为3，目录级别强制覆盖。移动源目录至目标目录下，目标目录下移动的目录内容与源目录完全一致。若目标目录下存在与源目录名冲突的目录，该目录下所有原始文件将被删除。 |
| callback | AsyncCallback<void, Array&lt;ConflictFiles&gt;> | 是 | 回调函数。当移动目录成功，err为undefined，否则为错误对象。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { ConflictFiles } from '@kit.CoreFileKit';

let srcPath = pathDir + "/srcDir";
let destPath = pathDir + "/destDir";
fileIo.moveDir(srcPath, destPath, 1, (err: BusinessError<Array<ConflictFiles>>) => {
  if (err && err.code == 13900015 && err.data?.length !== undefined) {
    for (let i = 0; i < err.data.length; i++) {
      console.error(`Failed to move directory, with conflicting files: ${err.data[i].srcFile} ${err.data[i].destFile}`);
    }
  } else if (err) {
    console.error(`Failed to move directory. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in moving directory.`);
  }
});
```



#### fileIo.moveDir10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

moveDir(src: string, dest: string, callback: AsyncCallback&lt;void&gt;): void

移动源目录至目标路径下。使用callback异步回调。

移动模式为目录级别抛异常。当目标目录下存在与源目录名冲突的目录，则抛出异常。

> [!NOTE]
> 该接口不支持在分布式文件路径下操作。


**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 源目录的应用沙箱路径。 |
| dest | string | 是 | 目标目录的应用沙箱路径。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当移动目录成功，err为undefined，否则为错误对象。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let srcPath = pathDir + "/srcDir";
let destPath = pathDir + "/destDir";
fileIo.moveDir(srcPath, destPath, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to move directory. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in moving directory.`);
  }
});
```



#### fileIo.moveDir10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

moveDir(src: string, dest: string, callback: AsyncCallback<void, Array&lt;ConflictFiles&gt;>): void

移动源目录至目标路径下。使用callback异步回调。

移动模式为目录级别抛异常。当目标目录下存在与源目录名冲突的目录，则抛出异常。

> [!NOTE]
> 该接口不支持在分布式文件路径下操作。


**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 源目录的应用沙箱路径。 |
| dest | string | 是 | 目标目录的应用沙箱路径。 |
| callback | AsyncCallback<void, Array&lt;ConflictFiles&gt;> | 是 | 回调函数。当移动目录成功，err为undefined，否则为错误对象。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { ConflictFiles } from '@kit.CoreFileKit';

let srcPath = pathDir + "/srcDir";
let destPath = pathDir + "/destDir";
fileIo.moveDir(srcPath, destPath, (err: BusinessError<Array<ConflictFiles>>) => {
  if (err && err.code == 13900015 && err.data?.length !== undefined) {
    for (let i = 0; i < err.data.length; i++) {
      console.error(`Failed to move directory, with conflicting files: ${err.data[i].srcFile} ${err.data[i].destFile}`);
    }
  } else if (err) {
    console.error(`Failed to move directory. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in moving directory.`);
  }
});
```



#### fileIo.moveDirSync10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

moveDirSync(src: string, dest: string, mode?: number): void

以同步方法移动源目录至目标路径下。

> [!NOTE]
> 该接口不支持在分布式文件路径下操作。


**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 源目录的应用沙箱路径。 |
| dest | string | 是 | 目标目录的应用沙箱路径。 |
| mode | number | 否 | 移动模式，默认值为0。 - mode为0，目录级别抛异常。若目标目录下存在与源目录名冲突的目录，则抛出异常。 - mode为1，文件级别抛异常。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则抛出异常。源目录下未冲突的文件全部移动至目标目录下，目标目录下未冲突文件将继续保留，且冲突文件信息将在抛出异常的data属性中以Array&lt;ConflictFiles&gt;形式提供。 - mode为2，文件级别强制覆盖。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则强制覆盖冲突目录下所有同名文件，未冲突文件将继续保留。 - mode为3，目录级别强制覆盖。移动源目录至目标目录下，目标目录下移动的目录内容与源目录完全一致。若目标目录下存在与源目录名冲突的目录，该目录下所有原始文件将被删除。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { ConflictFiles } from '@kit.CoreFileKit';

let srcPath = pathDir + "/srcDir";
let destPath = pathDir + "/destDir";
try {
  fileIo.moveDirSync(srcPath, destPath, 1);
  console.info(`Succeeded in moving directory.`);
} catch (error) {
  let err: BusinessError<Array<ConflictFiles>> = error as BusinessError<Array<ConflictFiles>>;
  if (err.code == 13900015 && err.data?.length !== undefined) {
    for (let i = 0; i < err.data.length; i++) {
      console.error(`Failed to move directory, with conflicting files: ${err.data[i].srcFile} ${err.data[i].destFile}`);
    }
  } else {
    console.error(`Failed to move directory. Code: ${err.code}, message: ${err.message}`);
  }
}
```



#### fileIo.moveFile

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

moveFile(src: string, dest: string, mode?: number): Promise&lt;void&gt;

移动文件，使用promise异步回调。

> [!NOTE]
> 该接口不支持在分布式文件路径下操作。


**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 源文件的应用沙箱路径。 |
| dest | string | 是 | 目标文件的应用沙箱路径。 |
| mode | number | 否 | 移动模式。若mode为0，移动位置存在同名文件时，强制移动覆盖。若mode为1，移动位置存在同名文件时，抛出异常。默认为0。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回值。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let srcPath = pathDir + "/source.txt";
let destPath = pathDir + "/dest.txt";
fileIo.moveFile(srcPath, destPath, 0).then(() => {
  console.info(`Succeeded in moving file.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to move file. Code: ${err.code}, message: ${err.message}`);
});
```



#### fileIo.moveFile

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

moveFile(src: string, dest: string, mode: number, callback: AsyncCallback&lt;void&gt;): void

移动文件，支持设置移动模式。使用callback异步回调。

> [!NOTE]
> 该接口不支持在分布式文件路径下操作。


**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 源文件的应用沙箱路径。 |
| dest | string | 是 | 目标文件的应用沙箱路径。 |
| mode | number | 是 | 移动模式。若mode为0，移动位置存在同名文件时，强制移动覆盖。若mode为1，移动位置存在同名文件时，抛出异常。默认为0。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 异步移动文件之后的回调。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let srcPath = pathDir + "/source.txt";
let destPath = pathDir + "/dest.txt";
fileIo.moveFile(srcPath, destPath, 0, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to move file. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in moving file.`);
  }
});
```



#### fileIo.moveFile

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

moveFile(src: string, dest: string, callback: AsyncCallback&lt;void&gt;): void

移动文件。如果移动位置存在同名文件，将强制覆盖。使用callback异步回调。

> [!NOTE]
> 该接口不支持在分布式文件路径下操作。


**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 源文件的应用沙箱路径。 |
| dest | string | 是 | 目标文件的应用沙箱路径。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 异步移动文件之后的回调。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let srcPath = pathDir + "/source.txt";
let destPath = pathDir + "/dest.txt";
fileIo.moveFile(srcPath, destPath, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to move file. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in moving file.`);
  }
});
```



#### fileIo.moveFileSync

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

moveFileSync(src: string, dest: string, mode?: number): void

以同步方式移动文件。

> [!NOTE]
> 该接口不支持在分布式文件路径下操作。


**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 源文件的应用沙箱路径。 |
| dest | string | 是 | 目标文件的应用沙箱路径。 |
| mode | number | 否 | 移动模式。若mode为0，移动位置存在同名文件时，强制移动覆盖。若mode为1，移动位置存在同名文件时，抛出异常。默认为0。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let srcPath = pathDir + "/source.txt";
let destPath = pathDir + "/dest.txt";
fileIo.moveFileSync(srcPath, destPath, 0);
console.info(`Succeeded in moving file.`);
```



#### fileIo.mkdtemp

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

mkdtemp(prefix: string): Promise&lt;string&gt;

创建临时目录，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| prefix | string | 是 | 指定目录路径，命名时需要以"XXXXXX"作为结尾。路径末尾的"XXXXXX"字符串将被替换为随机字符，以创建唯一的目录名。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise对象。返回生成的唯一目录路径。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

fileIo.mkdtemp(pathDir + "/XXXXXX").then((dir: string) => {
  console.info(`Succeeded in making temporary directory.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to make temporary directory. Code: ${err.code}, message: ${err.message}`);
});
```



#### fileIo.mkdtemp

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

mkdtemp(prefix: string, callback: AsyncCallback&lt;string&gt;): void

创建临时目录。使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| prefix | string | 是 | 指定目录路径，命名时需要以"XXXXXX"作为结尾。路径末尾的"XXXXXX"字符串将被替换为随机字符，以创建唯一的目录名。 |
| callback | AsyncCallback&lt;string&gt; | 是 | 异步创建临时目录之后的回调。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

fileIo.mkdtemp(pathDir + "/XXXXXX", (err: BusinessError, res: string) => {
  if (err) {
    console.error(`Failed to make temporary directory. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in making temporary directory.`);
  }
});
```



#### fileIo.mkdtempSync

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

mkdtempSync(prefix: string): string

以同步的方法创建临时目录。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| prefix | string | 是 | 指定目录路径，命名时需要以"XXXXXX"作为结尾。路径末尾的"XXXXXX"字符串将被替换为随机字符，以创建唯一的目录名。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 产生的唯一目录路径。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let res = fileIo.mkdtempSync(pathDir + "/XXXXXX");
```



#### fileIo.utimes11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

utimes(path: string, mtime: number): void

更改文件上次修改该文件的时间。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件的应用沙箱路径。 |
| mtime | number | 是 | 待更新的时间戳。自1970年1月1日起至目标时间的毫秒数。仅支持更改上次修改该文件的时间属性。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
fileIo.writeSync(file.fd, 'test data');
fileIo.closeSync(file);
fileIo.utimes(filePath, new Date().getTime());
```



#### fileIo.createRandomAccessFile10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

createRandomAccessFile(file: string | File, mode?: number): Promise&lt;RandomAccessFile&gt;

基于文件路径或文件对象创建RandomAccessFile对象，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string \| File | 是 | 文件的应用沙箱路径或已打开的File对象。 |
| mode | number | 否 | 创建文件RandomAccessFile对象的OpenMode，仅当传入文件沙箱路径时生效，必须指定如下选项中的一个，默认以只读方式创建： - OpenMode.READ_ONLY(0o0)：只读创建。 - OpenMode.WRITE_ONLY(0o1)：只写创建。 - OpenMode.READ_WRITE(0o2)：读写创建。 给定如下功能选项，以按位或的方式追加，默认不给定任何额外选项： - OpenMode.CREATE(0o100)：若文件不存在，则创建文件。 - OpenMode.TRUNC(0o1000)：如果RandomAccessFile对象存在且对应文件具有写权限，则将其长度裁剪为零。 - OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到RandomAccessFile对象末尾。 - OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。 - OpenMode.DIR(0o200000)：如果path未指向目录，则出错。不允许附加写权限。 - OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。 - OpenMode.SYNC(0o4010000)：以同步IO的方式创建RandomAccessFile对象。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;RandomAccessFile&gt; | Promise对象。返回RandomAccessFile对象的结果。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
fileIo.createRandomAccessFile(file).then((randomAccessFile: fileIo.RandomAccessFile) => {
  console.info(`Succeeded in creating randomaccessfile, fd: ${randomAccessFile.fd}`);
  randomAccessFile.close();
}).catch((err: BusinessError) => {
  console.error(`Failed to create randomaccessfile. Code: ${err.code}, message: ${err.message}`);
}).finally(() => {
  fileIo.closeSync(file);
});
```



#### fileIo.createRandomAccessFile10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

createRandomAccessFile(file: string | File, callback: AsyncCallback&lt;RandomAccessFile&gt;): void

基于文件路径或文件对象，以只读方式创建RandomAccessFile对象。使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string \| File | 是 | 文件的应用沙箱路径或已打开的File对象。 |
| callback | AsyncCallback&lt;RandomAccessFile&gt; | 是 | 异步创建RandomAccessFile对象之后的回调。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
fileIo.createRandomAccessFile(file, (err: BusinessError, randomAccessFile: fileIo.RandomAccessFile) => {
  if (err) {
    console.error(`Failed to create randomaccessfile. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in creating randomaccessfile, fd: ${randomAccessFile.fd}`);
    randomAccessFile.close();
  }
  fileIo.closeSync(file);
});
```



#### fileIo.createRandomAccessFile10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

createRandomAccessFile(file: string | File, mode: number, callback: AsyncCallback&lt;RandomAccessFile&gt;): void

基于文件路径或文件对象创建RandomAccessFile对象。使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string \| File | 是 | 文件的应用沙箱路径或已打开的File对象。 |
| mode | number | 是 | 创建文件RandomAccessFile对象的OpenMode，仅当传入文件沙箱路径时生效，必须指定如下选项中的一个，默认以只读方式创建： - OpenMode.READ_ONLY(0o0)：只读创建。 - OpenMode.WRITE_ONLY(0o1)：只写创建。 - OpenMode.READ_WRITE(0o2)：读写创建。 给定如下功能选项，以按位或的方式追加，默认不给定任何额外选项： - OpenMode.CREATE(0o100)：若文件不存在，则创建文件。 - OpenMode.TRUNC(0o1000)：如果RandomAccessFile对象存在且对应文件具有写权限，则将其长度裁剪为零。 - OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到RandomAccessFile对象末尾。 - OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。 - OpenMode.DIR(0o200000)：如果path不指向目录，则出错。不允许附加写权限。 - OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。 - OpenMode.SYNC(0o4010000)：以同步IO的方式创建RandomAccessFile对象。 |
| callback | AsyncCallback&lt;RandomAccessFile&gt; | 是 | 异步创建RandomAccessFile对象之后的回调。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
fileIo.createRandomAccessFile(file, fileIo.OpenMode.READ_ONLY, (err: BusinessError, randomAccessFile: fileIo.RandomAccessFile) => {
  if (err) {
    console.error(`Failed to create randomaccessfile. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in creating randomaccessfile, fd: ${randomAccessFile.fd}`);
    randomAccessFile.close();
  }
  fileIo.closeSync(file);
});
```



#### fileIo.createRandomAccessFile12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

createRandomAccessFile(file: string | File, mode?: number, options?: RandomAccessFileOptions): Promise&lt;RandomAccessFile&gt;

基于文件路径或文件对象创建RandomAccessFile对象，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string \| File | 是 | 文件的应用沙箱路径或已打开的File对象。 |
| mode | number | 否 | 创建文件RandomAccessFile对象的OpenMode，仅当传入文件沙箱路径时生效，必须指定如下选项中的一个，默认以只读方式创建： - OpenMode.READ_ONLY(0o0)：只读创建。 - OpenMode.WRITE_ONLY(0o1)：只写创建。 - OpenMode.READ_WRITE(0o2)：读写创建。 给定如下功能选项，以按位或的方式追加，默认不给定任何额外选项： - OpenMode.CREATE(0o100)：若文件不存在，则创建文件。 - OpenMode.TRUNC(0o1000)：如果RandomAccessFile对象存在且对应文件具有写权限，则将其长度裁剪为零。 - OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到RandomAccessFile对象末尾。 - OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。 - OpenMode.DIR(0o200000)：如果path不指向目录，则出错。不允许附加写权限。 - OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。 - OpenMode.SYNC(0o4010000)：以同步IO的方式创建RandomAccessFile对象。 |
| options | RandomAccessFileOptions | 否 | 支持如下选项： - start，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。 - end，number类型，表示期望读取结束的位置，单位为Byte。可选，默认文件末尾。 此选项仅对getreadstream及getwritestream获取的文件流对象生效。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;RandomAccessFile&gt; | Promise对象。返回RandomAccessFile对象的结果。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
fileIo.createRandomAccessFile(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE, { start: 10, end: 100 })
  .then((randomAccessFile: fileIo.RandomAccessFile) => {
    console.info(`Succeeded in creating randomaccessfile, fd: ${randomAccessFile.fd}`);
    randomAccessFile.close();
  })
  .catch((err: BusinessError) => {
    console.error(`Failed to create randomaccessfile. Code: ${err.code}, message: ${err.message}`);
  });
```



#### fileIo.createRandomAccessFileSync10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

createRandomAccessFileSync(file: string | File, mode?: number): RandomAccessFile

基于文件路径或文件对象创建RandomAccessFile对象。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string \| File | 是 | 文件的应用沙箱路径或已打开的File对象。 |
| mode | number | 否 | 创建文件RandomAccessFile对象的OpenMode，仅当传入文件沙箱路径时生效，必须指定如下选项中的一个，默认以只读方式创建： - OpenMode.READ_ONLY(0o0)：只读创建。 - OpenMode.WRITE_ONLY(0o1)：只写创建。 - OpenMode.READ_WRITE(0o2)：读写创建。 给定如下功能选项，以按位或的方式追加，默认不给定任何额外选项： - OpenMode.CREATE(0o100)：若文件不存在，则创建文件。 - OpenMode.TRUNC(0o1000)：如果RandomAccessFile对象存在且对应文件具有写权限，则将其长度裁剪为零。 - OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到RandomAccessFile对象末尾。 - OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。 - OpenMode.DIR(0o200000)：如果path不指向目录，则出错。不允许附加写权限。 - OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。 - OpenMode.SYNC(0o4010000)：以同步IO的方式创建RandomAccessFile对象。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| RandomAccessFile | 返回RandomAccessFile对象。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
let randomAccessFile = fileIo.createRandomAccessFileSync(file);
randomAccessFile.close();
```



#### fileIo.createRandomAccessFileSync12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

createRandomAccessFileSync(file: string | File, mode?: number, options?: RandomAccessFileOptions): RandomAccessFile

基于文件路径或文件对象创建RandomAccessFile对象。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string \| File | 是 | 文件的应用沙箱路径或已打开的File对象。 |
| mode | number | 否 | 创建文件RandomAccessFile对象的OpenMode，仅当传入文件沙箱路径时生效，必须指定如下选项中的一个，默认以只读方式创建： - OpenMode.READ_ONLY(0o0)：只读创建。 - OpenMode.WRITE_ONLY(0o1)：只写创建。 - OpenMode.READ_WRITE(0o2)：读写创建。 给定如下功能选项，以按位或的方式追加，默认不给定任何额外选项： - OpenMode.CREATE(0o100)：若文件不存在，则创建文件。 - OpenMode.TRUNC(0o1000)：如果RandomAccessFile对象存在且对应文件具有写权限，则将其长度裁剪为零。 - OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到RandomAccessFile对象末尾。 - OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。 - OpenMode.DIR(0o200000)：如果path不指向目录，则出错。不允许附加写权限。 - OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。 - OpenMode.SYNC(0o4010000)：以同步IO的方式创建RandomAccessFile对象。 |
| options | RandomAccessFileOptions | 否 | 支持如下选项： - start，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。 - end，number类型，表示期望读取结束的位置，单位为Byte。可选，默认文件末尾。 此选项仅对getreadstream及getwritestream获取的文件流对象生效。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| RandomAccessFile | 返回RandomAccessFile对象。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let filePath = pathDir + "/test.txt";
let randomAccessFile = fileIo.createRandomAccessFileSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE,
  { start: 10, end: 100 });
randomAccessFile.close();
```



#### fileIo.createStream

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

createStream(path: string, mode: string): Promise&lt;Stream&gt;

基于文件路径创建文件流，使用promise异步回调。需要配合[Stream](#stream)中的close()函数关闭文件流。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件的应用沙箱路径。 |
| mode | string | 是 | - r：打开只读文件，该文件必须存在。 - r+：打开可读写的文件，该文件必须存在。 - w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。 - w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。 - a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。 - a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Stream&gt; | Promise对象。返回文件流的结果。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
fileIo.createStream(filePath, "a+").then((stream: fileIo.Stream) => {
  stream.closeSync();
  console.info(`Succeeded in creating stream.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to create stream. Code: ${err.code}, message: ${err.message}`);
});
```



#### fileIo.createStream

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

createStream(path: string, mode: string, callback: AsyncCallback&lt;Stream&gt;): void

基于文件路径创建文件流，需要配合[Stream](#stream)中的close()函数关闭文件流。使用callback异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件的应用沙箱路径。 |
| mode | string | 是 | - r：打开只读文件，该文件必须存在。 - r+：打开可读写的文件，该文件必须存在。 - w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。 - w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。 - a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。 - a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。 |
| callback | AsyncCallback&lt;Stream&gt; | 是 | 异步打开文件流之后的回调。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
fileIo.createStream(filePath, "r+", (err: BusinessError, stream: fileIo.Stream) => {
  if (err) {
    console.error(`Failed to create stream. Code: ${err.code}, message: ${err.message}`);
  } else {
    stream.closeSync();
    console.info(`Succeeded in creating stream.`);
  }
})
```



#### fileIo.createStreamSync

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

createStreamSync(path: string, mode: string): Stream

以同步方法基于文件路径创建文件流。需要配合[Stream](#stream)中的close()函数关闭文件流。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件的应用沙箱路径。 |
| mode | string | 是 | - r：打开只读文件，该文件必须存在。 - r+：打开可读写的文件，该文件必须存在。 - w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。 - w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。 - a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。 - a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Stream | 返回文件流的结果。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
console.info(`Succeeded in creating stream.`);
stream.closeSync();
```



#### fileIo.fdopenStream

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

fdopenStream(fd: number, mode: string): Promise&lt;Stream&gt;

基于文件描述符打开文件流，使用promise异步回调。需要配合[Stream](#stream)中的close()函数关闭文件流。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符。 |
| mode | string | 是 | - r：打开只读文件，该文件必须存在。 - r+：打开可读写的文件，该文件必须存在。 - w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。 - w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。 - a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。 - a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Stream&gt; | Promise对象。返回文件流的结果。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath);
fileIo.fdopenStream(file.fd, "r+").then((stream: fileIo.Stream) => {
  console.info(`Succeeded in opening stream.`);
  stream.closeSync();
}).catch((err: BusinessError) => {
  console.error(`Failed to open stream. Code: ${err.code}, message: ${err.message}`);
  // 文件流打开失败后，文件描述符需要手动关闭
  fileIo.closeSync(file);
});
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/QggtD9gLQVWP89omHGhngg/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260528T025409Z&HW-CC-Expire=86400&HW-CC-Sign=8672DE86B88E6788C204C6E5FF04146D27DA4E697FFEBF2B8C2A4CD28F1C464A)


使用文件描述符创建的文件流时，文件描述符的生命周期将由文件流对象管理。调用文件流的close()函数后，初始的文件描述符也会被关闭。





#### fileIo.fdopenStream

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

fdopenStream(fd: number, mode: string, callback: AsyncCallback&lt;Stream&gt;): void

基于文件描述符打开文件流，需要配合[Stream](#stream)中的close()函数关闭文件流。使用callback异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符。 |
| mode | string | 是 | - r：打开只读文件，该文件必须存在。 - r+：打开可读写的文件，该文件必须存在。 - w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。 - w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。 - a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。 - a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。 |
| callback | AsyncCallback&lt;Stream&gt; | 是 | 异步打开文件流之后的回调。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_ONLY);
fileIo.fdopenStream(file.fd, "r+", (err: BusinessError, stream: fileIo.Stream) => {
  if (err) {
    console.error(`Failed to fdopen stream. Code: ${err.code}, message: ${err.message}`);
    // 文件流打开失败后，文件描述符需要手动关闭
    fileIo.closeSync(file);
  } else {
    console.info(`Succeeded in fdopening stream.`);
    stream.closeSync();
  }
});
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/oJs6doBMTc6NEoOKgO_jFA/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260528T025409Z&HW-CC-Expire=86400&HW-CC-Sign=19B1CC763B50AF32871F26A631BAE086499A9B10BE978AD78E45EA976C30DFDA)


使用文件描述符创建的文件流，文件描述符的生命周期也交由文件流对象，在调用文件流的close()函数后，初始的文件描述符也会被关闭。





#### fileIo.fdopenStreamSync

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

fdopenStreamSync(fd: number, mode: string): Stream

以同步方法基于文件描述符打开文件流。需要配合[Stream](#stream)中的close()函数关闭文件流。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 已打开的文件描述符。 |
| mode | string | 是 | - r：打开只读文件，该文件必须存在。 - r+：打开可读写的文件，该文件必须存在。 - w：打开只写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。 - w+：打开可读写文件，若文件存在则文件长度清0，即该文件内容会消失。若文件不存在则建立该文件。 - a：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。 - a+：以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Stream | 返回文件流的结果。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_ONLY | fileIo.OpenMode.CREATE);
let stream = fileIo.fdopenStreamSync(file.fd, "r+");
stream.closeSync();
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/4hLLzQ9dToW9XJYc5f0y5A/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260528T025409Z&HW-CC-Expire=86400&HW-CC-Sign=56437B7D2CAE735FF0C6DA24CCEEC19DC4FE3749C7F0A02BC37824EACBC26E21)


使用文件描述符创建的文件流，文件描述符的生命周期也交由文件流对象，在调用文件流的close()函数后，初始的文件描述符也会被关闭。





#### fileIo.createReadStream12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

createReadStream(path: string, options?: ReadStreamOptions ): ReadStream

以同步方法打开文件可读流。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件路径。 |
| options | ReadStreamOptions | 否 | 支持如下选项： - start，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。 - end，number类型，表示期望读取结束的位置，单位为Byte。可选，默认文件末尾。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| ReadStream | 文件可读流。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**示例：**

```text
// 创建文件可读流
const rs = fileIo.createReadStream(`${pathDir}/read.txt`);
// 创建文件可写流
const ws = fileIo.createWriteStream(`${pathDir}/write.txt`);
// 暂停模式拷贝文件
rs.on('readable', () => {
  const data = rs.read();
  if (!data) {
    return;
  }
  ws.write(data);
});
```



#### fileIo.createWriteStream12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

createWriteStream(path: string, options?: WriteStreamOptions): WriteStream

以同步方法打开文件可写流。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件路径。 |
| options | WriteStreamOptions | 否 | 支持如下选项： - start，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。 - mode，number 类型，创建文件可写流的OpenMode，可选，默认以只写方式创建。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| WriteStream | 文件可写流。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**示例：**

```text
// 创建文件可读流
const rs = fileIo.createReadStream(`${pathDir}/read.txt`);
// 创建文件可写流
const ws = fileIo.createWriteStream(`${pathDir}/write.txt`);
// 暂停模式拷贝文件
rs.on('readable', () => {
  const data = rs.read();
  if (!data) {
    return;
  }
  ws.write(data);
});
```



#### AtomicFile15+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

AtomicFile是一个用于对文件进行原子读写操作的类。

在写操作时，通过写入临时文件，并在写入成功后将其重命名到原始文件位置来确保写入文件的完整性；而在写入失败时删除临时文件，不修改原始文件内容。

使用者可以自行调用finishWrite或failWrite来完成文件内容的写入或回滚。

**系统能力**：SystemCapability.FileManagement.File.FileIO



#### constructor15+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

constructor(path: string)

对于给定路径的文件创建一个AtomicFile类。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件的沙箱路径。 |




#### getBaseFile15+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getBaseFile(): File

通过AtomicFile对象获取文件对象。

文件描述符fd需要由用户调用close方法关闭。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| File | 打开的File对象。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;

try {
  let atomicFile = new fileIo.AtomicFile(`${pathDir}/write.txt`);
  let writeStream = atomicFile.startWrite();
  writeStream.write("hello, world", "utf-8", ()=> {
    atomicFile.finishWrite();
    let file = atomicFile.getBaseFile();
    console.info(`Succeeded in getting base file. fd: ${file.fd}, path: ${file.path}, name:${file.name}`);
  })
} catch (err) {
  console.error(`Failed to get baseFile. Code: ${err.code}, message: ${err.message}`);
}
```



#### openRead15+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

openRead(): ReadStream

创建一个读文件流。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ReadStream | 文件可读流。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;

try {
  let file = new fileIo.AtomicFile(`${pathDir}/read.txt`);
  let writeStream = file.startWrite();
  writeStream.write("hello, world", "utf-8", ()=> {
    file.finishWrite();
    setTimeout(()=>{
      let readStream = file.openRead();
      readStream.on('readable', () => {
        const data = readStream.read();
        if (!data) {
          console.error(`Failed to read atomicfile, data is null.`);
          return;
        }
        console.info(`Succeeded in reading atomicfile, data is: ${data}`);
      });
    },1000);
  })
} catch (err) {
  console.error(`Failed to AtomicFile. Code: ${err.code}, message: ${err.message}`);
}
```



#### readFully15+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

readFully(): ArrayBuffer

读取文件全部内容。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArrayBuffer | 文件的全部内容。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { common } from '@kit.AbilityKit';
import { util, buffer } from '@kit.ArkTS';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;

try {
  let file = new fileIo.AtomicFile(`${pathDir}/read.txt`);
  let writeStream = file.startWrite();
  writeStream.write("hello, world", "utf-8", ()=> {
    file.finishWrite();
    setTimeout(()=>{
      let data = file.readFully();
      let decoder = util.TextDecoder.create('utf-8');
      let str = decoder.decodeToString(new Uint8Array(data));
      console.info(`Succeeded in reading atomicfile fully, str is: ${str}`);
    },1000);
  })
} catch (err) {
  console.error(`Failed to AtomicFile. Code: ${err.code}, message: ${err.message}`);
}
```



#### startWrite15+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

startWrite(): WriteStream

对文件开始新的写入操作。将返回一个WriteStream，用于在其中写入新的文件数据。

当文件不存在时新建文件。

在写入文件完成后，写入成功需要调用finishWrite()，写入失败需要调用failWrite()。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| WriteStream | 文件可写流。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;

try {
  let file = new fileIo.AtomicFile(`${pathDir}/write.txt`);
  let writeStream = file.startWrite();
  writeStream.write("hello, world", "utf-8", ()=> {
    file.finishWrite();
    console.info(`Succeeded in writing atomicfile finished.`);
  })
} catch (err) {
  console.error(`Failed to AtomicFile. Code: ${err.code}, message: ${err.message}`);
}
```



#### finishWrite15+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

finishWrite(): void

在完成对startWrite返回流的写入操作时调用，表示文件写入成功。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;

try {
  let file = new fileIo.AtomicFile(`${pathDir}/write.txt`);
  let writeStream = file.startWrite();
  writeStream.write("hello, world", "utf-8", ()=> {
    file.finishWrite();
  })
} catch (err) {
  console.error(`Failed to AtomicFile. Code: ${err.code}, message: ${err.message}`);
}
```



#### failWrite15+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

failWrite(): void

文件写入失败后调用，将执行文件回滚操作。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;

let file = new fileIo.AtomicFile(`${pathDir}/write.txt`);
try {
  let writeStream = file.startWrite();
  writeStream.write("hello, world", "utf-8", ()=> {
    console.info(`Succeeded in writing atomicFile.`);
  })
} catch (err) {
  file.failWrite();
  console.error(`Failed to AtomicFile. Code: ${err.code}, message: ${err.message}`);
}
```



#### delete15+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

delete(): void

删除AtomicFile类，会删除原始文件和临时文件。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { common } from '@kit.AbilityKit';
import { util } from '@kit.ArkTS';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;

try {
  let file = new fileIo.AtomicFile(`${pathDir}/read.txt`);
  let writeStream = file.startWrite();
  writeStream.write("hello, world", "utf-8", ()=> {
    file.finishWrite();
    setTimeout(()=>{
      let data = file.readFully();
      let decoder = util.TextDecoder.create('utf-8');
      let str = decoder.decodeToString(new Uint8Array(data));
      file.delete();
      console.info(`Succeeded in delete atomicfile.`);
    },1000);
  })
} catch (err) {
  console.error(`Failed to AtomicFile. Code: ${err.code}, message: ${err.message}`);
}
```



#### fileIo.createWatcher10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

createWatcher(path: string, events: number, listener: WatchEventListener): Watcher

创建Watcher对象，监听文件或目录变动。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 监听文件或目录的沙箱路径。 |
| events | number | 是 | 监听变动的事件集，多个事件通过或(\|)的方式进行集合。 - 0x1: IN_ACCESS， 文件被访问。 - 0x2: IN_MODIFY，文件内容被修改。 - 0x4: IN_ATTRIB，文件元数据被修改。 - 0x8: IN_CLOSE_WRITE，文件在打开时进行了写操作，然后被关闭。 - 0x10: IN_CLOSE_NOWRITE，文件或目录在打开时未进行写操作，然后被关闭。 - 0x20: IN_OPEN，文件或目录被打开。 - 0x40: IN_MOVED_FROM，监听目录中文件被移动走。 - 0x80: IN_MOVED_TO，监听目录中文件被移动过来。 - 0x100: IN_CREATE，监听目录中文件或子目录被创建。 - 0x200: IN_DELETE，监听目录中文件或子目录被删除。 - 0x400: IN_DELETE_SELF，监听的目录被删除，删除后监听停止。 - 0x800: IN_MOVE_SELF，监听的文件或目录被移动，移动后监听继续。 - 0xfff: IN_ALL_EVENTS，监听以上所有事件。 |
| listener | WatchEventListener | 是 | 监听事件发生后的回调。监听事件每发生一次，回调一次。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Watcher | 返回Watcher对象。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { common } from '@kit.AbilityKit';
import { WatchEvent } from '@kit.CoreFileKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let watcher = fileIo.createWatcher(filePath, 0x2 | 0x10, (watchEvent: WatchEvent) => {
  if (watchEvent.event == 0x2) {
    console.info(watchEvent.fileName + 'was modified');
  } else if (watchEvent.event == 0x10) {
    console.info(watchEvent.fileName + 'was closed');
  }
});
watcher.start();
fileIo.writeSync(file.fd, 'test');
fileIo.closeSync(file);
watcher.stop();
```



#### WatchEventListener10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

(event: WatchEvent): void

事件监听类。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | WatchEvent | 是 | 回调的事件类。 |




#### WatchEvent10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

事件类



#### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fileName | string | 是 | 否 | 发生监听事件对应文件的沙箱路径，该沙箱路径包含文件名称。 |
| event | number | 是 | 否 | 监听变动的事件集，多个事件通过或(\|)的方式进行集合。 - 0x1: IN_ACCESS， 文件被访问。 - 0x2: IN_MODIFY，文件内容被修改。 - 0x4: IN_ATTRIB，文件元数据被修改。 - 0x8: IN_CLOSE_WRITE，文件在打开时进行了写操作，然后被关闭。 - 0x10: IN_CLOSE_NOWRITE，文件或目录在打开时未进行写操作，然后被关闭。 - 0x20: IN_OPEN，文件或目录被打开。 - 0x40: IN_MOVED_FROM，监听目录中文件被移动走。 - 0x80: IN_MOVED_TO，监听目录中文件被移动过来。 - 0x100: IN_CREATE，监听目录中文件或子目录被创建。 - 0x200: IN_DELETE，监听目录中文件或子目录被删除。 - 0x400: IN_DELETE_SELF，监听的目录被删除，删除后监听停止。 - 0x800: IN_MOVE_SELF，监听的文件或目录被移动，移动后监听继续。 - 0xfff: IN_ALL_EVENTS，监听以上所有事件。 |
| cookie | number | 是 | 否 | 绑定相关事件的cookie。当前仅支持事件IN_MOVED_FROM与IN_MOVED_TO，同一个文件的移动事件IN_MOVED_FROM和IN_MOVED_TO具有相同的cookie值。 |




#### Progress11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

拷贝进度回调数据

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| processedSize | number | 是 | 否 | 已拷贝的数据大小，单位为Byte。 |
| totalSize | number | 是 | 否 | 待拷贝的数据总大小，单位为Byte。 |




#### TaskSignal12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

拷贝中断信号。

**系统能力**：SystemCapability.FileManagement.File.FileIO



#### cancel12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

cancel(): void

取消拷贝任务。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;

let srcDirPathLocal: string = pathDir + "/src";
let dstDirPathLocal: string = pathDir + "/dest";
let srcDirUriLocal: string = fileUri.getUriFromPath(srcDirPathLocal);
let dstDirUriLocal: string = fileUri.getUriFromPath(dstDirPathLocal);
let copySignal = new fileIo.TaskSignal;
let progressListener: fileIo.ProgressListener = (progress: fileIo.Progress) => {
  console.info(`progressSize: ${progress.processedSize}, totalSize: ${progress.totalSize}`);
  if (progress.processedSize / progress.totalSize > 0.5) {
    copySignal.cancel();
    console.info("copy cancel.");
  }
};
let options: fileIo.CopyOptions = {
  "progressListener" : progressListener,
  "copySignal" : copySignal,
}

try {
  fileIo.copy(srcDirUriLocal, dstDirUriLocal, options, (err: BusinessError) => {
    if (err) {
      console.error("copy fail, err: ", err.message);
      return;
    }
    console.info("copy success.");
  })
} catch (err) {
  console.error("copyFileWithCancel failed, err: ", err.message);
}
```



#### onCancel(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onCancel(): Promise&lt;string&gt;

> [!NOTE]
> 从API version 12开始支持，从API version 24开始废弃。


取消拷贝事件监听。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise对象。最后一个拷贝的文件路径。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { TaskSignal } from '@kit.CoreFileKit';

let copySignal: fileIo.TaskSignal = new TaskSignal();
copySignal.onCancel();
```



#### CopyOptions11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

拷贝进度回调监听

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| progressListener | ProgressListener | 否 | 是 | 拷贝进度监听。 |
| copySignal | TaskSignal | 否 | 是 | 取消拷贝信号。 |




#### ProgressListener11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

拷贝进度监听。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 类型 | 说明 |
| --- | --- |
| (progress: Progress) => void | 拷贝进度监听 |


**示例：**

```text
import { TaskSignal } from '@kit.CoreFileKit';

let copySignal: fileIo.TaskSignal = new TaskSignal();
let progressListener: fileIo.ProgressListener = (progress: fileIo.Progress) => {
  console.info(`processedSize: ${progress.processedSize}, totalSize: ${progress.totalSize}`);
};
let copyOption: fileIo.CopyOptions = {
  "progressListener" : progressListener,
  "copySignal" : copySignal,
}
```



#### Stat

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

文件具体信息，在调用Stat的方法前，需要先通过[stat()](#fileiostat)方法（同步或异步）构建一个Stat实例。



#### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| ino | bigint | 是 | 否 | 标识该文件。通常同设备上的不同文件的INO不同。 |
| mode | number | 是 | 否 | 表示文件权限，各特征位的含义如下： 说明：以下值为八进制，取得的返回值为十进制，请换算后查看。 - 0o400：用户读。对于普通文件，所有者可读取文件；对于目录，所有者可读取目录项。 - 0o200：用户写。对于普通文件，所有者可写入文件；对于目录，所有者可创建/删除目录项。 - 0o100：用户执行。对于普通文件，所有者可执行文件；对于目录，所有者可在目录中搜索给定路径名。 - 0o040：用户组读。对于普通文件，所有用户组可读取文件；对于目录，所有用户组可读取目录项。 - 0o020：用户组写。对于普通文件，所有用户组可写入文件；对于目录，所有用户组可创建/删除目录项。 - 0o010：用户组执行。对于普通文件，所有用户组可执行文件；对于目录，所有用户组是否可在目录中搜索给定路径名。 - 0o004：其他读。对于普通文件，其余用户可读取文件；对于目录，其他用户组可读取目录项。 - 0o002：其他写。对于普通文件，其余用户可写入文件；对于目录，其他用户组可创建/删除目录项。 - 0o001：其他执行。对于普通文件，其余用户可执行文件；对于目录，其他用户组可在目录中搜索给定路径名。 元服务API：从API version 11开始，该接口支持在元服务中使用。 |
| uid | number | 是 | 否 | 文件所有者的ID。 |
| gid | number | 是 | 否 | 文件所有组的ID。 |
| size | number | 是 | 否 | 文件的大小，单位为Byte。仅对普通文件有效。 元服务API：从API version 11开始，该接口支持在元服务中使用。 |
| atime | number | 是 | 否 | 上次访问该文件的时间，表示距1970年1月1日0时0分0秒的秒数。 注意：目前用户数据分区默认以“noatime”方式挂载，atime更新被禁用。 元服务API：从API version 11开始，该接口支持在元服务中使用。 |
| mtime | number | 是 | 否 | 上次修改该文件的时间，表示距1970年1月1日0时0分0秒的秒数。 元服务API：从API version 11开始，该接口支持在元服务中使用。 |
| ctime | number | 是 | 否 | 最近改变文件状态的时间，表示距1970年1月1日0时0分0秒的秒数。 |
| atimeNs15+ | bigint | 是 | 是 | 上次访问该文件的时间，表示距1970年1月1日0时0分0秒的纳秒数。 注意：目前用户数据分区默认以“noatime”方式挂载，atime更新被禁用。 |
| mtimeNs15+ | bigint | 是 | 是 | 上次修改该文件的时间，表示距1970年1月1日0时0分0秒的纳秒数。 |
| ctimeNs15+ | bigint | 是 | 是 | 最近改变文件状态的时间，表示距1970年1月1日0时0分0秒的纳秒数。 |
| location11+ | LocationType | 是 | 否 | 文件的位置，表示该文件是本地文件或者云端文件。 |


> [!NOTE]
> Stat中部分属性仅支持普通文件获取，开发者可通过 isFile() 接口判断文件是否为普通文件。




#### isBlockDevice

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isBlockDevice(): boolean

用于判断文件是否是块特殊文件。一个块特殊文件只能以块为粒度进行访问，且访问的时候带缓存。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示文件是否是块特殊设备。true：是块特殊设备；false：不是块特殊设备。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let filePath = pathDir + "/test.txt";
let isBLockDevice = fileIo.statSync(filePath).isBlockDevice();
```



#### isCharacterDevice

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isCharacterDevice(): boolean

判断文件是否为字符特殊文件。字符特殊设备支持随机访问，且访问时无缓存。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示文件是否是字符特殊设备。true：是字符特殊设备；false：不是字符特殊设备。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let filePath = pathDir + "/test.txt";
let isCharacterDevice = fileIo.statSync(filePath).isCharacterDevice();
```



#### isDirectory

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isDirectory(): boolean

判断文件是否为目录。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示文件是否是目录。true：是目录；false：不是目录。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let dirPath = pathDir + "/test";
let isDirectory = fileIo.statSync(dirPath).isDirectory();
```



#### isFIFO

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isFIFO(): boolean

用于判断文件是否是命名管道（有时也称为FIFO）。命名管道通常用于进程间通信。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示文件是否是 FIFO。true：是FIFO；false：不是FIFO。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let filePath = pathDir + "/test.txt";
let isFIFO = fileIo.statSync(filePath).isFIFO();
```



#### isFile

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isFile(): boolean

用于判断文件是否是普通文件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示文件是否是普通文件。true：是普通文件；false：不是普通文件。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let filePath = pathDir + "/test.txt";
let isFile = fileIo.statSync(filePath).isFile();
```



#### isSocket

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isSocket(): boolean

判断文件是否是套接字。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示文件是否是套接字。true：是套接字；false：不是套接字。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let filePath = pathDir + "/test.txt";
let isSocket = fileIo.statSync(filePath).isSocket();
```



#### isSymbolicLink

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isSymbolicLink(): boolean

判断文件是否为符号链接。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示文件是否是符号链接。true：是符号链接；false：不是符号链接。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let filePath = pathDir + "/test.txt";
let isSymbolicLink = fileIo.statSync(filePath).isSymbolicLink();
```



#### Stream

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

文件流，在调用Stream的方法前，需要先通过[fileIo.createStream](#fileiocreatestream)方法或者[fileIo.fdopenStream](#fileiofdopenstream)（同步或异步）来构建一个Stream实例。



#### close

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

close(): Promise&lt;void&gt;

关闭文件流，使用promise异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回值。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
stream.close().then(() => {
  console.info(`Succeeded in closing file stream.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to close file stream. Code: ${err.code}, message: ${err.message}`);
});
```



#### close

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

close(callback: AsyncCallback&lt;void&gt;): void

异步关闭文件流。使用callback异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 异步关闭文件流之后的回调。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
stream.close((err: BusinessError) => {
  if (err) {
    console.error(`Failed to close stream. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in closing stream.`);
  }
});
```



#### closeSync

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

closeSync(): void

同步关闭文件流。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
stream.closeSync();
```



#### flush

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

flush(): Promise&lt;void&gt;

刷新文件流，使用promise异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。返回表示异步刷新文件流的结果。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
stream.flush().then(() => {
  console.info(`Succeeded in flushing.`);
  stream.close();
}).catch((err: BusinessError) => {
  console.error(`Failed to flush. Code: ${err.code}, message: ${err.message}`);
});
```



#### flush

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

flush(callback: AsyncCallback&lt;void&gt;): void

异步刷新文件流。使用callback异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 异步刷新文件流后的回调函数。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
stream.flush((err: BusinessError) => {
  if (err) {
    console.error(`Failed to flush stream. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in flushing.`);
    stream.close();
  }
});
```



#### flushSync

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

flushSync(): void

同步刷新文件流。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
stream.flushSync();
stream.close();
```



#### write

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

write(buffer: ArrayBuffer | string, options?: WriteOptions): Promise&lt;number&gt;

将数据写入流文件，使用promise异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer \| string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | WriteOptions | 否 | 支持如下选项： - length，number类型，表示期望写入数据的长度，单位为Byte。默认缓冲区长度。 - offset，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。 - encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | Promise对象。返回实际写入的长度，单位为Byte。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { WriteOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
let writeOption: WriteOptions = {
  offset: 5,
  length: 5,
  encoding: 'utf-8'
};
stream.write("hello, world", writeOption).then((number: number) => {
  console.info(`Succeeded in writing, size is: ${number}`);
  stream.close();
}).catch((err: BusinessError) => {
  console.error(`Failed to write. Code: ${err.code}, message: ${err.message}`);
});
```



#### write

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

write(buffer: ArrayBuffer | string, callback: AsyncCallback&lt;number&gt;): void

将数据写入流文件。使用callback异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer \| string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| callback | AsyncCallback&lt;number&gt; | 是 | 回调函数，返回实际写入的数据长度，单位为Byte。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
stream.write("hello, world", (err: BusinessError, bytesWritten: number) => {
  if (err) {
    console.error(`Failed to write stream. Code: ${err.code}, message: ${err.message}`);
  } else {
    if (bytesWritten) {
      console.info(`Succeeded in writing, size is: ${bytesWritten}`);
    }
  }
  stream.close();
});
```



#### write

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

write(buffer: ArrayBuffer | string, options: WriteOptions, callback: AsyncCallback&lt;number&gt;): void

将数据写入流文件，支持配置写入选项。使用callback异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer \| string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | WriteOptions | 是 | 支持如下选项： - length，number类型，表示期望写入数据的长度，单位为Byte。可选，默认缓冲区长度。 - offset，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。 - encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。 |
| callback | AsyncCallback&lt;number&gt; | 是 | 回调函数，返回实际写入的数据长度，单位为Byte。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { WriteOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
let writeOption: WriteOptions = {
  offset: 5,
  length: 5,
  encoding: 'utf-8'
};
stream.write("hello, world", writeOption, (err: BusinessError, bytesWritten: number) => {
  if (err) {
    console.error(`Failed to write stream. Code: ${err.code}, message: ${err.message}`);
  } else {
    if (bytesWritten) {
      console.info(`Succeeded in writing, size is: ${bytesWritten}`);
    }
  }
  stream.close();
});
```



#### writeSync

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

writeSync(buffer: ArrayBuffer | string, options?: WriteOptions): number

以同步方法将数据写入流文件。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer \| string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | WriteOptions | 否 | 支持如下选项： - length，number类型，表示期望写入数据的长度，单位为Byte。可选，默认缓冲区长度。 - offset，number类型，表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。 - encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 实际写入的长度，单位为Byte。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { WriteOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath,"r+");
let writeOption: WriteOptions = {
  offset: 5,
  length: 5,
  encoding: 'utf-8'
};
let num = stream.writeSync("hello, world", writeOption);
stream.close();
```



#### read

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

read(buffer: ArrayBuffer, options?: ReadOptions): Promise&lt;number&gt;

从流文件读取数据，使用promise异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 用于读取文件的缓冲区。 |
| options | ReadOptions | 否 | 支持如下选项： - length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认缓冲区长度。 - offset，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | Promise对象。返回读取的结果，单位为Byte。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';
import { ReadOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
let arrayBuffer = new ArrayBuffer(4096);
let readOption: ReadOptions = {
  offset: 5,
  length: 5
};
stream.read(arrayBuffer, readOption).then((readLen: number) => {
  let buf = buffer.from(arrayBuffer, 0, readLen);
  console.info(`Succeeded in reading data, the content of file is: ${buf.toString()}`);
  stream.close();
}).catch((err: BusinessError) => {
  console.error(`Failed to read data. Code: ${err.code}, message: ${err.message}`);
});
```



#### read

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

read(buffer: ArrayBuffer, callback: AsyncCallback&lt;number&gt;): void

从流文件读取数据。使用callback异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 用于读取文件的缓冲区。 |
| callback | AsyncCallback&lt;number&gt; | 是 | 回调函数，返回读取的结果，单位为Byte。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';

let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
let arrayBuffer = new ArrayBuffer(4096);
stream.read(arrayBuffer, (err: BusinessError, readLen: number) => {
  if (err) {
    console.error(`Failed to read stream. Code: ${err.code}, message: ${err.message}`);
  } else {
    let buf = buffer.from(arrayBuffer, 0, readLen);
    console.info(`Succeeded in reading data, the content of file is: ${buf.toString()}`);
    stream.close();
  }
});
```



#### read

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

read(buffer: ArrayBuffer, options: ReadOptions, callback: AsyncCallback&lt;number&gt;): void

从流文件读取数据，支持配置读取选项。使用callback异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 用于读取文件的缓冲区。 |
| options | ReadOptions | 是 | 支持如下选项： - length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认缓冲区长度。 - offset，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读取。 |
| callback | AsyncCallback&lt;number&gt; | 是 | 回调函数，返回读取的结果，单位为Byte。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';
import { ReadOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
let arrayBuffer = new ArrayBuffer(4096);
let readOption: ReadOptions = {
  offset: 5,
  length: 5
};
stream.read(arrayBuffer, readOption, (err: BusinessError, readLen: number) => {
  if (err) {
    console.error(`Failed to read stream. Code: ${err.code}, message: ${err.message}`);
  } else {
    let buf = buffer.from(arrayBuffer, 0, readLen);
    console.info(`Succeeded in reading data, the content of file is: ${buf.toString()}`);
    stream.close();
  }
});
```



#### readSync

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

readSync(buffer: ArrayBuffer, options?: ReadOptions): number

以同步方法从流文件读取数据。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 用于读取文件的缓冲区。 |
| options | ReadOptions | 否 | 支持如下选项： - length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认缓冲区长度。 - offset，number类型，表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 实际读取的长度，单位为Byte。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { ReadOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let stream = fileIo.createStreamSync(filePath, "r+");
let readOption: ReadOptions = {
  offset: 5,
  length: 5
};
let buf = new ArrayBuffer(4096);
let num = stream.readSync(buf, readOption);
stream.close();
```



#### File

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

由open接口打开的File对象。



#### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fd | number | 是 | 否 | 打开的文件描述符。 元服务API：从API version 11开始，该接口支持在元服务中使用。 |
| path10+ | string | 是 | 否 | 文件路径。 |
| name10+ | string | 是 | 否 | 文件名。 |




#### getParent11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getParent(): string

获取File对象对应文件父目录。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回父目录路径。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
console.info(`Succeeded in getting parent path, the parent path is: ${file.getParent()}`);
fileIo.closeSync(file);
```



#### lock

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

lock(exclusive?: boolean): Promise&lt;void&gt;

对文件阻塞式施加共享锁或独占锁，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| exclusive | boolean | 否 | 是否施加独占锁，默认false。true：施加独占锁；false：不施加独占锁。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回值。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
file.lock(true).then(() => {
  console.info(`Succeeded in locking file.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to lock file. Code: ${err.code}, message: ${err.message}`);
}).finally(() => {
  fileIo.closeSync(file);
});
```



#### lock

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

lock(callback: AsyncCallback&lt;void&gt;): void

对文件阻塞式施加共享锁。使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当文件上锁成功，err为undefined，否则为错误对象。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
file.lock((err: BusinessError) => {
  if (err) {
    console.error(`Failed to lock file. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in locking file.`);
  }
  fileIo.closeSync(file);
});
```



#### lock

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

lock(exclusive: boolean, callback: AsyncCallback&lt;void&gt;): void

对文件阻塞式施加共享锁或独占锁。使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| exclusive | boolean | 是 | 是否施加独占锁。true：施加独占锁；false：不施加独占锁。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当文件上锁成功，err为undefined，否则为错误对象。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
file.lock(true, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to lock file. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in locking file.`);
  }
  fileIo.closeSync(file);
});
```



#### tryLock

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

tryLock(exclusive?: boolean): void

文件非阻塞式施加共享锁或独占锁。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| exclusive | boolean | 否 | 是否施加独占锁，默认false。true：施加独占锁；false：不施加独占锁。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
file.tryLock(true);
console.info(`Succeeded in locking file.`);
fileIo.closeSync(file);
```



#### unlock

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

unlock(): void

以同步方式解锁文件。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
file.tryLock(true);
file.unlock();
console.info(`Succeeded in unlocking file.`);
fileIo.closeSync(file);
```



#### fileIo.DfsListeners12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

事件监听类。创建DFSListener对象，用于监听分布式文件系统状态。

**系统能力**：SystemCapability.FileManagement.File.FileIO



#### onStatus12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onStatus(networkId: string, status: number): void;

事件回调类。参数由[connectDfs](#fileioconnectdfs12)传入。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| networkId | string | 是 | 设备的网络Id。 |
| status | number | 是 | 分布式文件系统的状态码（以connectDfs回调onStatus的特定错误码作为入参）。触发场景为connectDfs调用过程中出现对端设备异常，对应错误码为： - 13900046：软件造成连接中断。 |




#### RandomAccessFile10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

随机读写文件流。在调用RandomAccessFile的方法前，需要先通过createRandomAccessFile()方法（同步或异步）来构建一个RandomAccessFile实例。



#### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fd | number | 是 | 否 | 打开的文件描述符。 |
| filePointer | number | 是 | 否 | RandomAccessFile对象的偏移指针，单位为Byte。 |




#### setFilePointer10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setFilePointer(filePointer:number): void

设置文件偏移指针。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filePointer | number | 是 | RandomAccessFile对象的偏移指针，单位为Byte。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let filePath = pathDir + "/test.txt";
let randomAccessFile = fileIo.createRandomAccessFileSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
randomAccessFile.setFilePointer(1);
randomAccessFile.close();
```



#### close10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

close(): void

以同步方式关闭RandomAccessFile对象。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let filePath = pathDir + "/test.txt";
let randomAccessFile = fileIo.createRandomAccessFileSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
randomAccessFile.close();
```



#### write10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

write(buffer: ArrayBuffer | string, options?: WriteOptions): Promise&lt;number&gt;

将数据写入文件，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer \| string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | WriteOptions | 否 | 支持如下选项： - length，number类型，表示期望写入数据的长度，单位为Byte。默认缓冲区长度。 - offset，number类型，表示期望写入文件位置，单位为Byte（基于当前filePointer加上offset的位置）。可选，默认从偏移指针（filePointer）开始写。 - encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | Promise对象。返回实际写入的长度，单位为Byte。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { WriteOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
let randomAccessFile = fileIo.createRandomAccessFileSync(file);
let bufferLength: number = 4096;
let writeOption: WriteOptions = {
  offset: 1,
  length: 5,
  encoding: 'utf-8'
};
let arrayBuffer = new ArrayBuffer(bufferLength);
randomAccessFile.write(arrayBuffer, writeOption).then((bytesWritten: number) => {
  console.info(`Succeeded in writing, bytes written: ${bytesWritten}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to write. Code: ${err.code}, message: ${err.message}`);
}).finally(() => {
  randomAccessFile.close();
  fileIo.closeSync(file);
});
```



#### write10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

write(buffer: ArrayBuffer | string, callback: AsyncCallback&lt;number&gt;): void

将数据写入文件。使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer \| string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| callback | AsyncCallback&lt;number&gt; | 是 | 回调函数，返回实际写入数据长度，单位为Byte。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
let randomAccessFile = fileIo.createRandomAccessFileSync(file);
let bufferLength: number = 4096;
let arrayBuffer = new ArrayBuffer(bufferLength);
randomAccessFile.write(arrayBuffer, (err: BusinessError, bytesWritten: number) => {
  if (err) {
    console.error(`Failed to write. Code: ${err.code}, message: ${err.message}`);
  } else {
    if (bytesWritten) {
      console.info(`Succeeded in writing, size is: ${bytesWritten}`);
    }
  }
  randomAccessFile.close();
  fileIo.closeSync(file);
});
```



#### write10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

write(buffer: ArrayBuffer | string, options: WriteOptions, callback: AsyncCallback&lt;number&gt;): void

将数据写入文件，支持配置写入选项。使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer \| string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | WriteOptions | 是 | 支持如下选项： - length，number类型，表示期望写入数据的长度，单位为Byte。可选，默认为缓冲区长度。 - offset，number类型，表示期望写入文件位置，单位为Byte（基于当前filePointer加上offset的位置）。可选，默认从偏移指针（filePointer）开始写。 - encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。 |
| callback | AsyncCallback&lt;number&gt; | 是 | 回调函数，返回实际写入数据长度，单位为Byte。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { WriteOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
let randomAccessFile = fileIo.createRandomAccessFileSync(file);
let bufferLength: number = 4096;
let writeOption: WriteOptions = {
  offset: 1,
  length: bufferLength,
  encoding: 'utf-8'
};
let arrayBuffer = new ArrayBuffer(bufferLength);
randomAccessFile.write(arrayBuffer, writeOption, (err: BusinessError, bytesWritten: number) => {
  if (err) {
    console.error(`Failed to write. Code: ${err.code}, message: ${err.message}`);
  } else {
    if (bytesWritten) {
      console.info(`Succeeded in writing, size is: ${bytesWritten}`);
    }
  }
  randomAccessFile.close();
  fileIo.closeSync(file);
});
```



#### writeSync10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

writeSync(buffer: ArrayBuffer | string, options?: WriteOptions): number

以同步方法将数据写入文件。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer \| string | 是 | 待写入文件的数据，可来自缓冲区或字符串。 |
| options | WriteOptions | 否 | 支持如下选项： - length，number类型，表示期望写入数据的长度，单位为Byte。可选，默认缓冲区长度。 - offset，number类型，表示期望写入文件位置，单位为Byte（基于当前filePointer加上offset的位置）。可选，默认从偏移指针（filePointer）开始写。 - encoding，string类型，当数据是string类型时有效，表示数据的编码方式，默认 'utf-8'。仅支持 'utf-8'。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 实际写入的长度，单位为Byte。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { WriteOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let randomAccessFile = fileIo.createRandomAccessFileSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
let writeOption: WriteOptions = {
  offset: 5,
  length: 5,
  encoding: 'utf-8'
};
let bytesWritten = randomAccessFile.writeSync("hello, world", writeOption);
randomAccessFile.close();
```



#### read10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

read(buffer: ArrayBuffer, options?: ReadOptions): Promise&lt;number&gt;

从文件读取数据，使用promise异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 用于读取文件的缓冲区。 |
| options | ReadOptions | 否 | 支持如下选项： - length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认为缓冲区长度。 - offset，number类型，表示期望读取文件位置，单位为Byte（基于当前filePointer加上offset的位置）。可选，默认从偏移指针（filePointer）开始读。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | Promise对象。返回读取的结果，单位为Byte。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { ReadOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
let randomAccessFile = fileIo.createRandomAccessFileSync(file);
let bufferLength: number = 4096;
let readOption: ReadOptions = {
  offset: 1,
  length: 5
};
let arrayBuffer = new ArrayBuffer(bufferLength);
randomAccessFile.read(arrayBuffer, readOption).then((readLength: number) => {
  console.info(`Succeeded in reading, read length: ${readLength}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to read. Code: ${err.code}, message: ${err.message}`);
}).finally(() => {
  randomAccessFile.close();
  fileIo.closeSync(file);
});
```



#### read10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

read(buffer: ArrayBuffer, callback: AsyncCallback&lt;number&gt;): void

从文件读取数据。使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 用于读取文件的缓冲区。 |
| callback | AsyncCallback&lt;number&gt; | 是 | 回调函数，返回实际读取的数据长度，单位为Byte。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
let randomAccessFile = fileIo.createRandomAccessFileSync(file);
let length: number = 20;

let arrayBuffer = new ArrayBuffer(length);
randomAccessFile.read(arrayBuffer, (err: BusinessError, readLength: number) => {
  if (err) {
    console.error(`Failed to read. Code: ${err.code}, message: ${err.message}`);
  } else {
    if (readLength) {
      console.info(`Succeeded in reading, size is: ${readLength}`);
    }
  }
  randomAccessFile.close();
  fileIo.closeSync(file);
});
```



#### read10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

read(buffer: ArrayBuffer, options: ReadOptions, callback: AsyncCallback&lt;number&gt;): void

从文件读取数据，支持配置读取选项。使用callback异步回调。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 用于读取文件的缓冲区。 |
| options | ReadOptions | 是 | 支持如下选项： - length，number类型，表示读取数据的长度，单位为Byte。可选，默认为缓冲区长度。 - offset，number类型，表示读取文件位置，单位为Byte（基于当前filePointer加上offset的位置）。可选，默认从filePointer开始读。 |
| callback | AsyncCallback&lt;number&gt; | 是 | 回调函数，返回实际读取的数据长度，单位为Byte。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
import { BusinessError } from '@kit.BasicServicesKit';
import { ReadOptions } from '@kit.CoreFileKit';

let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
let randomAccessFile = fileIo.createRandomAccessFileSync(file);
let length: number = 20;
let readOption: ReadOptions = {
  offset: 1,
  length: 5
};
let arrayBuffer = new ArrayBuffer(length);
randomAccessFile.read(arrayBuffer, readOption, (err: BusinessError, readLength: number) => {
  if (err) {
    console.error(`Failed to read. Code: ${err.code}, message: ${err.message}`);
  } else {
    if (readLength) {
      console.info(`Succeeded in reading, size is: ${readLength}`);
    }
  }
  randomAccessFile.close();
  fileIo.closeSync(file);
});
```



#### readSync10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

readSync(buffer: ArrayBuffer, options?: ReadOptions): number

以同步方法从文件读取数据。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 用于读取文件的缓冲区。 |
| options | ReadOptions | 否 | 支持如下选项： - length，number类型，表示期望读取数据的长度，单位为Byte。可选，默认缓冲区长度。 - offset，number类型，表示期望读取文件位置，单位为Byte（基于当前filePointer加上offset的位置）。可选，默认从偏移指针（filePointer）开始读。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 实际读取的长度，单位为Byte。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let filePath = pathDir + "/test.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
let randomAccessFile = fileIo.createRandomAccessFileSync(file);
let length: number = 4096;
let arrayBuffer = new ArrayBuffer(length);
let readLength = randomAccessFile.readSync(arrayBuffer);
randomAccessFile.close();
fileIo.closeSync(file);
```



#### getReadStream12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getReadStream(): ReadStream

获取当前 RandomAccessFile 的一个 ReadStream 实例。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ReadStream | 文件可读流。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**示例：**

```text
const filePath = pathDir + "/test.txt";
const randomAccessFile = fileIo.createRandomAccessFileSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
const rs = randomAccessFile.getReadStream();
rs.close();
randomAccessFile.close();
```



#### getWriteStream12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getWriteStream(): WriteStream

获取当前 RandomAccessFile 的一个 WriteStream 实例。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**返回值：**

| 类型 | 说明 |
| --- | --- |
| WriteStream | 文件可写流。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**示例：**

```text
const filePath = pathDir + "/test.txt";
const randomAccessFile = fileIo.createRandomAccessFileSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
const ws = randomAccessFile.getWriteStream();
ws.close();
randomAccessFile.close();
```



#### Watcher10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

文件目录变化监听对象。由createWatcher接口获得。



#### start10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

start(): void

开启监听。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let filePath = pathDir + "/test.txt";
let watcher = fileIo.createWatcher(filePath, 0xfff, () => {});
watcher.start();
watcher.stop();
```



#### stop10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

stop(): void

停止监听并移除Watcher对象。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
let filePath = pathDir + "/test.txt";
let watcher = fileIo.createWatcher(filePath, 0xfff, () => {});
watcher.start();
watcher.stop();
```



#### OpenMode

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

open接口flags参数常量。文件打开标签。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 值 | 说明 |
| --- | --- | --- | --- |
| READ_ONLY | number | 0o0 | 只读打开。 元服务API：从API version 11开始，该接口支持在元服务中使用。 |
| WRITE_ONLY | number | 0o1 | 只写打开。 元服务API：从API version 11开始，该接口支持在元服务中使用。 |
| READ_WRITE | number | 0o2 | 读写打开。 元服务API：从API version 11开始，该接口支持在元服务中使用。 |
| CREATE | number | 0o100 | 若文件不存在，则创建文件。 元服务API：从API version 11开始，该接口支持在元服务中使用。 |
| TRUNC | number | 0o1000 | 如果文件存在且以只写或读写的方式打开，则将其长度裁剪为零。 元服务API：从API version 11开始，该接口支持在元服务中使用。 |
| APPEND | number | 0o2000 | 以追加方式打开，后续写将追加到文件末尾。 元服务API：从API version 11开始，该接口支持在元服务中使用。 |
| NONBLOCK | number | 0o4000 | 如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。 |
| DIR | number | 0o200000 | 如果path不指向目录，则出错。 |
| NOFOLLOW | number | 0o400000 | 如果path指向符号链接，则出错。 |
| SYNC | number | 0o4010000 | 以同步IO的方式打开文件。 |




#### Filter10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

文件过滤配置项，支持listFile接口使用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| suffix | Array&lt;string&gt; | 否 | 是 | 文件后缀名完全匹配，各个关键词OR关系。 |
| displayName | Array&lt;string&gt; | 否 | 是 | 文件名模糊匹配，各个关键词OR关系。当前仅支持通配符*。 |
| mimeType | Array&lt;string&gt; | 否 | 是 | mime类型完全匹配，各个关键词OR关系。预留字段，暂不支持使用。 |
| fileSizeOver | number | 否 | 是 | 文件大小匹配，大于指定大小的文件，单位为Byte。 |
| lastModifiedAfter | number | 否 | 是 | 文件最近修改时间匹配，在指定时间点及之后的文件。 |
| excludeMedia | boolean | 否 | 是 | 是否排除Media中已有的文件。true：排除Media中已有的文件；false：不排除Media中已有的文件。预留字段，暂不支持使用。 |




#### ConflictFiles10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

冲突文件信息，支持copyDir及moveDir接口使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| srcFile | string | 源冲突文件路径。 |
| destFile | string | 目标冲突文件路径。 |




#### Options11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

可选项类型，支持readLines接口使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| encoding | string | 文件编码方式。可选项。 |




#### WhenceType11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

枚举，文件偏移指针相对偏移位置类型，支持lseek接口使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SEEK_SET | 0 | 文件起始位置处。 |
| SEEK_CUR | 1 | 当前文件偏移指针位置处。 |
| SEEK_END | 2 | 文件末尾位置处。 |




#### LocationType11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

枚举，文件位置，表示该文件是否在本地或者云端存在。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LOCAL | 1 | 文件在本地存在。 |
| CLOUD | 2 | 文件在云端存在。 |




#### AccessModeType12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

枚举，表示需要校验的具体权限。若不填，默认校验文件是否存在。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EXIST | 0 | 文件是否存在。 |
| WRITE | 2 | 文件是否具有写入权限。 |
| READ | 4 | 文件是否具有读取权限。 |
| READ_WRITE | 6 | 文件是否具有读写权限。 |




#### AccessFlagType12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

枚举，表示需要校验的文件位置。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LOCAL | 0 | 文件是否在本地。 |




#### ReadOptions11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

可选项类型，支持read接口使用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| offset | number | 否 | 是 | 期望读取文件位置，单位为Byte（基于当前filePointer加上offset的位置）。可选，默认从偏移指针（filePointer）开始读。 |
| length | number | 否 | 是 | 期望读取数据的长度，单位为Byte。可选，默认缓冲区长度。 |




#### ReadTextOptions11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

可选项类型，支持readText接口使用，ReadTextOptions继承至[ReadOptions](#readoptions11)。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| offset | number | 否 | 是 | 期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读取。 |
| length | number | 否 | 是 | 期望读取数据的长度，单位为Byte。可选，默认文件长度。 |
| encoding | string | 否 | 是 | 当数据是 string 类型时有效，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。 元服务API：从API version 11开始，该接口支持在元服务中使用。 |




#### WriteOptions11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

可选项类型，支持write接口使用，WriteOptions继承至[Options](#options11)。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| offset | number | 否 | 是 | 期望写入文件位置，单位为Byte（基于当前filePointer加上offset的位置）。可选，默认从偏移指针（filePointer）开始写。 元服务API：从API version 11开始，该接口支持在元服务中使用。 |
| length | number | 否 | 是 | 期望写入数据的长度，单位为Byte。可选，默认缓冲区长度。 元服务API：从API version 11开始，该接口支持在元服务中使用。 |
| encoding | string | 否 | 是 | 当数据是string类型时有效，表示数据的编码方式。默认 'utf-8'。仅支持 'utf-8'。 |




#### ListFileOptions11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

可选项类型，支持listFile接口使用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| recursion | boolean | 否 | 是 | 是否递归子目录下文件名。可选，默认为false。当recursion为false时，返回当前目录下满足过滤要求的文件名及目录名。当recursion为true时，返回此目录下所有满足过滤要求的文件的相对路径（以“/”开头）。 |
| listNum | number | 否 | 是 | 列出文件名数量。可选，当设置0时，列出所有文件，默认为0。 |
| filter | Filter | 否 | 是 | 文件过滤配置项。 可选，设置过滤条件。 |




#### ReadStream12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

文件可读流，需要先通过[fileIo.createReadStream](#fileiocreatereadstream12)方法来构建一个ReadStream实例。ReadStream继承自数据流基类[stream.Readable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-stream#readable)。

**规格**：ReadStream读到的数据为解码后的字符串，其编码格式当前仅支持'utf-8'。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bytesRead | number | 是 | 否 | 可读流已经读取的字节数。 |
| path | string | 是 | 否 | 当前可读流对应的文件路径。 |




#### seek12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

seek(offset: number, whence?: WhenceType): number

调整可读流偏移指针位置。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 是 | 相对偏移位置，单位为Byte。 |
| whence | WhenceType | 否 | 偏移指针相对位置类型。默认值：SEEK_SET，文件起始位置处。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前可读流偏移指针位置（相对于文件头的偏移量，单位为Byte）。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**示例：**

```text
const filePath = pathDir + "/test.txt";
const rs = fileIo.createReadStream(filePath);
const curOff = rs.seek(5, fileIo.WhenceType.SEEK_SET);
console.info(`Succeeded in seeking, current offset is ${curOff}`);
rs.close();
```



#### close12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

close(): void

关闭可读流。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
const filePath = pathDir + "/test.txt";
const rs = fileIo.createReadStream(filePath);
rs.close();
```



#### WriteStream12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

文件可写流，需要先通过[fileIo.createWriteStream](#fileiocreatewritestream12)方法来构建一个WriteStream实例。WriteStream继承自数据流基类[stream.Writable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-stream#writable)。



#### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bytesWritten | number | 是 | 否 | 可写流已经写入的字节数。 |
| path | string | 是 | 否 | 当前可写流对应的文件路径。 |




#### seek12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

seek(offset: number, whence?: WhenceType): number;

调整可写流的偏移指针位置。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 是 | 相对偏移位置，单位为Byte。 |
| whence | WhenceType | 否 | 偏移指针相对位置类型。默认值：SEEK_SET，文件起始位置处。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前可写流偏移指针位置（相对于文件头的偏移量，单位为Byte）。 |


**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

**示例：**

```text
const filePath = pathDir + "/test.txt";
const ws = fileIo.createWriteStream(filePath);
const curOff = ws.seek(5, fileIo.WhenceType.SEEK_SET);
console.info(`Succeeded in seeking, current offset is ${curOff}`);
ws.close();
```



#### close12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

close(): void

关闭可写流。

**系统能力**：SystemCapability.FileManagement.File.FileIO

**错误码：**

接口抛出错误码的详细介绍请参见[基础文件IO错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement#基础文件io错误码)。

**示例：**

```text
const filePath = pathDir + "/test.txt";
const ws = fileIo.createWriteStream(filePath);
ws.close();
```



#### RandomAccessFileOptions12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

可选项类型，支持 createRandomAccessFile 接口使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| start | number | 否 | 是 | 表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。 |
| end | number | 否 | 是 | 表示期望读取结束的位置，单位为Byte。可选，默认文件末尾。 |




#### ReadStreamOptions12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

可选项类型，支持 createReadStream 接口使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| start | number | 否 | 是 | 表示期望读取文件的位置，单位为Byte。可选，默认从当前位置开始读。 |
| end | number | 否 | 是 | 表示期望读取结束的位置，单位为Byte。可选，默认文件末尾。 |




#### WriteStreamOptions12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

可选项类型，支持 createWriteStream 接口使用。

**系统能力**：SystemCapability.FileManagement.File.FileIO

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| start | number | 否 | 是 | 表示期望写入文件的位置，单位为Byte。可选，默认从当前位置开始写。 |
| mode | number | 否 | 是 | 创建文件可写流的OpenMode，必须指定如下选项中的一个，默认只写方式创建： - OpenMode.READ_ONLY(0o0)：只读。 - OpenMode.WRITE_ONLY(0o1)：只写。 - OpenMode.READ_WRITE(0o2)：读写。 给定如下功能选项，以按位或的方式追加，默认不给定任何额外选项： - OpenMode.CREATE(0o100)：若文件不存在，则创建文件。 - OpenMode.TRUNC(0o1000)：如果文件存在且文件具有写权限，则将其长度裁剪为零。 - OpenMode.APPEND(0o2000)：以追加方式打开，后续写将追加到文件末尾。 - OpenMode.NONBLOCK(0o4000)：如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。 - OpenMode.DIR(0o200000)：如果path不指向目录，则出错。不允许附加写权限。 - OpenMode.NOFOLLOW(0o400000)：如果path指向符号链接，则出错。 - OpenMode.SYNC(0o4010000)：以同步IO的方式打开文件。 |
