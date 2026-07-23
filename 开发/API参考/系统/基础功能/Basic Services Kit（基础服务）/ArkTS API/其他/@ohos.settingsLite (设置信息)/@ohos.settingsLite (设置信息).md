# @ohos.settingsLite (设置信息)

更新时间：2026-07-21 07:44:23

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-settings-lite
**支持设备：** Wearable | lite_wearable

本模块提供轻量级设置能力，支持跳转至设置页面。
 
> [!NOTE]
> 本模块首批接口从API version 24开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

  

#### 导入模块

**支持设备：** Wearable | lite_wearable

```text
import settingsLite from '@ohos.settingsLite';
```
 
  

#### settingsLite.openPinSettingPage

**支持设备：** Wearable | lite_wearable

openPinSettingPage(): void
 
打开密码设置页面。
 
**系统能力：** SystemCapability.Applications.Settings.Core.Lite
 
**模型约束：** 此接口仅可在FA模型下使用。
 
**示例：**
 
```text
import settingsLite from '@ohos.settingsLite';

settingsLite.openPinSettingPage();
```
 
  

#### settingsLite.openNfcSettingsPage

**支持设备：** Wearable | lite_wearable

openNfcSettingsPage(): void
 
打开NFC设置页面。
 
**系统能力：** SystemCapability.Applications.Settings.Core.Lite
 
**模型约束：** 此接口仅可在FA模型下使用。
 
**示例：**
 
```text
import settingsLite from '@ohos.settingsLite';

settingsLite.openNfcSettingsPage();
```
 
  

#### settingsLite.openDoubleClickSettingsPage

**支持设备：** Wearable | lite_wearable

openDoubleClickSettingsPage(): void
 
打开按键设置-双击下按键页面。
 
**系统能力：** SystemCapability.Applications.Settings.Core.Lite
 
**模型约束：** 此接口仅可在FA模型下使用。
 
**示例：**
 
```text
import settingsLite from '@ohos.settingsLite';

settingsLite.openDoubleClickSettingsPage();
```
 
  

#### settingsLite.isDoubleClickAppForSelf

**支持设备：** Wearable | lite_wearable

isDoubleClickAppForSelf(callback: ClickCallback): void
 
判断双击下按键的默认启动应用是否为本应用。
 
**系统能力：** SystemCapability.Applications.Settings.Core.Lite
 
**模型约束：** 此接口仅可在FA模型下使用。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | ClickCallback | 是 | 返回检查结果。 |
 
 
**示例：**
 
```text
import settingsLite from '@ohos.settingsLite';

settingsLite.isDoubleClickAppForSelf({
    onResult(result) {
        console.info('isDoubleClickAppForSelf result: ' + result);
    }
});
```
 
  

#### ClickCallback

**支持设备：** Wearable | lite_wearable

按键设置-双击下按键页面检查回调。
 
**系统能力：** SystemCapability.Applications.Settings.Core.Lite
  
| 名称 | 类型 | 说明 |
| --- | --- | --- |
| onResult | (result: boolean) => void | 双击下按键的默认启动应用为当前应用则返回true，否则返回false。 |
