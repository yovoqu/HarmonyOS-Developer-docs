# Network Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-networkkit-6002

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明：declare namespace eap 差异内容：declare namespace eap | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：eap； API声明：function regCustomEapHandler(netType: number, eapCode: number, eapType: number, callback: Callback&lt;EapData&gt;): void; 差异内容：function regCustomEapHandler(netType: number, eapCode: number, eapType: number, callback: Callback&lt;EapData&gt;): void; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：eap； API声明：function unregCustomEapHandler(netType: number, eapCode: number, eapType: number, callback: Callback&lt;EapData&gt;): void; 差异内容：function unregCustomEapHandler(netType: number, eapCode: number, eapType: number, callback: Callback&lt;EapData&gt;): void; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：eap； API声明：function replyCustomEapData(result: CustomResult, data: EapData): void; 差异内容：function replyCustomEapData(result: CustomResult, data: EapData): void; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：eap； API声明：function startEthEap(netId: number, profile: EthEapProfile): void; 差异内容：function startEthEap(netId: number, profile: EthEapProfile): void; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：eap； API声明：function logOffEthEap(netId: number): void; 差异内容：function logOffEthEap(netId: number): void; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：eap； API声明：interface EapData 差异内容：interface EapData | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EapData； API声明：msgId: number; 差异内容：msgId: number; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EapData； API声明：eapBuffer: Uint8Array; 差异内容：eapBuffer: Uint8Array; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EapData； API声明：bufferLen: number; 差异内容：bufferLen: number; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：eap； API声明：enum CustomResult 差异内容：enum CustomResult | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：CustomResult； API声明：RESULT_FAIL 差异内容：RESULT_FAIL | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：CustomResult； API声明：RESULT_NEXT 差异内容：RESULT_NEXT | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：CustomResult； API声明：RESULT_FINISH 差异内容：RESULT_FINISH | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：eap； API声明：enum EapMethod 差异内容：enum EapMethod | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EapMethod； API声明：EAP_NONE 差异内容：EAP_NONE | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EapMethod； API声明：EAP_PEAP 差异内容：EAP_PEAP | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EapMethod； API声明：EAP_TLS 差异内容：EAP_TLS | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EapMethod； API声明：EAP_TTLS 差异内容：EAP_TTLS | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EapMethod； API声明：EAP_PWD 差异内容：EAP_PWD | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EapMethod； API声明：EAP_SIM 差异内容：EAP_SIM | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EapMethod； API声明：EAP_AKA 差异内容：EAP_AKA | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EapMethod； API声明：EAP_AKA_PRIME 差异内容：EAP_AKA_PRIME | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EapMethod； API声明：EAP_UNAUTH_TLS 差异内容：EAP_UNAUTH_TLS | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：eap； API声明：enum Phase2Method 差异内容：enum Phase2Method | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：Phase2Method； API声明：PHASE2_NONE 差异内容：PHASE2_NONE | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：Phase2Method； API声明：PHASE2_PAP 差异内容：PHASE2_PAP | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：Phase2Method； API声明：PHASE2_MSCHAP 差异内容：PHASE2_MSCHAP | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：Phase2Method； API声明：PHASE2_MSCHAPV2 差异内容：PHASE2_MSCHAPV2 | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：Phase2Method； API声明：PHASE2_GTC 差异内容：PHASE2_GTC | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：Phase2Method； API声明：PHASE2_SIM 差异内容：PHASE2_SIM | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：Phase2Method； API声明：PHASE2_AKA 差异内容：PHASE2_AKA | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：Phase2Method； API声明：PHASE2_AKA_PRIME 差异内容：PHASE2_AKA_PRIME | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：eap； API声明：interface EthEapProfile 差异内容：interface EthEapProfile | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapProfile； API声明：eapMethod: EapMethod; 差异内容：eapMethod: EapMethod; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapProfile； API声明：phase2Method: Phase2Method; 差异内容：phase2Method: Phase2Method; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapProfile； API声明：identity: string; 差异内容：identity: string; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapProfile； API声明：anonymousIdentity: string; 差异内容：anonymousIdentity: string; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapProfile； API声明：password: string; 差异内容：password: string; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapProfile； API声明：caCertAliases: string; 差异内容：caCertAliases: string; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapProfile； API声明：caPath: string; 差异内容：caPath: string; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapProfile； API声明：clientCertAliases: string; 差异内容：clientCertAliases: string; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapProfile； API声明：certEntry: Uint8Array; 差异内容：certEntry: Uint8Array; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapProfile； API声明：certPassword: string; 差异内容：certPassword: string; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapProfile； API声明：altSubjectMatch: string; 差异内容：altSubjectMatch: string; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapProfile； API声明：domainSuffixMatch: string; 差异内容：domainSuffixMatch: string; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapProfile； API声明：realm: string; 差异内容：realm: string; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapProfile； API声明：plmn: string; 差异内容：plmn: string; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：EthEapProfile； API声明：eapSubId: number; 差异内容：eapSubId: number; | api/@ohos.net.eap.d.ts |
| 新增API | NA | 类名：connection； API声明：function setNetExtAttribute(netHandle: NetHandle, netExtAttribute: string): Promise&lt;void&gt;; 差异内容：function setNetExtAttribute(netHandle: NetHandle, netExtAttribute: string): Promise&lt;void&gt;; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection； API声明：function setNetExtAttributeSync(netHandle: NetHandle, netExtAttribute: string): void; 差异内容：function setNetExtAttributeSync(netHandle: NetHandle, netExtAttribute: string): void; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection； API声明：function getNetExtAttribute(netHandle: NetHandle): Promise&lt;string&gt;; 差异内容：function getNetExtAttribute(netHandle: NetHandle): Promise&lt;string&gt;; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection； API声明：function getNetExtAttributeSync(netHandle: NetHandle): string; 差异内容：function getNetExtAttributeSync(netHandle: NetHandle): string; | api/@ohos.net.connection.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@ohos.net.eap.d.ts 差异内容：NetworkKit | api/@ohos.net.eap.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：WebSocketRequestOptions； API声明：skipServerCertVerification?: boolean; 差异内容：skipServerCertVerification?: boolean; | api/@ohos.net.webSocket.d.ts |
