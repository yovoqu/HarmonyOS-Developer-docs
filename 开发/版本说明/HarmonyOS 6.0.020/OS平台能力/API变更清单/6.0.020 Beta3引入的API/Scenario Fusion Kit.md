# Scenario Fusion Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-scenariofusionkit-6003

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：OpenType； API声明：REQUEST_SUBSCRIBE_MESSAGE = 12 差异内容：REQUEST_SUBSCRIBE_MESSAGE = 12 | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：OpenType； API声明：SHARE = 13 差异内容：SHARE = 13 | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：OpenType； API声明：FEEDBACK = 14 差异内容：FEEDBACK = 14 | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：functionalButtonComponentManager； API声明：export interface RequestSubscribeMessageResult 差异内容：export interface RequestSubscribeMessageResult | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：RequestSubscribeMessageResult； API声明：code: string; 差异内容：code: string; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：functionalButtonComponentManager； API声明：export interface ShareParam 差异内容：export interface ShareParam | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：ShareParam； API声明：description?: string; 差异内容：description?: string; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：ShareParam； API声明：previewUri?: string; 差异内容：previewUri?: string; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 类新增必选属性或非同名方法 | 类名：global； API声明： 差异内容：NA | 类名：FunctionalButtonController； API声明：onRequestSubscribeMessage(callback: AsyncCallback<RequestSubscribeMessageResult>): FunctionalButtonController; 差异内容：onRequestSubscribeMessage(callback: AsyncCallback<RequestSubscribeMessageResult>): FunctionalButtonController; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 类新增必选属性或非同名方法 | 类名：global； API声明： 差异内容：NA | 类名：FunctionalButtonController； API声明：onShare(callback: AsyncCallback<void>): FunctionalButtonController; 差异内容：onShare(callback: AsyncCallback<void>): FunctionalButtonController; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 类新增必选属性或非同名方法 | 类名：global； API声明： 差异内容：NA | 类名：FunctionalButtonController； API声明：onFeedback(callback: AsyncCallback<void>): FunctionalButtonController; 差异内容：onFeedback(callback: AsyncCallback<void>): FunctionalButtonController; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：FunctionalButtonParams； API声明：subSceneId?: string; 差异内容：subSceneId?: string; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：FunctionalButtonParams； API声明：shareParam?: ShareParam; 差异内容：shareParam?: ShareParam; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
