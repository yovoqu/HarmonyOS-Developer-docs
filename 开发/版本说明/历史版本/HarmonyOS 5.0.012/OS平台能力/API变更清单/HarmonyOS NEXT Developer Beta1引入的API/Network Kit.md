# Network Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-networkkit-hdc

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：connection； API声明：function getDefaultNet(): Promise&lt;NetHandle&gt;; 差异内容：NA | 类名：connection； API声明：function getDefaultNet(): Promise&lt;NetHandle&gt;; 差异内容：201,2100002,2100003 | api/@ohos.net.connection.d.ts |
| 错误码变更 | 类名：connection； API声明：function getAllNets(): Promise<Array&lt;NetHandle&gt;>; 差异内容：NA | 类名：connection； API声明：function getAllNets(): Promise<Array&lt;NetHandle&gt;>; 差异内容：201,2100002,2100003 | api/@ohos.net.connection.d.ts |
| 错误码变更 | 类名：connection； API声明：function getConnectionProperties(netHandle: NetHandle): Promise&lt;ConnectionProperties&gt;; 差异内容：NA | 类名：connection； API声明：function getConnectionProperties(netHandle: NetHandle): Promise&lt;ConnectionProperties&gt;; 差异内容：201,2100001,2100002,2100003,401 | api/@ohos.net.connection.d.ts |
| 错误码变更 | 类名：connection； API声明：function getNetCapabilities(netHandle: NetHandle): Promise&lt;NetCapabilities&gt;; 差异内容：NA | 类名：connection； API声明：function getNetCapabilities(netHandle: NetHandle): Promise&lt;NetCapabilities&gt;; 差异内容：201,2100001,2100002,2100003,401 | api/@ohos.net.connection.d.ts |
| 错误码变更 | 类名：connection； API声明：function isDefaultNetMetered(): Promise&lt;boolean&gt;; 差异内容：NA | 类名：connection； API声明：function isDefaultNetMetered(): Promise&lt;boolean&gt;; 差异内容：201,2100002,2100003 | api/@ohos.net.connection.d.ts |
| 错误码变更 | 类名：connection； API声明：function hasDefaultNet(): Promise&lt;boolean&gt;; 差异内容：NA | 类名：connection； API声明：function hasDefaultNet(): Promise&lt;boolean&gt;; 差异内容：201,2100002,2100003 | api/@ohos.net.connection.d.ts |
| 错误码变更 | 类名：connection； API声明：function reportNetConnected(netHandle: NetHandle): Promise&lt;void&gt;; 差异内容：NA | 类名：connection； API声明：function reportNetConnected(netHandle: NetHandle): Promise&lt;void&gt;; 差异内容：201,2100001,2100002,2100003,401 | api/@ohos.net.connection.d.ts |
| 错误码变更 | 类名：connection； API声明：function reportNetDisconnected(netHandle: NetHandle): Promise&lt;void&gt;; 差异内容：NA | 类名：connection； API声明：function reportNetDisconnected(netHandle: NetHandle): Promise&lt;void&gt;; 差异内容：201,2100001,2100002,2100003,401 | api/@ohos.net.connection.d.ts |
| 错误码变更 | 类名：connection； API声明：function getAddressesByName(host: string): Promise<Array&lt;NetAddress&gt;>; 差异内容：NA | 类名：connection； API声明：function getAddressesByName(host: string): Promise<Array&lt;NetAddress&gt;>; 差异内容：201,2100001,2100002,2100003,401 | api/@ohos.net.connection.d.ts |
| 错误码变更 | 类名：NetHandle； API声明：bindSocket(socketParam: TCPSocket \| UDPSocket): Promise&lt;void&gt;; 差异内容：NA | 类名：NetHandle； API声明：bindSocket(socketParam: TCPSocket \| UDPSocket): Promise&lt;void&gt;; 差异内容：2100001,2100002,2100003,401 | api/@ohos.net.connection.d.ts |
| 错误码变更 | 类名：NetHandle； API声明：getAddressesByName(host: string): Promise<Array&lt;NetAddress&gt;>; 差异内容：NA | 类名：NetHandle； API声明：getAddressesByName(host: string): Promise<Array&lt;NetAddress&gt;>; 差异内容：201,2100001,2100002,2100003,401 | api/@ohos.net.connection.d.ts |
| 错误码变更 | 类名：NetHandle； API声明：getAddressByName(host: string): Promise&lt;NetAddress&gt;; 差异内容：NA | 类名：NetHandle； API声明：getAddressByName(host: string): Promise&lt;NetAddress&gt;; 差异内容：201,2100001,2100002,2100003,401 | api/@ohos.net.connection.d.ts |
| 错误码变更 | 类名：HttpRequest； API声明：request(url: string, options: HttpRequestOptions, callback: AsyncCallback&lt;HttpResponse&gt;): void; 差异内容：NA | 类名：HttpRequest； API声明：request(url: string, options: HttpRequestOptions, callback: AsyncCallback&lt;HttpResponse&gt;): void; 差异内容：201,2300001,2300003,2300005,2300006,2300007,2300008,2300009,2300016,2300018,2300023,2300025,2300026,2300027,2300028,2300047,2300052,2300055,2300056,2300058,2300059,2300060,2300061,2300063,2300070,2300073,2300077,2300078,2300094,2300999,401 | api/@ohos.net.http.d.ts |
| 错误码变更 | 类名：HttpRequest； API声明：request(url: string, options?: HttpRequestOptions): Promise&lt;HttpResponse&gt;; 差异内容：NA | 类名：HttpRequest； API声明：request(url: string, options?: HttpRequestOptions): Promise&lt;HttpResponse&gt;; 差异内容：201,2300001,2300003,2300005,2300006,2300007,2300008,2300009,2300016,2300018,2300023,2300025,2300026,2300027,2300028,2300047,2300052,2300055,2300056,2300058,2300059,2300060,2300061,2300063,2300070,2300073,2300077,2300078,2300094,2300999,401 | api/@ohos.net.http.d.ts |
| 错误码变更 | 类名：UDPSocket； API声明：bind(address: NetAddress): Promise&lt;void&gt;; 差异内容：NA | 类名：UDPSocket； API声明：bind(address: NetAddress): Promise&lt;void&gt;; 差异内容：201,401 | api/@ohos.net.socket.d.ts |
| 错误码变更 | 类名：UDPSocket； API声明：send(options: UDPSendOptions): Promise&lt;void&gt;; 差异内容：NA | 类名：UDPSocket； API声明：send(options: UDPSendOptions): Promise&lt;void&gt;; 差异内容：201,401 | api/@ohos.net.socket.d.ts |
| 错误码变更 | 类名：UDPSocket； API声明：close(): Promise&lt;void&gt;; 差异内容：NA | 类名：UDPSocket； API声明：close(): Promise&lt;void&gt;; 差异内容：201 | api/@ohos.net.socket.d.ts |
| 错误码变更 | 类名：UDPSocket； API声明：getState(): Promise&lt;SocketStateBase&gt;; 差异内容：NA | 类名：UDPSocket； API声明：getState(): Promise&lt;SocketStateBase&gt;; 差异内容：201 | api/@ohos.net.socket.d.ts |
| 错误码变更 | 类名：UDPSocket； API声明：setExtraOptions(options: UDPExtraOptions): Promise&lt;void&gt;; 差异内容：NA | 类名：UDPSocket； API声明：setExtraOptions(options: UDPExtraOptions): Promise&lt;void&gt;; 差异内容：201,401 | api/@ohos.net.socket.d.ts |
| 错误码变更 | 类名：TCPSocket； API声明：bind(address: NetAddress): Promise&lt;void&gt;; 差异内容：NA | 类名：TCPSocket； API声明：bind(address: NetAddress): Promise&lt;void&gt;; 差异内容：201,401 | api/@ohos.net.socket.d.ts |
| 错误码变更 | 类名：TCPSocket； API声明：connect(options: TCPConnectOptions): Promise&lt;void&gt;; 差异内容：NA | 类名：TCPSocket； API声明：connect(options: TCPConnectOptions): Promise&lt;void&gt;; 差异内容：201,401 | api/@ohos.net.socket.d.ts |
| 错误码变更 | 类名：TCPSocket； API声明：send(options: TCPSendOptions): Promise&lt;void&gt;; 差异内容：NA | 类名：TCPSocket； API声明：send(options: TCPSendOptions): Promise&lt;void&gt;; 差异内容：201,401 | api/@ohos.net.socket.d.ts |
| 错误码变更 | 类名：TCPSocket； API声明：close(): Promise&lt;void&gt;; 差异内容：NA | 类名：TCPSocket； API声明：close(): Promise&lt;void&gt;; 差异内容：201 | api/@ohos.net.socket.d.ts |
| 错误码变更 | 类名：TCPSocket； API声明：getRemoteAddress(): Promise&lt;NetAddress&gt;; 差异内容：NA | 类名：TCPSocket； API声明：getRemoteAddress(): Promise&lt;NetAddress&gt;; 差异内容：201 | api/@ohos.net.socket.d.ts |
| 错误码变更 | 类名：TCPSocket； API声明：getState(): Promise&lt;SocketStateBase&gt;; 差异内容：NA | 类名：TCPSocket； API声明：getState(): Promise&lt;SocketStateBase&gt;; 差异内容：201 | api/@ohos.net.socket.d.ts |
| 错误码变更 | 类名：TCPSocket； API声明：setExtraOptions(options: TCPExtraOptions): Promise&lt;void&gt;; 差异内容：NA | 类名：TCPSocket； API声明：setExtraOptions(options: TCPExtraOptions): Promise&lt;void&gt;; 差异内容：201,401 | api/@ohos.net.socket.d.ts |
| 错误码变更 | 类名：TLSSocket； API声明：bind(address: NetAddress): Promise&lt;void&gt;; 差异内容：NA | 类名：TLSSocket； API声明：bind(address: NetAddress): Promise&lt;void&gt;; 差异内容：201,2300002,2303198,401 | api/@ohos.net.socket.d.ts |
| 错误码变更 | 类名：TLSSocket； API声明：getRemoteAddress(): Promise&lt;NetAddress&gt;; 差异内容：NA | 类名：TLSSocket； API声明：getRemoteAddress(): Promise&lt;NetAddress&gt;; 差异内容：2300002,2303188 | api/@ohos.net.socket.d.ts |
| 错误码变更 | 类名：TLSSocket； API声明：getState(): Promise&lt;SocketStateBase&gt;; 差异内容：NA | 类名：TLSSocket； API声明：getState(): Promise&lt;SocketStateBase&gt;; 差异内容：2300002,2303188 | api/@ohos.net.socket.d.ts |
| 错误码变更 | 类名：TLSSocket； API声明：setExtraOptions(options: TCPExtraOptions): Promise&lt;void&gt;; 差异内容：NA | 类名：TLSSocket； API声明：setExtraOptions(options: TCPExtraOptions): Promise&lt;void&gt;; 差异内容：2300002,2303188,401 | api/@ohos.net.socket.d.ts |
| 错误码变更 | 类名：TLSSocket； API声明：getCertificate(): Promise&lt;X509CertRawData&gt;; 差异内容：NA | 类名：TLSSocket； API声明：getCertificate(): Promise&lt;X509CertRawData&gt;; 差异内容：2300002,2303501,2303504 | api/@ohos.net.socket.d.ts |
| 错误码变更 | 类名：TLSSocket； API声明：getRemoteCertificate(): Promise&lt;X509CertRawData&gt;; 差异内容：NA | 类名：TLSSocket； API声明：getRemoteCertificate(): Promise&lt;X509CertRawData&gt;; 差异内容：2300002,2303501 | api/@ohos.net.socket.d.ts |
| 错误码变更 | 类名：TLSSocket； API声明：getProtocol(): Promise&lt;string&gt;; 差异内容：NA | 类名：TLSSocket； API声明：getProtocol(): Promise&lt;string&gt;; 差异内容：2300002,2303501,2303505 | api/@ohos.net.socket.d.ts |
| 错误码变更 | 类名：TLSSocket； API声明：getCipherSuite(): Promise<Array&lt;string&gt;>; 差异内容：NA | 类名：TLSSocket； API声明：getCipherSuite(): Promise<Array&lt;string&gt;>; 差异内容：2300002,2303501,2303502,2303505 | api/@ohos.net.socket.d.ts |
| 错误码变更 | 类名：TLSSocket； API声明：getSignatureAlgorithms(): Promise<Array&lt;string&gt;>; 差异内容：NA | 类名：TLSSocket； API声明：getSignatureAlgorithms(): Promise<Array&lt;string&gt;>; 差异内容：2300002,2303501 | api/@ohos.net.socket.d.ts |
| 错误码变更 | 类名：TLSSocket； API声明：connect(options: TLSConnectOptions): Promise&lt;void&gt;; 差异内容：NA | 类名：TLSSocket； API声明：connect(options: TLSConnectOptions): Promise&lt;void&gt;; 差异内容：2300002,2303104,2303109,2303111,2303188,2303191,2303198,2303199,2303210,2303501,2303502,2303503,2303505,2303506,401 | api/@ohos.net.socket.d.ts |
| 错误码变更 | 类名：TLSSocket； API声明：send(data: string): Promise&lt;void&gt;; 差异内容：NA | 类名：TLSSocket； API声明：send(data: string \| ArrayBuffer): Promise&lt;void&gt;; 差异内容：2300002,2303501,2303503,2303505,2303506,401 | api/@ohos.net.socket.d.ts |
| 错误码变更 | 类名：TLSSocket； API声明：close(): Promise&lt;void&gt;; 差异内容：NA | 类名：TLSSocket； API声明：close(): Promise&lt;void&gt;; 差异内容：2300002,2303501,2303505,2303506,401 | api/@ohos.net.socket.d.ts |
| 错误码变更 | 类名：WebSocket； API声明：connect(url: string, options: WebSocketRequestOptions, callback: AsyncCallback&lt;boolean&gt;): void; 差异内容：NA | 类名：WebSocket； API声明：connect(url: string, options: WebSocketRequestOptions, callback: AsyncCallback&lt;boolean&gt;): void; 差异内容：201,401 | api/@ohos.net.webSocket.d.ts |
| 错误码变更 | 类名：WebSocket； API声明：connect(url: string, options?: WebSocketRequestOptions): Promise&lt;boolean&gt;; 差异内容：NA | 类名：WebSocket； API声明：connect(url: string, options?: WebSocketRequestOptions): Promise&lt;boolean&gt;; 差异内容：201,401 | api/@ohos.net.webSocket.d.ts |
| 错误码变更 | 类名：WebSocket； API声明：send(data: string \| ArrayBuffer): Promise&lt;boolean&gt;; 差异内容：NA | 类名：WebSocket； API声明：send(data: string \| ArrayBuffer): Promise&lt;boolean&gt;; 差异内容：201,401 | api/@ohos.net.webSocket.d.ts |
| 错误码变更 | 类名：WebSocket； API声明：close(options: WebSocketCloseOptions, callback: AsyncCallback&lt;boolean&gt;): void; 差异内容：NA | 类名：WebSocket； API声明：close(options: WebSocketCloseOptions, callback: AsyncCallback&lt;boolean&gt;): void; 差异内容：201,401 | api/@ohos.net.webSocket.d.ts |
| 错误码变更 | 类名：WebSocket； API声明：close(options?: WebSocketCloseOptions): Promise&lt;boolean&gt;; 差异内容：NA | 类名：WebSocket； API声明：close(options?: WebSocketCloseOptions): Promise&lt;boolean&gt;; 差异内容：201,401 | api/@ohos.net.webSocket.d.ts |
| 错误码变更 | 类名：connection； API声明：function getDefaultNet(callback: AsyncCallback&lt;NetHandle&gt;): void; 差异内容：201,2100002,2100003 | 类名：connection； API声明：function getDefaultNet(callback: AsyncCallback&lt;NetHandle&gt;): void; 差异内容：201,2100002,2100003,401 | api/@ohos.net.connection.d.ts |
| 错误码变更 | 类名：connection； API声明：function getAllNets(callback: AsyncCallback<Array&lt;NetHandle&gt;>): void; 差异内容：201,2100002,2100003 | 类名：connection； API声明：function getAllNets(callback: AsyncCallback<Array&lt;NetHandle&gt;>): void; 差异内容：201,2100002,2100003,401 | api/@ohos.net.connection.d.ts |
| 错误码变更 | 类名：connection； API声明：function isDefaultNetMetered(callback: AsyncCallback&lt;boolean&gt;): void; 差异内容：201,2100002,2100003 | 类名：connection； API声明：function isDefaultNetMetered(callback: AsyncCallback&lt;boolean&gt;): void; 差异内容：201,2100002,2100003,401 | api/@ohos.net.connection.d.ts |
| 错误码变更 | 类名：connection； API声明：function hasDefaultNet(callback: AsyncCallback&lt;boolean&gt;): void; 差异内容：201,2100002,2100003 | 类名：connection； API声明：function hasDefaultNet(callback: AsyncCallback&lt;boolean&gt;): void; 差异内容：201,2100002,2100003,401 | api/@ohos.net.connection.d.ts |
| 错误码变更 | 类名：connection； API声明：function getAppNet(callback: AsyncCallback&lt;NetHandle&gt;): void; 差异内容：2100002,2100003 | 类名：connection； API声明：function getAppNet(callback: AsyncCallback&lt;NetHandle&gt;): void; 差异内容：2100002,2100003,401 | api/@ohos.net.connection.d.ts |
| 错误码变更 | 类名：NetConnection； API声明：register(callback: AsyncCallback&lt;void&gt;): void; 差异内容：201,2100002,2100003,2101008,2101022 | 类名：NetConnection； API声明：register(callback: AsyncCallback&lt;void&gt;): void; 差异内容：201,2100002,2100003,2101008,2101022,401 | api/@ohos.net.connection.d.ts |
| 错误码变更 | 类名：NetConnection； API声明：unregister(callback: AsyncCallback&lt;void&gt;): void; 差异内容：2100002,2100003,2101007 | 类名：NetConnection； API声明：unregister(callback: AsyncCallback&lt;void&gt;): void; 差异内容：2100002,2100003,2101007,401 | api/@ohos.net.connection.d.ts |
| 权限变更 | 类名：connection； API声明：function getDefaultNet(): Promise&lt;NetHandle&gt;; 差异内容：NA | 类名：connection； API声明：function getDefaultNet(): Promise&lt;NetHandle&gt;; 差异内容：ohos.permission.GET_NETWORK_INFO | api/@ohos.net.connection.d.ts |
| 权限变更 | 类名：connection； API声明：function getAllNets(): Promise<Array&lt;NetHandle&gt;>; 差异内容：NA | 类名：connection； API声明：function getAllNets(): Promise<Array&lt;NetHandle&gt;>; 差异内容：ohos.permission.GET_NETWORK_INFO | api/@ohos.net.connection.d.ts |
| 权限变更 | 类名：connection； API声明：function getConnectionProperties(netHandle: NetHandle): Promise&lt;ConnectionProperties&gt;; 差异内容：NA | 类名：connection； API声明：function getConnectionProperties(netHandle: NetHandle): Promise&lt;ConnectionProperties&gt;; 差异内容：ohos.permission.GET_NETWORK_INFO | api/@ohos.net.connection.d.ts |
| 权限变更 | 类名：connection； API声明：function getNetCapabilities(netHandle: NetHandle): Promise&lt;NetCapabilities&gt;; 差异内容：NA | 类名：connection； API声明：function getNetCapabilities(netHandle: NetHandle): Promise&lt;NetCapabilities&gt;; 差异内容：ohos.permission.GET_NETWORK_INFO | api/@ohos.net.connection.d.ts |
| 权限变更 | 类名：connection； API声明：function isDefaultNetMetered(): Promise&lt;boolean&gt;; 差异内容：NA | 类名：connection； API声明：function isDefaultNetMetered(): Promise&lt;boolean&gt;; 差异内容：ohos.permission.GET_NETWORK_INFO | api/@ohos.net.connection.d.ts |
| 权限变更 | 类名：connection； API声明：function hasDefaultNet(): Promise&lt;boolean&gt;; 差异内容：NA | 类名：connection； API声明：function hasDefaultNet(): Promise&lt;boolean&gt;; 差异内容：ohos.permission.GET_NETWORK_INFO | api/@ohos.net.connection.d.ts |
| 权限变更 | 类名：connection； API声明：function reportNetConnected(netHandle: NetHandle): Promise&lt;void&gt;; 差异内容：NA | 类名：connection； API声明：function reportNetConnected(netHandle: NetHandle): Promise&lt;void&gt;; 差异内容：ohos.permission.GET_NETWORK_INFO and ohos.permission.INTERNET | api/@ohos.net.connection.d.ts |
| 权限变更 | 类名：connection； API声明：function reportNetDisconnected(netHandle: NetHandle): Promise&lt;void&gt;; 差异内容：NA | 类名：connection； API声明：function reportNetDisconnected(netHandle: NetHandle): Promise&lt;void&gt;; 差异内容：ohos.permission.GET_NETWORK_INFO and ohos.permission.INTERNET | api/@ohos.net.connection.d.ts |
| 权限变更 | 类名：connection； API声明：function getAddressesByName(host: string): Promise<Array&lt;NetAddress&gt;>; 差异内容：NA | 类名：connection； API声明：function getAddressesByName(host: string): Promise<Array&lt;NetAddress&gt;>; 差异内容：ohos.permission.INTERNET | api/@ohos.net.connection.d.ts |
| 权限变更 | 类名：NetHandle； API声明：getAddressesByName(host: string): Promise<Array&lt;NetAddress&gt;>; 差异内容：NA | 类名：NetHandle； API声明：getAddressesByName(host: string): Promise<Array&lt;NetAddress&gt;>; 差异内容：ohos.permission.INTERNET | api/@ohos.net.connection.d.ts |
| 权限变更 | 类名：NetHandle； API声明：getAddressByName(host: string): Promise&lt;NetAddress&gt;; 差异内容：NA | 类名：NetHandle； API声明：getAddressByName(host: string): Promise&lt;NetAddress&gt;; 差异内容：ohos.permission.INTERNET | api/@ohos.net.connection.d.ts |
| 权限变更 | 类名：HttpRequest； API声明：request(url: string, options: HttpRequestOptions, callback: AsyncCallback&lt;HttpResponse&gt;): void; 差异内容：NA | 类名：HttpRequest； API声明：request(url: string, options: HttpRequestOptions, callback: AsyncCallback&lt;HttpResponse&gt;): void; 差异内容：ohos.permission.INTERNET | api/@ohos.net.http.d.ts |
| 权限变更 | 类名：HttpRequest； API声明：request(url: string, options?: HttpRequestOptions): Promise&lt;HttpResponse&gt;; 差异内容：NA | 类名：HttpRequest； API声明：request(url: string, options?: HttpRequestOptions): Promise&lt;HttpResponse&gt;; 差异内容：ohos.permission.INTERNET | api/@ohos.net.http.d.ts |
| 权限变更 | 类名：UDPSocket； API声明：bind(address: NetAddress): Promise&lt;void&gt;; 差异内容：NA | 类名：UDPSocket； API声明：bind(address: NetAddress): Promise&lt;void&gt;; 差异内容：ohos.permission.INTERNET | api/@ohos.net.socket.d.ts |
| 权限变更 | 类名：UDPSocket； API声明：send(options: UDPSendOptions): Promise&lt;void&gt;; 差异内容：NA | 类名：UDPSocket； API声明：send(options: UDPSendOptions): Promise&lt;void&gt;; 差异内容：ohos.permission.INTERNET | api/@ohos.net.socket.d.ts |
| 权限变更 | 类名：UDPSocket； API声明：close(): Promise&lt;void&gt;; 差异内容：NA | 类名：UDPSocket； API声明：close(): Promise&lt;void&gt;; 差异内容：ohos.permission.INTERNET | api/@ohos.net.socket.d.ts |
| 权限变更 | 类名：UDPSocket； API声明：getState(): Promise&lt;SocketStateBase&gt;; 差异内容：NA | 类名：UDPSocket； API声明：getState(): Promise&lt;SocketStateBase&gt;; 差异内容：ohos.permission.INTERNET | api/@ohos.net.socket.d.ts |
| 权限变更 | 类名：UDPSocket； API声明：setExtraOptions(options: UDPExtraOptions): Promise&lt;void&gt;; 差异内容：NA | 类名：UDPSocket； API声明：setExtraOptions(options: UDPExtraOptions): Promise&lt;void&gt;; 差异内容：ohos.permission.INTERNET | api/@ohos.net.socket.d.ts |
| 权限变更 | 类名：TCPSocket； API声明：bind(address: NetAddress): Promise&lt;void&gt;; 差异内容：NA | 类名：TCPSocket； API声明：bind(address: NetAddress): Promise&lt;void&gt;; 差异内容：ohos.permission.INTERNET | api/@ohos.net.socket.d.ts |
| 权限变更 | 类名：TCPSocket； API声明：connect(options: TCPConnectOptions): Promise&lt;void&gt;; 差异内容：NA | 类名：TCPSocket； API声明：connect(options: TCPConnectOptions): Promise&lt;void&gt;; 差异内容：ohos.permission.INTERNET | api/@ohos.net.socket.d.ts |
| 权限变更 | 类名：TCPSocket； API声明：send(options: TCPSendOptions): Promise&lt;void&gt;; 差异内容：NA | 类名：TCPSocket； API声明：send(options: TCPSendOptions): Promise&lt;void&gt;; 差异内容：ohos.permission.INTERNET | api/@ohos.net.socket.d.ts |
| 权限变更 | 类名：TCPSocket； API声明：close(): Promise&lt;void&gt;; 差异内容：NA | 类名：TCPSocket； API声明：close(): Promise&lt;void&gt;; 差异内容：ohos.permission.INTERNET | api/@ohos.net.socket.d.ts |
| 权限变更 | 类名：TCPSocket； API声明：getRemoteAddress(): Promise&lt;NetAddress&gt;; 差异内容：NA | 类名：TCPSocket； API声明：getRemoteAddress(): Promise&lt;NetAddress&gt;; 差异内容：ohos.permission.INTERNET | api/@ohos.net.socket.d.ts |
| 权限变更 | 类名：TCPSocket； API声明：getState(): Promise&lt;SocketStateBase&gt;; 差异内容：NA | 类名：TCPSocket； API声明：getState(): Promise&lt;SocketStateBase&gt;; 差异内容：ohos.permission.INTERNET | api/@ohos.net.socket.d.ts |
| 权限变更 | 类名：TCPSocket； API声明：setExtraOptions(options: TCPExtraOptions): Promise&lt;void&gt;; 差异内容：NA | 类名：TCPSocket； API声明：setExtraOptions(options: TCPExtraOptions): Promise&lt;void&gt;; 差异内容：ohos.permission.INTERNET | api/@ohos.net.socket.d.ts |
| 权限变更 | 类名：TLSSocket； API声明：bind(address: NetAddress): Promise&lt;void&gt;; 差异内容：NA | 类名：TLSSocket； API声明：bind(address: NetAddress): Promise&lt;void&gt;; 差异内容：ohos.permission.INTERNET | api/@ohos.net.socket.d.ts |
| 权限变更 | 类名：WebSocket； API声明：connect(url: string, options: WebSocketRequestOptions, callback: AsyncCallback&lt;boolean&gt;): void; 差异内容：NA | 类名：WebSocket； API声明：connect(url: string, options: WebSocketRequestOptions, callback: AsyncCallback&lt;boolean&gt;): void; 差异内容：ohos.permission.INTERNET | api/@ohos.net.webSocket.d.ts |
| 权限变更 | 类名：WebSocket； API声明：connect(url: string, options?: WebSocketRequestOptions): Promise&lt;boolean&gt;; 差异内容：NA | 类名：WebSocket； API声明：connect(url: string, options?: WebSocketRequestOptions): Promise&lt;boolean&gt;; 差异内容：ohos.permission.INTERNET | api/@ohos.net.webSocket.d.ts |
| 权限变更 | 类名：WebSocket； API声明：send(data: string \| ArrayBuffer): Promise&lt;boolean&gt;; 差异内容：NA | 类名：WebSocket； API声明：send(data: string \| ArrayBuffer): Promise&lt;boolean&gt;; 差异内容：ohos.permission.INTERNET | api/@ohos.net.webSocket.d.ts |
| 权限变更 | 类名：WebSocket； API声明：close(options: WebSocketCloseOptions, callback: AsyncCallback&lt;boolean&gt;): void; 差异内容：NA | 类名：WebSocket； API声明：close(options: WebSocketCloseOptions, callback: AsyncCallback&lt;boolean&gt;): void; 差异内容：ohos.permission.INTERNET | api/@ohos.net.webSocket.d.ts |
| 权限变更 | 类名：WebSocket； API声明：close(options?: WebSocketCloseOptions): Promise&lt;boolean&gt;; 差异内容：NA | 类名：WebSocket； API声明：close(options?: WebSocketCloseOptions): Promise&lt;boolean&gt;; 差异内容：ohos.permission.INTERNET | api/@ohos.net.webSocket.d.ts |
| 函数变更 | 类名：NetConnection； API声明：on(type: 'netBlockStatusChange', callback: Callback<{ netHandle: NetHandle; blocked: boolean; }>): void; 差异内容：callback: Callback<{ netHandle: NetHandle; blocked: boolean; }> | 类名：NetConnection； API声明：on(type: 'netBlockStatusChange', callback: Callback&lt;NetBlockStatusInfo&gt;): void; 差异内容：callback: Callback&lt;NetBlockStatusInfo&gt; | api/@ohos.net.connection.d.ts |
| 函数变更 | 类名：NetConnection； API声明：on(type: 'netCapabilitiesChange', callback: Callback<{ netHandle: NetHandle; netCap: NetCapabilities; }>): void; 差异内容：callback: Callback<{ netHandle: NetHandle; netCap: NetCapabilities; }> | 类名：NetConnection； API声明：on(type: 'netCapabilitiesChange', callback: Callback&lt;NetCapabilityInfo&gt;): void; 差异内容：callback: Callback&lt;NetCapabilityInfo&gt; | api/@ohos.net.connection.d.ts |
| 函数变更 | 类名：NetConnection； API声明：on(type: 'netConnectionPropertiesChange', callback: Callback<{ netHandle: NetHandle; connectionProperties: ConnectionProperties; }>): void; 差异内容：callback: Callback<{ netHandle: NetHandle; connectionProperties: ConnectionProperties; }> | 类名：NetConnection； API声明：on(type: 'netConnectionPropertiesChange', callback: Callback&lt;NetConnectionPropertyInfo&gt;): void; 差异内容：callback: Callback&lt;NetConnectionPropertyInfo&gt; | api/@ohos.net.connection.d.ts |
| 函数变更 | 类名：UDPSocket； API声明：on(type: 'message', callback: Callback<{ message: ArrayBuffer; remoteInfo: SocketRemoteInfo; }>): void; 差异内容：callback: Callback<{ message: ArrayBuffer; remoteInfo: SocketRemoteInfo; }> | 类名：UDPSocket； API声明：on(type: 'message', callback: Callback&lt;SocketMessageInfo&gt;): void; 差异内容：callback: Callback&lt;SocketMessageInfo&gt; | api/@ohos.net.socket.d.ts |
| 函数变更 | 类名：UDPSocket； API声明：off(type: 'message', callback?: Callback<{ message: ArrayBuffer; remoteInfo: SocketRemoteInfo; }>): void; 差异内容：callback?: Callback<{ message: ArrayBuffer; remoteInfo: SocketRemoteInfo; }> | 类名：UDPSocket； API声明：off(type: 'message', callback?: Callback&lt;SocketMessageInfo&gt;): void; 差异内容：callback?: Callback&lt;SocketMessageInfo&gt; | api/@ohos.net.socket.d.ts |
| 函数变更 | 类名：TCPSocket； API声明：on(type: 'message', callback: Callback<{ message: ArrayBuffer; remoteInfo: SocketRemoteInfo; }>): void; 差异内容：callback: Callback<{ message: ArrayBuffer; remoteInfo: SocketRemoteInfo; }> | 类名：TCPSocket； API声明：on(type: 'message', callback: Callback&lt;SocketMessageInfo&gt;): void; 差异内容：callback: Callback&lt;SocketMessageInfo&gt; | api/@ohos.net.socket.d.ts |
| 函数变更 | 类名：TCPSocket； API声明：off(type: 'message', callback?: Callback<{ message: ArrayBuffer; remoteInfo: SocketRemoteInfo; }>): void; 差异内容：callback?: Callback<{ message: ArrayBuffer; remoteInfo: SocketRemoteInfo; }> | 类名：TCPSocket； API声明：off(type: 'message', callback?: Callback&lt;SocketMessageInfo&gt;): void; 差异内容：callback?: Callback&lt;SocketMessageInfo&gt; | api/@ohos.net.socket.d.ts |
| 函数变更 | 类名：TLSSocket； API声明：on(type: 'message', callback: Callback<{ message: ArrayBuffer; remoteInfo: SocketRemoteInfo; }>): void; 差异内容：callback: Callback<{ message: ArrayBuffer; remoteInfo: SocketRemoteInfo; }> | 类名：TLSSocket； API声明：on(type: 'message', callback: Callback&lt;SocketMessageInfo&gt;): void; 差异内容：callback: Callback&lt;SocketMessageInfo&gt; | api/@ohos.net.socket.d.ts |
| 函数变更 | 类名：TLSSocket； API声明：off(type: 'message', callback?: Callback<{ message: ArrayBuffer; remoteInfo: SocketRemoteInfo; }>): void; 差异内容：callback?: Callback<{ message: ArrayBuffer; remoteInfo: SocketRemoteInfo; }> | 类名：TLSSocket； API声明：off(type: 'message', callback?: Callback&lt;SocketMessageInfo&gt;): void; 差异内容：callback?: Callback&lt;SocketMessageInfo&gt; | api/@ohos.net.socket.d.ts |
| 函数变更 | 类名：WebSocket； API声明：on(type: 'close', callback: AsyncCallback<{ code: number; reason: string; }>): void; 差异内容：callback: AsyncCallback<{ code: number; reason: string; }> | 类名：WebSocket； API声明：on(type: 'close', callback: AsyncCallback&lt;CloseResult&gt;): void; 差异内容：callback: AsyncCallback&lt;CloseResult&gt; | api/@ohos.net.webSocket.d.ts |
| 函数变更 | 类名：WebSocket； API声明：off(type: 'close', callback?: AsyncCallback<{ code: number; reason: string; }>): void; 差异内容：callback?: AsyncCallback<{ code: number; reason: string; }> | 类名：WebSocket； API声明：off(type: 'close', callback?: AsyncCallback&lt;CloseResult&gt;): void; 差异内容：callback?: AsyncCallback&lt;CloseResult&gt; | api/@ohos.net.webSocket.d.ts |
| 函数变更 | 类名：TLSSocket； API声明：send(data: string, callback: AsyncCallback&lt;void&gt;): void; 差异内容：data: string | 类名：TLSSocket； API声明：send(data: string \| ArrayBuffer, callback: AsyncCallback&lt;void&gt;): void; 差异内容：data: string \| ArrayBuffer | api/@ohos.net.socket.d.ts |
| 函数变更 | 类名：TLSSocket； API声明：send(data: string): Promise&lt;void&gt;; 差异内容：data: string | 类名：TLSSocket； API声明：send(data: string \| ArrayBuffer): Promise&lt;void&gt;; 差异内容：data: string \| ArrayBuffer | api/@ohos.net.socket.d.ts |
| 属性变更 | 类名：TLSSecureOptions； API声明：ca: string \| Array&lt;string&gt;; 差异内容：ca: string \| Array&lt;string&gt;; | 类名：TLSSecureOptions； API声明：ca?: string \| Array&lt;string&gt;; 差异内容：ca?: string \| Array&lt;string&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：connection； API声明：function getAllNetsSync(): Array&lt;NetHandle&gt;; 差异内容：function getAllNetsSync(): Array&lt;NetHandle&gt;; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection； API声明：function getConnectionPropertiesSync(netHandle: NetHandle): ConnectionProperties; 差异内容：function getConnectionPropertiesSync(netHandle: NetHandle): ConnectionProperties; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection； API声明：function getNetCapabilitiesSync(netHandle: NetHandle): NetCapabilities; 差异内容：function getNetCapabilitiesSync(netHandle: NetHandle): NetCapabilities; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection； API声明：function isDefaultNetMeteredSync(): boolean; 差异内容：function isDefaultNetMeteredSync(): boolean; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection； API声明：function hasDefaultNetSync(): boolean; 差异内容：function hasDefaultNetSync(): boolean; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection； API声明：function getAppNetSync(): NetHandle; 差异内容：function getAppNetSync(): NetHandle; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection； API声明：function getDefaultHttpProxy(callback: AsyncCallback&lt;HttpProxy&gt;): void; 差异内容：function getDefaultHttpProxy(callback: AsyncCallback&lt;HttpProxy&gt;): void; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection； API声明：function getDefaultHttpProxy(): Promise&lt;HttpProxy&gt;; 差异内容：function getDefaultHttpProxy(): Promise&lt;HttpProxy&gt;; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection； API声明：function setAppHttpProxy(httpProxy: HttpProxy): void; 差异内容：function setAppHttpProxy(httpProxy: HttpProxy): void; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection； API声明：function addCustomDnsRule(host: string, ip: Array&lt;string&gt;, callback: AsyncCallback&lt;void&gt;): void; 差异内容：function addCustomDnsRule(host: string, ip: Array&lt;string&gt;, callback: AsyncCallback&lt;void&gt;): void; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection； API声明：function addCustomDnsRule(host: string, ip: Array&lt;string&gt;): Promise&lt;void&gt;; 差异内容：function addCustomDnsRule(host: string, ip: Array&lt;string&gt;): Promise&lt;void&gt;; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection； API声明：function removeCustomDnsRule(host: string, callback: AsyncCallback&lt;void&gt;): void; 差异内容：function removeCustomDnsRule(host: string, callback: AsyncCallback&lt;void&gt;): void; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection； API声明：function removeCustomDnsRule(host: string): Promise&lt;void&gt;; 差异内容：function removeCustomDnsRule(host: string): Promise&lt;void&gt;; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection； API声明：function clearCustomDnsRules(callback: AsyncCallback&lt;void&gt;): void; 差异内容：function clearCustomDnsRules(callback: AsyncCallback&lt;void&gt;): void; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection； API声明：function clearCustomDnsRules(): Promise&lt;void&gt;; 差异内容：function clearCustomDnsRules(): Promise&lt;void&gt;; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection； API声明： export interface NetCapabilityInfo 差异内容： export interface NetCapabilityInfo | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：NetCapabilityInfo； API声明：netHandle: NetHandle; 差异内容：netHandle: NetHandle; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：NetCapabilityInfo； API声明：netCap: NetCapabilities; 差异内容：netCap: NetCapabilities; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection； API声明： export interface NetConnectionPropertyInfo 差异内容： export interface NetConnectionPropertyInfo | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：NetConnectionPropertyInfo； API声明：netHandle: NetHandle; 差异内容：netHandle: NetHandle; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：NetConnectionPropertyInfo； API声明：connectionProperties: ConnectionProperties; 差异内容：connectionProperties: ConnectionProperties; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection； API声明： export interface NetBlockStatusInfo 差异内容： export interface NetBlockStatusInfo | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：NetBlockStatusInfo； API声明：netHandle: NetHandle; 差异内容：netHandle: NetHandle; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：NetBlockStatusInfo； API声明：blocked: boolean; 差异内容：blocked: boolean; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：NetCap； API声明：NET_CAPABILITY_PORTAL = 17 差异内容：NET_CAPABILITY_PORTAL = 17 | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：NetBearType； API声明：BEARER_VPN = 4 差异内容：BEARER_VPN = 4 | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：connection； API声明： export interface HttpProxy 差异内容： export interface HttpProxy | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：HttpProxy； API声明：host: string; 差异内容：host: string; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：HttpProxy； API声明：port: number; 差异内容：port: number; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：HttpProxy； API声明：username?: string; 差异内容：username?: string; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：HttpProxy； API声明：password?: string; 差异内容：password?: string; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：HttpProxy； API声明：exclusionList: Array&lt;string&gt;; 差异内容：exclusionList: Array&lt;string&gt;; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：ethernet； API声明：type HttpProxy = connection.HttpProxy; 差异内容：type HttpProxy = connection.HttpProxy; | api/@ohos.net.ethernet.d.ts |
| 新增API | NA | 类名：http； API声明：type HttpProxy = connection.HttpProxy; 差异内容：type HttpProxy = connection.HttpProxy; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpRequestOptions； API声明：usingProxy?: boolean \| HttpProxy; 差异内容：usingProxy?: boolean \| HttpProxy; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpRequestOptions； API声明：caPath?: string; 差异内容：caPath?: string; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpRequestOptions； API声明：resumeFrom?: number; 差异内容：resumeFrom?: number; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpRequestOptions； API声明：resumeTo?: number; 差异内容：resumeTo?: number; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpRequestOptions； API声明：clientCert?: ClientCert; 差异内容：clientCert?: ClientCert; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpRequestOptions； API声明：dnsOverHttps?: string; 差异内容：dnsOverHttps?: string; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpRequestOptions； API声明：dnsServers?: Array&lt;string&gt;; 差异内容：dnsServers?: Array&lt;string&gt;; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpRequestOptions； API声明：maxLimit?: number; 差异内容：maxLimit?: number; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpRequestOptions； API声明：multiFormDataList?: Array&lt;MultiFormData&gt;; 差异内容：multiFormDataList?: Array&lt;MultiFormData&gt;; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：http； API声明： export interface MultiFormData 差异内容： export interface MultiFormData | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：MultiFormData； API声明：name: string; 差异内容：name: string; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：MultiFormData； API声明：contentType: string; 差异内容：contentType: string; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：MultiFormData； API声明：remoteFileName?: string; 差异内容：remoteFileName?: string; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：MultiFormData； API声明：data?: string \| Object \| ArrayBuffer; 差异内容：data?: string \| Object \| ArrayBuffer; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：MultiFormData； API声明：filePath?: string; 差异内容：filePath?: string; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：http； API声明： export enum CertType 差异内容： export enum CertType | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：CertType； API声明：PEM = 'PEM' 差异内容：PEM = 'PEM' | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：CertType； API声明：DER = 'DER' 差异内容：DER = 'DER' | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：CertType； API声明：P12 = 'P12' 差异内容：P12 = 'P12' | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：http； API声明： export interface ClientCert 差异内容： export interface ClientCert | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：ClientCert； API声明：certPath: string; 差异内容：certPath: string; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：ClientCert； API声明：certType?: CertType; 差异内容：certType?: CertType; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：ClientCert； API声明：keyPath: string; 差异内容：keyPath: string; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：ClientCert； API声明：keyPassword?: string; 差异内容：keyPassword?: string; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpRequest； API声明：requestInStream(url: string, callback: AsyncCallback&lt;number&gt;): void; 差异内容：requestInStream(url: string, callback: AsyncCallback&lt;number&gt;): void; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpRequest； API声明：requestInStream(url: string, options: HttpRequestOptions, callback: AsyncCallback&lt;number&gt;): void; 差异内容：requestInStream(url: string, options: HttpRequestOptions, callback: AsyncCallback&lt;number&gt;): void; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpRequest； API声明：requestInStream(url: string, options?: HttpRequestOptions): Promise&lt;number&gt;; 差异内容：requestInStream(url: string, options?: HttpRequestOptions): Promise&lt;number&gt;; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpRequest； API声明：on(type: "dataReceive", callback: Callback&lt;ArrayBuffer&gt;): void; 差异内容：on(type: "dataReceive", callback: Callback&lt;ArrayBuffer&gt;): void; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpRequest； API声明：off(type: "dataReceive", callback?: Callback&lt;ArrayBuffer&gt;): void; 差异内容：off(type: "dataReceive", callback?: Callback&lt;ArrayBuffer&gt;): void; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpRequest； API声明：on(type: "dataEnd", callback: Callback&lt;void&gt;): void; 差异内容：on(type: "dataEnd", callback: Callback&lt;void&gt;): void; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpRequest； API声明：off(type: "dataEnd", callback?: Callback&lt;void&gt;): void; 差异内容：off(type: "dataEnd", callback?: Callback&lt;void&gt;): void; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpRequest； API声明：on(type: 'dataReceiveProgress', callback: Callback&lt;DataReceiveProgressInfo&gt;): void; 差异内容：on(type: 'dataReceiveProgress', callback: Callback&lt;DataReceiveProgressInfo&gt;): void; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpRequest； API声明：off(type: 'dataReceiveProgress', callback?: Callback&lt;DataReceiveProgressInfo&gt;): void; 差异内容：off(type: 'dataReceiveProgress', callback?: Callback&lt;DataReceiveProgressInfo&gt;): void; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpRequest； API声明：on(type: 'dataSendProgress', callback: Callback&lt;DataSendProgressInfo&gt;): void; 差异内容：on(type: 'dataSendProgress', callback: Callback&lt;DataSendProgressInfo&gt;): void; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpRequest； API声明：off(type: 'dataSendProgress', callback?: Callback&lt;DataSendProgressInfo&gt;): void; 差异内容：off(type: 'dataSendProgress', callback?: Callback&lt;DataSendProgressInfo&gt;): void; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：ResponseCode； API声明：RANGE_NOT_SATISFIABLE 差异内容：RANGE_NOT_SATISFIABLE | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpProtocol； API声明：HTTP3 差异内容：HTTP3 | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：HttpResponse； API声明：performanceTiming: PerformanceTiming; 差异内容：performanceTiming: PerformanceTiming; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：http； API声明： export interface PerformanceTiming 差异内容： export interface PerformanceTiming | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：PerformanceTiming； API声明：dnsTiming: number; 差异内容：dnsTiming: number; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：PerformanceTiming； API声明：tcpTiming: number; 差异内容：tcpTiming: number; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：PerformanceTiming； API声明：tlsTiming: number; 差异内容：tlsTiming: number; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：PerformanceTiming； API声明：firstSendTiming: number; 差异内容：firstSendTiming: number; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：PerformanceTiming； API声明：firstReceiveTiming: number; 差异内容：firstReceiveTiming: number; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：PerformanceTiming； API声明：totalFinishTiming: number; 差异内容：totalFinishTiming: number; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：PerformanceTiming； API声明：redirectTiming: number; 差异内容：redirectTiming: number; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：PerformanceTiming； API声明：responseHeaderTiming: number; 差异内容：responseHeaderTiming: number; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：PerformanceTiming； API声明：responseBodyTiming: number; 差异内容：responseBodyTiming: number; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：PerformanceTiming； API声明：totalTiming: number; 差异内容：totalTiming: number; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：http； API声明： export interface DataReceiveProgressInfo 差异内容： export interface DataReceiveProgressInfo | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：DataReceiveProgressInfo； API声明：receiveSize: number; 差异内容：receiveSize: number; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：DataReceiveProgressInfo； API声明：totalSize: number; 差异内容：totalSize: number; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：http； API声明： export interface DataSendProgressInfo 差异内容： export interface DataSendProgressInfo | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：DataSendProgressInfo； API声明：sendSize: number; 差异内容：sendSize: number; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：DataSendProgressInfo； API声明：totalSize: number; 差异内容：totalSize: number; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：socket； API声明：function constructMulticastSocketInstance(): MulticastSocket; 差异内容：function constructMulticastSocketInstance(): MulticastSocket; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：socket； API声明：function constructTCPSocketServerInstance(): TCPSocketServer; 差异内容：function constructTCPSocketServerInstance(): TCPSocketServer; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：socket； API声明：function constructTLSSocketServerInstance(): TLSSocketServer; 差异内容：function constructTLSSocketServerInstance(): TLSSocketServer; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：socket； API声明：function constructLocalSocketInstance(): LocalSocket; 差异内容：function constructLocalSocketInstance(): LocalSocket; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：socket； API声明：function constructLocalSocketServerInstance(): LocalSocketServer; 差异内容：function constructLocalSocketServerInstance(): LocalSocketServer; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：socket； API声明： export interface LocalSocketMessageInfo 差异内容： export interface LocalSocketMessageInfo | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocketMessageInfo； API声明：message: ArrayBuffer; 差异内容：message: ArrayBuffer; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocketMessageInfo； API声明：address: string; 差异内容：address: string; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocketMessageInfo； API声明：size: number; 差异内容：size: number; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：socket； API声明： export interface LocalAddress 差异内容： export interface LocalAddress | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalAddress； API声明：address: string; 差异内容：address: string; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：socket； API声明： export interface LocalConnectOptions 差异内容： export interface LocalConnectOptions | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalConnectOptions； API声明：address: LocalAddress; 差异内容：address: LocalAddress; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalConnectOptions； API声明：timeout?: number; 差异内容：timeout?: number; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：socket； API声明： export interface LocalSendOptions 差异内容： export interface LocalSendOptions | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSendOptions； API声明：data: string \| ArrayBuffer; 差异内容：data: string \| ArrayBuffer; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSendOptions； API声明：encoding?: string; 差异内容：encoding?: string; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：socket； API声明： export interface MulticastSocket 差异内容： export interface MulticastSocket | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：MulticastSocket； API声明：addMembership(multicastAddress: NetAddress, callback: AsyncCallback&lt;void&gt;): void; 差异内容：addMembership(multicastAddress: NetAddress, callback: AsyncCallback&lt;void&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：MulticastSocket； API声明：addMembership(multicastAddress: NetAddress): Promise&lt;void&gt;; 差异内容：addMembership(multicastAddress: NetAddress): Promise&lt;void&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：MulticastSocket； API声明：dropMembership(multicastAddress: NetAddress, callback: AsyncCallback&lt;void&gt;): void; 差异内容：dropMembership(multicastAddress: NetAddress, callback: AsyncCallback&lt;void&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：MulticastSocket； API声明：dropMembership(multicastAddress: NetAddress): Promise&lt;void&gt;; 差异内容：dropMembership(multicastAddress: NetAddress): Promise&lt;void&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：MulticastSocket； API声明：setMulticastTTL(ttl: number, callback: AsyncCallback&lt;void&gt;): void; 差异内容：setMulticastTTL(ttl: number, callback: AsyncCallback&lt;void&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：MulticastSocket； API声明：setMulticastTTL(ttl: number): Promise&lt;void&gt;; 差异内容：setMulticastTTL(ttl: number): Promise&lt;void&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：MulticastSocket； API声明：getMulticastTTL(callback: AsyncCallback&lt;number&gt;): void; 差异内容：getMulticastTTL(callback: AsyncCallback&lt;number&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：MulticastSocket； API声明：getMulticastTTL(): Promise&lt;number&gt;; 差异内容：getMulticastTTL(): Promise&lt;number&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：MulticastSocket； API声明：setLoopbackMode(flag: boolean, callback: AsyncCallback&lt;void&gt;): void; 差异内容：setLoopbackMode(flag: boolean, callback: AsyncCallback&lt;void&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：MulticastSocket； API声明：setLoopbackMode(flag: boolean): Promise&lt;void&gt;; 差异内容：setLoopbackMode(flag: boolean): Promise&lt;void&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：MulticastSocket； API声明：getLoopbackMode(callback: AsyncCallback&lt;boolean&gt;): void; 差异内容：getLoopbackMode(callback: AsyncCallback&lt;boolean&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：MulticastSocket； API声明：getLoopbackMode(): Promise&lt;boolean&gt;; 差异内容：getLoopbackMode(): Promise&lt;boolean&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：socket； API声明： export interface LocalSocket 差异内容： export interface LocalSocket | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocket； API声明：bind(address: LocalAddress): Promise&lt;void&gt;; 差异内容：bind(address: LocalAddress): Promise&lt;void&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocket； API声明：connect(options: LocalConnectOptions): Promise&lt;void&gt;; 差异内容：connect(options: LocalConnectOptions): Promise&lt;void&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocket； API声明：send(options: LocalSendOptions): Promise&lt;void&gt;; 差异内容：send(options: LocalSendOptions): Promise&lt;void&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocket； API声明：close(): Promise&lt;void&gt;; 差异内容：close(): Promise&lt;void&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocket； API声明：getState(): Promise&lt;SocketStateBase&gt;; 差异内容：getState(): Promise&lt;SocketStateBase&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocket； API声明：getSocketFd(): Promise&lt;number&gt;; 差异内容：getSocketFd(): Promise&lt;number&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocket； API声明：setExtraOptions(options: ExtraOptionsBase): Promise&lt;void&gt;; 差异内容：setExtraOptions(options: ExtraOptionsBase): Promise&lt;void&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocket； API声明：getExtraOptions(): Promise&lt;ExtraOptionsBase&gt;; 差异内容：getExtraOptions(): Promise&lt;ExtraOptionsBase&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocket； API声明：on(type: 'message', callback: Callback&lt;LocalSocketMessageInfo&gt;): void; 差异内容：on(type: 'message', callback: Callback&lt;LocalSocketMessageInfo&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocket； API声明：off(type: 'message', callback?: Callback&lt;LocalSocketMessageInfo&gt;): void; 差异内容：off(type: 'message', callback?: Callback&lt;LocalSocketMessageInfo&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocket； API声明：on(type: 'connect', callback: Callback&lt;void&gt;): void; 差异内容：on(type: 'connect', callback: Callback&lt;void&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocket； API声明：off(type: 'connect', callback?: Callback&lt;void&gt;): void; 差异内容：off(type: 'connect', callback?: Callback&lt;void&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocket； API声明：on(type: 'close', callback: Callback&lt;void&gt;): void; 差异内容：on(type: 'close', callback: Callback&lt;void&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocket； API声明：off(type: 'close', callback?: Callback&lt;void&gt;): void; 差异内容：off(type: 'close', callback?: Callback&lt;void&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocket； API声明：on(type: 'error', callback: ErrorCallback): void; 差异内容：on(type: 'error', callback: ErrorCallback): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocket； API声明：off(type: 'error', callback?: ErrorCallback): void; 差异内容：off(type: 'error', callback?: ErrorCallback): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：socket； API声明： export interface LocalSocketConnection 差异内容： export interface LocalSocketConnection | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocketConnection； API声明：clientId: number; 差异内容：clientId: number; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocketConnection； API声明：send(options: LocalSendOptions): Promise&lt;void&gt;; 差异内容：send(options: LocalSendOptions): Promise&lt;void&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocketConnection； API声明：close(): Promise&lt;void&gt;; 差异内容：close(): Promise&lt;void&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocketConnection； API声明：on(type: 'message', callback: Callback&lt;LocalSocketMessageInfo&gt;): void; 差异内容：on(type: 'message', callback: Callback&lt;LocalSocketMessageInfo&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocketConnection； API声明：off(type: 'message', callback?: Callback&lt;LocalSocketMessageInfo&gt;): void; 差异内容：off(type: 'message', callback?: Callback&lt;LocalSocketMessageInfo&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocketConnection； API声明：on(type: 'close', callback: Callback&lt;void&gt;): void; 差异内容：on(type: 'close', callback: Callback&lt;void&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocketConnection； API声明：off(type: 'close', callback?: Callback&lt;void&gt;): void; 差异内容：off(type: 'close', callback?: Callback&lt;void&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocketConnection； API声明：on(type: 'error', callback: ErrorCallback): void; 差异内容：on(type: 'error', callback: ErrorCallback): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocketConnection； API声明：off(type: 'error', callback?: ErrorCallback): void; 差异内容：off(type: 'error', callback?: ErrorCallback): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：socket； API声明： export interface LocalSocketServer 差异内容： export interface LocalSocketServer | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocketServer； API声明：listen(address: LocalAddress): Promise&lt;void&gt;; 差异内容：listen(address: LocalAddress): Promise&lt;void&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocketServer； API声明：getState(): Promise&lt;SocketStateBase&gt;; 差异内容：getState(): Promise&lt;SocketStateBase&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocketServer； API声明：setExtraOptions(options: ExtraOptionsBase): Promise&lt;void&gt;; 差异内容：setExtraOptions(options: ExtraOptionsBase): Promise&lt;void&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocketServer； API声明：getExtraOptions(): Promise&lt;ExtraOptionsBase&gt;; 差异内容：getExtraOptions(): Promise&lt;ExtraOptionsBase&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocketServer； API声明：on(type: 'connect', callback: Callback&lt;LocalSocketConnection&gt;): void; 差异内容：on(type: 'connect', callback: Callback&lt;LocalSocketConnection&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocketServer； API声明：off(type: 'connect', callback?: Callback&lt;LocalSocketConnection&gt;): void; 差异内容：off(type: 'connect', callback?: Callback&lt;LocalSocketConnection&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocketServer； API声明：on(type: 'error', callback: ErrorCallback): void; 差异内容：on(type: 'error', callback: ErrorCallback): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：LocalSocketServer； API声明：off(type: 'error', callback?: ErrorCallback): void; 差异内容：off(type: 'error', callback?: ErrorCallback): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TCPSocket； API声明：getSocketFd(callback: AsyncCallback&lt;number&gt;): void; 差异内容：getSocketFd(callback: AsyncCallback&lt;number&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TCPSocket； API声明：getSocketFd(): Promise&lt;number&gt;; 差异内容：getSocketFd(): Promise&lt;number&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：socket； API声明： export interface TCPSocketConnection 差异内容： export interface TCPSocketConnection | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TCPSocketConnection； API声明：clientId: number; 差异内容：clientId: number; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TCPSocketConnection； API声明：send(options: TCPSendOptions, callback: AsyncCallback&lt;void&gt;): void; 差异内容：send(options: TCPSendOptions, callback: AsyncCallback&lt;void&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TCPSocketConnection； API声明：send(options: TCPSendOptions): Promise&lt;void&gt;; 差异内容：send(options: TCPSendOptions): Promise&lt;void&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TCPSocketConnection； API声明：close(callback: AsyncCallback&lt;void&gt;): void; 差异内容：close(callback: AsyncCallback&lt;void&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TCPSocketConnection； API声明：close(): Promise&lt;void&gt;; 差异内容：close(): Promise&lt;void&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TCPSocketConnection； API声明：getRemoteAddress(callback: AsyncCallback&lt;NetAddress&gt;): void; 差异内容：getRemoteAddress(callback: AsyncCallback&lt;NetAddress&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TCPSocketConnection； API声明：getRemoteAddress(): Promise&lt;NetAddress&gt;; 差异内容：getRemoteAddress(): Promise&lt;NetAddress&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TCPSocketConnection； API声明：on(type: 'message', callback: Callback&lt;SocketMessageInfo&gt;): void; 差异内容：on(type: 'message', callback: Callback&lt;SocketMessageInfo&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TCPSocketConnection； API声明：off(type: 'message', callback?: Callback&lt;SocketMessageInfo&gt;): void; 差异内容：off(type: 'message', callback?: Callback&lt;SocketMessageInfo&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TCPSocketConnection； API声明：on(type: 'close', callback: Callback&lt;void&gt;): void; 差异内容：on(type: 'close', callback: Callback&lt;void&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TCPSocketConnection； API声明：off(type: 'close', callback?: Callback&lt;void&gt;): void; 差异内容：off(type: 'close', callback?: Callback&lt;void&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TCPSocketConnection； API声明：on(type: 'error', callback: ErrorCallback): void; 差异内容：on(type: 'error', callback: ErrorCallback): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TCPSocketConnection； API声明：off(type: 'error', callback?: ErrorCallback): void; 差异内容：off(type: 'error', callback?: ErrorCallback): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：socket； API声明： export interface TCPSocketServer 差异内容： export interface TCPSocketServer | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TCPSocketServer； API声明：listen(address: NetAddress, callback: AsyncCallback&lt;void&gt;): void; 差异内容：listen(address: NetAddress, callback: AsyncCallback&lt;void&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TCPSocketServer； API声明：listen(address: NetAddress): Promise&lt;void&gt;; 差异内容：listen(address: NetAddress): Promise&lt;void&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TCPSocketServer； API声明：getState(callback: AsyncCallback&lt;SocketStateBase&gt;): void; 差异内容：getState(callback: AsyncCallback&lt;SocketStateBase&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TCPSocketServer； API声明：getState(): Promise&lt;SocketStateBase&gt;; 差异内容：getState(): Promise&lt;SocketStateBase&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TCPSocketServer； API声明：setExtraOptions(options: TCPExtraOptions, callback: AsyncCallback&lt;void&gt;): void; 差异内容：setExtraOptions(options: TCPExtraOptions, callback: AsyncCallback&lt;void&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TCPSocketServer； API声明：setExtraOptions(options: TCPExtraOptions): Promise&lt;void&gt;; 差异内容：setExtraOptions(options: TCPExtraOptions): Promise&lt;void&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TCPSocketServer； API声明：on(type: 'connect', callback: Callback&lt;TCPSocketConnection&gt;): void; 差异内容：on(type: 'connect', callback: Callback&lt;TCPSocketConnection&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TCPSocketServer； API声明：off(type: 'connect', callback?: Callback&lt;TCPSocketConnection&gt;): void; 差异内容：off(type: 'connect', callback?: Callback&lt;TCPSocketConnection&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TCPSocketServer； API声明：on(type: 'error', callback: ErrorCallback): void; 差异内容：on(type: 'error', callback: ErrorCallback): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TCPSocketServer； API声明：off(type: 'error', callback?: ErrorCallback): void; 差异内容：off(type: 'error', callback?: ErrorCallback): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：socket； API声明： export interface TLSSocketConnection 差异内容： export interface TLSSocketConnection | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketConnection； API声明：clientId: number; 差异内容：clientId: number; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketConnection； API声明：send(data: string \| ArrayBuffer, callback: AsyncCallback&lt;void&gt;): void; 差异内容：send(data: string \| ArrayBuffer, callback: AsyncCallback&lt;void&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketConnection； API声明：send(data: string \| ArrayBuffer): Promise&lt;void&gt;; 差异内容：send(data: string \| ArrayBuffer): Promise&lt;void&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketConnection； API声明：close(callback: AsyncCallback&lt;void&gt;): void; 差异内容：close(callback: AsyncCallback&lt;void&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketConnection； API声明：close(): Promise&lt;void&gt;; 差异内容：close(): Promise&lt;void&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketConnection； API声明：getRemoteAddress(callback: AsyncCallback&lt;NetAddress&gt;): void; 差异内容：getRemoteAddress(callback: AsyncCallback&lt;NetAddress&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketConnection； API声明：getRemoteAddress(): Promise&lt;NetAddress&gt;; 差异内容：getRemoteAddress(): Promise&lt;NetAddress&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketConnection； API声明：getRemoteCertificate(callback: AsyncCallback&lt;X509CertRawData&gt;): void; 差异内容：getRemoteCertificate(callback: AsyncCallback&lt;X509CertRawData&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketConnection； API声明：getRemoteCertificate(): Promise&lt;X509CertRawData&gt;; 差异内容：getRemoteCertificate(): Promise&lt;X509CertRawData&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketConnection； API声明：getCipherSuite(callback: AsyncCallback<Array&lt;string&gt;>): void; 差异内容：getCipherSuite(callback: AsyncCallback<Array&lt;string&gt;>): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketConnection； API声明：getCipherSuite(): Promise<Array&lt;string&gt;>; 差异内容：getCipherSuite(): Promise<Array&lt;string&gt;>; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketConnection； API声明：getSignatureAlgorithms(callback: AsyncCallback<Array&lt;string&gt;>): void; 差异内容：getSignatureAlgorithms(callback: AsyncCallback<Array&lt;string&gt;>): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketConnection； API声明：getSignatureAlgorithms(): Promise<Array&lt;string&gt;>; 差异内容：getSignatureAlgorithms(): Promise<Array&lt;string&gt;>; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketConnection； API声明：on(type: 'message', callback: Callback&lt;SocketMessageInfo&gt;): void; 差异内容：on(type: 'message', callback: Callback&lt;SocketMessageInfo&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketConnection； API声明：off(type: 'message', callback?: Callback&lt;SocketMessageInfo&gt;): void; 差异内容：off(type: 'message', callback?: Callback&lt;SocketMessageInfo&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketConnection； API声明：on(type: 'close', callback: Callback&lt;void&gt;): void; 差异内容：on(type: 'close', callback: Callback&lt;void&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketConnection； API声明：off(type: 'close', callback?: Callback&lt;void&gt;): void; 差异内容：off(type: 'close', callback?: Callback&lt;void&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketConnection； API声明：on(type: 'error', callback: ErrorCallback): void; 差异内容：on(type: 'error', callback: ErrorCallback): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketConnection； API声明：off(type: 'error', callback?: ErrorCallback): void; 差异内容：off(type: 'error', callback?: ErrorCallback): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：socket； API声明： export interface SocketMessageInfo 差异内容： export interface SocketMessageInfo | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：SocketMessageInfo； API声明：message: ArrayBuffer; 差异内容：message: ArrayBuffer; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：SocketMessageInfo； API声明：remoteInfo: SocketRemoteInfo; 差异内容：remoteInfo: SocketRemoteInfo; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：socket； API声明： export interface TLSSocketServer 差异内容： export interface TLSSocketServer | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketServer； API声明：listen(options: TLSConnectOptions, callback: AsyncCallback&lt;void&gt;): void; 差异内容：listen(options: TLSConnectOptions, callback: AsyncCallback&lt;void&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketServer； API声明：listen(options: TLSConnectOptions): Promise&lt;void&gt;; 差异内容：listen(options: TLSConnectOptions): Promise&lt;void&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketServer； API声明：getState(callback: AsyncCallback&lt;SocketStateBase&gt;): void; 差异内容：getState(callback: AsyncCallback&lt;SocketStateBase&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketServer； API声明：getState(): Promise&lt;SocketStateBase&gt;; 差异内容：getState(): Promise&lt;SocketStateBase&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketServer； API声明：setExtraOptions(options: TCPExtraOptions, callback: AsyncCallback&lt;void&gt;): void; 差异内容：setExtraOptions(options: TCPExtraOptions, callback: AsyncCallback&lt;void&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketServer； API声明：setExtraOptions(options: TCPExtraOptions): Promise&lt;void&gt;; 差异内容：setExtraOptions(options: TCPExtraOptions): Promise&lt;void&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketServer； API声明：getCertificate(callback: AsyncCallback&lt;X509CertRawData&gt;): void; 差异内容：getCertificate(callback: AsyncCallback&lt;X509CertRawData&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketServer； API声明：getCertificate(): Promise&lt;X509CertRawData&gt;; 差异内容：getCertificate(): Promise&lt;X509CertRawData&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketServer； API声明：getProtocol(callback: AsyncCallback&lt;string&gt;): void; 差异内容：getProtocol(callback: AsyncCallback&lt;string&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketServer； API声明：getProtocol(): Promise&lt;string&gt;; 差异内容：getProtocol(): Promise&lt;string&gt;; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketServer； API声明：on(type: 'connect', callback: Callback&lt;TLSSocketConnection&gt;): void; 差异内容：on(type: 'connect', callback: Callback&lt;TLSSocketConnection&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketServer； API声明：off(type: 'connect', callback?: Callback&lt;TLSSocketConnection&gt;): void; 差异内容：off(type: 'connect', callback?: Callback&lt;TLSSocketConnection&gt;): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketServer； API声明：on(type: 'error', callback: ErrorCallback): void; 差异内容：on(type: 'error', callback: ErrorCallback): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSSocketServer； API声明：off(type: 'error', callback?: ErrorCallback): void; 差异内容：off(type: 'error', callback?: ErrorCallback): void; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：webSocket； API声明：type HttpProxy = connection.HttpProxy; 差异内容：type HttpProxy = connection.HttpProxy; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocketRequestOptions； API声明：caPath?: string; 差异内容：caPath?: string; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocketRequestOptions； API声明：clientCert?: ClientCert; 差异内容：clientCert?: ClientCert; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocketRequestOptions； API声明：proxy?: ProxyConfiguration; 差异内容：proxy?: ProxyConfiguration; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocketRequestOptions； API声明：protocol?: string; 差异内容：protocol?: string; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：webSocket； API声明：export type ProxyConfiguration = 'system' \| 'no-proxy' \| HttpProxy; 差异内容：export type ProxyConfiguration = 'system' \| 'no-proxy' \| HttpProxy; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：webSocket； API声明： export interface ClientCert 差异内容： export interface ClientCert | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：ClientCert； API声明：certPath: string; 差异内容：certPath: string; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：ClientCert； API声明：keyPath: string; 差异内容：keyPath: string; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：ClientCert； API声明：keyPassword?: string; 差异内容：keyPassword?: string; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：webSocket； API声明： export interface CloseResult 差异内容： export interface CloseResult | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：CloseResult； API声明：code: number; 差异内容：code: number; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：CloseResult； API声明：reason: string; 差异内容：reason: string; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：webSocket； API声明：export type ResponseHeaders = { [k: string]: string \| string[] \| undefined; }; 差异内容：export type ResponseHeaders = { [k: string]: string \| string[] \| undefined; }; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocket； API声明：on(type: 'dataEnd', callback: Callback&lt;void&gt;): void; 差异内容：on(type: 'dataEnd', callback: Callback&lt;void&gt;): void; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocket； API声明：off(type: 'dataEnd', callback?: Callback&lt;void&gt;): void; 差异内容：off(type: 'dataEnd', callback?: Callback&lt;void&gt;): void; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocket； API声明：on(type: 'headerReceive', callback: Callback&lt;ResponseHeaders&gt;): void; 差异内容：on(type: 'headerReceive', callback: Callback&lt;ResponseHeaders&gt;): void; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：WebSocket； API声明：off(type: 'headerReceive', callback?: Callback&lt;ResponseHeaders&gt;): void; 差异内容：off(type: 'headerReceive', callback?: Callback&lt;ResponseHeaders&gt;): void; | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：global； API声明： export default class VpnExtensionAbility 差异内容： export default class VpnExtensionAbility | api/@ohos.app.ability.VpnExtensionAbility.d.ts |
| 新增API | NA | 类名：VpnExtensionAbility； API声明：context: VpnExtensionContext; 差异内容：context: VpnExtensionContext; | api/@ohos.app.ability.VpnExtensionAbility.d.ts |
| 新增API | NA | 类名：VpnExtensionAbility； API声明：onCreate(want: Want): void; 差异内容：onCreate(want: Want): void; | api/@ohos.app.ability.VpnExtensionAbility.d.ts |
| 新增API | NA | 类名：VpnExtensionAbility； API声明：onDestroy(): void; 差异内容：onDestroy(): void; | api/@ohos.app.ability.VpnExtensionAbility.d.ts |
| 新增API | NA | 类名：global； API声明： declare namespace mdns 差异内容： declare namespace mdns | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：mdns； API声明：type NetAddress = connection.NetAddress; 差异内容：type NetAddress = connection.NetAddress; | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：mdns； API声明：function addLocalService(context: Context, serviceInfo: LocalServiceInfo, callback: AsyncCallback&lt;LocalServiceInfo&gt;): void; 差异内容：function addLocalService(context: Context, serviceInfo: LocalServiceInfo, callback: AsyncCallback&lt;LocalServiceInfo&gt;): void; | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：mdns； API声明：function addLocalService(context: Context, serviceInfo: LocalServiceInfo): Promise&lt;LocalServiceInfo&gt;; 差异内容：function addLocalService(context: Context, serviceInfo: LocalServiceInfo): Promise&lt;LocalServiceInfo&gt;; | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：mdns； API声明：function removeLocalService(context: Context, serviceInfo: LocalServiceInfo, callback: AsyncCallback&lt;LocalServiceInfo&gt;): void; 差异内容：function removeLocalService(context: Context, serviceInfo: LocalServiceInfo, callback: AsyncCallback&lt;LocalServiceInfo&gt;): void; | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：mdns； API声明：function removeLocalService(context: Context, serviceInfo: LocalServiceInfo): Promise&lt;LocalServiceInfo&gt;; 差异内容：function removeLocalService(context: Context, serviceInfo: LocalServiceInfo): Promise&lt;LocalServiceInfo&gt;; | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：mdns； API声明：function createDiscoveryService(context: Context, serviceType: string): DiscoveryService; 差异内容：function createDiscoveryService(context: Context, serviceType: string): DiscoveryService; | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：mdns； API声明：function resolveLocalService(context: Context, serviceInfo: LocalServiceInfo, callback: AsyncCallback&lt;LocalServiceInfo&gt;): void; 差异内容：function resolveLocalService(context: Context, serviceInfo: LocalServiceInfo, callback: AsyncCallback&lt;LocalServiceInfo&gt;): void; | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：mdns； API声明：function resolveLocalService(context: Context, serviceInfo: LocalServiceInfo): Promise&lt;LocalServiceInfo&gt;; 差异内容：function resolveLocalService(context: Context, serviceInfo: LocalServiceInfo): Promise&lt;LocalServiceInfo&gt;; | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：mdns； API声明： export interface DiscoveryService 差异内容： export interface DiscoveryService | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：DiscoveryService； API声明：on(type: 'discoveryStart', callback: Callback&lt;DiscoveryEventInfo&gt;): void; 差异内容：on(type: 'discoveryStart', callback: Callback&lt;DiscoveryEventInfo&gt;): void; | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：DiscoveryService； API声明：off(type: 'discoveryStart', callback?: Callback&lt;DiscoveryEventInfo&gt;): void; 差异内容：off(type: 'discoveryStart', callback?: Callback&lt;DiscoveryEventInfo&gt;): void; | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：DiscoveryService； API声明：on(type: 'discoveryStop', callback: Callback&lt;DiscoveryEventInfo&gt;): void; 差异内容：on(type: 'discoveryStop', callback: Callback&lt;DiscoveryEventInfo&gt;): void; | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：DiscoveryService； API声明：off(type: 'discoveryStop', callback?: Callback&lt;DiscoveryEventInfo&gt;): void; 差异内容：off(type: 'discoveryStop', callback?: Callback&lt;DiscoveryEventInfo&gt;): void; | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：DiscoveryService； API声明：on(type: 'serviceFound', callback: Callback&lt;LocalServiceInfo&gt;): void; 差异内容：on(type: 'serviceFound', callback: Callback&lt;LocalServiceInfo&gt;): void; | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：DiscoveryService； API声明：off(type: 'serviceFound', callback?: Callback&lt;LocalServiceInfo&gt;): void; 差异内容：off(type: 'serviceFound', callback?: Callback&lt;LocalServiceInfo&gt;): void; | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：DiscoveryService； API声明：on(type: 'serviceLost', callback: Callback&lt;LocalServiceInfo&gt;): void; 差异内容：on(type: 'serviceLost', callback: Callback&lt;LocalServiceInfo&gt;): void; | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：DiscoveryService； API声明：off(type: 'serviceLost', callback?: Callback&lt;LocalServiceInfo&gt;): void; 差异内容：off(type: 'serviceLost', callback?: Callback&lt;LocalServiceInfo&gt;): void; | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：DiscoveryService； API声明：startSearchingMDNS(): void; 差异内容：startSearchingMDNS(): void; | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：DiscoveryService； API声明：stopSearchingMDNS(): void; 差异内容：stopSearchingMDNS(): void; | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：mdns； API声明： export interface LocalServiceInfo 差异内容： export interface LocalServiceInfo | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：LocalServiceInfo； API声明：serviceType: string; 差异内容：serviceType: string; | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：LocalServiceInfo； API声明：serviceName: string; 差异内容：serviceName: string; | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：LocalServiceInfo； API声明：port?: number; 差异内容：port?: number; | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：LocalServiceInfo； API声明：host?: NetAddress; 差异内容：host?: NetAddress; | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：LocalServiceInfo； API声明：serviceAttribute?: Array&lt;ServiceAttribute&gt;; 差异内容：serviceAttribute?: Array&lt;ServiceAttribute&gt;; | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：mdns； API声明： export interface ServiceAttribute 差异内容： export interface ServiceAttribute | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：ServiceAttribute； API声明：key: string; 差异内容：key: string; | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：ServiceAttribute； API声明：value: Array&lt;number&gt;; 差异内容：value: Array&lt;number&gt;; | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：mdns； API声明： export interface DiscoveryEventInfo 差异内容： export interface DiscoveryEventInfo | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：DiscoveryEventInfo； API声明：serviceInfo: LocalServiceInfo; 差异内容：serviceInfo: LocalServiceInfo; | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：DiscoveryEventInfo； API声明：errorCode?: MdnsError; 差异内容：errorCode?: MdnsError; | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：mdns； API声明： export enum MdnsError 差异内容： export enum MdnsError | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：MdnsError； API声明：INTERNAL_ERROR = 0 差异内容：INTERNAL_ERROR = 0 | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：MdnsError； API声明：ALREADY_ACTIVE = 1 差异内容：ALREADY_ACTIVE = 1 | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：MdnsError； API声明：MAX_LIMIT = 2 差异内容：MAX_LIMIT = 2 | api/@ohos.net.mdns.d.ts |
| 新增API | NA | 类名：global； API声明： declare namespace networkSecurity 差异内容： declare namespace networkSecurity | api/@ohos.net.networkSecurity.d.ts |
| 新增API | NA | 类名：networkSecurity； API声明： export enum CertType 差异内容： export enum CertType | api/@ohos.net.networkSecurity.d.ts |
| 新增API | NA | 类名：CertType； API声明：CERT_TYPE_PEM = 0 差异内容：CERT_TYPE_PEM = 0 | api/@ohos.net.networkSecurity.d.ts |
| 新增API | NA | 类名：CertType； API声明：CERT_TYPE_DER = 1 差异内容：CERT_TYPE_DER = 1 | api/@ohos.net.networkSecurity.d.ts |
| 新增API | NA | 类名：networkSecurity； API声明： export interface CertBlob 差异内容： export interface CertBlob | api/@ohos.net.networkSecurity.d.ts |
| 新增API | NA | 类名：CertBlob； API声明：type: CertType; 差异内容：type: CertType; | api/@ohos.net.networkSecurity.d.ts |
| 新增API | NA | 类名：CertBlob； API声明：data: string \| ArrayBuffer; 差异内容：data: string \| ArrayBuffer; | api/@ohos.net.networkSecurity.d.ts |
| 新增API | NA | 类名：networkSecurity； API声明：export function certVerification(cert: CertBlob, caCert?: CertBlob): Promise&lt;number&gt;; 差异内容：export function certVerification(cert: CertBlob, caCert?: CertBlob): Promise&lt;number&gt;; | api/@ohos.net.networkSecurity.d.ts |
| 新增API | NA | 类名：networkSecurity； API声明：export function certVerificationSync(cert: CertBlob, caCert?: CertBlob): number; 差异内容：export function certVerificationSync(cert: CertBlob, caCert?: CertBlob): number; | api/@ohos.net.networkSecurity.d.ts |
| 新增API | NA | 类名：global； API声明： declare namespace policy 差异内容： declare namespace policy | api/@ohos.net.policy.d.ts |
| 新增API | NA | 类名：policy； API声明：type NetBearType = connection.NetBearType; 差异内容：type NetBearType = connection.NetBearType; | api/@ohos.net.policy.d.ts |
| 新增API | NA | 类名：global； API声明： declare namespace statistics 差异内容： declare namespace statistics | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：statistics； API声明：type NetBearType = connection.NetBearType; 差异内容：type NetBearType = connection.NetBearType; | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：statistics； API声明：function getIfaceRxBytes(nic: string, callback: AsyncCallback&lt;number&gt;): void; 差异内容：function getIfaceRxBytes(nic: string, callback: AsyncCallback&lt;number&gt;): void; | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：statistics； API声明：function getIfaceRxBytes(nic: string): Promise&lt;number&gt;; 差异内容：function getIfaceRxBytes(nic: string): Promise&lt;number&gt;; | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：statistics； API声明：function getIfaceTxBytes(nic: string, callback: AsyncCallback&lt;number&gt;): void; 差异内容：function getIfaceTxBytes(nic: string, callback: AsyncCallback&lt;number&gt;): void; | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：statistics； API声明：function getIfaceTxBytes(nic: string): Promise&lt;number&gt;; 差异内容：function getIfaceTxBytes(nic: string): Promise&lt;number&gt;; | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：statistics； API声明：function getCellularRxBytes(callback: AsyncCallback&lt;number&gt;): void; 差异内容：function getCellularRxBytes(callback: AsyncCallback&lt;number&gt;): void; | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：statistics； API声明：function getCellularRxBytes(): Promise&lt;number&gt;; 差异内容：function getCellularRxBytes(): Promise&lt;number&gt;; | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：statistics； API声明：function getCellularTxBytes(callback: AsyncCallback&lt;number&gt;): void; 差异内容：function getCellularTxBytes(callback: AsyncCallback&lt;number&gt;): void; | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：statistics； API声明：function getCellularTxBytes(): Promise&lt;number&gt;; 差异内容：function getCellularTxBytes(): Promise&lt;number&gt;; | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：statistics； API声明：function getAllRxBytes(callback: AsyncCallback&lt;number&gt;): void; 差异内容：function getAllRxBytes(callback: AsyncCallback&lt;number&gt;): void; | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：statistics； API声明：function getAllRxBytes(): Promise&lt;number&gt;; 差异内容：function getAllRxBytes(): Promise&lt;number&gt;; | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：statistics； API声明：function getAllTxBytes(callback: AsyncCallback&lt;number&gt;): void; 差异内容：function getAllTxBytes(callback: AsyncCallback&lt;number&gt;): void; | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：statistics； API声明：function getAllTxBytes(): Promise&lt;number&gt;; 差异内容：function getAllTxBytes(): Promise&lt;number&gt;; | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：statistics； API声明：function getUidRxBytes(uid: number, callback: AsyncCallback&lt;number&gt;): void; 差异内容：function getUidRxBytes(uid: number, callback: AsyncCallback&lt;number&gt;): void; | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：statistics； API声明：function getUidRxBytes(uid: number): Promise&lt;number&gt;; 差异内容：function getUidRxBytes(uid: number): Promise&lt;number&gt;; | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：statistics； API声明：function getUidTxBytes(uid: number, callback: AsyncCallback&lt;number&gt;): void; 差异内容：function getUidTxBytes(uid: number, callback: AsyncCallback&lt;number&gt;): void; | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：statistics； API声明：function getUidTxBytes(uid: number): Promise&lt;number&gt;; 差异内容：function getUidTxBytes(uid: number): Promise&lt;number&gt;; | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：statistics； API声明：function getSockfdRxBytes(sockfd: number, callback: AsyncCallback&lt;number&gt;): void; 差异内容：function getSockfdRxBytes(sockfd: number, callback: AsyncCallback&lt;number&gt;): void; | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：statistics； API声明：function getSockfdRxBytes(sockfd: number): Promise&lt;number&gt;; 差异内容：function getSockfdRxBytes(sockfd: number): Promise&lt;number&gt;; | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：statistics； API声明：function getSockfdTxBytes(sockfd: number, callback: AsyncCallback&lt;number&gt;): void; 差异内容：function getSockfdTxBytes(sockfd: number, callback: AsyncCallback&lt;number&gt;): void; | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：statistics； API声明：function getSockfdTxBytes(sockfd: number): Promise&lt;number&gt;; 差异内容：function getSockfdTxBytes(sockfd: number): Promise&lt;number&gt;; | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：global； API声明： declare namespace vpn 差异内容： declare namespace vpn | api/@ohos.net.vpn.d.ts |
| 新增API | NA | 类名：vpn； API声明：export type LinkAddress = connection.LinkAddress; 差异内容：export type LinkAddress = connection.LinkAddress; | api/@ohos.net.vpn.d.ts |
| 新增API | NA | 类名：vpn； API声明：export type RouteInfo = connection.RouteInfo; 差异内容：export type RouteInfo = connection.RouteInfo; | api/@ohos.net.vpn.d.ts |
| 新增API | NA | 类名：vpn； API声明：export type AbilityContext = _AbilityContext; 差异内容：export type AbilityContext = _AbilityContext; | api/@ohos.net.vpn.d.ts |
| 新增API | NA | 类名：global； API声明： declare namespace vpnExtension 差异内容： declare namespace vpnExtension | api/@ohos.net.vpnExtension.d.ts |
| 新增API | NA | 类名：vpnExtension； API声明：export type LinkAddress = connection.LinkAddress; 差异内容：export type LinkAddress = connection.LinkAddress; | api/@ohos.net.vpnExtension.d.ts |
| 新增API | NA | 类名：vpnExtension； API声明：export type RouteInfo = connection.RouteInfo; 差异内容：export type RouteInfo = connection.RouteInfo; | api/@ohos.net.vpnExtension.d.ts |
| 新增API | NA | 类名：vpnExtension； API声明：export type VpnExtensionContext = _VpnExtensionContext; 差异内容：export type VpnExtensionContext = _VpnExtensionContext; | api/@ohos.net.vpnExtension.d.ts |
| 新增API | NA | 类名：vpnExtension； API声明：function startVpnExtensionAbility(want: Want): Promise&lt;void&gt;; 差异内容：function startVpnExtensionAbility(want: Want): Promise&lt;void&gt;; | api/@ohos.net.vpnExtension.d.ts |
| 新增API | NA | 类名：vpnExtension； API声明：function stopVpnExtensionAbility(want: Want): Promise&lt;void&gt;; 差异内容：function stopVpnExtensionAbility(want: Want): Promise&lt;void&gt;; | api/@ohos.net.vpnExtension.d.ts |
| 新增API | NA | 类名：vpnExtension； API声明：function createVpnConnection(context: VpnExtensionContext): VpnConnection; 差异内容：function createVpnConnection(context: VpnExtensionContext): VpnConnection; | api/@ohos.net.vpnExtension.d.ts |
| 新增API | NA | 类名：vpnExtension； API声明： export interface VpnConnection 差异内容： export interface VpnConnection | api/@ohos.net.vpnExtension.d.ts |
| 新增API | NA | 类名：VpnConnection； API声明：create(config: VpnConfig): Promise&lt;number&gt;; 差异内容：create(config: VpnConfig): Promise&lt;number&gt;; | api/@ohos.net.vpnExtension.d.ts |
| 新增API | NA | 类名：VpnConnection； API声明：protect(socketFd: number): Promise&lt;void&gt;; 差异内容：protect(socketFd: number): Promise&lt;void&gt;; | api/@ohos.net.vpnExtension.d.ts |
| 新增API | NA | 类名：VpnConnection； API声明：destroy(): Promise&lt;void&gt;; 差异内容：destroy(): Promise&lt;void&gt;; | api/@ohos.net.vpnExtension.d.ts |
| 新增API | NA | 类名：vpnExtension； API声明： export interface VpnConfig 差异内容： export interface VpnConfig | api/@ohos.net.vpnExtension.d.ts |
| 新增API | NA | 类名：VpnConfig； API声明：addresses: Array&lt;LinkAddress&gt;; 差异内容：addresses: Array&lt;LinkAddress&gt;; | api/@ohos.net.vpnExtension.d.ts |
| 新增API | NA | 类名：VpnConfig； API声明：routes?: Array&lt;RouteInfo&gt;; 差异内容：routes?: Array&lt;RouteInfo&gt;; | api/@ohos.net.vpnExtension.d.ts |
| 新增API | NA | 类名：VpnConfig； API声明：dnsAddresses?: Array&lt;string&gt;; 差异内容：dnsAddresses?: Array&lt;string&gt;; | api/@ohos.net.vpnExtension.d.ts |
| 新增API | NA | 类名：VpnConfig； API声明：searchDomains?: Array&lt;string&gt;; 差异内容：searchDomains?: Array&lt;string&gt;; | api/@ohos.net.vpnExtension.d.ts |
| 新增API | NA | 类名：VpnConfig； API声明：mtu?: number; 差异内容：mtu?: number; | api/@ohos.net.vpnExtension.d.ts |
| 新增API | NA | 类名：VpnConfig； API声明：isIPv4Accepted?: boolean; 差异内容：isIPv4Accepted?: boolean; | api/@ohos.net.vpnExtension.d.ts |
| 新增API | NA | 类名：VpnConfig； API声明：isIPv6Accepted?: boolean; 差异内容：isIPv6Accepted?: boolean; | api/@ohos.net.vpnExtension.d.ts |
| 新增API | NA | 类名：VpnConfig； API声明：isInternal?: boolean; 差异内容：isInternal?: boolean; | api/@ohos.net.vpnExtension.d.ts |
| 新增API | NA | 类名：VpnConfig； API声明：isBlocking?: boolean; 差异内容：isBlocking?: boolean; | api/@ohos.net.vpnExtension.d.ts |
| 新增API | NA | 类名：VpnConfig； API声明：trustedApplications?: Array&lt;string&gt;; 差异内容：trustedApplications?: Array&lt;string&gt;; | api/@ohos.net.vpnExtension.d.ts |
| 新增API | NA | 类名：VpnConfig； API声明：blockedApplications?: Array&lt;string&gt;; 差异内容：blockedApplications?: Array&lt;string&gt;; | api/@ohos.net.vpnExtension.d.ts |
| 新增API | NA | 类名：global； API声明： export default class VpnExtensionContext 差异内容： export default class VpnExtensionContext | api/application/VpnExtensionContext.d.ts |
