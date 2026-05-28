# MediaKeySession_Callback

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-mediakeysession-callback
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct MediaKeySession_Callback {...} MediaKeySession_Callback
```
  

##### 概述

MediaKeySession_Callback结构体，用于监听密钥过期、密钥更改等事件，不返回媒体密钥会话实例，适用于单媒体密钥会话解密场景。
 
**起始版本：** 11
 
**相关模块：** [Drm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm)
 
**所在头文件：** [native_mediakeysession.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-mediakeysession-h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| MediaKeySession_EventCallback eventCallback | 正常事件回调，如密钥过期等。 |
| MediaKeySession_KeyChangeCallback keyChangeCallback | 密钥更改事件的密钥更改回调。 |
