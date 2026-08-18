# 物体摆放（C/C++）

更新时间：2026-08-14 11:17:56

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-arworld

本章节给出了关键开发步骤，完整代码可以参考[示例代码](https://gitcode.com/harmonyos_samples/arengine_-sample-code_-clientdemo_cpp)。


#### 约束与限制

从5.0.0(12)开始，物体摆放能力支持部分Phone、部分Tablet设备。请参考[硬件要求](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-preparations#硬件要求)判断设备是否支持运动跟踪及平面识别特性（[ARENGINE_FEATURE_TYPE_SLAM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#arengine_featuretype)）。



#### 接口说明

以下接口为AR物体摆放相关接口。详细接口和说明，请参考[AR Engine API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine)。

| 接口名 | 描述 |
| --- | --- |
| HMS_AREngine_ARSession_Create | 创建一个新的AREngine_ARSession会话。 |
| HMS_AREngine_ARSession_Update | 更新AR Engine的计算结果。 |
| HMS_AREngine_ARSession_Configure | 配置AREngine_ARSession会话。 |
| HMS_AREngine_ARFrame_Create | 创建一个新的AREngine_ARFrame对象，将指针存储到中*outFrame。 |
| HMS_AREngine_ARSession_SetDisplayGeometry | 设置显示的高和宽（以Pixel为单位）。该高度和宽度是显示视图的高度和宽度，如果不一致，会导致显示相机预览出错。 |
| HMS_AREngine_ARSession_SetCameraGLTexture | 设置可用于存储相机预览流数据的openGL纹理。 |
| HMS_AREngine_ARSession_GetAllTrackables | 获取所有指定类型的可跟踪对象集合。 |
| HMS_AREngine_ARTrackableList_AcquireItem | 从可跟踪列表中获取指定index的对象。 |
| HMS_AREngine_ARPlane_GetCenterPose | 获取从平面的局部坐标系到世界坐标系转换的位姿信息。 |
| HMS_AREngine_ARFrame_HitTest | 根据屏幕上兴趣点位置获取命中检测结果。 |
| HMS_AREngine_ARHitResultList_GetSize | 获取命中检测结果对象列表中包含的对象数。 |
| HMS_AREngine_ARHitResultList_GetItem | 在命中检测结果列表中获取指定索引的命中检测结果对象。 |
| HMS_AREngine_ARHitResult_Create | 创建一个空的命中检测结果对象。 |
| HMS_AREngine_ARHitResult_AcquireNewAnchor | 在碰撞命中位置创建一个新的锚点。 |
| HMS_AREngine_ARHitResult_AcquireTrackable | 获取被命中的可追踪对象。 |
| HMS_AREngine_ARFrame_AcquireCamera | 获取当前帧的相机参数对象。 |
| HMS_AREngine_ARPose_Create | 分配并初始化一个新的位姿对象。 |
| HMS_AREngine_ARCamera_GetPose | 获取当前相机对象在AR世界空间中的位姿。 |




#### 开发步骤



#### 声明Native接口

ArkTS接口声明。

```text
import { resourceManager } from '@kit.LocalizationKit';
// ...
export const start: (id: string, params: Int32Array) => void;
export const show: (id: string) => void;
export const hide: (id: string) => void;
export const update: (id: string) => number;
export const stop: (id: string) => void;
export const init: (resmgr: resourceManager.ResourceManager) => void;
export const getDistance: (id: string) => string;
export const initImage: (id: string, width: number, height: number, buffer: ArrayBuffer) => number;
export const setPath: (id: string, path: string) => void;
export const saveImageDataBaseToLocal: (id: string, path: string) => void;
export const getImageCount: (id: string) => number;
export const getVolume: (id: string) => string;
export const getLandmark: (id: string) => Landmark[];
export const getBoneLine: (id: string) => SkeletonConnectionAndType;
```

建立ArkTS接口与C++接口之间的映射。

```text
napi_property_descriptor desc[] = {
    {"init", nullptr, Global::Init, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"start", nullptr, NapiManager::NapiOnPageAppear, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"show", nullptr, NapiManager::NapiOnPageShow, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"hide", nullptr, NapiManager::NapiOnPageHide, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"update", nullptr, NapiManager::NapiOnPageUpdate, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"stop", nullptr, NapiManager::NapiOnPageDisappear, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"getDistance", nullptr, NapiManager::NapiGetDistance, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"initImage", nullptr, NapiManager::NapiInitImage, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"setPath", nullptr, NapiManager::NapiSetPath, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"saveImageDataBaseToLocal", nullptr, NapiManager::NapiSaveImageDataBaseToLocal, nullptr, nullptr, nullptr,
     napi_default, nullptr},
    {"getImageCount", nullptr, NapiManager::NapiGetImageCount, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"getVolume", nullptr, NapiManager::NapiGetVolume, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"getLandmark", nullptr, NapiManager::NapiGetBodyPoint2D, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"getBoneLine", nullptr, NapiManager::NapiGetSkeletonConnections, nullptr, nullptr, nullptr, napi_default,
     nullptr}};
```



#### 创建UI界面

创建一个UI界面，使用[XComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-xcomponent)组件用于显示相机预览画面，并定时触发每一帧绘制。

```text
import { display, PromptAction } from '@kit.ArkUI';
import { BusinessError, systemDateTime } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';
import arEngineDemo from 'libentry.so';
import { logger } from '../utils/Logger';

@Builder
export function ARWorldBuilder() {
  ARWorld();
}

@Component
struct ARWorld {
  pageInfos: NavPathStack = new NavPathStack();
  @State context: Context = this.getUIContext().getHostContext() as Context;
  @State numberOfPlans: number = 0;
  @State rotation: number = 0;
  private currentMillisecond: number = 0;
  private interval: number = -1;
  private isUpdate: boolean = true;
  private xComponentId: string = 'ARWorld';
  private idStr: string = systemDateTime.getTime(false).toString() + this.xComponentId;
  private resMgr: resourceManager.ResourceManager = this.context.resourceManager;
  // ...
  build(): void {
    NavDestination() {
      RelativeContainer() {
        XComponent({ id: this.idStr, type: XComponentType.SURFACE, libraryname: 'entry' })
          .width('100%')
          .height('100%')
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onLoad(() => {
            this.interval = setInterval(() => {
              if (this.isUpdate) {
                // 调用Native API更新方法，更新AR Engine每一帧的计算结果。
                this.numberOfPlans = arEngineDemo.update(this.idStr);
                this.planeNum();
              }
            }, 33) // 将帧率设置为30fps（每33毫秒刷新一次帧）。
          })
          .onDestroy(() => {
            clearInterval(this.interval);
          })
      }
    }
    .onAppear(() => {
      arEngineDemo.init(this.resMgr);
      let config: Int32Array = new Int32Array([1, this.rotation]);
      arEngineDemo.start(this.idStr, config);
    })
    .onWillDisappear(() => {
      arEngineDemo.stop(this.idStr);
    })
    .onShown(() => {
      this.isUpdate = true;
      arEngineDemo.show(this.idStr);
    })
    .onHidden(() => {
      this.isUpdate = false;
      arEngineDemo.hide(this.idStr);
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }

  private messageNotification(): void {
    let promptAction: PromptAction = this.getUIContext().getPromptAction();
    try {
      promptAction.showToast({
        message: $r('app.string.alert_desc'),
        bottom: 300
      })
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`promptAction Failed. Code is ${err.code}, message is ${err.message}`);
    }
  }

  private planeNum(): void {
    if (this.numberOfPlans < 1) {
      // 平面数量小于1。
      let tempMillisecond: number = new Date().getTime();
      // 为特性首次启动的时间赋值。
      if (this.currentMillisecond === 0) {
        this.currentMillisecond = tempMillisecond;
        return;
      }
      // 如果平面在10秒内未被识别，则显示弹出窗口。
      if (tempMillisecond - this.currentMillisecond > 10000) {
        this.messageNotification();
        this.currentMillisecond = 0;
      }
    } else {
      this.currentMillisecond = 0;
    }
  }
}
```



#### 引入AR Engine

开发者可参考管理AR会话章节的[引入AR Engine](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-arsession#引入ar-engine)。



#### 创建AR场景
1. 调用[HMS_AREngine_ARSession_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#hms_arengine_arsession_create)函数创建[AREngine_ARSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#arengine_arsession)会话。您可以参考[管理AR会话](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-arsession)创建ARSession。
2. 配置AR会话及预览尺寸。

  
```text
AREngine_ARConfig *arConfig = nullptr;
CHECK(HMS_AREngine_ARConfig_Create(mArSession, &arConfig));
// ...
CHECK(HMS_AREngine_ARSession_Configure(mArSession, arConfig));
HMS_AREngine_ARConfig_Destroy(arConfig);
// 创建一个AREngine_ARFrame对象。
CHECK(HMS_AREngine_ARFrame_Create(mArSession, &mArFrame));
NativeDisplayManager_Rotation displayRotation;
if (OH_NativeDisplayManager_GetDefaultDisplayRotation(&displayRotation) == DISPLAY_MANAGER_OK) {
    mDisplayRotation = ArEngineRotateType(displayRotation);
}
// ...
CHECK(HMS_AREngine_ARSession_SetDisplayGeometry(mArSession, mDisplayRotation, mWidth, mHeight));
// 设置显示高度和宽度（以像素为单位）。请确保在此处设置的高度和宽度与显示视图的高度和宽度一致。
```

3. 通过OpenGL接口获取纹理ID。

  
```text
glGenTextures(1, &textureId);
```

4. 设置OpenGL纹理，存储相机预览流数据。

  
```text
HMS_AREngine_ARSession_SetCameraGLTexture(mArSession, mWorldRenderManager.GetPreviewTextureId());
```




#### 获取平面
1. 调用[HMS_AREngine_ARSession_Update](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#hms_arengine_arsession_update)函数更新当前[AREngine_ARFrame](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#arengine_arframe)对象。

  
```text
HMS_AREngine_ARSession_Update(mArSession, mArFrame);
```

2. 获取相机的视图矩阵和相机的投影矩阵，用于后续渲染。

  
```text
// 获取当前帧的相机参数。
AREngine_ARCamera *arCamera = nullptr;
CHECK(HMS_AREngine_ARFrame_AcquireCamera(arSession, arFrame, &arCamera));
// 获取最新帧中相机的视图矩阵。
CHECK(HMS_AREngine_ARCamera_GetViewMatrix(arSession, arCamera, viewMat->data(), 16));
// 获取用于在相机图像上渲染虚拟内容的投影矩阵。此矩阵可用于将相机坐标系统转换为裁剪坐标系统。近点 (0.1) 远点 (100)。
CHECK(HMS_AREngine_ARCamera_GetProjectionMatrix(arSession, arCamera, {0.1f, 100.f}, projectionMat->data(), 16));
```

> [!NOTE]
> 这里直接获取相机的视图矩阵和相机的投影矩阵，是为了便于渲染。获取相机运动中的位姿变化，还可以调用 HMS_AREngine_ARCamera_GetPose 函数配合 HMS_AREngine_ARPose_GetPoseRaw 函数进行获取。详细可参考 获取设备当前位姿 。

3. 调用[HMS_AREngine_ARSession_GetAllTrackables](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#hms_arengine_arsession_getalltrackables)函数获取平面列表。详细可参考[检测环境中的平面](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-get-plane)章节。

  
```text
// 更新并渲染平面。
AREngine_ARTrackableList *planeList = nullptr;
// 创建可跟踪对象列表。
CHECK(HMS_AREngine_ARTrackableList_Create(arSession, &planeList));
// 获取指定类型的所有可跟踪对象列表。
AREngine_ARTrackableType planeTrackedType = ARENGINE_TRACKABLE_PLANE;
CHECK(HMS_AREngine_ARSession_GetAllTrackables(arSession, planeTrackedType, planeList));
int32_t planeListSize = 0;
// 获取列表中可跟踪对象的数量。
CHECK(HMS_AREngine_ARTrackableList_GetSize(arSession, planeList, &planeListSize));
mPlaneCount = planeListSize;

for (int i = 0; i < planeListSize; ++i) {
    AREngine_ARTrackable *arTrackable = nullptr;
    // 从可跟踪对象列表中获取指定索引的对象。
    CHECK(HMS_AREngine_ARTrackableList_AcquireItem(arSession, planeList, i, &arTrackable));
    AREngine_ARPlane *arPlane = reinterpret_cast<AREngine_ARPlane *>(arTrackable);
    // 获取当前可跟踪对象的跟踪状态。只有当跟踪状态为ARENGINE_TRACKING_STATE_TRACKING（可跟踪）时，才执行平面绘制。
    AREngine_ARTrackingState outTrackingState;
    CHECK(HMS_AREngine_ARTrackable_GetTrackingState(arSession, arTrackable, &outTrackingState));
    AREngine_ARPlane *subsumePlane = nullptr;
    // 获取平面的父平面（当平面与另一个平面合并时生成）。如果没有父平面，则返回NULL。
    CHECK(HMS_AREngine_ARPlane_AcquireSubsumedBy(arSession, arPlane, &subsumePlane));
    if (subsumePlane != nullptr) {
        HMS_AREngine_ARTrackable_Release(reinterpret_cast<AREngine_ARTrackable *>(subsumePlane));
        continue;
    }
    if (AREngine_ARTrackingState::ARENGINE_TRACKING_STATE_TRACKING != outTrackingState) {
        continue;
    }
    // ...
}
HMS_AREngine_ARTrackableList_Destroy(planeList);
planeList = nullptr;
```

4. 调用[HMS_AREngine_ARPlane_GetPolygon](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#hms_arengine_arplane_getpolygon)函数获取平面的二维顶点坐标数组，用于绘制平面边界。

  
```text
int32_t polygonLength = 0;
// 获取检测到的平面的2D顶点数组的大小。
CHECK(HMS_AREngine_ARPlane_GetPolygonSize(session, plane, &polygonLength));

if (polygonLength == 0) {
    LOGE("WorldPlaneRenderer::UpdateForPlane, no valid plane polygon is found.");
    return;
}
const int32_t verticesSize = polygonLength / 2;
std::vector<Eigen::Vector2f> raw_vertices(verticesSize);
// 获取检测到的平面的2D顶点数组，格式为[x1, z1, x2, z2, ...]。
CHECK(HMS_AREngine_ARPlane_GetPolygon(session, plane, raw_vertices.front().data(), polygonLength));
// 填充顶点0到3。使用该顶点。
// xy坐标用于顶点的x和z坐标。
// 顶点的z坐标用于alpha。
// 外多边形的alpha值为 0。
for (int32_t i = 0; i < verticesSize; ++i) {
    vertices.emplace_back(raw_vertices[i].x(), raw_vertices[i].y(), 0.75f);
}
```

> [!NOTE]
> 调用 HMS_AREngine_ARPlane_GetPolygon 函数获取平面的二维顶点坐标数组格式为[x1，z1，x2，z2，...]。这些值均在平面局部坐标系的x-z平面中定义，须先调用 HMS_AREngine_ARPlane_GetCenterPose 函数获取从平面的局部坐标系到世界坐标系转换的位姿数据，然后调用 HMS_AREngine_ARPose_GetMatrix 函数将位姿数据转换成4X4的矩阵，该矩阵与局部坐标系的坐标点做乘法，可以得到局部坐标系到世界坐标系的转换。

5. 将平面的二维顶点坐标转换到世界坐标系，并绘制平面。

  
```text
AREngine_ARPose *scopedArPose = nullptr;
// 获取从平面的局部坐标系统到世界坐标系统的转换的位姿信息。
CHECK(HMS_AREngine_ARPose_Create(session, nullptr, 0, &scopedArPose));
CHECK(HMS_AREngine_ARPlane_GetCenterPose(session, plane, scopedArPose));
// 将位姿数据转换为4x4矩阵。outMatrixColMajor4x4是用于存储矩阵的数组，其中数据以列优先顺序存储。局部坐标系统中的坐标可以通过将此矩阵与局部坐标系统中的坐标相乘来转换为世界坐标系统中的坐标。
CHECK(HMS_AREngine_ARPose_GetMatrix(session, scopedArPose, modelMat.data(), 16));
HMS_AREngine_ARPose_Destroy(scopedArPose);

// 生成一个三角形。
for (int i = 1; i < verticesSize - 1; ++i) {
    triangles.push_back(0);
    triangles.push_back(i);
    triangles.push_back(i + 1);
}
// 生成平面边界。
for (int i = 0; i < verticesSize; ++i) {
    lines.push_back(i);
}
```




#### 点击屏幕
1. 用户点击屏幕后，基于点击事件获取屏幕坐标。可参考[Native XComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent)。

  添加头文件：native_interface_xcomponent.h。

  
```text
#include <ace/xcomponent/native_interface_xcomponent.h>
```
通过点击事件获取屏幕点击坐标。

  
```text
float pixeLX = 0.0f;
float pixeLY = 0.0f;
int32_t ret = OH_NativeXComponent_GetTouchEvent(component, window, &mTouchEvent);
if (ret == OH_NATIVEXCOMPONENT_RESULT_SUCCESS) {
    if (mTouchEvent.type == OH_NATIVEXCOMPONENT_DOWN) {
        pixeLX = mTouchEvent.touchPoints[0].x;
        pixeLY = mTouchEvent.touchPoints[0].y;
        LOGD("Pos: %{public}f %{public}f.", pixeLX, pixeLY);
    } else {
        return;
    }
} else {
    LOGE("Touch fail");
    return;
}
```

2. 调用[HMS_AREngine_ARFrame_HitTest](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#hms_arengine_arframe_hittest)函数进行碰撞检测，结果存放在碰撞检测结果列表中。

  
```text
AREngine_ARHitResultList *hitResultList = nullptr;
CHECK(HMS_AREngine_ARHitResultList_Create(mArSession, &hitResultList));
CHECK(HMS_AREngine_ARFrame_HitTest(mArSession, mArFrame, pixeLX, pixeLY, hitResultList));
```

> [!NOTE]
> 碰撞结果按照交点与设备的距离从近到远进行排序，存放在碰撞结果列表中。




#### 放置虚拟物体
1. 调用[HMS_AREngine_ARHitResultList_GetItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#hms_arengine_arhitresultlist_getitem)函数遍历碰撞检测结果列表，获取命中的可跟踪对象。

  
```text
AREngine_ARHitResult *arHit = nullptr;
CHECK(HMS_AREngine_ARHitResult_Create(mArSession, &arHit));
CHECK(HMS_AREngine_ARHitResultList_GetItem(mArSession, hitResultList, i, arHit));
if (arHit == nullptr) {
    return false;
}
AREngine_ARTrackable *arTrackable = nullptr;
CHECK(HMS_AREngine_ARHitResult_AcquireTrackable(mArSession, arHit, &arTrackable));
```

2. 判断碰撞结果是否存在于平面内部。

  
```text
AREngine_ARTrackableType ar_trackable_type = ARENGINE_TRACKABLE_INVALID;
CHECK(HMS_AREngine_ARTrackable_GetType(mArSession, arTrackable, &ar_trackable_type));

// 如果遇到平面或方向点，则创建锚点。
if (ARENGINE_TRACKABLE_PLANE == ar_trackable_type) {
    AREngine_ARPose *arPose = nullptr;
    CHECK(HMS_AREngine_ARPose_Create(mArSession, nullptr, 0, &arPose));
    CHECK(HMS_AREngine_ARHitResult_GetHitPose(mArSession, arHit, arPose));
    int32_t inPolygon = 0;
    AREngine_ARPlane *arPlane = reinterpret_cast<AREngine_ARPlane *>(arTrackable);
    // 检查位姿是否在平面的边界多边形内。值为0表示超出范围，其他值表示在范围内。
    CHECK(HMS_AREngine_ARPlane_IsPoseInPolygon(mArSession, arPlane, arPose, &inPolygon));
    HMS_AREngine_ARPose_Destroy(arPose);
    if (!inPolygon) {
        continue;
    }
    // ...
```

3. 在碰撞结果位置创建一个新的锚点，并基于此锚点放置虚拟模型。

  
```text
AREngine_ARAnchor *anchor = nullptr;
CHECK(HMS_AREngine_ARHitResult_AcquireNewAnchor(mArSession, arHitResult, &anchor));

AREngine_ARTrackingState trackingState = ARENGINE_TRACKING_STATE_STOPPED;
CHECK(HMS_AREngine_ARAnchor_GetTrackingState(mArSession, anchor, &trackingState));
if (trackingState != ARENGINE_TRACKING_STATE_TRACKING) {
    HMS_AREngine_ARAnchor_Release(anchor);
    return;
}
```

4. 绘制模型。

  调用[HMS_AREngine_ARAnchor_GetPose](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#hms_arengine_aranchor_getpose)函数获取锚点位姿，并基于该位姿绘制虚拟模型。

  
```text
AREngine_ARPose *pose = nullptr;
CHECK(HMS_AREngine_ARPose_Create(arSession, nullptr, 0, &pose));
CHECK(HMS_AREngine_ARAnchor_GetPose(arSession, coloredAnchor.anchor, pose));
CHECK(HMS_AREngine_ARPose_GetMatrix(arSession, pose, modelMat.data(), 16));
HMS_AREngine_ARPose_Destroy(pose);
```
