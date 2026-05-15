# Image Kit

更新时间：2026-04-30 02:39:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-imagekit-6111

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：ImageSource； API声明：createPicture(options?: DecodingOptionsForPicture): Promise<Picture>; 差异内容：NA | 类名：ImageSource； API声明：createPicture(options?: DecodingOptionsForPicture): Promise<Picture>; 差异内容：7700203 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image； API声明：function createAuxiliaryPictureUsingAllocator(auxiliaryPictureInfo: AuxiliaryPictureInfo, allocatorType?: AllocatorType, pixels?: ArrayBuffer): AuxiliaryPicture; 差异内容：function createAuxiliaryPictureUsingAllocator(auxiliaryPictureInfo: AuxiliaryPictureInfo, allocatorType?: AllocatorType, pixels?: ArrayBuffer): AuxiliaryPicture; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MetadataType； API声明：DNG_METADATA = 16 差异内容：DNG_METADATA = 16 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：MetadataType； API声明：WEBP_METADATA = 17 差异内容：WEBP_METADATA = 17 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image； API声明：enum DngPropertyKey 差异内容：enum DngPropertyKey | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：DNG_VERSION = 'DNGVersion' 差异内容：DNG_VERSION = 'DNGVersion' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：DNG_BACKWARD_VERSION = 'DNGBackwardVersion' 差异内容：DNG_BACKWARD_VERSION = 'DNGBackwardVersion' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：UNIQUE_CAMERA_MODEL = 'UniqueCameraModel' 差异内容：UNIQUE_CAMERA_MODEL = 'UniqueCameraModel' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：LOCALIZED_CAMERA_MODEL = 'LocalizedCameraModel' 差异内容：LOCALIZED_CAMERA_MODEL = 'LocalizedCameraModel' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：CFA_PLANE_COLOR = 'CFAPlaneColor' 差异内容：CFA_PLANE_COLOR = 'CFAPlaneColor' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：CFA_LAYOUT = 'CFALayout' 差异内容：CFA_LAYOUT = 'CFALayout' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：LINEARIZATION_TABLE = 'LinearizationTable' 差异内容：LINEARIZATION_TABLE = 'LinearizationTable' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：BLACK_LEVEL_REPEAT_DIM = 'BlackLevelRepeatDim' 差异内容：BLACK_LEVEL_REPEAT_DIM = 'BlackLevelRepeatDim' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：BLACK_LEVEL = 'BlackLevel' 差异内容：BLACK_LEVEL = 'BlackLevel' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：BLACK_LEVEL_DELTA_H = 'BlackLevelDeltaH' 差异内容：BLACK_LEVEL_DELTA_H = 'BlackLevelDeltaH' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：BLACK_LEVEL_DELTA_V = 'BlackLevelDeltaV' 差异内容：BLACK_LEVEL_DELTA_V = 'BlackLevelDeltaV' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：WHITE_LEVEL = 'WhiteLevel' 差异内容：WHITE_LEVEL = 'WhiteLevel' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：DEFAULT_SCALE = 'DefaultScale' 差异内容：DEFAULT_SCALE = 'DefaultScale' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：DEFAULT_CROP_ORIGIN = 'DefaultCropOrigin' 差异内容：DEFAULT_CROP_ORIGIN = 'DefaultCropOrigin' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：DEFAULT_CROP_SIZE = 'DefaultCropSize' 差异内容：DEFAULT_CROP_SIZE = 'DefaultCropSize' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：COLOR_MATRIX1 = 'ColorMatrix1' 差异内容：COLOR_MATRIX1 = 'ColorMatrix1' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：COLOR_MATRIX2 = 'ColorMatrix2' 差异内容：COLOR_MATRIX2 = 'ColorMatrix2' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：CAMERA_CALIBRATION1 = 'CameraCalibration1' 差异内容：CAMERA_CALIBRATION1 = 'CameraCalibration1' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：CAMERA_CALIBRATION2 = 'CameraCalibration2' 差异内容：CAMERA_CALIBRATION2 = 'CameraCalibration2' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：REDUCTION_MATRIX1 = 'ReductionMatrix1' 差异内容：REDUCTION_MATRIX1 = 'ReductionMatrix1' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：REDUCTION_MATRIX2 = 'ReductionMatrix2' 差异内容：REDUCTION_MATRIX2 = 'ReductionMatrix2' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：ANALOG_BALANCE = 'AnalogBalance' 差异内容：ANALOG_BALANCE = 'AnalogBalance' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：AS_SHOT_NEUTRAL = 'AsShotNeutral' 差异内容：AS_SHOT_NEUTRAL = 'AsShotNeutral' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：AS_SHOT_WHITEXY = 'AsShotWhiteXY' 差异内容：AS_SHOT_WHITEXY = 'AsShotWhiteXY' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：BASELINE_EXPOSURE = 'BaselineExposure' 差异内容：BASELINE_EXPOSURE = 'BaselineExposure' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：BASELINE_NOISE = 'BaselineNoise' 差异内容：BASELINE_NOISE = 'BaselineNoise' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：BASELINE_SHARPNESS = 'BaselineSharpness' 差异内容：BASELINE_SHARPNESS = 'BaselineSharpness' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：BAYER_GREEN_SPLIT = 'BayerGreenSplit' 差异内容：BAYER_GREEN_SPLIT = 'BayerGreenSplit' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：LINEAR_RESPONSE_LIMIT = 'LinearResponseLimit' 差异内容：LINEAR_RESPONSE_LIMIT = 'LinearResponseLimit' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：CAMERA_SERIAL_NUMBER = 'CameraSerialNumber' 差异内容：CAMERA_SERIAL_NUMBER = 'CameraSerialNumber' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：LENS_INFO = 'LensInfo' 差异内容：LENS_INFO = 'LensInfo' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：CHROMA_BLUR_RADIUS = 'ChromaBlurRadius' 差异内容：CHROMA_BLUR_RADIUS = 'ChromaBlurRadius' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：ANTI_ALIAS_STRENGTH = 'AntiAliasStrength' 差异内容：ANTI_ALIAS_STRENGTH = 'AntiAliasStrength' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：SHADOW_SCALE = 'ShadowScale' 差异内容：SHADOW_SCALE = 'ShadowScale' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：DNG_PRIVATE_DATA = 'DNGPrivateData' 差异内容：DNG_PRIVATE_DATA = 'DNGPrivateData' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：MAKER_NOTE_SAFETY = 'MakerNoteSafety' 差异内容：MAKER_NOTE_SAFETY = 'MakerNoteSafety' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：CALIBRATION_ILLUMINANT1 = 'CalibrationIlluminant1' 差异内容：CALIBRATION_ILLUMINANT1 = 'CalibrationIlluminant1' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：CALIBRATION_ILLUMINANT2 = 'CalibrationIlluminant2' 差异内容：CALIBRATION_ILLUMINANT2 = 'CalibrationIlluminant2' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：BEST_QUALITY_SCALE = 'BestQualityScale' 差异内容：BEST_QUALITY_SCALE = 'BestQualityScale' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：RAW_DATA_UNIQUE_ID = 'RawDataUniqueID' 差异内容：RAW_DATA_UNIQUE_ID = 'RawDataUniqueID' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：ORIGINAL_RAW_FILE_NAME = 'OriginalRawFileName' 差异内容：ORIGINAL_RAW_FILE_NAME = 'OriginalRawFileName' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：ORIGINAL_RAW_FILE_DATA = 'OriginalRawFileData' 差异内容：ORIGINAL_RAW_FILE_DATA = 'OriginalRawFileData' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：ACTIVE_AREA = 'ActiveArea' 差异内容：ACTIVE_AREA = 'ActiveArea' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：MASKED_AREAS = 'MaskedAreas' 差异内容：MASKED_AREAS = 'MaskedAreas' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：AS_SHOT_ICC_PROFILE = 'AsShotICCProfile' 差异内容：AS_SHOT_ICC_PROFILE = 'AsShotICCProfile' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：AS_SHOT_PRE_PROFILE_MATRIX = 'AsShotPreProfileMatrix' 差异内容：AS_SHOT_PRE_PROFILE_MATRIX = 'AsShotPreProfileMatrix' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：CURRENT_ICC_PROFILE = 'CurrentICCProfile' 差异内容：CURRENT_ICC_PROFILE = 'CurrentICCProfile' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：CURRENT_PRE_PROFILE_MATRIX = 'CurrentPreProfileMatrix' 差异内容：CURRENT_PRE_PROFILE_MATRIX = 'CurrentPreProfileMatrix' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：COLORIMETRIC_REFERENCE = 'ColorimetricReference' 差异内容：COLORIMETRIC_REFERENCE = 'ColorimetricReference' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：CAMERA_CALIBRATION_SIGNATURE = 'CameraCalibrationSignature' 差异内容：CAMERA_CALIBRATION_SIGNATURE = 'CameraCalibrationSignature' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：PROFILE_CALIBRATION_SIGNATURE = 'ProfileCalibrationSignature' 差异内容：PROFILE_CALIBRATION_SIGNATURE = 'ProfileCalibrationSignature' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：EXTRA_CAMERA_PROFILES = 'ExtraCameraProfiles' 差异内容：EXTRA_CAMERA_PROFILES = 'ExtraCameraProfiles' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：AS_SHOT_PROFILE_NAME = 'AsShotProfileName' 差异内容：AS_SHOT_PROFILE_NAME = 'AsShotProfileName' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：NOISE_REDUCTION_APPLIED = 'NoiseReductionApplied' 差异内容：NOISE_REDUCTION_APPLIED = 'NoiseReductionApplied' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：PROFILE_NAME = 'ProfileName' 差异内容：PROFILE_NAME = 'ProfileName' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：PROFILE_HUE_SAT_MAP_DIMS = 'ProfileHueSatMapDims' 差异内容：PROFILE_HUE_SAT_MAP_DIMS = 'ProfileHueSatMapDims' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：PROFILE_HUE_SAT_MAP_DATA1 = 'ProfileHueSatMapData1' 差异内容：PROFILE_HUE_SAT_MAP_DATA1 = 'ProfileHueSatMapData1' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：PROFILE_HUE_SAT_MAP_DATA2 = 'ProfileHueSatMapData2' 差异内容：PROFILE_HUE_SAT_MAP_DATA2 = 'ProfileHueSatMapData2' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：PROFILE_TONE_CURVE = 'ProfileToneCurve' 差异内容：PROFILE_TONE_CURVE = 'ProfileToneCurve' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：PROFILE_EMBED_POLICY = 'ProfileEmbedPolicy' 差异内容：PROFILE_EMBED_POLICY = 'ProfileEmbedPolicy' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：PROFILE_COPYRIGHT = 'ProfileCopyright' 差异内容：PROFILE_COPYRIGHT = 'ProfileCopyright' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：FORWARD_MATRIX1 = 'ForwardMatrix1' 差异内容：FORWARD_MATRIX1 = 'ForwardMatrix1' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：FORWARD_MATRIX2 = 'ForwardMatrix2' 差异内容：FORWARD_MATRIX2 = 'ForwardMatrix2' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：PREVIEW_APPLICATION_NAME = 'PreviewApplicationName' 差异内容：PREVIEW_APPLICATION_NAME = 'PreviewApplicationName' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：PREVIEW_APPLICATION_VERSION = 'PreviewApplicationVersion' 差异内容：PREVIEW_APPLICATION_VERSION = 'PreviewApplicationVersion' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：PREVIEW_SETTINGS_NAME = 'PreviewSettingsName' 差异内容：PREVIEW_SETTINGS_NAME = 'PreviewSettingsName' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：PREVIEW_SETTINGS_DIGEST = 'PreviewSettingsDigest' 差异内容：PREVIEW_SETTINGS_DIGEST = 'PreviewSettingsDigest' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：PREVIEW_COLOR_SPACE = 'PreviewColorSpace' 差异内容：PREVIEW_COLOR_SPACE = 'PreviewColorSpace' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：PREVIEW_DATE_TIME = 'PreviewDateTime' 差异内容：PREVIEW_DATE_TIME = 'PreviewDateTime' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：RAW_IMAGE_DIGEST = 'RawImageDigest' 差异内容：RAW_IMAGE_DIGEST = 'RawImageDigest' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：ORIGINAL_RAW_FILE_DIGEST = 'OriginalRawFileDigest' 差异内容：ORIGINAL_RAW_FILE_DIGEST = 'OriginalRawFileDigest' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：SUB_TILE_BLOCK_SIZE = 'SubTileBlockSize' 差异内容：SUB_TILE_BLOCK_SIZE = 'SubTileBlockSize' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：ROW_INTERLEAVE_FACTOR = 'RowInterleaveFactor' 差异内容：ROW_INTERLEAVE_FACTOR = 'RowInterleaveFactor' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：PROFILE_LOOK_TABLE_DIMS = 'ProfileLookTableDims' 差异内容：PROFILE_LOOK_TABLE_DIMS = 'ProfileLookTableDims' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：PROFILE_LOOK_TABLE_DATA = 'ProfileLookTableData' 差异内容：PROFILE_LOOK_TABLE_DATA = 'ProfileLookTableData' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：OPCODE_LIST1 = 'OpcodeList1' 差异内容：OPCODE_LIST1 = 'OpcodeList1' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：OPCODE_LIST2 = 'OpcodeList2' 差异内容：OPCODE_LIST2 = 'OpcodeList2' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：OPCODE_LIST3 = 'OpcodeList3' 差异内容：OPCODE_LIST3 = 'OpcodeList3' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：NOISE_PROFILE = 'NoiseProfile' 差异内容：NOISE_PROFILE = 'NoiseProfile' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：ORIGINAL_DEFAULT_FINAL_SIZE = 'OriginalDefaultFinalSize' 差异内容：ORIGINAL_DEFAULT_FINAL_SIZE = 'OriginalDefaultFinalSize' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：ORIGINAL_BEST_QUALITY_FINAL_SIZE = 'OriginalBestQualityFinalSize' 差异内容：ORIGINAL_BEST_QUALITY_FINAL_SIZE = 'OriginalBestQualityFinalSize' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：ORIGINAL_DEFAULT_CROP_SIZE = 'OriginalDefaultCropSize' 差异内容：ORIGINAL_DEFAULT_CROP_SIZE = 'OriginalDefaultCropSize' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：PROFILE_HUE_SAT_MAP_ENCODING = 'ProfileHueSatMapEncoding' 差异内容：PROFILE_HUE_SAT_MAP_ENCODING = 'ProfileHueSatMapEncoding' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：PROFILE_LOOK_TABLE_ENCODING = 'ProfileLookTableEncoding' 差异内容：PROFILE_LOOK_TABLE_ENCODING = 'ProfileLookTableEncoding' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：BASELINE_EXPOSURE_OFFSET = 'BaselineExposureOffset' 差异内容：BASELINE_EXPOSURE_OFFSET = 'BaselineExposureOffset' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：DEFAULT_BLACK_RENDER = 'DefaultBlackRender' 差异内容：DEFAULT_BLACK_RENDER = 'DefaultBlackRender' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：NEW_RAW_IMAGE_DIGEST = 'NewRawImageDigest' 差异内容：NEW_RAW_IMAGE_DIGEST = 'NewRawImageDigest' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：RAW_TO_PREVIEW_GAIN = 'RawToPreviewGain' 差异内容：RAW_TO_PREVIEW_GAIN = 'RawToPreviewGain' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngPropertyKey； API声明：DEFAULT_USER_CROP = 'DefaultUserCrop' 差异内容：DEFAULT_USER_CROP = 'DefaultUserCrop' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image； API声明：class DngMetadata 差异内容：class DngMetadata | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly dngVersion?: number[]; 差异内容：readonly dngVersion?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly dngBackwardVersion?: number[]; 差异内容：readonly dngBackwardVersion?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly uniqueCameraModel?: string; 差异内容：readonly uniqueCameraModel?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly localizedCameraModel?: string; 差异内容：readonly localizedCameraModel?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly cfaPlaneColor?: number[]; 差异内容：readonly cfaPlaneColor?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly cfaLayout?: number; 差异内容：readonly cfaLayout?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly linearizationTable?: number[]; 差异内容：readonly linearizationTable?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly blackLevelRepeatDim?: number[]; 差异内容：readonly blackLevelRepeatDim?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly blackLevel?: number[]; 差异内容：readonly blackLevel?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly blackLevelDeltaH?: number[]; 差异内容：readonly blackLevelDeltaH?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly blackLevelDeltaV?: number[]; 差异内容：readonly blackLevelDeltaV?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly whiteLevel?: number[]; 差异内容：readonly whiteLevel?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly defaultScale?: number[]; 差异内容：readonly defaultScale?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly defaultCropOrigin?: number[]; 差异内容：readonly defaultCropOrigin?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly defaultCropSize?: number[]; 差异内容：readonly defaultCropSize?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly colorMatrix1?: number[]; 差异内容：readonly colorMatrix1?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly colorMatrix2?: number[]; 差异内容：readonly colorMatrix2?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly cameraCalibration1?: number[]; 差异内容：readonly cameraCalibration1?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly cameraCalibration2?: number[]; 差异内容：readonly cameraCalibration2?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly reductionMatrix1?: number[]; 差异内容：readonly reductionMatrix1?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly reductionMatrix2?: number[]; 差异内容：readonly reductionMatrix2?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly analogBalance?: number[]; 差异内容：readonly analogBalance?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly asShotNeutral?: number[]; 差异内容：readonly asShotNeutral?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly asShotWhiteXY?: number[]; 差异内容：readonly asShotWhiteXY?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly baselineExposure?: number; 差异内容：readonly baselineExposure?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly baselineNoise?: number; 差异内容：readonly baselineNoise?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly baselineSharpness?: number; 差异内容：readonly baselineSharpness?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly bayerGreenSplit?: number; 差异内容：readonly bayerGreenSplit?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly linearResponseLimit?: number; 差异内容：readonly linearResponseLimit?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly cameraSerialNumber?: string; 差异内容：readonly cameraSerialNumber?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly lensInfo?: number[]; 差异内容：readonly lensInfo?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly chromaBlurRadius?: number; 差异内容：readonly chromaBlurRadius?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly antiAliasStrength?: number; 差异内容：readonly antiAliasStrength?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly shadowScale?: number; 差异内容：readonly shadowScale?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly dngPrivateData?: ArrayBuffer; 差异内容：readonly dngPrivateData?: ArrayBuffer; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly makerNoteSafety?: boolean; 差异内容：readonly makerNoteSafety?: boolean; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly calibrationIlluminant1?: number; 差异内容：readonly calibrationIlluminant1?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly calibrationIlluminant2?: number; 差异内容：readonly calibrationIlluminant2?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly bestQualityScale?: number; 差异内容：readonly bestQualityScale?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly rawDataUniqueID?: string; 差异内容：readonly rawDataUniqueID?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly originalRawFileName?: string; 差异内容：readonly originalRawFileName?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly originalRawFileData?: ArrayBuffer; 差异内容：readonly originalRawFileData?: ArrayBuffer; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly activeArea?: number[]; 差异内容：readonly activeArea?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly maskedAreas?: number[]; 差异内容：readonly maskedAreas?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly asShotICCProfile?: ArrayBuffer; 差异内容：readonly asShotICCProfile?: ArrayBuffer; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly asShotPreProfileMatrix?: number[]; 差异内容：readonly asShotPreProfileMatrix?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly currentICCProfile?: ArrayBuffer; 差异内容：readonly currentICCProfile?: ArrayBuffer; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly currentPreProfileMatrix?: number[]; 差异内容：readonly currentPreProfileMatrix?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly colorimetricReference?: number; 差异内容：readonly colorimetricReference?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly cameraCalibrationSignature?: string; 差异内容：readonly cameraCalibrationSignature?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly profileCalibrationSignature?: string; 差异内容：readonly profileCalibrationSignature?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly extraCameraProfiles?: number[]; 差异内容：readonly extraCameraProfiles?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly asShotProfileName?: string; 差异内容：readonly asShotProfileName?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly noiseReductionApplied?: number; 差异内容：readonly noiseReductionApplied?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly profileName?: string; 差异内容：readonly profileName?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly profileHueSatMapDims?: number[]; 差异内容：readonly profileHueSatMapDims?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly profileHueSatMapData1?: number[]; 差异内容：readonly profileHueSatMapData1?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly profileHueSatMapData2?: number[]; 差异内容：readonly profileHueSatMapData2?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly profileToneCurve?: number[]; 差异内容：readonly profileToneCurve?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly profileEmbedPolicy?: number; 差异内容：readonly profileEmbedPolicy?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly profileCopyright?: string; 差异内容：readonly profileCopyright?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly forwardMatrix1?: number[]; 差异内容：readonly forwardMatrix1?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly forwardMatrix2?: number[]; 差异内容：readonly forwardMatrix2?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly previewApplicationName?: string; 差异内容：readonly previewApplicationName?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly previewApplicationVersion?: string; 差异内容：readonly previewApplicationVersion?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly previewSettingsName?: string; 差异内容：readonly previewSettingsName?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly previewSettingsDigest?: string; 差异内容：readonly previewSettingsDigest?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly previewColorSpace?: number; 差异内容：readonly previewColorSpace?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly previewDateTime?: string; 差异内容：readonly previewDateTime?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly rawImageDigest?: string; 差异内容：readonly rawImageDigest?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly originalRawFileDigest?: string; 差异内容：readonly originalRawFileDigest?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly subTileBlockSize?: number[]; 差异内容：readonly subTileBlockSize?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly rowInterleaveFactor?: number; 差异内容：readonly rowInterleaveFactor?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly profileLookTableDims?: number[]; 差异内容：readonly profileLookTableDims?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly profileLookTableData?: number[]; 差异内容：readonly profileLookTableData?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly opcodeList1?: ArrayBuffer; 差异内容：readonly opcodeList1?: ArrayBuffer; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly opcodeList2?: ArrayBuffer; 差异内容：readonly opcodeList2?: ArrayBuffer; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly opcodeList3?: ArrayBuffer; 差异内容：readonly opcodeList3?: ArrayBuffer; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly noiseProfile?: number[]; 差异内容：readonly noiseProfile?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly originalDefaultFinalSize?: number[]; 差异内容：readonly originalDefaultFinalSize?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly originalBestQualityFinalSize?: number[]; 差异内容：readonly originalBestQualityFinalSize?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly originalDefaultCropSize?: number[]; 差异内容：readonly originalDefaultCropSize?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly profileHueSatMapEncoding?: number; 差异内容：readonly profileHueSatMapEncoding?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly profileLookTableEncoding?: number; 差异内容：readonly profileLookTableEncoding?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly baselineExposureOffset?: number; 差异内容：readonly baselineExposureOffset?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly defaultBlackRender?: number; 差异内容：readonly defaultBlackRender?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly newRawImageDigest?: string; 差异内容：readonly newRawImageDigest?: string; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly rawToPreviewGain?: number; 差异内容：readonly rawToPreviewGain?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DngMetadata； API声明：readonly defaultUserCrop?: number[]; 差异内容：readonly defaultUserCrop?: number[]; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image； API声明：enum WebPPropertyKey 差异内容：enum WebPPropertyKey | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：WebPPropertyKey； API声明：CANVAS_WIDTH = 'WebPCanvasWidth' 差异内容：CANVAS_WIDTH = 'WebPCanvasWidth' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：WebPPropertyKey； API声明：CANVAS_HEIGHT = 'WebPCanvasHeight' 差异内容：CANVAS_HEIGHT = 'WebPCanvasHeight' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：WebPPropertyKey； API声明：DELAY_TIME = 'WebPDelayTime' 差异内容：DELAY_TIME = 'WebPDelayTime' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：WebPPropertyKey； API声明：UNCLAMPED_DELAY_TIME = 'WebPUnclampedDelayTime' 差异内容：UNCLAMPED_DELAY_TIME = 'WebPUnclampedDelayTime' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：WebPPropertyKey； API声明：LOOP_COUNT = 'WebPLoopCount' 差异内容：LOOP_COUNT = 'WebPLoopCount' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image； API声明：class WebPMetadata 差异内容：class WebPMetadata | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：WebPMetadata； API声明：readonly canvasWidth?: number; 差异内容：readonly canvasWidth?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：WebPMetadata； API声明：readonly canvasHeight?: number; 差异内容：readonly canvasHeight?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：WebPMetadata； API声明：readonly delayTime?: number; 差异内容：readonly delayTime?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：WebPMetadata； API声明：readonly unclampedDelayTime?: number; 差异内容：readonly unclampedDelayTime?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：WebPMetadata； API声明：readonly loopCount?: number; 差异内容：readonly loopCount?: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageMetadata； API声明：dngMetadata?: DngMetadata; 差异内容：dngMetadata?: DngMetadata; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageMetadata； API声明：webPMetadata?: WebPMetadata; 差异内容：webPMetadata?: WebPMetadata; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DecodingOptionsForPicture； API声明：desiredSizeForMainPixelMap?: Size; 差异内容：desiredSizeForMainPixelMap?: Size; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：DecodingOptionsForPicture； API声明：desiredPixelFormat?: PixelMapFormat; 差异内容：desiredPixelFormat?: PixelMapFormat; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image； API声明：interface ImageRawData 差异内容：interface ImageRawData | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageRawData； API声明：buffer: ArrayBuffer; 差异内容：buffer: ArrayBuffer; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageRawData； API声明：bitsPerPixel: number; 差异内容：bitsPerPixel: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageSource； API声明：readImageMetadataByType(metadataTypes?: MetadataType[], index?: number): Promise<ImageMetadata>; 差异内容：readImageMetadataByType(metadataTypes?: MetadataType[], index?: number): Promise<ImageMetadata>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageSource； API声明：createImageRawData(): Promise<ImageRawData>; 差异内容：createImageRawData(): Promise<ImageRawData>; | api/@ohos.multimedia.image.d.ts |
