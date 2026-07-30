# 设置KIA文件水印图片

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-set-kia-watermark

#### 场景介绍

为应用提供设置KIA文件水印图片能力。



#### 接口说明

详细接口说明可参考[接口文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataguard-fileguard)。

| 接口名 | 描述 |
| --- | --- |
| setKiaWatermarkImage(image: Uint8Array, info: string): Promise&lt;void&gt; | 使用Promise方式设置KIA文件水印图片。 |




#### 开发步骤
1. 导入模块。

  
```text
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
```

2. 初始化[FileGuard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataguard-fileguard#fileguard)对象guard，调用接口[setKiaWatermarkImage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataguard-fileguard#setkiawatermarkimage)，设置KIA文件水印图片。

  
```text
const TAG: string = 'FileGuard_KIAWatermarkImage';
const DOMAIN: number = 0x0000;

/**
 * 设置KIA文件水印图片。使用Promise异步回调。
 */
async function testSetKiaWaterMarkImage() {
  let fd: number = -1;
  try {
    let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
    let imagePath: string = `/data/service/el2/test_water.png`;
    fd = await guard.openFile(imagePath);
    let stat: fileIo.Stat = fileIo.statSync(fd);
    let buffer: ArrayBuffer = new ArrayBuffer(stat.size);
    fileIo.readSync(fd, buffer);

    let image: Uint8Array = new Uint8Array(buffer);
    let info: string = new Date().toLocaleString();
    guard.setKiaWatermarkImage(image, info).then(() => {
      hilog.info(DOMAIN, TAG, `Succeeded in setting the watermark image for Kia file.`);
    }).catch((err: BusinessError) => {
      hilog.error(DOMAIN, TAG,
        `Failed to set the watermark image for Kia file. Code: ${err.code}, message: ${err.message}.`);
    })
  } catch (e) {
    hilog.error(DOMAIN, TAG, `testSetKiaWaterMarkImage Exception, Code: ${e.code}, message: ${e.message}`);
  } finally {
    if (fd !== -1) {
      fileIo.close(fd);
    }
  }
}
```
