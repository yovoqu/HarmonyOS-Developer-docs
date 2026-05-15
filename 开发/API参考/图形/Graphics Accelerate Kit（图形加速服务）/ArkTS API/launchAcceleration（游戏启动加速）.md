# launchAcceleration（游戏启动加速）

更新时间：2026-04-28 03:31:56

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/graphics-accelerate-launchacceleration
**支持设备：** Phone / PC/2in1 / Tablet

本模块提供游戏启动加速能力。

**系统能力：** SystemCapability.GraphicsGame.LaunchAcceleration

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 6.0.0(20)


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet


```ts
import { launchAcceleration } from '@kit.GraphicsAccelerateKit';
```


## isLaunchMirrorEnabled
**支持设备：** Phone / PC/2in1 / Tablet

isLaunchMirrorEnabled(): boolean

查询游戏的内存镜像功能是否使能。

**系统能力：** SystemCapability.GraphicsGame.LaunchAcceleration

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 6.0.0(20)

**返回值：**


| 类型 | 说明 |
| --- | --- |
| boolean | 系统将结合当前设备的游戏热度、内存镜像数、当日磁盘换出量综合判定是否使能内存镜像功能： - true：游戏使能了内存镜像功能。游戏先切换场景（建议开发者将场景切换至游戏登录界面），系统在退出游戏前自动制作内存镜像，制作内存镜像大概需要4s。 - false：游戏未使能内存镜像功能，系统将直接退出游戏进程。 默认为false。 |


**示例**：


```ts
import { launchAcceleration } from '@kit.GraphicsAccelerateKit';

onWindowStageWillDestroy(): void {
  // 查询当前游戏内存镜像功能是否使能。
  let enable = launchAcceleration.isLaunchMirrorEnabled()
  if (enable) {
    // 切换场景的代码逻辑
  }
}
```
