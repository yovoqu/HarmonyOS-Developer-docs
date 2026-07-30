# 使用AudioHaptic开发音振协同播放功能(ArkTS)

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-audiohaptic-for-playback

从API版本11开始支持音振协同播放。

AudioHaptic提供音频与振动协同播放及管理的方法，适用于需要在播放音频时同步发起振动的场景，如来电铃声随振、键盘按键反馈、消息通知反馈等。


#### 开发指导

使用AudioHaptic开发音频与振动协同播放功能，涉及到音频及振动资源的管理、音频时延模式及音频流使用类型的配置、音振播放器的创建及管理等。本文将以一次音振协同播放的过程为例，讲解如何使用AudioHaptic开发音振协同播放功能，建议结合[audioHaptic](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-audiohaptic)API接口文档一起阅读。



#### 权限申请

如果应用创建的AudioHapticPlayer需要触发振动，则需要校验应用是否拥有该权限：ohos.permission.VIBRATE。
1. 请参考[声明权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions)指导，声明该振动权限。
2. 由于该权限为用户授予类权限，需要拉起用户授权弹窗让用户使用时授权，否则无法获取该权限，代码开发请参考[向用户申请授权](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/request-user-authorization)。



#### 开发步骤及注意事项
1. 获取音振管理器实例，并注册音频及振动资源，单个应用最多支持同时注册128个资源，播放器支持的音频和振动资源格式，请查看[registerSource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-audiohaptic#registersource)文档中的描述。开发者可通过如下两种方式注册资源：

  
方式1：使用[registerSource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-audiohaptic#registersource)接口，通过文件URI来注册资源。
2. 方式2（推荐）：从API版本20开始，支持使用[registerSourceFromFd](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-audiohaptic#registersourcefromfd20)接口，通过文件描述符来注册资源。
3. 设置音振播放器音频时延模式和音频流使用类型，具体作用和类型可以查看[setAudioLatencyMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-audiohaptic#setaudiolatencymode)和[setStreamUsage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-audiohaptic#setstreamusage)接口的文档，推荐短信、通知音等短提示音搭配FAST模式，来电铃声等长铃声搭配NORMAL模式。

  
```ArkTS
let latencyMode: audioHaptic.AudioLatencyMode = audioHaptic.AudioLatencyMode.AUDIO_LATENCY_MODE_NORMAL;
audioHapticManagerInstance.setAudioLatencyMode(idForFd, latencyMode);

let usage: audio.StreamUsage = audio.StreamUsage.STREAM_USAGE_NOTIFICATION;
audioHapticManagerInstance.setStreamUsage(idForFd, usage);
```

4. 调用[createPlayer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-audiohaptic#createplayer)方法，创建AudioHapticPlayer实例，其中options参数控制是否将音频静音，是否禁止振动。参数为空时，播放器默认开启音频，允许振动。

  
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

7. 应用在使用完音振协同播放器后应主动调用[release](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-audiohaptic#release)方法，释放AudioHapticPlayer实例，防止播放器实例长期占用系统音振资源，产生严重的内存与系统资源泄漏，从而导致应用后续无法再创建音振协同播放器。

  
```ArkTS
audioHapticPlayer.release().then(() => {
  console.info('Succeeded in releasing audio haptic player.');
  // ...
}).catch((err: BusinessError) => {
  console.error(`Failed to release audio haptic player. Code: ${err.code}, message: ${err.message}`);
  // ...
});
```

8. 当资源不再使用时，应用必须调用[unregisterSource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-audiohaptic#unregistersource)方法，将已注册的音频及振动资源移除注册，若长期堆积未注销的无效资源，会快速耗尽应用128个资源注册配额，直接导致后续所有音振资源注册失败、播放器无法创建，音振协同播放功能不可用，同时会引发持续性资源泄漏问题。

  
```ArkTS
audioHapticManagerInstance.unregisterSource(idForFd).then(() => {
  console.info('Succeeded in unregistering source.');
  // ...
}).catch((err: BusinessError) => {
  console.error(`Failed to unregister source. Code: ${err.code}, message: ${err.message}`);
  // ...
});
```
