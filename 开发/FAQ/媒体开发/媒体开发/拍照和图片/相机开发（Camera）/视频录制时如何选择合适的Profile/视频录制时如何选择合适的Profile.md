# 视频录制时如何选择合适的Profile

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-59

#### 问题现象

在视频录制的开发过程中，该如何选择合适的Profile？VideoOutput.Profile跟AVRecorderProfile之间有什么关系？
 
 

#### 背景知识

- [VideoProfile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-i#videoprofile)：视频配置信息项，继承[Profile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-i#profile)。可通过[getSupportedOutputCapability](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-cameramanager#getsupportedoutputcapability11)接口查询到当前设备支持的视频规格，规格参数中包括视频帧率范围、输出格式、分辨率宽高。
- [AVRecorderProfile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-i#avrecorderprofile9)：音视频录制的配置文件。
- [AVRecorderConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-i#avrecorderconfig9)：表示音视频录制的参数设置。通过audioSourceType和videoSourceType区分纯音频录制、纯视频录制或音视频录制。纯音频录制时，仅需要设置audioSourceType；纯视频录制时，仅需要设置videoSourceType；音视频录制时，audioSourceType和videoSourceType均需要设置。

 
 

#### 解决方案
1. **如何选择合适的Profile**首先通过getSupportedOutputCapability接口查询当前设备支持的视频输出规格，然后再根据分辨率、输出格式、帧率等维度出发，从中挑选符合业务需求的规格去创建VideoOutput和AVRecorder。

  完整的示例代码可参考[录像实践(ArkTS)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-recording-case)或[录像实践(C/C++)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-recording-case)。
2. **VideoOutput.Profile与AVRecorderProfile之间的关联与限制**VideoOutput的配置参数与AVRecorder配置参数之间的关联和限制主要有如下几点：

  
VideoOutput的分辨率要与AVRecorderProfile中的分辨率一致。
3. AVRecorderProfile配置中的帧率不能超出VideoOutput的帧率规格的限制。
4. 如果需要录制HDR视频，则VideoOutput的输出格式要选择camera.CameraFormat.CAMERA_FORMAT_YCBCR_P010或者camera.CameraFormat.CAMERA_FORMAT_YCRCB_P010，并且AVRecorderProfile配置参数中的isHdr需要设置为true。
 
 

#### 常见FAQ

Q：Mate X6视频录制失败，界面显示黑屏，应该怎么解决？
 
A：代码中下发的视频帧率为60，但是X6并不支持这个帧率规格。建议使用getSupportedOutputCapability接口查询当前设备支持的视频规格，并从中选取支持的规格去实现业务需求。
 
Q：Mate70 Pro升级系统版本后，视频录制时出现黑屏，应该怎么解决？
 
A：预览流与视频流的分辨率不一致导致，请至少保持两边分辨率宽高比一致。
 
Q：视频录制分辨率为640*480时录制有问题，录制分辨率为1280*720可以正常录制，这是为什么？
 
A：录制的分辨率宽高比要与预览流的分辨率宽高比一致。
