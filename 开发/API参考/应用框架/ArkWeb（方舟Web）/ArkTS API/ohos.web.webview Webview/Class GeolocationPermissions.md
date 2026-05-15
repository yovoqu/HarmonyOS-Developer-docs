# Class (GeolocationPermissions)

更新时间：2026-04-28 03:31:56

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-geolocationpermissions
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

Web组件地理位置权限管理对象。


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```ts
import { webview } from '@kit.ArkWeb';
```


## 需要权限
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

访问地理位置时需添加权限：ohos.permission.LOCATION、ohos.permission.APPROXIMATELY_LOCATION、ohos.permission.LOCATION_IN_BACKGROUND，具体权限说明请参考[位置服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-geolocation)。


## allowGeolocation
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static allowGeolocation(origin: string, incognito?: boolean): void

允许指定源使用地理位置接口。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| origin | string | 是 | 指定源的字符串。          origin格式必须遵循RFC 6454中定义的格式。 |
| incognito11+ | boolean | 否 | true表示隐私模式下允许指定源使用地理位置，false表示正常非隐私模式下允许指定源使用地理位置。          默认值：false。          传入null或undefined时为false。 |


**错误码：**

以下错误码的详细介绍请参见[Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)、[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 17100011 | Invalid origin. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |


**示例：**


```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  origin: string = "file:///";

  build() {
    Column() {
      Button('allowGeolocation')
      .onClick(() => {
        try {
          webview.GeolocationPermissions.allowGeolocation(this.origin);
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```


## deleteGeolocation
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static deleteGeolocation(origin: string, incognito?: boolean): void

清除指定源的地理位置权限状态。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| origin | string | 是 | 指定源的字符串。          origin格式必须遵循RFC 6454中定义的格式。 |
| incognito11+ | boolean | 否 | true表示隐私模式下清除指定源的地理位置权限状态，false表示正常非隐私模式下清除指定源的地理位置权限状态。          默认值：false。          传入null或undefined时为false。 |


**错误码：**

以下错误码的详细介绍请参见[Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)、[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 17100011 | Invalid origin. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |


**示例：**


```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  origin: string = "file:///";

  build() {
    Column() {
      Button('deleteGeolocation')
      .onClick(() => {
        try {
          webview.GeolocationPermissions.deleteGeolocation(this.origin);
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```


## getAccessibleGeolocation
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static getAccessibleGeolocation(origin: string, callback: AsyncCallback<boolean>, incognito?: boolean): void

以回调方式异步获取指定源的地理位置权限状态。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| origin | string | 是 | 指定源的字符串。          origin格式必须遵循RFC 6454中定义的格式。 |
| callback | AsyncCallback&lt;boolean&gt; | 是 | 返回指定源的地理位置权限状态。          获取成功，true表示已授权，false表示拒绝访问。          获取失败，表示不存在指定源的权限状态。 |
| incognito11+ | boolean | 否 | true表示隐私模式下以回调方式异步获取指定源的地理位置权限状态，false表示正常非隐私模式下以回调方式异步获取指定源的地理位置权限状态。          默认值：false。          传入null或undefined时会抛出异常错误码401。 |


**错误码：**

以下错误码的详细介绍请参见[Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)、[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 17100011 | Invalid origin. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |


**示例：**


```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  origin: string = "file:///";

  build() {
    Column() {
      Button('getAccessibleGeolocation')
      .onClick(() => {
        try {
          webview.GeolocationPermissions.getAccessibleGeolocation(this.origin, (error, result) => {
            if (error) {
              console.error(`getAccessibleGeolocationAsync error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
              return;
            }
            console.info('getAccessibleGeolocationAsync result: ' + result);
          });
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```


## getAccessibleGeolocation
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static getAccessibleGeolocation(origin: string, incognito?: boolean): Promise<boolean>

以Promise方式异步获取指定源的地理位置权限状态。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| origin | string | 是 | 指定源的字符串。          origin格式必须遵循RFC 6454中定义的格式。 |
| incognito11+ | boolean | 否 | true表示隐私模式下以Promise方式异步获取指定源的地理位置权限状态，false表示正常非隐私模式下以Promise方式异步获取指定源的地理位置权限状态。          默认值：false。          传入null或undefined时会抛出异常错误码401。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Promise实例，用于获取指定源的权限状态。          获取成功，true表示已授权，false表示拒绝访问。          获取失败，表示不存在指定源的权限状态。 |


**错误码：**

以下错误码的详细介绍请参见[Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)、[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 17100011 | Invalid origin. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |


**示例：**


```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  origin: string = "file:///";

  build() {
    Column() {
      Button('getAccessibleGeolocation')
      .onClick(() => {
        try {
          webview.GeolocationPermissions.getAccessibleGeolocation(this.origin)
          .then(result => {
            console.info('getAccessibleGeolocationPromise result: ' + result);
          }).catch((error: BusinessError) => {
            console.error(`getAccessibleGeolocationPromise error, ErrorCode: ${error.code},  Message: ${error.message}`);
          });
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```


## getStoredGeolocation
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static getStoredGeolocation(callback: AsyncCallback<Array<string>>, incognito?: boolean): void

以回调方式异步获取已存储地理位置权限状态的所有源信息。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;Array&lt;string&gt;&gt; | 是 | 返回已存储地理位置权限状态的所有源信息。 |
| incognito11+ | boolean | 否 | true表示隐私模式下以回调方式异步获取已存储地理位置权限状态的所有源信息，false表示正常非隐私模式下以回调方式异步获取已存储地理位置权限状态的所有源信息。          默认值：false。          传入null或undefined时会抛出异常错误码401。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |


**示例：**


```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getStoredGeolocation')
      .onClick(() => {
        try {
          webview.GeolocationPermissions.getStoredGeolocation((error, origins) => {
            if (error) {
              console.error(`getStoredGeolocationAsync error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
              return;
            }
            let origins_str: string = origins.join();
            console.info('getStoredGeolocationAsync origins: ' + origins_str);
          });
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```


## getStoredGeolocation
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static getStoredGeolocation(incognito?: boolean): Promise<Array<string>>

以Promise方式异步获取已存储地理位置权限状态的所有源信息。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| incognito11+ | boolean | 否 | true表示隐私模式下以Promise方式异步获取已存储地理位置权限状态的所有源信息，false表示正常非隐私模式下以Promise方式异步获取已存储地理位置权限状态的所有源信息。          默认值：false。          传入null或undefined时会抛出异常错误码401。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;string&gt;&gt; | Promise实例，用于获取已存储地理位置权限状态的所有源信息。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |


**示例：**


```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getStoredGeolocation')
      .onClick(() => {
        try {
          webview.GeolocationPermissions.getStoredGeolocation()
          .then(origins => {
            let origins_str: string = origins.join();
            console.info('getStoredGeolocationPromise origins: ' + origins_str);
          }).catch((error: BusinessError) => {
            console.error(`getStoredGeolocationPromise error, ErrorCode: ${error.code},  Message: ${error.message}`);
          });
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```


## deleteAllGeolocation
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static deleteAllGeolocation(incognito?: boolean): void

清除所有源的地理位置权限状态。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| incognito11+ | boolean | 否 | true表示隐私模式下清除所有源的地理位置权限状态，false表示正常非隐私模式下清除所有源的地理位置权限状态。          默认值：false。          传入null或undefined时为false。 |


**示例：**


```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('deleteAllGeolocation')
      .onClick(() => {
        try {
          webview.GeolocationPermissions.deleteAllGeolocation();
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```
