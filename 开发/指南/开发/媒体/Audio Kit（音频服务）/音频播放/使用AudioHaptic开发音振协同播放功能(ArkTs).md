# 使用AudioHaptic开发音振协同播放功能(ArkTs)

更新时间：2026-07-17 09:35:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-audiohaptic-for-playback

AudioHaptic提供音频与振动协同播放及管理的方法，适用于需要在播放音频时同步发起振动的场景，如来电铃声随振、键盘按键反馈、消息通知反馈等。


#### 开发指导

使用AudioHaptic播放音频并同步开启振动，涉及到音频及振动资源的管理、音频时延模式及音频流使用类型的配置、音振播放器的创建及管理等。本开发指导将以一次音振协同播放的过程为例，向开发者讲解如何使用AudioHaptic进行音振协同播放，建议配合[audioHaptic](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-audiohaptic)的API说明阅读。



#### 权限申请

如果应用创建的AudioHapticPlayer需要触发振动，则需要校验应用是否拥有该权限：ohos.permission.VIBRATE。
1. [声明权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions)。
2. [向用户申请授权](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/request-user-authorization)。



#### 开发步骤及注意事项

以下各步骤示例为片段代码，可通过示例代码右下方链接获取[完整示例](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/Audio/AudioRendererSampleJS)。
1. 获取音振管理器实例，并注册音频及振动资源，资源支持情况可以查看[AudioHapticManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-audiohaptic#audiohapticmanager)。

  
> [!NOTE]
> 开发者可通过如下两种方式注册资源： 方式1：使用 registerSource 接口，通过文件URI来注册资源。 方式2（推荐）：从API version 20开始，支持使用 registerSourceFromFd 接口，通过文件描述符来注册资源，更便于开发者使用。


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/lxCUx5KTQ0SLO-9xCf1nLQ/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260723T012151Z&HW-CC-Expire=86400&HW-CC-Sign=169DDE39AECBDCD9945781135DCD4C3B98122823F8CE2D9A379C49B88117D988)
 

  
单个应用最多支持同时注册128个资源，超过之后将会注册失败，返回注册的资源ID为负数。
2. 推荐应用合理控制注册资源数量，对于不再需要使用的资源，建议及时取消注册。
3. 设置音振播放器参数，各参数作用可以查看[AudioHapticManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-audiohaptic#audiohapticmanager)。

  
```ArkTS
let latencyMode: audioHaptic.AudioLatencyMode = audioHaptic.AudioLatencyMode.AUDIO_LATENCY_MODE_NORMAL;
audioHapticManagerInstance.setAudioLatencyMode(idForFd, latencyMode);

let usage: audio.StreamUsage = audio.StreamUsage.STREAM_USAGE_NOTIFICATION;
audioHapticManagerInstance.setStreamUsage(idForFd, usage);
```

4. 调用[createPlayer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-audiohaptic#createplayer)方法，创建AudioHapticPlayer实例。

  
```ArkTS
let options: audioHaptic.AudioHapticPlayerOptions = {muteAudio: false, muteHaptics: false};
let audioHapticPlayer: audioHaptic.AudioHapticPlayer | undefined = undefined;
// ...
  audioHapticManagerInstance.createPlayer(idForFd, options).then((value: audioHaptic.AudioHapticPlayer) => {
    console.info('Succeeded in creating player.');
    audioHapticPlayer = value;
    // ...
  }).catch((err: BusinessError) => {
    console.error(`Failed to create player. Code: ${err.code}, message: ${err.message}`);
    // ...
  });
```

5. 调用[start](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-audiohaptic#start)方法，开启音频播放并同步开启振动。

  
```ArkTS
audioHapticPlayer.start().then(() => {
  console.info('Succeeded in starting audio haptic player.');
  // ...
}).catch((err: BusinessError) => {
  console.error(`Failed to start audio haptic player. Code: ${err.code}, message: ${err.message}`);
  // ...
});
```

6. 调用[stop](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-audiohaptic#stop)方法，停止音频播放并同步停止振动。

  
```ArkTS
audioHapticPlayer.stop().then(() => {
  console.info('Succeeded in stopping audio haptic player.');
  // ...
}).catch((err: BusinessError) => {
  console.error(`Failed to stop audio haptic player. Code: ${err.code}, message: ${err.message}`);
  // ...
});
```

7. 调用[release](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-audiohaptic#release)方法，释放AudioHapticPlayer实例。

  
```ArkTS
audioHapticPlayer.release().then(() => {
  console.info('Succeeded in releasing audio haptic player.');
  // ...
}).catch((err: BusinessError) => {
  console.error(`Failed to release audio haptic player. Code: ${err.code}, message: ${err.message}`);
  // ...
});
```

8. 调用[unregisterSource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-audiohaptic#unregistersource)方法，将已注册的音频及振动资源移除注册。

  
```ArkTS
// 对于不再需要使用的资源，建议应用及时取消注册，避免出现资源泄漏或资源数量超上限等问题。
audioHapticManagerInstance.unregisterSource(idForFd).then(() => {
  console.info('Succeeded in unregistering source.');
  // ...
}).catch((err: BusinessError) => {
  console.error(`Failed to unregister source. Code: ${err.code}, message: ${err.message}`);
  // ...
});
```
