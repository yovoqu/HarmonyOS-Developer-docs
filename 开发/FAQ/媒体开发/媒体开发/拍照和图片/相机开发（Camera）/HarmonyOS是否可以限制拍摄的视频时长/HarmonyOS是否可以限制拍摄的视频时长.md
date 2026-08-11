# HarmonyOS是否可以限制拍摄的视频时长

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-36

#### 问题现象

业务场景：朋友圈发送视频，一般限制大小是15s。所以是否可以通过参数来控制拍摄视频的最大时长，比如30秒或者60秒等？
 
 

#### 背景知识

- 系统相机开发可参考[通过系统相机拍照和录像](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-picker)，开发者调用picker方法会直接跳转到系统相机页面，功能完备齐全。
- 自定义相机开发需要开发者自行开发相机[拍照](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-shooting-case)与[录像](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-recording-case)功能。

 
 

#### 解决方案

- 使用[系统相机](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-camerapicker)时，可以通过相机配置选项[PickerProfiles](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-camerapicker#pickerprofile)中的videoDuration设置录制的最大时长，默认单位是秒。
```text
let <span style="color: rgb(255,255,255);">pickerProfile</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">picker</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">PickerProfile </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">cameraPosition</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">camera</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">CameraPosition</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">CAMERA_POSITION_BACK</span><span style="color: rgb(181,106,1);">,</span>
 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">录制的最大时长（单位：秒）</span></em>
  <span style="color: rgb(255,255,255);">videoDuration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">5</span>
<span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
let <span style="color: rgb(255,255,255);">pickerResult</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">picker</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">PickerResult </span><span style="color: rgb(181,106,1);">= </span>await <span style="color: rgb(255,255,255);">picker</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pick</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,0,170);">[</span><span style="color: rgb(255,255,255);">picker</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">PickerMediaType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">PHOTO</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">picker</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">PickerMediaType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">VIDEO</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">pickerProfile</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
```

- 使用自定义相机[录制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-recording-case)视频，可以通过配置音视频参数[AVRecorderConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-i#avrecorderconfig9)中的maxDuration设置录制的最大时长，单位为秒。
```text
let <span style="color: rgb(255,255,255);">aVRecorderConfig</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">media</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">AVRecorderConfig </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">audioSourceType</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">media</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">AudioSourceType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">AUDIO_SOURCE_TYPE_MIC</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,255,255);">videoSourceType</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">media</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">VideoSourceType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">VIDEO_SOURCE_TYPE_SURFACE_YUV</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,255,255);">profile</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">aVRecorderProfile</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,255,255);">url</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">`fd://</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">file</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">fd</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">文件需先由调用者创建，赋予读写权限，将文件</span><span style="color: rgb(128,128,128);">fd</span><span style="color: rgb(128,128,128);">传给此参数，</span><span style="color: rgb(128,128,128);">eg.fd://45--file:///data/media/01.mp4</span></em>
  <span style="color: rgb(255,255,255);">metadata</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">avMetadata</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,255,255);">maxDuration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">5</span>
<span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
```
