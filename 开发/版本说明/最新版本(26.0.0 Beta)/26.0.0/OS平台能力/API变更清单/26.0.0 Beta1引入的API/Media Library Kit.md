# Media Library Kit

更新时间：2026-06-27 01:41:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-medialibrarykit-7001

## Media Library Kit
 
 
| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：PickerController； API声明：completed(): Promise&lt;CompletedResult&gt;; 差异内容：completed(): Promise&lt;CompletedResult&gt;; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PickerOptions； API声明：contextRecoveryInfo?: photoAccessHelper.ContextRecoveryInfo; 差异内容：contextRecoveryInfo?: photoAccessHelper.ContextRecoveryInfo; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：global； API声明：export declare class CompletedResult 差异内容：export declare class CompletedResult | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：CompletedResult； API声明：photoUris: Array&lt;string&gt;; 差异内容：photoUris: Array&lt;string&gt;; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：CompletedResult； API声明：contextRecoveryInfo: photoAccessHelper.ContextRecoveryInfo; 差异内容：contextRecoveryInfo: photoAccessHelper.ContextRecoveryInfo; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：CompletedResult； API声明：movingPhotoBadgeStates: Array<photoAccessHelper.MovingPhotoBadgeStateType>; 差异内容：movingPhotoBadgeStates: Array<photoAccessHelper.MovingPhotoBadgeStateType>; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PhotoKeys； API声明：LOCAL_ASSET_SIZE = 'local_asset_size' 差异内容：LOCAL_ASSET_SIZE = 'local_asset_size' | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAccessHelper； API声明：onMediaLibraryAvailability(callback: Callback&lt;MediaLibraryAvailability&gt;): void; 差异内容：onMediaLibraryAvailability(callback: Callback&lt;MediaLibraryAvailability&gt;): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAccessHelper； API声明：offMediaLibraryAvailability(callback?: Callback&lt;MediaLibraryAvailability&gt;): void; 差异内容：offMediaLibraryAvailability(callback?: Callback&lt;MediaLibraryAvailability&gt;): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAccessHelper； API声明：checkPhotoUrisReadPermission(uris: string[]): Promise<Map<string, MediaAssetPermissionState>>; 差异内容：checkPhotoUrisReadPermission(uris: string[]): Promise<Map<string, MediaAssetPermissionState>>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：BaseSelectOptions； API声明：preferredCompatibleMode?: PreferredCompatibleMode; 差异内容：preferredCompatibleMode?: PreferredCompatibleMode; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoSelectOptions； API声明：isSelectionNumberVisible?: boolean; 差异内容：isSelectionNumberVisible?: boolean; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoSelectOptions； API声明：isSelectionOrderAdjustable?: boolean; 差异内容：isSelectionOrderAdjustable?: boolean; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AssetCompatibleCapability； API声明：supportedMimeType?: Array&lt;string&gt;; 差异内容：supportedMimeType?: Array&lt;string&gt;; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper； API声明：enum PreferredCompatibleMode 差异内容：enum PreferredCompatibleMode | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PreferredCompatibleMode； API声明：DEFAULT = 0 差异内容：DEFAULT = 0 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PreferredCompatibleMode； API声明：CURRENT = 1 差异内容：CURRENT = 1 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PreferredCompatibleMode； API声明：COMPATIBLE = 2 差异内容：COMPATIBLE = 2 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper； API声明：enum MediaAssetPermissionState 差异内容：enum MediaAssetPermissionState | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAssetPermissionState； API声明：URI_FORMAT_ERROR = 0 差异内容：URI_FORMAT_ERROR = 0 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAssetPermissionState； API声明：FILE_NOT_EXIST = 1 差异内容：FILE_NOT_EXIST = 1 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAssetPermissionState； API声明：READ_PERMISSION = 2 差异内容：READ_PERMISSION = 2 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAssetPermissionState； API声明：NO_READ_PERMISSION = 3 差异内容：NO_READ_PERMISSION = 3 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper； API声明：interface MediaLibraryAvailability 差异内容：interface MediaLibraryAvailability | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaLibraryAvailability； API声明：availabilityStatus: AvailabilityStatus; 差异内容：availabilityStatus: AvailabilityStatus; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaLibraryAvailability； API声明：unavailabilityReason: string; 差异内容：unavailabilityReason: string; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper； API声明：enum AvailabilityStatus 差异内容：enum AvailabilityStatus | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AvailabilityStatus； API声明：AVAILABLE = 'available' 差异内容：AVAILABLE = 'available' | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AvailabilityStatus； API声明：UNAVAILABLE = 'unavailable' 差异内容：UNAVAILABLE = 'unavailable' | api/@ohos.file.photoAccessHelper.d.ts |
