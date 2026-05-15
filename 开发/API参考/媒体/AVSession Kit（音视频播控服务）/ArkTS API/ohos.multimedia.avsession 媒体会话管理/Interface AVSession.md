# Interface (AVSession)

更新时间：2026-05-07 09:37:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-avsession
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

调用[avSession.createAVSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-f#avsessioncreateavsession10)后，返回会话的实例，可以获得会话ID，完成设置元数据，播放状态信息等操作。


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```ts
import { avSession } from '@kit.AVSessionKit';
```


## 属性
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

**系统能力：** SystemCapability.Multimedia.AVSession.Core


| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sessionId10+ | string | 是 | 否 | AVSession对象唯一的会话标识。          元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| sessionType10+ | [AVSessionType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-t#avsessiontype10) | 是 | 否 | AVSession会话类型。          元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| sessionTag22+ | string | 是 | 否 | AVSession会话的自定义标签信息。          元服务API： 从API version 22开始，该接口支持在元服务中使用。 |


**示例：**


```ts
let sessionId: string = currentAVSession.sessionId;
let sessionType: avSession.AVSessionType = currentAVSession.sessionType;
```


## setAVMetadata10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setAVMetadata(data: AVMetadata): Promise<void>

设置会话元数据。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [AVMetadata](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#avmetadata10) | 是 | 会话元数据。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。当元数据设置成功，无返回结果，否则返回错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
let metadata: avSession.AVMetadata = {
  assetId: '121278',
  title: 'lose yourself',
  artist: 'Eminem',
  author: 'ST',
  album: 'Slim shady',
  writer: 'ST',
  composer: 'ST',
  duration: 2222,
  mediaImage: 'https://www.example.com/example.jpg',
  subtitle: '8 Mile',
  description: 'Rap',
  // LRC中有两类元素：一种是时间标签+歌词，一种是ID标签。
  // 例如：[00:25.44]xxx\r\n[00:26.44]xxx\r\n
  lyric: 'lrc格式歌词内容',
  // singleLyricText字段存储单条歌词文本，不包含时间戳。
  // 例如："单条歌词内容"。
  singleLyricText: '单条歌词内容',
  previousAssetId: '121277',
  nextAssetId: '121279',
};
currentAVSession.setAVMetadata(metadata).then(() => {
  console.info('Succeeded in setting AVMetadata.');
});
```


## setAVMetadata10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setAVMetadata(data: AVMetadata, callback: AsyncCallback<void>): void

设置会话元数据。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [AVMetadata](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#avmetadata10) | 是 | 会话元数据。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当元数据设置成功，err为undefined，否则返回错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
let metadata: avSession.AVMetadata = {
  assetId: '121278',
  title: 'lose yourself',
  artist: 'Eminem',
  author: 'ST',
  album: 'Slim shady',
  writer: 'ST',
  composer: 'ST',
  duration: 2222,
  mediaImage: 'https://www.example.com/example.jpg',
  subtitle: '8 Mile',
  description: 'Rap',
  // LRC中有两类元素：一种是时间标签+歌词，一种是ID标签。
  // 例如：[00:25.44]xxx\r\n[00:26.44]xxx\r\n
  lyric: 'lrc格式歌词内容',
  // singleLyricText字段存储单条歌词文本，不包含时间戳。
  // 例如："单条歌词内容"。
  singleLyricText: '单条歌词内容',
  previousAssetId: '121277',
  nextAssetId: '121279',
};
currentAVSession.setAVMetadata(metadata, () => {
  console.info('Succeeded in setting AVMetadata.');
});
```


## setCallMetadata11+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setCallMetadata(data: CallMetadata): Promise<void>

设置通话会话元数据。结果通过Promise异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [CallMetadata](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#callmetadata11) | 是 | 通话会话元数据。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。当通话元数据设置成功，无返回结果，否则返回错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';

import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Text('Hello World')
      .fontSize(50)
      .fontWeight(FontWeight.Bold)
    }
    .width('100%')
    .height('100%')
  }
}

class CallManager {
  private currentAVSession: avSession.AVSession | null = null;

  async setCallMetadata() {
    try {
      let value = await resourceManager.getSysResourceManager().getRawFileContent('IMAGE_URI');
      let imageSource = await image.createImageSource(value.buffer);
      let imagePixel = await imageSource.createPixelMap({ desiredSize: { width: 150, height: 150 } });
      let calldata: avSession.CallMetadata = {
        name: "xiaoming",
        phoneNumber: "111xxxxxxxx",
        avatar: imagePixel
      };
      await this.currentAVSession?.setCallMetadata(calldata);
      console.info('Succeeded in setting call metadata.');
    }
  }
}
```


## setCallMetadata11+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setCallMetadata(data: CallMetadata, callback: AsyncCallback<void>): void

设置通话会话元数据。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [CallMetadata](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#callmetadata11) | 是 | 通话会话元数据。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当通话元数据设置成功，err为undefined，否则返回错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';

import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Text('Hello World')
      .fontSize(50)
      .fontWeight(FontWeight.Bold)
    }
    .width('100%')
    .height('100%')
  }
}

class CallManager {
  private currentAVSession: avSession.AVSession | null = null;

  async setCallMetadata() {
    try {
      let value = await resourceManager.getSysResourceManager().getRawFileContent('IMAGE_URI');
      let imageSource = await image.createImageSource(value.buffer);
      let imagePixel = await imageSource.createPixelMap({ desiredSize: { width: 150, height: 150 } });
      let calldata: avSession.CallMetadata = {
        name: "xiaoming",
        phoneNumber: "111xxxxxxxx",
        avatar: imagePixel
      };
      this.currentAVSession?.setCallMetadata(calldata, () => {
        console.info('Succeeded in setting call metadata.');
      });
    }
  }
}
```


## setAVCallState11+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setAVCallState(state: AVCallState): Promise<void>

设置通话状态。结果通过Promise异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | [AVCallState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#avcallstate11) | 是 | 通话状态。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。当通话元数据设置成功，无返回结果，否则返回错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
let calldata: avSession.AVCallState = {
  state: avSession.CallState.CALL_STATE_ACTIVE,
  muted: false,
};
currentAVSession.setAVCallState(calldata).then(() => {
  console.info('Succeeded in setting AVCallState.');
});
```


## setAVCallState11+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setAVCallState(state: AVCallState, callback: AsyncCallback<void>): void

设置通话状态。结果通过callback异���回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | [AVCallState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#avcallstate11) | 是 | 通话状态。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当通话元数据设置成功，err为undefined，否则返回错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
let avcalldata: avSession.AVCallState = {
  state: avSession.CallState.CALL_STATE_ACTIVE,
  muted: false,
};
currentAVSession.setAVCallState(avcalldata, () => {
  console.info('Succeeded in setting AVCallState.');
});
```


## setAVPlaybackState10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setAVPlaybackState(state: AVPlaybackState): Promise<void>

设置会话播放状态。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | [AVPlaybackState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#avplaybackstate10) | 是 | 会话播放状态，包括状态、倍数、循环模式等信息。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。当播放状态设置成功，无返回结果，否则返回错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
let playbackState: avSession.AVPlaybackState = {
  state: avSession.PlaybackState.PLAYBACK_STATE_PLAY,
  speed: 1.0,
  position: { elapsedTime: 10, updateTime: new Date().getTime() },
  bufferedTime: 1000,
  loopMode: avSession.LoopMode.LOOP_MODE_SINGLE,
  isFavorite: true,
};
currentAVSession.setAVPlaybackState(playbackState).then(() => {
  console.info('Succeeded in setting AVPlaybackState.');
});
```


## setAVPlaybackState10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setAVPlaybackState(state: AVPlaybackState, callback: AsyncCallback<void>): void

设置会话播放状态。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | [AVPlaybackState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#avplaybackstate10) | 是 | 会话播放状态，包括状态、倍数、循环模式等信息。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当播放状态设置成功，err为undefined，否则返回错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
let PlaybackState: avSession.AVPlaybackState = {
  state: avSession.PlaybackState.PLAYBACK_STATE_PLAY,
  speed: 1.0,
  position: { elapsedTime: 10, updateTime: new Date().getTime() },
  bufferedTime: 1000,
  loopMode: avSession.LoopMode.LOOP_MODE_SINGLE,
  isFavorite: true,
};
currentAVSession.setAVPlaybackState(PlaybackState, () => {
  console.info('Succeeded in setting AVPlaybackState.');
});
```


## setLaunchAbility10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setLaunchAbility(ability: WantAgent): Promise<void>

设置一个WantAgent用于拉起会话的Ability。结果通过Promise异步回调方式返回。

通过点击播控组件可以跳转到对应的播放界面，默认跳转到[avSession.createAVSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-f#avsessioncreateavsession10)接口传入的context所属的UIAbility界面。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [WantAgent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-wantagent) | 是 | 应用的相关属性信息，如bundleName，abilityName，deviceId等。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。当Ability设置成功，无返回结果，否则返回错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例��**


```ts
import { wantAgent } from '@kit.AbilityKit';

// WantAgentInfo对象。
let wantAgentInfo: wantAgent.WantAgentInfo = {
  wants: [
    {
      deviceId: 'deviceId',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility',
      action: 'action1',
      entities: ['entity1'],
      type: 'MIMETYPE',
      uri: 'key = {true,true,false}',
      parameters: {
        mykey0: 2222,
        mykey1: [1, 2, 3],
        mykey2: '[1, 2, 3]',
        mykey3: 'ssssssssssssssssssssssssss',
        mykey4: [false, true, false],
        mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
        mykey6: true,
      },
    },
  ],
  operationType: wantAgent.OperationType.START_ABILITIES,
  requestCode: 0,
  wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG],
};

wantAgent.getWantAgent(wantAgentInfo).then((agent) => {
  currentAVSession.setLaunchAbility(agent).then(() => {
    console.info('Succeeded in setting launch ability.');
  });
});
```


## setLaunchAbility10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setLaunchAbility(ability: WantAgent, callback: AsyncCallback<void>): void

设置一个WantAgent用于拉起会话的Ability。结果通过callback异步回调方式返回。

通过点击播控组件可以跳转到对应的播放界面，默认跳转到[avSession.createAVSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-f#avsessioncreateavsession10)接口传入的context所属的UIAbility界面。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [WantAgent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-wantagent) | 是 | 应用的相关属性信息，如bundleName，abilityName，deviceId等。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当Ability设置成功，err为undefined，否则返回错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
import { wantAgent } from '@kit.AbilityKit';

// WantAgentInfo对象。
let wantAgentInfo: wantAgent.WantAgentInfo = {
  wants: [
    {
      deviceId: 'deviceId',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility',
      action: 'action1',
      entities: ['entity1'],
      type: 'MIMETYPE',
      uri: 'key = {true,true,false}',
      parameters: {
        mykey0: 2222,
        mykey1: [1, 2, 3],
        mykey2: '[1, 2, 3]',
        mykey3: 'ssssssssssssssssssssssssss',
        mykey4: [false, true, false],
        mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
        mykey6: true,
      },
    },
  ],
  operationType: wantAgent.OperationType.START_ABILITIES,
  requestCode: 0,
  wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG],
};

wantAgent.getWantAgent(wantAgentInfo).then((agent) => {
  currentAVSession.setLaunchAbility(agent, () => {
    console.info('Succeeded in setting launch ability.');
  });
});
```


## dispatchSessionEvent10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

dispatchSessionEvent(event: string, args: {[key: string]: Object}): Promise<void>

媒体提供方设置一个会话内自定义事件，包括事件名和键值对形式的事件内容。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 需要设置的会话事件的名称。 |
| args | {[key: string]: Object} | 是 | 需要传递的会话事件内容。 |


> [!NOTE]
> 参数args支持的数据类型有：字符串、数字、布尔值、对象、数组和文件描述符等，详细介绍请参见[@ohos.app.ability.Want(Want)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want)。

**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。当事件设置成功，无返回结果，否则返回错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
      Text(this.message)
      .onClick(()=>{
        let currentAVSession: avSession.AVSession | undefined = undefined;
        let tag = "createNewSession";
        let context: Context = this.getUIContext().getHostContext() as Context;

        avSession.createAVSession(context, tag, "audio", (data: avSession.AVSession) => {
          currentAVSession = data;
          let eventName = "dynamic_lyric";
          if (currentAVSession !== undefined) {
            (currentAVSession as avSession.AVSession).dispatchSessionEvent(eventName, {lyric : "This is lyric"}).then(() => {
              console.info('Succeeded in dispatching session event.');
            })
          }
        });
      })
    }
    .width('100%')
    .height('100%')
  }
}
```


## dispatchSessionEvent10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

dispatchSessionEvent(event: string, args: {[key: string]: Object}, callback: AsyncCallback<void>): void

媒体提供方设置一个会话内自定义事件，包括事件名和键值对形式的事件内容。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 需要设置的会话事件的名称。 |
| args | {[key: string]: Object} | 是 | 需要传递的会话事件内容。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当会话事件设置成功，err为undefined，否则返回错误对象。 |


参数args支持的数据类型有：字符串、数字、布尔值、对象、数组和文件描述符等，详细介绍请参见[@ohos.app.ability.Want(Want)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want)。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
import { avSession } from '@kit.AVSessionKit';
@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
      Text(this.message)
      .onClick(()=>{
        let currentAVSession: avSession.AVSession | undefined = undefined;
        let tag = "createNewSession";
        let context: Context = this.getUIContext().getHostContext() as Context;

        avSession.createAVSession(context, tag, "audio", (data: avSession.AVSession) => {
          currentAVSession = data;
          let eventName: string = "dynamic_lyric";
          if (currentAVSession !== undefined) {
            (currentAVSession as avSession.AVSession).dispatchSessionEvent(eventName, {lyric : "This is lyric"}, () => {
              console.info('Succeeded in dispatching session event.');
            })
          }
        });
      })
    }
    .width('100%')
    .height('100%')
  }
}
```


## setAVQueueItems10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setAVQueueItems(items: Array<AVQueueItem>): Promise<void>

设置媒体播放列表。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | Array&lt;[AVQueueItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#avqueueitem10)&gt; | 是 | 播放列表单项的队列，用以表示播放列表。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。当播放列表设置成功，无返回结果，否则返回错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';

import { avSession } from '@kit.AVSessionKit';
interface ExtrasType {
  extras: string;
}

@Entry
@Component
struct Index {
  build() {
    Column() {
    }
  }
}

let currentAVSession: avSession.AVSession;

async function setAVQueueItems() {
  try {
    let value = await resourceManager.getSysResourceManager().getRawFileContent('IMAGE_URI');
    let imageSource = await image.createImageSource(value.buffer);
    let imagePixel = await imageSource.createPixelMap({desiredSize:{width: 150, height: 150}});
    let queueItemDescription_1: avSession.AVMediaDescription = {
      assetId: '001',
      title: 'music_name',
      subtitle: 'music_sub_name',
      description: 'music_description',
      mediaImage : imagePixel,
      extras: {extras:'any'}
    };
    let queueItem_1: avSession.AVQueueItem = {
      itemId: 1,
      description: queueItemDescription_1
    } as avSession.AVQueueItem;
    let queueItemDescription_2: avSession.AVMediaDescription = {
      assetId: '002',
      title: 'music_name',
      subtitle: 'music_sub_name',
      description: 'music_description',
      mediaImage: imagePixel,
      extras: {extras:'any'}
    };
    let queueItem_2: avSession.AVQueueItem = {
      itemId: 2,
      description: queueItemDescription_2
    } as avSession.AVQueueItem;
    let queueItemsArray: avSession.AVQueueItem[] = [queueItem_1, queueItem_2];
    currentAVSession.setAVQueueItems(queueItemsArray).then(() => {
      console.info('Succeeded in setting AVQueueItems.');
    });
  }
}
```


## setAVQueueItems10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setAVQueueItems(items: Array<AVQueueItem>, callback: AsyncCallback<void>): void

设置媒体播放列表。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | Array&lt;[AVQueueItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#avqueueitem10)&gt; | 是 | 播放列表单项的队列，用以表示播放列表。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当播放状态设置成功，err为undefined，否则返回错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';

import { avSession } from '@kit.AVSessionKit'

interface ExtrasType {
  extras: string;
}

@Entry
@Component
struct Index {
  build() {
    Column() {
    }
  }
}

let currentAVSession: avSession.AVSession;

async function setAVQueueItems() {
  try {
    let value = await resourceManager.getSysResourceManager().getRawFileContent('IMAGE_URI');
    let imageSource = await image.createImageSource(value.buffer);
    let imagePixel = await imageSource.createPixelMap({ desiredSize: { width: 150, height: 150 } });
    let queueItemDescription_1: avSession.AVMediaDescription = {
      assetId: '001',
      title: 'music_name',
      subtitle: 'music_sub_name',
      description: 'music_description',
      mediaImage: imagePixel,
      extras: { extras: 'any' }
    };
    let queueItem_1: avSession.AVQueueItem = {
      itemId: 1,
      description: queueItemDescription_1
    };
    let queueItemDescription_2: avSession.AVMediaDescription = {
      assetId: '002',
      title: 'music_name',
      subtitle: 'music_sub_name',
      description: 'music_description',
      mediaImage: imagePixel,
      extras: { extras: 'any' }
    };
    let queueItem_2: avSession.AVQueueItem = {
      itemId: 2,
      description: queueItemDescription_2
    };
    let queueItemsArray: avSession.AVQueueItem[] = [queueItem_1, queueItem_2];
    currentAVSession.setAVQueueItems(queueItemsArray, () => {
      console.info('Succeeded in setting AVQueueItems.');
    });
  }
}
```


## setAVQueueTitle10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setAVQueueTitle(title: string): Promise<void>

设置媒体播放列表名称。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| title | string | 是 | 播放列表的名称。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。当播放列表设置成功，无返回结果，否则返回错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
let queueTitle = 'QUEUE_TITLE';
currentAVSession.setAVQueueTitle(queueTitle).then(() => {
  console.info('Succeeded in setting AVQueueTitle.');
});
```


## setAVQueueTitle10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setAVQueueTitle(title: string, callback: AsyncCallback<void>): void

设置媒体播放列表名称。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| title | string | 是 | 播放列表名称字段。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当播放状态设置成功，err为undefined，否则返回错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
let queueTitle = 'QUEUE_TITLE';
currentAVSession.setAVQueueTitle(queueTitle, () => {
  console.info('Succeeded in setting AVQueueTitle.');
});
```


## setExtras10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setExtras(extras: {[key: string]: Object}): Promise<void>

媒体提供方设置键值对形式的自定义媒体数据包。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| extras | {[key: string]: Object} | 是 | 需要传递的自定义媒体数据包键值对。          说明： 参数extras支持的数据类型有：字符串、数字、布尔值、对象、数组和文件描述符等，详细介绍请参见[@ohos.app.ability.Want(Want)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want)。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified.2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
import { avSession } from '@kit.AVSessionKit';
@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
      Text(this.message)
      .onClick(() => {
        let currentAVSession: avSession.AVSession | undefined = undefined;
        let tag = "createNewSession";
        let context: Context = this.getUIContext().getHostContext() as Context;

        avSession.createAVSession(context, tag, "audio", (data: avSession.AVSession) => {
          currentAVSession = data;
          if (currentAVSession !== undefined) {
            (currentAVSession as avSession.AVSession).setExtras({extras : "This is custom media packet"}).then(() => {
              console.info('Succeeded in setting extras.');
            })
          }
        });
      })
    }
    .width('100%')
    .height('100%')
  }
}
```


## setExtras10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setExtras(extras:{[key: string]: Object}, callback: AsyncCallback<void>): void

媒体提供方设置键值对形式的自定义媒体数据包，使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| extras | {[key: string]: Object} | 是 | 需要传递的自定义媒体数据包键值对。          说明： 参数extras支持的数据类型有：字符串、数字、布尔值、对象、数组和文件描述符等，详细介绍请参见[@ohos.app.ability.Want(Want)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want)。 |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当自定义媒体数据包设置成功，err为undefined，否则返回错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
import { avSession } from '@kit.AVSessionKit';
@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
      Text(this.message)
      .onClick(()=>{
        let currentAVSession: avSession.AVSession | undefined = undefined;
        let tag = "createNewSession";
        let context: Context = this.getUIContext().getHostContext() as Context;

        avSession.createAVSession(context, tag, "audio", (data: avSession.AVSession) => {
          currentAVSession = data;
          if (currentAVSession !== undefined) {
            (currentAVSession as avSession.AVSession).setExtras({extras : "This is custom media packet"}, () => {
              console.info('Succeeded in setting extras.');
            })
          }
        });
      })
    }
    .width('100%')
    .height('100%')
  }
}
```


## sendCustomData20+
**支持设备：** Phone / PC/2in1 / Tablet / TV

sendCustomData(data: Record<string, Object>): Promise<void>

发送私有数据到远端设备。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | Record&lt;string, Object&gt; | 是 | 应用程序填充的自定义数据。服务端仅解析key为'customData'，且Object为string类型的对象。 |


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


**示例：**


```ts
import { avSession } from '@kit.AVSessionKit';
@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
      Text(this.message)
      .onClick(()=>{
        let currentAVSession: avSession.AVSession | undefined = undefined;
        let tag = "createNewSession";
        let context: Context = this.getUIContext().getHostContext() as Context;

        avSession.createAVSession(context, tag, "audio", (data: avSession.AVSession) => {
          currentAVSession = data;
        });
        if (currentAVSession !== undefined) {
          (currentAVSession as avSession.AVSession).sendCustomData({customData : "This is custom data"}).then(() => {
            console.info('Succeeded in sending custom data.');
          })
        }
      })
    }
    .width('100%')
    .height('100%')
  }
}
```


## enableDesktopLyric23+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

enableDesktopLyric(enable: boolean): Promise<void>

当前会话是否启用桌面歌词功能。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否启用桌面歌词。true表示启用，false表示不启用。 |


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
| 6600111 | The desktop lyrics feature is not supported. |


**示例：**


```ts
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
      Text(this.message)
      .onClick(() => {
        let currentAVSession: avSession.AVSession | undefined = undefined;
        let tag = "createNewSession";
        let context: Context = this.getUIContext().getHostContext() as Context;

        avSession.createAVSession(context, tag, "audio", (data: avSession.AVSession) => {
          currentAVSession = data;
        });
        if (currentAVSession !== undefined) {
          (currentAVSession as avSession.AVSession).enableDesktopLyric(true).then(() => {
            console.info('Succeeded in enabling desktop lyric.');
          })
        }
      })
    }
    .width('100%')
    .height('100%')
  }
}
```


## setDesktopLyricVisible23+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setDesktopLyricVisible(visible: boolean): Promise<void>

设置当前会话桌面歌词的显示状态。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**模型约束：** 此接口仅可在Stage模型下使用。

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
| 6600110 | The desktop lyrics feature of this application is not enabled. |
| 6600111 | The desktop lyrics feature is not supported. |


**示例：**


```ts
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
      Text(this.message)
      .onClick(() => {
        let currentAVSession: avSession.AVSession | undefined = undefined;
        let tag = "createNewSession";
        let context: Context = this.getUIContext().getHostContext() as Context;

        avSession.createAVSession(context, tag, "audio", (data: avSession.AVSession) => {
          currentAVSession = data;
        });
        if (currentAVSession !== undefined) {
          (currentAVSession as avSession.AVSession).setDesktopLyricVisible(true).then(() => {
            console.info('Succeeded in setting desktop lyric visible.');
          })
        }
      })
    }
    .width('100%')
    .height('100%')
  }
}
```


## isDesktopLyricVisible23+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

isDesktopLyricVisible(): Promise<boolean>

查询当前会话桌面歌词的显示状态。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**模型约束：** 此接口仅可在Stage模型下使用。

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
| 6600110 | The desktop lyrics feature of this application is not enabled. |
| 6600111 | The desktop lyrics feature is not supported. |


**示例：**


```ts
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
      Text(this.message)
      .onClick(() => {
        let currentAVSession: avSession.AVSession | undefined = undefined;
        let tag = "createNewSession";
        let context: Context = this.getUIContext().getHostContext() as Context;
        avSession.createAVSession(context, tag, "audio", (data: avSession.AVSession) => {
          currentAVSession = data;
        });
        if (currentAVSession !== undefined) {
          (currentAVSession as avSession.AVSession).isDesktopLyricVisible().then((visible: boolean) => {
            console.info(`isDesktopLyricVisible: ${visible}`);
          })
        }
      })
    }
    .width('100%')
    .height('100%')
  }
}
```


## onDesktopLyricVisibilityChanged23+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

onDesktopLyricVisibilityChanged(callback: Callback<boolean>): void

显示桌面歌词状态变更的监听事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;boolean&gt; | 是 | 回调函数。返回true表示开启显示桌面歌词状态；返回false表示关闭显示桌面歌词状态。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
      Text(this.message)
      .onClick(() => {
        let currentAVSession: avSession.AVSession | undefined = undefined;
        let tag = "createNewSession";
        let context: Context = this.getUIContext().getHostContext() as Context;
        avSession.createAVSession(context, tag, "audio", (data: avSession.AVSession) => {
          currentAVSession = data;
        });
        if (currentAVSession !== undefined) {
          (currentAVSession as avSession.AVSession).onDesktopLyricVisibilityChanged((visible: boolean) => {
            console.info(`desktop lyric visible state: ${visible}`);
          });
        }
      })
    }
    .width('100%')
    .height('100%')
  }
}
```


