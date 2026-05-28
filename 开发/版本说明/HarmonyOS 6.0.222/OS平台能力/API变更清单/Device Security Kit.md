# Device Security Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicesecuritykit-6021

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明：declare namespace superPrivacyMode 差异内容：declare namespace superPrivacyMode | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：superPrivacyMode； API声明：function getSuperPrivacyMode(): Promise&lt;SuperPrivacyMode&gt;; 差异内容：function getSuperPrivacyMode(): Promise&lt;SuperPrivacyMode&gt;; | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：superPrivacyMode； API声明：function on(type: 'superPrivacyModeChange', callback: Callback&lt;SuperPrivacyMode&gt;): void; 差异内容：function on(type: 'superPrivacyModeChange', callback: Callback&lt;SuperPrivacyMode&gt;): void; | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：superPrivacyMode； API声明：enum SuperPrivacyMode 差异内容：enum SuperPrivacyMode | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：SuperPrivacyMode； API声明：OFF = 0 差异内容：OFF = 0 | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：SuperPrivacyMode； API声明：ON_WHEN_FOLDED = 1 差异内容：ON_WHEN_FOLDED = 1 | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：SuperPrivacyMode； API声明：ALWAYS_ON = 2 差异内容：ALWAYS_ON = 2 | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：superPrivacyMode； API声明：function off(type: 'superPrivacyModeChange', callback?: Callback&lt;SuperPrivacyMode&gt;): void; 差异内容：function off(type: 'superPrivacyModeChange', callback?: Callback&lt;SuperPrivacyMode&gt;): void; | api/@hms.security.superPrivacyMode.d.ts |
| 新增API | NA | 类名：businessRiskIntelligentDetection； API声明：interface SimulatedClickDetectionEnhancedRequest 差异内容：interface SimulatedClickDetectionEnhancedRequest | api/@hms.security.businessRiskIntelligentDetection.d.ts |
| 新增API | NA | 类名：SimulatedClickDetectionEnhancedRequest； API声明：version?: number; 差异内容：version?: number; | api/@hms.security.businessRiskIntelligentDetection.d.ts |
| 新增API | NA | 类名：SimulatedClickDetectionEnhancedRequest； API声明：nonce: Uint8Array; 差异内容：nonce: Uint8Array; | api/@hms.security.businessRiskIntelligentDetection.d.ts |
| 新增API | NA | 类名：SimulatedClickDetectionEnhancedRequest； API声明：algorithm: SigningAlgorithm; 差异内容：algorithm: SigningAlgorithm; | api/@hms.security.businessRiskIntelligentDetection.d.ts |
| 新增API | NA | 类名：businessRiskIntelligentDetection； API声明：function detectSimulatedClickRiskEnhanced(params: SimulatedClickDetectionEnhancedRequest): Promise&lt;string&gt;; 差异内容：function detectSimulatedClickRiskEnhanced(params: SimulatedClickDetectionEnhancedRequest): Promise&lt;string&gt;; | api/@hms.security.businessRiskIntelligentDetection.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@hms.security.superPrivacyMode.d.ts 差异内容：DeviceSecurityKit | api/@hms.security.superPrivacyMode.d.ts |
