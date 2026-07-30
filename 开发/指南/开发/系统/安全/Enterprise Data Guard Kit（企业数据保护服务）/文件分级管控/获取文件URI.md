# 获取文件URI

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-get-file-url

#### 场景介绍

Enterprise Data Guard Kit为应用提供获取[用户个人数据目录](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/dataguard-introduction#访问限制)下文件路径信息的能力，该路径可被应用直接打开，从而辅助判断是否是KIA文件。



#### 接口说明

详细接口说明可参考[接口文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataguard-fileguard)。

| 接口名 | 描述 |
| --- | --- |
| getFileUri(path: string, callback: AsyncCallback&lt;FilePathInfo&gt;): void | 使用Callback方式获取文件路径信息。 |
| getFileUri(path: string): Promise&lt;FilePathInfo&gt; | 使用Promise方式获取文件路径信息。 |




#### 开发步骤
1. 导入模块。

  
```text
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
```

2. 初始化[FileGuard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataguard-fileguard#fileguard)对象guard，调用接口[getFileUri](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataguard-fileguard#getfileuri)，获取文件URI。

  
通过回调函数方式，获取文件URI。

  
```text
const TAG: string = 'FileGuard_FileUri';
const DOMAIN: number = 0x0000;

/**
 * 获取文件URI。使用callback异步回调。
 * @param accountId: 用户ID
 */
function getFileUriCallBack(accountId: number) {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = `/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/aaa.txt`;
  guard.getFileUri(path, (err: BusinessError, data: fileGuard.FilePathInfo) => {
    if (err) {
      hilog.error(DOMAIN, TAG, `Failed to get file uri. Code: ${err.code}, message: ${err.message}.`);
    } else {
      hilog.info(DOMAIN, TAG, `Succeeded in getting file uri. absolutePath: ${data.absolutePath}, uri: ${data.uri}.`);
    }
  });
}
```

3. 通过Promise方式，获取文件URI。

  
```text
const TAG: string = 'FileGuard_FileUri';
const DOMAIN: number = 0x0000;

// ...
/**
 * 获取文件URI。使用Promise异步回调。
 * @param accountId: 用户ID
 */
function getFileUriPromise(accountId: number) {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = `/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/bbb.txt`;
  guard.getFileUri(path).then((data: fileGuard.FilePathInfo) => {
    hilog.info(DOMAIN, TAG,
      `Succeeded in getting the uri of file. absolutePath: ${data.absolutePath}, uri: ${data.uri}.`);
  }).catch((err: BusinessError) => {
    hilog.error(DOMAIN, TAG, `Failed to get the uri of file. Code: ${err.code}, message: ${err.message}.`);
  });
}
```
