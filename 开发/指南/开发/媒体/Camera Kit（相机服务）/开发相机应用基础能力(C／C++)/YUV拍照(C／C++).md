# YUV拍照(C/C++)

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-yuv-shooting

从API version 23开始，相机框架提供YUV格式图片拍照能力。与普通拍照相比，YUV拍照获取到的是未经过编码的图像数据，完整保留了传感器捕获的原始亮度和色度信息，适用于视频编码或专业处理。同时，拍摄过程会产生更高的能耗开销，保存会占用更多的存储空间。


#### 开发步骤

详细的相机功能API说明请参考Camera模块描述[OH_Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)。
1. 导入NDK接口，接口中提供了相机相关的属性和方法，导入方法如下。

  
```text
// 导入NDK接口头文件。
#include <cstdint>
#include <cstdlib>
#include <cstring>
#include <string.h>
#include <new>
#include "hilog/log.h"
#include "multimedia/image_framework/image/image_source_native.h"
#include "multimedia/image_framework/image/image_packer_native.h"
#include "multimedia/media_library/media_access_helper_capi.h"
#include "multimedia/media_library/media_asset_base_capi.h"
#include "multimedia/media_library/media_asset_capi.h"
#include "multimedia/media_library/media_asset_change_request_capi.h"
#include "multimedia/media_library/media_asset_manager_capi.h"
#include "ohcamera/camera.h"
#include "ohcamera/camera_input.h"
#include "ohcamera/camera_manager.h"
#include "ohcamera/capture_session.h"
#include "ohcamera/photo_native.h"
#include "ohcamera/photo_output.h"
#include "ohcamera/preview_output.h"
#include "ohcamera/video_output.h"
```

2. 在CMake脚本中链接相关动态库。

  
```text
target_link_libraries(entry PUBLIC
    libace_napi.z.so
    libhilog_ndk.z.so
    libnative_buffer.so
    libohcamera.so
    libohimage.so
    libohfileuri.so
    libmedia_asset_manager.so
    libimage_source.so
    libpixelmap.so
    libimage_packer.so
    libpicture.so
)
```

3. 创建并打开相机设备，参考[设备输入(C/C++)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-device-input)中的步骤3-4。
4. 获取相机设备完整输出能力。

  通过[OH_CameraManager_GetSupportedFullCameraOutputCapabilityWithSceneMode()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_getsupportedfullcameraoutputcapabilitywithscenemode)方法，获取当前设备支持的所有输出流的能力，包含预览流、拍照流、录像流等。输出流在CameraOutputCapability中的各个profile字段中，其中拍照流支持YUV格式。根据相机设备指定模式[Camera_SceneMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_scenemode)的不同，需要添加不同类型的输出流。

  
```text
Camera_OutputCapability* GetSupportedFullCameraOutputCapability(Camera_Manager* cameraManager, Camera_Device &camera)
{
     Camera_OutputCapability* cameraOutputCapability = nullptr;
     // 获取相机设备支持的输出流能力。
     const Camera_Profile* previewProfile = nullptr;
     const Camera_Profile* photoProfile = nullptr;
     Camera_ErrorCode ret = OH_CameraManager_GetSupportedFullCameraOutputCapabilityWithSceneMode(cameraManager, &camera,
         Camera_SceneMode::NORMAL_PHOTO, &cameraOutputCapability);
     if (cameraOutputCapability == nullptr || ret != CAMERA_OK) {
         OH_LOG_ERROR(LOG_APP, "OH_CameraManager_GetSupportedCameraOutputCapability failed.");
         return nullptr;
     }
     return cameraOutputCapability;
}
```

5. 选择设备支持的输出流能力，创建拍照输出流。

  通过[OH_CameraManager_CreatePhotoOutputWithoutSurface()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_createphotooutputwithoutsurface)方法创建拍照输出流。

  可以通过[OH_CameraManager_GetSupportedFullCameraOutputCapabilityWithSceneMode()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_getsupportedfullcameraoutputcapabilitywithscenemode)获取相机在指定模式下支持的完整输出能力cameraOutputCapability，参考步骤2。在cameraOutputCapability的photoProfiles中选择支持YUV格式的profile，作为创建拍照输出流的参数photoProfile。

  
```text
Camera_PhotoOutput* CreatePhotoOutput(Camera_Manager* cameraManager, const Camera_Profile* photoProfile)
{
    Camera_PhotoOutput* photoOutput = nullptr;
    // 无需传入surfaceId，直接创建拍照流。
    Camera_ErrorCode ret = OH_CameraManager_CreatePhotoOutputWithoutSurface(cameraManager, photoProfile, &photoOutput);
    if (photoOutput == nullptr || ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreatePhotoOutputWithoutSurface failed.");
    }
    return photoOutput;
}
```

6. 注册单段式(PhotoAvailable)或分段式(PhotoAssetAvailable)拍照回调，若应用希望快速得到回图，推荐使用[分段式拍照(PhotoAssetAvailable)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-deferred-capture)回调。

  
![](assets/YUV拍照(C／C++)/file-20260514131530082-0.png)
 

  如果已经注册了PhotoAssetAvailable回调，并且在Session开始之后又注册了PhotoAvailable回调，PhotoAssetAvailable和PhotoAvailable同时注册会导致流被重启，仅PhotoAssetAvailable生效。

  
 - **单段式拍照（PhotoAvailable）开发流程**：

  
