# Rcp_ResponseCookies

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response_cookies
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

##### 概述

响应Cookie。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| char * name | 响应Cookie名称。 |
| char * value | 响应Cookie值。 |
| char * domain | 响应Cookie域属性。 |
| char * path | 响应Cookie路径属性。 |
| char * expires | 响应Cookie过期属性。 |
| uint64_t maxAge | 响应Cookie maxAge属性。 |
| bool secure | 响应Cookie安全属性。true表示此cookie是通过安全连接返回的，false表示此cookie不是通过安全连接返回的。 |
| bool httpOnly | 响应Cookie httpOnly属性。true表示不可通过页面脚本等活动内容访问cookie，false表示表示可以通过页面脚本等活动内容访问cookie。 |
| char * sameSite | 响应Cookie sameSite属性。 |
| uint64_t rawSize | 此响应Cookie的原始大小。 |
| char * originString | 原始字符串。 |
| Rcp_CookieAttributes * cookieAttributes | 响应Cookie中的所有属性。 |
| struct Rcp_ResponseCookies * next | 链式存储。指向下一个Rcp_ResponseCookies的指针。 |
 
 
  

##### 结构体成员变量说明

  

##### cookieAttributes

```text
Rcp_CookieAttributes* Rcp_ResponseCookies::cookieAttributes
```
 
**描述**
 
响应Cookie中的所有属性。
 
  

##### domain

```text
char* Rcp_ResponseCookies::domain
```
 
**描述**
 
响应Cookie域属性。
 
  

##### expires

```text
char* Rcp_ResponseCookies::expires
```
 
**描述**
 
响应Cookie过期属性。
 
  

##### httpOnly

```text
bool Rcp_ResponseCookies::httpOnly
```
 
**描述**
 
响应Cookie httpOnly属性。true表示不可通过页面脚本等活动内容访问cookie，false表示表示可以通过页面脚本等活动内容访问cookie。
 
  

##### maxAge

```text
uint64_t Rcp_ResponseCookies::maxAge
```
 
**描述**
 
响应Cookie maxAge属性。
 
  

##### name

```text
char* Rcp_ResponseCookies::name
```
 
**描述**
 
响应Cookie名称。
 
  

##### next

```text
struct Rcp_ResponseCookies* Rcp_ResponseCookies::next
```
 
**描述**
 
链式存储。指向下一个[Rcp_ResponseCookies](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response_cookies)的指针。
 
  

##### originString

```text
char* Rcp_ResponseCookies::originString
```
 
**描述**
 
原始字符串。
 
  

##### path

```text
char* Rcp_ResponseCookies::path
```
 
**描述**
 
响应Cookie路径属性。
 
  

##### rawSize

```text
uint64_t Rcp_ResponseCookies::rawSize
```
 
**描述**
 
此响应Cookie的原始大小。
 
  

##### sameSite

```text
char* Rcp_ResponseCookies::sameSite
```
 
**描述**
 
响应Cookie sameSite属性。
 
  

##### secure

```text
bool Rcp_ResponseCookies::secure
```
 
**描述**
 
响应Cookie安全属性。true表示此cookie是通过安全连接返回的，false表示此cookie不是通过安全连接返回的。
 
  

##### value

```text
char* Rcp_ResponseCookies::value
```
 
**描述**
 
响应Cookie值。
