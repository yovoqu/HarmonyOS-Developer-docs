# 高精几何重建（ArkTS）

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-volume-measurement

#### 约束与限制

从6.0.0(20)开始，高精几何重建能力支持部分Phone、部分Tablet设备。请参考[硬件要求](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-preparations#硬件要求)判断设备是否支持高精几何重建特性（[ARENGINE_FEATURE_TYPE_SEMANTIC_DENSE](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-api-arengine#arfeaturetype)）。



#### 接口说明

高精几何重建主要依赖[ARSemanticDenseData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-api-arengine#arsemanticdensedata)，以下接口为高精几何重建的相关接口。详细接口和说明，请参考[AR Engine API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-api-arengine)。

| 接口名 | 描述 |
| --- | --- |
| ARSession.getFrame | 获取AR Engine处理后的一帧数据。 |
| ARFrame.acquireSemanticDense | 返回当前帧的高精几何重建对象数据。 |
| ARSemanticDenseData.acquireCubeData | 返回一个高精几何重建对象的立方体数据信息的列表。 |
| ARSemanticDenseData.release | 释放高精几何重建对象数据。 |




#### 开发步骤

对于使用ArkTS的任何AR应用，首先需要创建一个AR会话[ARViewContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-api-arviewcontroller#arviewcontext)，用于管理AR Engine的系统状态。AR会话[ARViewContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-api-arviewcontroller#arviewcontext)的创建可以参考[管理AR会话](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-arsession)章节。



#### 导入模块

高精几何重建能力所需要导入的模块如下：

```text
import { arEngine, ARView, arViewController } from '@kit.AREngine';
import { Node, Scene, Vec3 } from '@kit.ArkGraphics3D';
import { BusinessError } from '@kit.BasicServicesKit';
```



#### 定义变量

定义变量cubeVertexData接收立方体顶点数据，定义变量cubeConfidence接收识别出立方体的置信度数据，定义变量cubeLabel接收立方体的语义信息。

```text
let cubeVertexData: number[];
let cubeConfidence: number;
let cubeLabel: arEngine.ARSemanticPlaneLabel;
```



#### 显示预览流

首先初始化AR会话和AR场景，可以参考[初始化AR会话和AR场景](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-arsession#初始化ar会话和ar场景)章节。

更改semanticDenseMode为[ARSemanticDenseMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-api-arengine#arsemanticdensemode).CUBE_VOLUME，启用体积测量识别能力。

```text
@Builder
export function ARSemanticDenseBuilder() {
  ARSemanticDense()
}

let arSession: arEngine.ARSession;
let frame: arEngine.ARFrame
let semanticData: arEngine.ARSemanticDenseData
let cubeVertexData: number[];
let cubeConfidence: number;
let cubeLabel: arEngine.ARSemanticPlaneLabel;

@Component
struct ARSemanticDense {
  pageInfos: NavPathStack = new NavPathStack();
  @State arContext?: arViewController.ARViewContext = undefined;
  private intervalId: number = -1;
  private delayInterval: number = 33;
  private params: arEngine.ARConfig = { type: arEngine.ARType.WORLD };
  @State translation: Vec3 = {
    x: 0,
    y: 0,
    z: 0
  };
  @State currentTimeStamp: Date = new Date();

  build() {
    NavDestination() {
      RelativeContainer() {
        if (this.arContext) {
          ARView({ context: this.arContext })
            .height('100%')
            .width('100%')
            .alignRules({
              center: { anchor: '__container__', align: VerticalAlign.Center },
              middle: { anchor: '__container__', align: HorizontalAlign.Center }
            })

        }
      }
    }
    .onAppear(() => {
      this.initARView()
    })
    .onWillDisappear(() => {
      clearInterval(this.intervalId);
      this.arContext?.destroy();
    })
    .onShown(() => {
      this.resumeARView()
    })
    .onHidden(() => {
      this.pauseARView()
    })
    .onReady(ctx => {
      this.params = ctx.pathInfo.param as arEngine.ARConfig;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }

  private pauseARView(): void {
    // ...
  }

  private resumeARView(): void {
    // ...
  }

  private initARView(): void {
    Scene.load().then(async (scene: Scene) => {
      let ret :boolean = arViewController.isARTypeSupported(arEngine.ARFeatureType.ARENGINE_FEATURE_TYPE_SEMANTIC_DENSE);
      logger.info('ARSemanticDense isARTypeSupported is' + ret);
      let context = new arViewController.ARViewContext()
      context.scene = scene
      context.callback = new ARViewCallbackImpl()
      context.config = {
        type: arEngine.ARType.WORLD,
        planeFindingMode: arEngine.ARPlaneFindingMode.DISABLED,
        powerMode: this.params?.powerMode,
        semanticDenseMode: arEngine.ARSemanticDenseMode.CUBE_VOLUME
      };
      context.init().then(() => {
        this.arContext = context;
        // ...
```



#### 获取立方体体积数据

调用[ARViewCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-api-arviewcontroller#arviewcallback)，使用其中的[onFrameUpdate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-api-arviewcontroller#arviewcallbackonframeupdate)方法进行帧数据更新，通过[ARSession.getFrame](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-api-arengine#arsessiongetframe)方法获取当前帧，通过[ARFrame.acquireSemanticDense](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-api-arengine#arframeacquiresemanticdense)获得当前帧的高精几何重建对象数据，通过[ARSemanticDenseData.acquireCubeData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-api-arengine#arsemanticdensedataacquirecubedata)从高精几何重建对象数据中获取识别到的立方体顶点数据，经过计算可以得到立方体的体积信息，相关变量定义参考[定义变量](#定义变量)。

```text
class ARViewCallbackImpl extends arViewController.ARViewCallback {
  onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  }

  onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  }

  onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): void {
    let session: arEngine.ARSession | undefined = ctx.session;
    if (session) {
      arSession = session;
      frame = session.getFrame()
      if (!frame){
        // ...
      } else {
        semanticData = frame.acquireSemanticDense();
        if(semanticData !== undefined){
          // ...
          if(semanticData.cubeDataSize>0){
            let semanticCubeData: arEngine.ARSemanticDenseCubeData = semanticData.acquireCubeData()[0];
            cubeVertexData = semanticCubeData.vertexData;
            cubeConfidence = semanticCubeData.confidence;
            cubeLabel = semanticCubeData.label;
            // ...
          }
        }
        semanticData.release()
        semanticData.timestamp
      }
      releaseFrame(frame);
    // ...
    }
  }
}
```
