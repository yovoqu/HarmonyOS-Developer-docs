# RemoteCommunication

更新时间：2026-06-13 03:51:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

提供远程通信能力相关接口。
 
支持http会话功能。
 
**起始版本：** 5.0.0(12)
 
支持quic功能。
 
**起始版本：** 26.0.0
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 文件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| rcp.h | 声明用于访问远程通信的API。提供基本的函数，结构体和const定义。 |
| rcp_quic.h | 声明quic协议相关的API。提供基本的函数，结构体和常量定义。 |
 
 
  

#### 结构体

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| struct Rcp_Buffer | 文本存储结构。 |
| struct Rcp_ContentOrPathOrCallback | Rcp_FormFieldFileValue中使用的简单表单数据字段值。 |
| struct Rcp_FormFieldFileValue | 表单字段文件值。 |
| struct Rcp_FormFieldValue | 简单表单数据字段值，参见Rcp_Form和Rcp_MultipartFormFieldValue。 |
| struct Rcp_MultipartFormFieldValue | 多部分表单域值，在Rcp_MultipartForm中使用。 |
| struct Rcp_FormOrder | 表单键值对发送顺序。 |
| struct Rcp_RequestContent | 请求的内容。 |
| struct Rcp_HeaderValue | 请求或响应的标头映射的值类型。 |
| struct Rcp_HeaderEntry | 请求或响应的标头的所有键值对。 |
| struct Rcp_Credential | 服务器身份验证中使用的身份验证凭据，包括用户名和密码。 |
| struct Rcp_ServerAuthentication | 服务器身份验证。 |
| struct Rcp_Urls | URL，用于确定主机是否正在使用代理。 |
| struct Rcp_Exclusions | 代理配置中用于过滤不使用代理的URLs。 |
| struct Rcp_CertificateAuthority | 用于验证远程服务器标识的证书颁发机构（CA）。 |
| struct Rcp_ClientCertificate | 发送到远程服务器的客户端证书，远程服务器将使用它来验证客户端的标识。 |
| struct Rcp_SecurityConfiguration | 请求的安全配置。 |
| struct Rcp_WebProxy | 自定义代理配置。 |
| struct Rcp_IpAndPort | 该接口用在Rcp_DnsServers中，表示一个DNS服务器的地址和端口。 |
| struct Rcp_DnsServers | DNS服务器。Rcp_DnsConfiguration.dnsRules中的类型之一。 |
| struct Rcp_IpAddress | 指定静态DNS规则使用的IP地址组。用于Rcp_StaticDnsRuleItem。 |
| struct Rcp_StaticDnsRuleItem | 描述单个静态DNS规则。 |
| struct Rcp_StaticDnsRule | 静态DNS规则。 |
| struct Rcp_DnsRule | DNS规则配置。 |
| struct Rcp_OnDataReceiveCallback | 接收到数据时回调。Rcp_EventsHandler中的配置。 |
| struct Rcp_OnProgressCallback | 收发时回调配置，在Rcp_EventsHandler中配置。 |
| struct Rcp_OnHeaderReceiveCallback | Rcp_EventsHandler中配置的接收到的header的回调配置。 |
| struct Rcp_OnVoidCallback | 在Rcp_EventsHandler中配置的数据结束或取消事件的回调配置。 |
| struct Rcp_EventsHandler | 监听不同HTTP事件的回调函数。 |
| struct Rcp_Timeout | 请求的超时配置。 |
| struct Rcp_DnsOverHttps | HTTPS上的DNS配置如果设置，则首选由DOH dns服务器解析的地址。 |
| struct Rcp_TransferConfiguration | 传输配置。 |
| struct Rcp_InfoToCollect | 指定要收集的请求处理事件。可以通过响应对象检查收集的事件。 |
| struct Rcp_TracingConfiguration | 请求追踪配置。 |
| struct Rcp_ProxyConfiguration | 代理配置。 |
| struct Rcp_DnsConfiguration | DNS解析配置。 |
| struct Rcp_Configuration | 请求配置。 |
| struct Rcp_TransferRange | HTTP传输范围。该设置将转换为HTTP Range标头。具有范围标头的HTTP请求要求服务器仅发送回HTTP响应的一部分。 |
| struct Rcp_Request | 网络请求。 |
| struct Rcp_RequestCookieEntry | 描述请求的所有Cookie键值对。 |
| struct Rcp_DebugInfo | 描述存储在Rcp_Response中的调试信息的结构。 |
| struct Rcp_CookieAttributeEntry | 响应Cookie属性条目。 |
| struct Rcp_ResponseCookies | 响应Cookie。 |
| struct Rcp_TimeInfo | 响应计时信息。 |
| struct Rcp_ResponseCallbackObject | 响应回调结构体。 |
| struct Rcp_Response | 网络请求的响应。 |
| struct Rcp_Interceptor | 异步拦截器。 |
| struct Rcp_SyncInterceptor | 同步拦截器。 |
| struct Rcp_InterceptorArray | 异步拦截器数组。 |
| struct Rcp_SyncInterceptorArray | 同步拦截器数组。 |
| struct Rcp_SessionListener | 关闭或取消会话事件的回调函数。 |
| struct Rcp_ConnectionConfiguration | 连接配置。 |
| struct Rcp_SessionConfiguration | 会话配置。 |
| struct Rcp_OnBinaryReceiveCallback | 接收到响应的二进制数据时的回调。 |
| struct Rcp_OnStatusCodeReceiveCallback | 接收到响应的状态码时的回调。 |
| struct Rcp_OnGetDataCallback | 获取数据的回调。 |
| struct Rcp_QuicSlist | 链表数据结构。 |
| struct Rcp_QuicIpAddress | 用于存储IP地址的数据结构。 |
| struct Rcp_QuicIoVec | 用于存储二进制内容的数据结构。 |
| struct Rcp_QuicStreamData | quic连接中用于接收流式数据的存储结构。 |
 
 
  

#### 宏定义

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| RCP_MAX_REQUEST_ID_LEN 32 | 请求ID的最大长度。 |
| RCP_MAX_CONTENT_TYPE_LEN 64 | 内容类型最大长度。 |
| RCP_MAX_FILENAME_LEN 128 | 文件名最大长度。 |
| RCP_MAX_PATH_LEN 128 | 路径的最大长度。 |
| RCP_METHOD_GET "GET" | HTTP get方法。 |
| RCP_METHOD_HEAD "HEAD" | HTTP head方法。 |
| RCP_METHOD_OPTIONS "OPTIONS" | HTTP options方法。 |
| RCP_METHOD_TRACE "TRACE" | HTTP trace方法。 |
| RCP_METHOD_DELETE "DELETE" | HTTP delete方法。 |
| RCP_METHOD_POST "POST" | HTTP post方法。 |
| RCP_METHOD_PUT "PUT" | HTTP put方法。 |
| RCP_METHOD_PATCH "PATCH" | HTTP patch方法。 |
| RCP_IP_MAX_LEN 40 | IP地址的最大长度。 |
| RCP_HOST_MAX_LEN 256 | 主机名的最大长度。 |
| RCP_QUIC_IP_MAX_LEN 40 | quic连接的IP地址的最大长度。 |
 
 
  

#### 类型定义

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| typedef enum Rcp_FormValueType Rcp_FormValueType | 表单值类型。 |
| typedef int(* Rcp_GetDataCallback) (char *out, uint32_t size) | 通过回调函数获取数据。当API需要将数据的下一部分发送到服务器时，将调用此回调。 |
| typedef enum Rcp_ContentOrPathOrCallbackType Rcp_ContentOrPathOrCallbackType | 回调的内容、路径或类型。用于区分Rcp_ContentOrPathOrCallback中使用的数据。 |
| typedef struct Rcp_Buffer Rcp_Buffer | 文本存储结构。 |
| typedef struct Rcp_ContentOrPathOrCallback Rcp_ContentOrPathOrCallback | Rcp_FormFieldFileValue中使用的简单表单数据字段值。 |
| typedef enum Rcp_MultipartValueType Rcp_MultipartValueType | 多部分值类型。用于区分Rcp_MultipartFormFieldValue中使用的数据。 |
| typedef struct Rcp_FormFieldFileValue Rcp_FormFieldFileValue | 表单字段文件值。 |
| typedef struct Rcp_FormFieldValue Rcp_FormFieldValue | 简单表单数据字段值，参见Rcp_Form和Rcp_MultipartFormFieldValue。 |
| typedef struct Rcp_MultipartFormFieldValue Rcp_MultipartFormFieldValue | 多部分表单域值，在Rcp_MultipartForm中使用。 |
| typedef enum Rcp_ContentType Rcp_ContentType | 内容类型。用于区分Rcp_RequestContent中使用的数据。 |
| typedef struct Rcp_Form Rcp_Form | 简单表单。 |
| typedef struct Rcp_MultipartForm Rcp_MultipartForm | 多部分表单。 |
| typedef struct Rcp_FormOrder Rcp_FormOrder | 表单键值对发送顺序。 |
| typedef struct Rcp_RequestContent Rcp_RequestContent | 请求的内容。 |
| typedef struct Rcp_Headers Rcp_Headers | 请求或响应的标头。 |
| typedef struct Rcp_HeaderValue Rcp_HeaderValue | 请求或响应的标头映射的值类型。 |
| typedef struct Rcp_HeaderEntry Rcp_HeaderEntry | 请求或响应的标头的所有键值对。 |
| typedef enum Rcp_AuthenticationType Rcp_AuthenticationType | 枚举类型。服务器的身份验证类型。如果未设置，请与服务器协商。 |
| typedef struct Rcp_Credential Rcp_Credential | 服务器身份验证中使用的身份验证凭据，包括用户名和密码。 |
| typedef struct Rcp_ServerAuthentication Rcp_ServerAuthentication | 服务器身份验证。 |
| typedef bool(* Rcp_ExclusionFunction) (const char *url) | 判断host是否使用代理的函数指针，true代表使用，false代表不使用。 |
| typedef struct Rcp_Urls Rcp_Urls | url，用于确定主机是否正在使用代理。 |
| typedef enum Rcp_ExclusionsValueType Rcp_ExclusionsValueType | 代理排除中使用的数据类型. 用于区分Rcp_Exclusions中使用的数据。 |
| typedef struct Rcp_Exclusions Rcp_Exclusions | 代理配置中用于过滤不使用代理的URLs。 |
| typedef enum Rcp_CertType Rcp_CertType | 客户端证书类型。 |
| typedef struct Rcp_CertificateAuthority Rcp_CertificateAuthority | 用于验证远程服务器标识的证书颁发机构（CA）。 |
| typedef struct Rcp_ClientCertificate Rcp_ClientCertificate | 发送到远程服务器的客户端证书，远程服务器将使用它来验证客户端的标识。 |
| typedef enum Rcp_RemoteValidationType Rcp_RemoteValidationType | 远程验证类型。 |
| typedef struct Rcp_SecurityConfiguration Rcp_SecurityConfiguration | 请求的安全配置。 |
| typedef enum Rcp_ProxyTunnelMode Rcp_ProxyTunnelMode | 用于控制何时创建代理隧道。 隧道或隧道传输意味着向代理发送HTTP CONNECT请求，要求它连接到特定端口号上的远程主机，然后流量只是通过代理。“auto”表示为HTTPS创建隧道，而不是为HTTP创建隧道。“always”表示始终创建隧道。 |
| typedef struct Rcp_WebProxy Rcp_WebProxy | 自定义代理配置。 |
| typedef struct Rcp_IpAndPort Rcp_IpAndPort | 该接口用在Rcp_DnsServers中，表示一个DNS服务器的地址和端口。 |
| typedef struct Rcp_DnsServers Rcp_DnsServers | DNS服务器。Rcp_DnsConfiguration.dnsRules中的类型之一。 |
| typedef struct Rcp_IpAddress Rcp_IpAddress | 指定静态DNS规则使用的IP地址组。用于Rcp_StaticDnsRuleItem。 |
| typedef struct Rcp_StaticDnsRuleItem Rcp_StaticDnsRuleItem | 描述单个静态DNS规则。 |
| typedef struct Rcp_StaticDnsRule Rcp_StaticDnsRule | 静态DNS规则。 |
| typedef Rcp_IpAddress *(* Rcp_DynamicDnsRuleFunction) (const char *host, uint16_t port) | 一个可以根据主机名和端口直接返回IP地址的函数。用于动态DNS解析。 |
| typedef enum Rcp_DnsRuleType Rcp_DnsRuleType | DNS规则类型。用于区分Rcp_DnsRule中使用的dns规则类型。 |
| typedef struct Rcp_DnsRule Rcp_DnsRule | DNS规则配置。 |
| typedef size_t(* Rcp_OnDataReceiveCallbackFunc) (void *usrObject, const char *data) | 接收到响应正文时调用的回调函数（字符数据）。 |
| typedef size_t(* Rcp_OnBinaryReceiveCallbackFunc) (void *usrObject, Rcp_Buffer *buffer) | 接收到响应正文时调用的回调函数（二进制数据）。 |
| typedef void (* Rcp_OnStatusCodeReceiveCallbackFunc)(void *usrObject, uint32_t statusCode) | 接收到响应状态码时调用的回调函数。 |
| typedef void(* Rcp_OnProgressCallbackFunc) (void *usrObject, uint64_t totalSize, uint64_t transferredSize) | 请求/响应数据传输过程中调用的回调函数。 |
| typedef void(* Rcp_OnHeaderReceiveCallbackFunc) (void *usrObject, Rcp_Headers *headers) | 收到所有请求时调用的回调。 |
| typedef void(* Rcp_OnVoidCallbackFunc) (void *usrObject) | 请求的DataEnd或Canceled事件回调的回调函数。 |
| typedef struct Rcp_OnDataReceiveCallback Rcp_OnDataReceiveCallback | 接收到数据时回调。Rcp_EventsHandler中的配置。 |
| typedef struct Rcp_OnProgressCallback Rcp_OnProgressCallback | 收发时回调配置，在Rcp_EventsHandler中配置。 |
| typedef struct Rcp_OnHeaderReceiveCallback Rcp_OnHeaderReceiveCallback | Rcp_EventsHandler中配置的接收到的header回调配置。 |
| typedef struct Rcp_OnVoidCallback Rcp_OnVoidCallback | 在Rcp_EventsHandler中配置的数据结束或已取消事件的回调配置。 |
| typedef struct Rcp_EventsHandler Rcp_EventsHandler | 监听不同HTTP事件的回调函数。 |
| typedef struct Rcp_Timeout Rcp_Timeout | 请求的超时配置。 |
| typedef struct Rcp_DnsOverHttps Rcp_DnsOverHttps | HTTPS上的DNS配置如果设置，则首选由DOH DNS服务器解析的地址。 |
| typedef enum Rcp_PathPreference Rcp_PathPreference | 请求路径首选项。 |
| typedef struct Rcp_TransferConfiguration Rcp_TransferConfiguration | 传输配置。 |
| typedef struct Rcp_InfoToCollect Rcp_InfoToCollect | 指定要收集的请求处理事件。可以通过响应对象检查收集的事件。 |
| typedef struct Rcp_TracingConfiguration Rcp_TracingConfiguration | 请求追踪配置。 |
| typedef enum Rcp_ProxyType Rcp_ProxyType | 代理类型。用于区分不同的代理配置。 |
| typedef struct Rcp_ProxyConfiguration Rcp_ProxyConfiguration | 代理配置。 |
| typedef struct Rcp_DnsConfiguration Rcp_DnsConfiguration | DNS解析配置。 |
| typedef struct Rcp_Configuration Rcp_Configuration | 请求配置。 |
| typedef struct Rcp_TransferRange Rcp_TransferRange | HTTP传输范围。该设置将转换为HTTP Range标头。具有范围标头的HTTP请求要求服务器仅返回HTTP响应的一部分。 |
| typedef struct Rcp_RequestCookies Rcp_RequestCookies | 请求Cookie。 |
| typedef struct Rcp_Request Rcp_Request | 网络请求。 |
| typedef struct Rcp_RequestCookieEntry Rcp_RequestCookieEntry | 描述请求的所有Cookie键值对。 |
| typedef enum Rcp_StatusCode Rcp_StatusCode | 请求响应的状态码。 |
| typedef enum Rcp_DebugEvent Rcp_DebugEvent | 描述调试信息的事件类型。 |
| typedef struct Rcp_DebugInfo Rcp_DebugInfo | 描述存储在Rcp_Response中的调试信息的结构。 |
| typedef struct Rcp_CookieAttributes Rcp_CookieAttributes | 描述Rcp_Response中Cookie属性的类型。 |
| typedef struct Rcp_CookieAttributeEntry Rcp_CookieAttributeEntry | 响应Cookie属性条目。 |
| typedef struct Rcp_ResponseCookies Rcp_ResponseCookies | 响应Cookie。 |
| typedef struct Rcp_TimeInfo Rcp_TimeInfo | 响应计时信息。 |
| typedef struct Rcp_Response Rcp_Response | 网络请求的响应。 |
| typedef void(* Rcp_ResponseCallback) (void *usrCtx, Rcp_Response *response, uint32_t errCode) | 响应回调函数指针。 |
| typedef struct Rcp_ResponseCallbackObject Rcp_ResponseCallbackObject | 响应回调结构体。 |
| typedef struct Rcp_RequestHandler Rcp_RequestHandler | 与Rcp_Interceptor关联的异步处理器。 |
| typedef struct Rcp_SyncRequestHandler Rcp_SyncRequestHandler | 与Rcp_SyncInterceptor关联的同步处理器。 |
| typedef struct Rcp_Interceptor Rcp_Interceptor | 异步拦截器。 |
| typedef struct Rcp_SyncInterceptor Rcp_SyncInterceptor | 同步拦截器。 |
| typedef struct Rcp_InterceptorArray Rcp_InterceptorArray | 异步拦截器数组。 |
| typedef struct Rcp_SyncInterceptorArray Rcp_SyncInterceptorArray | 同步拦截器数组。 |
| typedef enum Rcp_SessionType Rcp_SessionType | 会话类型。 |
| typedef struct Rcp_Session Rcp_Session | 会话。 |
| typedef struct Rcp_SessionListener Rcp_SessionListener | 关闭或取消会话事件的回调函数。 |
| typedef struct Rcp_ConnectionConfiguration Rcp_ConnectionConfiguration | 连接配置。 |
| typedef struct Rcp_SessionConfiguration Rcp_SessionConfiguration | 会话配置。 |
| typedef struct Rcp_OnBinaryReceiveCallback Rcp_OnBinaryReceiveCallback | 接收到响应的二进制数据时的回调。 |
| typedef struct Rcp_OnStatusCodeReceiveCallback Rcp_OnStatusCodeReceiveCallback | 接收到响应的状态码时的回调。 |
| typedef struct Rcp_OnGetDataCallback Rcp_OnGetDataCallback | 获取数据的回调。 |
| typedef size_t(* Rcp_GetDataCallbackFunc) (void *userObject, uint8_t *outData, size_t size) | 获取数据的回调函数。 |
| typedef void Rcp_QuicConn | quic连接实例的类型。 |
| typedef void Rcp_QuicSession | quic会话的类型，可以管理多个连接实例。 |
| typedef struct Rcp_QuicSlist Rcp_QuicSlist | 链表数据结构。 |
| typedef enum RCP_QuicIpResolve RCP_QuicIpResolve | 请求DNS解析时使用的IP解析类型。 |
| typedef struct Rcp_QuicIpAddress Rcp_QuicIpAddress | 用于存储IP地址的数据结构。 |
| typedef Rcp_QuicIpAddress (*Rcp_QuicDynamicDnsRuleFunction) (Rcp_QuicConn *conn, void *userObject, const char *host, uint16_t port) | 自定义DNS解析回调函数，根据主机名和端口返回IP地址。 |
| typedef enum Rcp_QuicConnOpt | quic连接选项类型，用于配置连接的各种参数和回调函数。 |
| typedef enum Rcp_QuicStreamOpt | quic流选项类型，用于配置流的各种参数和回调函数。 |
| typedef enum Rcp_QuicConnInfo | quic连接信息类型。用于查询连接的各种信息。 |
| typedef enum Rcp_QuicStreamInfo | quic流信息类型。用于查询流的各种信息。 |
| typedef enum Rcp_QuicErrorCode | quic请求中可能出现的错误码。 |
| typedef enum Rcp_QuicStreamDirection | quic流的方向类型。 |
| typedef enum Rcp_QuicStreamShutdown | quic流的关闭操作的类型。用于指定关闭流的读或写方向。 |
| typedef struct Rcp_QuicIoVec Rcp_QuicIoVec | 用于存储二进制内容的数据结构。 |
| typedef struct Rcp_QuicStreamData Rcp_QuicStreamData | quic连接中用于接收流式数据的存储结构。 |
| typedef Rcp_QuicErrorCode (*Rcp_QuicConnectionOnCertAuthority) (Rcp_QuicConn *conn, void *userObject, const unsigned char *const *certs, const size_t *certLens, size_t certsCount) | 证书校验的回调函数。在quic建链时，用于自定义校验对端证书。 |
| typedef void (*Rcp_QuicConnectionOnSessionTicketUpdate) (Rcp_QuicConn *conn, void *userObject, const char *sessionTicket, size_t length) | quic会话票据更新回调函数。在quic会话中票据更新时触发，返回新的票据。 |
| typedef void (*Rcp_QuicConnectionOnConnected) (Rcp_QuicConn *conn, void *userObject) | quic连接成功回调函数。quic连接成功建立时触发该函数。 |
| typedef void (*Rcp_QuicConnectionOnError) (Rcp_QuicConn *conn, void *userObject, Rcp_QuicErrorCode errCode, const char *errDetail) | quic连接失败回调函数。quic连接建立失败时触发该函数，返回失败原因。 |
| typedef void (*Rcp_QuicConnectionOnClosed) (Rcp_QuicConn *conn, void *userObject) | quic连接关闭回调函数。quic连接关闭时触发，通知连接已关闭。 |
| typedef void (*Rcp_QuicConnectionOnStreamInbound) (Rcp_QuicConn *conn, void *userObject, uint64_t streamId) | quic连接中入站流回调函数。当quic连接中对端创建流时触发，处理对端发起的流，设置流的选项和回调。 |
| typedef void (*Rcp_QuicStreamOnEvent) (Rcp_QuicConn *conn, void *userObject, uint64_t streamId, Rcp_QuicErrorCode errCode, const char *errDetail) | quic连接中流事件回调函数。当quic连接中的流发生事件时触发，用于处理流的状态变化和错误。 |
| typedef uint64_t (*Rcp_QuicStreamOnReceiveData) (Rcp_QuicConn *conn, void *userObject, uint64_t streamId, const Rcp_QuicStreamData *streamData) | quic连接中流数据接收回调函数。当quic连接中接收到流数据时触发，用于处理接收到的数据。 |
 
 
  

