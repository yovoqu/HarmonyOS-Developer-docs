# Class (WebCookieManager)

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webcookiemanager
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

通过WebCookieManager可以控制Web组件中的cookie的各种行为，其中每个应用中的所有Web组件共享一个WebCookieManager实例。cookie的格式遵循[RFC6265](https://www.rfc-editor.org/rfc/rfc6265)标准。当前WebCookieManager的获取cookie接口不支持partitioned cookie。使用隐私模式浏览网页时，Cookie、缓存等数据不会写入本地持久化存储；隐私模式的Web组件销毁后，这些数据将被清除，不会保留。


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```ts
import { webview } from '@kit.ArkWeb';
```


## fetchCookieSync11+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static fetchCookieSync(url: string, incognito?: boolean): string

获取指定url对应cookie的值。


**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 要获取的cookie所属的url，建议使用完整的url。 |
| incognito | boolean | 否 | true表示获取隐私模式下webview的内存cookies，false表示正常非隐私模式下的cookies。          默认值：false。          传入undefined或null会抛出异常错误码401。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| string | 指定url对应的cookie的值。 |


**错误码：**

以下错误码的详细介绍请参见[Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)、[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 17100002 | URL error. No valid cookie found for the specified URL. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |


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
      Button('fetchCookieSync')
      .onClick(() => {
        try {
          let value = webview.WebCookieManager.fetchCookieSync('https://www.example.com');
          console.info("fetchCookieSync cookie = " + value);
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```


## fetchCookie11+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static fetchCookie(url: string, callback: AsyncCallback<string>): void

异步callback方式获取指定url对应cookie的值。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 要获取的cookie所属的url，建议使用完整的url。 |
| callback | AsyncCallback&lt;string&gt; | 是 | callback回调，用于获取cookie |


**错误码：**

以下错误码的详细介绍请参见[Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)、[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 17100002 | URL error. No valid cookie found for the specified URL. |


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
      Button('fetchCookie')
      .onClick(() => {
        try {
          webview.WebCookieManager.fetchCookie('https://www.example.com', (error, cookie) => {
            if (error) {
              console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
              return;
            }
            if (cookie) {
              console.info('fetchCookie cookie = ' + cookie);
            }
          })
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```


## fetchCookie11+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static fetchCookie(url: string): Promise<string>

以Promise方式异步获取指定url对应cookie的值。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 要获取的cookie所属的url，建议使用完整的url。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise实例，用于获取指定url对应的cookie值。 |


**错误码：**

以下错误码的详细介绍请参见[Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)、[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 17100002 | URL error. No valid cookie found for the specified URL. |


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
      Button('fetchCookie')
      .onClick(() => {
        try {
          webview.WebCookieManager.fetchCookie('https://www.example.com')
          .then(cookie => {
            console.info("fetchCookie cookie = " + cookie);
          })
          .catch((error: BusinessError) => {
            console.error(`ErrorCode: ${error.code},  Message: ${error.message}`);
          })
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```


## fetchCookie14+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static fetchCookie(url: string, incognito: boolean): Promise<string>

以Promise方式异步获取指定url对应cookie的值。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 要获取的cookie所属的url，建议使用完整的url。 |
| incognito | boolean | 是 | true表示获取隐私模式下webview的内存cookies，false表示正常非隐私模式下的cookies。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise实例，用于获取指定url对应的cookie值。 |


**错误码：**

以下错误码的详细介绍请参见[Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)、[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 17100002 | URL error. No valid cookie found for the specified URL. |


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
      Button('fetchCookie')
      .onClick(() => {
        try {
          webview.WebCookieManager.fetchCookie('https://www.example.com', false)
          .then(cookie => {
            console.info("fetchCookie cookie = " + cookie);
          })
          .catch((error: BusinessError) => {
            console.error(`ErrorCode: ${error.code},  Message: ${error.message}`);
          })
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```


## configCookieSync11+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static configCookieSync(url: string, value: string, incognito?: boolean): void

为指定url设置单个cookie的值。


**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 要设置的cookie所属的url，建议使用完整的url。 |
| value | string | 是 | 要设置的cookie的值。 |
| incognito | boolean | 否 | true表示设置隐私模式下对应url的cookies，false表示设置正常非隐私模式下对应url的cookies。          默认值：false。          传入undefined或null会抛出异常错误码401。 |


**错误码：**

以下错误码的详细介绍请参见[Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)、[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 17100002 | URL error. No valid cookie found for the specified URL. |
| 17100005 | The provided cookie value is invalid. It must follow the format specified in RFC 6265. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |


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
      Button('configCookieSync')
      .onClick(() => {
        try {
          // configCookieSync每次仅支持设置单个cookie值。
          webview.WebCookieManager.configCookieSync('https://www.example.com', 'a=b');
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```


## configCookieSync14+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static configCookieSync(url: string, value: string, incognito: boolean, includeHttpOnly: boolean): void

为指定url设置cookie的值。


**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 要设置的cookie所属的url，建议使用完整的url。 |
| value | string | 是 | 要设置的cookie的值。 |
| incognito | boolean | 是 | true表示设置隐私模式下对应url的cookies，false表示设置正常非隐私模式下对应url的cookies。 |
| includeHttpOnly | boolean | 是 | true表示允许覆盖含有http-only的cookies，false表示不允许覆盖含有http-only的cookies。 |


**错误码：**

以下错误码的详细介绍请参见[Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)、[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 17100002 | URL error. No valid cookie found for the specified URL. |
| 17100005 | The provided cookie value is invalid. It must follow the format specified in RFC 6265. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |


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
      Button('configCookieSync')
      .onClick(() => {
        try {
          // 仅支持设置单个cookie值。
          webview.WebCookieManager.configCookieSync('https://www.example.com', 'a=b', false, false);
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```


## configCookie11+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static configCookie(url: string, value: string, callback: AsyncCallback<void>): void

异步callback方式为指定url设置单个cookie的值。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 要设置的cookie所属的url，建议使用完整的url。 |
| value | string | 是 | 要设置的cookie的值。 |
| callback | AsyncCallback&lt;void&gt; | 是 | callback回调，用于获取设置cookie的结果 |


**错误码：**

以下错误码的详细介绍请参见[Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)、[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 17100002 | URL error. No valid cookie found for the specified URL. |
| 17100005 | The provided cookie value is invalid. It must follow the format specified in RFC 6265. |


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
      Button('configCookie')
      .onClick(() => {
        try {
          webview.WebCookieManager.configCookie('https://www.example.com', "a=b", (error) => {
            if (error) {
              console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
            }
          })
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```


## configCookie11+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static configCookie(url: string, value: string): Promise<void>

指定url设置单个cookie的值。使用Promise异步回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 要设置的cookie所属的url，建议使用完整的url。 |
| value | string | 是 | 要设置的cookie的值。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise实例，用于获取指定url设置单个cookie值是否成功。 |


**错误码：**

以下错误码的详细介绍请参见[Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)、[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 17100002 | URL error. No valid cookie found for the specified URL. |
| 17100005 | The provided cookie value is invalid. It must follow the format specified in RFC 6265. |


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
      Button('configCookie')
      .onClick(() => {
        try {
          webview.WebCookieManager.configCookie('https://www.example.com', 'a=b')
          .then(() => {
            console.info('configCookie success!');
          })
          .catch((error: BusinessError) => {
            console.info('error: ' + JSON.stringify(error));
          })
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```


## configCookie14+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static configCookie(url: string, value: string, incognito: boolean, includeHttpOnly: boolean): Promise<void>

指定url设置单个cookie的值。使用Promise异步回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 要设置的cookie所属的url，建议使用完整的url。 |
| value | string | 是 | 要设置的cookie的值。 |
| incognito | boolean | 是 | true表示设置隐私模式下对应url的cookies，false表示设置正常非隐私模式下对应url的cookies。 |
| includeHttpOnly | boolean | 是 | true表示允许覆盖含有http-only的cookies，false表示不允许覆盖含有http-only的cookies。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise实例，用于获取指定url设置单个cookie值是否成功。 |


**错误码：**

以下错误码的详细介绍请参见[Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)、[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 17100002 | URL error. No valid cookie found for the specified URL. |
| 17100005 | The provided cookie value is invalid. It must follow the format specified in RFC 6265. |


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
      Button('configCookie')
      .onClick(() => {
        try {
          webview.WebCookieManager.configCookie('https://www.example.com', 'a=b', false, false)
          .then(() => {
            console.info('configCookie success!');
          })
          .catch((error: BusinessError) => {
            console.info('error: ' + JSON.stringify(error));
          })
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```


## saveCookieSync15+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static saveCookieSync(): void

将当前可通过fetchCookie获取到的所有需要持久化的cookie同步保存到磁盘中。

**系统能力：** SystemCapability.Web.Webview.Core


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
      Button('saveCookieSync')
      .onClick(() => {
        try {
          webview.WebCookieManager.saveCookieSync();
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```


## saveCookieAsync
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static saveCookieAsync(callback: AsyncCallback<void>): void

将当前可通过fetchCookie获取到的所有需要持久化的cookie异步保存到磁盘中。


**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | callback回调，用于获取cookie是否成功保存。 |


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
      Button('saveCookieAsync')
      .onClick(() => {
        try {
          webview.WebCookieManager.saveCookieAsync((error) => {
            if (error) {
              console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
            }
          })
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```


## saveCookieAsync
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static saveCookieAsync(): Promise<void>

将当前可通过fetchCookie获取到的所有需要持久化的cookie以Promise方法异步保存到磁盘中。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise实例，用于获取cookie是否成功保存。 |


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
      Button('saveCookieAsync')
      .onClick(() => {
        try {
          webview.WebCookieManager.saveCookieAsync()
          .then(() => {
            console.info("saveCookieAsyncCallback success!");
          })
          .catch((error: BusinessError) => {
            console.error("error: " + error);
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


## putAcceptCookieEnabled
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static putAcceptCookieEnabled(accept: boolean): void

设置WebCookieManager实例是否拥有发送和接收cookie的权限。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| accept | boolean | 是 | 设置是否拥有发送和接收cookie的权限，默认为true，表示拥有发送和接收cookie的权限。false表示没有发送和接收cookie的权限。 |


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
      Button('putAcceptCookieEnabled')
      .onClick(() => {
        try {
          webview.WebCookieManager.putAcceptCookieEnabled(false);
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```


## isCookieAllowed
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static isCookieAllowed(): boolean

获取WebCookieManager实例是否拥有发送和接收cookie的权限。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| boolean | 是否拥有发送和接收cookie的权限。          true表示拥有发送和接收cookie的权限，false表示无发送和接收cookie的权限。          默认值：true。 |


**示例：**


```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('isCookieAllowed')
      .onClick(() => {
        let result = webview.WebCookieManager.isCookieAllowed();
        console.info("result: " + result);
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```


## putAcceptThirdPartyCookieEnabled
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static putAcceptThirdPartyCookieEnabled(accept: boolean): void

设置WebCookieManager实例是否拥有发送和接收第三方cookie的权限。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| accept | boolean | 是 | 是否允许设置、获取第三方cookie。          true表示允许设置、获取第三方cookie，false表示不允许设置、获取第三方cookie。 |


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
      Button('putAcceptThirdPartyCookieEnabled')
      .onClick(() => {
        try {
          webview.WebCookieManager.putAcceptThirdPartyCookieEnabled(false);
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```


## isThirdPartyCookieAllowed
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static isThirdPartyCookieAllowed(): boolean

获取WebCookieManager实例是否拥有发送和接收第三方cookie的权限。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| boolean | 是否拥有发送和接收第三方cookie的权限。          true表示拥有发送和接收第三方cookie的权限，false表示无发送和接收第三方cookie的权限。          默认值：false。 |


**示例：**


```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('isThirdPartyCookieAllowed')
      .onClick(() => {
        let result = webview.WebCookieManager.isThirdPartyCookieAllowed();
        console.info("result: " + result);
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```


## existCookie
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static existCookie(incognito?: boolean): boolean

获取是否存在cookie。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| incognito11+ | boolean | 否 | true表示隐私模式下查询是否存在cookies，false表示正常非隐私模式下查询是否存在cookies。          默认值：false。          传入undefined或null时返回undefined。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| boolean | true表示存在cookie，false表示不存在cookie。 |


**示例：**


```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('existCookie')
      .onClick(() => {
        let result = webview.WebCookieManager.existCookie();
        console.info("result: " + result);
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```


## clearAllCookiesSync11+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static clearAllCookiesSync(incognito?: boolean): void

清除所有cookie。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| incognito | boolean | 否 | true表示清除隐私模式下Webview的所有内存cookies，false表示清除正常非隐私模式下的持久化cookies。          默认值：false。          传入undefined或null时不清除cookies。 |


**示例：**


```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('clearAllCookiesSync')
      .onClick(() => {
        webview.WebCookieManager.clearAllCookiesSync();
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```


## clearAllCookies11+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static clearAllCookies(callback: AsyncCallback<void>): void

异步callback方式清除所有cookie。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | callback回调，用于获取清除所有cookie是否成功。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |


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
      Button('clearAllCookies')
      .onClick(() => {
        try {
          webview.WebCookieManager.clearAllCookies((error) => {
            if (error) {
              console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
            }
          })
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```


## clearAllCookies11+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static clearAllCookies(): Promise<void>

清除所有cookie。使用Promise异步回调。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise实例，用于获取清除所有cookie是否成功。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |


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
      Button('clearAllCookies')
      .onClick(() => {
        webview.WebCookieManager.clearAllCookies()
        .then(() => {
          console.info("clearAllCookies success!");
        })
        .catch((error: BusinessError) => {
          console.error("error: " + error);
        });
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```


## clearSessionCookieSync11+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static clearSessionCookieSync(): void

清除所有会话cookie。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**


```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('clearSessionCookieSync')
      .onClick(() => {
        webview.WebCookieManager.clearSessionCookieSync();
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```


## clearSessionCookie11+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static clearSessionCookie(callback: AsyncCallback<void>): void

异步callback方式清除所有会话cookie。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | callback回调，用于获取清除所有会话cookie是否成功。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |


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
      Button('clearSessionCookie')
      .onClick(() => {
        try {
          webview.WebCookieManager.clearSessionCookie((error) => {
            if (error) {
              console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
            }
          })
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```


## clearSessionCookie11+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static clearSessionCookie(): Promise<void>

清除所有会话cookie。使用Promise异步回调。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise实例，用于获取清除所有会话cookie是否成功。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |


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
      Button('clearSessionCookie')
      .onClick(() => {
        try {
          webview.WebCookieManager.clearSessionCookie()
          .then(() => {
            console.info("clearSessionCookie success!");
          })
          .catch((error: BusinessError) => {
            console.error("error: " + error);
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


## setLazyInitializeWebEngine22+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static setLazyInitializeWebEngine(lazy: boolean): void

设置是否延后初始化ArkWeb内核，不调用该方法时，默认不延后初始化ArkWeb内核。


**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lazy | boolean | 是 | 是否延后初始化ArkWeb内核，true：延后，false：不延后。 |


**示例：**


```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';

webview.WebCookieManager.setLazyInitializeWebEngine(true);

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  aboutToAppear(): void {
    webview.WebCookieManager.configCookieSync('https://www.example.com', 'a=b');
    webview.WebCookieManager.fetchCookieSync('https://www.example.com');
  }

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```


## fetchAllCookies23+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static fetchAllCookies(incognito: boolean): Promise<Array<WebHttpCookie>>

获取所有cookie，使用Promise异步回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| incognito | boolean | 是 | true表示获取隐私模式下webview的所有cookie，false表示正常非隐私模式下的所有cookie。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;[WebHttpCookie](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-i#webhttpcookie23)&gt;&gt; | Promise对象，用于获取所有cookie及其对应的字段值。 |


**示例：**


```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController()

  build() {
    Row() {
      Column() {
        Button('Config Cookie')
        .onClick(() => {
          try {
            webview.WebCookieManager.configCookieSync('https://www.example.com', 'a=b');
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })

        Button('Get All Cookies')
        .onClick(() => {
          webview.WebCookieManager.fetchAllCookies(false).then((cookies) => {
            for (let i = 0; i < cookies.length; i++) {
              console.info('fetchAllCookies cookie[' + i + '].name = ' + cookies[i].name);
              console.info('fetchAllCookies cookie[' + i + '].value = ' + cookies[i].value);
            }
          })
        })

        Web({ src: 'https://www.example.com', controller: this.controller})
      }
    }
  }
}
```


## getCookie(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static getCookie(url: string): string

获取指定url对应cookie的值。


> [!NOTE]
> 从API version 9开始支持，从API version 11开始废弃。建议使用[fetchCookieSync](#fetchcookiesync11)替代。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 要获取的cookie所属的url，建议使用完整的url。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| string | 指定url对应的cookie的值。 |


**错误码：**

以下错误码的详细介绍请参见[Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)、[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 17100002 | URL error. No valid cookie found for the specified URL. |
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
      Button('getCookie')
      .onClick(() => {
        try {
          let value = webview.WebCookieManager.getCookie('https://www.example.com');
          console.info("value: " + value);
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```


## setCookie(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static setCookie(url: string, value: string): void

为指定url设置单个cookie的值。


> [!NOTE]
> 从API version 9开始支持，从API version 11开始废弃。建议使用[configCookieSync11+](#configcookiesync11)替代。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 要设置的cookie所属的url，建议使用完整的url。 |
| value | string | 是 | 要设置的cookie的值。 |


**错误码：**

以下错误码的详细介绍请参见[Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)、[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。


| 错误码ID | 错误信息 |
| --- | --- |
| 17100002 | URL error. No valid cookie found for the specified URL. |
| 17100005 | The provided cookie value is invalid. It must follow the format specified in RFC 6265. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |


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
      Button('setCookie')
      .onClick(() => {
        try {
          webview.WebCookieManager.setCookie('https://www.example.com', 'a=b');
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```


## deleteEntireCookie(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static deleteEntireCookie(): void

清除所有cookie。


> [!NOTE]
> 从API version 9开始支持，从API version 11开始废弃。建议使用[clearAllCookiesSync](#clearallcookiessync11)替代。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**


```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('deleteEntireCookie')
      .onClick(() => {
        webview.WebCookieManager.deleteEntireCookie();
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```


## deleteSessionCookie(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static deleteSessionCookie(): void

清除所有会话cookie。


> [!NOTE]
> 从API version 9开始支持，从API version 11开始废弃。建议使用[clearSessionCookieSync](#clearsessioncookiesync11)替代。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**


```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('deleteSessionCookie')
      .onClick(() => {
        webview.WebCookieManager.deleteSessionCookie();
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```