## offDesktopLyricVisibilityChanged23+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

offDesktopLyricVisibilityChanged(callback?: Callback<boolean>): void

取消显示桌面歌词状态变更事件监听，取消后将不再对该事件进行监听。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;boolean&gt; | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。          该参数为可选参数，若不填写该参数，则认为取消所有显示桌面歌词状态变更事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
      Text(this.message)
      .onClick(() => {
        let currentAVSession: avSession.AVSession | undefined = undefined;
        let tag = "createNewSession";
        let context: Context = this.getUIContext().getHostContext() as Context;
        avSession.createAVSession(context, tag, "audio", (data: avSession.AVSession) => {
          currentAVSession = data;
        });
        if (currentAVSession !== undefined) {
          (currentAVSession as avSession.AVSession).offDesktopLyricVisibilityChanged();
        }
      })
    }
    .width('100%')
    .height('100%')
  }
}
```


## setDesktopLyricState23+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setDesktopLyricState(state: DesktopLyricState): Promise<void>

设置当前会话桌面歌词状态。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | [DesktopLyricState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#desktoplyricstate23) | 是 | 桌面歌词状态。 |


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
| 6600110 | The desktop lyrics feature of this application is not enabled. |
| 6600111 | The desktop lyrics feature is not supported. |


**示例：**


```ts
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
      Text(this.message)
      .onClick(() => {
        let currentAVSession: avSession.AVSession | undefined = undefined;
        let tag = "createNewSession";
        let context: Context = this.getUIContext().getHostContext() as Context;

        avSession.createAVSession(context, tag, "audio", (data: avSession.AVSession) => {
          currentAVSession = data;
        });
        if (currentAVSession !== undefined) {
          let state: avSession.DesktopLyricState = {
            isLocked: true,
          };
          (currentAVSession as avSession.AVSession).setDesktopLyricState(state).then(() => {
            console.info('Succeeded in setting desktop lyric state.');
          })
        }
      })
    }
    .width('100%')
    .height('100%')
  }
}
```


## getDesktopLyricState23+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getDesktopLyricState(): Promise<DesktopLyricState>

获取当前会话桌面歌词状态。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;[DesktopLyricState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#desktoplyricstate23)&gt; | Promise对象。返回桌面歌词状态。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600110 | The desktop lyrics feature of this application is not enabled. |
| 6600111 | The desktop lyrics feature is not supported. |


**示例：**


```ts
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
      Text(this.message)
      .onClick(() => {
        let currentAVSession: avSession.AVSession | undefined = undefined;
        let tag = "createNewSession";
        let context: Context = this.getUIContext().getHostContext() as Context;

        avSession.createAVSession(context, tag, "audio", (data: avSession.AVSession) => {
          currentAVSession = data;
        });
        if (currentAVSession !== undefined) {
          (currentAVSession as avSession.AVSession).getDesktopLyricState()
          .then((state: avSession.DesktopLyricState) => {
            console.info(`getDesktopLyricState: ${state.isLocked}`);
          })
        }
      })
    }
    .width('100%')
    .height('100%')
  }
}
```


## onDesktopLyricStateChanged23+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

onDesktopLyricStateChanged(callback: Callback<DesktopLyricState>): void

桌面歌词状态变更的监听事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;[DesktopLyricState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#desktoplyricstate23)&gt; | 是 | 回调函数。返回桌面歌词状态。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
      Text(this.message)
      .onClick(() => {
        let currentAVSession: avSession.AVSession | undefined = undefined;
        let tag = "createNewSession";
        let context: Context = this.getUIContext().getHostContext() as Context;

        avSession.createAVSession(context, tag, "audio", (data: avSession.AVSession) => {
          currentAVSession = data;
        });
        if (currentAVSession !== undefined) {
          (currentAVSession as avSession.AVSession).onDesktopLyricStateChanged((state: avSession.DesktopLyricState) => {
            console.info(`desktop lyric isLocked : ${state.isLocked}`);
          })
        }
      })
    }
    .width('100%')
    .height('100%')
  }
}
```


