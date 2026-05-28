# 分段式拍照(C/C++)

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-deferred-capture

分段式拍照是相机的最重要功能之一，相机输出低质量图用作快速显示，提升用户感知拍照速度，同时使用高质量图保证最后的成图质量达到系统相机的水平，既满足了后处理算法的需求，又不阻塞前台的拍照速度，构筑相机性能竞争力，提升了用户的体验。

 - 在第一阶段，系统快速上报轻量处理的图片，轻量处理的图片比全质量图低，出图速度快。应用通过回调会收到一个PhotoAsset对象，通过该对象可调用媒体库接口，读取图片或落盘图片。
 - 在第二阶段，相机框架会根据应用的请求图片诉求或者在系统闲时，进行图像增强处理得到全质量图，将处理好的图片传回给媒体库，替换轻量处理的图片。



##### 开发步骤

详细的API说明请参考[OH_Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)。
1. 导入NDK接口，接口中提供了相机相关的属性和方法，导入方法如下。

  
```cpp
#include <cstdint>
#include <unistd.h>
#include <string>
#include <thread>
#include <cstdio>
#include <fcntl.h>
#include <map>
#include <string>
#include <vector>
#include <native_buffer/native_buffer.h>
#include "iostream"
#include "mutex"

#include "hilog/log.h"
#include "ohcamera/camera.h"
#include "ohcamera/camera_input.h"
#include "ohcamera/capture_session.h"
#include "ohcamera/photo_output.h"
#include "ohcamera/preview_output.h"
#include "ohcamera/video_output.h"
#include "napi/native_api.h"
#include "ohcamera/camera_manager.h"
#include "common/log_common.h"

#include "multimedia/image_framework/image/image_native.h"
#include "multimedia/image_framework/image/image_source_native.h"
#include "multimedia/image_framework/image/image_packer_native.h"
#include "multimedia/media_library/media_access_helper_capi.h"
#include "multimedia/media_library/media_asset_base_capi.h"
#include "multimedia/media_library/media_asset_capi.h"
#include "multimedia/media_library/media_asset_change_request_capi.h"
#include "multimedia/media_library/media_asset_manager_capi.h"
#include "multimedia/media_library/moving_photo_capi.h"
#include "ohcamera/photo_native.h"
#include <window_manager/oh_display_info.h>
#include <window_manager/oh_display_manager.h>
```

2. 在CMake脚本中链接相关动态库。

  
```text
target_link_libraries(entry PUBLIC
    libace_napi.z.so
    libhilog_ndk.z.so
    libohcamera.so
    libimage_source.so
    libmedia_asset_manager.so
    libimage_packer.so
)
```

3. 相机初始化及拍照触发参考[拍照(C/C++)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-shooting)。
4. 注册分段式（PhotoAssetAvailable）拍照回调，对比单段式拍照，仅注册的拍照回调接口不同。

  
![](assets/分段式拍照(C／C++)/file-20260514131527438-0.png)
 

  如果已经注册了PhotoAssetAvailable回调，并且在Session开始之后又注册了PhotoAvailable回调，PhotoAssetAvailable和PhotoAvailable同时注册，会导致流被重启，仅PhotoAssetAvailable生效。

  不建议开发者同时注册PhotoAssetAvailable和PhotoAvailable。

  注册PhotoAssetAvailableCallback回调，接收分段式拍照回图示例：

  **分段式拍照开发流程（PhotoAssetAvailableCallback）**：

  
在会话commitConfig前注册分段式拍照回调。
5. 通过分段式拍照回调，获取媒体库资源mediaAsset。
6. 通过mediaAsset直接落盘图片或者通过mediaAsset配置策略模式请求图像资源，业务处理后通过buffer保存图片，或显示图片(参考[拍照(C/C++)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-shooting)步骤5)。
7. 使用完后解注册分段式拍照回调函数。