#### 枚举

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| Rcp_FormValueType { RCP_FORM_VALUE_TYPE_INT32, RCP_FORM_VALUE_TYPE_INT64, RCP_FORM_VALUE_TYPE_BOOL, RCP_FORM_VALUE_TYPE_STRING, RCP_FORM_VALUE_TYPE_DOUBLE } | 表单值类型。 |
| Rcp_ContentOrPathOrCallbackType { RCP_FILE_VALUE_TYPE_CONTENT, RCP_FILE_VALUE_TYPE_PATH, RCP_FILE_VALUE_TYPE_CALLBACK } | 回调的内容、路径或类型。用于区分Rcp_ContentOrPathOrCallback中使用的数据。 |
| Rcp_MultipartValueType { RCP_TYPE_FORM_FIELD_VALUE, RCP_TYPE_FORM_FIELD_FILE_VALUE } | 多部分值类型。用于区分Rcp_MultipartFormFieldValue中使用的数据。 |
| Rcp_ContentType { RCP_CONTENT_TYPE_STRING, RCP_CONTENT_TYPE_FORM, RCP_CONTENT_TYPE_MULTIPARTFORM, RCP_CONTENT_TYPE_GETCALLBACK } | 内容类型。用于区分Rcp_RequestContent中使用的数据。 |
| Rcp_AuthenticationType { RCP_AUTHENTICATION_AUTO, RCP_AUTHENTICATION_BASIC, RCP_AUTHENTICATION_NTLM, RCP_AUTHENTICATION_DIGEST } | 枚举类型。服务器的身份验证类型。如果未设置，请与服务器协商。 |
| Rcp_ExclusionsValueType { RCP_EXCLUSION_USE_URL_ARRAY, RCP_EXCLUSION_USE_CALLBACK } | 代理排除中使用的数据类型，用于区分Rcp_Exclusions中使用的数据。 |
| Rcp_CertType { RCP_CERT_PEM, RCP_CERT_DER, RCP_CERT_P12 } | 客户端证书类型。 |
| Rcp_RemoteValidationType { RCP_REMOTE_VALIDATION_SYSTEM, RCP_REMOTE_VALIDATION_SKIP, RCP_REMOTE_VALIDATION_CERTIFICATE_AUTHORITY } | 远程验证类型。 |
| Rcp_ProxyTunnelMode { RCP_PROXY_TUNNEL_AUTO, RCP_PROXY_TUNNEL_ALWAYS } | 用于控制何时创建代理隧道。 隧道或隧道传输意味着向代理发送HTTP CONNECT请求，要求它连接到特定端口号上的远程主机，然后流量只是通过代理。“auto”表示为HTTPS创建隧道，而不是为HTTP创建隧道。“always”表示始终创建隧道。 |
| Rcp_DnsRuleType { RCP_DNS_RULE_DNS_SERVERS, RCP_DNS_RULE_STATIC, RCP_DNS_RULE_DYNAMIC } | DNS规则类型。用于区分Rcp_DnsRule中使用的DNS规则类型。 |
| Rcp_PathPreference { RCP_PATH_PREFERENCE_AUTO, RCP_PATH_PREFERENCE_WIFI, RCP_PATH_PREFERENCE_CELLULAR } | 请求路径首选项。 |
| Rcp_ProxyType { RCP_PROXY_SYSTEM, RCP_PROXY_CUSTOM, RCP_PROXY_NO_PROXY } | 代理类型。用于区分不同的代理配置。 |
| Rcp_StatusCode { RCP_NONE = 0, RCP_OK = 200, RCP_CREATED, RCP_ACCEPTED, RCP_NOT_AUTHORITATIVE, RCP_NO_CONTENT, RCP_RESET, RCP_PARTIAL, RCP_MULTI_CHOICE = 300, RCP_MOVED_PERMANENTLY, RCP_MOVED_TEMPORARILY, RCP_SEE_OTHER, RCP_NOT_MODIFIED, RCP_USE_PROXY, RCP_BAD_REQUEST = 400, RCP_UNAUTHORIZED, RCP_PAYMENT_REQUIRED, RCP_FORBIDDEN, RCP_NOT_FOUND, RCP_BAD_METHOD, RCP_NOT_ACCEPTABLE, RCP_PROXY_AUTH, RCP_CLIENT_TIMEOUT, RCP_CONFLICT, RCP_GONE, RCP_LENGTH_REQUIRED, RCP_PRECON_FAILED, RCP_ENTITY_TOO_LARGE, RCP_REQ_TOO_LONG, RCP_UNSUPPORTED_TYPE, RCP_INTERNAL_ERROR = 500, RCP_NOT_IMPLEMENTED, RCP_BAD_GATEWAY, RCP_UNAVAILABLE, RCP_GATEWAY_TIMEOUT, RCP_VERSION } | 请求响应的状态码。 |
| Rcp_DebugEvent { RCP_DEBUG_EVENT_TEXT, RCP_DEBUG_EVENT_HEADER_IN, RCP_DEBUG_EVENT_HEADER_OUT, RCP_DEBUG_EVENT_DATA_IN, RCP_DEBUG_EVENT_DATA_OUT, RCP_DEBUG_EVENT_SSL_DATA_IN, RCP_DEBUG_EVENT_SSL_DATA_OUT } | 描述调试信息的事件类型。 |
| Rcp_SessionType { RCP_SESSION_TYPE_HTTP = 0, RCP_SESSION_TYPE_MAX = 100 } | 会话类型。 |
| RCP_QuicIpResolve {RCP_QUIC_IP_RESOLVE_WHATEVER = 0, RCP_QUIC_IP_RESOLVE_V4, RCP_QUIC_IP_RESOLVE_V6} | 请求DNS解析时使用的IP解析类型。 |
| Rcp_QuicConnOpt { RCP_QUIC_CONN_IP_ADDRESS = 0, RCP_QUIC_CONN_IP_RESOLVE, RCP_QUIC_CONN_DNS_FUNCTION, RCP_QUIC_CONN_ON_CONNECTED_FUNCTION, RCP_QUIC_CONN_ON_ERROR_FUNCTION, RCP_QUIC_CONN_ON_CLOSED_FUNCTION, RCP_QUIC_CONN_STREAM_INBOUND_FUNCTION, RCP_QUIC_CONN_CONNECT_TIMEOUT_MS, RCP_QUIC_CONN_IDLE_TIMEOUT_MS, RCP_QUIC_TLS_CERT_AUTHORITY_FUNCTION = 1000, RCP_QUIC_TLS_CERT_AUTHORITY_CONTENT, RCP_QUIC_TLS_SESSION_TICKET_UPDATE_FUNCTION, RCP_QUIC_TLS_SESSION_TICKET_CONTENT, RCP_QUIC_TP_INITIAL_MAX_BIDIRECTIONAL_STREAMS = 2000, RCP_QUIC_TP_INITIAL_MAX_DATA, RCP_QUIC_TP_INITIAL_MAX_STREAMDATA_BIDIRECTIONAL_LOCAL, RCP_QUIC_TP_INITIAL_MAX_STREAMDATA_BIDIRECTIONAL_REMOTE, RCP_QUIC_TP_INITIAL_MAX_STREAMDATA_UNIDIRECTIONAL, RCP_QUIC_TP_INITIAL_MAX_UNIDIRECTIONAL_STREAMS} | quic连接选项类型。 |
| Rcp_QuicStreamOpt { RCP_QUIC_STREAM_EVENT_FUNCTION = 0, RCP_QUIC_STREAM_DATA_FUNCTION, RCP_QUIC_INBOUND_STREAM_USER_OBJECT, RCP_QUIC_STREAM_SND_BUFFER_SIZE_KB} | quic连接中配置流选项。 |
| Rcp_QuicConnInfo { RCP_INFO_CONN_GET_LOCALADDR = 0, RCP_INFO_CONN_GET_PEERADDR, RCP_INFO_CONN_DNS_TIME_MS, RCP_INFO_CONN_CONNECT_TIME_MS, RCP_INFO_CONN_SCID, RCP_INFO_CONN_DCID } | quic连接中的信息类型。 |
| Rcp_QuicStreamInfo { RCP_INFO_STREAM_SND_BUFFER_SIZE_KB = 0 } | quic流中的信息类型。 |
| Rcp_QuicErrorCode { RCP_QUIC_ERROR_CODE_SUCCESS, RCP_QUIC_PERMISSION_DENIED, RCP_QUIC_ERROR_CODE_FAILED, RCP_QUIC_ERROR_CODE_INVALID_PARAM, RCP_QUIC_ERROR_CODE_INVALID_STATE, RCP_QUIC_ERROR_CODE_OUT_OF_MEM, RCP_QUIC_ERROR_CODE_CLOSE_FROM_PEER, RCP_QUIC_ERROR_CODE_HANDSHAKE_TIMEOUT, RCP_QUIC_ERROR_CODE_NETWORK_IDLE_TIMEOUT, RCP_QUIC_ERROR_INVALID_FRAME, RCP_QUIC_ERROR_CODE_SEND_PENDING, RCP_QUIC_ERROR_CODE_FINALIZE_PENDING, RCP_QUIC_ERROR_CODE_NETWORK_UNREACHABLE, RCP_QUIC_ERROR_CODE_ENCRYPT_ERROR, RCP_QUIC_ERROR_CODE_BUFFER_TOO_SMALL, RCP_QUIC_ERROR_CODE_EAGAIN, RCP_QUIC_ERROR_CODE_STREAM_CLOSED, RCP_QUIC_ERROR_CODE_STREAM_RESET_RECEIVED, RCP_QUIC_ERROR_CODE_STREAM_STOP_SENDING_RECEIVED } | quic请求中可能出现的错误码。 |
| Rcp_QuicStreamDirection { RCP_QUIC_STREAM_BIDI = 0, RCP_QUIC_STREAM_UNI } | quic流的方向类型。 |
| Rcp_QuicStreamShutdown { RCP_QUIC_STREAM_SHUTDOWN_READ = 1, RCP_QUIC_STREAM_SHUTDOWN_WRITE = 2 } | quic流的关闭操作的类型。用于指定关闭流的读或写方向。 |
 
 
  

