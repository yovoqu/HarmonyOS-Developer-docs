# 使用相机预配置(C/C++)

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-preconfig-native

相机预配置（Preconfig），对常用的场景和分辨率进行了预配置集成，可简化开发相机应用流程，提高应用的开发效率。

 开发者在开发相机应用时，在获取到CameraDevice之后，如果遵循通用流程开发，步骤较为繁琐。需要先查询当前相机在指定模式下所支持的各类输出的配置信息，拿到[Camera_OutputCapability](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-outputcapability)之后，应用开发者还需要对里面的各类数据进行解析，筛选，找到自己需要的配置数据[Camera_Profile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-profile)和[Camera_VideoProfile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-videoprofile)。最后使用对应的Profile以及VideoProfile创建对应的[Camera_PreviewOutput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-previewoutput)、[Camera_PhotoOutput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-photooutput)以及[Camera_VideoOutput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-videooutput)。

 为了解决上述问题，优化应用开发流程，系统针对拍照、录像两类场景（即[Camera_SceneMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_scenemode)为NORMAL_PHOTO或NORMAL_VIDEO），提供了[OH_CameraManager_CreatePreviewOutputUsedInPreconfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_createpreviewoutputusedinpreconfig)、[OH_CameraManager_CreatePhotoOutputUsedInPreconfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_createphotooutputusedinpreconfig)、[OH_CameraManager_CreateVideoOutputUsedInPreconfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_createvideooutputusedinpreconfig)接口帮助开发者快速完成相机参数配置。推荐仅需要自定义拍照界面的无需开发专业相机应用的开发者，使用相机预配置功能快速开发应用。


## 规格说明

系统提供了4种预配置类型（[Camera_PreconfigType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_preconfigtype)），分别为PRECONFIG_720P、PRECONFIG_1080P、PRECONFIG_4K、PRECONFIG_HIGH_QUALITY。以及3种画幅比例规格（[Camera_PreconfigRatio](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_preconfigratio)），1:1画幅（PRECONFIG_RATIO_1_1）、4:3画幅（PRECONFIG_RATIO_4_3）、16:9画幅（PRECONFIG_RATIO_16_9）。
![](assets/使用相机预配置(C／C++)
/file-20260514131532037-0.png)  由于不同的设备所支持的能力不同。使用相机预配置（preconfig）功能时，需要先调用[OH_CaptureSession_CanPreconfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_canpreconfig)或[OH_CaptureSession_CanPreconfigWithRatio](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_canpreconfigwithratio)检查对应的PreconfigType和PreconfigRatio的组合在当前设备上是否支持。   在不同的画幅比例下，其分辨率规格不同，详见下表。 普通拍照模式下的预览输出
| 预配置类型PreconfigType | PRECONFIG_RATIO_1_1 | PRECONFIG_RATIO_4_3 | PRECONFIG_RATIO_16_9 |
| --- | --- | --- | --- |
| PRECONFIG_720P | 720x720 | 960x720 | 1280x720 |
| PRECONFIG_1080P | 1080x1080 | 1440x1080 | 1920x1080 |
| PRECONFIG_4K | 1080x1080 | 1440x1080 | 1920x1080 |
| PRECONFIG_HIGH_QUALITY | 1440x1440 | 1920x1440 | 2560x1440 |

普通拍照模式下的拍照输出
| 预配置类型PreconfigType | PRECONFIG_RATIO_1_1 | PRECONFIG_RATIO_4_3 | PRECONFIG_RATIO_16_9 |
| --- | --- | --- | --- |
| PRECONFIG_720P | 720x720 | 960x720 | 1280x720 |
| PRECONFIG_1080P | 1080x1080 | 1440x1080 | 1920x1080 |
| PRECONFIG_4K | 2160x2160 | 2880x2160 | 3840x2160 |
| PRECONFIG_HIGH_QUALITY | 跟随Sensor最大能力 | 跟随Sensor最大能力 | 跟随Sensor最大能力 |

普通录像模式下的预览输出
| 预配置类型PreconfigType | PRECONFIG_RATIO_1_1 | PRECONFIG_RATIO_4_3 | PRECONFIG_RATIO_16_9 |
| --- | --- | --- | --- |
| PRECONFIG_720P | 720x720 | 960x720 | 1280x720 |
| PRECONFIG_1080P | 1080x1080 | 1440x1080 | 1920x1080 |
| PRECONFIG_4K | 1080x1080 | 1440x1080 | 1920x1080 |
| PRECONFIG_HIGH_QUALITY | 1080x1080 | 1440x1080 | 1920x1080 |

普通录像模式下的录像输出
| 预配置类型PreconfigType | PRECONFIG_RATIO_1_1 | PRECONFIG_RATIO_4_3 | PRECONFIG_RATIO_16_9 |
| --- | --- | --- | --- |
| PRECONFIG_720P | 720x720 | 960x720 | 1280x720 |
| PRECONFIG_1080P | 1080x1080 | 1440x1080 | 1920x1080 |
| PRECONFIG_4K | 2160x2160 | 2880x2160 | 3840x2160 |
| PRECONFIG_HIGH_QUALITY | 2160x2160 | 2880x2160 | 3840x2160 |

