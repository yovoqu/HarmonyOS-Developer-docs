# Camera Kit

更新时间：2026-06-27 01:41:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-camerakit-7001

## Camera Kit
 
 
| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：CameraManager； API声明：setTorchMode(mode: TorchMode): void; 差异内容：NA | 类名：CameraManager； API声明：setTorchMode(mode: TorchMode): void; 差异内容：7400101 | api/@ohos.multimedia.camera.d.ts |
| 新增错误码 | 类名：Zoom； API声明：setSmoothZoom(targetRatio: number, mode?: SmoothZoomMode): void; 差异内容：NA | 类名：Zoom； API声明：setSmoothZoom(targetRatio: number, mode?: SmoothZoomMode): void; 差异内容：7400103 | api/@ohos.multimedia.camera.d.ts |
| 新增错误码 | 类名：ColorManagementQuery； API声明：getSupportedColorSpaces(): Array<colorSpaceManager.ColorSpace>; 差异内容：NA | 类名：ColorManagementQuery； API声明：getSupportedColorSpaces(): Array<colorSpaceManager.ColorSpace>; 差异内容：7400103 | api/@ohos.multimedia.camera.d.ts |
| 新增错误码 | 类名：AutoDeviceSwitchQuery； API声明：isAutoDeviceSwitchSupported(): boolean; 差异内容：NA | 类名：AutoDeviceSwitchQuery； API声明：isAutoDeviceSwitchSupported(): boolean; 差异内容：7400103 | api/@ohos.multimedia.camera.d.ts |
| 新增错误码 | 类名：Session； API声明：addInput(cameraInput: CameraInput): void; 差异内容：NA | 类名：Session； API声明：addInput(cameraInput: CameraInput): void; 差异内容：7400103 | api/@ohos.multimedia.camera.d.ts |
| 新增错误码 | 类名：Session； API声明：removeInput(cameraInput: CameraInput): void; 差异内容：NA | 类名：Session； API声明：removeInput(cameraInput: CameraInput): void; 差异内容：7400103 | api/@ohos.multimedia.camera.d.ts |
| 新增错误码 | 类名：Session； API声明：addOutput(cameraOutput: CameraOutput): void; 差异内容：NA | 类名：Session； API声明：addOutput(cameraOutput: CameraOutput): void; 差异内容：7400103 | api/@ohos.multimedia.camera.d.ts |
| 新增错误码 | 类名：Session； API声明：removeOutput(cameraOutput: CameraOutput): void; 差异内容：NA | 类名：Session； API声明：removeOutput(cameraOutput: CameraOutput): void; 差异内容：7400103 | api/@ohos.multimedia.camera.d.ts |
| 新增错误码 | 类名：SecureSession； API声明：addSecureOutput(previewOutput: PreviewOutput): void; 差异内容：NA | 类名：SecureSession； API声明：addSecureOutput(previewOutput: PreviewOutput): void; 差异内容：7400103 | api/@ohos.multimedia.camera.d.ts |
| 新增错误码 | 类名：PreviewOutput； API声明：getPreviewRotation(displayRotation?: number): ImageRotation; 差异内容：NA | 类名：PreviewOutput； API声明：getPreviewRotation(displayRotation?: number): ImageRotation; 差异内容：7400101 | api/@ohos.multimedia.camera.d.ts |
| 新增错误码 | 类名：PhotoOutput； API声明：getPhotoRotation(deviceDegree?: number): ImageRotation; 差异内容：NA | 类名：PhotoOutput； API声明：getPhotoRotation(deviceDegree?: number): ImageRotation; 差异内容：7400101 | api/@ohos.multimedia.camera.d.ts |
| 新增错误码 | 类名：VideoOutput； API声明：getVideoRotation(deviceDegree?: number): ImageRotation; 差异内容：NA | 类名：VideoOutput； API声明：getVideoRotation(deviceDegree?: number): ImageRotation; 差异内容：7400101 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CameraManager； API声明：isTorchLevelControlSupported(): boolean; 差异内容：isTorchLevelControlSupported(): boolean; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CameraManager； API声明：setTorchModeOnWithLevel(torchLevel: number): void; 差异内容：setTorchModeOnWithLevel(torchLevel: number): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CameraFormat； API声明：CAMERA_FORMAT_DNG_XDRAW = 5 差异内容：CAMERA_FORMAT_DNG_XDRAW = 5 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera； API声明：enum ExposureState 差异内容：enum ExposureState | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ExposureState； API声明：EXPOSURE_STATE_SCAN = 0 差异内容：EXPOSURE_STATE_SCAN = 0 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ExposureState； API声明：EXPOSURE_STATE_CONVERGED = 1 差异内容：EXPOSURE_STATE_CONVERGED = 1 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutoExposure； API声明：onExposureStateChange(callback: Callback&lt;ExposureState&gt;): void; 差异内容：onExposureStateChange(callback: Callback&lt;ExposureState&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutoExposure； API声明：offExposureStateChange(callback?: Callback&lt;ExposureState&gt;): void; 差异内容：offExposureStateChange(callback?: Callback&lt;ExposureState&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：WhiteBalanceQuery； API声明：getColorTintRange(): Array&lt;number&gt;; 差异内容：getColorTintRange(): Array&lt;number&gt;; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：WhiteBalance； API声明：setColorTint(colorTint: number): void; 差异内容：setColorTint(colorTint: number): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：WhiteBalance； API声明：getColorTint(): number; 差异内容：getColorTint(): number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera； API声明：interface ZoomPointInfo 差异内容：interface ZoomPointInfo | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ZoomPointInfo； API声明：readonly zoomRatio: number; 差异内容：readonly zoomRatio: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ZoomPointInfo； API声明：readonly equivalentFocalLength: number; 差异内容：readonly equivalentFocalLength: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ZoomQuery； API声明：getZoomPointInfos(): Array&lt;ZoomPointInfo&gt;; 差异内容：getZoomPointInfos(): Array&lt;ZoomPointInfo&gt;; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ControlCenterEffectType； API声明：COLOR_EFFECT = 3 差异内容：COLOR_EFFECT = 3 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：VideoSession； API声明：onExposureInfoChange(callback: Callback&lt;ExposureInfo&gt;): void; 差异内容：onExposureInfoChange(callback: Callback&lt;ExposureInfo&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：VideoSession； API声明：offExposureInfoChange(callback?: Callback&lt;ExposureInfo&gt;): void; 差异内容：offExposureInfoChange(callback?: Callback&lt;ExposureInfo&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataObjectType； API声明：CAT_FACE = 2 差异内容：CAT_FACE = 2 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataObjectType； API声明：CAT_BODY = 3 差异内容：CAT_BODY = 3 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataObjectType； API声明：DOG_FACE = 4 差异内容：DOG_FACE = 4 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataObjectType； API声明：DOG_BODY = 5 差异内容：DOG_BODY = 5 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataObjectType； API声明：SALIENT_DETECTION = 6 差异内容：SALIENT_DETECTION = 6 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera； API声明：enum Emotion 差异内容：enum Emotion | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：Emotion； API声明：NEUTRAL = 0 差异内容：NEUTRAL = 0 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：Emotion； API声明：SADNESS = 1 差异内容：SADNESS = 1 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：Emotion； API声明：SMILE = 2 差异内容：SMILE = 2 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：Emotion； API声明：SURPRISE = 3 差异内容：SURPRISE = 3 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera； API声明：interface MetadataBasicFaceObject 差异内容：interface MetadataBasicFaceObject | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataBasicFaceObject； API声明：readonly leftEyeBoundingBox?: Rect; 差异内容：readonly leftEyeBoundingBox?: Rect; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataBasicFaceObject； API声明：readonly rightEyeBoundingBox?: Rect; 差异内容：readonly rightEyeBoundingBox?: Rect; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataBasicFaceObject； API声明：readonly pitchAngle?: number; 差异内容：readonly pitchAngle?: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataBasicFaceObject； API声明：readonly yawAngle?: number; 差异内容：readonly yawAngle?: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataBasicFaceObject； API声明：readonly rollAngle?: number; 差异内容：readonly rollAngle?: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera； API声明：interface MetadataFaceObject 差异内容：interface MetadataFaceObject | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataFaceObject； API声明：readonly leftEyeBoundingBox: Rect; 差异内容：readonly leftEyeBoundingBox: Rect; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataFaceObject； API声明：readonly rightEyeBoundingBox: Rect; 差异内容：readonly rightEyeBoundingBox: Rect; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataFaceObject； API声明：readonly emotion: Emotion; 差异内容：readonly emotion: Emotion; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataFaceObject； API声明：readonly emotionConfidence: number; 差异内容：readonly emotionConfidence: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataFaceObject； API声明：readonly pitchAngle: number; 差异内容：readonly pitchAngle: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataFaceObject； API声明：readonly yawAngle: number; 差异内容：readonly yawAngle: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataFaceObject； API声明：readonly rollAngle: number; 差异内容：readonly rollAngle: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera； API声明：interface MetadataHumanBodyObject 差异内容：interface MetadataHumanBodyObject | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera； API声明：interface MetadataCatFaceObject 差异内容：interface MetadataCatFaceObject | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataCatFaceObject； API声明：readonly leftEyeBoundingBox: Rect; 差异内容：readonly leftEyeBoundingBox: Rect; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataCatFaceObject； API声明：readonly rightEyeBoundingBox: Rect; 差异内容：readonly rightEyeBoundingBox: Rect; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera； API声明：interface MetadataCatBodyObject 差异内容：interface MetadataCatBodyObject | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera； API声明：interface MetadataDogFaceObject 差异内容：interface MetadataDogFaceObject | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataDogFaceObject； API声明：readonly leftEyeBoundingBox: Rect; 差异内容：readonly leftEyeBoundingBox: Rect; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataDogFaceObject； API声明：readonly rightEyeBoundingBox: Rect; 差异内容：readonly rightEyeBoundingBox: Rect; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera； API声明：interface MetadataDogBodyObject 差异内容：interface MetadataDogBodyObject | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera； API声明：interface MetadataSalientDetectionObject 差异内容：interface MetadataSalientDetectionObject | api/@ohos.multimedia.camera.d.ts |