## offDesktopLyricStateChanged23+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

offDesktopLyricStateChanged(callback?: Callback<DesktopLyricState>): void

取消桌面歌词状态变更事件监听，取消后将不再对该事件进行监听。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;[DesktopLyricState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#desktoplyricstate23)&gt; | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。          该参数为可选参数，若不填写该参数，则认为取消所有桌面歌词状态变更事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
      Text(this.message)
      .onClick(() => {
        let currentAVSession: avSession.AVSession | undefined = undefined;
        let tag = "createNewSession";
        let context: Context = this.getUIContext().getHostContext() as Context;
        avSession.createAVSession(context, tag, "audio", (data: avSession.AVSession) => {
          currentAVSession = data;
        });
        if (currentAVSession !== undefined) {
          (currentAVSession as avSession.AVSession).offDesktopLyricStateChanged();
        }
      })
    }
    .width('100%')
    .height('100%')
  }
}
```


## setBackgroundPlayMode24+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setBackgroundPlayMode(mode: BackgroundPlayMode): Promise<void>

设置后台播放模式。使用promise异步回调。

建议与应用内"是否支持后台播放开关"关联。如未设置，'audio'类型会话默认值为ENABLE_BACKGROUND_PLAY；'video'类型会话默认值为DISABLE_BACKGROUND_PLAY。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [BackgroundPlayMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-e#backgroundplaymode24) | 是 | 后台播放模式。 |


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


**示例：**


```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
      Text(this.message)
      .onClick(() => {
        let currentAVSession: avSession.AVSession | undefined = undefined;
        let tag = "createNewSession";
        let context: Context = this.getUIContext().getHostContext() as Context;
        avSession.createAVSession(context, tag, "audio", (err: BusinessError, data: avSession.AVSession) => {
          if (err) {
            console.error(`CreateAVSession BusinessError: code: ${err.code}, message: ${err.message}`);
          } else {
            currentAVSession = data;
          }
        });
        if (currentAVSession !== undefined) {
          try {
            (currentAVSession as avSession.AVSession).setBackgroundPlayMode(avSession.BackgroundPlayMode.ENABLE_BACKGROUND_PLAY);
          } catch (err) {
            console.error(`setBackgroundPlayMode BusinessError: code: ${err.code}, message: ${err.message}`);
          }
        }
      })
    }
    .width('100%')
    .height('100%')
  }
}
```


## getController10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getController(): Promise<AVSessionController>

获取本会话对应的控制器。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;[AVSessionController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-avsessioncontroller)&gt; | Promise对象。返回会话控制器。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  @State message: string = 'hello world';
  build() {
    Column() {
      Text(this.message)
      .onClick(async ()=>{
        let context: Context = this.getUIContext().getHostContext() as Context;
        let currentAVSession: avSession.AVSession = await avSession.createAVSession(context, 'SESSION_NAME', 'audio');
        let avSessionController: avSession.AVSessionController;
        currentAVSession.getController().then((avController: avSession.AVSessionController) => {
          avSessionController = avController;
          console.info(`Succeeded in getting controller, sessionid: ${avSessionController.sessionId}`);
        });
      })
    }
    .width('100%')
    .height('100%')
  }
}
```


