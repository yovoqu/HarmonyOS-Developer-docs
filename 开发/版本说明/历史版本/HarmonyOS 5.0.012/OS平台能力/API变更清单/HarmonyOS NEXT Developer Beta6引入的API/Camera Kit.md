# Camera Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-camerakit-b061

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明： interface CameraOutput 差异内容： interface CameraOutput | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CameraOutput； API声明：release(callback: AsyncCallback&lt;void&gt;): void; 差异内容：release(callback: AsyncCallback&lt;void&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CameraOutput； API声明：release(): Promise&lt;void&gt;; 差异内容：release(): Promise&lt;void&gt;; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：global； API声明： interface PreviewOutput 差异内容： interface PreviewOutput | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreviewOutput； API声明：start(callback: AsyncCallback&lt;void&gt;): void; 差异内容：start(callback: AsyncCallback&lt;void&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreviewOutput； API声明：start(): Promise&lt;void&gt;; 差异内容：start(): Promise&lt;void&gt;; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreviewOutput； API声明：stop(callback: AsyncCallback&lt;void&gt;): void; 差异内容：stop(callback: AsyncCallback&lt;void&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreviewOutput； API声明：stop(): Promise&lt;void&gt;; 差异内容：stop(): Promise&lt;void&gt;; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreviewOutput； API声明：on(type: 'frameStart', callback: AsyncCallback&lt;void&gt;): void; 差异内容：on(type: 'frameStart', callback: AsyncCallback&lt;void&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreviewOutput； API声明：off(type: 'frameStart', callback?: AsyncCallback&lt;void&gt;): void; 差异内容：off(type: 'frameStart', callback?: AsyncCallback&lt;void&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreviewOutput； API声明：on(type: 'frameEnd', callback: AsyncCallback&lt;void&gt;): void; 差异内容：on(type: 'frameEnd', callback: AsyncCallback&lt;void&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreviewOutput； API声明：off(type: 'frameEnd', callback?: AsyncCallback&lt;void&gt;): void; 差异内容：off(type: 'frameEnd', callback?: AsyncCallback&lt;void&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreviewOutput； API声明：on(type: 'error', callback: ErrorCallback): void; 差异内容：on(type: 'error', callback: ErrorCallback): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreviewOutput； API声明：off(type: 'error', callback?: ErrorCallback): void; 差异内容：off(type: 'error', callback?: ErrorCallback): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreviewOutput； API声明：getSupportedFrameRates(): Array&lt;FrameRateRange&gt;; 差异内容：getSupportedFrameRates(): Array&lt;FrameRateRange&gt;; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreviewOutput； API声明：setFrameRate(minFps: number, maxFps: number): void; 差异内容：setFrameRate(minFps: number, maxFps: number): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreviewOutput； API声明：getActiveFrameRate(): FrameRateRange; 差异内容：getActiveFrameRate(): FrameRateRange; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：global； API声明： enum ImageRotation 差异内容： enum ImageRotation | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ImageRotation； API声明：ROTATION_0 = 0 差异内容：ROTATION_0 = 0 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ImageRotation； API声明：ROTATION_90 = 90 差异内容：ROTATION_90 = 90 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ImageRotation； API声明：ROTATION_180 = 180 差异内容：ROTATION_180 = 180 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ImageRotation； API声明：ROTATION_270 = 270 差异内容：ROTATION_270 = 270 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：global； API声明： interface Location 差异内容： interface Location | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：Location； API声明：latitude: number; 差异内容：latitude: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：Location； API声明：longitude: number; 差异内容：longitude: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：Location； API声明：altitude: number; 差异内容：altitude: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：global； API声明： enum QualityLevel 差异内容： enum QualityLevel | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：QualityLevel； API声明：QUALITY_LEVEL_HIGH = 0 差异内容：QUALITY_LEVEL_HIGH = 0 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：QualityLevel； API声明：QUALITY_LEVEL_MEDIUM = 1 差异内容：QUALITY_LEVEL_MEDIUM = 1 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：QualityLevel； API声明：QUALITY_LEVEL_LOW = 2 差异内容：QUALITY_LEVEL_LOW = 2 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：global； API声明： interface PhotoCaptureSetting 差异内容： interface PhotoCaptureSetting | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoCaptureSetting； API声明：quality?: QualityLevel; 差异内容：quality?: QualityLevel; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoCaptureSetting； API声明：rotation?: ImageRotation; 差异内容：rotation?: ImageRotation; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoCaptureSetting； API声明：location?: Location; 差异内容：location?: Location; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoCaptureSetting； API声明：mirror?: boolean; 差异内容：mirror?: boolean; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：global； API声明： interface Photo 差异内容： interface Photo | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：Photo； API声明：main: image.Image; 差异内容：main: image.Image; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：Photo； API声明：release(): Promise&lt;void&gt;; 差异内容：release(): Promise&lt;void&gt;; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：global； API声明： interface PhotoOutput 差异内容： interface PhotoOutput | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput； API声明：capture(callback: AsyncCallback&lt;void&gt;): void; 差异内容：capture(callback: AsyncCallback&lt;void&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput； API声明：capture(): Promise&lt;void&gt;; 差异内容：capture(): Promise&lt;void&gt;; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput； API声明：capture(setting: PhotoCaptureSetting, callback: AsyncCallback&lt;void&gt;): void; 差异内容：capture(setting: PhotoCaptureSetting, callback: AsyncCallback&lt;void&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput； API声明：capture(setting: PhotoCaptureSetting): Promise&lt;void&gt;; 差异内容：capture(setting: PhotoCaptureSetting): Promise&lt;void&gt;; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput； API声明：on(type: 'photoAvailable', callback: AsyncCallback&lt;Photo&gt;): void; 差异内容：on(type: 'photoAvailable', callback: AsyncCallback&lt;Photo&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput； API声明：off(type: 'photoAvailable', callback?: AsyncCallback&lt;Photo&gt;): void; 差异内容：off(type: 'photoAvailable', callback?: AsyncCallback&lt;Photo&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput； API声明：on(type: 'photoAssetAvailable', callback: AsyncCallback<photoAccessHelper.PhotoAsset>): void; 差异内容：on(type: 'photoAssetAvailable', callback: AsyncCallback<photoAccessHelper.PhotoAsset>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput； API声明：off(type: 'photoAssetAvailable', callback?: AsyncCallback<photoAccessHelper.PhotoAsset>): void; 差异内容：off(type: 'photoAssetAvailable', callback?: AsyncCallback<photoAccessHelper.PhotoAsset>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput； API声明：isMirrorSupported(): boolean; 差异内容：isMirrorSupported(): boolean; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput； API声明：on(type: 'captureStart', callback: AsyncCallback&lt;number&gt;): void; 差异内容：on(type: 'captureStart', callback: AsyncCallback&lt;number&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput； API声明：off(type: 'captureStart', callback?: AsyncCallback&lt;number&gt;): void; 差异内容：off(type: 'captureStart', callback?: AsyncCallback&lt;number&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput； API声明：on(type: 'captureStartWithInfo', callback: AsyncCallback&lt;CaptureStartInfo&gt;): void; 差异内容：on(type: 'captureStartWithInfo', callback: AsyncCallback&lt;CaptureStartInfo&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput； API声明：off(type: 'captureStartWithInfo', callback?: AsyncCallback&lt;CaptureStartInfo&gt;): void; 差异内容：off(type: 'captureStartWithInfo', callback?: AsyncCallback&lt;CaptureStartInfo&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput； API声明：on(type: 'frameShutter', callback: AsyncCallback&lt;FrameShutterInfo&gt;): void; 差异内容：on(type: 'frameShutter', callback: AsyncCallback&lt;FrameShutterInfo&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput； API声明：off(type: 'frameShutter', callback?: AsyncCallback&lt;FrameShutterInfo&gt;): void; 差异内容：off(type: 'frameShutter', callback?: AsyncCallback&lt;FrameShutterInfo&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput； API声明：on(type: 'frameShutterEnd', callback: AsyncCallback&lt;FrameShutterEndInfo&gt;): void; 差异内容：on(type: 'frameShutterEnd', callback: AsyncCallback&lt;FrameShutterEndInfo&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput； API声明：off(type: 'frameShutterEnd', callback?: AsyncCallback&lt;FrameShutterEndInfo&gt;): void; 差异内容：off(type: 'frameShutterEnd', callback?: AsyncCallback&lt;FrameShutterEndInfo&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput； API声明：on(type: 'captureEnd', callback: AsyncCallback&lt;CaptureEndInfo&gt;): void; 差异内容：on(type: 'captureEnd', callback: AsyncCallback&lt;CaptureEndInfo&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput； API声明：off(type: 'captureEnd', callback?: AsyncCallback&lt;CaptureEndInfo&gt;): void; 差异内容：off(type: 'captureEnd', callback?: AsyncCallback&lt;CaptureEndInfo&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput； API声明：on(type: 'captureReady', callback: AsyncCallback&lt;void&gt;): void; 差异内容：on(type: 'captureReady', callback: AsyncCallback&lt;void&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput； API声明：off(type: 'captureReady', callback?: AsyncCallback&lt;void&gt;): void; 差异内容：off(type: 'captureReady', callback?: AsyncCallback&lt;void&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput； API声明：on(type: 'estimatedCaptureDuration', callback: AsyncCallback&lt;number&gt;): void; 差异内容：on(type: 'estimatedCaptureDuration', callback: AsyncCallback&lt;number&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput； API声明：off(type: 'estimatedCaptureDuration', callback?: AsyncCallback&lt;number&gt;): void; 差异内容：off(type: 'estimatedCaptureDuration', callback?: AsyncCallback&lt;number&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput； API声明：on(type: 'error', callback: ErrorCallback): void; 差异内容：on(type: 'error', callback: ErrorCallback): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput； API声明：off(type: 'error', callback?: ErrorCallback): void; 差异内容：off(type: 'error', callback?: ErrorCallback): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput； API声明：isMovingPhotoSupported(): boolean; 差异内容：isMovingPhotoSupported(): boolean; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput； API声明：enableMovingPhoto(enabled: boolean): void; 差异内容：enableMovingPhoto(enabled: boolean): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：global； API声明： interface FrameShutterInfo 差异内容： interface FrameShutterInfo | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：FrameShutterInfo； API声明：captureId: number; 差异内容：captureId: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：FrameShutterInfo； API声明：timestamp: number; 差异内容：timestamp: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：global； API声明： interface FrameShutterEndInfo 差异内容： interface FrameShutterEndInfo | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：FrameShutterEndInfo； API声明：captureId: number; 差异内容：captureId: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：global； API声明： interface CaptureStartInfo 差异内容： interface CaptureStartInfo | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CaptureStartInfo； API声明：captureId: number; 差异内容：captureId: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CaptureStartInfo； API声明：time: number; 差异内容：time: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：global； API声明： interface CaptureEndInfo 差异内容： interface CaptureEndInfo | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CaptureEndInfo； API声明：captureId: number; 差异内容：captureId: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CaptureEndInfo； API声明：frameCount: number; 差异内容：frameCount: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：global； API声明： interface VideoOutput 差异内容： interface VideoOutput | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：VideoOutput； API声明：start(callback: AsyncCallback&lt;void&gt;): void; 差异内容：start(callback: AsyncCallback&lt;void&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：VideoOutput； API声明：start(): Promise&lt;void&gt;; 差异内容：start(): Promise&lt;void&gt;; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：VideoOutput； API声明：stop(callback: AsyncCallback&lt;void&gt;): void; 差异内容：stop(callback: AsyncCallback&lt;void&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：VideoOutput； API声明：stop(): Promise&lt;void&gt;; 差异内容：stop(): Promise&lt;void&gt;; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：VideoOutput； API声明：getSupportedFrameRates(): Array&lt;FrameRateRange&gt;; 差异内容：getSupportedFrameRates(): Array&lt;FrameRateRange&gt;; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：VideoOutput； API声明：setFrameRate(minFps: number, maxFps: number): void; 差异内容：setFrameRate(minFps: number, maxFps: number): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：VideoOutput； API声明：getActiveFrameRate(): FrameRateRange; 差异内容：getActiveFrameRate(): FrameRateRange; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：VideoOutput； API声明：on(type: 'frameStart', callback: AsyncCallback&lt;void&gt;): void; 差异内容：on(type: 'frameStart', callback: AsyncCallback&lt;void&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：VideoOutput； API声明：off(type: 'frameStart', callback?: AsyncCallback&lt;void&gt;): void; 差异内容：off(type: 'frameStart', callback?: AsyncCallback&lt;void&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：VideoOutput； API声明：on(type: 'frameEnd', callback: AsyncCallback&lt;void&gt;): void; 差异内容：on(type: 'frameEnd', callback: AsyncCallback&lt;void&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：VideoOutput； API声明：off(type: 'frameEnd', callback?: AsyncCallback&lt;void&gt;): void; 差异内容：off(type: 'frameEnd', callback?: AsyncCallback&lt;void&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：VideoOutput； API声明：on(type: 'error', callback: ErrorCallback): void; 差异内容：on(type: 'error', callback: ErrorCallback): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：VideoOutput； API声明：off(type: 'error', callback?: ErrorCallback): void; 差异内容：off(type: 'error', callback?: ErrorCallback): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：global； API声明： enum MetadataObjectType 差异内容： enum MetadataObjectType | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataObjectType； API声明：FACE_DETECTION = 0 差异内容：FACE_DETECTION = 0 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：global； API声明： interface Rect 差异内容： interface Rect | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：Rect； API声明：topLeftX: number; 差异内容：topLeftX: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：Rect； API声明：topLeftY: number; 差异内容：topLeftY: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：Rect； API声明：width: number; 差异内容：width: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：Rect； API声明：height: number; 差异内容：height: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：global； API声明： interface MetadataObject 差异内容： interface MetadataObject | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataObject； API声明：readonly type: MetadataObjectType; 差异内容：readonly type: MetadataObjectType; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataObject； API声明：readonly timestamp: number; 差异内容：readonly timestamp: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataObject； API声明：readonly boundingBox: Rect; 差异内容：readonly boundingBox: Rect; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：global； API声明： interface MetadataOutput 差异内容： interface MetadataOutput | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataOutput； API声明：start(callback: AsyncCallback&lt;void&gt;): void; 差异内容：start(callback: AsyncCallback&lt;void&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataOutput； API声明：start(): Promise&lt;void&gt;; 差异内容：start(): Promise&lt;void&gt;; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataOutput； API声明：stop(callback: AsyncCallback&lt;void&gt;): void; 差异内容：stop(callback: AsyncCallback&lt;void&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataOutput； API声明：stop(): Promise&lt;void&gt;; 差异内容：stop(): Promise&lt;void&gt;; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataOutput； API声明：on(type: 'metadataObjectsAvailable', callback: AsyncCallback<Array&lt;MetadataObject&gt;>): void; 差异内容：on(type: 'metadataObjectsAvailable', callback: AsyncCallback<Array&lt;MetadataObject&gt;>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataOutput； API声明：off(type: 'metadataObjectsAvailable', callback?: AsyncCallback<Array&lt;MetadataObject&gt;>): void; 差异内容：off(type: 'metadataObjectsAvailable', callback?: AsyncCallback<Array&lt;MetadataObject&gt;>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataOutput； API声明：on(type: 'error', callback: ErrorCallback): void; 差异内容：on(type: 'error', callback: ErrorCallback): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataOutput； API声明：off(type: 'error', callback?: ErrorCallback): void; 差异内容：off(type: 'error', callback?: ErrorCallback): void; | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：camera； API声明： interface CameraOutput 差异内容： interface CameraOutput | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：CameraOutput； API声明：release(callback: AsyncCallback&lt;void&gt;): void; 差异内容：release(callback: AsyncCallback&lt;void&gt;): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：CameraOutput； API声明：release(): Promise&lt;void&gt;; 差异内容：release(): Promise&lt;void&gt;; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：camera； API声明： interface PreviewOutput 差异内容： interface PreviewOutput | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PreviewOutput； API声明：start(callback: AsyncCallback&lt;void&gt;): void; 差异内容：start(callback: AsyncCallback&lt;void&gt;): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PreviewOutput； API声明：start(): Promise&lt;void&gt;; 差异内容：start(): Promise&lt;void&gt;; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PreviewOutput； API声明：stop(callback: AsyncCallback&lt;void&gt;): void; 差异内容：stop(callback: AsyncCallback&lt;void&gt;): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PreviewOutput； API声明：stop(): Promise&lt;void&gt;; 差异内容：stop(): Promise&lt;void&gt;; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PreviewOutput； API声明：on(type: 'frameStart', callback: AsyncCallback&lt;void&gt;): void; 差异内容：on(type: 'frameStart', callback: AsyncCallback&lt;void&gt;): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PreviewOutput； API声明：off(type: 'frameStart', callback?: AsyncCallback&lt;void&gt;): void; 差异内容：off(type: 'frameStart', callback?: AsyncCallback&lt;void&gt;): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PreviewOutput； API声明：on(type: 'frameEnd', callback: AsyncCallback&lt;void&gt;): void; 差异内容：on(type: 'frameEnd', callback: AsyncCallback&lt;void&gt;): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PreviewOutput； API声明：off(type: 'frameEnd', callback?: AsyncCallback&lt;void&gt;): void; 差异内容：off(type: 'frameEnd', callback?: AsyncCallback&lt;void&gt;): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PreviewOutput； API声明：on(type: 'error', callback: ErrorCallback): void; 差异内容：on(type: 'error', callback: ErrorCallback): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PreviewOutput； API声明：off(type: 'error', callback?: ErrorCallback): void; 差异内容：off(type: 'error', callback?: ErrorCallback): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PreviewOutput； API声明：getSupportedFrameRates(): Array&lt;FrameRateRange&gt;; 差异内容：getSupportedFrameRates(): Array&lt;FrameRateRange&gt;; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PreviewOutput； API声明：setFrameRate(minFps: number, maxFps: number): void; 差异内容：setFrameRate(minFps: number, maxFps: number): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PreviewOutput； API声明：getActiveFrameRate(): FrameRateRange; 差异内容：getActiveFrameRate(): FrameRateRange; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：camera； API声明： enum ImageRotation 差异内容： enum ImageRotation | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：ImageRotation； API声明：ROTATION_0 = 0 差异内容：ROTATION_0 = 0 | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：ImageRotation； API声明：ROTATION_90 = 90 差异内容：ROTATION_90 = 90 | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：ImageRotation； API声明：ROTATION_180 = 180 差异内容：ROTATION_180 = 180 | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：ImageRotation； API声明：ROTATION_270 = 270 差异内容：ROTATION_270 = 270 | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：camera； API声明： interface Location 差异内容： interface Location | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：Location； API声明：latitude: number; 差异内容：latitude: number; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：Location； API声明：longitude: number; 差异内容：longitude: number; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：Location； API声明：altitude: number; 差异内容：altitude: number; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：camera； API声明： enum QualityLevel 差异内容： enum QualityLevel | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：QualityLevel； API声明：QUALITY_LEVEL_HIGH = 0 差异内容：QUALITY_LEVEL_HIGH = 0 | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：QualityLevel； API声明：QUALITY_LEVEL_MEDIUM = 1 差异内容：QUALITY_LEVEL_MEDIUM = 1 | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：QualityLevel； API声明：QUALITY_LEVEL_LOW = 2 差异内容：QUALITY_LEVEL_LOW = 2 | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：camera； API声明： interface PhotoCaptureSetting 差异内容： interface PhotoCaptureSetting | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoCaptureSetting； API声明：quality?: QualityLevel; 差异内容：quality?: QualityLevel; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoCaptureSetting； API声明：rotation?: ImageRotation; 差异内容：rotation?: ImageRotation; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoCaptureSetting； API声明：location?: Location; 差异内容：location?: Location; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoCaptureSetting； API声明：mirror?: boolean; 差异内容：mirror?: boolean; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：camera； API声明： interface Photo 差异内容： interface Photo | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：Photo； API声明：main: image.Image; 差异内容：main: image.Image; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：Photo； API声明：release(): Promise&lt;void&gt;; 差异内容：release(): Promise&lt;void&gt;; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：camera； API声明： interface PhotoOutput 差异内容： interface PhotoOutput | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput； API声明：capture(callback: AsyncCallback&lt;void&gt;): void; 差异内容：capture(callback: AsyncCallback&lt;void&gt;): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput； API声明：capture(): Promise&lt;void&gt;; 差异内容：capture(): Promise&lt;void&gt;; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput； API声明：capture(setting: PhotoCaptureSetting, callback: AsyncCallback&lt;void&gt;): void; 差异内容：capture(setting: PhotoCaptureSetting, callback: AsyncCallback&lt;void&gt;): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput； API声明：capture(setting: PhotoCaptureSetting): Promise&lt;void&gt;; 差异内容：capture(setting: PhotoCaptureSetting): Promise&lt;void&gt;; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput； API声明：on(type: 'photoAvailable', callback: AsyncCallback&lt;Photo&gt;): void; 差异内容：on(type: 'photoAvailable', callback: AsyncCallback&lt;Photo&gt;): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput； API声明：off(type: 'photoAvailable', callback?: AsyncCallback&lt;Photo&gt;): void; 差异内容：off(type: 'photoAvailable', callback?: AsyncCallback&lt;Photo&gt;): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput； API声明：on(type: 'photoAssetAvailable', callback: AsyncCallback<photoAccessHelper.PhotoAsset>): void; 差异内容：on(type: 'photoAssetAvailable', callback: AsyncCallback<photoAccessHelper.PhotoAsset>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput； API声明：off(type: 'photoAssetAvailable', callback?: AsyncCallback<photoAccessHelper.PhotoAsset>): void; 差异内容：off(type: 'photoAssetAvailable', callback?: AsyncCallback<photoAccessHelper.PhotoAsset>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput； API声明：isMirrorSupported(): boolean; 差异内容：isMirrorSupported(): boolean; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput； API声明：on(type: 'captureStart', callback: AsyncCallback&lt;number&gt;): void; 差异内容：on(type: 'captureStart', callback: AsyncCallback&lt;number&gt;): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput； API声明：off(type: 'captureStart', callback?: AsyncCallback&lt;number&gt;): void; 差异内容：off(type: 'captureStart', callback?: AsyncCallback&lt;number&gt;): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput； API声明：on(type: 'captureStartWithInfo', callback: AsyncCallback&lt;CaptureStartInfo&gt;): void; 差异内容：on(type: 'captureStartWithInfo', callback: AsyncCallback&lt;CaptureStartInfo&gt;): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput； API声明：off(type: 'captureStartWithInfo', callback?: AsyncCallback&lt;CaptureStartInfo&gt;): void; 差异内容：off(type: 'captureStartWithInfo', callback?: AsyncCallback&lt;CaptureStartInfo&gt;): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput； API声明：on(type: 'frameShutter', callback: AsyncCallback&lt;FrameShutterInfo&gt;): void; 差异内容：on(type: 'frameShutter', callback: AsyncCallback&lt;FrameShutterInfo&gt;): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput； API声明：off(type: 'frameShutter', callback?: AsyncCallback&lt;FrameShutterInfo&gt;): void; 差异内容：off(type: 'frameShutter', callback?: AsyncCallback&lt;FrameShutterInfo&gt;): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput； API声明：on(type: 'frameShutterEnd', callback: AsyncCallback&lt;FrameShutterEndInfo&gt;): void; 差异内容：on(type: 'frameShutterEnd', callback: AsyncCallback&lt;FrameShutterEndInfo&gt;): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput； API声明：off(type: 'frameShutterEnd', callback?: AsyncCallback&lt;FrameShutterEndInfo&gt;): void; 差异内容：off(type: 'frameShutterEnd', callback?: AsyncCallback&lt;FrameShutterEndInfo&gt;): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput； API声明：on(type: 'captureEnd', callback: AsyncCallback&lt;CaptureEndInfo&gt;): void; 差异内容：on(type: 'captureEnd', callback: AsyncCallback&lt;CaptureEndInfo&gt;): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput； API声明：off(type: 'captureEnd', callback?: AsyncCallback&lt;CaptureEndInfo&gt;): void; 差异内容：off(type: 'captureEnd', callback?: AsyncCallback&lt;CaptureEndInfo&gt;): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput； API声明：on(type: 'captureReady', callback: AsyncCallback&lt;void&gt;): void; 差异内容：on(type: 'captureReady', callback: AsyncCallback&lt;void&gt;): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput； API声明：off(type: 'captureReady', callback?: AsyncCallback&lt;void&gt;): void; 差异内容：off(type: 'captureReady', callback?: AsyncCallback&lt;void&gt;): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput； API声明：on(type: 'estimatedCaptureDuration', callback: AsyncCallback&lt;number&gt;): void; 差异内容：on(type: 'estimatedCaptureDuration', callback: AsyncCallback&lt;number&gt;): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput； API声明：off(type: 'estimatedCaptureDuration', callback?: AsyncCallback&lt;number&gt;): void; 差异内容：off(type: 'estimatedCaptureDuration', callback?: AsyncCallback&lt;number&gt;): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput； API声明：on(type: 'error', callback: ErrorCallback): void; 差异内容：on(type: 'error', callback: ErrorCallback): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput； API声明：off(type: 'error', callback?: ErrorCallback): void; 差异内容：off(type: 'error', callback?: ErrorCallback): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput； API声明：isMovingPhotoSupported(): boolean; 差异内容：isMovingPhotoSupported(): boolean; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput； API声明：enableMovingPhoto(enabled: boolean): void; 差异内容：enableMovingPhoto(enabled: boolean): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：camera； API声明： interface FrameShutterInfo 差异内容： interface FrameShutterInfo | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：FrameShutterInfo； API声明：captureId: number; 差异内容：captureId: number; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：FrameShutterInfo； API声明：timestamp: number; 差异内容：timestamp: number; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：camera； API声明： interface FrameShutterEndInfo 差异内容： interface FrameShutterEndInfo | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：FrameShutterEndInfo； API声明：captureId: number; 差异内容：captureId: number; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：camera； API声明： interface CaptureStartInfo 差异内容： interface CaptureStartInfo | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：CaptureStartInfo； API声明：captureId: number; 差异内容：captureId: number; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：CaptureStartInfo； API声明：time: number; 差异内容：time: number; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：camera； API声明： interface CaptureEndInfo 差异内容： interface CaptureEndInfo | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：CaptureEndInfo； API声明：captureId: number; 差异内容：captureId: number; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：CaptureEndInfo； API声明：frameCount: number; 差异内容：frameCount: number; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：camera； API声明： interface VideoOutput 差异内容： interface VideoOutput | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：VideoOutput； API声明：start(callback: AsyncCallback&lt;void&gt;): void; 差异内容：start(callback: AsyncCallback&lt;void&gt;): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：VideoOutput； API声明：start(): Promise&lt;void&gt;; 差异内容：start(): Promise&lt;void&gt;; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：VideoOutput； API声明：stop(callback: AsyncCallback&lt;void&gt;): void; 差异内容：stop(callback: AsyncCallback&lt;void&gt;): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：VideoOutput； API声明：stop(): Promise&lt;void&gt;; 差异内容：stop(): Promise&lt;void&gt;; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：VideoOutput； API声明：getSupportedFrameRates(): Array&lt;FrameRateRange&gt;; 差异内容：getSupportedFrameRates(): Array&lt;FrameRateRange&gt;; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：VideoOutput； API声明：setFrameRate(minFps: number, maxFps: number): void; 差异内容：setFrameRate(minFps: number, maxFps: number): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：VideoOutput； API声明：getActiveFrameRate(): FrameRateRange; 差异内容：getActiveFrameRate(): FrameRateRange; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：VideoOutput； API声明：on(type: 'frameStart', callback: AsyncCallback&lt;void&gt;): void; 差异内容：on(type: 'frameStart', callback: AsyncCallback&lt;void&gt;): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：VideoOutput； API声明：off(type: 'frameStart', callback?: AsyncCallback&lt;void&gt;): void; 差异内容：off(type: 'frameStart', callback?: AsyncCallback&lt;void&gt;): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：VideoOutput； API声明：on(type: 'frameEnd', callback: AsyncCallback&lt;void&gt;): void; 差异内容：on(type: 'frameEnd', callback: AsyncCallback&lt;void&gt;): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：VideoOutput； API声明：off(type: 'frameEnd', callback?: AsyncCallback&lt;void&gt;): void; 差异内容：off(type: 'frameEnd', callback?: AsyncCallback&lt;void&gt;): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：VideoOutput； API声明：on(type: 'error', callback: ErrorCallback): void; 差异内容：on(type: 'error', callback: ErrorCallback): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：VideoOutput； API声明：off(type: 'error', callback?: ErrorCallback): void; 差异内容：off(type: 'error', callback?: ErrorCallback): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：camera； API声明： enum MetadataObjectType 差异内容： enum MetadataObjectType | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：MetadataObjectType； API声明：FACE_DETECTION = 0 差异内容：FACE_DETECTION = 0 | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：camera； API声明： interface Rect 差异内容： interface Rect | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：Rect； API声明：topLeftX: number; 差异内容：topLeftX: number; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：Rect； API声明：topLeftY: number; 差异内容：topLeftY: number; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：Rect； API声明：width: number; 差异内容：width: number; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：Rect； API声明：height: number; 差异内容：height: number; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：camera； API声明： interface MetadataObject 差异内容： interface MetadataObject | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：MetadataObject； API声明：readonly type: MetadataObjectType; 差异内容：readonly type: MetadataObjectType; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：MetadataObject； API声明：readonly timestamp: number; 差异内容：readonly timestamp: number; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：MetadataObject； API声明：readonly boundingBox: Rect; 差异内容：readonly boundingBox: Rect; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：camera； API声明： interface MetadataOutput 差异内容： interface MetadataOutput | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：MetadataOutput； API声明：start(callback: AsyncCallback&lt;void&gt;): void; 差异内容：start(callback: AsyncCallback&lt;void&gt;): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：MetadataOutput； API声明：start(): Promise&lt;void&gt;; 差异内容：start(): Promise&lt;void&gt;; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：MetadataOutput； API声明：stop(callback: AsyncCallback&lt;void&gt;): void; 差异内容：stop(callback: AsyncCallback&lt;void&gt;): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：MetadataOutput； API声明：stop(): Promise&lt;void&gt;; 差异内容：stop(): Promise&lt;void&gt;; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：MetadataOutput； API声明：on(type: 'metadataObjectsAvailable', callback: AsyncCallback<Array&lt;MetadataObject&gt;>): void; 差异内容：on(type: 'metadataObjectsAvailable', callback: AsyncCallback<Array&lt;MetadataObject&gt;>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：MetadataOutput； API声明：off(type: 'metadataObjectsAvailable', callback?: AsyncCallback<Array&lt;MetadataObject&gt;>): void; 差异内容：off(type: 'metadataObjectsAvailable', callback?: AsyncCallback<Array&lt;MetadataObject&gt;>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：MetadataOutput； API声明：on(type: 'error', callback: ErrorCallback): void; 差异内容：on(type: 'error', callback: ErrorCallback): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：MetadataOutput； API声明：off(type: 'error', callback?: ErrorCallback): void; 差异内容：off(type: 'error', callback?: ErrorCallback): void; | NA | api/@ohos.multimedia.camera.d.ts |
