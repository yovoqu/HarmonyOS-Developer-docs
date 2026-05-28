# Interface (AVSessionController)

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-avsessioncontroller
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

AVSessionController控制器可查看会话ID，并可完成对会话发送命令及事件，获取会话元数据，播放状态信息等操作。

> [!NOTE]
> 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 本Interface首批接口从API version 10开始支持。



#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { avSession } from '@kit.AVSessionKit';
import { BusinessError } from '@kit.BasicServicesKit';
```



#### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sessionId10+ | string | 是 | 否 | AVSessionController对象唯一的会话标识。 |


**示例：**

```ArkTS
// Index.ets
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  private tag: string = "createNewSession";
  private sessionId: string = "";
  private AVSessionController?: avSession.AVSessionController;
  private currentAVSession?: avSession.AVSession;
  context = this.getUIContext();

  aboutToAppear(): void {

    avSession.createAVSession(this.getUIContext().getHostContext(), this.tag, "audio").then(async (data: avSession.AVSession) => {
      this.currentAVSession = data;
      this.sessionId = this.currentAVSession.sessionId;
      this.avsessionController = await this.currentAVSession.getController();
      console.info(`Succeeded in creating AV session, sessionId: ${this.sessionId}`);
    });
  }

  build() {
    Column() {
      Text('AVSession Demo')
        .fontSize(20)
        .margin(10)
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```



#### getAVPlaybackState10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getAVPlaybackState(callback: AsyncCallback&lt;AVPlaybackState&gt;): void

获取当前的远端播放状态。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;AVPlaybackState&gt; | 是 | 回调函数，返回远端播放状态。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.getAVPlaybackState((err: BusinessError, state: avSession.AVPlaybackState) => {
  if (err) {
    console.error(`Failed to get AV playback state, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in getting AV playback state.');
});
```



#### getAVPlaybackState10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getAVPlaybackState(): Promise&lt;AVPlaybackState&gt;

获取当前的远端播放状态。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;AVPlaybackState&gt; | Promise对象,返回远端播放状态。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.getAVPlaybackState().then((state: avSession.AVPlaybackState) => {
  console.info('Succeeded in getting AV playback state.');
});
```



#### getAVMetadata10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getAVMetadata(): Promise&lt;AVMetadata&gt;

获取会话元数据。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;AVMetadata&gt; | Promise对象，返回会话元数据。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.getAVMetadata().then((metadata: avSession.AVMetadata) => {
  console.info(`Succeeded in getting AV metadata, assetId: ${metadata.assetId}`);
});
```



#### getAVMetadata10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getAVMetadata(callback: AsyncCallback&lt;AVMetadata&gt;): void

获取会话元数据。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;AVMetadata&gt; | 是 | 回调函数，返回会话元数据。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.getAVMetadata((err: BusinessError, metadata: avSession.AVMetadata) => {
  if (err) {
    console.error(`Failed to get AV metadata, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting AV metadata, assetId: ${metadata.assetId}`);
});
```



#### getAVQueueTitle10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getAVQueueTitle(): Promise&lt;string&gt;

获取当前会话播放列表的名称。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise对象。返回播放列表名称。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.getAVQueueTitle().then((title: string) => {
  console.info(`Succeeded in getting AV queue title: ${title}`);
});
```



#### getAVQueueTitle10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getAVQueueTitle(callback: AsyncCallback&lt;string&gt;): void

获取当前播放列表的名称。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;string&gt; | 是 | 回调函数，返回播放列表名称。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.getAVQueueTitle((err: BusinessError, title: string) => {
  if (err) {
    console.error(`Failed to get AV queue title, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting AV queue title: ${title}`);
});
```



#### getAVQueueItems10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getAVQueueItems(): Promise<Array&lt;AVQueueItem&gt;>

获取当前会话播放列表相关信息。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array&lt;AVQueueItem&gt;> | Promise对象。返回播放列表队列。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.getAVQueueItems().then((items: avSession.AVQueueItem[]) => {
  console.info(`Succeeded in getting AV queue items, length: ${items.length}`);
});
```



#### getAVQueueItems10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getAVQueueItems(callback: AsyncCallback<Array&lt;AVQueueItem&gt;>): void

获取当前播放列表相关信息。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array&lt;AVQueueItem&gt;> | 是 | 回调函数，返回播放列表队列。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.getAVQueueItems((err: BusinessError, items: avSession.AVQueueItem[]) => {
  if (err) {
    console.error(`Failed to get AV queue items, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting AV queue items, length: ${items.length}`);
});
```



#### skipToQueueItem10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

skipToQueueItem(itemId: number): Promise&lt;void&gt;

设置指定播放列表单项的ID，发送给session端处理，session端可以选择对这个单项歌曲进行播放。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| itemId | number | 是 | 播放列表单项的ID值，用以表示选中的播放列表单项。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。当播放列表单项ID设置成功，无返回结果，否则返回错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
let queueItemId = 0;
avcontroller.skipToQueueItem(queueItemId).then(() => {
  console.info('Succeeded in skipping to queue item.');
});
```



#### skipToQueueItem10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

skipToQueueItem(itemId: number, callback: AsyncCallback&lt;void&gt;): void

设置指定播放列表单项的ID，发送给session端处理，session端可以选择对这个单项歌曲进行播放。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| itemId | number | 是 | 播放列表单项的ID值，用以表示选中的播放列表单项。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当播放状态设置成功，err为undefined，否则返回错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
let queueItemId = 0;
avcontroller.skipToQueueItem(queueItemId, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to skip to queue item, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in skipping to queue item.');
});
```



