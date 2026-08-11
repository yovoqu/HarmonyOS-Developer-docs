# Camera Kit

更新时间：2026-07-28 11:14:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-camerakit-7002

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：CameraDevice； API声明：readonly automotiveCameraPosition?: AutomotiveCameraPosition; 差异内容：readonly automotiveCameraPosition?: AutomotiveCameraPosition; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：FocusQuery； API声明：isLockFocusTrackingSupported(): boolean; 差异内容：isLockFocusTrackingSupported(): boolean; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：Focus； API声明：lockFocusTracking(focusPoint: Point): void; 差异内容：lockFocusTracking(focusPoint: Point): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：Focus； API声明：unlockFocusTracking(): void; 差异内容：unlockFocusTracking(): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreviewOutput； API声明：isLogViewAssistSupported(): boolean; 差异内容：isLogViewAssistSupported(): boolean; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreviewOutput； API声明：setLogViewAssistEnable(enable: boolean): void; 差异内容：setLogViewAssistEnable(enable: boolean): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoCaptureSetting； API声明：compressionQuality?: number; 差异内容：compressionQuality?: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput； API声明：isAutoExtendedGainmapDeliverySupported(): boolean; 差异内容：isAutoExtendedGainmapDeliverySupported(): boolean; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput； API声明：enableAutoExtendedGainmapDelivery(enabled: boolean): void; 差异内容：enableAutoExtendedGainmapDelivery(enabled: boolean): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataObjectType； API声明：BAR_CODE_DETECTION = 7 差异内容：BAR_CODE_DETECTION = 7 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataObjectType； API声明：BASIC_FACE_DETECTION = 8 差异内容：BASIC_FACE_DETECTION = 8 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataObject； API声明：readonly isLockFocusTracked?: boolean; 差异内容：readonly isLockFocusTracked?: boolean; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera； API声明：interface MetadataBarcodeObject 差异内容：interface MetadataBarcodeObject | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataOutput； API声明：isLockMetadataObjectTrackingSupported(): boolean; 差异内容：isLockMetadataObjectTrackingSupported(): boolean; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataOutput； API声明：lockMetadataObjectTracking(point: Point): void; 差异内容：lockMetadataObjectTracking(point: Point): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataOutput； API声明：unlockMetadataObjectTracking(): void; 差异内容：unlockMetadataObjectTracking(): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera； API声明：enum AutomotiveCameraPosition 差异内容：enum AutomotiveCameraPosition | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutomotiveCameraPosition； API声明：AUTOMOTIVE_CAMERA_POSITION_EXTERIOR_OTHER = 0 差异内容：AUTOMOTIVE_CAMERA_POSITION_EXTERIOR_OTHER = 0 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutomotiveCameraPosition； API声明：AUTOMOTIVE_CAMERA_POSITION_EXTERIOR_FRONT = 1 差异内容：AUTOMOTIVE_CAMERA_POSITION_EXTERIOR_FRONT = 1 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutomotiveCameraPosition； API声明：AUTOMOTIVE_CAMERA_POSITION_EXTERIOR_REAR = 2 差异内容：AUTOMOTIVE_CAMERA_POSITION_EXTERIOR_REAR = 2 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutomotiveCameraPosition； API声明：AUTOMOTIVE_CAMERA_POSITION_EXTERIOR_LEFT = 3 差异内容：AUTOMOTIVE_CAMERA_POSITION_EXTERIOR_LEFT = 3 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutomotiveCameraPosition； API声明：AUTOMOTIVE_CAMERA_POSITION_EXTERIOR_RIGHT = 4 差异内容：AUTOMOTIVE_CAMERA_POSITION_EXTERIOR_RIGHT = 4 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutomotiveCameraPosition； API声明：AUTOMOTIVE_CAMERA_POSITION_INTERIOR_OTHER = 5 差异内容：AUTOMOTIVE_CAMERA_POSITION_INTERIOR_OTHER = 5 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutomotiveCameraPosition； API声明：AUTOMOTIVE_CAMERA_POSITION_INTERIOR_ROW_1_LEFT = 6 差异内容：AUTOMOTIVE_CAMERA_POSITION_INTERIOR_ROW_1_LEFT = 6 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutomotiveCameraPosition； API声明：AUTOMOTIVE_CAMERA_POSITION_INTERIOR_ROW_1_CENTER = 7 差异内容：AUTOMOTIVE_CAMERA_POSITION_INTERIOR_ROW_1_CENTER = 7 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutomotiveCameraPosition； API声明：AUTOMOTIVE_CAMERA_POSITION_INTERIOR_ROW_1_RIGHT = 8 差异内容：AUTOMOTIVE_CAMERA_POSITION_INTERIOR_ROW_1_RIGHT = 8 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutomotiveCameraPosition； API声明：AUTOMOTIVE_CAMERA_POSITION_INTERIOR_ROW_2_LEFT = 9 差异内容：AUTOMOTIVE_CAMERA_POSITION_INTERIOR_ROW_2_LEFT = 9 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutomotiveCameraPosition； API声明：AUTOMOTIVE_CAMERA_POSITION_INTERIOR_ROW_2_CENTER = 10 差异内容：AUTOMOTIVE_CAMERA_POSITION_INTERIOR_ROW_2_CENTER = 10 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutomotiveCameraPosition； API声明：AUTOMOTIVE_CAMERA_POSITION_INTERIOR_ROW_2_RIGHT = 11 差异内容：AUTOMOTIVE_CAMERA_POSITION_INTERIOR_ROW_2_RIGHT = 11 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutomotiveCameraPosition； API声明：AUTOMOTIVE_CAMERA_POSITION_INTERIOR_ROW_3_LEFT = 12 差异内容：AUTOMOTIVE_CAMERA_POSITION_INTERIOR_ROW_3_LEFT = 12 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutomotiveCameraPosition； API声明：AUTOMOTIVE_CAMERA_POSITION_INTERIOR_ROW_3_CENTER = 13 差异内容：AUTOMOTIVE_CAMERA_POSITION_INTERIOR_ROW_3_CENTER = 13 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutomotiveCameraPosition； API声明：AUTOMOTIVE_CAMERA_POSITION_INTERIOR_ROW_3_RIGHT = 14 差异内容：AUTOMOTIVE_CAMERA_POSITION_INTERIOR_ROW_3_RIGHT = 14 | api/@ohos.multimedia.camera.d.ts |
