# Scenario Fusion Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-scenariofusionkit-b031

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：OpenType； API声明：REAL_NAME_AUTHENTICATION = 7 差异内容：REAL_NAME_AUTHENTICATION = 7 | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：OpenType； API声明：FACE_AUTHENTICATION = 8 差异内容：FACE_AUTHENTICATION = 8 | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：functionalButtonComponentManager； API声明： export interface RealNameAuthenticationResult 差异内容： export interface RealNameAuthenticationResult | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：RealNameAuthenticationResult； API声明：authCode?: string; 差异内容：authCode?: string; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：RealNameAuthenticationResult； API声明：openID?: string; 差异内容：openID?: string; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：functionalButtonComponentManager； API声明： export interface FaceAuthenticationResult 差异内容： export interface FaceAuthenticationResult | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：FaceAuthenticationResult； API声明：authCode?: string; 差异内容：authCode?: string; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：FaceAuthenticationResult； API声明：openID?: string; 差异内容：openID?: string; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：functionalButtonComponentManager； API声明： export interface FaceVerificationResult 差异内容： export interface FaceVerificationResult | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：FaceVerificationResult； API声明：facialRecognitionVerificationToken?: string; 差异内容：facialRecognitionVerificationToken?: string; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：FaceVerificationResult； API声明：state?: string; 差异内容：state?: string; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：FunctionalButtonController； API声明：onRealNameAuthentication(callback: AsyncCallback&lt;RealNameAuthenticationResult&gt;): FunctionalButtonController; 差异内容：onRealNameAuthentication(callback: AsyncCallback&lt;RealNameAuthenticationResult&gt;): FunctionalButtonController; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：FunctionalButtonController； API声明：onFaceAuthentication(callback: AsyncCallback&lt;FaceAuthenticationResult&gt;): FunctionalButtonController; 差异内容：onFaceAuthentication(callback: AsyncCallback&lt;FaceAuthenticationResult&gt;): FunctionalButtonController; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
| 新增API | NA | 类名：FunctionalButtonController； API声明：onFaceVerification(verifyToken: string, callback: AsyncCallback&lt;FaceVerificationResult&gt;): void; 差异内容：onFaceVerification(verifyToken: string, callback: AsyncCallback&lt;FaceVerificationResult&gt;): void; | api/@hms.core.atomicserviceComponent.atomicserviceUi.d.ets |