#### getOutputDevice10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getOutputDevice(): Promise&lt;OutputDeviceInfo&gt;

获取播放设备信息。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;OutputDeviceInfo&gt; | Promise对象，返回播放设备信息。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 600101 | Session service exception. |
| 600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.getOutputDevice().then((deviceInfo: avSession.OutputDeviceInfo) => {
  console.info('Succeeded in getting output device.');
});
```



#### getOutputDevice10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getOutputDevice(callback: AsyncCallback&lt;OutputDeviceInfo&gt;): void

获取播放设备信息。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;OutputDeviceInfo&gt; | 是 | 回调函数，返回播放设备信息。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 600101 | Session service exception. |
| 600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.getOutputDevice((err: BusinessError, deviceInfo: avSession.OutputDeviceInfo) => {
  if (err) {
    console.error(`Failed to get output device, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in getting output device.');
});
```



#### sendAVKeyEvent10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

sendAVKeyEvent(event: KeyEvent): Promise&lt;void&gt;

发送按键事件到控制器对应的会话。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | KeyEvent | 是 | 按键事件。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 600101 | Session service exception. |
| 600102 | The session does not exist. |
| 600103 | The session controller does not exist. |
| 600105 | Invalid session command. |
| 600106 | The session is not activated. |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。当事件发送成功，无返回结果，否则返回错误对象。 |


**示例：**

```text
import { Key, KeyEvent } from '@kit.InputKit';

let keyItem: Key = {code:0x49, pressedTime:2, deviceId:0};
let event:KeyEvent = {id:1, deviceId:0, actionTime:1, screenId:1, windowId:1, action:2, key:keyItem, unicodeChar:0, keys:[keyItem], ctrlKey:false, altKey:false, shiftKey:false, logoKey:false, fnKey:false, capsLock:false, numLock:false, scrollLock:false};

avcontroller.sendAVKeyEvent(event).then(() => {
  console.info('Succeeded in sending AV key event.');
});
```



#### sendAVKeyEvent10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

sendAVKeyEvent(event: KeyEvent, callback: AsyncCallback&lt;void&gt;): void

发送按键事件到会话。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | KeyEvent | 是 | 按键事件。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当事件发送成功，err为undefined，否则返回错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 600101 | Session service exception. |
| 600102 | The session does not exist. |
| 600103 | The session controller does not exist. |
| 600105 | Invalid session command. |
| 600106 | The session is not activated. |


**示例：**

```text
import { Key, KeyEvent } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

let keyItem: Key = {code:0x49, pressedTime:2, deviceId:0};
let event:KeyEvent = {id:1, deviceId:0, actionTime:1, screenId:1, windowId:1, action:2, key:keyItem, unicodeChar:0, keys:[keyItem], ctrlKey:false, altKey:false, shiftKey:false, logoKey:false, fnKey:false, capsLock:false, numLock:false, scrollLock:false};
avcontroller.sendAVKeyEvent(event, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to send AV key event, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in sending AV key event.');
});
```



#### getLaunchAbility10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getLaunchAbility(): Promise&lt;WantAgent&gt;

获取应用在会话中保存的WantAgent对象。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;WantAgent&gt; | Promise对象，返回在setLaunchAbility保存的对象，包括应用的相关属性信息，如bundleName，abilityName，deviceId等。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.getLaunchAbility().then((agent: object) => {
  console.info(`Succeeded in getting launch ability: ${agent}`);
});
```



#### getLaunchAbility10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getLaunchAbility(callback: AsyncCallback&lt;WantAgent&gt;): void

获取应用在会话中保存的WantAgent对象。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;WantAgent&gt; | 是 | 回调函数。返回在setLaunchAbility保存的对象，包括应用的相关属性信息，如bundleName，abilityName，deviceId等。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.getLaunchAbility((err: BusinessError, agent: object) => {
  if (err) {
    console.error(`Failed to get launch ability, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting launch ability: ${agent}`);
});
```



#### getRealPlaybackPositionSync10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getRealPlaybackPositionSync(): number

获取当前播放位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 时间节点，毫秒数。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
let time: number = avcontroller.getRealPlaybackPositionSync();
```



#### isActive10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isActive(): Promise&lt;boolean&gt;

获取会话是否被激活。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象，返回会话是否为激活状态，true表示被激活，false表示禁用。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.isActive().then((isActive: boolean) => {
  console.info(`Succeeded in checking active state: ${isActive}`);
});
```



#### isActive10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isActive(callback: AsyncCallback&lt;boolean&gt;): void

判断会话是否被激活。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;boolean&gt; | 是 | 回调函数。返回会话是否为激活状态，true表示被激活，false表示禁用。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.isActive((err: BusinessError, isActive: boolean) => {
  if (err) {
    console.error(`Failed to check active state, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in checking active state: ${isActive}`);
});
```



#### destroy10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

destroy(): Promise&lt;void&gt;

销毁当前控制器，销毁后当前控制器不可再用。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。当控制器销毁成功，无返回结果，否则返回错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.destroy().then(() => {
  console.info('Succeeded in destroying.');
});
```



#### destroy10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

destroy(callback: AsyncCallback&lt;void&gt;): void

销毁当前控制器，销毁后当前控制器不可再用。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当控制器销毁成功，err为undefined，否则返回错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.destroy((err: BusinessError) => {
  if (err) {
    console.error(`Failed to destroy controller, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in destroying.');
});
```



#### getValidCommands10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getValidCommands(): Promise<Array&lt;AVControlCommandType&gt;>

获取会话支持的有效命令。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array&lt;AVControlCommandType&gt;> | Promise对象。返回有效命令的集合。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.getValidCommands().then((validCommands: avSession.AVControlCommandType[]) => {
  console.info(`Succeeded in getting valid commands, size: ${validCommands.length}`);
});
```



