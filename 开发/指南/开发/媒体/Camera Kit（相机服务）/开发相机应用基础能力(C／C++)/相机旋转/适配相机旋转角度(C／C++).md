# 适配相机旋转角度(C/C++)

更新时间：2026-08-03 11:34:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-rotation-angle-adaptation-native

屏幕处于不同的屏幕状态时，原始图像需旋转不同的角度，以确保图像在合适的方向显示，效果如图所示。


![](assets/适配相机旋转角度(C／C++)/file-20260514131530739-0.png)


本开发指导将指导开发者在预览、拍照、录像等不同场景下，如何适配相机的旋转角度。

 - 在预览时，图像旋转角度与屏幕显示旋转角度（[NativeDisplayManager_Rotation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_rotation)）相关。具体开发指导：[创建会话](#创建会话) > [预览](#预览)。
 - 在拍照、录像时，图像旋转角度与设备重力方向（即[设备旋转角度](#计算设备旋转角度)）相关。

  拍照开发指导：[创建会话](#创建会话) > [计算设备旋转角度](#计算设备旋转角度) > [拍照](#拍照)。

  录像开发指导：[创建会话](#创建会话) > [计算设备旋转角度](#计算设备旋转角度) > [录像](#录像)。


在本开发指导中，提供两种方案来获取预览、拍照、录像的旋转角度：

 - 方案一：需要应用通过[OH_NativeDisplayManager_GetDefaultDisplayRotation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-manager-h#oh_nativedisplaymanager_getdefaultdisplayrotation)接口获取[显示设备的屏幕旋转角度](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-rotation-term#屏幕旋转角度)，通过重力传感器来[计算设备旋转角度](#计算设备旋转角度)。
 - 方案二：从API版本23开始，支持通过[OH_PreviewOutput_GetPreviewRotationWithoutDisplayRotation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-preview-output-h#oh_previewoutput_getpreviewrotationwithoutdisplayrotation)、[OH_PhotoOutput_GetPhotoRotationWithoutDeviceDegree](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-photo-output-h#oh_photooutput_getphotorotationwithoutdevicedegree)、[OH_VideoOutput_GetVideoRotationWithoutDeviceDegree](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-output-h#oh_videooutput_getvideorotationwithoutdevicedegree)接口来获取旋转角度，由系统侧获取[显示设备的屏幕旋转角度](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-rotation-term#屏幕旋转角度)和[计算设备旋转角度](#计算设备旋转角度)。如果应用涉及使用USB相机或在多屏场景下，建议使用方案二。


详细的API参考说明，请参考[Camera API文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)。


#### 创建会话
1. 导入相机等相关模块。

  
```text
#include "hilog/log.h"
#include "ohcamera/camera.h"
#include "ohcamera/camera_manager.h"
#include "ohcamera/capture_session.h"
```

2. 创建Session会话。

  相机使用预览等功能前，均需创建相机会话，调用[camera_manager.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-manager-h)中的[OH_CameraManager_CreateCaptureSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_createcapturesession)方法创建一个会话，创建会话时需指定创建[Camera_SceneMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_scenemode)为NORMAL_PHOTO或NORMAL_VIDEO，创建的session处于拍照或者录像模式。

  
```text
void createPhotosession(Camera_Manager *cameraManager) {
    Camera_CaptureSession *captureSession;
    Camera_SceneMode sceneMode = NORMAL_PHOTO;
    Camera_ErrorCode ret = OH_CameraManager_CreateCaptureSession(cameraManager, &captureSession);
    if (captureSession == nullptr || ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "Create captureSession failed.");
    }
    ret = OH_CaptureSession_SetSessionMode(captureSession, sceneMode);
    if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_SetSessionMode failed.");
    }
}

void createVideosession(Camera_Manager *cameraManager) {
    Camera_CaptureSession *captureSession;
    Camera_SceneMode sceneMode = NORMAL_VIDEO;
    Camera_ErrorCode ret = OH_CameraManager_CreateCaptureSession(cameraManager, &captureSession);
    if (captureSession == nullptr || ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "Create captureSession failed.");
    }
    ret = OH_CaptureSession_SetSessionMode(captureSession, sceneMode);
    if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_SetSessionMode failed.");
    }
}
```




#### 预览

完成[会话创建](#创建会话)后，开发者可根据实际需求，配置输出流。
1. 在[会话管理](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-session-management)过程中获取并设置[预览旋转角度](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-rotation-term#预览旋转角度)，即：使用[OH_CaptureSession_CommitConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_commitconfig)接口提交相关配置后调用，建议在[OH_CaptureSession_Start](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_start)起流前调用。

  **接口说明**       
通过调用[preview_output.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-preview-output-h)中的[OH_PreviewOutput_GetPreviewRotation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-preview-output-h#oh_previewoutput_getpreviewrotation)接口或[OH_PreviewOutput_GetPreviewRotationWithoutDisplayRotation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-preview-output-h#oh_previewoutput_getpreviewrotationwithoutdisplayrotation)接口，获取预览旋转角度。
2. 通过调用[preview_output.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-preview-output-h)中的[OH_PreviewOutput_SetPreviewRotation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-preview-output-h#oh_previewoutput_setpreviewrotation)，设置预览旋转角度。如果多次调用，以最新调用设置的预览旋转角度为准。
3. 上述三个接口需要在session调用[OH_CaptureSession_CommitConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_commitconfig)完成配流后调用，如果存在异步执行的情况，previewOutput未添加到session里或者已调用[OH_CaptureSession_Release](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_release)，导致session与PreviewOutput两者关系未绑定，此时调用接口会调用失败，并抛出错误码[CAMERA_SERVICE_FATAL_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera#section7400201-相机服务异常)。
4. **方案一：**

  由应用通过[OH_NativeDisplayManager_GetDefaultDisplayRotation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-manager-h#oh_nativedisplaymanager_getdefaultdisplayrotation)接口获取displayRotation（[显示设备的屏幕旋转角度](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-rotation-term-native#屏幕旋转角度)），并将对应角度填入[OH_PreviewOutput_GetPreviewRotation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-preview-output-h#oh_previewoutput_getpreviewrotation)接口。

  例如，OH_NativeDisplayManager_GetDefaultDisplayRotation获取结果为1，表示显示设备屏幕顺时针旋转为90°，此处displayRotation填入90。

  
isDisplayLocked：Surface在屏幕旋转时是否锁定方向。当设置为false，即屏幕方向未锁定，[预览旋转角度](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-rotation-term-native#预览旋转角度)将根据[相机镜头角度](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-rotation-term-native#相机镜头安装角度)和[屏幕显示旋转角度](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-rotation-term-native#屏幕旋转角度)的值计算；当设置为true，Surface旋转锁定，不跟随窗口变化，旋转角度仅取相机镜头角度计算。

  
```cpp
int32_t NDKCamera::GetDefaultDisplayRotation()
{
    int32_t imageRotation = 0;
    NativeDisplayManager_Rotation displayRotation = DISPLAY_MANAGER_ROTATION_0;
    int32_t ret = OH_NativeDisplayManager_GetDefaultDisplayRotation(&displayRotation);
    if (ret != DISPLAY_MANAGER_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_NativeDisplayManager_GetDefaultDisplayRotation failed.");
    }
    imageRotation = displayRotation * IAMGE_ROTATION_90;
    return imageRotation;
}

void NDKCamera::GetAndSetPreviewRotation()
{
    // previewOutput_是创建的预览输出
    Camera_ImageRotation previewRotation = IAMGE_ROTATION_0;
    int32_t imageRotation = GetDefaultDisplayRotation();
    Camera_ErrorCode ret = OH_PreviewOutput_GetPreviewRotation(previewOutput_, imageRotation, &previewRotation);
    if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_PreviewOutput_GetPreviewRotation failed.");
    }
    bool isDisplayLocked = false; // 建议与setXComponentSurfaceRotation入参的lock属性保持一致
    ret = OH_PreviewOutput_SetPreviewRotation(previewOutput_, previewRotation, isDisplayLocked);
    if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_PreviewOutput_SetPreviewRotation failed.");
    }
}
```

5. **方案二：**

  从API版本23开始，可通过[OH_PreviewOutput_GetPreviewRotationWithoutDisplayRotation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-preview-output-h#oh_previewoutput_getpreviewrotationwithoutdisplayrotation)接口，获取预览旋转角度。该方案由系统获取displayRotation，并进行预览旋转角度计算。如果应用涉及使用USB相机或在多屏场景下，建议使用方案二。

  
isDisplayLocked：Surface在屏幕旋转时是否锁定方向。当设置为false，即屏幕方向未锁定，[预览旋转角度](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-rotation-term-native#预览旋转角度)将根据[相机镜头角度](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-rotation-term-native#相机镜头安装角度)和[屏幕显示旋转角度](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-rotation-term-native#屏幕旋转角度)的值计算；当设置为true，Surface旋转锁定，不跟随窗口变化，旋转角度仅取相机镜头角度计算。

  
```cpp
void NDKCamera::GetAndSetPreviewRotationWithoutDisplayRotation()
{
    // previewOutput_是创建的预览输出
    Camera_ImageRotation previewRotation = IAMGE_ROTATION_0;
    Camera_ErrorCode ret = OH_PreviewOutput_GetPreviewRotationWithoutDisplayRotation(previewOutput_, &previewRotation);
    if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_PreviewOutput_GetPreviewRotationWithoutDisplayRotation failed.");
    }
    bool isDisplayLocked = false; // 建议与setXComponentSurfaceRotation入参的lock属性保持一致
    ret = OH_PreviewOutput_SetPreviewRotation(previewOutput_, previewRotation, isDisplayLocked);
    if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_PreviewOutput_SetPreviewRotation failed.");
    }
}
```

6. 通过[监听屏幕状态变化](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-display-manager)，感知窗口当前状态，如当前相机窗口发生旋转时，需对预览流进行角度修正。推荐在[会话管理](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-session-management)中完成调用预览旋转接口后，直接创建监听。

  
**方案一：**

  由应用获取displayRotation（[显示设备的屏幕旋转角度](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-rotation-term-native#屏幕旋转角度)）并将对应角度填入[OH_PreviewOutput_GetPreviewRotation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-preview-output-h#oh_previewoutput_getpreviewrotation)接口。

  
```cpp
// 应用需监听屏幕状态变化，使用如下回调函数对预览流进行角度修正
void NDKCamera::DisplayChangeCallback(uint64_t displayId)
{
    // previewOutput是创建的预览输出
    OH_LOG_INFO(LOG_APP, "DisplayChangeCallback displayId=%{public}lu.", displayId);
    Camera_ImageRotation previewRotation = IAMGE_ROTATION_0;
    int32_t imageRotation = GetDefaultDisplayRotation();
    Camera_ErrorCode ret = OH_PreviewOutput_GetPreviewRotation(previewOutput_, imageRotation, &previewRotation);
    if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_PreviewOutput_GetPreviewRotation failed.");
    }
    bool isDisplayLocked = false; // 建议与setXComponentSurfaceRotation入参的lock属性保持一致
    ret = OH_PreviewOutput_SetPreviewRotation(previewOutput_, previewRotation, isDisplayLocked);
    if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_PreviewOutput_SetPreviewRotation failed.");
    }
}
```

7. **方案二：**

  从API版本23开始，可通过[OH_PreviewOutput_GetPreviewRotationWithoutDisplayRotation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-preview-output-h#oh_previewoutput_getpreviewrotationwithoutdisplayrotation)接口，获取预览旋转角度。该方案由系统获取displayRotation，并进行预览旋转角度计算。如果应用涉及使用USB相机或在多屏场景下，建议使用方案二。

  
```cpp
// 应用需监听屏幕状态变化，使用如下回调函数对预览流进行角度修正
void NDKCamera::DisplayChangeCallback(uint64_t displayId)
{
    // previewOutput是创建的预览输出
    OH_LOG_INFO(LOG_APP, "DisplayChangeCallback displayId=%{public}lu.", displayId);
    Camera_ImageRotation previewRotation = IAMGE_ROTATION_0;
    int32_t imageRotation = GetDefaultDisplayRotation();
    Camera_ErrorCode ret = OH_PreviewOutput_GetPreviewRotation(previewOutput_, imageRotation, &previewRotation);
    if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_PreviewOutput_GetPreviewRotation failed.");
    }
    bool isDisplayLocked = false; // 建议与setXComponentSurfaceRotation入参的lock属性保持一致
    ret = OH_PreviewOutput_SetPreviewRotation(previewOutput_, previewRotation, isDisplayLocked);
    if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_PreviewOutput_SetPreviewRotation failed.");
    }
}
```




#### 拍照

完成[会话创建](#创建会话)后，开发者可根据实际需求，配置输出流。
1. 获取拍照旋转角度。

  
**方案一：**

  调用[photo_output.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-photo-output-h)中的[OH_PhotoOutput_GetPhotoRotation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-photo-output-h#oh_photooutput_getphotorotation)可以获取到拍照旋转角度。该接口需要在session调用[OH_CaptureSession_CommitConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_commitconfig)完成配流后调用。

  deviceDegree：设备旋转角度。拍照的旋转角度与重力方向（即设备旋转角度）相关，获取方式请见[计算设备旋转角度](#计算设备旋转角度)。

  
```cpp
Camera_ImageRotation NDKCamera::GetPhotoRotation(Camera_PhotoOutput* photoOutput, int32_t deviceDegree)
{
    Camera_ImageRotation photoRotation = IAMGE_ROTATION_0;
    Camera_ErrorCode ret = OH_PhotoOutput_GetPhotoRotation(photoOutput, deviceDegree, &photoRotation);
    if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_PhotoOutput_GetPhotoRotation failed.");
    }
    return photoRotation;
}
```

2. **方案二：**

  从API版本23开始，可调用[photo_output.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-photo-output-h)中的[OH_PhotoOutput_GetPhotoRotationWithoutDeviceDegree](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-photo-output-h#oh_photooutput_getphotorotationwithoutdevicedegree)可以获取到拍照旋转角度。由系统获取deviceDegree进行拍照旋转角度计算。当重力传感器数据无效，无法计算deviceDegree时，系统将使用最后一次有效的deviceDegree。如果应用涉及使用USB相机或在多屏场景下，建议使用方案二。

  该接口需要在session调用[OH_CaptureSession_CommitConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_commitconfig)完成配流后调用。

  
```cpp
Camera_ImageRotation NDKCamera::GetPhotoRotationWithoutDeviceDegree(Camera_PhotoOutput* photoOutput)
{
    Camera_ImageRotation photoRotation = IAMGE_ROTATION_0;
    Camera_ErrorCode ret = OH_PhotoOutput_GetPhotoRotationWithoutDeviceDegree(photoOutput, &photoRotation);
    if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_PhotoOutput_GetPhotoRotationWithoutDeviceDegree failed.");
    }
    return photoRotation;
}
```

3. 应用将拍照角度写入[Camera_PhotoCaptureSetting](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-photocapturesetting)的rotation。
4. 其余参数的配置及拍照，可参考[拍照开发指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-shooting)。



#### 录像

完成[会话创建](#创建会话)后，开发者可根据实际需求，配置输出流。
1. 获取录像旋转角度。

  
**方案一：**

  调用[video_output.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-output-h)中的[OH_VideoOutput_GetVideoRotation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-output-h#oh_videooutput_getvideorotation)可以获取到录像的旋转角度。该接口需要在session调用[OH_CaptureSession_CommitConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_commitconfig)完成配流后调用。

  deviceDegree：设备旋转角度。录像的旋转角度与重力方向（即设备旋转角度）相关，获取方式请见[计算设备旋转角度](#计算设备旋转角度)。

  
```cpp
Camera_ImageRotation NDKCamera::GetVideoRotation(int32_t deviceDegree)
{
    Camera_ImageRotation videoRotation = IAMGE_ROTATION_0;
    Camera_ErrorCode ret = OH_VideoOutput_GetVideoRotation(videoOutput_, deviceDegree, &videoRotation);
    if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_VideoOutput_GetVideoRotation failed.");
    }
    return videoRotation;
}
```

2. **方案二：**

  从API版本23开始，可调用[video_output.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-output-h)中的[OH_VideoOutput_GetVideoRotationWithoutDeviceDegree](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-output-h#oh_videooutput_getvideorotationwithoutdevicedegree)可以获取到录像的旋转角度。由系统获取deviceDegree进行录像旋转角度计算。当重力传感器数据无效，无法计算deviceDegree时，系统将使用最后一次有效的deviceDegree。如果应用涉及使用USB相机或在多屏场景下，建议使用方案二。

  该接口需要在session调用[OH_CaptureSession_CommitConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_commitconfig)完成配流后调用。

  
```cpp
Camera_ImageRotation NDKCamera::GetVideoRotationWithoutDeviceDegree()
{
    Camera_ImageRotation videoRotation = IAMGE_ROTATION_0;
    Camera_ErrorCode ret = OH_VideoOutput_GetVideoRotationWithoutDeviceDegree(videoOutput_, &videoRotation);
    if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_VideoOutput_GetVideoRotationWithoutDeviceDegree failed.");
    }
    return videoRotation;
}
```

3. 在[OH_AVRecorder_Prepare](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-h#oh_avrecorder_prepare)后使用[OH_AVRecorder_UpdateRotation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-h#oh_avrecorder_updaterotation)设置录像角度。
4. 其余参数的配置及启动录像，可参考[录像开发指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-recording)。



#### 计算设备旋转角度

当前可通过监听[OH_Sensor_Subscribe](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-sensor-h#oh_sensor_subscribe)获取重力传感器在x、y、z三个方向上的数据，计算得出设备旋转角度deviceDegree，示例如下所示。

如果无法获得重力传感器数据，需要申请重力传感器权限ohos.permission.ACCELEROMETER。权限申请请参考[声明权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions)，如何获取传感器数据请参考[传感器开发指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sensor-guidelines-capi)。

```cpp
Sensor_SubscriptionId *id;
Sensor_Subscriber *subscriber;
Sensor_SubscriptionAttribute *attr;

// Sensor获取方式为注册监听获取单次数据后解注册,监听回调为异步触发,等待g_isDegreeReady设置为true后说明获取设备角度成功;
// 角度保存在g_deviceDegree,使用角度后将g_isDegreeReady置为false;
float g_deviceDegree = 0.0f;
bool g_isDegreeReady = false;

float GetDeviceDegreeFromXYZ(float x, float y, float z)
{
    // 判断条件 (x * x + y * y) * 3 < z * z
    if ((x * x + y * y) * 3 < z * z) {
        return -1.0f;
    } else {
        // 计算 atan2(y, -x) 并转换为角度
        float sd = std::atan2(y, -x);                      // 返回弧度
        float sc = std::round(sd / 3.141592653589f * 180); // 转换为角度并四舍五入
        float getDeviceDegree = 90.0f - sc;

        // 保证角度在 0 到 360 之间
        if (getDeviceDegree >= 0) {
            getDeviceDegree = fmod(getDeviceDegree, 360.0f); // 取模，保证结果在 0 到 360 之间
        } else {
            getDeviceDegree = fmod(getDeviceDegree, 360.0f) + 360.0f; // 如果小于0，加上360
        }
        OH_LOG_INFO(LOG_APP, "GetDeviceDegreeFromXYZ getDeviceDegree:%{public}f", getDeviceDegree);
        return getDeviceDegree;
    }
}

void SensorDataCallback(Sensor_Event *event)
{
    OH_LOG_INFO(LOG_APP, "SensorDataCallbackImpl start");
    // SENSOR_TYPE_GRAVITY:data[0]、data[1]、data[2]分别表示设备x、y、z轴的重力加速度分量，单位m/s²；
    float *data = nullptr;
    uint32_t length = 0;
    OH_SensorEvent_GetData(event, &data, &length); // 获取传感器数据。
    for (uint32_t i = 0; i < length; ++i) {
        OH_LOG_INFO(LOG_APP, "SensorDataCallbackImpl data[%{public}d]:%{public}f", i, data[i]);
    }
    float x = data[0];
    float y = data[1];
    float z = data[2];
    g_deviceDegree = GetDeviceDegreeFromXYZ(x, y, z);
    g_isDegreeReady = true;

    OH_Sensor_Unsubscribe(id, subscriber); // 取消订阅传感器数据。
    if (id != nullptr) {
        OH_Sensor_DestroySubscriptionId(id); // 销毁Sensor_SubscriptionId实例并回收内存。
    }
    if (attr != nullptr) {
        OH_Sensor_DestroySubscriptionAttribute(attr); // 销毁Sensor_SubscriptionAttribute实例并回收内存。
    }
    if (subscriber != nullptr) {
        OH_Sensor_DestroySubscriber(subscriber); // 销毁Sensor_Subscriber实例并回收内存。
        subscriber = nullptr;
    }
}

void GetCurGravity()
{
    Sensor_Type SENSOR_ID{ SENSOR_TYPE_GRAVITY };
    id = OH_Sensor_CreateSubscriptionId(); // 创建一个Sensor_SubscriptionId实例。
    if (id == nullptr) {
        OH_LOG_ERROR(LOG_APP, "OH_Sensor_CreateSubscriptionId error");
    }
    int32_t res = OH_SensorSubscriptionId_SetType(id, SENSOR_ID); // 设置传感器类型为重力。
    if (res != 0) {
        OH_LOG_ERROR(LOG_APP, "OH_SensorSubscriptionId_SetType error");
    }
    attr = OH_Sensor_CreateSubscriptionAttribute(); // 创建Sensor_SubscriptionAttribute实例。
    if (attr == nullptr) {
        OH_LOG_ERROR(LOG_APP, "OH_Sensor_CreateSubscriptionAttribute error");
    }
    int64_t sensorSamplePeriod = 15000000;
    res = OH_SensorSubscriptionAttribute_SetSamplingInterval(attr, sensorSamplePeriod); // 设置传感器数据报告间隔。
    if (res != 0) {
        OH_LOG_ERROR(LOG_APP, "OH_SensorSubscriptionAttribute_SetSamplingInterval error");
    }
    subscriber = OH_Sensor_CreateSubscriber();
    if (subscriber == nullptr) {
        OH_LOG_ERROR(LOG_APP, "OH_Sensor_CreateSubscriber error");
    }

    OH_SensorSubscriber_SetCallback(subscriber, SensorDataCallback);
    Sensor_Result sensorRes = OH_Sensor_Subscribe(id, attr, subscriber); // 订阅传感器数据。
    if (sensorRes != SENSOR_SUCCESS) {
        OH_LOG_INFO(LOG_APP, "OH_Sensor_Subscribe error");
    }
}

int32_t CalDeviceDegree()
{
    float deviceDegree = 0.0f;
    GetCurGravity();
    while (!g_isDegreeReady) {
        std::this_thread::sleep_for(std::chrono::milliseconds(NUM_TEN));
    }
    deviceDegree = g_deviceDegree;
    g_isDegreeReady = false;
    return deviceDegree;
}
```



#### 视频通话送远端场景

两个设备之间进行视频通话，存在设备间持握方向不一致问题，建议**在本端将画面转正**，再通过网络发送到对端。



#### 实现相机无损出图

在部分折叠屏设备上，[不同折叠状态](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#foldstatus10)下的[设备自然方向](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-rotation-term-native#设备自然方向)会发生改变，导致不同折叠状态下的[相机镜头安装角度](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-rotation-term-native#相机镜头安装角度)不同。为了屏蔽不同设备间的差异，使得不同折叠状态下的相机镜头安装角度一致，系统会自动调整部分折叠状态下的相机采集图像方向（通过旋转裁切的方式）和相机镜头安装角度，因此会存在视场角（Field of View, FOV）损失，可能会导致相机预览、拍照、录像可见范围降低，因此如果需要实现相机无损出图，可以通过[OH_CameraInput_UsePhysicalCameraOrientation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_createcamerainput)接口来实现相机无损出图。具体方式如下：

设备是否支持无损出图，首先需要确认设备的相机镜头安装角度是否可变，可以通过[OH_CameraInput_IsPhysicalCameraOrientationVariable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-input-h#oh_camerainput_isphysicalcameraorientationvariable)接口查询。
1. 当相机镜头安装角度不可变时，不同折叠状态下的相机出图均为无损出图。
2. 当相机镜头安装角度可变时：

  如应用需要实现相机无损出图，由于相机镜头安装角度与相机旋转相关，需要应用完成[相机旋转的适配](#top)后，通过[OH_CameraInput_GetPhysicalCameraOrientation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-input-h#oh_camerainput_getphysicalcameraorientation)接口获取设备当前折叠状态下真实的相机镜头安装角度，并通过[OH_CameraInput_UsePhysicalCameraOrientation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-input-h#oh_camerainput_usephysicalcameraorientation)接口实现相机无损出图（相机镜头安装角度不可变时使用[OH_CameraInput_UsePhysicalCameraOrientation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-input-h#oh_camerainput_usephysicalcameraorientation)将会返回[7400102](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera#section7400102-非法操作)错误码，未适配相机旋转时使用相机无损出图会导致预览、拍照、录像旋转异常），推荐在[OH_CameraManager_CreateCameraInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_createcamerainput)后直接使用[OH_CameraInput_UsePhysicalCameraOrientation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_createcamerainput)接口实现相机无损出图。

示例代码如下：

```cpp
Camera_ErrorCode NDKCamera::EnablePhysicalCameraOrientation(Camera_Input* cameraInput)
{
    bool isVariable = false;
    // 查询设备的相机镜头安装角度是否可变
    Camera_ErrorCode ret = OH_CameraInput_IsPhysicalCameraOrientationVariable(cameraInput, &isVariable);
    if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_CameraInput_IsPhysicalCameraOrientationVariable failed.");
        return ret;
    }
    if (!isVariable) {
        OH_LOG_INFO(LOG_APP, "Physical Camera Orientation is not variable.");
        return CAMERA_OK;
    }
    // 获取设备当前折叠状态下真实的相机镜头安装角度
    uint32_t physicalOrientation = 0;
    ret = OH_CameraInput_GetPhysicalCameraOrientation(cameraInput, &physicalOrientation);
    if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_CameraInput_GetPhysicalCameraOrientation failed.");
        return ret;
    }
    // 选择是否使用真实的相机镜头安装角度, 以实现无损出图
    bool isUsed = true;
    ret = OH_CameraInput_UsePhysicalCameraOrientation(cameraInput, isUsed);
    if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_CameraInput_UsePhysicalCameraOrientation failed.");
        return ret;
    }
    return ret;
}
```
