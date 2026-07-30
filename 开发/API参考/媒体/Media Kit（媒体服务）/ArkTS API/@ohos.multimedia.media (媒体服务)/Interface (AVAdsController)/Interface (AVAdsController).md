# Interface (AVAdsController)

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avadscontroller
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

广告内容控制接口，用于管理广告播放控制器中的广告资源及监听广告事件。通过[createAVAdsController()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-f#mediacreateavadscontroller)创建实例。
 
> [!NOTE]
> 本Interface首批接口从API版本26.0.0开始支持。

  

#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { media } from '@kit.MediaKit';
```
 
  

#### addAdsMediaSource

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

addAdsMediaSource(src: MediaSource, start: number): Promise&lt;string&gt;
 
向广告控制器添加一个广告影片源，可以指定插入时间（即广告在主媒体资源播放进度中的插入位置）。使用Promise异步回调。
 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.Multimedia.Media.AVPlayer
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | MediaSource | 是 | 要插入到主内容中播放的视频源。 |
| start | number | 是 | 广告数据在主媒体资源播放进度中的插入位置。 单位：毫秒。 取值限定为非负整数。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回添加到广告控制器中的媒体源ID。 |
 
 
**错误码：**
 
以下错误码的详细介绍请参见[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 5400108 | Insert a media asset whose start value exceeds the value of the main content. |
 
 
**示例：**
 
```text
async function test() {
  let player: media.AVPlayer = await media.createAVPlayer();
  let adsController: media.AVAdsController | undefined = await media.createAVAdsController(player);
  if (adsController) {
    let headers: Record<string, string> = {"User-Agent" : "MyApp/1.0"};
    let mediaSource: media.MediaSource = media.createMediaSourceWithUrl("http://example.com/ad.mp4", headers);
    let adsId: string = await adsController.addAdsMediaSource(mediaSource, 5000);
    console.info(`Succeeded in adding ads media source, adsId: ${adsId}`);
  }
}
```
 
  

#### removeAdsMediaSource

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

removeAdsMediaSource(id: string): void
 
移除广告控制器中指定的广告源。
 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.Multimedia.Media.AVPlayer
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | addAdsMediaSource接口的返回值。 |
 
 
**错误码：**
 
以下错误码的详细介绍请参见[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 5400108 | If the specified ID is not in the AdsController. |
 
 
**示例：**
 
```text
async function test() {
  let player: media.AVPlayer = await media.createAVPlayer();
  let adsController: media.AVAdsController | undefined = await media.createAVAdsController(player);
  if (adsController) {
    let headers: Record<string, string> = {"User-Agent" : "MyApp/1.0"};
    let mediaSource: media.MediaSource = media.createMediaSourceWithUrl("http://example.com/ad.mp4", headers);
    let adsId: string = await adsController.addAdsMediaSource(mediaSource, 5000);
    adsController.removeAdsMediaSource(adsId);
  }
}
```
 
  

#### skipCurrentAdsMediaSource

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

skipCurrentAdsMediaSource(): void
 
跳过当前正在播放的广告内容。
 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.Multimedia.Media.AVPlayer
 
**示例：**
 
```text
async function test() {
  let player: media.AVPlayer = await media.createAVPlayer();
  let adsController: media.AVAdsController | undefined = await media.createAVAdsController(player);
  if (adsController) {
    adsController.skipCurrentAdsMediaSource();
  }
}
```
 
  

#### disableAllAdsMediaSource

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

disableAllAdsMediaSource(): void
 
禁用当前会话中剩余的广告内容播放。
 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.Multimedia.Media.AVPlayer
 
**示例：**
 
```text
async function test() {
  let player: media.AVPlayer = await media.createAVPlayer();
  let adsController: media.AVAdsController | undefined = await media.createAVAdsController(player);
  if (adsController) {
    adsController.disableAllAdsMediaSource();
  }
}
```
 
  

#### release

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

release(): void
 
释放AVAdsController对象。
 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.Multimedia.Media.AVPlayer
 
**示例：**
 
```text
async function test() {
  let player: media.AVPlayer = await media.createAVPlayer();
  let adsController: media.AVAdsController | undefined = await media.createAVAdsController(player);
  if (adsController) {
    adsController.release();
  }
}
```
 
  

#### onAdsEventListenerLoadingError

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onAdsEventListenerLoadingError(callback: OnAdsEventLoadingErrorHandle): void
 
注册广告内容加载失败时的事件处理函数。
 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.Multimedia.Media.AVPlayer
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | OnAdsEventLoadingErrorHandle | 是 | 广告内容加载失败的处理函数。由使用方实现。 第一个参数用于传递广告ID，第二个参数用于传递失败原因。 |
 
 
**示例：**
 
```text
async function test() {
  let player: media.AVPlayer = await media.createAVPlayer();
  let adsController: media.AVAdsController | undefined = await media.createAVAdsController(player);
  if (adsController) {
    adsController.onAdsEventListenerLoadingError((adsId: string, reason: BusinessError) => {
      console.error(`Ads loading failed, adsId: ${adsId}, reason: ${reason.message}`);
    });
  }
}
```
 
  

#### onAdsListenerAdsStarted

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onAdsListenerAdsStarted(callback: OnAdsEventAdsStartedHandle): void
 
注册新广告内容播放时触发的事件处理函数。
 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.Multimedia.Media.AVPlayer
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | OnAdsEventAdsStartedHandle | 是 | 广告内容开始播放时的处理函数。常用于切换播放页面的逻辑。 第一个参数表示正在播放的广告ID，第二个参数表示广告的时长。 |
 
 
**示例：**
 
```text
async function test() {
  let player: media.AVPlayer = await media.createAVPlayer();
  let adsController: media.AVAdsController | undefined = await media.createAVAdsController(player);
  if (adsController) {
    adsController.onAdsListenerAdsStarted((adsId: string, duration: number) => {
      console.info(`Ads started, adsId: ${adsId}, duration: ${duration}ms`);
    });
  }
}
```
 
  

#### onAdsListenerAdsSkipped

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onAdsListenerAdsSkipped(callback: Callback&lt;string&gt;): void
 
注册广告被跳过时触发的事件处理函数。
 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.Multimedia.Media.AVPlayer
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;string&gt; | 是 | 广告跳过的处理函数。参数为被跳过的广告ID。 |
 
 
**示例：**
 
```text
async function test() {
  let player: media.AVPlayer = await media.createAVPlayer();
  let adsController: media.AVAdsController | undefined = await media.createAVAdsController(player);
  if (adsController) {
    adsController.onAdsListenerAdsSkipped((adsId: string) => {
      console.info(`Ads skipped, adsId: ${adsId}`);
    });
  }
}
```
 
  

#### onAdsListenerAdsCompleted

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onAdsListenerAdsCompleted(callback: Callback&lt;string&gt;): void
 
注册广告内容播放完成时触发的事件处理函数。
 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.Multimedia.Media.AVPlayer
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;string&gt; | 是 | 广告播放完成的处理函数。参数为播放完成的广告ID。 |
 
 
**示例：**
 
```text
async function test() {
  let player: media.AVPlayer = await media.createAVPlayer();
  let adsController: media.AVAdsController | undefined = await media.createAVAdsController(player);
  if (adsController) {
    adsController.onAdsListenerAdsCompleted((adsId: string) => {
      console.info(`Ads completed, adsId: ${adsId}`);
    });
  }
}
```
 
  

#### offAdsEventListenerLoadingError

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

offAdsEventListenerLoadingError(callback?: OnAdsEventLoadingErrorHandle): void
 
取消注册广告内容加载失败时的事件处理函数。
 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.Multimedia.Media.AVPlayer
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | OnAdsEventLoadingErrorHandle | 否 | 广告内容加载失败的处理函数。 默认值为取消订阅该事件的所有回调函数。 |
 
 
**示例：**
 
```text
async function test() {
  let player: media.AVPlayer = await media.createAVPlayer();
  let adsController: media.AVAdsController | undefined = await media.createAVAdsController(player);
  if (adsController) {
    adsController.offAdsEventListenerLoadingError();
  }
}
```
 
  

#### offAdsListenerAdsStarted

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

offAdsListenerAdsStarted(callback?: OnAdsEventAdsStartedHandle): void
 
取消注册新广告内容播放时触发的事件处理函数。
 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.Multimedia.Media.AVPlayer
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | OnAdsEventAdsStartedHandle | 否 | 广告内容开始播放时的处理函数。常用于切换播放页面的逻辑。 默认值为取消订阅该事件的所有回调函数。 |
 
 
**示例：**
 
```text
async function test() {
  let player: media.AVPlayer = await media.createAVPlayer();
  let adsController: media.AVAdsController | undefined = await media.createAVAdsController(player);
  if (adsController) {
    adsController.offAdsListenerAdsStarted();
  }
}
```
 
  

#### offAdsListenerAdsSkipped

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

offAdsListenerAdsSkipped(callback?: Callback&lt;string&gt;): void
 
取消注册广告被跳过时触发的事件处理函数。
 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.Multimedia.Media.AVPlayer
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;string&gt; | 否 | 广告跳过的处理函数。 默认值为取消订阅该事件的所有回调函数。 |
 
 
**示例：**
 
```text
async function test() {
  let player: media.AVPlayer = await media.createAVPlayer();
  let adsController: media.AVAdsController | undefined = await media.createAVAdsController(player);
  if (adsController) {
    adsController.offAdsListenerAdsSkipped();
  }
}
```
 
  

#### offAdsListenerAdsCompleted

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

offAdsListenerAdsCompleted(callback?: Callback&lt;string&gt;): void
 
取消注册广告内容播放完成时触发的事件处理函数。
 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.Multimedia.Media.AVPlayer
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;string&gt; | 否 | 广告播放完成的处理函数。 默认值为取消订阅该事件的所有回调函数。 |
 
 
**示例：**
 
```text
async function test() {
  let player: media.AVPlayer = await media.createAVPlayer();
  let adsController: media.AVAdsController | undefined = await media.createAVAdsController(player);
  if (adsController) {
    adsController.offAdsListenerAdsCompleted();
  }
}
```