## getController10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getController(callback: AsyncCallback<AVSessionController>): void

获取本会话相应的控制器。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;[AVSessionController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-avsessioncontroller)&gt; | 是 | 回调函数。返回会话控制器。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
import { avSession } from '@kit.AVSessionKit';


@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
      Text(this.message)
      .onClick(async () => {
        let context: Context = this.getUIContext().getHostContext() as Context;
        let currentAVSession: avSession.AVSession = await avSession.createAVSession(context, 'SESSION_NAME', 'audio');
        let avsessionController: avSession.AVSessionController;
        currentAVSession.getController((avcontroller: avSession.AVSessionController) => {
          avsessionController = avcontroller;
          console.info(`Succeeded in getting controller, sessionid: ${avsessionController.sessionId}`);
        });
      })
    }
    .width('100%')
    .height('100%')
  }
}
```


## getAVCastController10+
**支持设备：** Phone / PC/2in1 / Tablet / TV

getAVCastController(): Promise<AVCastController>

设备建立连接后，获取投播控制器。结果通过Promise异步回调方式返回。如果 avsession 未处于投播状态，则控制器将返回 null。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;[AVCastController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-avcastcontroller)&gt; | Promise对象。返回投播控制器实例。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600102 | The session does not exist. |
| 6600109 | The remote connection is not established. |


**示例：**


```ts
let avCastController: avSession.AVCastController;
currentAVSession
  .getAVCastController()
  .then((avcontroller: avSession.AVCastController) => {
    avCastController = avcontroller;
    console.info('Succeeded in getting AV cast controller.');
  });
