# 获取设备位姿（ArkTS）

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-get-pose

本章节给出了关键开发步骤，完整代码可以参考[示例代码](https://gitcode.com/HarmonyOS_Samples/arengine_samplecode_clientdemo_arkts)。


#### 约束与限制

从5.1.0(18)开始，获取设备位姿支持部分Phone、部分Tablet设备。并且从6.1.0(23)版本开始，新增支持TV设备。请参考[硬件要求](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-preparations#硬件要求)判断设备是否支持运动跟踪及平面识别特性（[ARENGINE_FEATURE_TYPE_SLAM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-api-arengine#arfeaturetype)）。



#### 接口说明

获取设备位姿可以通过[ARCamera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-api-arengine#arcamera)相机对象获取，以下接口为获取设备位姿接口。详细接口和说明，请参考[AR Engine API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-api-arengine)。

| 接口名 | 描述 |
| --- | --- |
| ARCamera.getPose | 获取设备在世界空间中的位姿信息。 |




#### 开发步骤



#### 导入模块

获取设备位姿能力需要依赖以下模块。

```text
import { arEngine, ARView, arViewController } from '@kit.AREngine';
import { Node, Scene, Vec3 } from '@kit.ArkGraphics3D';
import { BusinessError } from '@kit.BasicServicesKit';
```

Vec3是一个三维向量，用于存储设备的位姿信息。



#### 定义变量

定义两个变量pose和stateReason，用于接收pose位姿信息和追踪失败原因。

```text
let pose: arEngine.ARPose;
let stateReason: arEngine.ARTrackingStateReason;
```



#### 显示预览流及设备位姿信息

首先初始化AR会话和AR场景，可以参考[初始化AR会话和AR场景](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-arsession#初始化ar会话和ar场景)章节。

在设备界面上显示设备位姿信息及追踪失败原因，使用重复调用函数方法在设备界面上实时更新位姿和追踪失败原因的信息。

```text
@Builder
export function ARPoseBuilder() {
  ARPose()
}
let pose: arEngine.ARPose;
let stateReason: arEngine.ARTrackingStateReason;
@Component
struct ARPose {
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
  @State reason: arEngine.ARTrackingStateReason = stateReason;

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

          Column() {
            Text(`x: ${this.translation.x.toFixed(4)}`)
              .infoStyles()
            Text(`y: ${this.translation.y.toFixed(4)}`)
              .infoStyles()
            Text(`z: ${this.translation.z.toFixed(4)}`)
              .infoStyles()
            Text(`reason: ${this.reason}`)
              .infoStyles()
            Text(`time: ${this.getCurrentTime(this.currentTimeStamp)}`)
              .infoStyles()
          }
          .alignItems(HorizontalAlign.Start)
          .margin({ left: '28vp' })
          .alignRules({
            top: { anchor: '__container__', align: VerticalAlign.Top },
            left: { anchor: '__container__', align: HorizontalAlign.Start }
          })
        }
      }
    }
    .onAppear(() => {
      this.initARView()

      this.intervalId = setInterval(() => {
        if (pose !== undefined) {
          this.translation = pose.translation
          this.reason = stateReason
          this.currentTimeStamp = new Date()
        }
      }, this.delayInterval);
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
    // ...
  }
  // ...
  }
}
@Extend(Text)
function infoStyles() {
  .fontColor(Color.Yellow)
  .fontSize(20)
  .textShadow({
    radius: 10,
    color: Color.Black,
    offsetX: 0,
    offsetY: 0
  })
  .textAlign(TextAlign.Start)
}
```



#### 获取设备位姿信息

调用[ARViewCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-api-arviewcontroller#arviewcallback)，使用其中的[onFrameUpdate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-api-arviewcontroller#arviewcallbackonframeupdate)方法获取AR会话对象arSession，之后通过AR会话对象arSession获取每一帧对应的设备位姿信息。

```text
class ARViewCallbackImpl extends arViewController.ARViewCallback {
  onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  }

  onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  }

  async onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): Promise<void> {
    if (!ctx.session) {
      return;
    }

    let session: arEngine.ARSession = ctx.session;
    try {
      let frame = session.getFrame();
      pose = frame.getCamera().getPose();
      stateReason = frame.getCamera().stateReason;
      releaseFrame(frame);
    } catch (error) {
      const err = error as BusinessError;
      // ...
    }
  }
}
```