#### 函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| Rcp_Form * HMS_Rcp_CreateForm (void) | 创建一个简单表单。 |
| void HMS_Rcp_DestroyForm (Rcp_Form *form) | 销毁一个简单表单。 |
| uint32_t HMS_Rcp_SetFormValue (Rcp_Form *form, const char *key, const Rcp_FormFieldValue *value) | 设置简单表单的键值对。 |
| Rcp_FormFieldValue * HMS_Rcp_GetFormValue (Rcp_Form *form, const char *key) | 通过键获取一个简单表单的对应值。 |
| Rcp_MultipartForm * HMS_Rcp_CreateMultipartForm (void) | 创建一个多部分表单。 |
| void HMS_Rcp_DestroyMultipartForm (Rcp_MultipartForm *multipartForm) | 销毁一个多部分表单。 |
| uint32_t HMS_Rcp_SetMultipartFormValue (Rcp_MultipartForm *multipartForm, const char *key, const Rcp_MultipartFormFieldValue *value) | 设置多部分表单的键值对。 |
| Rcp_MultipartFormFieldValue * HMS_Rcp_GetMultipartFormValue (Rcp_MultipartForm *multipartForm, const char *key) | 通过键获取多部分表单的值。 |
| uint32_t HMS_Rcp_SetFormOrder (Rcp_Form *form, Rcp_FormOrder order) | 设置Form表单的键值对发送顺序。 |
| uint32_t HMS_Rcp_SetMultipartFormOrder (Rcp_MultipartForm *multipartForm, Rcp_FormOrder order) | 设置MultipartForm表单的键值对发送顺序。 |
| Rcp_Headers * HMS_Rcp_CreateHeaders (void) | 为请求或响应创建标头。 |
| void HMS_Rcp_DestroyHeaders (Rcp_Headers *headers) | 销毁请求或响应的标头。 |
| uint32_t HMS_Rcp_SetHeaderValue (Rcp_Headers *headers, const char *name, const char *value) | 设置请求或响应头的键值对。 |
| Rcp_HeaderValue * HMS_Rcp_GetHeaderValue (Rcp_Headers *headers, const char *name) | 通过键获取请求或响应头的值。 |
| Rcp_HeaderEntry * HMS_Rcp_GetHeaderEntries (Rcp_Headers *headers) | 获取请求或响应头的所有键值对。 |
| void HMS_Rcp_DestroyHeaderEntries (Rcp_HeaderEntry *headerEntry) | 销毁HMS_Rcp_GetHeaderEntries中获取的所有键值对。 |
| Rcp_Request * HMS_Rcp_CreateRequest (const char *url) | 创建请求。 |
| void HMS_Rcp_DestroyRequest (Rcp_Request *request) | 销毁请求。 |
| Rcp_RequestCookies * HMS_Rcp_CreateRequestCookies (void) | 创建空的请求Cookie。 |
| void HMS_Rcp_DestroyRequestCookies (Rcp_RequestCookies *cookies) | 销毁请求Cookie。 |
| uint32_t HMS_Rcp_SetRequestCookieValue (Rcp_RequestCookies *cookies, const char *name, const char *value) | 设置请求Cookie。 |
| char * HMS_Rcp_GetRequestCookieValue (Rcp_RequestCookies *cookies, const char *name) | 通过名称获取请求Cookie的值。 |
| Rcp_RequestCookieEntry * HMS_Rcp_GetRequestCookieEntries (Rcp_RequestCookies *cookies) | 获取请求Cookie中的所有键值对。 |
| void HMS_Rcp_DestroyRequestCookieEntries (Rcp_RequestCookieEntry *cookieEntry) | 销毁从HMS_Rcp_GetRequestCookieValue获取的所有与请求Cookie相关的键值对。 |
| const char * HMS_Rcp_GetResponseCookieAttrValue (Rcp_CookieAttributes *cookieAttributes, const char *name) | 通过名称获取Cookie属性的值。 |
| Rcp_CookieAttributeEntry * HMS_Rcp_GetResponseCookieAttrEntries (Rcp_CookieAttributes *cookieAttributes) | 在Rcp_CookieAttributes中获取所有响应Cookie属性。 |
| void HMS_Rcp_DestroyResponseCookieAttrEntries (Rcp_CookieAttributeEntry *entries) | 销毁响应Cookie属性。 |
| uint32_t HMS_Rcp_CallNextRequestHandler (Rcp_Request *request, const Rcp_RequestHandler *next, const Rcp_ResponseCallbackObject *responseCallback) | 在拦截器Rcp_Interceptor的函数中可以调用下一个拦截器或defaultHandler。 |
| Rcp_Response * HMS_Rcp_CallNextSyncRequestHandler (Rcp_Request *request, const Rcp_SyncRequestHandler *next, uint32_t *errCode) | 在拦截器Rcp_SyncInterceptor的函数中可以调用下一个拦截器或默认处理器。 |
| Rcp_Session * HMS_Rcp_CreateSession (const Rcp_SessionConfiguration *configuration, uint32_t *errCode) | 创建会话。 |
| const char * HMS_Rcp_GetSessionId (Rcp_Session *session) | 获取会话ID。 |
| const Rcp_SessionConfiguration * HMS_Rcp_GetSessionConfiguration (Rcp_Session *session) | 获取会话配置。 |
| Rcp_Response * HMS_Rcp_FetchSync (Rcp_Session *session, Rcp_Request *request, uint32_t *errCode) | 发送同步请求并获取响应。 |
| uint32_t HMS_Rcp_Fetch (Rcp_Session *session, Rcp_Request *request, const Rcp_ResponseCallbackObject *responseCallback) | 发送异步请求并获取响应。 |
| uint32_t HMS_Rcp_CancelRequest (Rcp_Session *session, const Rcp_Request *request) | 取消一个请求。 |
| uint32_t HMS_Rcp_CancelSession (Rcp_Session *session) | 取消会话。 |
| uint32_t HMS_Rcp_CloseSession (Rcp_Session **session) | 关闭会话。 |
| uint32_t HMS_Rcp_SetRequestOnBinaryDataRecvCallback (Rcp_Request *request, Rcp_OnBinaryReceiveCallback onBinaryReceiveCallback) | 为请求设置流式接收二进制数据的回调函数。该回调函数与Rcp_Configuration中配置的Rcp_OnDataReceiveCallback功能一致。设置后将替换在Rcp_Configuration中配置的Rcp_OnDataReceiveCallback。 |
| uint32_t HMS_Rcp_SetRequestOnStatusCodeReceiveCallback (Rcp_Request *request, Rcp_OnStatusCodeReceiveCallback onStatusCodeReceiveCallback) | 为请求设置响应状态码接收回调函数。 |
| uint32_t HMS_Rcp_GetDefaultSession (Rcp_Session **session) | 获取默认会话。 |
| uint32_t HMS_Rcp_SetRequestConnectOnly (Rcp_Request *request, bool connectOnly) | 设置请求仅用于建立连接，而不进行数据传输。 |
| uint32_t HMS_Rcp_SetRequestGetDataCallback (Rcp_Request *request, Rcp_OnGetDataCallback getDataCallback) | 设置获取数据的回调函数。 |
| Rcp_QuicErrorCode HMS_Rcp_QuicConnSetOpt (Rcp_QuicConn *conn, Rcp_QuicConnOpt opt, const void *optVal, uint32_t optLen) | 设置quic连接选项。用于设置连接的各种参数和回调函数。 |
| Rcp_QuicErrorCode HMS_Rcp_QuicConnGetInfo (Rcp_QuicConn *conn, Rcp_QuicConnInfo info, void *infoVal, uint32_t *infoLen) | 获取quic连接信息。用于建立quic连接成功后，获取相关quic连接信息。 |
| Rcp_QuicErrorCode HMS_Rcp_QuicStreamSetOpt (Rcp_QuicConn *conn, uint64_t streamId, Rcp_QuicStreamOpt opt, const void *optVal, uint32_t optLen) | 设置quic连接中流的参数。 |
| Rcp_QuicErrorCode HMS_Rcp_QuicStreamGetInfo (Rcp_QuicConn *conn, uint64_t streamId, Rcp_QuicStreamInfo info, void *infoVal, uint32_t *infoLen) | 获取quic连接中streamId对应流的信息。 |
| Rcp_QuicSession * HMS_Rcp_QuicCreateSession () | 创建quic会话对象。一个quic会话中可以管理多个quic连接。 |
| void HMS_Rcp_QuicDestroySession (Rcp_QuicSession *session) | 销毁quic会话对象。释放quic会话资源。 |
| Rcp_QuicConn * HMS_Rcp_QuicConnCreate (char *alpn, void *userObject) | 创建quic连接对象。 |
| Rcp_QuicErrorCode HMS_Rcp_QuicConnConnect (Rcp_QuicSession *session, Rcp_QuicConn *conn, const char *serverName, uint16_t port) | 发起quic连接握手。握手结果通过连接回调通知。 |
| Rcp_QuicErrorCode HMS_Rcp_QuicConnDestroy (Rcp_QuicConn *conn) | 销毁quic连接对象。释放quic连接资源。 |
| Rcp_QuicErrorCode HMS_Rcp_QuicConnStreamOpen (Rcp_QuicConn *conn, Rcp_QuicStreamDirection direction, uint64_t *streamId, void *userObject) | 在quic连接中打开一个quic流。quic连接建立成功后才能打开quic流。 |
| Rcp_QuicErrorCode HMS_Rcp_QuicConnStreamSend (Rcp_QuicConn *conn, uint64_t streamId, const Rcp_QuicIoVec *ioVec, uint32_t ioVecCount, bool fin) | 通过quic流发送数据。 |
| Rcp_QuicErrorCode HMS_Rcp_QuicConnStreamWantRead (Rcp_QuicConn *conn, uint64_t streamId) | 触发quic流数据读取回调。 |
| Rcp_QuicErrorCode HMS_Rcp_QuicConnStreamReset (Rcp_QuicConn *conn, uint64_t streamId, uint64_t appErr) | 重置quic流。立即终止流，丢弃所有未发送和已接收的数据。 |
| Rcp_QuicErrorCode HMS_Rcp_QuicConnStreamShutdown (Rcp_QuicConn *conn, uint64_t streamId, Rcp_QuicStreamShutdown flag, uint64_t appErr) | 关闭连接中streamId对应流的读或写。 |
| Rcp_QuicStreamDirection HMS_Rcp_QuicStreamGetDirection (uint64_t streamId) | 获取quic流的方向类型。 |
| void HMS_Rcp_QuicFreeSlist (Rcp_QuicSlist *list) | 释放Rcp_QuicSlist链表，释放链表中的所有节点和数据。 |
 
 
  

#### 宏定义说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### RCP_HOST_MAX_LEN

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
#define RCP_HOST_MAX_LEN   256
```
 
**描述**
 
主机名的最大长度。
 
**起始版本：** 5.0.0(12)
 
  

#### RCP_IP_MAX_LEN

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
#define RCP_IP_MAX_LEN   40
```
 
**描述**
 
IP地址的最大长度。
 
**起始版本：** 5.0.0(12)
 
  

#### RCP_MAX_CONTENT_TYPE_LEN

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
#define RCP_MAX_CONTENT_TYPE_LEN   64
```
 
**描述**
 
内容类型最大长度。
 
**起始版本：** 5.0.0(12)
 
  

#### RCP_MAX_FILENAME_LEN

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
#define RCP_MAX_FILENAME_LEN   128
```
 
**描述**
 
文件名最大长度。
 
**起始版本：** 5.0.0(12)
 
  

#### RCP_MAX_PATH_LEN

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
#define RCP_MAX_PATH_LEN   128
```
 
**描述**
 
路径的最大长度。
 
**起始版本：** 5.0.0(12)
 
  

#### RCP_MAX_REQUEST_ID_LEN

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
#define RCP_MAX_REQUEST_ID_LEN   32
```
 
**描述**
 
请求ID的最大长度。
 
**起始版本：** 5.0.0(12)
 
  

#### RCP_METHOD_DELETE

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
#define RCP_METHOD_DELETE   "DELETE"
```
 
**描述**
 
HTTP delete方法。
 
**起始版本：** 5.0.0(12)
 
  

#### RCP_METHOD_GET

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
#define RCP_METHOD_GET   "GET"
```
 
**描述**
 
HTTP get方法。
 
**起始版本：** 5.0.0(12)
 
  

#### RCP_METHOD_HEAD

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
#define RCP_METHOD_HEAD   "HEAD"
```
 
**描述**
 
HTTP head方法。
 
**起始版本：** 5.0.0(12)
 
  

#### RCP_METHOD_OPTIONS

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
#define RCP_METHOD_OPTIONS   "OPTIONS"
```
 
**描述**
 
HTTP options方法。
 
**起始版本：** 5.0.0(12)
 
  

#### RCP_METHOD_PATCH

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
#define RCP_METHOD_PATCH   "PATCH"
```
 
**描述**
 
HTTP patch方法。
 
**起始版本：** 5.0.0(12)
 
  

#### RCP_METHOD_POST

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
#define RCP_METHOD_POST   "POST"
```
 
**描述**
 
HTTP post方法。
 
**起始版本：** 5.0.0(12)
 
  

#### RCP_METHOD_PUT

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
#define RCP_METHOD_PUT   "PUT"
```
 
**描述**
 
HTTP put方法。
 
**起始版本：** 5.0.0(12)
 
  

#### RCP_METHOD_TRACE

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
#define RCP_METHOD_TRACE   "TRACE"
```
 
**描述**
 
HTTP trace方法。
 
**起始版本：** 5.0.0(12)
 
  

#### RCP_QUIC_IP_MAX_LEN

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
#define RCP_QUIC_IP_MAX_LEN   40
```
 
**描述**
 
quic连接的IP地址的最大长度。
 
**起始版本：** 26.0.0
 
  

#### 类型定义说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### Rcp_AuthenticationType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef enum Rcp_AuthenticationType Rcp_AuthenticationType
```
 
**描述**
 
枚举类型。服务器的身份验证类型。如果未设置，请与服务器协商。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_Buffer

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_Buffer Rcp_Buffer
```
 
**描述**
 
文本存储结构。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_CertificateAuthority

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_CertificateAuthority Rcp_CertificateAuthority
```
 
**描述**
 
用于验证远程服务器标识的证书颁发机构（CA）。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_CertType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef enum Rcp_CertType Rcp_CertType
```
 
**描述**
 
客户端证书类型。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_ClientCertificate

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_ClientCertificate Rcp_ClientCertificate
```
 
**描述**
 
发送到远程服务器的客户端证书，远程服务器将使用它来验证客户端的标识。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_Configuration

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_Configuration Rcp_Configuration
```
 
**描述**
 
请求配置。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_ConnectionConfiguration

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_ConnectionConfiguration Rcp_ConnectionConfiguration
```
 
**描述**
 