```


## getAVCastController10+
**支持设备：** Phone / PC/2in1 / Tablet / TV

getAVCastController(callback: AsyncCallback<AVCastController>): void

设备建立连接后，获取投播控制器。结果通过callback异步回调方式返回。如果 avsession 未处于投播状态，则控制器将返回 null。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;[AVCastController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-avcastcontroller)&gt; | 是 | 回调函数，返回投播控制器实例。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600102 | The session does not exist. |
| 6600109 | The remote connection is not established. |


**示例：**


```ts
let avCastController: avSession.AVCastController;
currentAVSession.getAVCastController(
  (avcontroller: avSession.AVCastController) => {
    avCastController = avcontroller;
    console.info('Succeeded in getting AV cast controller.');
  },
);
```


## getOutputDevice10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getOutputDevice(): Promise<OutputDeviceInfo>

通过会话获取播放设备信息。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;[OutputDeviceInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#outputdeviceinfo10)&gt; | Promise对象。返回播放设备信息。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession
  .getOutputDevice()
  .then((outputDeviceInfo: avSession.OutputDeviceInfo) => {
    console.info(
      `Succeeded in getting output device, devices length: ${outputDeviceInfo.devices.length}`,
    );
  });
```


## getOutputDevice10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getOutputDevice(callback: AsyncCallback<OutputDeviceInfo>): void

通过会话获取播放设备相关信息。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;[OutputDeviceInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#outputdeviceinfo10)&gt; | 是 | 回调函数，返回播放设备信息。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.getOutputDevice(
  (outputDeviceInfo: avSession.OutputDeviceInfo) => {
    console.info(
      `Succeeded in getting output device, devices length: ${outputDeviceInfo.devices.length}`,
    );
  },
);
```


## activate10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

activate(): Promise<void>

激活会话，激活后可正常使用会话。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。当会话激活成功，无返回结果，否则返回错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.activate().then(() => {
  console.info('Succeeded in activating.');
});
```


## activate10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

activate(callback: AsyncCallback<void>): void

激活会话，激活后可正常使用会话。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当会话激活成功，err为undefined，否则返回错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.activate(() => {
  console.info('Succeeded in activating.');
});
```


## deactivate10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

deactivate(): Promise<void>

禁用当前会话的功能，可通过[activate](#activate10)恢复。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。当禁用会话成功，无返回结果，否则返回错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.deactivate().then(() => {
  console.info('Succeeded in deactivating.');
});
```


## deactivate10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

deactivate(callback: AsyncCallback<void>): void

禁用当前会话。结果通过callback异步回调方式返回。

禁用当前会话的功能，可通过[activate](#activate10)恢复。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当禁用会话成功，err为undefined，否则返回错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.deactivate(() => {
  console.info('Succeeded in deactivating.');
});
```


## destroy10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

destroy(): Promise<void>

销毁当前会话，使当前会话完全失效。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。当会话销毁成功，无返回结果，否则返回错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.destroy().then(() => {
  console.info('Succeeded in destroying.');
});
```


## destroy10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

destroy(callback: AsyncCallback<void>): void

销毁当前会话，使当前会话完全失效。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数。当会话销毁成功，err为undefined，否则返回错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.destroy(() => {
  console.info('Succeeded in destroying.');
});
```


## on('play')10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

on(type: 'play', callback: () => void): void

设置播放命令监听事件。注册该监听，说明应用支持播放指令。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'play'，当播放命令被发送到会话时，触发该事件回调。 |
| callback | () =&gt; void | 是 | 回调函数。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.on('play', () => {
  console.info('on play entry');
});
```


## onPlay22+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

onPlay(callback: Callback<CommandInfo>): void

设置播放命令监听事件。使用callback异步回调。

应用将通过回调接收控制器发送的[CommandInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#commandinfo22)信息。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;[CommandInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#commandinfo22)&gt; | 是 | 回调函数。当监听事件注册成功，err为undefined，否则为错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.onPlay((info: avSession.CommandInfo) => {
  console.info('on play entry');
});
```


## on('pause')10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

on(type: 'pause', callback: () => void): void

设置暂停命令监听事件。注册该监听，说明应用支持暂停指令。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'pause'，当暂停命令被发送到会话时，触发该事件回调。 |
| callback | () =&gt; void | 是 | 回调函数。当监听事件注册成功，err为undefined，否则为错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.on('pause', () => {
  console.info('on pause entry');
});
```


## on('stop')10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

on(type:'stop', callback: () => void): void

设置停止命令监听事件。注册该监听，说明应用支持停止指令。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件是'stop'，当停止命令被发送到会话时，触发该事件回调。 |
| callback | () =&gt; void | 是 | 回调函数。当监听事件注册成功，err为undefined，否则为错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.on('stop', () => {
  console.info('on stop entry');
});
```


## on('playNext')10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

on(type:'playNext', callback: () => void): void

设置播放下一首命令监听事件。注册该监听，说明应用支持下一首指令。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件是'playNext'，当播放下一首命令被发送到会话时，触发该事件回调。 |
| callback | () =&gt; void | 是 | 回调函数。当监听事件注册成功，err为undefined，否则为错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.on('playNext', () => {
  console.info('on playNext entry');
});
```


