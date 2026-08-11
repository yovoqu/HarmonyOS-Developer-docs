# LiveViewCardExtensionAbility

更新时间：2026-08-03 11:34:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/liveview-card-ability
**支持设备：** Phone | PC/2in1 | Tablet

LiveViewCardExtensionAbility为实况窗卡片自定义扩展区的[ExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/extensionability-overview)组件，适用于需要在扩展区展示自定义丰富内容的实时活动场景。开发者通过继承该类并实现应用的扩展组件，可以在实况窗扩展区呈现开发者自定义的内容。
 
**起始版本：** 26.0.0
  

#### 约束限制

**支持设备：** Phone | PC/2in1 | Tablet

- LiveViewCardExtensionAbility为独立子进程，不能跨进程拉起其他Ability。
- 不允许访问网络。
- 该ExtensionAbility每次的运行时长限制在80毫秒内，超时会导致实况卡片自定义扩展区无法正常展示，因此禁止用于复杂耗时的处理。
- 为保障系统安全性和稳定性，防止LiveViewCardExtensionAbility滥用系统资源，系统对其能力进行管控，不支持部分模块的引用，详情请参考[附录](#附录)。

 
  

#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet

```text
import { LiveViewCardExtensionAbility } from '@kit.LiveViewKit';
```
 
**设备行为差异：** 该模块在Phone、Tablet中可正常调用，在其他设备类型中无效果。
 
  

#### LiveViewCardExtensionAbility

**支持设备：** Phone | PC/2in1 | Tablet

**模型约束：** 属性仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.LiveView.LiveViewService
 
**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。
 
**起始版本：** 26.0.0
 
  

#### 属性
 
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | LiveViewCardExtensionContext | 否 | 否 | LiveViewCardExtensionAbility的上下文环境，继承自ExtensionContext。 |
 
 
  

#### onRender

**支持设备：** Phone | PC/2in1 | Tablet

onRender(param: Record<string, string>): CardInfo
 
开发者继承LiveViewCardExtensionAbility并实现自身的组件，当组件实例被系统加载时，系统会触发该回调。开发者可以在onRender中实现实况窗卡片扩展区的业务逻辑和界面组件绘制，并返回要加载的[CardInfo](#cardinfo)给系统，由系统渲染页面。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.LiveView.LiveViewService
 
**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | Record<string, string> | 是 | 开发者创建实况窗卡片自定义扩展区时传入的参数CustomLayout.abilityParameters 默认会携带以下key值（由系统赋值，开发者手动修改也不会生效）： 'ohos.extra.param.key.colorMode'：实况卡片深浅色模式（dark：深色模式；light：浅色模式） 'ohos.extra.param.key.fontColor'：实况卡片字体颜色（"#ARGB"16进制格式，长度为9） 'ohos.extra.param.key.contentWidth'：实况窗卡片自定义扩展区的宽度（单位为vp；自定义扩展区左右边界距离实况窗卡片边界各为12vp）。 |
 
 
  

#### CardInfo

**支持设备：** Phone | PC/2in1 | Tablet

onRender函数接口返回的卡片渲染信息对象。
 
**模型约束：** 此属性仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.LiveView.LiveViewService
 
**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。
 
**起始版本：** 26.0.0
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pagePath | string | 否 | 否 | 待加载到系统中的扩展区域页面的路径，系统将渲染该页面。 |
| storage | LocalStorage | 否 | 是 | 页面级UI状态存储单元，用于传递pagePath内容的状态属性。 |
 
 
  

#### 示例

**支持设备：** Phone | PC/2in1 | Tablet

```text
import { LiveViewCardExtensionAbility } from '@kit.LiveViewKit';
import { CardInfo } from '@hms.core.liveview.LiveViewCardExtensionAbility';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class LiveViewCardExtAbility extends LiveViewCardExtensionAbility {
  onRender(param: Record<string, string>): CardInfo {
    hilog.info(0x0000, 'LiveViewCardTag', 'LiveViewCardExtAbility onRender begin.');
    
    // 将param的参数构造到LocalStorage传递给页面使用。
    const storage = new LocalStorage(param);
      
    // 加载实况窗卡片自定义扩展区页面
    return {
        pagePath: 'pages/LiveViewCardPage',
        storage: storage
    }
  }
}
```
 
```text
@Entry({ useSharedStorage: true })
@Component
struct LiveViewCardPage {
  private storage: LocalStorage | undefined = this.getUIContext().getSharedLocalStorage();
  // 获取从AbilityParameters中传入的参数
  private words: string | undefined = this.storage?.get('words');

  // 解析获取系统实况窗卡片自定义扩展区的宽度、深浅色模式、字体颜色
  private contentWidth: string | undefined = this.storage?.get('ohos.extra.param.key.contentWidth');
  private colorMode: string | undefined = this.storage?.get('ohos.extra.param.key.colorMode');
  private fontColor: string | undefined = this.storage?.get('ohos.extra.param.key.fontColor');

  build() {
    Column() {
      Scroll() {
        Column() {
          Text(this.words)
            .fontColor(this.fontColor)
        }
        .width(this.contentWidth)
      }
    }
  }
}
```
 
  

#### 附录

**支持设备：** Phone | PC/2in1 | Tablet

LiveViewCardExtensionAbility不允许调用的API名单如下。
  
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
| Call Service Kit | voipCall (应用内通话管理) |
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