在会话[OH_CaptureSession_CommitConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_commitconfig)前注册单段式拍照回调。

7. 在单段式拍照回调函数中获取图片信息，解析出pixelMap数据，做自定义业务处理。

8. 将处理完的pixelMap通过回调传给ArkTS侧，做图片显示或通过安全控件写文件保存图片。

9. 使用完后解注册单段式拍照回调函数。

10. **分段式拍照（PhotoAvailable）开发流程**：

  
在会话[OH_CaptureSession_CommitConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_commitconfig)前注册分段式拍照回调。

11. 在分段式拍照回调函数中获取图片信息，解析出pixelMap数据，做自定义业务处理。

12. 将处理完的pixelMap通过回调传给ArkTS侧，做图片显示或通过安全控件写文件保存图片。

13. 调用[OH_PhotoOutput_Capture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-photo-output-h#oh_photooutput_capture)拍照后，需要及时调用[OH_MediaAssetChangeRequest_SaveCameraPhoto](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-media-asset-change-request-capi-h#oh_mediaassetchangerequest_savecameraphoto)保存图片或[OH_MediaAssetChangeRequest_DiscardCameraPhoto](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-media-asset-change-request-capi-h#oh_mediaassetchangerequest_discardcameraphoto)取消保存图片，否则会影响后续图片的拍摄。

14. 使用完后解注册分段式拍照回调函数。

15. 创建拍照类型会话（参考[会话管理(C/C++)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-session-management)），开启会话，准备拍照。

16. 触发拍照。

  通过[OH_PhotoOutput_Capture()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-photo-output-h#oh_photooutput_capture)方法，执行拍照任务。

  
```text
Camera_ErrorCode Capture(Camera_PhotoOutput* photoOutput)
{
    Camera_ErrorCode ret = OH_PhotoOutput_Capture(photoOutput);
    if (ret == CAMERA_OK) {
        OH_LOG_INFO(LOG_APP, "OH_PhotoOutput_Capture success ");
    } else {
        OH_LOG_ERROR(LOG_APP, "OH_PhotoOutput_Capture failed. %d ", ret);
    }
    return ret;
}
```


  

  #### 状态监听

  在相机应用开发过程中，可以随时监听拍照输出流状态，包括拍照流开始、拍照帧的开始与结束、拍摄下一张图片是否就绪、拍照输出流的错误。

  
通过注册固定的onFrameStart回调函数获取监听拍照开始结果，当photoOutput创建成功时，即可监听。拍照第一次曝光时触发。

  
```text
void PhotoOutputOnFrameStart(Camera_PhotoOutput* photoOutput)
{
    OH_LOG_INFO(LOG_APP, "PhotoOutputOnFrameStart");
}
void PhotoOutputOnFrameShutter(Camera_PhotoOutput* photoOutput, Camera_FrameShutterInfo* info)
{
    OH_LOG_INFO(LOG_APP, "PhotoOutputOnFrameShutter");
}
```

 - 通过注册固定的onFrameEnd回调函数监听拍照结束结果，当photoOutput创建成功时，即可监听。

  
```text
void PhotoOutputOnFrameEnd(Camera_PhotoOutput* photoOutput, int32_t frameCount)
{
    OH_LOG_INFO(LOG_APP, "PhotoOutput frameCount = %{public}d", frameCount);
}
```

 - 通过注册固定的captureReady回调函数监听能否继续拍摄下一张的结果，当photoOutput创建成功时，即可监听。当下一张可拍时触发，该事件返回结果为下一张可拍的相关信息。

  
```text
static bool g_captureReadyFlag = false;
void CaptureReadyCb(Camera_PhotoOutput* photoOutput) {
  g_captureReadyFlag = true;
  OH_LOG_INFO(LOG_APP, "PhotoOutputOnCaptureReady captureReadyFlag = %{public}d", g_captureReadyFlag);
}

void OnPhotoOutputOnCaptureReady(Camera_PhotoOutput* photoOutput)
{
    OH_LOG_INFO(LOG_APP, "PhotoOutputOnCaptureReady");
    Camera_ErrorCode ret = OH_PhotoOutput_RegisterCaptureReadyCallback(photoOutput, CaptureReadyCb);
}
```

 - 通过注册固定的onError回调函数获取监听拍照输出流的错误结果。callback返回拍照输出接口使用错误时的对应错误码，错误码类型参见[Camera_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_errorcode)。

  
```text
void PhotoOutputOnError(Camera_PhotoOutput* photoOutput, Camera_ErrorCode errorCode)
{
    OH_LOG_INFO(LOG_APP, "PhotoOutput errorCode = %{public}d", errorCode);
}
```

```text
PhotoOutput_Callbacks* GetPhotoOutputListener()
{
    static PhotoOutput_Callbacks photoOutputListener = {
        .onFrameStart = PhotoOutputOnFrameStart,
        .onFrameShutter = PhotoOutputOnFrameShutter,
        .onFrameEnd = PhotoOutputOnFrameEnd,
        .onError = PhotoOutputOnError
    };
    return &photoOutputListener;
}
Camera_ErrorCode RegisterPhotoOutputCallback(Camera_PhotoOutput* photoOutput)
{
    Camera_ErrorCode ret = OH_PhotoOutput_RegisterCallback(photoOutput, GetPhotoOutputListener());
    if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_PhotoOutput_RegisterCallback failed.");
    }
    return ret;
}
```
