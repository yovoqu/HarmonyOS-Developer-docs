# HarmonyOS_Samples GitCode 仓库项目总览

> 来源：https://gitcode.com/HarmonyOS_Samples  
> 项目总数：462 个仓库 | 组织：华为 HarmonyOS 官方示例代码  
> 更新时间：2026-05-25

---

## 仓库简介

HarmonyOS_Samples 是华为在 GitCode（AtomGit）平台上的官方示例代码组织，汇聚了覆盖 HarmonyOS 全场景开发需求的优质代码案例。仓库涵盖：

- **ArkTS 声明式 UI 开发**：组件、动画、导航、响应式布局
- **系统 Kit 集成**：媒体、网络、安全、AI、支付等 30+ Kit
- **多设备适配**：手机、平板、折叠屏、智能手表、PC/2in1
- **架构最佳实践**：MVVM、模块化（HAP/HAR/HSP）、API 版本兼容
- **性能与调测**：日志、调试、性能分析、后台任务

所有项目要求 **HarmonyOS 5.0.5+**、**DevEco Studio 5.0.5+**，支持 Stage 模型。

---

## 项目分类概览

### 01-媒体与下载（9 个项目）

| 项目 | 核心 Kit | 亮点 |
|------|---------|------|
| [multi-file-download](01-媒体与下载/multi-file-download.md) | @ohos.request | 多文件下载进度监听，暂停/恢复 |
| [NetBoost](01-媒体与下载/NetBoost.md) | Network Boost Kit | 多网并发加速上传下载 |
| [HMOS_LiveStream](01-媒体与下载/HMOS_LiveStream.md) | AVCodec Kit, Camera Kit | 完整直播推流+播放 |
| [avplayer-embeded-short-video](01-媒体与下载/avplayer-embeded-short-video.md) | AVPlayer, XComponent | 嵌入式短视频播放，懒加载 |
| [AVPlayerShortVideo](01-媒体与下载/AVPlayerShortVideo.md) | AVPlayer, Swiper | 短视频滑动切换播放 |
| [AVPlayerLongVideo](01-媒体与下载/AVPlayerLongVideo.md) | AVPlayer | 长视频画中画/字幕/弹幕 |
| [avscreen-capture-record-system-audio-arkts](01-媒体与下载/avscreen-capture-system-audio-arkts.md) | AVScreenCapture | 系统内录+后台任务 |
| [AudioFocus](01-媒体与下载/AudioFocus.md) | Audio Kit, AVSession | 音频焦点管理 |
| [AudioFormatSwitch](01-媒体与下载/AudioFormatSwitch.md) | AudioRender, AVPlayer | 音频格式无缝切换 |

### 02-UI 与 ArkUI（7 个项目）

| 项目 | 核心 API | 亮点 |
|------|---------|------|
| [PureTabs](02-UI与ArkUI/PureTabs.md) | Tabs, TabContent | MVVM 架构，双层嵌套 Tabs |
| [animation-collection](02-UI与ArkUI/animation-collection.md) | animateTo, animation | 常见动效合集 |
| [water-flow](02-UI与ArkUI/water-flow.md) | WaterFlow, LazyForEach | 瀑布流布局 |
| [component-collection](02-UI与ArkUI/component-collection.md) | ArkUI 全组件 | 组件/通用/动画/全局方法集合 |
| [HarmonyOSComponentUXExamples](02-UI与ArkUI/HarmonyOSComponentUXExamples.md) | ArkUI Design | 符合 HDS 规范的 UI 示例 |
| [custom-notification-badge](02-UI与ArkUI/custom-notification-badge.md) | notificationManager | 桌面角标与通知管理 |
| [SmallWindowScene](02-UI与ArkUI/SmallWindowScene.md) | List, Scroll, Stack | 小窗场景适配 |

### 03-导航与多设备（6 个项目）

| 项目 | 核心 API | 亮点 |
|------|---------|------|
| [multi-travel-navigation](03-导航与多设备/multi-travel-navigation.md) | Map Kit, Live View Kit | 多端地图导航+实况窗 |
| [MultiWeb](03-导航与多设备/MultiWeb.md) | CSS 响应式 | Web 端响应式多设备适配 |
| [multi-columns](03-导航与多设备/multi-columns.md) | RowSplit, ColumnSplit | 分栏控件响应式 |
| [fluent-news-homepage](03-导航与多设备/fluent-news-homepage.md) | Tabs, List, Breakpoint | 新闻首页+断点布局 |
| [WindowOrientation](03-导航与多设备/WindowOrientation.md) | 窗口旋转策略 | 5 种场景窗口旋转 |
| [SmartWatch](03-导航与多设备/SmartWatch.md) | Navigation, Timer | 手表端导航应用合集 |

### 04-架构与模块化（4 个项目）

| 项目 | 核心 API | 亮点 |
|------|---------|------|
| [CrossModuleResourceAccess](04-架构与模块化/CrossModuleResourceAccess.md) | resourceManager, createModuleContext | HAP+HAR+HSP 跨模块资源访问 |
| [APILevelAdapt](04-架构与模块化/APILevelAdapt.md) | deviceInfo.sdkApiVersion, dlopen | 三层架构 API 版本兼容 |
| [CrossModuleReference](04-架构与模块化/CrossModuleReference.md) | NAPI | Native 跨模块调用 |
| [OnlineEditorCollaboration](04-架构与模块化/OnlineEditorCollaboration.md) | ArkWeb, distributed | 跨设备协同编辑 |

