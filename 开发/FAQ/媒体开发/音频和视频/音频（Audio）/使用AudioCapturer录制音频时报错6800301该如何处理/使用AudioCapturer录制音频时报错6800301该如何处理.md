# 使用AudioCapturer录制音频时报错6800301该如何处理

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-34

#### 问题现象

使用AudioCapturer录制音频时会发生报错，错误码为6800301，错误示例代码如下：
 
```text
Create AudioCapturer failed, error: {"code":6800301}
```
 
 

#### 背景知识

[AudioCapturer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiocapturer)：用于音频输入的API，仅支持PCM格式，需要应用持续读取音频数据进行工作。使用AudioCapturer录制音频涉及到AudioCapturer实例的创建、音频采集参数的配置、采集的开始与停止、资源的释放等。可以使用on('stateChange')方法可以监听AudioCapturer的状态变化，每个状态对应值与说明见[AudioState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiostate8)。
 
 

#### 问题定位

错误码6800301是系统内部错误，包含系统处理异常、权限校验异常、参数校验异常、状态检查异常以及焦点抢占失败等。
 
- 可以尝试重启实例来排除系统服务重启、跨进程调用异常等情况。
- 如果重启实例无效，则需要检查音频源类型和权限设置。当设置Mic音频源（即[SourceType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#sourcetype8)为SOURCE_TYPE_MIC、SOURCE_TYPE_VOICE_RECOGNITION、SOURCE_TYPE_VOICE_COMMUNICATION、SOURCE_TYPE_VOICE_MESSAGE）时，需要申请麦克风权限，否则会涉及权限校验异常造成系统报错。
- 检查音频流信息模块的参数配置是否正确，错误的参数会导致校验异常造成系统报错。
- 检查是否正确的进行初始化，初始化应该在申请权限之后，否则会涉及状态检查异常造成系统报错。
- 如果和其他音频开发功能同时进行时，可能会涉及焦点抢占问题，造成录制过程中断而报错。

 
 

#### 分析结论

如下图所示，如果权限没有正确申请，则会导致权限校验异常造成报错，这里取消了麦克风权限导致报错：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/Aq6YUIQ7STuNif_2EWKDzw/zh-cn_image_0000002658791891.png?HW-CC-KV=V1&HW-CC-Date=20260730T072623Z&HW-CC-Expire=86400&HW-CC-Sign=533EC26C1C9BA95AE9C93488EBEC9ED4D1FBD77D32CBE5E4B26924AEC06920E9)

 
如下图所示，如果参数配置不正确，则会导致参数校验异常造成报错，音频采集参数的详细信息可以查看[AudioStreamInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i#audiostreaminfo8)，这里配置了错误的采样率导致报错：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/4hCixKyCT8-aDwJBtk_sPw/zh-cn_image_0000002628552524.png?HW-CC-KV=V1&HW-CC-Date=20260730T072623Z&HW-CC-Expire=86400&HW-CC-Sign=6764DD463AD850A090603D8655E5F9DB18C70837E03CE28105DCC685A257D85E)

 
如下图所示，如果没有进行正确的初始化，则会导致状态检查异常造成系统报错，这里初始化步骤在申请权限之前导致报错：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/j3Cml7jXT-C1kR2dpG0-oA/zh-cn_image_0000002658911835.png?HW-CC-KV=V1&HW-CC-Date=20260730T072623Z&HW-CC-Expire=86400&HW-CC-Sign=F1AAFF00B6B5D9FEB68422BD0F0C054AF186CCA249C901C013DB06A5D16E17A5)

 
 

#### 修改建议

- **申请麦克风权限**：申请麦克风权限方式参考[向用户申请授权](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/request-user-authorization)，如果用户拒绝了权限申请，则需要去设置里另外开启，另外在module.json5文件里也要申请相关权限。
- **配置正确的参数**：配置音频采集参数时应当注意相应参数范围，音频采集参数的详细信息可以查看[AudioStreamInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i#audiostreaminfo8)。
- **正确的初始化**：初始化方法应该在申请权限之后，具体代码逻辑可以参考[AudioCapturer开发步骤](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-audiocapturer-for-recording#开发步骤及注意事项)。
- **处理音频焦点变化**：音频录制过程中，可能会涉及焦点被其他应用程序抢占，导致录制进程被打断，具体处理方法可以参考[音频焦点的管理解决方案](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-audio-focus-management)。

 
完整示例代码可以参考[AudioCapturer录制音频完整示例](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-audiocapturer-for-recording#完整示例)。
 
 

#### 常见FAQ

Q：AudioCapturer录制音频过程中，麦克风权限被禁止，此时AudioState状态为多少？
 
A：此时AudioState状态是STATE_RUNNING，但是后续录到的是静音数据。麦克风权限影响的是录到的数据是不是静音数据，不会影响能不能录到数据。
