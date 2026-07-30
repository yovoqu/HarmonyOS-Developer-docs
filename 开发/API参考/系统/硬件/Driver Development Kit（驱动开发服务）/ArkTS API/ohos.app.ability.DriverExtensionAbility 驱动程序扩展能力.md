# @ohos.app.ability.DriverExtensionAbility (驱动程序扩展能力)

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-driverextensionability
**支持设备：** PC/2in1

DriverExtensionAbility模块提供驱动相关扩展能力，提供驱动创建、销毁、连接、断开等生命周期回调。

> [!NOTE]
> 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。



#### 约束限制

**支持设备：** PC/2in1

为保障系统安全性和稳定性，防止 DriverExtensionAbility滥用系统资源，系统对其能力进行管控，不支持部分模块的引用，详情请参考[附录](#附录)。



#### 导入模块

**支持设备：** PC/2in1

```text
import { DriverExtensionAbility } from '@kit.DriverDevelopmentKit';
```



#### DriverExtensionAbility

**支持设备：** PC/2in1



#### 属性

**支持设备：** PC/2in1

DriverExtensionAbility类，包含驱动生命周期回调的定义。

**模型约束**：此接口仅在Stage模型下使用。

**系统能力**：SystemCapability.Driver.ExternalDevice

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | DriverExtensionContext | 否 | 否 | DriverExtension的上下文环境，继承自ExtensionContext。 |




#### onInit

**支持设备：** PC/2in1

onInit(want: Want): void

Extension生命周期回调，在创建时回调，执行初始化业务逻辑操作。

**模型约束**：此接口仅在Stage模型下使用。

**系统能力**：SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 当前Extension相关的Want类型信息，包括ability名称、bundle名称等。 |


**示例：**

```text
import { DriverExtensionAbility } from '@kit.DriverDevelopmentKit';
import { Want } from '@kit.AbilityKit';

class DriverExt extends DriverExtensionAbility {
  onInit(want : Want) {
    console.info(`onInit, want: ${want.abilityName}`);
  }
}
```



#### onRelease

**支持设备：** PC/2in1

onRelease(): void

Extension生命周期回调，在销毁时回调，执行资源清理等操作。

**模型约束**：此接口仅在Stage模型下使用。

**系统能力**：SystemCapability.Driver.ExternalDevice

**示例：**

```text
class DriverExt extends DriverExtensionAbility {
  onRelease() {
    console.info('onRelease');
  }
}
```



#### onConnect

**支持设备：** PC/2in1

onConnect(want: Want): rpc.RemoteObject | Promise<rpc.RemoteObject>

Extension生命周期回调，会在[onCreate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilitystage#oncreate)之后回调。返回一个[RemoteObject](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-rpc#remoteobject)对象，用于客户端和服务端进行通信。

**模型约束**：此接口仅在Stage模型下使用。

**系统能力**：SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 当前Extension相关的Want类型信息，包括ability名称、bundle名称等。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| rpc.RemoteObject \| Promise<rpc.RemoteObject> | 一个RemoteObject对象，用于客户端和服务端进行通信；或一个Promise对象，返回用于通信的RemoteObject对象。 |


**示例：**

```text
import { DriverExtensionAbility } from '@kit.DriverDevelopmentKit';
import { rpc } from '@kit.IPCKit';
import { Want } from '@kit.AbilityKit';

class StubTest extends rpc.RemoteObject{
    constructor(des : string) {
        super(des);
    }
    onRemoteMessageRequest(code : number, data : rpc.MessageSequence, reply : rpc.MessageSequence, option : rpc.MessageOption) {
      // 必须重写此接口
      return true;
    }
}
class DriverExt extends DriverExtensionAbility {
  onConnect(want : Want) {
    console.info(`onConnect , want: ${want.abilityName}`);
    return new StubTest('test');
  }
}
```

如果生成返回值[RemoteObject](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-rpc#remoteobject)依赖一个异步接口，可以使用异步生命周期：

```text
import { DriverExtensionAbility } from '@kit.DriverDevelopmentKit';
import { rpc } from '@kit.IPCKit';
import { Want } from '@kit.AbilityKit';

class StubTest extends rpc.RemoteObject{
    constructor(des : string) {
        super(des);
    }
    onRemoteMessageRequest(code : number, data : rpc.MessageSequence, reply : rpc.MessageSequence, option : rpc.MessageOption) {
      // 必须重写此接口
      return true;
    }
}
async function getDescriptor() {
    // 调用异步函数...
    return "asyncTest";
}
class DriverExt extends DriverExtensionAbility {
  async onConnect(want : Want) {
    console.info(`onConnect , want: ${want.abilityName}`);
    let descriptor = await getDescriptor();
    return new StubTest(descriptor);
  }
}
```



#### onDisconnect

**支持设备：** PC/2in1

onDisconnect(want: Want): void | Promise&lt;void&gt;

Extension的生命周期回调，客户端执行断开连接服务时回调。

**模型约束**：此接口仅在Stage模型下使用。

**系统能力**：SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 当前Extension相关的Want类型信息，包括ability名称、bundle名称等。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| void \| Promise&lt;void&gt; | 返回值为空；或一个Promise对象，无返回结果。 |


**示例：**

```text
import { DriverExtensionAbility } from '@kit.DriverDevelopmentKit';
import { Want } from '@kit.AbilityKit';

class DriverExt extends DriverExtensionAbility {
  onDisconnect(want : Want) {
    console.info(`onDisconnect, want: ${want.abilityName}`);
  }
}
```

在执行完onDisconnect生命周期回调后，应用可能会退出，从而可能导致onDisconnect中的异步函数未能正确执行，比如异步写入数据库。可以使用异步生命周期，以确保异步onDisconnect完成后再继续后续的生命周期。

```text
import { DriverExtensionAbility } from '@kit.DriverDevelopmentKit';
import { Want } from '@kit.AbilityKit';

class DriverExt extends DriverExtensionAbility {
  async onDisconnect(want : Want) {
    console.info(`onDisconnect, want: ${want.abilityName}`);
    // 调用异步函数...
  }
}
```



#### onDump

**支持设备：** PC/2in1

onDump(params: Array&lt;string&gt;): Array&lt;string&gt;

转储客户端信息时调用，建议不要转储敏感信息。

**模型约束**：此接口仅在Stage模型下使用。

**系统能力**：SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | Array&lt;string&gt; | 是 | 表示命令形式的参数。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;string&gt; | 一个string类型的数组，用于转存客户端信息。 |


**示例：**

```json
class DriverExt extends DriverExtensionAbility {
    onDump(params : Array<string>) {
        console.info(`dump, params: ${JSON.stringify(params)}`);
        return ['params'];
    }
}
```



#### DriverExtensionContext

**支持设备：** PC/2in1

type DriverExtensionContext = _DriverExtensionContext;

DriverExtensionAbility的上下文环境。

**系统能力**：SystemCapability.Driver.ExternalDevice

| 类型 | 说明 |
| --- | --- |
| _DriverExtensionContext | DriverExtensionAbility的上下文环境，继承自ExtensionContext，其具体使用方法可参考DriverExtensionContext。 |




#### 附录

**支持设备：** PC/2in1

DriverExtensionAbility不支持以下模块的引用。

| Kit | 模块 |
| --- | --- |
| Ability Kit（程序框架服务） | @ohos.abilityAccessCtrl (程序访问控制管理) |
| Ability Kit（程序框架服务） | @ohos.ability.particleAbility (ParticleAbility模块) |
| Ability Kit（程序框架服务） | @ohos.app.ability.abilityManager (Ability信息管理) |
| Ability Kit（程序框架服务） | @ohos.app.ability.appManager (应用管理) |
| Ability Kit（程序框架服务） | @ohos.application.appManager (appManager) |
| Ability Kit（程序框架服务） | @ohos.bundle (Bundle模块) |
| Ability Kit（程序框架服务） | @ohos.bundle.bundleManager (应用程序包管理模块) |
| Ability Kit（程序框架服务） | @ohos.bundle.defaultAppManager (默认应用管理) |
| Ability Kit（程序框架服务） | @ohos.bundle.launcherBundleManager (launcherBundleManager模块) |
| Ability Kit（程序框架服务） | Context (Stage模型的上下文基类) |
| Ability Kit（程序框架服务） | @ohos.continuation.continuationManager (流转/协同管理) |
| ArkData（方舟数据管理） | @ohos.data.distributedData (分布式数据管理) |
| ArkData（方舟数据管理） | @ohos.data.distributedDataObject (分布式数据对象) |
| ArkData（方舟数据管理） | @ohos.data.distributedKVStore (分布式键值数据库) |
| ArkData（方舟数据管理） | @ohos.data.rdb (关系型数据库) |
| ArkUI（方舟UI框架） | @ohos.screenshot (屏幕截图) |
| Background Tasks Kit（后台任务开发服务） | @ohos.reminderAgent (后台代理提醒) |
| Background Tasks Kit（后台任务开发服务） | @ohos.reminderAgentManager (后台代理提醒) |
| Background Tasks Kit（后台任务开发服务） | @ohos.resourceschedule.backgroundTaskManager (后台任务管理) |
| Background Tasks Kit（后台任务开发服务） | @ohos.backgroundTaskManager (后台任务管理) |
| Background Tasks Kit（后台任务开发服务） | @ohos.bundleState (设备使用信息统计) |
| Basic Services Kit（基础服务） | @ohos.account.appAccount (应用账号管理) |
| Basic Services Kit（基础服务） | @ohos.account.distributedAccount (分布式账号管理) |
| Basic Services Kit（基础服务） | @ohos.account.osAccount (系统账号管理) |
| Basic Services Kit（基础服务） | @ohos.deviceInfo (设备信息) |
| Basic Services Kit（基础服务） | @ohos.power (系统电源管理) |
| Basic Services Kit（基础服务） | @ohos.request (上传下载) |
| Basic Services Kit（基础服务） | @ohos.runningLock (RunningLock锁) |
| Basic Services Kit（基础服务） | @ohos.settings (设置数据项名称) |
| Basic Services Kit（基础服务） | @ohos.systemTime (系统时间、时区) |
| Basic Services Kit（基础服务） | @ohos.wallpaper (壁纸) |
| Connectivity Kit（短距通信服务） | @ohos.bluetooth (蓝牙) |
| Connectivity Kit（短距通信服务） | @ohos.bluetoothManager (蓝牙) |
| Connectivity Kit（短距通信服务） | @ohos.connectedTag (有源标签) |
| Connectivity Kit（短距通信服务） | @ohos.nfc.cardEmulation (标准NFC-cardEmulation) |
| Connectivity Kit（短距通信服务） | @ohos.nfc.controller (标准NFC) |
| Connectivity Kit（短距通信服务） | @ohos.nfc.tag (标准NFC-Tag) |
| Connectivity Kit（短距通信服务） | @ohos.wifi (WLAN) |
| Connectivity Kit（短距通信服务） | @ohos.wifiext (WLAN扩展接口) |
| Connectivity Kit（短距通信服务） | @ohos.wifiManager (WLAN) |
| Connectivity Kit（短距通信服务） | @ohos.wifiManagerExt (WLAN扩展接口) |
| Contacts Kit（联系人服务） | @ohos.contact (联系人) |
| Core File Kit（文件基础服务） | @ohos.file.storageStatistics (应用空间统计) |
| Form Kit（卡片开发服务） | @ohos.application.formError (formError) |
| IME Kit（输入法开发服务） | @ohos.inputMethod (输入法框架) |
| Location Kit | @ohos.geolocation (位置服务) |
| Location Kit | @ohos.geoLocationManager (位置服务) |
| MDM Kit（企业设备管理服务） | @ohos.enterprise.adminManager（admin权限管理） |
| MDM Kit（企业设备管理服务） | @ohos.enterprise.deviceInfo（设备信息管理） |
| MultimediaKit | @ohos.multimedia.mediaLibrary (媒体库管理) |
| Network Kit（网络服务） | @ohos.net.connection (网络连接管理) |
| Network Kit（网络服务） | @ohos.net.ethernet (以太网连接管理) |
| Network Kit（网络服务） | @ohos.net.http (数据请求) |
| Network Kit（网络服务） | @ohos.net.sharing (网络共享管理) |
| Network Kit（网络服务） | @ohos.net.socket (Socket连接) |
| Network Kit（网络服务） | @ohos.net.webSocket (WebSocket连接) |
| Notification Kit（用户通知服务） | @ohos.notification (Notification模块) |
| Notification Kit（用户通知服务） | @ohos.notificationManager (NotificationManager模块) |
| Performance Analysis Kit（性能分析服务） | @ohos.hidebug (Debug调试) |
| Sensor Service Kit（传感器服务） | @ohos.sensor (传感器) |
| Sensor Service Kit（传感器服务） | @ohos.vibrator (振动) |
| Telephony Kit（蜂窝通信服务） | @ohos.telephony.call (拨打电话) |
| Telephony Kit（蜂窝通信服务） | @ohos.telephony.data (蜂窝数据) |
| Telephony Kit（蜂窝通信服务） | @ohos.telephony.observer (observer) |
| Telephony Kit（蜂窝通信服务） | @ohos.telephony.radio (网络搜索) |
| Telephony Kit（蜂窝通信服务） | @ohos.telephony.sim (SIM卡管理) |
| Telephony Kit（蜂窝通信服务） | @ohos.telephony.sms (短信服务) |
