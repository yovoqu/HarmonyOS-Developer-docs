# @system.package (应用管理)

更新时间：2026-05-08 09:27:50

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-package
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```ts
import Package from '@system.package';
```


## package.hasInstalled(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


> [!NOTE]
> 从API version 3开始支持，从API version 9开始废弃，建议使用[getBundleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager#bundlemanagergetbundleinfo14)替代。

hasInstalled(options: CheckPackageHasInstalledOptions): void

查询指定应用是否存在，或者原生应用是否安装。

**系统能力：** SystemCapability.BundleManager.BundleFramework

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [CheckPackageHasInstalledOptions](#checkpackagehasinstalledoptions) | 是 | 选项参数。 |


**示例：**


```ts
import Package from '@system.package';

@Entry
@Component
struct MainPage {
  hasInstalled() {
    Package.hasInstalled({
      bundleName: 'com.example.bundlename',
      success: (data) => {
        console.info('package has installed: ' + data);
      },
      fail: (msg:string, code) => {
        console.error('query package fail, code: ' + code + ', data: ' + msg);
      },
    });
  }
  build() {
  }
}
```


## CheckPackageHasInstalledResponse
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


> [!NOTE]
> 从API version 3开始支持，从API version 9开始废弃。

指示应用包是否已安装。

**系统能力：** SystemCapability.BundleManager.BundleFramework


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | boolean | 是 | 指示应用是否已安装。 |


## CheckPackageHasInstalledOptions
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


> [!NOTE]
> 从API version 3开始支持，从API version 9开始废弃。

查询包是否已安装时的选项。

**系统能力：** SystemCapability.BundleManager.BundleFramework


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 应用Bundle名称。 |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |
