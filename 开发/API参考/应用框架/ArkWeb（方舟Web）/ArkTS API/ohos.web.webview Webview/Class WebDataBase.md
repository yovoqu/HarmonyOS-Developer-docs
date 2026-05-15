# Class (WebDataBase)

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webdatabase
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

Web组件数据库管理对象。


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```ts
import { webview } from '@kit.ArkWeb';
```


## getHttpAuthCredentials
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static getHttpAuthCredentials(host: string, realm: string): Array<string>

检索给定主机和域的HTTP身份验证凭据，该方法为同步方法。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| host | string | 是 | HTTP身份验证凭据应用的主机。 |
| realm | string | 是 | HTTP身份验证凭据应用的域。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| Array&lt;string&gt; | 包含用户名和密码的数组，检索失败返回空数组。 |


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
  host: string = "www.spincast.org";
  realm: string = "protected example";
  username_password: string[] = [];

  build() {
    Column() {
      Button('getHttpAuthCredentials')
      .onClick(() => {
        try {
          this.username_password = webview.WebDataBase.getHttpAuthCredentials(this.host, this.realm);
          console.info('num: ' + this.username_password.length);
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```


## saveHttpAuthCredentials
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static saveHttpAuthCredentials(host: string, realm: string, username: string, password: string): void

保存给定主机和域的HTTP身份验证凭据，该方法为同步方法。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| host | string | 是 | HTTP身份验证凭据应用的主机。 |
| realm | string | 是 | HTTP身份验证凭据应用的域。 |
| username | string | 是 | 用户名。 |
| password | string | 是 | 密码。 |


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
  host: string = "www.spincast.org";
  realm: string = "protected example";

  build() {
    Column() {
      Button('saveHttpAuthCredentials')
      .onClick(() => {
        try {
          webview.WebDataBase.saveHttpAuthCredentials(this.host, this.realm, "Stromgol", "Laroche");
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```


## existHttpAuthCredentials
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static existHttpAuthCredentials(): boolean

判断是否存在任何已保存的HTTP身份验证凭据，该方法为同步方法。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| boolean | 是否存在任何已保存的HTTP身份验证凭据。          存在返回true，不存在返回false。 |


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
      Button('existHttpAuthCredentials')
      .onClick(() => {
        try {
          let result = webview.WebDataBase.existHttpAuthCredentials();
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```


## deleteHttpAuthCredentials
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static deleteHttpAuthCredentials(): void

清除所有已保存的HTTP身份验证凭据，该方法为同步方法。

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
      Button('deleteHttpAuthCredentials')
      .onClick(() => {
        try {
          webview.WebDataBase.deleteHttpAuthCredentials();
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```
