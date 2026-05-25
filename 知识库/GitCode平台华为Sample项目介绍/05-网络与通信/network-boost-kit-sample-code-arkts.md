# network-boost-kit-sample-code-arkts — 网络加速套件

> 来源：https://gitcode.com/HarmonyOS_Samples/network-boost-kit-sample-code-arkts  
> 语言：ArkTS | 版本要求：HarmonyOS NEXT Beta1+

## 项目简介

展示 Network Boost Kit 的四项核心能力：网络质量评估、网络场景识别、传输体验反馈（QoS）、连接迁移。

## 核心 API

| API | 用途 |
|-----|------|
| `netQuality.on('netQosChange')` | 网络质量变化监听 |
| `netQuality.on('netSceneChange')` | 网络场景识别（视频/游戏/下载） |
| `netQuality.reportQoe()` | 上报传输体验指标 |
| `netHandover.on('handoverChange')` | 连接迁移监听（Wi-Fi↔蜂窝） |
| `netHandover.setHandoverMode()` | 设置切换模式 |

## 功能

- **网络质量评估**：实时获取延迟、带宽、丢包率
- **场景识别**：自动识别当前应用场景（视频播放、下载、游戏）
- **QoS 反馈**：上报用户体验指标，系统据此优化调度
- **连接迁移**：Wi-Fi 断开时无缝切换到蜂窝，或反向