## onPlayNext22+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

onPlayNext(callback: Callback<CommandInfo>): void

设置播放下一首命令监听事件。使用callback异步回调。

应用将通过回调接收控制器发送的[CommandInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#commandinfo22)信息。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;[CommandInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#commandinfo22)&gt; | 是 | 回调函数。当监听事件注册成功，err为undefined，否则为错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.onPlayNext((info: avSession.CommandInfo) => {
  console.info('on playNext entry');
});
```


## on('playPrevious')10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

on(type:'playPrevious', callback: () => void): void

设置播放上一首命令监听事件。注册该监听，说明应用支持上一首指令。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件是'playPrevious'，当播放上一首命令被发送到会话时，触发该事件回调。 |
| callback | () =&gt; void | 是 | 回调函数。当监听事件注册成功，err为undefined，否则为错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.on('playPrevious', () => {
  console.info('on playPrevious entry');
});
```


## onPlayPrevious22+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

onPlayPrevious(callback: Callback<CommandInfo>): void

设置播放上一首命令监听事件。使用callback异步回调。

应用将通过回调接收控制器发送的[CommandInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#commandinfo22)信息。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;[CommandInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#commandinfo22)&gt; | 是 | 回调函数。当监听事件注册成功，err为undefined，否则为错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.onPlayPrevious((info: avSession.CommandInfo) => {
  console.info('on playPrevious entry');
});
```


## on('fastForward')10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

on(type: 'fastForward', callback: (time?: number) => void): void

设置快进命令监听事件。注册该监听，说明应用支持快进指令。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件是 'fastForward'，当快进命令被发送到会话时，触发该事件回调。 |
| callback | (time?: number) =&gt; void | 是 | 回调函数。参数time是时间节点，单位为秒。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.on('fastForward', (time?: number) => {
  console.info('on fastForward entry');
});
```


## onFastForward22+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

onFastForward(callback: TwoParamCallback<number, CommandInfo>): void

设置快进命令监听事件。使用callback异步回调。

应用将通过回调接收控制器发送的快进时间参数，以及对应的[CommandInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#commandinfo22)信息。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | TwoParamCallback&lt;number, [CommandInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#commandinfo22)&gt; | 是 | 回调函数。用于处理'fastForward'操作。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.onFastForward((time: number, info: avSession.CommandInfo) => {
  console.info('on fastForward entry');
});
```


## on('rewind')10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

on(type:'rewind', callback: (time?: number) => void): void

设置快退命令监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件是'rewind'，当快退命令被发送到会话时，触发该事件回调。 |
| callback | (time?: number) =&gt; void | 是 | 回调函数。参数time是时间节点，单位为秒。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.on('rewind', (time?: number) => {
  console.info('on rewind entry');
});
```


## onRewind22+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

onRewind(callback: TwoParamCallback<number, CommandInfo>): void

设置快退命令监听事件。使用callback异步回调。

应用将通过回调接收控制器发送的快退时间参数，以及对应的[CommandInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#commandinfo22)信息。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | TwoParamCallback&lt;number, [CommandInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#commandinfo22)&gt; | 是 | 回调函数。用于处理'rewind'操作。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.onRewind((time: number, info: avSession.CommandInfo) => {
  console.info('on rewind entry');
});
```


## on('playWithAssetId')20+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

on(type:'playWithAssetId', callback: Callback<string>): void

设置指定资源id进行播放的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件是'playWithAssetId'，当指定资源id进行播放时，触发该事件回调。 |
| callback | Callback&lt;string&gt; | 是 | 回调函数。参数assetId是媒体id。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
let playWithAssetIdCallback = (assetId: string) => {
  console.info(`on playWithAssetId entry,  assetId = ${assetId}`);
};
currentAVSession.on('playWithAssetId', playWithAssetIdCallback);
```


## off('playWithAssetId')20+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

off(type: 'playWithAssetId', callback?: Callback<string>): void

取消指定资源id进行播放的事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'playWithAssetId'。 |
| callback | Callback&lt;string&gt; | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。          该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。参数assetId是媒体id。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.off('playWithAssetId');
```


## on('seek')10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

on(type: 'seek', callback: (time: number) => void): void

设置跳转节点监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'seek'：当跳转节点命令被发送到会话时，触发该事件。 |
| callback | (time: number) =&gt; void | 是 | 回调函数。参数time是时间节点，单位为毫秒。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.on('seek', (time: number) => {
  console.info(`on seek entry time : ${time}`);
});
```


## on('setSpeed')10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

on(type: 'setSpeed', callback: (speed: number) => void): void

设置播放速率的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'setSpeed'：当设置播放速率的命令被发送到会话时，触发该事件。 |
| callback | (speed: number) =&gt; void | 是 | 回调函数。参数speed是播放倍速。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.on('setSpeed', (speed: number) => {
  console.info(`on setSpeed speed : ${speed}`);
});
```


## on('setLoopMode')10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

on(type: 'setLoopMode', callback: (mode: LoopMode) => void): void

设置循环模式的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'setLoopMode'：当设置循环模式的命令被发送到会话时，触发该事件。 |
| callback | (mode: [LoopMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-e#loopmode10)) =&gt; void | 是 | 回调函数。参数mode是循环模式。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.on('setLoopMode', (mode: avSession.LoopMode) => {
  console.info(`on setLoopMode mode : ${mode}`);
});
```


## on('setTargetLoopMode')18+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

on(type: 'setTargetLoopMode', callback: Callback<LoopMode>): void

设置目标循环模式的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'setTargetLoopMode'。          - 'setTargetLoopMode'：当设置目标循环模式的命令被发送到会话时，触发该事件。 |
| callback | Callback&lt;[LoopMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-e#loopmode10)&gt; | 是 | 回调函数。参数表示目标循环模式。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.on('setTargetLoopMode', (mode: avSession.LoopMode) => {
  console.info(`on setTargetLoopMode mode : ${mode}`);
});
```


## on('toggleFavorite')10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

on(type: 'toggleFavorite', callback: (assetId: string) => void): void

设置是否收藏的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'toggleFavorite'：当是否收藏的命令被发送到会话时，触发该事件。 |
| callback | (assetId: string) =&gt; void | 是 | 回调函数。参数assetId是媒体ID。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.on('toggleFavorite', (assetId: string) => {
  console.info(`on toggleFavorite mode : ${assetId}`);
});
```


## on('skipToQueueItem')10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

on(type: 'skipToQueueItem', callback: (itemId: number) => void): void

设置播放列表其中某项被选中的监听事件，session端可以选择对这个单项歌曲进行播放。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'skipToQueueItem'：当播放列表选中单项的命令被发送到会话时，触发该事件。 |
| callback | (itemId: number) =&gt; void | 是 | 回调函数。参数itemId是选中的播放列表项的ID。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.on('skipToQueueItem', (itemId: number) => {
  console.info(`on skipToQueueItem id : ${itemId}`);
});
```


## on('handleKeyEvent')10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

on(type: 'handleKeyEvent', callback: (event: KeyEvent) => void): void

设置蓝牙/有线等外设接入的按键输入事件的监听，监听多媒体按键事件中播放、暂停、上下一首、快进、快退的指令。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'handleKeyEvent'：当按键事件被发送到会话时，触发该事件。 |
| callback | (event: [KeyEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-keyevent)) =&gt; void | 是 | 回调函数。参数event是按键事件。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
import { KeyEvent } from '@kit.InputKit';

currentAVSession.on('handleKeyEvent', (event: KeyEvent) => {
  console.info(`on handleKeyEvent event : ${event}`);
});
```


## on('outputDeviceChange')10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

