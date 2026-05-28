# ArkWeb

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkweb-5111

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API从不支持元服务到支持元服务 | 类名：webview； API声明：enum ProxySchemeFilter 差异内容：NA | 类名：webview； API声明：enum ProxySchemeFilter 差异内容：atomicservice | api/@ohos.web.webview.d.ts |
| API从不支持元服务到支持元服务 | 类名：ProxySchemeFilter； API声明：MATCH_ALL_SCHEMES = 0 差异内容：NA | 类名：ProxySchemeFilter； API声明：MATCH_ALL_SCHEMES = 0 差异内容：atomicservice | api/@ohos.web.webview.d.ts |
| API从不支持元服务到支持元服务 | 类名：ProxySchemeFilter； API声明：MATCH_HTTP = 1 差异内容：NA | 类名：ProxySchemeFilter； API声明：MATCH_HTTP = 1 差异内容：atomicservice | api/@ohos.web.webview.d.ts |
| API从不支持元服务到支持元服务 | 类名：ProxySchemeFilter； API声明：MATCH_HTTPS = 2 差异内容：NA | 类名：ProxySchemeFilter； API声明：MATCH_HTTPS = 2 差异内容：atomicservice | api/@ohos.web.webview.d.ts |
| API从不支持元服务到支持元服务 | 类名：webview； API声明：class ProxyConfig 差异内容：NA | 类名：webview； API声明：class ProxyConfig 差异内容：atomicservice | api/@ohos.web.webview.d.ts |
| API从不支持元服务到支持元服务 | 类名：ProxyConfig； API声明：insertBypassRule(bypassRule: string): void; 差异内容：NA | 类名：ProxyConfig； API声明：insertBypassRule(bypassRule: string): void; 差异内容：atomicservice | api/@ohos.web.webview.d.ts |
| API从不支持元服务到支持元服务 | 类名：ProxyConfig； API声明：insertDirectRule(schemeFilter?: ProxySchemeFilter): void; 差异内容：NA | 类名：ProxyConfig； API声明：insertDirectRule(schemeFilter?: ProxySchemeFilter): void; 差异内容：atomicservice | api/@ohos.web.webview.d.ts |
| API从不支持元服务到支持元服务 | 类名：ProxyConfig； API声明：insertProxyRule(proxyRule: string, schemeFilter?: ProxySchemeFilter): void; 差异内容：NA | 类名：ProxyConfig； API声明：insertProxyRule(proxyRule: string, schemeFilter?: ProxySchemeFilter): void; 差异内容：atomicservice | api/@ohos.web.webview.d.ts |
| API从不支持元服务到支持元服务 | 类名：ProxyConfig； API声明：bypassHostnamesWithoutPeriod(): void; 差异内容：NA | 类名：ProxyConfig； API声明：bypassHostnamesWithoutPeriod(): void; 差异内容：atomicservice | api/@ohos.web.webview.d.ts |
| API从不支持元服务到支持元服务 | 类名：ProxyConfig； API声明：clearImplicitRules(): void; 差异内容：NA | 类名：ProxyConfig； API声明：clearImplicitRules(): void; 差异内容：atomicservice | api/@ohos.web.webview.d.ts |
| API从不支持元服务到支持元服务 | 类名：ProxyConfig； API声明：enableReverseBypass(reverse: boolean): void; 差异内容：NA | 类名：ProxyConfig； API声明：enableReverseBypass(reverse: boolean): void; 差异内容：atomicservice | api/@ohos.web.webview.d.ts |
| API从不支持元服务到支持元服务 | 类名：ProxyConfig； API声明：getBypassRules(): Array&lt;string&gt;; 差异内容：NA | 类名：ProxyConfig； API声明：getBypassRules(): Array&lt;string&gt;; 差异内容：atomicservice | api/@ohos.web.webview.d.ts |
| API从不支持元服务到支持元服务 | 类名：ProxyConfig； API声明：getProxyRules(): Array&lt;ProxyRule&gt;; 差异内容：NA | 类名：ProxyConfig； API声明：getProxyRules(): Array&lt;ProxyRule&gt;; 差异内容：atomicservice | api/@ohos.web.webview.d.ts |
| API从不支持元服务到支持元服务 | 类名：ProxyConfig； API声明：isReverseBypassEnabled(): boolean; 差异内容：NA | 类名：ProxyConfig； API声明：isReverseBypassEnabled(): boolean; 差异内容：atomicservice | api/@ohos.web.webview.d.ts |
| API从不支持元服务到支持元服务 | 类名：webview； API声明：class ProxyRule 差异内容：NA | 类名：webview； API声明：class ProxyRule 差异内容：atomicservice | api/@ohos.web.webview.d.ts |
| API从不支持元服务到支持元服务 | 类名：ProxyRule； API声明：getSchemeFilter(): ProxySchemeFilter; 差异内容：NA | 类名：ProxyRule； API声明：getSchemeFilter(): ProxySchemeFilter; 差异内容：atomicservice | api/@ohos.web.webview.d.ts |
| API从不支持元服务到支持元服务 | 类名：ProxyRule； API声明：getUrl(): string; 差异内容：NA | 类名：ProxyRule； API声明：getUrl(): string; 差异内容：atomicservice | api/@ohos.web.webview.d.ts |
| API从不支持元服务到支持元服务 | 类名：webview； API声明：type OnProxyConfigChangeCallback = () => void; 差异内容：NA | 类名：webview； API声明：type OnProxyConfigChangeCallback = () => void; 差异内容：atomicservice | api/@ohos.web.webview.d.ts |
| API从不支持元服务到支持元服务 | 类名：webview； API声明：class ProxyController 差异内容：NA | 类名：webview； API声明：class ProxyController 差异内容：atomicservice | api/@ohos.web.webview.d.ts |
| API从不支持元服务到支持元服务 | 类名：ProxyController； API声明：static applyProxyOverride(proxyConfig: ProxyConfig, callback: OnProxyConfigChangeCallback): void; 差异内容：NA | 类名：ProxyController； API声明：static applyProxyOverride(proxyConfig: ProxyConfig, callback: OnProxyConfigChangeCallback): void; 差异内容：atomicservice | api/@ohos.web.webview.d.ts |
| API从不支持元服务到支持元服务 | 类名：ProxyController； API声明：static removeProxyOverride(callback: OnProxyConfigChangeCallback): void; 差异内容：NA | 类名：ProxyController； API声明：static removeProxyOverride(callback: OnProxyConfigChangeCallback): void; 差异内容：atomicservice | api/@ohos.web.webview.d.ts |
| 错误码变更 | 类名：WebviewController； API声明：static prepareForPageLoad(url: string, preconnectable: boolean, numSockets: number): void; 差异内容：171000013,17100002 | 类名：WebviewController； API声明：static prepareForPageLoad(url: string, preconnectable: boolean, numSockets: number): void; 差异内容：17100002,17100013 | api/@ohos.web.webview.d.ts |
