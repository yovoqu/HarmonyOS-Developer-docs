# Device Security Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-devicesecuritykit-b060

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明： declare namespace businessRiskIntelligentDetection 差异内容： declare namespace businessRiskIntelligentDetection | api/@hms.security.businessRiskIntelligentDetection.d.ts |
| 新增API | NA | 类名：businessRiskIntelligentDetection； API声明： enum SigningAlgorithm 差异内容： enum SigningAlgorithm | api/@hms.security.businessRiskIntelligentDetection.d.ts |
| 新增API | NA | 类名：SigningAlgorithm； API声明：ES256 = 0 差异内容：ES256 = 0 | api/@hms.security.businessRiskIntelligentDetection.d.ts |
| 新增API | NA | 类名：businessRiskIntelligentDetection； API声明： interface FraudDetectionRequest 差异内容： interface FraudDetectionRequest | api/@hms.security.businessRiskIntelligentDetection.d.ts |
| 新增API | NA | 类名：FraudDetectionRequest； API声明：nonce: Uint8Array; 差异内容：nonce: Uint8Array; | api/@hms.security.businessRiskIntelligentDetection.d.ts |
| 新增API | NA | 类名：FraudDetectionRequest； API声明：algorithm: SigningAlgorithm; 差异内容：algorithm: SigningAlgorithm; | api/@hms.security.businessRiskIntelligentDetection.d.ts |
| 新增API | NA | 类名：businessRiskIntelligentDetection； API声明：function detectFraudRisk(params: FraudDetectionRequest): Promise&lt;string&gt;; 差异内容：function detectFraudRisk(params: FraudDetectionRequest): Promise&lt;string&gt;; | api/@hms.security.businessRiskIntelligentDetection.d.ts |
