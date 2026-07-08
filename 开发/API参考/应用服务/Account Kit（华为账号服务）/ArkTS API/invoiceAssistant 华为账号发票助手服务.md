# @hms.core.account.invoiceAssistant (华为账号发票助手服务)

更新时间：2026-07-03 02:18:23

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-invoiceassistant
**支持设备：** Phone | PC/2in1 | Tablet

#### 模块概述

**支持设备：** Phone | PC/2in1 | Tablet

@hms.core.account.invoiceAssistant模块提供华为账号发票助手能力。开发者可通过该能力拉起发票抬头选择页面，帮助用户快速管理、选择发票抬头。用户选择发票抬头后，会将发票抬头信息返回给开发者，可用于完善相关业务场景。
 
**起始版本：** 5.0.0(12)
 
  

#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet

```text
import { invoiceAssistant } from '@kit.AccountKit';
```
 
  

#### InvoiceAssistantErrorCode

**支持设备：** Phone | PC/2in1 | Tablet

华为账号发票助手服务接口错误码枚举。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.HuaweiID.InvoiceAssistant
 
**起始版本：** 5.0.0(12)
  
| 名称 | 值 | 说明 |
| --- | --- | --- |
| USER_CANCELED | 1010060001 | 用户取消发票助手服务。 |
| SYSTEM_ERROR | 1010060002 | 系统内部错误。 |
| APP_NOT_AUTHORIZED | 1010060003 | 应用指纹证书校验失败。 |
| FREQUENT_CALLS | 1010060004 | 接口调用过于频繁。 |
| NETWORK_ERROR | 1010060005 | 网络连接错误。 |
| ACCOUNT_NOT_LOGGED_IN | 1010060006 | 用户未登录华为账号。 |
| INVOICE_TITLE_EXISTS | 1010060007 | 发票抬头信息已存在。 |
| UNSUPPORTED | 1010060008 | 已登录的华为账号不支持发票助手服务。 |
 
 
  

#### InvoiceTitle

**支持设备：** Phone | PC/2in1 | Tablet

发票抬头数据结构。[selectInvoiceTitle](#selectinvoicetitle)返回值，包含发票抬头、公司信息等数据。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.HuaweiID.InvoiceAssistant
 
**起始版本：** 5.0.0(12)
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | string | 否 | 否 | 抬头类型，0-个人 1-企业。 |
| title | string | 否 | 否 | 抬头名称。 |
| taxNumber | string | 否 | 否 | 纳税人识别号。如果抬头类型为企业，则根据真实值返回；如果抬头类型为个人，则返回空字符串。 |
| companyAddress | string | 否 | 否 | 公司地址。如果抬头类型为企业，则根据真实值返回；如果抬头类型为个人，则返回空字符串。 |
| telephone | string | 否 | 否 | 公司电话。如果抬头类型为企业，则根据真实值返回；如果抬头类型为个人，则返回空字符串。 |
| bankName | string | 否 | 否 | 公司银行名称。如果抬头类型为企业，则根据真实值返回；如果抬头类型为个人，则返回空字符串。 |
| bankAccount | string | 否 | 否 | 公司银行账户。如果抬头类型为企业，则根据真实值返回；如果抬头类型为个人，则返回空字符串。 |
 
 
  

#### selectInvoiceTitle

**支持设备：** Phone | PC/2in1 | Tablet

selectInvoiceTitle(context: common.Context): Promise&lt;InvoiceTitle&gt;
 
选择发票抬头方法。开发者可调用该方法打开发票抬头选择页面，用户选择发票抬头后，会通过Promise异步回调，返回发票抬头信息。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.HuaweiID.InvoiceAssistant
 
**起始版本：** 5.0.0(12)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.Context | 是 | Context上下文。 应用可支持的Context有：UIAbilityContext和UIExtensionContext。不支持应用在半模态、弹出框、子窗口等非全页面组件中使用UIExtensionContext调用。 元服务可支持的Context有：UIAbilityContext。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;InvoiceTitle&gt; | Promise对象，返回InvoiceTitle对象。 |
 
 
**错误码：**
 
以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account-kit)。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1010060001 | The operation was canceled by the user. |
| 1010060002 | System internal error. |
| 1010060003 | Failed to check the fingerprint of the app bundle. |
| 1010060004 | Too frequent API calls. |
| 1010060005 | Network connection error. |
| 1010060006 | The HUAWEI ID is not signed in. |
| 1010060007 | Failed to create an invoice title because the title already exists. |
| 1010060008 | The invoice service does not support the logged HUAWEI ID. |
 
 
**示例：**
 
```text
import { invoiceAssistant } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 执行请求
if (canIUse('SystemCapability.HuaweiID.InvoiceAssistant')) {
  try {
    // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
    invoiceAssistant.selectInvoiceTitle(this.getUIContext().getHostContext())
      .then((data: invoiceAssistant.InvoiceTitle) => {
        hilog.info(0x0000, 'testTag', 'Succeeded in selecting invoice title');
        const type: string = data.type;
        const title: string = data.title;
        const taxNumber: string = data.taxNumber;
        const companyAddress: string = data.companyAddress;
        const telephone: string = data.telephone;
        const bankName: string = data.bankName;
        const bankAccount: string = data.bankAccount;

        // 开发者处理type, title, taxNumber, companyAddress, telephone, bankName, bankAccount
        // ...

      })
      .catch((error: BusinessError<Object>) => {
        dealAllError(error);
      });
  } catch (error) {
    dealAllError(error);
  }
} else {
  hilog.info(0x0000, 'testTag',
    'The current device does not support the invoking of the selectInvoiceTitle interface.');
}

// 错误处理
function dealAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', `Failed to select invoice title. Code: ${error.code}, message: ${error.message}`);
}
```