#### getValidCommands10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getValidCommands(callback: AsyncCallback<Array&lt;AVControlCommandType&gt;>): void

获取会话支持的有效命令。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array&lt;AVControlCommandType&gt;> | 是 | 回调函数，返回有效命令的集合。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.getValidCommands((err: BusinessError, validCommands: avSession.AVControlCommandType[]) => {
  if (err) {
    console.error(`Failed to get valid commands, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting valid commands, size: ${validCommands.length}`);
});
```



#### sendControlCommand10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

sendControlCommand(command: AVControlCommand): Promise&lt;void&gt;

通过控制器发送命令到其对应的会话。结果通过Promise异步回调方式返回。

> [!NOTE]
> 媒体控制方在使用sendControlCommand命令前，需要确保控制对应的媒体会话注册了对应的监听，注册媒体会话相关监听的方法请参见接口 on('play') 、 on('pause') 等。


**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| command | AVControlCommand | 是 | 会话的相关命令和命令相关参数。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。当命令发送成功，无返回结果，否则返回错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600105 | Invalid session command. |
| 6600106 | The session is not activated. |
| 6600107 | Too many commands or events. |


**示例：**

```text
let avCommand: avSession.AVControlCommand = {command:'play'};
avcontroller.sendControlCommand(avCommand).then(() => {
  console.info('Succeeded in sending control command.');
});
```



#### sendControlCommand10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

sendControlCommand(command: AVControlCommand, callback: AsyncCallback&lt;void&gt;): void

通过会话控制器发送命令到其对应的会话。结果通过callback异步回调方式返回。

> [!NOTE]
> 媒体控制方在使用sendControlCommand命令前，需要确保控制对应的媒体会话注册了对应的监听，注册媒体会话相关监听的方法请参见接口 on('play') 、 on('pause') 等。


**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| command | AVControlCommand | 是 | 会话的相关命令和命令相关参数。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当命令发送成功，err为undefined，否则返回错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600105 | Invalid session command. |
| 6600106 | The session is not activated. |
| 6600107 | Too many commands or events. |


**示例：**

```text
let avCommand: avSession.AVControlCommand = {command:'play'};
avcontroller.sendControlCommand(avCommand, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to send control command, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in sending control command.');
});
```



#### sendCommonCommand10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

sendCommonCommand(command: string, args: {[key: string]: Object}): Promise&lt;void&gt;

通过会话控制器发送自定义控制命令到其对应的会话。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| command | string | 是 | 需要设置的自定义控制命令的名称。 |
| args | {[key: string]: Object} | 是 | 需要传递的控制命令键值对。 |


> [!NOTE]
> 参数args支持的数据类型有：字符串、数字、布尔、对象、数组和文件描述符等，详细介绍请参见 @ohos.app.ability.Want (Want) 。


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600105 | Invalid session command. |
| 6600106 | The session is not activated. |
| 6600107 | Too many commands or events. |


**示例：**

```text
let commandName = "my_command";
avcontroller.sendCommonCommand(commandName, {command : "This is my command"}).then(() => {
  console.info('Succeeded in sending common command.');
});
```



#### sendCommonCommand10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

sendCommonCommand(command: string, args: {[key: string]: Object}, callback: AsyncCallback&lt;void&gt;): void

通过会话控制器发送自定义命令到其对应的会话。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| command | string | 是 | 需要设置的自定义控制命令的名称。 |
| args | {[key: string]: Object} | 是 | 需要传递的控制命令键值对。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当命令发送成功，err为undefined，否则返回错误对象。 |


> [!NOTE]
> 参数args支持的数据类型有：字符串、数字、布尔、对象、数组和文件描述符等，详细介绍请参见 @ohos.app.ability.Want (Want) 。


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600105 | Invalid session command. |
| 6600106 | The session is not activated. |
| 6600107 | Too many commands or events. |


**示例：**

```text
let commandName = "my_command";
avcontroller.sendCommonCommand(commandName, {command : "This is my command"}, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to send common command, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in sending common command.');
})
```



#### sendCustomData20+

**支持设备：** Phone | PC/2in1 | Tablet | TV

sendCustomData(data: Record<string, Object>): Promise&lt;void&gt;

发送私有数据到远端设备。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | Record<string, Object> | 是 | 应用程序填充的自定义数据。服务端仅解析key为'customData'，且Object为string类型的对象。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception.You are advised to:1.Scheduled retry.2.Destroy the current session or session controller and re-create it. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |


**示例：**

```ArkTS
// Index.ets
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  private tag: string = "createNewSession";
  private sessionId: string = "";
  private controller: avSession.AVSessionController | undefined = undefined;
  private currentAVSession?: avSession.AVSession;
  context = this.getUIContext();

  aboutToAppear(): void {
    avSession.createAVSession(this.getUIContext().getHostContext(), this.tag, "audio")
      .then(async (data: avSession.AVSession) => {
        this.currentAVSession = data;
        this.sessionId = this.currentAVSession.sessionId;
        this.controller = await this.currentAVSession.getController();
        console.info(`Succeeded in creating AV session, sessionId: ${this.sessionId}`);
      });

    if (this.controller !== undefined) {
      (this.controller as avSession.AVSessionController).sendCustomData({ customData: "This is my data" })
    }
  }

  build() {
    Column() {
      Text('AVSession Demo')
        .fontSize(20)
        .margin(10)
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```



#### getExtras10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getExtras(): Promise<{[key: string]: Object}>

获取媒体提供方设置的自定义媒体数据包。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<{[key: string]: Object}> | Promise对象，返回媒体提供方设置的自定义媒体数据包，数据包的内容与setExtras设置的内容完全一致。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600105 | Invalid session command. |
| 6600107 | Too many commands or events. |


**示例：**

```ArkTS
// Index.ets
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  private tag: string = "createNewSession";
  private sessionId: string = "";
  private controller: avSession.AVSessionController | undefined = undefined;
  private currentAVSession?: avSession.AVSession;
  context = this.getUIContext();

  aboutToAppear(): void {

    avSession.createAVSession(this.getUIContext().getHostContext(), this.tag, "audio")
      .then(async (data: avSession.AVSession) => {
        this.currentAVSession = data;
        this.sessionId = this.currentAVSession.sessionId;
        this.controller = await this.currentAVSession.getController();
        console.info(`Succeeded in creating AV session, sessionId: ${this.sessionId}`);
      });
    if (this.controller !== undefined) {
      (this.controller as avSession.AVSessionController).getExtras().then((extras) => {
        console.info(`Succeeded in getting extras: ${extras}`);
      });
    }
  }

  build() {
    Column() {
      Text('AVSession Demo')
        .fontSize(20)
        .margin(10)
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```



#### getExtras10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getExtras(callback: AsyncCallback<{[key: string]: Object}>): void

获取媒体提供方设置的自定义媒体数据包。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<{[key: string]: Object}> | 是 | 回调函数，返回媒体提供方设置的自定义媒体数据包，数据包的内容与setExtras设置的内容完全一致。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600105 | Invalid session command. |
| 6600107 | Too many commands or events. |


**示例：**

```text
avcontroller.getExtras((err: BusinessError, extras) => {
  if (err) {
    console.error(`Failed to get extras, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting extras: ${extras}`);
});
```



#### getExtrasWithEvent18+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getExtrasWithEvent(extraEvent: string): Promise&lt;ExtraInfo&gt;

根据远端分布式事件类型，获取远端分布式媒体提供方设置的自定义媒体数据包。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| extraEvent | string | 是 | 远端分布式事件类型。可获取的事件类型来自于setExtras。 对Wearable设备类型，额外提供以下预设的事件类型： 'AUDIO_GET_VOLUME'：获取远端设备音量。 'AUDIO_GET_AVAILABLE_DEVICES'：获取远端所有可连接设备。 'AUDIO_GET_PREFERRED_OUTPUT_DEVICE_FOR_RENDERER_INFO'：获取远端实际发声设备。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;ExtraInfo&gt; | Promise对象，返回远端分布式媒体提供方设置的自定义媒体数据包。 参数ExtraInfo支持的数据类型有：字符串、数字、布尔、对象、数组和文件描述符等，详细介绍请参见@ohos.app.ability.Want (Want)。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600105 | Invalid session command. |


**示例：**

```text
let controller: avSession.AVSessionController | ESObject;
const COMMON_COMMAND_STRING_1 = 'AUDIO_GET_VOLUME';
const COMMON_COMMAND_STRING_2 = 'AUDIO_GET_AVAILABLE_DEVICES';
const COMMON_COMMAND_STRING_3 = 'AUDIO_GET_PREFERRED_OUTPUT_DEVICE_FOR_RENDERER_INFO';
if (controller !== undefined) {
  controller.getExtrasWithEvent(COMMON_COMMAND_STRING_1).then(() => {
    console.info(`${[COMMON_COMMAND_STRING_1]}`);
  })

  controller.getExtrasWithEvent(COMMON_COMMAND_STRING_2).then(() => {
    console.info(`${[COMMON_COMMAND_STRING_2]}`);
  })

  controller.getExtrasWithEvent(COMMON_COMMAND_STRING_3).then(() => {
    console.info(`${[COMMON_COMMAND_STRING_3]}`);
  })
}
```



#### isDesktopLyricEnabled23+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isDesktopLyricEnabled(): Promise&lt;boolean&gt;

查询是否启用桌面歌词功能。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回true表示启用桌面歌词功能；返回false表示不启用桌面歌词功能。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600111 | The desktop lyrics feature is not supported. |


```text
avcontroller.isDesktopLyricEnabled();
```



#### onDesktopLyricEnabled23+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onDesktopLyricEnabled(callback: Callback&lt;boolean&gt;): void

桌面歌词功能启用状态变更的监听事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;boolean&gt; | 是 | 回调函数。返回true表示桌面歌词功能启用；返回false表示桌面歌词功能未启用。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.onDesktopLyricEnabled((enabled: boolean) => {
  console.info(`desktop lyric enabled state : ${enabled}`);
})
```



#### offDesktopLyricEnabled23+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

offDesktopLyricEnabled(callback?: Callback&lt;boolean&gt;): void

取消桌面歌词启用状态变更事件监听，取消后将不再对该事件进行监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;boolean&gt; | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。 该参数为可选参数，若不填写该参数，则认为取消所有桌面歌词功能启用状态变更事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.offDesktopLyricEnabled();
```



#### setDesktopLyricVisible23+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setDesktopLyricVisible(visible: boolean): Promise&lt;void&gt;

设置当前会话桌面歌词的显示状态。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| visible | boolean | 是 | 是否显示桌面歌词。true表示显示；false表示不显示。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600110 | The desktop lyrics feature of this application is not enabled. |
| 6600111 | The desktop lyrics feature is not supported. |


**示例：**

```text
avcontroller.setDesktopLyricVisible(true);
```



#### isDesktopLyricVisible23+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isDesktopLyricVisible(): Promise&lt;boolean&gt;

查询当前会话桌面歌词的显示状态。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回true表示显示桌面歌词；返回false表示不显示桌面歌词。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600110 | The desktop lyrics feature of this application is not enabled. |
| 6600111 | The desktop lyrics feature is not supported. |


**示例：**

```text
avcontroller.isDesktopLyricVisible();
```



#### onDesktopLyricVisibilityChanged23+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onDesktopLyricVisibilityChanged(callback: Callback&lt;boolean&gt;): void

显示桌面歌词状态变更的监听事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;boolean&gt; | 是 | 回调函数。返回true表示开启显示桌面歌词状态；返回false表示关闭显示桌面歌词状态。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.onDesktopLyricVisibilityChanged((visible: boolean) => {
  console.info(`desktop lyric visible state: ${visible}`);
});
```



#### offDesktopLyricVisibilityChanged23+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

offDesktopLyricVisibilityChanged(callback?: Callback&lt;boolean&gt;): void

取消显示桌面歌词状态变更事件监听，取消后将不再对该事件进行监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;boolean&gt; | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。 该参数为可选参数，若不填写该参数，则认为取消所有显示桌面歌词状态变更事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.offDesktopLyricVisibilityChanged();
```



#### setDesktopLyricState23+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setDesktopLyricState(state: DesktopLyricState): Promise&lt;void&gt;

设置当前会话桌面歌词状态。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | DesktopLyricState | 是 | 桌面歌词状态。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600110 | The desktop lyrics feature of this application is not enabled. |
| 6600111 | The desktop lyrics feature is not supported. |


**示例：**

```text
let state: avSession.DesktopLyricState = {
  isLocked: true,
};
avcontroller.setDesktopLyricState(state);
```



#### getDesktopLyricState23+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getDesktopLyricState(): Promise&lt;DesktopLyricState&gt;

获取当前会话桌面歌词状态。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;DesktopLyricState&gt; | Promise对象。返回桌面歌词状态。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600110 | The desktop lyrics feature of this application is not enabled. |
| 6600111 | The desktop lyrics feature is not supported. |


**示例：**

```text
avcontroller.getDesktopLyricState();
```



#### onDesktopLyricStateChanged23+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onDesktopLyricStateChanged(callback: Callback&lt;DesktopLyricState&gt;): void

桌面歌词状态变更的监听事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;DesktopLyricState&gt; | 是 | 回调函数。返回桌面歌词状态。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.onDesktopLyricStateChanged((state: avSession.DesktopLyricState) => {
  console.info(`desktop lyric isLocked : ${state.isLocked}`);
})
```



#### offDesktopLyricStateChanged23+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

offDesktopLyricStateChanged(callback?: Callback&lt;DesktopLyricState&gt;): void

取消桌面歌词状态变更事件监听，取消后将不再对该事件进行监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;DesktopLyricState&gt; | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。 该参数为可选参数，若不填写该参数，则认为取消所有桌面歌词状态变更事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.offDesktopLyricStateChanged();
```



#### on('metadataChange')10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'metadataChange', filter: Array<keyof AVMetadata> | 'all', callback: (data: AVMetadata) => void)

设置元数据变化的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'metadataChange'：当元数据需要更新时，触发该事件。 需要更新表示对应属性值被重新设置过，不论新值与旧值是否相同。 |
| filter | Array<keyof AVMetadata>\|'all' | 是 | 'all'表示关注通话状态所有字段变化；Array<keyof AVMetadata>表示关注Array中的字段变化。 |
| callback | (data: AVMetadata) => void | 是 | 回调函数，参数data是需要更新的元数据。只包含需要更新的元数据属性，不代表当前全量的元数据。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.on('metadataChange', 'all', (metadata: avSession.AVMetadata) => {
  console.info(`on metadataChange assetId : ${metadata.assetId}`);
});

avcontroller.on('metadataChange', ['assetId', 'title', 'description'], (metadata: avSession.AVMetadata) => {
  console.info(`on metadataChange assetId : ${metadata.assetId}`);
});
```



#### off('metadataChange')10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

off(type: 'metadataChange', callback?: (data: AVMetadata) => void)

取消元数据变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'metadataChange'。 |
| callback | (data: AVMetadata) => void | 否 | 回调函数，参数data是需要更新的元数据。只包含需要更新的元数据属性，并不代表当前全量的元数据。 该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.off('metadataChange');
```



#### on('playbackStateChange')10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'playbackStateChange', filter: Array<keyof AVPlaybackState> | 'all', callback: (state: AVPlaybackState) => void)

设置播放状态变化的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'playbackStateChange'，当播放状态需要更新时，触发该事件。 需要更新表示对应属性值被重新设置过，不论新值与旧值是否相同。 |
| filter | Array<keyof AVPlaybackState>\|'all' | 是 | 'all'表示关注播放状态所有字段更新。 Array<keyof AVPlaybackstate> 表示关注Array中的字段更新。 |
| callback | (state: AVPlaybackState) => void | 是 | 回调函数，参数state是需要更新的播放状态。只包含需要更新的播放状态属性，并不代表当前全量的播放状态。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.on('playbackStateChange', 'all', (playbackState: avSession.AVPlaybackState) => {
  console.info(`on playbackStateChange state : ${playbackState.state}`);
});

avcontroller.on('playbackStateChange', ['state', 'speed', 'loopMode'], (playbackState: avSession.AVPlaybackState) => {
  console.info(`on playbackStateChange state : ${playbackState.state}`);
});
```



#### off('playbackStateChange')10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

off(type: 'playbackStateChange', callback?: (state: AVPlaybackState) => void)

取消播放状态变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'playbackStateChange'。 |
| callback | (state: AVPlaybackState) => void | 否 | 回调函数，参数state是需要更新的播放状态。只包含需要更新的播放状态属性，并不代表当前全量的播放状态。 该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.off('playbackStateChange');
```



#### on('callMetadataChange')11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'callMetadataChange', filter: Array<keyof CallMetadata> | 'all', callback: Callback&lt;CallMetadata&gt;): void

设置通话元数据变化的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'callMetadataChange'：当通话元数据变化时，触发该事件。 |
| filter | Array<keyof CallMetadata>\|'all' | 是 | 'all'表示关注通话元数据所有字段变化；Array<keyof CallMetadata> 表示关注Array中的字段变化。\| 'all'。 |
| callback | Callback&lt;CallMetadata&gt; | 是 | 回调函数，参数callmetadata是变化后的通话元数据。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.on('callMetadataChange', 'all', (callmetadata: avSession.CallMetadata) => {
  console.info(`on callMetadataChange state : ${callmetadata.name}`);
});

avcontroller.on('callMetadataChange', ['name'], (callmetadata: avSession.CallMetadata) => {
  console.info(`on callMetadataChange state : ${callmetadata.name}`);
});
```



#### off('callMetadataChange')11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

off(type: 'callMetadataChange', callback?: Callback&lt;CallMetadata&gt;): void

取消设置通话元数据变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'callMetadataChange'。 |
| callback | Callback&lt;CallMetadata&gt; | 否 | 回调函数，参数calldata是变化后的通话原数据。 该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.off('callMetadataChange');
```



#### on('callStateChange')11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'callStateChange', filter: Array<keyof AVCallState> | 'all', callback: Callback&lt;AVCallState&gt;): void

设置通话状态变化的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'callStateChange'：当通话状态变化时，触发该事件。 |
| filter | Array<keyof AVCallState>\|'all' | 是 | 'all' 表示关注通话状态所有字段变化；Array<keyof AVCallState>表示关注Array中的字段变化。\| 'all'。 |
| callback | Callback&lt;AVCallState&gt; | 是 | 回调函数，参数callstate是变化后的通话状态。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified.2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.on('callStateChange', 'all', (callstate: avSession.AVCallState) => {
  console.info(`on callStateChange state : ${callstate.state}`);
});

avcontroller.on('callStateChange', ['state'], (callstate: avSession.AVCallState) => {
  console.info(`on callStateChange state : ${callstate.state}`);
});
```



#### off('callStateChange')11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

off(type: 'callStateChange', callback?: Callback&lt;AVCallState&gt;): void

取消设置通话状态变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'callStateChange'。 |
| callback | Callback&lt;AVCallState&gt; | 否 | 回调函数，参数callstate是变化后的通话状态。 该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.off('callStateChange');
```



#### on('sessionDestroy')10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'sessionDestroy', callback: () => void)

会话销毁的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'sessionDestroy'：当检测到会话销毁时，触发该事件。 |
| callback | () => void | 是 | 回调函数。当监听事件注册成功，err为undefined，否则为错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.on('sessionDestroy', () => {
  console.info('Succeeded in session destroy.');
});
```



#### off('sessionDestroy')10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

off(type: 'sessionDestroy', callback?: () => void)

取消监听会话的销毁事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'sessionDestroy'。 |
| callback | () => void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。 该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified.2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.off('sessionDestroy');
```



#### on('activeStateChange')10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'activeStateChange', callback: (isActive: boolean) => void)

会话的激活状态的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'activeStateChange'：当检测到会话的激活状态发生改变时，触发该事件。 |
| callback | (isActive: boolean) => void | 是 | 回调函数。参数isActive表示会话是否被激活。true表示被激活，false表示禁用。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.on('activeStateChange', (isActive: boolean) => {
  console.info(`Succeeded in active state change: ${isActive}`);
});
```



#### off('activeStateChange')10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

off(type: 'activeStateChange', callback?: (isActive: boolean) => void)

取消监听会话激活状态变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'activeStateChange'。 |
| callback | (isActive: boolean) => void | 否 | 回调函数。参数isActive表示会话是否被激活。true表示被激活，false表示禁用。 该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.off('activeStateChange');
```



#### on('validCommandChange')10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'validCommandChange', callback: (commands: Array&lt;AVControlCommandType&gt;) => void)

会话支持的有效命令变化监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'validCommandChange'：当检测到会话的合法命令发生改变时，触发该事件。 |
| callback | (commands: Array&lt;AVControlCommandType&gt;) => void | 是 | 回调函数。参数commands是有效命令的集合。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.on('validCommandChange', (validCommands: avSession.AVControlCommandType[]) => {
  console.info(`Succeeded in valid command change, size: ${validCommands.length}`);
  console.info(`Succeeded in valid command change, validCommands: ${validCommands.values()}`);
});
```



#### off('validCommandChange')10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

off(type: 'validCommandChange', callback?: (commands: Array&lt;AVControlCommandType&gt;) => void)

取消监听会话有效命令变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'validCommandChange'。 |
| callback | (commands: Array&lt;AVControlCommandType&gt;) => void | 否 | 回调函数。参数commands是有效命令的集合。 该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.off('validCommandChange');
```



#### on('outputDeviceChange')10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'outputDeviceChange', callback: (state: ConnectionState, device: OutputDeviceInfo) => void): void

设置播放设备变化的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件为'outputDeviceChange'：当播放设备变化时，触发该事件）。 |
| callback | (state: ConnectionState, device: OutputDeviceInfo) => void | 是 | 回调函数，参数device是设备相关信息。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.on('outputDeviceChange', (state: avSession.ConnectionState, device: avSession.OutputDeviceInfo) => {
  console.info(`on outputDeviceChange state: ${state}, device : ${device}`);
});
```



#### off('outputDeviceChange')10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

off(type: 'outputDeviceChange', callback?: (state: ConnectionState, device: OutputDeviceInfo) => void): void

取消监听分布式设备变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'outputDeviceChange'。 |
| callback | (state: ConnectionState, device: OutputDeviceInfo) => void | 否 | 回调函数，参数device是设备相关信息。 该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.off('outputDeviceChange');
```



#### on('sessionEvent')10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'sessionEvent', callback: (sessionEvent: string, args: {[key: string]: Object}) => void): void

媒体控制器设置会话自定义事件变化的监听器。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'sessionEvent'：当会话事件变化时，触发该事件。 |
| callback | (sessionEvent: string, args: {[key: string]: Object}) => void | 是 | 回调函数，sessionEvent为变化的会话事件名，args为事件的参数。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```ArkTS
// Index.ets
avcontroller.on('sessionEvent', (sessionEvent, args) => {
  console.info(`OnSessionEvent, sessionEvent is ${sessionEvent}, args: ${JSON.stringify(args)}`);
});
```



#### off('sessionEvent')10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

off(type: 'sessionEvent', callback?: (sessionEvent: string, args: {[key: string]: Object}) => void): void

取消会话事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'sessionEvent'。 |
| callback | (sessionEvent: string, args: {[key: string]: Object}) => void | 否 | 回调函数，参数sessionEvent是变化的事件名，args为事件的参数。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.off('sessionEvent');
```



#### on('queueItemsChange')10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'queueItemsChange', callback: (items: Array<[AVQueueItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#avqueueitem10)>) => void): void

媒体控制器设置会话自定义播放列表变化的监听器。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'queueItemsChange'：当session修改播放列表时，触发该事件。 |
| callback | (items: Array&lt;AVQueueItem&gt;) => void | 是 | 回调函数，items为变化的播放列表。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.on('queueItemsChange', (items: avSession.AVQueueItem[]) => {
  console.info(`OnQueueItemsChange, items length is ${items.length}`);
});
```



#### off('queueItemsChange')10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

off(type: 'queueItemsChange', callback?: (items: Array<[AVQueueItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#avqueueitem10)>) => void): void

取消播放列表变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'queueItemsChange'。 |
| callback | (items: Array&lt;AVQueueItem&gt;) => void | 否 | 回调函数，参数items是变化的播放列表。 该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.off('queueItemsChange');
```



#### on('queueTitleChange')10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'queueTitleChange', callback: (title: string) => void): void

媒体控制器设置会话自定义播放列表的名称变化的监听器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'queueTitleChange'：当session修改播放列表名称时，触发该事件。 |
| callback | (title: string) => void | 是 | 回调函数，title为变化的播放列表名称。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.on('queueTitleChange', (title: string) => {
  console.info(`queueTitleChange, title is ${title}`);
});
```



#### off('queueTitleChange')10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

off(type: 'queueTitleChange', callback?: (title: string) => void): void

取消播放列表名称变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'queueTitleChange'。 |
| callback | (title: string) => void | 否 | 回调函数，参数items是变化的播放列表名称。 该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.off('queueTitleChange');
```



#### on('extrasChange')10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

on(type: 'extrasChange', callback: (extras: {[key: string]: Object}) => void): void

媒体控制器设置自定义媒体数据包事件变化的监听器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'extrasChange'：当媒体提供方设置自定义媒体数据包时，触发该事件。 |
| callback | (extras: {[key: string]: Object}) => void | 是 | 回调函数，extras为媒体提供方新设置的自定义媒体数据包，该自定义媒体数据包与dispatchSessionEvent方法设置的数据包完全一致。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```json
avcontroller.on('extrasChange', (extras) => {
  console.info(`Caught extrasChange event,the new extra is: ${JSON.stringify(extras)}`);
});
```



#### off('extrasChange')10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

off(type: 'extrasChange', callback?: (extras: {[key: string]: Object}) => void): void

取消自定义媒体数据包变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'extrasChange'。 |
| callback | (extras: {[key: string]: Object}) => void | 否 | 注册监听事件时的回调函数。 该参数为可选参数，若不填写该参数，则认为取消会话所有与此事件相关的监听。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.off('extrasChange');
```



#### on('customDataChange')20+

**支持设备：** Phone | PC/2in1 | Tablet | TV

on(type: 'customDataChange', callback: Callback<Record<string, Object>>): void

注册从远程设备发送的自定义数据的监听器。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'customDataChange'，当媒体提供方发送自定义数据时，触发该事件。 |
| callback | Callback<Record<string, Object>> | 是 | 回调函数，用于接收自定义数据。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```json
avcontroller.on('customDataChange', (callback) => {
  console.info(`Caught customDataChange event,the new callback is: ${JSON.stringify(callback)}`);
});
```



#### off('customDataChange')20+

**支持设备：** Phone | PC/2in1 | Tablet | TV

off(type: 'customDataChange', callback?: Callback<Record<string, Object>>): void

取消自定义数据监听。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持的事件是'customDataChange'。 |
| callback | Callback<Record<string, Object>> | 否 | 注册监听事件时的回调函数。该参数为可选参数，若不填写该参数，则认为取消会话所有与此事件相关的监听。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.off('customDataChange');
```



#### getAVPlaybackStateSync10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getAVPlaybackStateSync(): AVPlaybackState;

使用同步方法获取当前会话的播放状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| AVPlaybackState | 当前会话的播放状态。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
let playbackState: avSession.AVPlaybackState = avcontroller.getAVPlaybackStateSync();
```



#### getAVMetadataSync10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getAVMetadataSync(): AVMetadata

使用同步方法获取会话元数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| AVMetadata | 会话元数据。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
let metaData: avSession.AVMetadata = avcontroller.getAVMetadataSync();
```



#### getAVCallState11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getAVCallState(): Promise&lt;AVCallState&gt;

获取通话状态数据。结果通过Promise异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;AVCallState&gt; | Promise对象，返回通话状态。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.getAVCallState().then((callstate: avSession.AVCallState) => {
  console.info(`Succeeded in getting AV call state: ${callstate.state}`);
});
```



#### getAVCallState11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getAVCallState(callback: AsyncCallback&lt;AVCallState&gt;): void

获取通话状态数据。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;AVCallState&gt; | 是 | 回调函数，返回通话状态。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.getAVCallState((err: BusinessError, callstate: avSession.AVCallState) => {
  console.info(`Succeeded in getting AV call state: ${callstate.state}`);
});
```



#### getCallMetadata11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getCallMetadata(): Promise&lt;CallMetadata&gt;

获取通话会话的元数据。结果通过Promise异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;CallMetadata&gt; | Promise对象，返回会话元数据。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.getCallMetadata().then((calldata: avSession.CallMetadata) => {
  console.info(`Succeeded in getting call metadata, name: ${calldata.name}`);
});
```



#### getCallMetadata11+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getCallMetadata(callback: AsyncCallback&lt;CallMetadata&gt;): void

获取通话会话的元数据。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;CallMetadata&gt; | 是 | 回调函数，返回会话元数据。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
avcontroller.getCallMetadata((calldata: avSession.CallMetadata) => {
  console.info(`Succeeded in getting call metadata, name: ${calldata.name}`);
});
```



#### getAVQueueTitleSync10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getAVQueueTitleSync(): string

使用同步方法获取当前会话播放列表的名称。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 当前会话播放列表名称。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
let currentQueueTitle: string = avcontroller.getAVQueueTitleSync();
```



#### getAVQueueItemsSync10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getAVQueueItemsSync(): Array&lt;AVQueueItem&gt;

使用同步方法获取当前会话播放列表相关信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;AVQueueItem&gt; | 当前会话播放列表队列。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
let currentQueueItems: Array<avSession.AVQueueItem> = avcontroller.getAVQueueItemsSync();
```



#### getOutputDeviceSync10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getOutputDeviceSync(): OutputDeviceInfo

使用同步方法获取当前输出设备信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| OutputDeviceInfo | 当前输出设备信息。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
let currentOutputDevice: avSession.OutputDeviceInfo = avcontroller.getOutputDeviceSync();
```



#### isActiveSync10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

isActiveSync(): boolean

使用同步方法判断会话是否被激活。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 会话是否为激活状态，true表示被激活，false表示禁用。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
let isActive: boolean = avcontroller.isActiveSync();
```



#### getValidCommandsSync10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getValidCommandsSync(): Array&lt;AVControlCommandType&gt;

使用同步方法获取会话支持的有效命令。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;AVControlCommandType&gt; | 会话支持的有效命令的集合。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |


**示例：**

```text
let validCommands: Array<avSession.AVControlCommandType> = avcontroller.getValidCommandsSync();
```
