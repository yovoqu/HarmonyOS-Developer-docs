# 会话管理(ArkTS)

更新时间：2026-03-23 08:10:50

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-session-management

相机使用预览、拍照、录像、元数据功能前，均需要创建相机会话。

在会话中，可以完成以下功能：


完成会话配置后，应用提交和开启会话，可以开始调用相机相关功能。


## 开发步骤

导入相关接口，导入方法如下。
```text
import { camera } from '@kit.CameraKit';
import { BusinessError } from '@kit.BasicServicesKit';
```

调用[cameraManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-cameramanager)中的[createSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-cameramanager#createsession11)方法创建一个会话。
```text
// 此处以videoSession为例。
function getSession(cameraManager: camera.CameraManager): camera.VideoSession | undefined {
  let videoSession: camera.VideoSession | undefined = undefined;
  try {
    videoSession = cameraManager.createSession(camera.SceneMode.NORMAL_VIDEO) as camera.VideoSession;
  } catch (error) {
    let err = error as BusinessError;
    console.error(`Failed to create the session instance. error: ${err.code}`);
  }
  return videoSession;
}
```

调用[VideoSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-videosession)中的[beginConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-session#beginconfig11)方法配置会话。
```text
function beginConfig(videoSession: camera.VideoSession): void {
  try {
    videoSession.beginConfig();
  } catch (error) {
    let err = error as BusinessError;
    console.error(`Failed to beginConfig. error: ${err.code}`);
  }
}
```

使能。向会话中添加相机的输入流和输出流，调用[addInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-session#addinput11)添加相机的输入流；调用[addOutput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-session#addoutput11)添加相机的输出流。以下示例代码以添加预览流previewOutput和拍照流photoOutput为例，即当前模式支持拍照和预览。 调用VideoSession中的[commitConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-session#commitconfig11)和[start](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-session#start11)方法提交相关配置，并启动会话。
> [!NOTE]
> 在调用addOutput添加相机的输出流前，可通过canAddOutput判断当前相机输出流是否可以添加到session中。 相机输入流cameraInput创建流程请参考设备输入，相机预览输出流previewOutput和拍照输出流photoOutput创建流程请分别参考预览和拍照。


```text
async function startSession(videoSession: camera.VideoSession, cameraInput: camera.CameraInput, previewOutput: camera.PreviewOutput, photoOutput: camera.PhotoOutput): Promise {
  try {
    videoSession.addInput(cameraInput);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`Failed to addInput. error: ${err.code}`);
  }
  let canAddPreviewOutput : boolean = false;
  try {
    canAddPreviewOutput = videoSession.canAddOutput(previewOutput);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`Failed to add previewOutput. error: ${err.code}`);
  }
  if (!canAddPreviewOutput) {
    console.error(`Failed to add preview output.`);
    return;
  }
  try {
    videoSession.addOutput(previewOutput);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`Failed to add previewOutput. error: ${err.code}`);
  }
  let canAddPhotoOutput : boolean = false
  try {
    canAddPhotoOutput = videoSession.canAddOutput(photoOutput);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`Failed to add photoOutput error: ${err.code}`);
  }
  if (!canAddPhotoOutput) {
    console.error(`Failed to add photo output.`);
    return;
  }
  try {
    videoSession.addOutput(photoOutput);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`Failed to add photoOutput. error: ${err.code}`);
  }
  try {
    await videoSession.commitConfig();
  } catch (error) {
    let err = error as BusinessError;
    console.error(`Failed to commitConfig. error: ${err.code}`);
   return;
  }

  try {
    await videoSession.start();
  } catch (error) {
    let err = error as BusinessError;
    console.error(`Failed to start. error: ${err.code}`);
  }
}
```

会话控制。调用VideoSession中的[stop](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-session#stop11)方法可以停止当前会话。调用[removeOutput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-session#removeoutput11)和[addOutput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-session#addoutput11)方法可以完成会话切换控制。以下示例代码以移除拍照流photoOutput，添加视频流videoOutput为例，完成了拍照到录像的切换。
```text
async function switchOutput(videoSession: camera.VideoSession, videoOutput: camera.VideoOutput, photoOutput: camera.PhotoOutput): Promise {
  try {
    await videoSession.stop();
  } catch (error) {
    let err = error as BusinessError;
    console.error(`Failed to stop. error: ${err.code}`);
  }

  try {
    videoSession.beginConfig();
  } catch (error) {
    let err = error as BusinessError;
    console.error(`Failed to beginConfig. error: ${err.code}`);
  }
  // 从会话中移除拍照输出流。
  try {
    videoSession.removeOutput(photoOutput);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`Failed to remove photoOutput. error: ${err.code}`);
  }
  try {
    videoSession.canAddOutput(videoOutput);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`Failed to add videoOutput error: ${err.code}`);
  }
  // 向会话中添加视频输出流。
  try {
    videoSession.addOutput(videoOutput);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`Failed to add videoOutput. error: ${err.code}`);
  }
  try {
    await videoSession.commitConfig();
  } catch (error) {
    let err = error as BusinessError;
    console.error(`Failed to commitConfig. error: ${err.code}`);
  }

  try {
    await videoSession.start();
  } catch (error) {
    let err = error as BusinessError;
    console.error(`Failed to start. error: ${err.code}`);
  }
}
```
