# Camera Kit

更新时间：2026-05-26 06:42:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-camerakit-6112

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：camera； API声明：enum SensorColorFilterArrangement 差异内容：enum SensorColorFilterArrangement | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：SensorColorFilterArrangement； API声明：BGGR = 0 差异内容：BGGR = 0 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：SensorColorFilterArrangement； API声明：GBRG = 1 差异内容：GBRG = 1 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：SensorColorFilterArrangement； API声明：GRBG = 2 差异内容：GRBG = 2 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：SensorColorFilterArrangement； API声明：RGGB = 3 差异内容：RGGB = 3 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CameraDevice； API声明：readonly lensEquivalentFocalLength?: Array&lt;number&gt;; 差异内容：readonly lensEquivalentFocalLength?: Array&lt;number&gt;; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CameraDevice； API声明：readonly isLogicalCamera?: boolean; 差异内容：readonly isLogicalCamera?: boolean; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CameraDevice； API声明：readonly constituentCameraDevices?: Array&lt;CameraDevice&gt;; 差异内容：readonly constituentCameraDevices?: Array&lt;CameraDevice&gt;; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CameraDevice； API声明：readonly lensFocalLength?: number; 差异内容：readonly lensFocalLength?: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CameraDevice； API声明：readonly minimumFocusDistance?: number; 差异内容：readonly minimumFocusDistance?: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CameraDevice； API声明：readonly lensDistortion?: Array&lt;number&gt;; 差异内容：readonly lensDistortion?: Array&lt;number&gt;; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CameraDevice； API声明：readonly lensIntrinsicCalibration?: Array&lt;number&gt;; 差异内容：readonly lensIntrinsicCalibration?: Array&lt;number&gt;; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CameraDevice； API声明：readonly sensorPhysicalSize?: Array&lt;number&gt;; 差异内容：readonly sensorPhysicalSize?: Array&lt;number&gt;; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CameraDevice； API声明：readonly sensorPixelArraySize?: Array&lt;number&gt;; 差异内容：readonly sensorPixelArraySize?: Array&lt;number&gt;; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CameraDevice； API声明：readonly sensorColorFilterArrangement?: SensorColorFilterArrangement; 差异内容：readonly sensorColorFilterArrangement?: SensorColorFilterArrangement; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CameraFormat； API声明：CAMERA_FORMAT_DNG = 4 差异内容：CAMERA_FORMAT_DNG = 4 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：Flash； API声明：onFlashStateChange(callback: Callback&lt;FlashState&gt;): void; 差异内容：onFlashStateChange(callback: Callback&lt;FlashState&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：Flash； API声明：offFlashStateChange(callback?: Callback&lt;FlashState&gt;): void; 差异内容：offFlashStateChange(callback?: Callback&lt;FlashState&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera； API声明：enum FlashState 差异内容：enum FlashState | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：FlashState； API声明：FLASH_STATE_UNAVAILABLE = 0 差异内容：FLASH_STATE_UNAVAILABLE = 0 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：FlashState； API声明：FLASH_STATE_READY = 1 差异内容：FLASH_STATE_READY = 1 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：FlashState； API声明：FLASH_STATE_FLASHING = 2 差异内容：FLASH_STATE_FLASHING = 2 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ExposureMode； API声明：EXPOSURE_MODE_MANUAL = 3 差异内容：EXPOSURE_MODE_MANUAL = 3 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera； API声明：enum ExposureMeteringMode 差异内容：enum ExposureMeteringMode | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ExposureMeteringMode； API声明：MATRIX = 0 差异内容：MATRIX = 0 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ExposureMeteringMode； API声明：CENTER = 1 差异内容：CENTER = 1 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ExposureMeteringMode； API声明：SPOT = 2 差异内容：SPOT = 2 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutoExposureQuery； API声明：isExposureMeteringModeSupported(aeMeteringMode: ExposureMeteringMode): boolean; 差异内容：isExposureMeteringModeSupported(aeMeteringMode: ExposureMeteringMode): boolean; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutoExposure； API声明：getExposureMeteringMode(): ExposureMeteringMode; 差异内容：getExposureMeteringMode(): ExposureMeteringMode; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutoExposure； API声明：setExposureMeteringMode(aeMeteringMode: ExposureMeteringMode): void; 差异内容：setExposureMeteringMode(aeMeteringMode: ExposureMeteringMode): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera； API声明：interface ManualFocusQuery 差异内容：interface ManualFocusQuery | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ManualFocusQuery； API声明：isFocusDistanceSupported(): boolean; 差异内容：isFocusDistanceSupported(): boolean; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera； API声明：interface ManualFocus 差异内容：interface ManualFocus | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ManualFocus； API声明：getFocusDistance(): number; 差异内容：getFocusDistance(): number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ManualFocus； API声明：setFocusDistance(distance: number): void; 差异内容：setFocusDistance(distance: number): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera； API声明：interface ManualIsoQuery 差异内容：interface ManualIsoQuery | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ManualIsoQuery； API声明：getSupportedIsoRange(): number[]; 差异内容：getSupportedIsoRange(): number[]; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera； API声明：interface ManualIso 差异内容：interface ManualIso | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ManualIso； API声明：getIso(): number; 差异内容：getIso(): number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ManualIso； API声明：setIso(iso: number): void; 差异内容：setIso(iso: number): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ZoomQuery； API声明：getRAWCaptureZoomRatioRange(): Array&lt;number&gt;; 差异内容：getRAWCaptureZoomRatioRange(): Array&lt;number&gt;; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ControlCenterEffectType； API声明：AUTO_FRAMING = 2 差异内容：AUTO_FRAMING = 2 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoSession； API声明：onIsoInfoChange(callback: Callback&lt;IsoInfo&gt;): void; 差异内容：onIsoInfoChange(callback: Callback&lt;IsoInfo&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoSession； API声明：offIsoInfoChange(callback?: Callback&lt;IsoInfo&gt;): void; 差异内容：offIsoInfoChange(callback?: Callback&lt;IsoInfo&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoSession； API声明：onExposureInfoChange(callback: Callback&lt;ExposureInfo&gt;): void; 差异内容：onExposureInfoChange(callback: Callback&lt;ExposureInfo&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoSession； API声明：offExposureInfoChange(callback?: Callback&lt;ExposureInfo&gt;): void; 差异内容：offExposureInfoChange(callback?: Callback&lt;ExposureInfo&gt;): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera； API声明：interface ZoomRange 差异内容：interface ZoomRange | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ZoomRange； API声明：readonly min: number; 差异内容：readonly min: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ZoomRange； API声明：readonly max: number; 差异内容：readonly max: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera； API声明：interface PhysicalAperture 差异内容：interface PhysicalAperture | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhysicalAperture； API声明：zoomRange: ZoomRange; 差异内容：zoomRange: ZoomRange; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhysicalAperture； API声明：apertures: Array&lt;number&gt;; 差异内容：apertures: Array&lt;number&gt;; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera； API声明：interface ApertureQuery 差异内容：interface ApertureQuery | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ApertureQuery； API声明：getSupportedPhysicalApertures(): Array&lt;PhysicalAperture&gt;; 差异内容：getSupportedPhysicalApertures(): Array&lt;PhysicalAperture&gt;; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera； API声明：interface Aperture 差异内容：interface Aperture | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：Aperture； API声明：getPhysicalAperture(): number; 差异内容：getPhysicalAperture(): number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：Aperture； API声明：setPhysicalAperture(aperture: number): void; 差异内容：setPhysicalAperture(aperture: number): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera； API声明：interface ManualExposureQuery 差异内容：interface ManualExposureQuery | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ManualExposureQuery； API声明：getSupportedExposureDurationRange(): Array&lt;number&gt;; 差异内容：getSupportedExposureDurationRange(): Array&lt;number&gt;; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ManualExposureQuery； API声明：getExposureBiasStep(): number; 差异内容：getExposureBiasStep(): number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera； API声明：interface ManualExposure 差异内容：interface ManualExposure | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ManualExposure； API声明：getExposureDuration(): number; 差异内容：getExposureDuration(): number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ManualExposure； API声明：setExposureDuration(exposureDuration: number): void; 差异内容：setExposureDuration(exposureDuration: number): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera； API声明：interface ExposureInfo 差异内容：interface ExposureInfo | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ExposureInfo； API声明：readonly exposureTime?: number; 差异内容：readonly exposureTime?: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera； API声明：enum OISMode 差异内容：enum OISMode | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：OISMode； API声明：OFF = 0 差异内容：OFF = 0 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：OISMode； API声明：AUTO = 1 差异内容：AUTO = 1 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：OISMode； API声明：CUSTOM = 2 差异内容：CUSTOM = 2 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera； API声明：enum OISAxes 差异内容：enum OISAxes | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：OISAxes； API声明：PITCH = 0 差异内容：PITCH = 0 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：OISAxes； API声明：YAW = 1 差异内容：YAW = 1 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera； API声明：interface OISQuery 差异内容：interface OISQuery | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：OISQuery； API声明：isOISModeSupported(mode: OISMode): boolean; 差异内容：isOISModeSupported(mode: OISMode): boolean; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：OISQuery； API声明：getSupportedOISBiasRange(oisAxis: OISAxes): Array&lt;number&gt;; 差异内容：getSupportedOISBiasRange(oisAxis: OISAxes): Array&lt;number&gt;; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：OISQuery； API声明：getSupportedOISBiasStep(oisAxis: OISAxes): number; 差异内容：getSupportedOISBiasStep(oisAxis: OISAxes): number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：OISQuery； API声明：getCurrentOISMode(): OISMode; 差异内容：getCurrentOISMode(): OISMode; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：OISQuery； API声明：getCurrentCustomOISBias(oisAxis: OISAxes): number; 差异内容：getCurrentCustomOISBias(oisAxis: OISAxes): number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera； API声明：interface OIS 差异内容：interface OIS | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：OIS； API声明：setOISMode(mode: OISMode): void; 差异内容：setOISMode(mode: OISMode): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：OIS； API声明：setOISModeCustom(pitch: number, yaw: number): void; 差异内容：setOISModeCustom(pitch: number, yaw: number): void; | api/@ohos.multimedia.camera.d.ts |