on(type: 'outputDeviceChange', callback: (state: ConnectionState, device: OutputDeviceInfo) => void): void

设置播放设备变化的监听事件。应用接入[multimedia.avCastPicker (投播组件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-multimedia-avcastpicker)，当用户通过组件切换设备时，会收到设备切换的回调。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'outputDeviceChange'：当播放设备变化时，触发该事件。 |
| callback | (state: [ConnectionState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-e#connectionstate10), device: [OutputDeviceInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#outputdeviceinfo10)) =&gt; void | 是 | 回调函数，参数device是设备相关信息。          该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.on(
  'outputDeviceChange',
  (state: avSession.ConnectionState, device: avSession.OutputDeviceInfo) => {
    console.info(`on outputDeviceChange device : ${device}`);
  },
);
```


## on('commonCommand')10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

on(type: 'commonCommand', callback: (command :string, args:{[key: string]: Object}) => void): void

设置自定义控制命令变化的监听器。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'commonCommand'：当自定义控制命令变化时，触发该事件。 |
| callback | (command :string, args:{[key: string]: Object}) =&gt; void | 是 | 回调函数，command为变化的自定义控制命令名，args为自定义控制命令的参数，参数内容与[sendCommonCommand](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-avsessioncontroller#sendcommoncommand10)方法设置的参数内容完全一致。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
import { avSession } from '@kit.AVSessionKit';
@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
      Text(this.message)
      .onClick(()=>{
        let currentAVSession: avSession.AVSession | undefined = undefined;
        let tag = "createNewSession";
        let context: Context = this.getUIContext().getHostContext() as Context;

        avSession.createAVSession(context, tag, "audio", (data: avSession.AVSession) => {
          currentAVSession = data;
          if (currentAVSession !== undefined) {
            (currentAVSession as avSession.AVSession).on('commonCommand', (commonCommand, args) => {
              console.info(`OnCommonCommand, the command is ${commonCommand}, args: ${JSON.stringify(args)}`);
            });
          }
        });
      })
    }
    .width('100%')
    .height('100%')
  }
}
```


## off('play')10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

off(type: 'play', callback?: () => void): void

取消会话播放事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'play'。 |
| callback | () =&gt; void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。          该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.off('play');
```


## offPlay22+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

offPlay(callback?: Callback<CommandInfo>): void

取消会话播放事件监听。使用callback异步回调。

指定callback，取消对应监听；未指定callback，则取消所有事件监听。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;[CommandInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#commandinfo22)&gt; | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。          该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.offPlay();
```


## off('pause')10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

off(type: 'pause', callback?: () => void): void

取消会话暂停事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'pause'。 |
| callback | () =&gt; void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。          该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.off('pause');
```


## off('stop')10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

off(type: 'stop', callback?: () => void): void

取消会话停止事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'stop'。 |
| callback | () =&gt; void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。          该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.off('stop');
```


## off('playNext')10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

off(type: 'playNext', callback?: () => void): void

取消会话播放下一首事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是 'playNext'。 |
| callback | () =&gt; void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。          该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.off('playNext');
```


## offPlayNext22+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

offPlayNext(callback?: Callback<CommandInfo>): void

取消会话播放下一首事件监听。使用callback异步回调。

指定callback，取消对应监听；未指定callback，则取消所有事件监听。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;[CommandInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#commandinfo22)&gt; | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。          该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.offPlayNext();
```


## off('playPrevious')10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

off(type: 'playPrevious', callback?: () => void): void

取消会话播放上一首事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'playPrevious'。 |
| callback | () =&gt; void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。          该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.off('playPrevious');
```


## offPlayPrevious22+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

offPlayPrevious(callback?: Callback<CommandInfo>): void

取消会话播放上一首事件监听。使用callback异步回调。

指定callback，取消对应监听；未指定callback，则取消所有事件监听。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback&lt;[CommandInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#commandinfo22)&gt; | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。          该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.offPlayPrevious();
```


## off('fastForward')10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

off(type: 'fastForward', callback?: () => void): void

取消会话快进事件监听。指定callback，可取消对应监听；��指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'fastForward'。 |
| callback | () =&gt; void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。          该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.off('fastForward');
```


## offFastForward22+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

offFastForward(callback?: TwoParamCallback<number, CommandInfo>): void

取消会话快进事件监听。使用callback异步回调。

指定callback，取消对应监听；未指定callback，则取消所有事件监听。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | TwoParamCallback&lt;number, [CommandInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#commandinfo22)&gt; | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。          该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.offFastForward();
```


## off('rewind')10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

off(type: 'rewind', callback?: () => void): void

取消会话快退事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'rewind'。 |
| callback | () =&gt; void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。          该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.off('rewind');
```


## offRewind22+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

offRewind(callback?: TwoParamCallback<number, CommandInfo>): void

取消会话快退事件监听。使用callback异步回调。

指定callback，取消对应监听；未指定callback，则取消所有事件监听。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | TwoParamCallback&lt;number, [CommandInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#commandinfo22)&gt; | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。          该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.offRewind();
```


## off('seek')10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

off(type: 'seek', callback?: (time: number) => void): void

取消跳转节点事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持关闭事件'seek'。 |
| callback | (time: number) =&gt; void | 否 | 回调函数，参数time是时间节点，单位为毫秒。          当监听事件取消成功，err为undefined，否则返回错误对象。          该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.off('seek');
```


## off('setSpeed')10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

off(type: 'setSpeed', callback?: (speed: number) => void): void

取消播放速率变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持关闭事件'setSpeed'。 |
| callback | (speed: number) =&gt; void | 否 | 回调函数，参数speed是播放倍速。          当监听事件取消成功，err为undefined，否则返回错误对象。          该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.off('setSpeed');
```


## off('setLoopMode')10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

off(type: 'setLoopMode', callback?: (mode: LoopMode) => void): void

取消循环模式变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持关闭事件'setLoopMode'。 |
| callback | (mode: [LoopMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-e#loopmode10)) =&gt; void | 否 | 回调函数，参数mode是循环模式。          - 当监听事件取消成功，err为undefined，否则返回错误对象。          - 该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.off('setLoopMode');
```


## off('setTargetLoopMode')18+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

off(type: 'setTargetLoopMode', callback?: Callback<LoopMode>): void

取消目标循环模式变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持关闭事件'setTargetLoopMode'。 |
| callback | Callback&lt;[LoopMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-e#loopmode10)&gt; | 否 | 回调函数，参数表示目标循环模式。          - 当监听事件取消成功，err为undefined，否则返回错误对象。          - 该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.off('setTargetLoopMode');
```


## off('toggleFavorite')10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

off(type: 'toggleFavorite', callback?: (assetId: string) => void): void

取消是否收藏的事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持关闭事件'toggleFavorite'。 |
| callback | (assetId: string) =&gt; void | 否 | 回调函数，参数assetId是媒体ID。          当监听事件取消成功，err为undefined，否则返回错误对象。          该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.off('toggleFavorite');
```


## off('skipToQueueItem')10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

off(type: 'skipToQueueItem', callback?: (itemId: number) => void): void

取消播放列表单项选中的事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持关闭事件'skipToQueueItem'。 |
| callback | (itemId: number) =&gt; void | 否 | 回调函数，参数itemId是播放列表单项ID。          当监听事件取消成功，err为undefined，否则返回错误对象。          该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.off('skipToQueueItem');
```


## off('handleKeyEvent')10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

off(type: 'handleKeyEvent', callback?: (event: KeyEvent) => void): void

取消按键事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持关闭事件'handleKeyEvent'。 |
| callback | (event: [KeyEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-keyevent)) =&gt; void | 否 | 回调函数，参数event是按键事件。          当监听事件取消成功，err为undefined，否则返回错误对象。          该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.off('handleKeyEvent');
```


## off('outputDeviceChange')10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

off(type: 'outputDeviceChange', callback?: (state: ConnectionState, device: OutputDeviceInfo) => void): void

取消播放设备变化的事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持关闭事件'outputDeviceChange'。 |
| callback | (state: [ConnectionState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-e#connectionstate10), device: [OutputDeviceInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#outputdeviceinfo10)) =&gt; void | 否 | 回调函数，参数device是设备相关信息。          当监听事件取消成功，err为undefined，否则返回错误对象。          该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.off('outputDeviceChange');
```


## off('commonCommand')10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

off(type: 'commonCommand', callback?: (command: string, args:{[key: string]: Object}) => void): void

取消自定义控制命令的变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'commonCommand'。 |
| callback | (command: string, args:{[key: string]: Object}) =&gt; void | 否 | 回调函数，参数command是变化的自定义控制命令名，args为自定义控制命令的参数。          该参数为可选参数，若不填写该参数，则认为取消所有对command事件的监听。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.off('commonCommand');
```


## on('answer')11+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

on(type: 'answer', callback: Callback<void>): void

设置通话接听的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'answer'：当通话接听时，触发该事件。 |
| callback | Callback&lt;void&gt; | 是 | 回调函数。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.on('answer', () => {
  console.info('on call answer');
});
```


## off('answer')11+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

off(type: 'answer', callback?: Callback<void>): void

取消通话接听事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'answer'。 |
| callback | Callback&lt;void&gt; | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。          该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.off('answer');
```


## on('hangUp')11+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

on(type: 'hangUp', callback: Callback<void>): void

设置通话挂断的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'hangUp'：当通话挂断时，触发该事件。 |
| callback | Callback&lt;void&gt; | 是 | 回调函数。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.on('hangUp', () => {
  console.info('on call hangUp');
});
```


## off('hangUp')11+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

off(type: 'hangUp', callback?: Callback<void>): void

取消通话挂断事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'hangUp'。 |
| callback | Callback&lt;void&gt; | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。          该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.off('hangUp');
```


## on('toggleCallMute')11+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

on(type: 'toggleCallMute', callback: Callback<void>): void

设置通话静音的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'toggleCallMute'：当通话静音或解除静音时，触发该事件。 |
| callback | Callback&lt;void&gt; | 是 | 回调函数。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.on('toggleCallMute', () => {
  console.info('on call toggleCallMute');
});
```


## off('toggleCallMute')11+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

off(type: 'toggleCallMute', callback?: Callback<void>): void

取消通话静音事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'toggleCallMute'。 |
| callback | Callback&lt;void&gt; | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。          该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.off('toggleCallMute');
```


## on('castDisplayChange')12+
**支持设备：** Phone / Tablet

on(type: 'castDisplayChange', callback: Callback<CastDisplayInfo>): void

设置扩展屏投播显示设备变化的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'castDisplayChange'：当扩展屏投播显示设备变化时触发事件。 |
| callback | Callback&lt;[CastDisplayInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#castdisplayinfo12)&gt; | 是 | 回调函数。参数是扩展屏投播显示设备信息。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
let castDisplay: avSession.CastDisplayInfo;
currentAVSession.on(
  'castDisplayChange',
  (display: avSession.CastDisplayInfo) => {
    if (display.state === avSession.CastDisplayState.STATE_ON) {
      castDisplay = display;
      console.info(`Succeeded in castDisplayChange display : ${display.id} ON`);
    } else if (display.state === avSession.CastDisplayState.STATE_OFF) {
      console.info(
        `Succeeded in castDisplayChange display : ${display.id} OFF`,
      );
    }
  },
);
```


## off('castDisplayChange')12+
**支持设备：** Phone / Tablet

off(type: 'castDisplayChange', callback?: Callback<CastDisplayInfo>): void

取消扩展屏投播显示设备变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'castDisplayChange'。 |
| callback | Callback&lt;[CastDisplayInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#castdisplayinfo12)&gt; | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.off('castDisplayChange');
```


## stopCasting10+
**支持设备：** Phone / PC/2in1 / Tablet / TV

stopCasting(callback: AsyncCallback<void>): void

结束投播。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback&lt;void&gt; | 是 | 回调函数��当命令发送成功，err为undefined，否则返回错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600109 | The remote connection is not established. |


**示例：**


```ts
currentAVSession.stopCasting(() => {
  console.info('Succeeded in stopping casting.');
});
```


## stopCasting10+
**支持设备：** Phone / PC/2in1 / Tablet / TV

stopCasting(): Promise<void>

结束投播。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。当成功结束投播，无返回结果，否则返回错误对象。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600109 | The remote connection is not established. |


**示例：**


```ts
currentAVSession.stopCasting().then(() => {
  console.info('Succeeded in stopping casting.');
});
```


## getOutputDeviceSync10+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getOutputDeviceSync(): OutputDeviceInfo

使用同步方法获取当前输出设备信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**


| 类型 | 说明 |
| --- | --- |
| [OutputDeviceInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#outputdeviceinfo10) | 当前输出设备信息。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
let currentOutputDevice: avSession.OutputDeviceInfo =
  currentAVSession.getOutputDeviceSync();
```


## getAllCastDisplays12+
**支持设备：** Phone / Tablet

getAllCastDisplays(): Promise<Array<CastDisplayInfo>>

获取当前系统中所有支持扩展屏投播的显示设备。通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;[CastDisplayInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#castdisplayinfo12)&gt;&gt; | Promise对象，返回当前系统中所有支持扩展屏投播的显示设备。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
let castDisplay: avSession.CastDisplayInfo;
currentAVSession
  .getAllCastDisplays()
  .then((data: Array<avSession.CastDisplayInfo>) => {
    if (data.length >= 1) {
      castDisplay = data[0];
    }
  });
```


## on('playFromAssetId')(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

on(type:'playFromAssetId', callback: (assetId: number) => void): void

设置媒体id播放监听事件。


> [!NOTE]
> 从 API version 11 开始支持，从 API version 20 开始废弃。建议使用[on('playWithAssetId')](#onplaywithassetid20)设置媒体id播放监听事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件是'playFromAssetId'，当媒体id播放时，触发该事件回调。 |
| callback | (assetId: number) =&gt; void | 是 | 回调函数。参数assetId是媒体id。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.on('playFromAssetId', (assetId: number) => {
  console.info('on playFromAssetId entry');
});
```


## off('playFromAssetId')(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

off(type: 'playFromAssetId', callback?: (assetId: number) => void): void

取消媒体id播放事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。


> [!NOTE]
> 从 API version 11 开始支持，从 API version 20 开始废弃。建议使用[off('playWithAssetId')](#offplaywithassetid20)取消媒体id播放事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'playFromAssetId'。 |
| callback | (assetId: number) =&gt; void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。          该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。参数assetId是媒体id。 |


**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.off('playFromAssetId');
```


## on('customDataChange')20+
**支持设备：** Phone / PC/2in1 / Tablet / TV

on(type: 'customDataChange', callback: Callback<Record<string, Object>>): void

注册从远程设备发送的自定义数据的监听器。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'customDataChange'，当媒体提供方发送自定义数据时，触发该事件。 |
| callback | Callback&lt;Record&lt;string, Object&gt;&gt; | 是 | 回调函数，用于接收自定义数据。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.on('customDataChange', (callback) => {
  console.info(
    `Caught customDataChange event,the new callback is: ${JSON.stringify(callback)}`,
  );
});
```


## off('customDataChange')20+
**支持设备：** Phone / PC/2in1 / Tablet / TV

off(type: 'customDataChange', callback?: Callback<Record<string, Object>>): void

取消自定义数据监听。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持的事件是'customDataChange'。 |
| callback | Callback&lt;Record&lt;string, Object&gt;&gt; | 否 | 注册监听事件时的回调函数。该参数为可选参数，若不填写该参数，则认为取消会话所有与此事件相关的监听。 |


**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。


| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |


**示例：**


```ts
currentAVSession.off('customDataChange');
```
