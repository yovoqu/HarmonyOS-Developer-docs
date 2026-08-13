# LiveViewLockScreenExtensionAbility

更新时间：2026-08-03 11:34:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/liveview-lock-screen-ability
**支持设备：** Phone | PC/2in1 | Tablet

LiveViewLockScreenExtensionAbility为[锁屏沉浸实况窗](https://developer.huawei.com/consumer/cn/doc/design-guides/system-features-live-view-0000001955186861#section553375320)可视化区的[ExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/extensionability-overview)组件，继承自[UIExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiextensionability)，适用于需要在锁屏状态下展示丰富内容的实时活动场景。开发者通过继承该类并实现应用的扩展组件，可以在用户未解锁屏幕的情况下，在锁屏界面以可视化形式呈现更多的数据情况以及提供更多快速操作。
 
**起始版本：** 5.0.0(12)
  

#### 约束限制

**支持设备：** Phone | PC/2in1 | Tablet

- LiveViewLockScreenExtensionAbility为独立子进程，不能跨进程拉起其他Ability。
- 为保障系统安全性和稳定性，防止LiveViewLockScreenExtensionAbility滥用系统资源，系统对其能力进行管控，不支持部分模块的引用，详情请参考[附录](#附录)。

 
  

#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet

```text
import { LiveViewLockScreenExtensionAbility } from '@kit.LiveViewKit';
```
 
**设备行为差异：** 该模块在Phone、Tablet中可正常调用，在其他设备类型中无效果。
 
  

#### LiveViewLockScreenExtensionAbility

**支持设备：** Phone | PC/2in1 | Tablet

锁屏沉浸实况窗扩展Ability，继承自[UIExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiextensionability)。
 
**模型约束：** 属性仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.LiveView.LiveViewService
 
**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。
 
**起始版本：** 5.0.0(12)
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | LiveViewLockScreenExtensionContext | 否 | 否 | LiveViewLockScreenExtensionAbility的上下文环境，继承自ExtensionContext。 |
 
 
  

#### 示例

**支持设备：** Phone | PC/2in1 | Tablet

```text
import { LiveViewLockScreenExtensionAbility } from '@kit.LiveViewKit';
import { UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class LiveViewLockScreenExtAbility extends LiveViewLockScreenExtensionAbility {
  onCreate(): void {
    hilog.info(0x0000, 'LiveViewLockScreenTag', 'LiveViewLockScreenExtAbility onCreate begin.');
  }

  onSessionCreate(want: Want, session: UIExtensionContentSession): void {
    hilog.info(0x0000, 'LiveViewLockScreenTag', 'LiveViewLockScreenExtAbility onSessionCreate begin.');
    let param: Record<string, UIExtensionContentSession> = {
      'session': session
    };
    let storage: LocalStorage = new LocalStorage(param);

    // 解析从liveViewLocalScreenAbilityParameters中传入的参数
    const parameters = want?.parameters;
    let words: string = parameters?.['words'] ? parameters?.['words'] as string : 'Hello World!';
    storage.setOrCreate('words', words);

    // 加载锁屏沉浸实况窗页面
    session.loadContent('pages/LiveViewLockScreenPage', storage);
  }
}
```
 
  

#### 附录

**支持设备：** Phone | PC/2in1 | Tablet

LiveViewLockScreenExtensionAbility不允许调用的API名单如下。
  
| Kit名称 | 模块名称 |
| --- | --- |
| Ability Kit | @ohos.ability.featureAbility (FeatureAbility模块) @ohos.ability.particleAbility (ParticleAbility模块) @ohos.bundle.launcherBundleManager (launcherBundleManager模块) @ohos.continuation.continuationManager (流转/协同管理) |
| AppGallery Kit | privacyManager（隐私管理服务） |
| ArkData | @ohos.data.distributedData (分布式数据管理) @ohos.data.distributedDataObject (分布式数据对象) @ohos.data.distributedKVStore (分布式键值数据库) |
| ArkUI | @ohos.window (窗口) |
| Audio Kit | @ohos.multimedia.audio (音频管理) |
| AVSession Kit | @ohos.multimedia.avsession (媒体会话管理) @ohos.multimedia.avCastPicker (投播组件) |
| Background Tasks Kit | @ohos.backgroundTaskManager (后台任务管理) @ohos.resourceschedule.backgroundTaskManager (后台任务管理) @ohos.reminderAgent (后台代理提醒) @ohos.reminderAgentManager (后台代理提醒) |
| Basic Services Kit | @ohos.account.appAccount (应用账号管理) @ohos.account.distributedAccount (分布式账号管理) @ohos.account.osAccount (系统账号管理) @ohos.request (上传下载) @ohos.wallpaper (壁纸) @ohos.pasteboard (剪贴板) |
| Calendar Kit | @ohos.calendarManager (日程管理能力) |
| Camera Kit | @ohos.multimedia.camera (相机管理) @ohos.multimedia.cameraPicker (相机选择器) |
| Connectivity Kit | @ohos.connectedTag (有源标签) @ohos.nfc.cardEmulation (标准NFC-cardEmulation) @ohos.nfc.controller (标准NFC) @ohos.nfc.tag (标准NFC-Tag) nfctech (标准NFC-Tag Nfc 技术) tagSession (标准NFC-Tag TagSession) |
| Contacts Kit | @ohos.contact (联系人) |
| Core File Kit | @ohos.file.picker (选择器) |
| Form Kit | @ohos.app.form.formInfo (formInfo) @ohos.application.formError (formError) |
| Map Kit | sceneMap（场景化控件） |
| MDM Kit | @ohos.enterprise.adminManager (admin权限管理) @ohos.enterprise.deviceInfo（设备信息管理） |
| Media Kit | @ohos.multimedia.media (媒体服务) |
| Media Library Kit | @ohos.file.sendablePhotoAccessHelper (基于Sendable对象的相册管理模块) @ohos.file.AlbumPickerComponent (Album Picker组件) @ohos.file.PhotoPickerComponent (PhotoPicker组件) @ohos.file.RecentPhotoComponent (最近图片组件) @ohos.multimedia.movingphotoview (动态照片) @ohos.file.photoAccessHelper (相册管理模块) |
| Notification Kit | @ohos.notification (Notification模块) @ohos.notificationManager (NotificationManager模块) |
| Payment Kit | paymentService (鸿蒙支付服务) |
| Performance Analysis Kit | @ohos.hidebug (Debug调试) |
| Scan Kit | customScan (自定义界面扫码) detectBarcode (图像识码) generateBarcode (码图生成) scanBarcode (默认界面扫码) scanCore (扫码公共信息) |
| Sensor Service Kit | @ohos.vibrator (振动) |
| Service Collaboration Kit | devicePicker (设备选择控制器) CollaborationDevicePicker (流转控件) |
| Share Kit | systemShare（分享） harmonyShare（华为分享） |
| Telephony Kit | @ohos.telephony.call (拨打电话) @ohos.telephony.data (蜂窝数据) @ohos.telephony.observer (observer) @ohos.telephony.radio (网络搜索) @ohos.telephony.sim (SIM卡管理) @ohos.telephony.sms (短信服务) |
| User Authentication Kit | @ohos.userIAM.userAuth (用户认证) |
| Vision Kit | CardRecognition（卡证识别控件） DocumentScanner（文档扫描控件） |
