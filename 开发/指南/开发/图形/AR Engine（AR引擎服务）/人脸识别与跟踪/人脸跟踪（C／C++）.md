# 人脸跟踪（C/C++）

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-face

#### 约束与限制

从6.1.0(23)开始，人脸识别与跟踪能力支持部分Phone、部分Tablet设备、TV设备。请参考[硬件要求](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-preparations#硬件要求)判断设备是否支持人脸识别与跟踪特性（[ARENGINE_FEATURE_TYPE_FACE](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#arengine_featuretype)）。



#### 接口说明

以下接口为AR Engine人脸跟踪相关接口，详细接口和说明，请参考[AR Engine API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine)。

| 接口名 | 描述 |
| --- | --- |
| HMS_AREngine_ARConfig_GetCameraLensFacing | 获取相机镜头朝向。 |
| HMS_AREngine_ARConfig_GetMultiFaceMode | 获取多人脸检测模式。 |
| HMS_AREngine_ARConfig_SetCameraLensFacing | 设置相机镜头朝向。 |
| HMS_AREngine_ARConfig_SetMultiFaceMode | 设置多人脸检测模式。 |
| HMS_AREngine_ARFace_AcquireBlendShapes | 获取人脸表情信息。 |
| HMS_AREngine_ARFace_AcquireGeometry | 获取人脸几何信息。 |
| HMS_AREngine_ARFace_AcquireViewMatrix | 获取当前人脸的面视图矩阵。 |
| HMS_AREngine_ARFace_GetCenterPose | 获取从人脸中心点位姿信息。 |
| HMS_AREngine_ARFaceBlendShapes_AcquireData | 获取微表情数据的集合。 |
| HMS_AREngine_ARFaceBlendShapes_AcquireTypes | 获取所有微表情参数类型数组。 |
| HMS_AREngine_ARFaceBlendShapes_GetCount | 获取人脸微表情数据的个数。 |
| HMS_AREngine_ARFaceBlendShapes_Release | 释放当前人脸的blendShapes对象，即由HMS_AREngine_ARFace_AcquireBlendShapes创建的对象。 |
| HMS_AREngine_ARFaceGeometry_AcquireIndices | 获取人脸Mesh中的三角形索引集合。 |
| HMS_AREngine_ARFaceGeometry_AcquireTexCoord | 获取人脸Mesh中的纹理坐标集。 |
| HMS_AREngine_ARFaceGeometry_AcquireTriangleLabels | 获取人脸Mesh中的三角形标签集合。 |
| HMS_AREngine_ARFaceGeometry_AcquireVertices | 获取人脸Mesh中的顶点集合。 |
| HMS_AREngine_ARFaceGeometry_GetIndicesSize | 获取人脸Mesh中三角形索引的大小。 |
| HMS_AREngine_ARFaceGeometry_GetTexCoordSize | 获取人脸Mesh中纹理坐标的大小。 |
| HMS_AREngine_ARFaceGeometry_GetTriangleCount | 获取人脸Mesh中三角形的大小。 |
| HMS_AREngine_ARFaceGeometry_GetTriangleLabelsSize | 获取人脸Mesh中三角形标签的大小。 |
| HMS_AREngine_ARFaceGeometry_GetVerticesSize | 获取人脸Mesh中顶点的大小。 |
| HMS_AREngine_ARFaceGeometry_Release | 释放当前人脸Mesh对象，即由HMS_AREngine_ARFace_AcquireGeometry创建的对象。 |




#### 开发步骤



#### 创建UI界面

创建一个UI界面，使用XComponent组件用于显示相机预览画面，并定时触发每一帧绘制。

```text
import { display } from '@kit.ArkUI';
import { systemDateTime } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';
import arEngineDemo from 'libentry.so';
import { logger } from '../utils/Logger';


@Builder
export function ARFaceBuilder() {
  ARFace();
}

@Component
struct ARFace {
  pageInfos: NavPathStack = new NavPathStack();
  @State context: Context = this.getUIContext().getHostContext() as Context;
  @State rotation: number = 0;
  private xComponentId = 'ARFace';
  private idStr: string = systemDateTime.getTime(false).toString() + this.xComponentId;
  private resMgr: resourceManager.ResourceManager = this.context.resourceManager;
  private interval: number = -1;
  // ...
  build() {
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
            logger.debug('XComponent onLoad ' + this.idStr);
            this.interval = setInterval(() => {
              // Call the update Native API to update the calculation result of each frame by AR Engine.
              arEngineDemo.update(this.idStr);
            }, 33) // Set the frame rate to 30 fps (with the frame refreshed every 33 ms).
          })
          .onDestroy(() => {
            logger.debug('XComponent onDestroy ' + this.idStr);
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
      logger.debug('aboutToDisappear ' + this.idStr);
      arEngineDemo.stop(this.idStr);
    })
    .onShown(() => {
      logger.debug('onPageShow ' + this.idStr);
      arEngineDemo.show(this.idStr);
    })
    .onHidden(() => {
      logger.debug('onPageHide ' + this.idStr);
      arEngineDemo.hide(this.idStr);
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }
}
```



#### 引入AR Engine

开发者可参考AR物体摆放章节的[引入AR Engine](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-arworld#引入ar-engine)。



#### 创建AR会话并配置为开启人脸跟踪模式

使用人脸识别与跟踪能力时请使用[HMS_AREngine_ARSession_Create_Human_Perception](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#hms_arengine_arsession_create_human_perception)创建AR会话。

```text
// 创建AR会话。
HMS_AREngine_ARSession_Create_Human_Perception(nullptr, nullptr, &arSession);
AREngine_ARConfig *arConfig = nullptr;
// 创建AR会话配置器。
HMS_AREngine_ARConfig_Create(mArSession, &arConfig);
// 设置ARType为FACE开启人脸跟踪模式。
HMS_AREngine_ARConfig_SetARType(mArSession, arConfig, ARENGINE_TYPE_FACE);
// （可选）设置为前置相机
HMS_AREngine_ARConfig_SetCameraLensFacing(mArSession, arConfig, ARENGINE_CAMERA_FACING_FRONT);
// （可选）设置为多人脸模式
HMS_AREngine_ARConfig_SetMultiFaceMode(mArSession, arConfig, ARENGINE_MULTIFACE_ENABLE);
// 配置器设置给AR会话。
HMS_AREngine_ARSession_Configure(mArSession, arConfig);
```



#### 获取当前环境中的人脸信息
1. 创建一个可追踪对象列表faceList，用于存放人脸跟踪模式下AR Engine运行过程中检测到的所有人脸。

  
```text
AREngine_ARTrackableList *faceList = nullptr;
// 创建trackable list获取所有face
CHECK(HMS_AREngine_ARTrackableList_Create(arSession, &faceList));

AREngine_ARTrackableType faceTrackedType = ARENGINE_TRACKABLE_FACE;
CHECK(HMS_AREngine_ARSession_GetAllTrackables(arSession, faceTrackedType, faceList));
```

2. 调用[HMS_AREngine_ARTrackableList_GetSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#hms_arengine_artrackablelist_getsize)函数获取可追踪对象数量，结果存放在faceListSize中。

  
```text
int32_t faceListSize = 0;
CHECK(HMS_AREngine_ARTrackableList_GetSize(arSession, faceList, &faceListSize));
```

3. 转化为人脸信息对象[AREngine_ARFace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#arengine_arface)。

  
```text
for (int i = 0; i < faceListSize; ++i) {
    AREngine_ARTrackable *arTrackable = nullptr;
    CHECK(HMS_AREngine_ARTrackableList_AcquireItem(arSession, faceList, i, &arTrackable));
    AREngine_ARFace *ARFace = reinterpret_cast<AREngine_ARFace *>(arTrackable);
    // ...
}
```




#### 获取当前人脸的位姿信息
1. 先通过[HMS_AREngine_ARPose_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#hms_arengine_arpose_create)接口创建一个[ARPose](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#arengine_arpose)对象，然后调用[HMS_AREngine_ARFace_GetCenterPose](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#hms_arengine_arface_getcenterpose)，获取当前人脸的位姿信息。

  
```text
AREngine_ARPose *facePose = nullptr;
HMS_AREngine_ARPose_Create(arSession, nullptr, 0, &facePose);
HMS_AREngine_ARFace_GetCenterPose(arSession, arFace, facePose);
```

2. 获取当前人脸的视图矩阵。

  调用[HMS_AREngine_ARFace_AcquireViewMatrix](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#hms_arengine_arface_acquireviewmatrix)函数，获取当前人脸的视图矩阵，该矩阵用于后续生成MVP矩阵实现渲染。

  
```text
Eigen::Matrix4f faceViewMat;
CHECK(HMS_AREngine_ARFace_AcquireViewMatrix(arSession, ARFace, faceViewMat.data(), COL_MAJOR_4X4_NUM));
```

3. 获取当前人脸的几何信息。

  调用[HMS_AREngine_ARFace_AcquireGeometry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#hms_arengine_arface_acquiregeometry)，获取当前人脸的几何信息，并将结果存放在arFaceGeometry中。

  
```text
AREngine_ARFaceGeometry *geometry = nullptr;
// 获得当前face的人脸集合信息指针
CHECK(HMS_AREngine_ARFace_AcquireGeometry(arSession, ARFace, &geometry));
```

4. 获取人脸的几何信息中的三角形顶点。

  
```text
int32_t meshVerticesSize = 0;
HMS_AREngine_ARFaceGeometry_GetVerticesSize(session, firstFace, &meshVerticesSize);
LOGD("HMS_AREngine_ARFaceGeometry_GetVerticesSize size=%{public}d", meshVerticesSize);
const float *meshVertices = nullptr;
auto ret = HMS_AREngine_ARFaceGeometry_AcquireVertices(session, firstFace, &meshVertices);
LOGD("HMS_AREngine_ARSceneMesh_AcquireVertexList result=%{public}d", ret);
```

5. 获取人脸的几何信息中的三角形面片。

  
```text
int32_t indexSize = 0;
HMS_AREngine_ARFaceGeometry_GetIndicesSize(session, firstFace, &indexSize);
const int32_t *meshTriangleIndices = nullptr;
ret = HMS_AREngine_ARFaceGeometry_AcquireIndices(session, firstFace, &meshTriangleIndices);
```

6. 获取人脸的几何信息中的三角形面片的语义标签。

  
```text
ret = HMS_AREngine_ARFaceGeometry_GetTriangleLabelsSize(session, firstFace, &mTrianglesNum);
const AREngine_ARAnimojiTriangleLabel* triangleLabels = nullptr;
ret = HMS_AREngine_ARFaceGeometry_AcquireTriangleLabels(session, firstFace, &triangleLabels);
```

7. 获取人脸几何信息中的UV纹理坐标。

  
```text
int texCoordSize = 0;
ret = HMS_AREngine_ARFaceGeometry_GetTexCoordSize(session, firstFace, &texCoordSize);
const float* texCoords = nullptr;
ret = HMS_AREngine_ARFaceGeometry_AcquireTexCoord(session, firstFace, &texCoords);
```

8. 获取当前人脸的微表情信息。

  
```text
// 调用HMS_AREngine_ARFace_AcquireBlendShapes，获取当前人脸的微表情信息，并将结果存放在arFaceBlendShapes中。
AREngine_ARFaceBlendShapes* arFaceBlendShapes = nullptr;
HMS_AREngine_ARFace_AcquireBlendShapes(arSession, arFace, &arFaceBlendShapes);
// 调用HMS_AREngine_ARFaceBlendShapes_GetCount，获取当前人脸的微表情的数量
int count = 0;
HMS_AREngine_ARFaceBlendShapes_GetCount(arSession, arFaceBlendShapes, &count);
// 调用HMS_AREngine_ARFaceBlendShapes_AcquireTypes，获取当前人脸的微表情的标签集合
const AREngine_ARAnimojiBlendShape* blendShapesTypes = nullptr;
HMS_AREngine_ARFaceBlendShapes_AcquireTypes(arSession, arFaceBlendShapes, &blendShapesTypes);
// 调用HMS_AREngine_ARFaceBlendShapes_AcquireData，获取当前人脸的微表情的数据集合，集合中的元素表示该位置在标签集合中表示的微表情的变化程度
const float *blendShapesData = nullptr;
HMS_AREngine_ARFaceBlendShapes_AcquireData(arSession, arFaceBlendShapes, &blendShapesData);
```