连接配置。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_ContentOrPathOrCallback

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_ContentOrPathOrCallback Rcp_ContentOrPathOrCallback
```
 
**描述**
 
[Rcp_FormFieldFileValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_field_file_value)中使用的简单表单数据字段值。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_ContentOrPathOrCallbackType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef enum Rcp_ContentOrPathOrCallbackType Rcp_ContentOrPathOrCallbackType
```
 
**描述**
 
回调的内容、路径或类型。用于区分[Rcp_ContentOrPathOrCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___content_or_path_or_callback)中使用的数据。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_ContentType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef enum Rcp_ContentType Rcp_ContentType
```
 
**描述**
 
内容类型。用于区分[Rcp_RequestContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request_content)中使用的数据。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_CookieAttributeEntry

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_CookieAttributeEntry Rcp_CookieAttributeEntry
```
 
**描述**
 
响应Cookie属性条目。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_CookieAttributes

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_CookieAttributes Rcp_CookieAttributes
```
 
**描述**
 
描述[Rcp_Response](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response)中Cookie属性的类型。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_Credential

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_Credential Rcp_Credential
```
 
**描述**
 
服务器身份验证中使用的身份验证凭据，包括用户名和密码。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_DebugEvent

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef enum Rcp_DebugEvent Rcp_DebugEvent
```
 
**描述**
 
描述调试信息的事件类型。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_DebugInfo

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_DebugInfo Rcp_DebugInfo
```
 
**描述**
 
描述存储在[Rcp_Response](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response)中的调试信息的结构。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_DnsConfiguration

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_DnsConfiguration Rcp_DnsConfiguration
```
 
**描述**
 
DNS解析配置。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_DnsOverHttps

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_DnsOverHttps Rcp_DnsOverHttps
```
 
**描述**
 
如果设置了HTTPS上的DNS配置，则首选由DOH DNS服务器解析的地址。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_DnsRule

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_DnsRule Rcp_DnsRule
```
 
**描述**
 
DNS规则配置。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_DnsRuleType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef enum Rcp_DnsRuleType Rcp_DnsRuleType
```
 
**描述**
 
DNS规则类型。用于区分[Rcp_DnsRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_rule)中使用的DNS规则类型。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_DnsServers

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_DnsServers Rcp_DnsServers
```
 
**描述**
 
DNS服务器。[Rcp_DnsConfiguration.dnsRules](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_configuration#dnsrules)中的类型之一。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_DynamicDnsRuleFunction

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef Rcp_IpAddress*(* Rcp_DynamicDnsRuleFunction) (const char *host, uint16_t port)
```
 
**描述**
 
一个可以根据主机名和端口直接返回IP地址的函数。用于动态DNS解析。
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| host | 主机名称。 |
| port | 端口号。 |
 
 
**返回：**
 
Rcp_IpAddress* 指向[Rcp_IpAddress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___ip_address)的指针。基于主机名和端口的IP地址。
 
  

#### Rcp_EventsHandler

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_EventsHandler Rcp_EventsHandler
```
 
**描述**
 
监听不同HTTP事件的回调函数。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_ExclusionFunction

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef bool(* Rcp_ExclusionFunction) (const char *url)
```
 
**描述**
 
判断host是否使用代理的函数指针。
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| url | 请求的URL。 |
 
 
**返回：**
 
bool 返回是否使用代理。true代表使用，false代表不使用。
 
  

#### Rcp_Exclusions

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_Exclusions Rcp_Exclusions
```
 
**描述**
 
代理配置中用于过滤不使用代理的URLs。
 
如果[Rcp_Request.url](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request#url)匹配[Rcp_Exclusions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___exclusions)规则，则[Rcp_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request)不会使用代理。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_ExclusionsValueType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef enum Rcp_ExclusionsValueType Rcp_ExclusionsValueType
```
 
**描述**
 
代理排除中使用的数据类型。用于区分[Rcp_Exclusions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___exclusions)中使用的数据。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_Form

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_Form Rcp_Form
```
 
**描述**
 
简单表单。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_FormFieldFileValue

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_FormFieldFileValue Rcp_FormFieldFileValue
```
 
**描述**
 
表单字段文件值。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_FormFieldValue

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_FormFieldValue Rcp_FormFieldValue
```
 
**描述**
 
简单表单数据字段值，参见[Rcp_Form](#rcp_form)和[Rcp_MultipartFormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___multipart_form_field_value)。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_FormValueType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef enum Rcp_FormValueType Rcp_FormValueType
```
 
**描述**
 
表单值类型。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_GetDataCallback

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef int(* Rcp_GetDataCallback) (char *out, uint32_t size)
```
 
**描述**
 
通过回调函数获取数据。当API需要将数据的下一部分发送到服务器时，将调用此回调。
 
该回调可能使用在[Rcp_FormFieldFileValue.contentOrPathOrCb](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_field_file_value#contentorpathorcb)和[Rcp_RequestContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request_content)中。
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| out | 输出的数据 |
| size | 数据大小 |
 
 
**返回：**
 
int 返回值为-1表示错误，返回值0表示停止传输。
 
  

#### Rcp_HeaderEntry

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_HeaderEntry Rcp_HeaderEntry
```
 
**描述**
 
请求或响应的标头的所有键值对。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_Headers

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_Headers Rcp_Headers
```
 
**描述**
 
请求或响应的标头。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_HeaderValue

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_HeaderValue Rcp_HeaderValue
```
 
**描述**
 
请求或响应的标头映射的值类型。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_InfoToCollect

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_InfoToCollect Rcp_InfoToCollect
```
 
**描述**
 
指定要收集的请求处理事件。可以通过响应对象检查收集的事件。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_Interceptor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_Interceptor Rcp_Interceptor
```
 
**描述**
 
异步拦截器。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_InterceptorArray

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_InterceptorArray Rcp_InterceptorArray
```
 
**描述**
 
异步拦截器数组。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_IpAddress

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_IpAddress Rcp_IpAddress
```
 
**描述**
 
指定静态DNS规则使用的IP地址组。用于[Rcp_StaticDnsRuleItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___static_dns_rule_item)。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_IpAndPort

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_IpAndPort Rcp_IpAndPort
```
 
**描述**
 
该接口用在[Rcp_DnsServers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_servers)中，表示一个DNS服务器的地址和端口。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_MultipartForm

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_MultipartForm Rcp_MultipartForm
```
 
**描述**
 
多部分表单。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_MultipartFormFieldValue

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_MultipartFormFieldValue Rcp_MultipartFormFieldValue
```
 
**描述**
 
多部分表单域值，在[Rcp_MultipartForm](#rcp_multipartform)中使用。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_MultipartValueType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef enum Rcp_MultipartValueType Rcp_MultipartValueType
```
 
**描述**
 
多部分值类型。用于区分[Rcp_MultipartFormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___multipart_form_field_value)中使用的数据。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_OnDataReceiveCallback

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_OnDataReceiveCallback Rcp_OnDataReceiveCallback
```
 
**描述**
 
接收到数据时回调。[Rcp_EventsHandler](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___events_handler)中的配置。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_OnDataReceiveCallbackFunc

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef size_t(* Rcp_OnDataReceiveCallbackFunc) (void *usrObject, const char *data)
```
 
**描述**
 
接收到响应正文时调用的回调函数。
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| usrObject | 用户定义的对象。 |
| data | 响应体。 |
 
 
**返回：**
 
size_t 响应体的长度。
 
  

#### Rcp_OnBinaryReceiveCallback

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_OnBinaryReceiveCallback Rcp_OnBinaryReceiveCallback
```
 
**描述**
 
响应的二进制数据接收回调函数。
 
**起始版本：** 5.0.1(13)
 
  

#### Rcp_OnBinaryReceiveCallbackFunc

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef size_t(* Rcp_OnBinaryReceiveCallbackFunc) (void *usrObject, Rcp_Buffer *buffer)
```
 
**描述**
 