普通录像模式下的拍照输出
| 预配置类型PreconfigType | PRECONFIG_RATIO_1_1 | PRECONFIG_RATIO_4_3 | PRECONFIG_RATIO_16_9 |
| --- | --- | --- | --- |
| PRECONFIG_720P | 跟随Sensor最大能力 | 跟随Sensor最大能力 | 跟随Sensor最大能力 |
| PRECONFIG_1080P | 跟随Sensor最大能力 | 跟随Sensor最大能力 | 跟随Sensor最大能力 |
| PRECONFIG_4K | 跟随Sensor最大能力 | 跟随Sensor最大能力 | 跟随Sensor最大能力 |
| PRECONFIG_HIGH_QUALITY | 跟随Sensor最大能力 | 跟随Sensor最大能力 | 跟随Sensor最大能力 |


## 开发示例

在CMake脚本中链接相关动态库。
```text
target_link_libraries(entry PUBLIC libohcamera.so libhilog_ndk.z.so)
```

cpp侧导入NDK接口，并根据传入的SurfaceId进行拍照。
```text
#include "hilog/log.h"
#include "ohcamera/camera.h"
#include "ohcamera/camera_input.h"
#include "ohcamera/capture_session.h"
#include "ohcamera/photo_output.h"
#include "ohcamera/preview_output.h"
#include "ohcamera/video_output.h"
#include "ohcamera/camera_manager.h"
class NDKCamera {
public:
    NDKCamera(char *previewId, char *photoId);
};

void CaptureSessionOnFocusStateChange(Camera_CaptureSession *session, Camera_FocusState focusState) {
    OH_LOG_INFO(LOG_APP, "CaptureSessionOnFocusStateChange");
}

void CaptureSessionOnError(Camera_CaptureSession *session, Camera_ErrorCode errorCode) {
    OH_LOG_INFO(LOG_APP, "CaptureSessionOnError = %{public}d", errorCode);
}

CaptureSession_Callbacks *GetCaptureSessionRegister(void) {
    static CaptureSession_Callbacks captureSessionCallbacks = {.onFocusStateChange = CaptureSessionOnFocusStateChange,
                                                               .onError = CaptureSessionOnError};
    return &captureSessionCallbacks;
}

void PreviewOutputOnFrameStart(Camera_PreviewOutput *previewOutput) {
    OH_LOG_INFO(LOG_APP, "PreviewOutputOnFrameStart");
}

void PreviewOutputOnFrameEnd(Camera_PreviewOutput *previewOutput, int32_t frameCount) {
    OH_LOG_INFO(LOG_APP, "PreviewOutputOnFrameEnd = %{public}d", frameCount);
}

void PreviewOutputOnError(Camera_PreviewOutput *previewOutput, Camera_ErrorCode errorCode) {
    OH_LOG_INFO(LOG_APP, "PreviewOutputOnError = %{public}d", errorCode);
}

PreviewOutput_Callbacks *GetPreviewOutputListener(void) {
    static PreviewOutput_Callbacks previewOutputListener = {.onFrameStart = PreviewOutputOnFrameStart,
                                                            .onFrameEnd = PreviewOutputOnFrameEnd,
                                                            .onError = PreviewOutputOnError};
    return &previewOutputListener;
}

void OnCameraInputError(const Camera_Input *cameraInput, Camera_ErrorCode errorCode) {
    OH_LOG_INFO(LOG_APP, "OnCameraInput errorCode = %{public}d", errorCode);
}

CameraInput_Callbacks *GetCameraInputListener(void) {
    static CameraInput_Callbacks cameraInputCallbacks = {.onError = OnCameraInputError};
    return &cameraInputCallbacks;
}

void CameraManagerStatusCallback(Camera_Manager *cameraManager, Camera_StatusInfo *status) {
    OH_LOG_INFO(LOG_APP, "CameraManagerStatusCallback is called");
}

CameraManager_Callbacks *GetCameraManagerListener() {
    static CameraManager_Callbacks cameraManagerListener = {.onCameraStatus = CameraManagerStatusCallback};
    return &cameraManagerListener;
}

NDKCamera::NDKCamera(char *previewId, char *photoId) {
    Camera_Manager *cameraManager = nullptr;
    Camera_Device *cameras = nullptr;
    Camera_CaptureSession *captureSession = nullptr;
    Camera_PreviewOutput *previewOutput = nullptr;
    Camera_PhotoOutput *photoOutput = nullptr;
    Camera_Input *cameraInput = nullptr;
    uint32_t size = 0;
    uint32_t cameraDeviceIndex = 0;
    char *previewSurfaceId = previewId;
    char *photoSurfaceId = photoId;
    // 创建CameraManager对象
    Camera_ErrorCode ret = OH_Camera_GetCameraManager(&cameraManager);
    if (cameraManager == nullptr || ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_Camera_GetCameraMananger failed.");
    }
    // 监听相机状态变化
    ret = OH_CameraManager_RegisterCallback(cameraManager, GetCameraManagerListener());
    if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_CameraManager_RegisterCallback failed.");
    }

    // 获取相机列表
    ret = OH_CameraManager_GetSupportedCameras(cameraManager, &cameras, &size);
    if (cameras == nullptr || size
