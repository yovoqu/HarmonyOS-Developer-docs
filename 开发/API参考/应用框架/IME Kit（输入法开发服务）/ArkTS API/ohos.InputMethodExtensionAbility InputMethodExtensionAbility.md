# @ohos.InputMethodExtensionAbility (InputMethodExtensionAbility)

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod-extension-ability
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

本模块支持开发者自行开发输入法应用，以及管理输入法Extension的生命周期。

> [!NOTE]
> 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 本模块接口仅可在Stage模型下使用。



#### 约束限制

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

为保障系统安全性和稳定性，防止InputMethodExtensionAbility滥用系统资源，系统对其能力进行管控，不支持部分模块的引用，详情请参考[附录](#附录)。

另外输入法应用区分基础模式和完整体验模式，关于基础模式和完整体验模式说明如下：

**基础模式介绍：**

基础模式下，输入法扩展（InputMethodExtensionAbility）进程无法拉起其他UIAbility或ExtensionAbility。

基础模式下，输入法扩展会受到系统管控，不能使用涉及访问或泄露用户个人数据的各种接口，同时无法将数据传递出进程。管控功能包括但不限于：网络、短信、电话、麦克风、定位、相机、蓝牙、壁纸、支付、日历、游戏、扬声器、Wi-Fi、剪切板、多媒体、联系人、公共事件、系统账号、健康数据、地图服务、推送服务、融合搜索、共享内存、分布式特性、广告设备标识、振动等。

基础模式下，输入法扩展可以使用基础输入功能必要的系统能力，例如，IME Kit、ArkUI、窗口、图形、屏幕管理等。

基础模式下，输入法扩展对共享沙箱只读，对输入法扩展独立沙箱可读写；应用主入口可以对共享沙箱及其独立沙箱读写。

**完整体验模式介绍：**

完整体验模式下，输入法扩展不受基础模式相关限制，例如可以拉起其他UIAbility或ExtensionAbility、可以调用访问用户数据的接口等。

完整体验模式下，输入法扩展可以对共享沙箱读写。



#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { InputMethodExtensionAbility } from '@kit.IMEKit';
```



#### InputMethodExtensionAbility

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

输入法Extension ability类。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework



#### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

输入法Extension ability的上下文信息。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | InputMethodExtensionContext | 否 | 否 | InputMethodExtension的上下文环境，继承于ExtensionContext。 |




#### onCreate

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onCreate(want: Want): void

Extension生命周期回调，在拉起输入法Extension时调用，执行初始化输入法应用操作。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 当前Extension相关的Want类型信息，包括ability名称、bundle名称等。 |


**示例：**

```text
import { InputMethodExtensionAbility } from '@kit.IMEKit';
import { Want } from '@kit.AbilityKit';

class InputMethodExt extends InputMethodExtensionAbility {
  onCreate(want: Want): void {
    console.info('onCreate, want:' + want?.abilityName);
  }
}
```



#### onDestroy

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onDestroy(): void

Extension生命周期回调，在销毁输入法应用时回调，执行资源清理等操作。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**示例：**

```text
import { InputMethodExtensionAbility } from '@kit.IMEKit';

class InputMethodExt extends InputMethodExtensionAbility {
  onDestroy(): void {
    console.info('onDestroy');
  }
}
```



#### 附录

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

InputMethodExtensionAbility不支持以下模块的引用。

| Kit | 模块 |
| --- | --- |
| Ability Kit | @ohos.ability.featureAbility (FeatureAbility模块) @ohos.ability.particleAbility (ParticleAbility模块) |
| Background Tasks Kit | @ohos.resourceschedule.backgroundTaskManager (后台任务管理) @ohos.reminderAgentManager (后台代理提醒) @ohos.reminderAgent (后台代理提醒) |
| Basic Services Kit | @ohos.account.osAccount (系统账号管理) @ohos.account.distributedAccount (分布式账号管理) @ohos.wallpaper (壁纸) |
| Connectivity Kit | @ohos.bluetooth (蓝牙) @ohos.bluetoothManager (蓝牙) nfctech (标准NFC-Tag Nfc 技术) @ohos.nfc.controller (标准NFC) @ohos.nfc.cardEmulation (标准NFC-cardEmulation) @ohos.connectedTag (有源标签) @ohos.wifiext (WLAN扩展接口) @ohos.wifiManager (WLAN) @ohos.wifiManagerExt (WLAN扩展接口) tagSession (标准NFC-Tag TagSession) |
| Location Kit | @ohos.geolocation (位置服务) @ohos.geoLocationManager (位置服务) |
| Telephony Kit | @ohos.telephony.call (拨打电话) @ohos.telephony.data (蜂窝数据) @ohos.telephony.observer (observer) @ohos.telephony.radio (网络搜索) @ohos.telephony.sms (短信服务) @ohos.telephony.sim (SIM卡管理) |
