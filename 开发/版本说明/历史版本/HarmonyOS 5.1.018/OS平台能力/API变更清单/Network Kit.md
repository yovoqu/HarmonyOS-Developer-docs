# Network Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-networkkit-510

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：HttpRequest； API声明：request(url: string, callback: AsyncCallback<HttpResponse>): void; 差异内容：NA | 类名：HttpRequest； API声明：request(url: string, callback: AsyncCallback<HttpResponse>): void; 差异内容：2300997,2300998 | api/@ohos.net.http.d.ts |
| 新增错误码 | 类名：HttpRequest； API声明：request(url: string, options: HttpRequestOptions, callback: AsyncCallback<HttpResponse>): void; 差异内容：NA | 类名：HttpRequest； API声明：request(url: string, options: HttpRequestOptions, callback: AsyncCallback<HttpResponse>): void; 差异内容：2300997,2300998 | api/@ohos.net.http.d.ts |
| 新增错误码 | 类名：HttpRequest； API声明：request(url: string, options?: HttpRequestOptions): Promise<HttpResponse>; 差异内容：NA | 类名：HttpRequest； API声明：request(url: string, options?: HttpRequestOptions): Promise<HttpResponse>; 差异内容：2300997,2300998 | api/@ohos.net.http.d.ts |
| 新增错误码 | 类名：HttpRequest； API声明：requestInStream(url: string, callback: AsyncCallback<number>): void; 差异内容：NA | 类名：HttpRequest； API声明：requestInStream(url: string, callback: AsyncCallback<number>): void; 差异内容：2300997 | api/@ohos.net.http.d.ts |
| 新增错误码 | 类名：HttpRequest； API声明：requestInStream(url: string, options: HttpRequestOptions, callback: AsyncCallback<number>): void; 差异内容：NA | 类名：HttpRequest； API声明：requestInStream(url: string, options: HttpRequestOptions, callback: AsyncCallback<number>): void; 差异内容：2300997 | api/@ohos.net.http.d.ts |
| 新增错误码 | 类名：HttpRequest； API声明：requestInStream(url: string, options?: HttpRequestOptions): Promise<number>; 差异内容：NA | 类名：HttpRequest； API声明：requestInStream(url: string, options?: HttpRequestOptions): Promise<number>; 差异内容：2300997 | api/@ohos.net.http.d.ts |
| 新增错误码 | 类名：UDPSocket； API声明：send(options: UDPSendOptions, callback: AsyncCallback<void>): void; 差异内容：NA | 类名：UDPSocket； API声明：send(options: UDPSendOptions, callback: AsyncCallback<void>): void; 差异内容：2301206,2301207,2301208,2301209,2301210,2301211,2301212,2301213 | api/@ohos.net.socket.d.ts |
| 新增错误码 | 类名：UDPSocket； API声明：send(options: UDPSendOptions): Promise<void>; 差异内容：NA | 类名：UDPSocket； API声明：send(options: UDPSendOptions): Promise<void>; 差异内容：2301206,2301207,2301208,2301209,2301210,2301211,2301212,2301213 | api/@ohos.net.socket.d.ts |
| 新增错误码 | 类名：TCPSocket； API声明：connect(options: TCPConnectOptions, callback: AsyncCallback<void>): void; 差异内容：NA | 类名：TCPSocket； API声明：connect(options: TCPConnectOptions, callback: AsyncCallback<void>): void; 差异内容：2301206,2301207,2301208,2301209,2301210,2301211,2301212,2301213 | api/@ohos.net.socket.d.ts |
| 新增错误码 | 类名：TCPSocket； API声明：connect(options: TCPConnectOptions): Promise<void>; 差异内容：NA | 类名：TCPSocket； API声明：connect(options: TCPConnectOptions): Promise<void>; 差异内容：2301206,2301207,2301208,2301209,2301210,2301211,2301212,2301213 | api/@ohos.net.socket.d.ts |
| 新增错误码 | 类名：TLSSocket； API声明：connect(options: TLSConnectOptions, callback: AsyncCallback<void>): void; 差异内容：NA | 类名：TLSSocket； API声明：connect(options: TLSConnectOptions, callback: AsyncCallback<void>): void; 差异内容：2301206,2301207,2301208,2301209,2301210,2301211,2301212,2301213 | api/@ohos.net.socket.d.ts |
| 新增错误码 | 类名：TLSSocket； API声明：connect(options: TLSConnectOptions): Promise<void>; 差异内容：NA | 类名：TLSSocket； API声明：connect(options: TLSConnectOptions): Promise<void>; 差异内容：2301206,2301207,2301208,2301209,2301210,2301211,2301212,2301213 | api/@ohos.net.socket.d.ts |
| 新增错误码 | 类名：WebSocket； API声明：connect(url: string, callback: AsyncCallback<boolean>): void; 差异内容：NA | 类名：WebSocket； API声明：connect(url: string, callback: AsyncCallback<boolean>): void; 差异内容：2302998 | api/@ohos.net.webSocket.d.ts |
| 新增错误码 | 类名：WebSocket； API声明：connect(url: string, options: WebSocketRequestOptions, callback: AsyncCallback<boolean>): void; 差异内容：NA | 类名：WebSocket； API声明：connect(url: string, options: WebSocketRequestOptions, callback: AsyncCallback<boolean>): void; 差异内容：2302998 | api/@ohos.net.webSocket.d.ts |
| 新增错误码 | 类名：WebSocket； API声明：connect(url: string, options?: WebSocketRequestOptions): Promise<boolean>; 差异内容：NA | 类名：WebSocket； API声明：connect(url: string, options?: WebSocketRequestOptions): Promise<boolean>; 差异内容：2302998 | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：http； API声明：export interface ServerAuthentication 差异内容：export interface ServerAuthentication | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：ServerAuthentication； API声明：credential: Credential; 差异内容：credential: Credential; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：ServerAuthentication； API声明：authenticationType?: AuthenticationType; 差异内容：authenticationType?: AuthenticationType; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：http； API声明：export type TlsOptions = 'system' \| TlsConfig; 差异内容：export type TlsOptions = 'system' \| TlsConfig; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：http； API声明：export type RemoteValidation = 'system' \| 'skip'; 差异内容：export type RemoteValidation = 'system' \| 'skip'; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：http； API声明：export type AuthenticationType = 'basic' \| 'ntlm' \| 'digest'; 差异内容：export type AuthenticationType = 'basic' \| 'ntlm' \| 'digest'; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：http； API声明：export interface Credential 差异内容：export interface Credential | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：Credential； API声明：username: string; 差异内容：username: string; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：Credential； API声明：password: string; 差异内容：password: string; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：http； API声明：export interface TlsConfig 差异内容：export interface TlsConfig | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：TlsConfig； API声明：tlsVersionMin: TlsVersion; 差异内容：tlsVersionMin: TlsVersion; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：TlsConfig； API声明：tlsVersionMax: TlsVersion; 差异内容：tlsVersionMax: TlsVersion; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：TlsConfig； API声明：cipherSuites?: CipherSuite[]; 差异内容：cipherSuites?: CipherSuite[]; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：http； API声明：export type TlsV13SpecificCipherSuite = 'TLS_AES_128_GCM_SHA256' \| 'TLS_AES_256_GCM_SHA384' \| 'TLS_CHACHA20_POLY1305_SHA256'; 差异内容：export type TlsV13SpecificCipherSuite = 'TLS_AES_128_GCM_SHA256' \| 'TLS_AES_256_GCM_SHA384' \| 'TLS_CHACHA20_POLY1305_SHA256'; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：http； API声明：export type TlsV12SpecificCipherSuite = 'TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256' \| 'TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256' \| 'TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384' \| 'TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384' \| 'TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256' \| 'TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256' \| 'TLS_RSA_WITH_AES_128_GCM_SHA256' \| 'TLS_RSA_WITH_AES_256_GCM_SHA384'; 差异内容：export type TlsV12SpecificCipherSuite = 'TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256' \| 'TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256' \| 'TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384' \| 'TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384' \| 'TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256' \| 'TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256' \| 'TLS_RSA_WITH_AES_128_GCM_SHA256' \| 'TLS_RSA_WITH_AES_256_GCM_SHA384'; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：http； API声明：export type TlsV10SpecificCipherSuite = 'TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA' \| 'TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA' \| 'TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA' \| 'TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA' \| 'TLS_RSA_WITH_AES_128_CBC_SHA' \| 'TLS_RSA_WITH_AES_256_CBC_SHA' \| 'TLS_RSA_WITH_3DES_EDE_CBC_SHA'; 差异内容：export type TlsV10SpecificCipherSuite = 'TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA' \| 'TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA' \| 'TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA' \| 'TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA' \| 'TLS_RSA_WITH_AES_128_CBC_SHA' \| 'TLS_RSA_WITH_AES_256_CBC_SHA' \| 'TLS_RSA_WITH_3DES_EDE_CBC_SHA'; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：http； API声明：export type CipherSuite = TlsV13CipherSuite; 差异内容：export type CipherSuite = TlsV13CipherSuite; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：http； API声明：export type TlsV13CipherSuite = TlsV12CipherSuite \| TlsV13SpecificCipherSuite; 差异内容：export type TlsV13CipherSuite = TlsV12CipherSuite \| TlsV13SpecificCipherSuite; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：http； API声明：export type TlsV12CipherSuite = TlsV11CipherSuite \| TlsV12SpecificCipherSuite; 差异内容：export type TlsV12CipherSuite = TlsV11CipherSuite \| TlsV12SpecificCipherSuite; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：http； API声明：export type TlsV11CipherSuite = TlsV10CipherSuite; 差异内容：export type TlsV11CipherSuite = TlsV10CipherSuite; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：http； API声明：export type TlsV10CipherSuite = TlsV10SpecificCipherSuite; 差异内容：export type TlsV10CipherSuite = TlsV10SpecificCipherSuite; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：http； API声明：export enum TlsVersion 差异内容：export enum TlsVersion | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：TlsVersion； API声明：TLS_V_1_0 = 4 差异内容：TLS_V_1_0 = 4 | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：TlsVersion； API声明：TLS_V_1_1 = 5 差异内容：TLS_V_1_1 = 5 | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：TlsVersion； API声明：TLS_V_1_2 = 6 差异内容：TLS_V_1_2 = 6 | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：TlsVersion； API声明：TLS_V_1_3 = 7 差异内容：TLS_V_1_3 = 7 | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：socket； API声明：export enum ProxyTypes 差异内容：export enum ProxyTypes | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：ProxyTypes； API声明：NONE = 0 差异内容：NONE = 0 | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：ProxyTypes； API声明：SOCKS5 = 1 差异内容：SOCKS5 = 1 | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：socket； API声明：export interface ProxyOptions 差异内容：export interface ProxyOptions | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：ProxyOptions； API声明：type: ProxyTypes; 差异内容：type: ProxyTypes; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：ProxyOptions； API声明：address: NetAddress; 差异内容：address: NetAddress; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：ProxyOptions； API声明：username?: string; 差异内容：username?: string; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：ProxyOptions； API声明：password?: string; 差异内容：password?: string; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：networkSecurity； API声明：export function isCleartextPermitted(): boolean; 差异内容：export function isCleartextPermitted(): boolean; | api/@ohos.net.networkSecurity.d.ts |
| 新增API | NA | 类名：networkSecurity； API声明：export function isCleartextPermittedByHostName(hostName: string): boolean; 差异内容：export function isCleartextPermittedByHostName(hostName: string): boolean; | api/@ohos.net.networkSecurity.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：HttpRequestOptions； API声明：remoteValidation?: RemoteValidation; 差异内容：remoteValidation?: RemoteValidation; | api/@ohos.net.http.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：HttpRequestOptions； API声明：tlsOptions?: TlsOptions; 差异内容：tlsOptions?: TlsOptions; | api/@ohos.net.http.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：HttpRequestOptions； API声明：serverAuthentication?: ServerAuthentication; 差异内容：serverAuthentication?: ServerAuthentication; | api/@ohos.net.http.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：UDPSendOptions； API声明：proxy?: ProxyOptions; 差异内容：proxy?: ProxyOptions; | api/@ohos.net.socket.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：TCPConnectOptions； API声明：proxy?: ProxyOptions; 差异内容：proxy?: ProxyOptions; | api/@ohos.net.socket.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：TLSConnectOptions； API声明：proxy?: ProxyOptions; 差异内容：proxy?: ProxyOptions; | api/@ohos.net.socket.d.ts |
