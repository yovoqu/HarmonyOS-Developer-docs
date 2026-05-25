# push-kit-atomic — 推送通知元服务

> 来源：https://gitcode.com/HarmonyOS_Samples/push-kit-sample-code-client-atomic-arkts  
> 语言：ArkTS (97%) | 版本要求：HarmonyOS NEXT Beta5+

## 项目简介

基于 Push Kit 的推送服务元服务项目，演示基于华为账号 ID 订阅推送、使用服务通知模板、通知点击跳转。

## 核心 API

| API | 用途 |
|-----|------|
| Push Kit 订阅 API | 获取 Push Token，订阅主题 |
| `serviceNotification` | 服务通知模板 |
| 华为账号登录 | 用户身份标识 |
| `ClickActionAbility` | 通知点击动作处理 |

## 项目结构

```
ClickActionAbility.ets       — 通知点击处理
SubscribePage.ets            — 订阅 UI
ClickActionInnerPage.ets     — 落地页
```

## 配置要求

需在 AppGallery Connect 开通 Push 服务，配置模板 ID。