接收到响应正文时调用的二进制回调函数。其回调点与[Rcp_Configuration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___configuration)中配置的[Rcp_OnDataReceiveCallback](#rcp_ondatareceivecallback)一致。设置后其回调函数会替换在[Rcp_Configuration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___configuration)中配置的[Rcp_OnDataReceiveCallback](#rcp_ondatareceivecallback)，功能上能够涵盖[Rcp_OnDataReceiveCallback](#rcp_ondatareceivecallback)的字符数据接收获取功能。
 
**起始版本：** 5.0.1(13)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| usrObject | 用户定义的对象。 |
| buffer | 响应体的二进制数据。 |
 
 
**返回：**
 
size_t 响应体二进制数据的长度。
 
  

#### Rcp_OnStatusCodeReceiveCallback

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_OnStatusCodeReceiveCallback Rcp_OnStatusCodeReceiveCallback
```
 
**描述**
 
用于接收响应状态码的回调函数。
 
**起始版本：** 6.0.1(21)
 
  

#### Rcp_OnStatusCodeReceiveCallbackFunc

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef void (*Rcp_OnStatusCodeReceiveCallbackFunc) (void *usrObject, uint32_t statusCode)
```
 
**描述**
 
接收到响应状态码时调用的回调函数。
 
**起始版本：** 6.0.1(21)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| usrObject | 用户定义的对象。 |
| statusCode | 响应状态码。 |
 
 
  

#### Rcp_OnHeaderReceiveCallback

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_OnHeaderReceiveCallback Rcp_OnHeaderReceiveCallback
```
 
**描述**
 
[Rcp_EventsHandler](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___events_handler)中配置的接收到的header的回调配置。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_OnHeaderReceiveCallbackFunc

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef void(* Rcp_OnHeaderReceiveCallbackFunc) (void *usrObject, Rcp_Headers *headers)
```
 
**描述**
 
收到所有请求时调用的回调。
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| usrObject | 用户定义的对象。 |
| headers | 接收到的请求头，指向Rcp_Headers的指针。 |
 
 
  

#### Rcp_OnProgressCallback

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_OnProgressCallback Rcp_OnProgressCallback
```
 
**描述**
 
收发时回调配置，在[Rcp_EventsHandler](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___events_handler)中配置。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_OnProgressCallbackFunc

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef void(* Rcp_OnProgressCallbackFunc) (void *usrObject, uint64_t totalSize, uint64_t transferredSize)
```
 
**描述**
 
请求/响应数据传输过程中调用的回调函数。
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| usrObject | 用户定义的对象。 |
| totalSize | 数据总大小。 |
| transferredSize | 已传输的数据大小。 |
 
 
  

#### Rcp_OnVoidCallback

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_OnVoidCallback Rcp_OnVoidCallback
```
 
**描述**
 
在[Rcp_EventsHandler](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___events_handler)中配置的数据结束或已取消事件的回调配置。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_OnVoidCallbackFunc

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef void(* Rcp_OnVoidCallbackFunc) (void *usrObject)
```
 
**描述**
 
请求的DataEnd或Canceled事件回调的回调函数。
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| usrObject | 用户定义的对象。 |
 
 
  

#### Rcp_PathPreference

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef enum Rcp_PathPreference Rcp_PathPreference
```
 
**描述**
 
请求路径首选项。
 
调用者的建议，最终由系统决定使用哪个路径。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_ProxyConfiguration

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_ProxyConfiguration Rcp_ProxyConfiguration
```
 
**描述**
 
代理配置。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_ProxyTunnelMode

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef enum Rcp_ProxyTunnelMode Rcp_ProxyTunnelMode
```
 
**描述**
 
用于控制何时创建代理隧道。 隧道或隧道传输意味着向代理发送HTTP CONNECT请求，要求它连接到特定端口号上的远程主机，然后流量只是通过代理。'auto'表示为HTTPS创建隧道，而不是为HTTP创建隧道。“always”表示始终创建隧道。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_ProxyType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef enum Rcp_ProxyType Rcp_ProxyType
```
 
**描述**
 
代理类型。用于区分不同的代理配置。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_RemoteValidationType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef enum Rcp_RemoteValidationType Rcp_RemoteValidationType
```
 
**描述**
 
远程验证类型。
 
用于区分验证远程服务器身份的CA，在[Rcp_SecurityConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___security_configuration)中描述。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_Request

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_Request Rcp_Request
```
 
**描述**
 
网络请求。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_FormOrder

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_FormOrder Rcp_FormOrder
```
 
**描述**
 
表单键值对发送顺序。
 
**起始版本：** 26.0.0
 
  

#### Rcp_RequestContent

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_RequestContent Rcp_RequestContent
```
 
**描述**
 
请求的内容。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_RequestCookieEntry

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_RequestCookieEntry Rcp_RequestCookieEntry
```
 
**描述**
 
描述请求的所有Cookie键值对。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_RequestCookies

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_RequestCookies Rcp_RequestCookies
```
 
**描述**
 
请求Cookie。
 
允许你在一个对象中指定你需要的所有Cookies，例如：{'name1'：'value1'，'name2'：'value2'}。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_RequestHandler

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_RequestHandler Rcp_RequestHandler
```
 
**描述**
 
与[Rcp_Interceptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___interceptor)关联的异步处理器。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_Response

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_Response Rcp_Response
```
 
**描述**
 
网络请求的响应。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_ResponseCallback

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef void(* Rcp_ResponseCallback) (void *usrCtx, Rcp_Response *response, uint32_t errCode)
```
 
**描述**
 
响应回调函数指针。
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| usrCtx | 用户上下文。 |
| response | 请求所生成的响应。指向Rcp_Response的指针。 |
| errCode | [out] 表示常见的错误代码。 0：成功。 1007900001：不支持的协议。 1007900003：URL使用了错误/非法的格式或缺少URL。 1007900005：无法解析代理名称。 1007900006：无法解析主机名。 1007900007：无法连接到服务器。 1007900008：异常的服务器回复。 1007900009：对远程资源的访问被拒绝。 1007900016：HTTP2框架层中的错误。 1007900018：已传输部分文件。 1007900025：上载失败。 1007900026：无法从文件/应用程序中打开/读取本地数据。 1007900027：内存不足。 1007900028：已达到超时。 1007900047：重定向数达到最大数量。 1007900052：服务器没有返回任何内容（没有标头，没有数据）。 1007900055：向对等方发送数据失败。 1007900056：从对等方接收数据时失败。 1007900058：本地SSL证书有问题。 1007900059：无法使用指定的SSL密钥。 1007900060：SSL对等证书或SSH远程密钥不正常。 1007900061：无法识别或错误的HTTP内容或传输编码。 1007900063：超过了最大文件大小。 1007900070：磁盘已满或分配超出。 1007900073：远程文件已存在。 1007900077：SSL CA证书有问题 (路径？ 访问权限？)。 1007900078：找不到远程文件。 1007900992：请求已取消。 1007900993：会话已关闭或无效。 1007900094：身份验证函数返回了错误。 1007900201：禁止明文传输。从6.1.0(23)起新增支持此错误码。 1007900995：获取系统代理失败。 1007900996：代理类型不受支持。 1007900997：无效的内容类型。 1007900998：方法不受支持。 1007900999：内部错误。 Others：1007900000 + CURL_ERROR_CODE。 更多常见的错误码，请参见curl错误码。 |
 
 
  

#### Rcp_ResponseCallbackObject

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_ResponseCallbackObject Rcp_ResponseCallbackObject
```
 
**描述**
 
响应回调结构体。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_ResponseCookies

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_ResponseCookies Rcp_ResponseCookies
```
 
**描述**
 
响应Cookie。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_SecurityConfiguration

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_SecurityConfiguration Rcp_SecurityConfiguration
```
 
**描述**
 
请求的安全配置。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_ServerAuthentication

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_ServerAuthentication Rcp_ServerAuthentication
```
 
**描述**
 
服务器身份验证。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_Session

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_Session Rcp_Session
```
 
**描述**
 
会话。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_SessionConfiguration

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_SessionConfiguration Rcp_SessionConfiguration
```
 
**描述**
 
会话配置。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_SessionListener

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_SessionListener Rcp_SessionListener
```
 
**描述**
 
关闭或取消会话事件的回调函数。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_SessionType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef enum Rcp_SessionType Rcp_SessionType
```
 
**描述**
 
会话类型。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_StaticDnsRule

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_StaticDnsRule Rcp_StaticDnsRule
```
 
**描述**
 
静态DNS规则。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_StaticDnsRuleItem

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_StaticDnsRuleItem Rcp_StaticDnsRuleItem
```
 
**描述**
 
描述单个静态DNS规则。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_StatusCode

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef enum Rcp_StatusCode Rcp_StatusCode
```
 
**描述**
 
请求响应的状态码。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_SyncInterceptor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_SyncInterceptor Rcp_SyncInterceptor
```
 
**描述**
 
同步拦截器。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_SyncInterceptorArray

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_SyncInterceptorArray Rcp_SyncInterceptorArray
```
 
**描述**
 
同步拦截器数组。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_SyncRequestHandler

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_SyncRequestHandler Rcp_SyncRequestHandler
```
 
**描述**
 
与[Rcp_SyncInterceptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___sync_interceptor)关联的同步处理器。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_TimeInfo

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_TimeInfo Rcp_TimeInfo
```
 
**描述**
 
响应计时信息。
 
它将在[Rcp_Response.timeInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response#timeinfo)中被收集，[Rcp_TracingConfiguration.collectTimeInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___tracing_configuration#collecttimeinfo)决定是否收集它。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_Timeout

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_Timeout Rcp_Timeout
```
 
**描述**
 
请求的超时配置。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_TracingConfiguration

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_TracingConfiguration Rcp_TracingConfiguration
```
 
**描述**
 
请求追踪配置。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_TransferConfiguration

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_TransferConfiguration Rcp_TransferConfiguration
```
 
**描述**
 
传输配置。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_TransferRange

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_TransferRange Rcp_TransferRange
```
 
**描述**
 
HTTP传输范围。该设置将转换为HTTP Range标头。具有范围标头的HTTP请求要求服务器仅发送回HTTP响应的一部分。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_Urls

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_Urls Rcp_Urls
```
 
**描述**
 
URLs，用于确定主机是否正在使用代理。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_WebProxy

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_WebProxy Rcp_WebProxy
```
 
**描述**
 
自定义代理配置。
 
**起始版本：** 5.0.0(12)
 
  

#### Rcp_OnGetDataCallback

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_OnGetDataCallback  Rcp_OnGetDataCallback
```
 
**描述**
 
获取数据的回调。
 
**起始版本：** 26.0.0
 
  

#### Rcp_GetDataCallbackFunc

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef size_t(* Rcp_GetDataCallbackFunc) (void *userObject, uint8_t *outData, size_t size)
```
 
**描述**
 
获取数据的回调函数。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| userObject | 用户定义的对象。 |
| outData | 输出数据的缓冲区。 |
| size | 缓冲区长度。 |
 
 
**返回：**
 
size_t 发送的数据长度。
 
  

#### Rcp_QuicConn

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef void Rcp_QuicConn
```
 
**描述**
 
quic连接实例的类型。
 
**起始版本：** 26.0.0
 
  

#### Rcp_QuicSession

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef void Rcp_QuicSession
```
 
**描述**
 
quic会话的类型，可以管理多个连接实例。
 
**起始版本：** 26.0.0
 
  

#### Rcp_QuicSlist

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_QuicSlist Rcp_QuicSlist
```
 
**描述**
 
链表数据结构。
 
**起始版本：** 26.0.0
 
  

#### Rcp_QuicIpAddress

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_QuicIpAddress Rcp_QuicIpAddress
```
 
**描述**
 
用于存储IP地址的数据结构。
 
**起始版本：** 26.0.0
 
  

#### Rcp_QuicDynamicDnsRuleFunction

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef Rcp_QuicIpAddress (*Rcp_QuicDynamicDnsRuleFunction)(Rcp_QuicConn *conn, void *userObject, const char *host, uint16_t port)
```
 
**描述**
 
自定义DNS解析回调函数，根据主机名和端口返回IP地址。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| userObject | 用户定义的对象。 |
| host | 请求的主机名。 |
| port | 请求的端口号。 |
 
 
**返回：**
 
[Rcp_QuicIpAddress](#rcp_quicipaddress) 根据主机名和端口解析的IP地址。
 
  

#### Rcp_QuicIoVec

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_QuicIoVec Rcp_QuicIoVec
```
 
**描述**
 
用于存储二进制内容的数据结构。
 
**起始版本：** 26.0.0
 
  

#### Rcp_QuicStreamData

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Rcp_QuicStreamData Rcp_QuicStreamData
```
 
**描述**
 
quic连接中用于接收流式数据的存储结构。
 
**起始版本：** 26.0.0
 
  

#### Rcp_QuicConnectionOnCertAuthority

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef Rcp_QuicErrorCode (*Rcp_QuicConnectionOnCertAuthority)(Rcp_QuicConn *conn, void *userObject, const unsigned char *const *certs, const size_t *certLens, size_t certsCount)
```
 
**描述**
 
证书校验的回调函数。在quic建链时，用于自定义校验对端证书。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| userObject | 用户定义的对象。 |
| certs | X509证书数组（DER格式）。 |
| certLens | 每个证书的长度数组。 |
| certsCount | 证书数量。 |
 
 
**返回：**
 
[Rcp_QuicErrorCode](#rcp_quicerrorcode) ：自定义证书验证结果，RCP_QUIC_ERROR_CODE_SUCCESS为验证通过，其余返回值均为验证失败。
 
  

#### Rcp_QuicConnectionOnSessionTicketUpdate

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef void (*Rcp_QuicConnectionOnSessionTicketUpdate)(Rcp_QuicConn *conn, void *userObject, const char *sessionTicket, size_t length)
```
 
**描述**
 
quic会话票据更新回调函数。在quic会话中票据更新时触发，返回新的票据。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| userObject | 用户定义的对象。 |
| sessionTicket | quic会话票据内容。 |
| length | 会话票据长度。 |
 
 
  

#### Rcp_QuicConnectionOnConnected

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef void (*Rcp_QuicConnectionOnConnected)(Rcp_QuicConn *conn, void *userObject)
```
 
**描述**
 
quic连接成功回调函数。quic连接成功建立时触发该函数。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| userObject | 用户定义的对象。 |
 
 
  

#### Rcp_QuicConnectionOnError

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef void (*Rcp_QuicConnectionOnError)(Rcp_QuicConn *conn, void *userObject, Rcp_QuicErrorCode errCode, const char *errDetail)
```
 
**描述**
 
quic连接失败回调函数。quic连接建立失败时触发该函数，返回失败原因。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| userObject | 用户定义的对象。 |
| errCode | 建立quic连接失败错误码。 |
| errDetail | 错误详细信息。 |
 
 
  

#### Rcp_QuicConnectionOnClosed

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef void (*Rcp_QuicConnectionOnClosed)(Rcp_QuicConn *conn, void *userObject)
```
 
**描述**
 
quic连接关闭回调函数。quic连接关闭时触发，通知连接已关闭。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| userObject | 用户定义的对象。 |
 
 
  

#### Rcp_QuicConnectionOnStreamInbound

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef void (*Rcp_QuicConnectionOnStreamInbound)(Rcp_QuicConn *conn, void *userObject, uint64_t streamId)
```
 
**描述**
 
quic连接中入站流回调函数。当quic连接中对端创建流时触发，处理对端发起的流，设置流的选项和回调。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| userObject | 用户定义的对象。 |
| streamId | 入站流的ID。 |
 
 
  

#### Rcp_QuicStreamOnEvent

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef void (*Rcp_QuicStreamOnEvent)(Rcp_QuicConn *conn, void *userObject, uint64_t streamId, Rcp_QuicErrorCode errCode, const char *errDetail)
```
 
**描述**
 
quic连接中流事件回调函数。当quic连接中的流发生事件时触发，用于处理流的状态变化和错误。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| userObject | 用户定义的对象。 |
| streamId | 入站流的ID。 |
| errCode | 建立quic连接失败错误码。 |
| errDetail | 错误详细信息。 |
 
 
  

#### Rcp_QuicStreamOnReceiveData

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef uint64_t (*Rcp_QuicStreamOnReceiveData)(Rcp_QuicConn *conn, void *userObject, uint64_t streamId, const Rcp_QuicStreamData *streamData)
```
 
**描述**
 
quic连接中流数据接收回调函数。当quic连接中接收到流数据时触发，用于处理接收到的数据。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| userObject | 用户定义的对象。 |
| streamId | quic流的ID。 |
| streamData | quic流数据。 |
 
 
**返回：**
 
uint64_t ：quic流接收数据的字节数。
 
  

#### 枚举类型说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### Rcp_AuthenticationType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum Rcp_AuthenticationType
```
 
**描述**
 
枚举类型。服务器的身份验证类型。如果未设置，请与服务器协商。
 
**起始版本：** 5.0.0(12)
  
| 枚举值 | 描述 |
| --- | --- |
| RCP_AUTHENTICATION_AUTO | 自动 |
| RCP_AUTHENTICATION_BASIC | 基本类型 |
| RCP_AUTHENTICATION_NTLM | NTLM类型 |
| RCP_AUTHENTICATION_DIGEST | DIGEST类型 |
 
 
  

#### Rcp_CertType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum Rcp_CertType
```
 
**描述**
 
客户端证书类型。
 
**起始版本：** 5.0.0(12)
  
| 枚举值 | 描述 |
| --- | --- |
| RCP_CERT_PEM | PEM证书类型。 |
| RCP_CERT_DER | DER证书类型。 |
| RCP_CERT_P12 | P12证书类型。 |
 
 
  

#### Rcp_ContentOrPathOrCallbackType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum Rcp_ContentOrPathOrCallbackType
```
 
**描述**
 
回调的内容、路径或类型。用于区分[Rcp_ContentOrPathOrCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___content_or_path_or_callback)中使用的数据。
 
**起始版本：** 5.0.0(12)
  
| 枚举值 | 描述 |
| --- | --- |
| RCP_FILE_VALUE_TYPE_CONTENT | 表示内容类型。 |
| RCP_FILE_VALUE_TYPE_PATH | 表示路径类型。 |
| RCP_FILE_VALUE_TYPE_CALLBACK | 表示回调类型。 |
 
 
  

#### Rcp_ContentType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum Rcp_ContentType
```
 
**描述**
 
内容类型。用于区分[Rcp_RequestContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request_content)中使用的数据。
 
**起始版本：** 5.0.0(12)
  
| 枚举值 | 描述 |
| --- | --- |
| RCP_CONTENT_TYPE_STRING | 文本。 |
| RCP_CONTENT_TYPE_FORM | 表格。 |
| RCP_CONTENT_TYPE_MULTIPARTFORM | 多部分表格。 |
| RCP_CONTENT_TYPE_GETCALLBACK | 回调函数。 |
 
 
  

#### Rcp_DebugEvent

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum Rcp_DebugEvent
```
 
**描述**
 
描述调试信息的事件类型。
 
**起始版本：** 5.0.0(12)
  
| 枚举值 | 描述 |
| --- | --- |
| RCP_DEBUG_EVENT_TEXT | 文本事件。 |
| RCP_DEBUG_EVENT_HEADER_IN | 传入标头事件。 |
| RCP_DEBUG_EVENT_HEADER_OUT | 传出标头事件。 |
| RCP_DEBUG_EVENT_DATA_IN | 接收数据事件。 |
| RCP_DEBUG_EVENT_DATA_OUT | 外发数据事件。 |
| RCP_DEBUG_EVENT_SSL_DATA_IN | 传入SSL/TLS事件。 |
| RCP_DEBUG_EVENT_SSL_DATA_OUT | 传出SSL/TLS事件。 |
 
 
  

#### Rcp_DnsRuleType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum Rcp_DnsRuleType
```
 
**描述**
 
DNS规则类型。用于区分[Rcp_DnsRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_rule)中使用的DNS规则类型。
 
**起始版本：** 5.0.0(12)
  
| 枚举值 | 描述 |
| --- | --- |
| RCP_DNS_RULE_DNS_SERVERS | DNS服务器。 |
| RCP_DNS_RULE_STATIC | 静态DNS规则。 |
| RCP_DNS_RULE_DYNAMIC | 动态DNS规则。 |
 
 
  

#### Rcp_ExclusionsValueType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum Rcp_ExclusionsValueType
```
 
**描述**
 
代理排除中使用的数据类型. 用于区分[Rcp_Exclusions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___exclusions)中使用的数据。
 
**起始版本：** 5.0.0(12)
  
| 枚举值 | 描述 |
| --- | --- |
| RCP_EXCLUSION_USE_URL_ARRAY | 表示在Rcp_Exclusions中使用urls。 |
| RCP_EXCLUSION_USE_CALLBACK | 在Rcp_Exclusions中使用回调函数Rcp_ExclusionFunction。 |
 
 
  

#### Rcp_FormValueType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum Rcp_FormValueType
```
 
**描述**
 
表单值类型。
 
**起始版本：** 5.0.0(12)
  
| 枚举值 | 描述 |
| --- | --- |
| RCP_FORM_VALUE_TYPE_INT32 | 表示INT32数据类型。 |
| RCP_FORM_VALUE_TYPE_INT64 | 表示INT64数据类型。 |
| RCP_FORM_VALUE_TYPE_BOOL | 表示bool数据类型。 |
| RCP_FORM_VALUE_TYPE_STRING | 表示string数据类型。 |
| RCP_FORM_VALUE_TYPE_DOUBLE | 表示double数据类型。 |
 
 
  

#### Rcp_MultipartValueType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum Rcp_MultipartValueType
```
 
**描述**
 
多部分值类型。用于区分[Rcp_MultipartFormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___multipart_form_field_value)中使用的数据。
 
**起始版本：** 5.0.0(12)
  
| 枚举值 | 描述 |
| --- | --- |
| RCP_TYPE_FORM_FIELD_VALUE | 表示使用Rcp_FormFieldValue。 |
| RCP_TYPE_FORM_FIELD_FILE_VALUE | 表示使用Rcp_FormFieldFileValue。 |
 
 
  

#### Rcp_PathPreference

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum Rcp_PathPreference
```
 
**描述**
 
请求路径首选项。
 
这只是调用者的建议，系统决定使用哪个路径。
 
**起始版本：** 5.0.0(12)
  
| 枚举值 | 描述 |
| --- | --- |
| RCP_PATH_PREFERENCE_AUTO | 自动。 |
| RCP_PATH_PREFERENCE_WIFI | 倾向WIFI网络。 |
| RCP_PATH_PREFERENCE_CELLULAR | 倾向蜂窝网路。 |
 
 
  

#### Rcp_ProxyTunnelMode

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum Rcp_ProxyTunnelMode
```
 
**描述**
 
用于控制何时创建代理隧道。 隧道或隧道传输意味着向代理发送HTTP CONNECT请求，要求它连接到特定端口号上的远程主机，然后流量只是通过代理。“auto”表示为HTTPS创建隧道，而不是为HTTP创建隧道。“always”表示始终创建隧道。
 
**起始版本：** 5.0.0(12)
  
| 枚举值 | 描述 |
| --- | --- |
| RCP_PROXY_TUNNEL_AUTO | 自动。 |
| RCP_PROXY_TUNNEL_ALWAYS | 总是创建。 |
 
 
  

#### Rcp_ProxyType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum Rcp_ProxyType
```
 
**描述**
 
代理类型。用于区分不同的代理配置。
 
**起始版本：** 5.0.0(12)
  
| 枚举值 | 描述 |
| --- | --- |
| RCP_PROXY_SYSTEM | 系统代理。 |
| RCP_PROXY_CUSTOM | 使用自定义代理，选择后将解析Rcp_ProxyConfiguration.customProxy。 |
| RCP_PROXY_NO_PROXY | 不使用代理。 |
 
 
  

#### Rcp_RemoteValidationType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum Rcp_RemoteValidationType
```
 
**描述**
 
远程验证类型。
 
用于区分验证远程服务器身份的CA在[Rcp_SecurityConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___security_configuration)中描述。
 
**起始版本：** 5.0.0(12)
  
| 枚举值 | 描述 |
| --- | --- |
| RCP_REMOTE_VALIDATION_SYSTEM | 系统验证。 |
| RCP_REMOTE_VALIDATION_SKIP | 跳过验证。 |
| RCP_REMOTE_VALIDATION_CERTIFICATE_AUTHORITY | CA验证。 |
 
 
  

#### Rcp_SessionType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum Rcp_SessionType
```
 
**描述**
 
会话类型。
 
**起始版本：** 5.0.0(12)
  
| 枚举值 | 描述 |
| --- | --- |
| RCP_SESSION_TYPE_HTTP = 0 | 使用HTTP会话。 |
| RCP_SESSION_TYPE_MAX = 100 | Rcp_SessionType的最大值。 |
 
 
  

#### Rcp_StatusCode

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum Rcp_StatusCode
```
 
**描述**
 
请求响应的状态码。
 
**起始版本：** 5.0.0(12)
  
| 枚举值 | 描述 |
| --- | --- |
| RCP_NONE = 0 | 默认值。 |
| RCP_OK = 200 | 请求成功。 |
| RCP_CREATED = 201 | 请求成功并创建了新资源。 |
| RCP_ACCEPTED = 202 | 请求已接受，但尚未处理。 |
| RCP_NOT_AUTHORITATIVE = 203 | 返回信息不是原始的。 |
| RCP_NO_CONTENT = 204 | 请求成功，但无返回内容。 |
| RCP_RESET= 205 | 请求已成功处理，但需要重置内容。 |
| RCP_PARTIAL = 206 | 部分内容请求成功。 |
| RCP_MULTI_CHOICE = 300 | 对于该请求，服务器支持多种操作方式。 |
| RCP_MOVED_PERMANENTLY = 301 | 永久重定向。 |
| RCP_MOVED_TEMPORARILY = 302 | 临时重定向。 |
| RCP_SEE_OTHER = 303 | 查看其他位置。 |
| RCP_NOT_MODIFIED = 304 | 资源未修改。 |
| RCP_USE_PROXY = 305 | 使用代理。 |
| RCP_BAD_REQUEST = 400 | 请求语法错误。 |
| RCP_UNAUTHORIZED = 401 | 未授权。 |
| RCP_PAYMENT_REQUIRED = 402 | 需要付费。 |
| RCP_FORBIDDEN = 403 | 禁止访问。 |
| RCP_NOT_FOUND = 404 | 资源未找到。 |
| RCP_BAD_METHOD = 405 | 方法不允许。 |
| RCP_NOT_ACCEPTABLE = 406 | 不接受。 |
| RCP_PROXY_AUTH = 407 | 需要代理授权。 |
| RCP_CLIENT_TIMEOUT = 408 | 请求超时。 |
| RCP_CONFLICT = 409 | 冲突。 |
| RCP_GONE = 410 | 资源已永久删除。 |
| RCP_LENGTH_REQUIRED = 411 | 需要有效长度。 |
| RCP_PRECON_FAILED = 412 | 未满足前提条件。 |
| RCP_ENTITY_TOO_LARGE = 413 | 请求实体过大。 |
| RCP_REQ_TOO_LONG = 414 | 请求的 URI 过长。 |
| RCP_UNSUPPORTED_TYPE = 415 | 不支持的媒体类型。 |
| RCP_INTERNAL_ERROR = 500 | 服务器内部错误。 |
| RCP_NOT_IMPLEMENTED = 501 | 尚未实现。 |
| RCP_BAD_GATEWAY = 502 | 网关错误。 |
| RCP_UNAVAILABLE = 503 | 服务不可用。 |
| RCP_GATEWAY_TIMEOUT = 504 | 网关超时。 |
| RCP_VERSION = 505 | 不支持的HTTP版本。 |
 
 
  

#### RCP_QuicIpResolve

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum RCP_QuicIpResolve
```
 
**描述**
 
请求DNS解析时使用的IP解析类型。
 
**起始版本：** 26.0.0
  
| 枚举值 | 描述 |
| --- | --- |
| RCP_QUIC_IP_RESOLVE_WHATEVER = 0 | 使用IPv4地址或者IPv6地址。默认值。 |
| RCP_QUIC_IP_RESOLVE_V4 | 仅使用IPv4地址。 |
| RCP_QUIC_IP_RESOLVE_V6 | 仅使用IPv6地址。 |
 
 
  

#### Rcp_QuicConnOpt

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum Rcp_QuicConnOpt
```
 
**描述**
 
quic连接选项类型，用于配置连接的各种参数和回调函数。
 
**起始版本：** 26.0.0
  
| 枚举值 | 描述 |
| --- | --- |
| RCP_QUIC_CONN_IP_ADDRESS = 0 | 配置quic建立连接时使用的IP地址。 |
| RCP_QUIC_CONN_IP_RESOLVE = 1 | 配置quic建立连接时使用的IP地址类型。 |
| RCP_QUIC_CONN_DNS_FUNCTION = 2 | 配置自定义DNS解析函数。 |
| RCP_QUIC_CONN_ON_CONNECTED_FUNCTION = 3 | 配置quic连接成功建立时的回调函数。 |
| RCP_QUIC_CONN_ON_ERROR_FUNCTION = 4 | 配置quic连接发生错误时的回调函数。 |
| RCP_QUIC_CONN_ON_CLOSED_FUNCTION = 5 | 配置quic连接关闭时的回调函数。 |
| RCP_QUIC_CONN_STREAM_INBOUND_FUNCTION = 6 | 配置quic连接接收到入站流时的回调函数。 |
| RCP_QUIC_CONN_CONNECT_TIMEOUT_MS = 7 | 配置quic连接连接超时时间（ms）参数。 |
| RCP_QUIC_CONN_IDLE_TIMEOUT_MS = 8 | 配置quic连接空闲超时时间（ms）参数。 |
| RCP_QUIC_TLS_CERT_AUTHORITY_FUNCTION = 1000 | 配置quic连接证书验证时的回调函数。 |
| RCP_QUIC_TLS_CERT_AUTHORITY_CONTENT = 1001 | 配置quic连接用于验证对端的CA证书。 |
| RCP_QUIC_TLS_SESSION_TICKET_UPDATE_FUNCTION = 1002 | 配置quic会话票据更新时的回调函数。 |
| RCP_QUIC_TLS_SESSION_TICKET_CONTENT = 1003 | 配置quic会话票据内容参数。 |
| RCP_QUIC_TP_INITIAL_MAX_BIDIRECTIONAL_STREAMS = 2000 | 配置quic连接的初始最大双向流数传输参数。 |
| RCP_QUIC_TP_INITIAL_MAX_DATA = 2001 | 配置quic连接的初始最大数据量传输参数。 |
| RCP_QUIC_TP_INITIAL_MAX_STREAMDATA_BIDIRECTIONAL_LOCAL = 2002 | 配置quic连接的初始最大双向流本地数据量传输参数。 |
| RCP_QUIC_TP_INITIAL_MAX_STREAMDATA_BIDIRECTIONAL_REMOTE = 2003 | 配置quic连接的初始最大双向流远程数据量传输参数。 |
| RCP_QUIC_TP_INITIAL_MAX_STREAMDATA_UNIDIRECTIONAL = 2004 | 配置quic连接的初始最大单向流数据量传输参数。 |
| RCP_QUIC_TP_INITIAL_MAX_UNIDIRECTIONAL_STREAMS = 2005 | 配置quic连接的初始最大单向流数传输参数。 |
 
 
  

#### Rcp_QuicStreamOpt

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum Rcp_QuicStreamOpt
```
 
**描述**
 
quic流选项类型，用于配置流的各种参数和回调函数。
 
**起始版本：** 26.0.0
  
| 枚举值 | 描述 |
| --- | --- |
| RCP_QUIC_STREAM_EVENT_FUNCTION = 0 | 配置quic流事件发生时的回调函数。 |
| RCP_QUIC_STREAM_DATA_FUNCTION = 1 | 配置quic流数据接收时的回调函数。 |
| RCP_QUIC_INBOUND_STREAM_USER_OBJECT = 2 | 配置入站QUIC流的用户对象。 |
| RCP_QUIC_STREAM_SND_BUFFER_SIZE_KB = 3 | 设置quic流发送缓冲区大小（KB）参数。 |
 
 
  

#### Rcp_QuicConnInfo

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum Rcp_QuicConnInfo
```
 
**描述**
 
quic连接信息类型。用于查询连接的各种信息。
 
**起始版本：** 26.0.0
  
| 枚举值 | 描述 |
| --- | --- |
| RCP_INFO_CONN_GET_LOCALADDR = 0 | 获取quic连接的本地IP地址。 |
| RCP_INFO_CONN_GET_PEERADDR = 1 | 获取quic连接的对端IP地址。 |
| RCP_INFO_CONN_DNS_TIME_MS = 2 | 获取quic连接的DNS解析时间（ms）。 |
| RCP_INFO_CONN_CONNECT_TIME_MS = 3 | 获取quic连接的连接时间（ms）。 |
| RCP_INFO_CONN_SCID = 4 | 获取quic连接的源CID（Source Connection ID）。 |
| RCP_INFO_CONN_DCID = 5 | 获取quic连接的目标CID（Destination Connection ID）。 |
 
 
  

#### Rcp_QuicStreamInfo

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum Rcp_QuicStreamInfo
```
 
**描述**
 
quic流信息类型。用于查询流的各种信息。
 
**起始版本：** 26.0.0
  
| 枚举值 | 描述 |
| --- | --- |
| RCP_INFO_STREAM_SND_BUFFER_SIZE_KB = 0 | 获取quic流的发送缓冲区大小（KB）。 |
 
 
  

#### Rcp_QuicErrorCode

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum Rcp_QuicErrorCode
```
 
**描述**
 
quic请求中可能出现的错误码。
 
**起始版本：** 26.0.0
  
| 枚举值 | 描述 |
| --- | --- |
| RCP_QUIC_ERROR_CODE_SUCCESS = 0 | 操作成功。 |
| RCP_QUIC_PERMISSION_DENIED = 201 | 权限被拒绝，需要ohos.permission.INTERNET权限。 |
| RCP_QUIC_ERROR_CODE_FAILED = 1007920001 | quic相关操作失败。 |
| RCP_QUIC_ERROR_CODE_INVALID_PARAM = 1007920002 | 无效参数，传入的参数不符合要求。 |
| RCP_QUIC_ERROR_CODE_INVALID_STATE = 1007920003 | 无效连接状态，当前状态下不允许执行该操作。 |
| RCP_QUIC_ERROR_CODE_OUT_OF_MEM = 1007920004 | 内存不足，无法分配所需内存。 |
| RCP_QUIC_ERROR_CODE_CLOSE_FROM_PEER = 1007920005 | quic连接被对端关闭。 |
| RCP_QUIC_ERROR_CODE_HANDSHAKE_TIMEOUT = 1007920006 | quic连接握手超时。 |
| RCP_QUIC_ERROR_CODE_NETWORK_IDLE_TIMEOUT = 1007920007 | quic连接网络空闲超时。 |
| RCP_QUIC_ERROR_INVALID_FRAME = 1007920008 | quic连接接收到无效帧。 |
| RCP_QUIC_ERROR_CODE_SEND_PENDING = 1007920009 | quic连接发送挂起，缓冲区已满。 |
| RCP_QUIC_ERROR_CODE_FINALIZE_PENDING = 1007920010 | quic连接关闭挂起。 |
| RCP_QUIC_ERROR_CODE_NETWORK_UNREACHABLE = 1007920011 | 网络不可达。 |
| RCP_QUIC_ERROR_CODE_ENCRYPT_ERROR = 1007920012 | 加密错误，TLS握手或数据加密失败。 |
| RCP_QUIC_ERROR_CODE_BUFFER_TOO_SMALL = 1007920013 | 内部缓冲区过小。 |
| RCP_QUIC_ERROR_CODE_EAGAIN = 1007920015 | 非阻塞I/O操作资源暂时不可用，应稍后重试。 |
| RCP_QUIC_ERROR_CODE_STREAM_CLOSED = 1007920018 | quic流已关闭。 |
| RCP_QUIC_ERROR_CODE_STREAM_RESET_RECEIVED = 1007920019 | quic流被对端重置。 |
| RCP_QUIC_ERROR_CODE_STREAM_STOP_SENDING_RECEIVED = 1007920020 | quic流接收到停止发送请求。 |
 
 
  

#### Rcp_QuicStreamDirection

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum Rcp_QuicStreamDirection
```
 
**描述**
 
quic流的方向类型。
 
**起始版本：** 26.0.0
  
| 枚举值 | 描述 |
| --- | --- |
| RCP_QUIC_STREAM_BIDI = 0 | 双向流，流的两端都可以发送和接收数据。 |
| RCP_QUIC_STREAM_UNI = 1 | 单向流，流只能由创建端发送数据，接收端只能接收。 |
 
 
  

#### Rcp_QuicStreamShutdown

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum Rcp_QuicStreamShutdown
```
 
**描述**
 
quic流的关闭操作的类型。用于指定关闭流的读或写方向。
 
**起始版本：** 26.0.0
  
| 枚举值 | 描述 |
| --- | --- |
| RCP_QUIC_STREAM_SHUTDOWN_READ = 1 | 关闭流的读方向，不再接收数据。 |
| RCP_QUIC_STREAM_SHUTDOWN_WRITE = 2 | 关闭流的写方向，不再发送数据。 |
 
 
  

#### 函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### HMS_Rcp_CallNextRequestHandler()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
uint32_t HMS_Rcp_CallNextRequestHandler (Rcp_Request * request, const Rcp_RequestHandler * next, const Rcp_ResponseCallbackObject * responseCallback )
```
 
**描述**
 
在拦截器[Rcp_Interceptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___interceptor)的函数中可以调用下一个拦截器或defaultHandler。
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| request | 指向Rcp_Request的指针。 |
| next | 指向下一个异步处理器的指针Rcp_RequestHandler。 |
| responseCallback | 响应回调。指向Rcp_ResponseCallbackObject的指针。 |
 
 
**返回：**
 
uint32_t。[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败) - 参数错误 或 表示下一个异步处理器的返回值。
 
  

#### HMS_Rcp_CallNextSyncRequestHandler()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_Response* HMS_Rcp_CallNextSyncRequestHandler (Rcp_Request * request, const Rcp_SyncRequestHandler * next, uint32_t * errCode )
```
 
**描述**
 
在拦截器[Rcp_SyncInterceptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___sync_interceptor)的函数中可以调用下一个拦截器或默认处理器。
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| request | 指向Rcp_Request的指针。 |
| next | 指向下一个同步处理器的指针Rcp_SyncRequestHandler。 |
| errCode | 输出项。401：参数错误 或 表示下一个同步处理器的返回值。 |
 
 
**返回：**
 
Rcp_Response* 返回响应。
 
  

#### HMS_Rcp_CancelRequest()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
uint32_t HMS_Rcp_CancelRequest (Rcp_Session * session, const Rcp_Request * request )
```
 
**描述**
 
取消一个请求。
 
**系统能力：** SystemCapability.Collaboration.RemoteCommunication
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| session | 需要取消请求的会话。指向Rcp_Session的指针。 |
| request | 需要取消的请求。指向要关闭的Rcp_Request的指针。 |
 
 
**返回：**
 
取消成功时返回0，权限不足时返回[201](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section201-权限校验失败)，输入参数为空指针时返回[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)，会话已关闭或无效时返回[1007900993](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-remote-communication#section1007900993-会话已关闭)。
 
  

#### HMS_Rcp_CancelSession()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
uint32_t HMS_Rcp_CancelSession (Rcp_Session * session)
```
 
**描述**
 
取消会话。
 
**系统能力：** SystemCapability.Collaboration.RemoteCommunication
 
**起始版本：** 5.0.0(12)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| session | 需要取消的会话。指向要关闭的Rcp_Session的指针。 |
 
 
**返回：**
 
取消成功时返回0，权限不足时返回[201](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section201-权限校验失败)，输入参数为空指针时返回[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)，会话已关闭或无效时返回[1007900993](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-remote-communication#section1007900993-会话已关闭)。
 
  

#### HMS_Rcp_CloseSession()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
uint32_t HMS_Rcp_CloseSession (Rcp_Session ** session)
```
 
**描述**
 
关闭会话。
 
**系统能力：** SystemCapability.Collaboration.RemoteCommunication
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| session | 需要关闭的会话。指向Rcp_Session指针的指针。 |
 
 
**返回：**
 
关闭成功时返回0，权限不足时返回[201](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section201-权限校验失败)，输入参数为空指针时返回[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)，会话已关闭或无效时返回[1007900993](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-remote-communication#section1007900993-会话已关闭)。
 
  

#### HMS_Rcp_CreateForm()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_Form* HMS_Rcp_CreateForm (void)
```
 
**描述**
 
创建一个简单表单。
 
**起始版本：** 5.0.0(12)
 
**返回：**
 
Rcp_Form* 指向[Rcp_Form](#rcp_form)的指针。
 
  

#### HMS_Rcp_CreateHeaders()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_Headers* HMS_Rcp_CreateHeaders (void)
```
 
**描述**
 
为请求或响应创建标头。
 
**起始版本：** 5.0.0(12)
 
**返回：**
 
Rcp_Headers* 创建的标头。指向[Rcp_Headers](#rcp_headers)的指针。
 
  

#### HMS_Rcp_CreateMultipartForm()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_MultipartForm* HMS_Rcp_CreateMultipartForm (void)
```
 
**描述**
 
创建一个多部分表单。
 
**起始版本：** 5.0.0(12)
 
**返回：**
 
Rcp_MultipartForm* 返回创建的多部分表单，指向[Rcp_MultipartForm](#rcp_multipartform)的指针。
 
  

#### HMS_Rcp_CreateRequest()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_Request* HMS_Rcp_CreateRequest (const char * url)
```
 
**描述**
 
创建请求。
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| url | 请求URL。 |
 
 
**返回：**
 
Rcp_Request* 返回创建的请求。指向[Rcp_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request)的指针。
 
  

#### HMS_Rcp_CreateRequestCookies()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_RequestCookies* HMS_Rcp_CreateRequestCookies (void)
```
 
**描述**
 
创建空的请求Cookie。
 
**起始版本：** 5.0.0(12)
 
**返回：**
 
Rcp_RequestCookies* 返回指向已创建的[Rcp_RequestCookies](#rcp_requestcookies)的指针。
 
  

#### HMS_Rcp_CreateSession()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_Session* HMS_Rcp_CreateSession (const Rcp_SessionConfiguration * configuration, uint32_t * errCode )
```
 
**描述**
 
创建会话。
 
**系统能力：** SystemCapability.Collaboration.RemoteCommunication
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| configuration | 会话配置。 |
| errCode | 0：成功。 401：参数错误。 201：权限不足。 1007900027：内存不足。 |
 
 
**返回：**
 
Rcp_Session* 返回创建的会话。指向[Rcp_Session](#rcp_session)的指针。
 
  

#### HMS_Rcp_GetDefaultSession()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
uint32_t HMS_Rcp_GetDefaultSession (Rcp_Session ** session)
```
 
**描述**
 
获取默认会话。
 
**需要权限：** ohos.permission.INTERNET（如需使用[PathPreference](#rcp_pathpreference-1)的RCP_PATH_PREFERENCE_CELLULAR模式，则额外需要ohos.permission.GET_NETWORK_INFO）
 
**系统能力：** SystemCapability.Collaboration.RemoteCommunication
 
**起始版本：** 6.1.1(24)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| session | 默认会话出参。默认会话指针将被复制到Rcp_Session指针所指向的位置。 |
 
 
**返回：**
 
设置成功时返回0，权限不足时返回[201](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section201-权限校验失败)，输入参数为空指针时返回[1007900401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-remote-communication#section1007900401-接口参数错误)，遇到内存问题时返回[1007900027](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-remote-communication#section1007900027-内存不足)。
 
  

#### HMS_Rcp_DestroyForm()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_Rcp_DestroyForm (Rcp_Form * form)
```
 
**描述**
 
销毁一个简单表单。
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| form | 要销毁的表格。指向Rcp_Form的指针。 |
 
 
  

#### HMS_Rcp_DestroyHeaderEntries()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_Rcp_DestroyHeaderEntries (Rcp_HeaderEntry * headerEntry)
```
 
**描述**
 
销毁[HMS_Rcp_GetHeaderEntries](#hms_rcp_getheaderentries)中获取的所有键值对。
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| headerEntry | 指向要销毁的Rcp_HeaderEntry的指针。 |
 
 
  

#### HMS_Rcp_DestroyHeaders()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_Rcp_DestroyHeaders (Rcp_Headers * headers)
```
 
**描述**
 
销毁请求或响应的标头。
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| headers | 指向要销毁的Rcp_Headers的指针。 |
 
 
  

#### HMS_Rcp_DestroyMultipartForm()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_Rcp_DestroyMultipartForm (Rcp_MultipartForm * multipartForm)
```
 
**描述**
 
销毁一个多部分表单。
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| multipartForm | 要销毁的多部分表单。指向Rcp_MultipartForm的指针。 |
 
 
  

#### HMS_Rcp_DestroyRequest()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_Rcp_DestroyRequest (Rcp_Request * request)
```
 
**描述**
 
销毁请求。
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| request | 指向要销毁的Rcp_Request的指针。 |
 
 
  

#### HMS_Rcp_DestroyRequestCookieEntries()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_Rcp_DestroyRequestCookieEntries (Rcp_RequestCookieEntry * cookieEntry)
```
 
**描述**
 
销毁从[HMS_Rcp_GetRequestCookieValue](#hms_rcp_getrequestcookievalue)获取的所有与请求Cookie相关的键值对。
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| cookieEntry | 指向要销毁的Rcp_RequestCookieEntry的指针。 |
 
 
  

#### HMS_Rcp_DestroyRequestCookies()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_Rcp_DestroyRequestCookies (Rcp_RequestCookies * cookies)
```
 
**描述**
 
销毁请求Cookie。
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| cookies | 指向要销毁的Rcp_RequestCookies的指针。 |
 
 
  

#### HMS_Rcp_DestroyResponseCookieAttrEntries()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_Rcp_DestroyResponseCookieAttrEntries (Rcp_CookieAttributeEntry * entries)
```
 
**描述**
 
销毁响应Cookie属性。
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| entries | 指向要销毁的Rcp_CookieAttributeEntry的指针。 |
 
 
  

#### HMS_Rcp_Fetch()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
uint32_t HMS_Rcp_Fetch (Rcp_Session * session, Rcp_Request * request, const Rcp_ResponseCallbackObject * responseCallback )
```
 
**描述**
 
发送异步请求并获取响应。
 
**系统能力：** SystemCapability.Collaboration.RemoteCommunication
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| session | 发起请求使用的会话。指向Rcp_Session的指针。 |
| request | 发送的请求。指向Rcp_Request的指针。 |
| responseCallback | 指向用户定义的响应回调函数的指针。详情请参见Rcp_ResponseCallbackObject。 |
 
 
**返回：**
 
执行成功时返回0，权限不足时返回[201](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section201-权限校验失败)，输入参数为空指针时返回[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)，会话已关闭或无效时返回[1007900993](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-remote-communication#section1007900993-会话已关闭)。
 
**权限：**
 
ohos.permission.INTERNET（如需使用[PathPreference](#rcp_pathpreference-1)的RCP_PATH_PREFERENCE_CELLULAR模式，则额外需要ohos.permission.GET_NETWORK_INFO）
 
  

#### HMS_Rcp_FetchSync()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_Response* HMS_Rcp_FetchSync (Rcp_Session * session, Rcp_Request * request, uint32_t * errCode )
```
 
**描述**
 
发送同步请求并获取响应。
 
**系统能力：** SystemCapability.Collaboration.RemoteCommunication
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| session | 发起请求使用的会话。指向Rcp_Session的指针。 |
| request | 发送的请求。指向Rcp_Request的指针。 |
| errCode | [out] 输出常见的错误代码。 0：成功。 201：权限不足。 401：参数错误。 1007900001：不支持的协议。 1007900003：URL使用了错误/非法的格式或缺少URL。 1007900005：无法解析代理名称。 1007900006：无法解析主机名。 1007900007：无法连接到服务器。 1007900008：异常的服务器回复。 1007900009：对远程资源的访问被拒绝。 1007900016：HTTP2框架层中的错误。 1007900018：已传输部分文件。 1007900025：上载失败。 1007900026：无法从文件/应用程序中打开/读取本地数据。 1007900027：内存不足。 1007900028：已达到超时。 1007900047：重定向数达到最大数量。 1007900052：服务器没有返回任何内容（没有标头，没有数据）。 1007900055：向对等方发送数据失败。 1007900056：从对等方接收数据时失败。 1007900058：本地SSL证书有问题。 1007900059：无法使用指定的SSL密钥。 1007900060：SSL对等证书或SSH远程密钥不正常。 1007900061：无法识别或错误的HTTP内容或传输编码。 1007900063：超过了最大文件大小。 1007900070：磁盘已满或分配超出。 1007900073：远程文件已存在。 1007900077：SSL CA证书有问题 (路径？ 访问权限?)。 1007900078：找不到远程文件。 1007900992：请求已取消。 1007900993：会话已关闭或无效。 1007900094：身份验证函数返回了错误。 1007900201：禁止明文传输。从6.1.0(23)起新增支持此错误码。 1007900995：获取系统代理失败。 1007900996：代理类型不受支持。 1007900997：无效的内容类型。 1007900998：方法不受支持。 1007900999：内部错误。 Others：1007900000 + CURL_ERROR_CODE。更多常见的错误码，请参见curl错误码。 |
 
 
**返回：**
 
Rcp_Response* 返回的响应。指向[Rcp_Response](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response)的指针。
 
**权限：**
 
ohos.permission.INTERNET（如需使用[PathPreference](#rcp_pathpreference-1)的RCP_PATH_PREFERENCE_CELLULAR模式，则额外需要ohos.permission.GET_NETWORK_INFO）
 
  

#### HMS_Rcp_GetFormValue()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_FormFieldValue* HMS_Rcp_GetFormValue (Rcp_Form * form, const char * key )
```
 
**描述**
 
通过键获取一个简单表单的对应值。
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| form | 指向Rcp_Form的指针。 |
| key | 键。 |
 
 
**返回：**
 
Rcp_FormFieldValue* 值。指向{@Rcp_FormFieldValue}的指针。
 
  

#### HMS_Rcp_GetHeaderEntries()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_HeaderEntry* HMS_Rcp_GetHeaderEntries (Rcp_Headers * headers)
```
 
**描述**
 
获取请求或响应头的所有键值对。
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| headers | 指向要获取所有键值对的Rcp_Headers的指针。 |
 
 
**返回：**
 
Rcp_HeaderEntry* 指向所有获取到的键值对[Rcp_HeaderEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___header_entry)。
 
  

#### HMS_Rcp_GetHeaderValue()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_HeaderValue* HMS_Rcp_GetHeaderValue (Rcp_Headers * headers, const char * name)
```
 
**描述**
 
通过键获取请求或响应头的值。
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| headers | 指向要获取值的Rcp_Headers的指针。 |
| name | 键。 |
 
 
**返回：**
 
Rcp_HeaderValue* 指向获得的[Rcp_HeaderValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___header_value)的指针。
 
  

#### HMS_Rcp_GetMultipartFormValue()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_MultipartFormFieldValue* HMS_Rcp_GetMultipartFormValue (Rcp_MultipartForm * multipartForm, const char * key)
```
 
**描述**
 
通过键获取多部分表单的值。
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| multipartForm | 需要获取值的多部分表单。指向Rcp_MultipartForm的指针。 |
| key | 键。 |
 
 
**返回：**
 
Rcp_MultipartFormFieldValue* 多部分表单的值。指向[Rcp_MultipartFormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___multipart_form_field_value)的指针。
 
  

#### HMS_Rcp_SetFormOrder()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
uint32_t HMS_Rcp_SetFormOrder (Rcp_Form * form, Rcp_FormOrder order)
```
 
**描述**
 
设置Form表单的键值对发送顺序。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| form | 需要设置的表单。指向Rcp_Form的指针。 |
| order | 指定的keys顺序。 |
 
 
**返回：**
 
设置成功返回0，入参有空指针或者size大小为0时返回[1007900401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-remote-communication#section1007900401-接口参数错误)，内存问题返回[1007900027](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-remote-communication#section1007900027-内存不足)。
 
  

#### HMS_Rcp_SetMultipartFormOrder()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
uint32_t HMS_Rcp_SetMultipartFormOrder (Rcp_MultipartForm * multipartForm, Rcp_FormOrder order)
```
 
**描述**
 
设置MultipartForm表单的键值对发送顺序。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| multipartForm | 需要设置的表单。指向Rcp_MultipartForm的指针。 |
| order | 指定的keys顺序。 |
 
 
**返回：**
 
设置成功返回0，入参有空指针或者size大小为0时返回[1007900401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-remote-communication#section1007900401-接口参数错误)，内存问题返回[1007900027](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-remote-communication#section1007900027-内存不足)。
 
  

#### HMS_Rcp_GetRequestCookieEntries()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_RequestCookieEntry* HMS_Rcp_GetRequestCookieEntries (Rcp_RequestCookies * cookies)
```
 
**描述**
 
获取请求Cookie中的所有键值对。
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| cookies | 需要获取所有键值对的请求Cookie。指向Rcp_RequestCookies的指针。 |
 
 
**返回：**
 
Rcp_RequestCookieEntry* 返回请求Cookie中的所有键值对。指向[Rcp_RequestCookieEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request_cookie_entry)的指针。
 
  

#### HMS_Rcp_GetRequestCookieValue()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
char* HMS_Rcp_GetRequestCookieValue (Rcp_RequestCookies * cookies, const char * name)
```
 
**描述**
 
通过名称获取请求Cookie的值。
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| cookies | 需要获取值的请求Cookie。指向Rcp_RequestCookies的指针。 |
| name | 键。 |
 
 
**返回：**
 
char* 返回请求Cookie的值。
 
  

#### HMS_Rcp_GetResponseCookieAttrEntries()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_CookieAttributeEntry* HMS_Rcp_GetResponseCookieAttrEntries (Rcp_CookieAttributes * cookieAttributes)
```
 
**描述**
 
在[Rcp_CookieAttributes](#rcp_cookieattributes)中获取所有响应Cookie属性。
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| cookieAttributes | 指向要获取所有Cookie属性的Rcp_CookieAttributes的指针。 |
 
 
**返回：**
 
[Rcp_CookieAttributeEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___cookie_attribute_entry) * 响应的Cookie属性列表。
 
  

#### HMS_Rcp_GetResponseCookieAttrValue()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
const char* HMS_Rcp_GetResponseCookieAttrValue (Rcp_CookieAttributes * cookieAttributes, const char * name)
```
 
**描述**
 
通过名称获取Cookie属性的值。
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| cookieAttributes | 指向要获取值的Rcp_CookieAttributes的指针。 |
| name | 键。 |
 
 
**返回：**
 
char* Cookie属性中的值。
 
  

#### HMS_Rcp_GetSessionConfiguration()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
const Rcp_SessionConfiguration* HMS_Rcp_GetSessionConfiguration (Rcp_Session * session)
```
 
**描述**
 
获取会话配置。
 
**系统能力：** SystemCapability.Collaboration.RemoteCommunication
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| session | 需要获取会话配置的会话。指向Rcp_Session的指针。 |
 
 
**返回：**
 
Rcp_SessionConfiguration* 返回的会话配置。指向[Rcp_SessionConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___session_configuration)的指针。
 
  

#### HMS_Rcp_GetSessionId()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
const char* HMS_Rcp_GetSessionId (Rcp_Session * session)
```
 
**描述**
 
获取会话ID。
 
**系统能力：** SystemCapability.Collaboration.RemoteCommunication
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| session | 需要获取会话ID的会话。指向Rcp_Session的指针。 |
 
 
**返回：**
 
char* 返回的会话ID。
 
  

#### HMS_Rcp_SetFormValue()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
uint32_t HMS_Rcp_SetFormValue (Rcp_Form * form, const char * key, const Rcp_FormFieldValue * value)
```
 
**描述**
 
设置简单表单的键值对。
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| form | 需要设置键值对的表单。指向Rcp_Form的指针。 |
| key | 键。 |
| value | 值。 |
 
 
**返回：**
 
设置成功返回0，入参有空指针或者size大小为0时返回[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)，内存问题返回[1007900027](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-remote-communication#section1007900027-内存不足)。
 
  

#### HMS_Rcp_SetHeaderValue()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
uint32_t HMS_Rcp_SetHeaderValue (Rcp_Headers * headers, const char * name, const char * value)
```
 
**描述**
 
设置请求或响应头的键值对。
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| headers | 指向要设置的Rcp_Headers的指针。 |
| name | 键。 |
| value | 值。 |
 
 
**返回：**
 
设置成功返回0，入参有空指针或者size大小为0时返回[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)，内存问题返回[1007900027](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-remote-communication#section1007900027-内存不足)。
 
  

#### HMS_Rcp_SetMultipartFormValue()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
uint32_t HMS_Rcp_SetMultipartFormValue (Rcp_MultipartForm * multipartForm, const char * key, const Rcp_MultipartFormFieldValue * value)
```
 
**描述**
 
设置多部分表单的键值对。
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| multipartForm | 需要设置的多部分表单。指向Rcp_MultipartForm的指针。 |
| key | 键。 |
| value | 值。 |
 
 
**返回：**
 
设置成功返回0，入参有空指针或者size大小为0时返回[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)，内存问题返回[1007900027](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-remote-communication#section1007900027-内存不足)。
 
  

#### HMS_Rcp_SetRequestCookieValue()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
uint32_t HMS_Rcp_SetRequestCookieValue (Rcp_RequestCookies * cookies, const char * name, const char * value)
```
 
**描述**
 
设置请求Cookie。
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| cookies | 需要设置的请求Cookie。指向Rcp_RequestCookies的指针。 |
| name | 键。 |
| value | 值。 |
 
 
**返回：**
 
设置成功返回0，入参有空指针或者size大小为0时返回[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)，内存问题返回[1007900027](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-remote-communication#section1007900027-内存不足)。
 
  

#### HMS_Rcp_SetRequestOnBinaryDataRecvCallback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
uint32_t HMS_Rcp_SetRequestOnBinaryDataRecvCallback (Rcp_Request * request, Rcp_OnBinaryReceiveCallback onBinaryReceiveCallback)
```
 
**描述**
 
为请求设置流式接收二进制数据的回调函数。该回调函数与[Rcp_Configuration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___configuration)中配置的[Rcp_OnDataReceiveCallback](#rcp_ondatareceivecallback)功能一致。设置后将替换在[Rcp_Configuration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___configuration)中配置的[Rcp_OnDataReceiveCallback](#rcp_ondatareceivecallback)。
 
**起始版本：** 5.0.1(13)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| request | 需要设置二进制数据回调的请求。指向Rcp_Request的指针。 |
| onBinaryReceiveCallback | 需要设置的二进制数据接收回调函数。 |
 
 
**返回：**
 
设置成功返回0，参数错误时返回[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)。
 
  

#### HMS_Rcp_SetRequestConnectOnly()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
uint32_t HMS_Rcp_SetRequestConnectOnly (Rcp_Request * request, bool connectOnly)
```
 
**描述**
 
设置请求仅用于建立连接，而不进行数据传输。
 
**起始版本：** 6.1.1(24)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| request | 需要仅用于建立连接的请求。指向Rcp_Request的指针。 |
| connectOnly | 此选项用于确定请求是否仅用于建立连接。如果设置为true，则表示本次请求仅用于建立连接；如果设置为false，则表示本次请求可以传输数据。默认值为false。 |
 
 
**返回：**
 
设置成功时返回0，输入参数为空指针时返回[1007900401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-remote-communication#section1007900401-接口参数错误)。
 
  

#### HMS_Rcp_SetRequestOnStatusCodeReceiveCallback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
uint32_t HMS_Rcp_SetRequestOnStatusCodeReceiveCallback (Rcp_Request * request, Rcp_OnStatusCodeReceiveCallback onStatusCodeReceiveCallback)
```
 
**描述**
 
为请求设置响应状态码回调函数。在请求收到对端返回的响应码时触发。不可通过重新设置[Rcp_OnStatusCodeReceiveCallbackFunc](#rcp_onstatuscodereceivecallbackfunc)为NULL实现取消监听。
 
**起始版本：** 6.0.1(21)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| request | 需要设置响应状态码回调的请求。指向Rcp_Request的指针。 |
| onStatusCodeReceiveCallback | 需要设置的响应状态码接收回调函数。 |
 
 
**返回：**
 
设置成功返回0，参数错误时返回[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)。
 
  

#### HMS_Rcp_SetRequestGetDataCallback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
uint32_t HMS_Rcp_SetRequestGetDataCallback (Rcp_Request * request, Rcp_OnGetDataCallback  getDataCallback)
```
 
**描述**
 
设置获取数据的回调函数。不可通过重新设置[Rcp_GetDataCallbackFunc](#rcp_getdatacallbackfunc)为NULL实现取消监听。调用此函数设置非空的[Rcp_GetDataCallbackFunc](#rcp_getdatacallbackfunc)后，[Rcp_Request](#rcp_request)的[content](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request#content)失效。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| request | 需要设置响应回调的请求。指向Rcp_Request的指针。 |
| getDataCallback | 需要设置获取数据的回调函数。 |
 
 
**返回：**
 
设置成功时返回0，输入request参数为空指针时返回[1007900401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-remote-communication#section1007900401-接口参数错误)。
 
  

#### HMS_Rcp_QuicConnSetOpt()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_QuicErrorCode HMS_Rcp_QuicConnSetOpt (Rcp_QuicConn *conn, Rcp_QuicConnOpt opt, const void *optVal, uint32_t optLen)
```
 
**描述**
 
设置quic连接选项。用于设置连接的各种参数和回调函数。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| opt | quic连接选项类型，可配置Rcp_QuicConnOpt类型参数。 |
| optVal | quic连接选项的值。 |
| optLen | quic连接选项的长度。 |
 
 
**返回：**
 
[Rcp_QuicErrorCode](#rcp_quicerrorcode): quic连接选项配置结果，RCP_QUIC_ERROR_CODE_SUCCESS为配置quic连接选项成功，其余返回值均为配置失败。
 
  

#### HMS_Rcp_QuicConnGetInfo()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_QuicErrorCode HMS_Rcp_QuicConnGetInfo (Rcp_QuicConn *conn, Rcp_QuicConnInfo info, void *infoVal, uint32_t *infoLen)
```
 
**描述**
 
获取quic连接信息。用于建立quic连接成功后，获取相关quic连接信息。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| info | quic连接信息类型，可获得Rcp_QuicConnInfo相关参数。 |
| infoVal | quic连接信息的值。 |
| infoLen | quic连接信息的长度。 |
 
 
**返回：**
 
[Rcp_QuicErrorCode](#rcp_quicerrorcode): quic连接信息获取结果，RCP_QUIC_ERROR_CODE_SUCCESS表示获取quic连接相关参数成功，其余返回值均为获取失败。
 
  

#### HMS_Rcp_QuicStreamSetOpt()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_QuicErrorCode HMS_Rcp_QuicStreamSetOpt (Rcp_QuicConn *conn, uint64_t streamId, Rcp_QuicStreamOpt opt, const void *optVal, uint32_t optLen)
```
 
**描述**
 
设置quic连接中流的参数。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| streamId | quic流ID。 |
| opt | quic流选项类型，可配置Rcp_QuicStreamOpt类型相关选项。 |
| optVal | quic流选项的值。 |
| optLen | quic流选项的长度。 |
 
 
**返回：**
 
[Rcp_QuicErrorCode](#rcp_quicerrorcode): quic流选项配置结果，RCP_QUIC_ERROR_CODE_SUCCESS表示配置quic相关选项成功，其余返回值均为配置失败。
 
  

#### HMS_Rcp_QuicStreamGetInfo()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_QuicErrorCode HMS_Rcp_QuicStreamGetInfo (Rcp_QuicConn *conn, uint64_t streamId, Rcp_QuicStreamInfo info, void *infoVal, uint32_t *infoLen)
```
 
**描述**
 
获取quic连接中streamId对应流的信息。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| streamId | quic流ID。 |
| info | quic流信息类型，可获取Rcp_QuicStreamInfo类型相关信息。 |
| infoVal | quic流信息的值。 |
| infoLen | quic流信息的长度。 |
 
 
**返回：**
 
[Rcp_QuicErrorCode](#rcp_quicerrorcode): quic流信息获取结果，RCP_QUIC_ERROR_CODE_SUCCESS表示获取quic流相关参数成功，其余返回值均为获取失败。
 
  

#### HMS_Rcp_QuicCreateSession()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_QuicSession *HMS_Rcp_QuicCreateSession ()
```
 
**描述**
 
创建quic会话对象。一个quic会话中可以管理多个quic连接。
 
**起始版本：** 26.0.0
 
**返回：**
 
[Rcp_QuicSession](#rcp_quicsession)*: quic会话对象指针，失败返回NULL。
 
  

#### HMS_Rcp_QuicDestroySession()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_Rcp_QuicDestroySession (Rcp_QuicSession *session)
```
 
**描述**
 
销毁quic会话对象。释放quic会话资源。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| session | quic会话对象。 |
 
 
  

#### HMS_Rcp_QuicConnCreate()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_QuicConn *HMS_Rcp_QuicConnCreate (char *alpn, void *userObject)
```
 
**描述**
 
创建quic连接对象。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| alpn | 应用层协议协商（ALPN）字符串。 |
| userObject | 用户定义的对象。 |
 
 
**返回：**
 
[Rcp_QuicConn](#rcp_quicconn)*: quic连接对象指针，失败返回NULL。
 
  

#### HMS_Rcp_QuicConnConnect()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_QuicErrorCode HMS_Rcp_QuicConnConnect (Rcp_QuicSession *session, Rcp_QuicConn *conn, const char *serverName, uint16_t port)
```
 
**描述**
 
发起quic连接握手。握手结果通过连接回调通知。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| session | quic会话对象。 |
| conn | quic连接对象。 |
| serverName | 服务器名称（域名或IP地址）。 |
| port | 服务器端口号。 |
 
 
**返回：**
 
[Rcp_QuicErrorCode](#rcp_quicerrorcode): quic连接发起结果，RCP_QUIC_ERROR_CODE_SUCCESS表示quic连接发起成功，其余返回值均为发起失败。
 
**权限：**
 
ohos.permission.INTERNET
 
  

#### HMS_Rcp_QuicConnDestroy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_QuicErrorCode HMS_Rcp_QuicConnDestroy (Rcp_QuicConn *conn)
```
 
**描述**
 
销毁quic连接对象。释放quic连接资源。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
 
 
**返回：**
 
[Rcp_QuicErrorCode](#rcp_quicerrorcode): quic连接对象销毁结果，RCP_QUIC_ERROR_CODE_SUCCESS表示quic连接对象销毁成功，其余返回值均为销毁失败。
 
  

#### HMS_Rcp_QuicConnStreamOpen()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_QuicErrorCode HMS_Rcp_QuicConnStreamOpen (Rcp_QuicConn *conn, Rcp_QuicStreamDirection direction, uint64_t *streamId, void *userObject)
```
 
**描述**
 
在quic连接中打开一个quic流。quic连接建立成功后才能打开quic流。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| direction | quic流方向，配置quic方向Rcp_QuicStreamDirection枚举类型。 |
| streamId | 创建的quic流ID指针。 |
| userObject | 流回调的用户对象。 |
 
 
**返回：**
 
[Rcp_QuicErrorCode](#rcp_quicerrorcode): quic流创建结果，RCP_QUIC_ERROR_CODE_SUCCESS表示quic流创建成功，其余返回值均为创建失败。
 
**权限：**
 
ohos.permission.INTERNET
 
  

#### HMS_Rcp_QuicConnStreamSend()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_QuicErrorCode HMS_Rcp_QuicConnStreamSend (Rcp_QuicConn *conn, uint64_t streamId, const Rcp_QuicIoVec *ioVec, uint32_t ioVecCount, bool fin)
```
 
**描述**
 
通过quic流发送数据。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| streamId | quic流ID。 |
| ioVec | 发送的内容数据向量数组。 |
| ioVecCount | 发送的内容数据向量数量。 |
| fin | true表示发送内容是最后一段数据，false表示发送的内容不是最后一段数据。 |
 
 
**返回：**
 
[Rcp_QuicErrorCode](#rcp_quicerrorcode): quic流发送数据结果，RCP_QUIC_ERROR_CODE_SUCCESS表示quic流发送数据成功，其余返回值均为发送失败。
 
**权限：**
 
ohos.permission.INTERNET
 
  

#### HMS_Rcp_QuicConnStreamWantRead()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_QuicErrorCode HMS_Rcp_QuicConnStreamWantRead (Rcp_QuicConn *conn, uint64_t streamId)
```
 
**描述**
 
触发quic流数据读取回调。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| streamId | quic流ID。 |
 
 
**返回：**
 
[Rcp_QuicErrorCode](#rcp_quicerrorcode): quic流数据读取回调开启结果，RCP_QUIC_ERROR_CODE_SUCCESS表示quic流数据读取回调开启成功，其余返回值均为开启失败。
 
  

#### HMS_Rcp_QuicConnStreamReset()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_QuicErrorCode HMS_Rcp_QuicConnStreamReset (Rcp_QuicConn *conn, uint64_t streamId, uint64_t appErr)
```
 
**描述**
 
重置quic流。立即终止流，丢弃所有未发送和已接收的数据。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| streamId | quic流ID。 |
| appErr | 应用错误码。 |
 
 
**返回：**
 
[Rcp_QuicErrorCode](#rcp_quicerrorcode): quic流重置结果，RCP_QUIC_ERROR_CODE_SUCCESS表示quic流重置成功，其余返回值均为重置失败。
 
**权限：**
 
ohos.permission.INTERNET
 
  

#### HMS_Rcp_QuicConnStreamShutdown()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_QuicErrorCode HMS_Rcp_QuicConnStreamShutdown (Rcp_QuicConn *conn, uint64_t streamId, Rcp_QuicStreamShutdown flag, uint64_t appErr)
```
 
**描述**
 
关闭连接中streamId对应流的读或写。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| conn | quic连接对象。 |
| streamId | quic流ID。 |
| flag | quic流关闭标志，可选Rcp_QuicStreamShutdown类型。 |
| appErr | 应用错误码。 |
 
 
**返回：**
 
[Rcp_QuicErrorCode](#rcp_quicerrorcode): quic流关闭结果，RCP_QUIC_ERROR_CODE_SUCCESS表示quic流关闭成功，其余返回值均为关闭失败。
 
**权限：**
 
ohos.permission.INTERNET
 
  

#### HMS_Rcp_QuicStreamGetDirection()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_QuicStreamDirection HMS_Rcp_QuicStreamGetDirection (uint64_t streamId)
```
 
**描述**
 
获取quic流的方向类型。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| streamId | quic流ID。 |
 
 
**返回：**
 
[Rcp_QuicStreamDirection](#rcp_quicstreamdirection): quic流的方向，RCP_QUIC_STREAM_BIDI表示双向流，RCP_QUIC_STREAM_UNI表示单向流。
 
  

#### HMS_Rcp_QuicFreeSlist()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_Rcp_QuicFreeSlist (Rcp_QuicSlist *list)
```
 
**描述**
 
释放[Rcp_QuicSlist](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___quic_slist)链表，释放链表中的所有节点和数据。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| list | Rcp_QuicSlist链表指针。 |