### 05-网络与通信（5 个项目）

| 项目 | 核心 API | 亮点 |
|------|---------|------|
| [network-boost-kit-sample-code-arkts](05-网络与通信/network-boost-kit-sample-code-arkts.md) | netQuality, netHandover | 网络质量评估+连接迁移 |
| [network-query](05-网络与通信/network-query.md) | Network Kit, Telephony Kit | 网络信息查询 |
| [nearlink-kit_-sample-code](05-网络与通信/nearlink-kit_-sample-code.md) | NearLink Kit | 星闪设备发现与连接 |
| [BluetoothLowEnergy](05-网络与通信/BluetoothLowEnergy.md) | BLE Kit | 蓝牙低功耗心率广播 |
| [NetworkReconnection](05-网络与通信/NetworkReconnection.md) | Network Kit | 网络重连逻辑 |

### 06-安全与加密（4 个项目）

| 项目 | 核心 API | 亮点 |
|------|---------|------|
| [crypto-collection](06-安全与加密/crypto-collection.md) | cryptoFramework | 全算法加解密（AES/RSA/SM2/SM4） |
| [crypto-framework](06-安全与加密/crypto-framework.md) | cryptoFramework, filePicker | 文件加解密+签名验证 |
| [cipher](06-安全与加密/cipher.md) | cryptoFramework.Cipher | RSA+AES 字符串加解密 |
| [crypto-js-collection](06-安全与加密/crypto-js-collection.md) | @ohos/crypto-js | MD5/SHA/HMAC/PBKDF2 |

### 07-日志调试与性能（4 个项目）

| 项目 | 核心 API | 亮点 |
|------|---------|------|
| [GenerateSandboxFile](07-日志调试与性能/GenerateSandboxFile.md) | fileIo, preferences, KVStore | 沙箱文件一键生成+日志工具 |
| [DFX-Debug](07-日志调试与性能/DFX-Debug.md) | hidebug | 内存监控 PSS/Dirty |
| [DataCache](07-日志调试与性能/DataCache.md) | @hadss/datacache | 冷启动加速 50% |
| [FunctionFlowRuntimeKit-JobPartner-CPP](07-日志调试与性能/FunctionFlowRuntimeKit-JobPartner-CPP.md) | FFRT Kit | 并行任务调度 |

### 08-AI 与视觉（4 个项目）

| 项目 | 核心 API | 亮点 |
|------|---------|------|
| [core-vision-kit-object-detect](08-AI与视觉/core-vision-kit-object-detect.md) | Core Vision Kit | 11 类物体检测 |
| [graphic-creation](08-AI与视觉/graphic-creation.md) | AI OCR, MovingPhoto, HDR | AI 图文编创 |
| [visionkit-document-scan](08-AI与视觉/visionkit-document-scan.md) | Vision Kit | 文档扫描导出 |
| [cannkit-lm-engine-cpp](08-AI与视觉/cannkit-lm-engine-cpp.md) | CANN Kit | 大模型推理引擎 |

### 09-账号支付推送（6 个项目）

| 项目 | 核心 API | 亮点 |
|------|---------|------|
| [accountkit-h5](09-账号支付推送/accountkit-h5.md) | Account Kit | 华为账号一键登录 |
| [game-player-client-demo](09-账号支付推送/game-player-client-demo.md) | Game Service Kit | 游戏登录+防沉迷 |
| [payment-kit-clientdemo](09-账号支付推送/payment-kit-clientdemo.md) | Payment Kit | 一次性支付+签约代扣 |
| [push-kit-atomic](09-账号支付推送/push-kit-atomic.md) | Push Kit | 推送通知+服务卡片 |
| [GesturesShare](09-账号支付推送/GesturesShare.md) | Share Kit | 隔空手势分享 |
| [multi-mobile-payment](09-账号支付推送/multi-mobile-payment.md) | Scan Kit | 多平台扫码支付 |

---

## 开发环境要求

所有项目统一要求：
- **系统**：HarmonyOS 5.0.5 Release 及以上
- **IDE**：DevEco Studio 5.0.5 Release 及以上
- **SDK**：HarmonyOS 5.0.5 Release SDK 及以上
- **模型**：Stage 模型（FA 模型已废弃）

部分高级项目（NetBoost、GestureShare 等）需要 HarmonyOS 6.0.0 Beta5+。

## 技术栈分布

| 语言 | 项目数 | 占比 |
|------|-------|------|
| ArkTS | ~85% | 主要开发语言 |
| C++ | ~10% | Native 层、AI 推理、性能优化 |
| JavaScript/H5 | ~5% | Web 组件、H5 页面 |

## 相关资源

- GitCode 组织：https://gitcode.com/HarmonyOS_Samples
- Gitee 镜像：https://gitee.com/harmonyos_samples
- 华为开发者文档：https://developer.huawei.com/consumer/cn/doc/
- OpenHarmony 示例：https://gitee.com/openharmony/applications_app_samples
