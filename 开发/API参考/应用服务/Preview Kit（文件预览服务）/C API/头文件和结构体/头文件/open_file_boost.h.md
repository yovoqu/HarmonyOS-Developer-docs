# open_file_boost.h

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost-open__file__boost_8h
**支持设备：** PC/2in1


## 概述
**支持设备：** PC/2in1

声明文件打开加速的API集合。

**引用文件：** <PreviewKit/open_file_boost.h>

**库：** libopen_file_boost.so

**系统能力：** SystemCapability.PCService.OpenFileBoost

**起始版本：** 5.0.3(15)

**相关模块：** [Preview](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost_preview)


## 汇总
**支持设备：** PC/2in1


### 宏定义
**支持设备：** PC/2in1


| 名称 | 描述 |
| --- | --- |
| [MAX_BUFFER_LENGTH](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost_preview#max_buffer_length)   1024 | 沙箱路径最大长度。 |


### 类型定义
**支持设备：** PC/2in1


| 名称 | 描述 |
| --- | --- |
| typedef [OpenFileBoost_AppState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost_preview#openfileboost_appstate)(*[HMS_OpenFileBoost_QueryAppState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost_preview#hms_openfileboost_queryappstate)) (void) | 系统查询app状态的回调函数定义，该函数在调用[HMS_OpenFileBoost_OnFilePreload](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost_preview#hms_openfileboost_onfilepreload)推荐文件之前先回调app。该函数用于系统向app查询当前是否允许推荐文件给app。如果应用处于前台焦点或者某些特殊状态，不适合预加载文件，app返回特定枚举值拒绝预加载。 |
| typedef [OpenFileBoost_CbErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost_preview#openfileboost_cberrcode)(*[HMS_OpenFileBoost_OnFilePreload](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost_preview#hms_openfileboost_onfilepreload)) (void* fileInfo) | 系统向应用推荐或取消推荐预加载文件的回调函数定义。 系统预测用户可能打开的文件，并通过该回调函数通知app，另外在某些场景下，比如当前系统可用内存不足，或者有其他文件更有可能被用户打开，则系统会通知app取消某些文件的预加载。 |


### 枚举
**支持设备：** PC/2in1


| 名称 | 描述 |
| --- | --- |
| [OpenFileBoost_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost_preview#openfileboost_errcode) { OPEN_FILE_BOOST_SUCCESS = 0, OPEN_FILE_BOOST_PERMISSION_NOT_GRANTED = 201, OPEN_FILE_BOOST_INVALID_PARAM = 401, OPEN_FILE_BOOST_INTERNAL_ERROR = 1017200001, OPEN_FILE_BOOST_INSUFFICIENT_BUFFER = 1017200002, OPEN_FILE_BOOST_SERVICE_UNAVAILABLE = 1017200003, OPEN_FILE_BOOST_NO_MEMORY = 1017200004 } | 文件打开加速的错误码定义。 |
| [OpenFileBoost_CbErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost_preview#openfileboost_cberrcode) { OPEN_FILE_BOOST_CALLBACK_SUCCESS = 0, OPEN_FILE_BOOST_CALLBACK_FAILURE = 1017210000 } | 回调函数[HMS_OpenFileBoost_OnFilePreload](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost_preview#hms_openfileboost_onfilepreload)的错误码定义， 它用于app向系统返回回调函数执行结果。 |
| [OpenFileBoost_AppState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost_preview#openfileboost_appstate) { OPEN_FILE_BOOST_APP_STATE_ALLOW_PRELOAD = 0, OPEN_FILE_BOOST_APP_STATE_REJECT_PRELOAD = 1, OPEN_FILE_BOOST_APP_STATE_FOREVER_REJECT_PRELOAD = 2 } | app状态，用于指示app当前是否允许系统推荐预加载文件。 |


### 函数
**支持设备：** PC/2in1


| 名称 | 描述 |
| --- | --- |
| [OpenFileBoost_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost_preview#openfileboost_errcode) [HMS_OpenFileBoost_GetFdFromPreloadFileInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost_preview#hms_openfileboost_getfdfrompreloadfileinfo) (void* fileInfo, int32_t* fd) | 获取文件描述符信息。 |
| [OpenFileBoost_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost_preview#openfileboost_errcode) [HMS_OpenFileBoost_GetSandboxPathFromPreloadFileInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost_preview#hms_openfileboost_getsandboxpathfrompreloadfileinfo) (void* fileInfo, char* sandboxPath, int32_t pathLen) | 获取沙箱路径信息。 |
| [OpenFileBoost_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost_preview#openfileboost_errcode) [HMS_OpenFileBoost_RegisterFilePreload](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost_preview#hms_openfileboost_registerfilepreload) ([HMS_OpenFileBoost_QueryAppState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost_preview#hms_openfileboost_queryappstate) queryAppState, [HMS_OpenFileBoost_OnFilePreload](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost_preview#hms_openfileboost_onfilepreload) filePreload, [HMS_OpenFileBoost_OnFilePreload](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost_preview#hms_openfileboost_onfilepreload) cancelFilePreload) | 注册预加载回调。 |
| [OpenFileBoost_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost_preview#openfileboost_errcode) [HMS_OpenFileBoost_UnregisterFilePreload](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost_preview#hms_openfileboost_unregisterfilepreload) (void) | 取消注册预加载回调。 |
| [OpenFileBoost_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost_preview#openfileboost_errcode) [HMS_OpenFileBoost_NotifyPreloadHit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost_preview#hms_openfileboost_notifypreloadhit) (int32_t fd, char* sandboxPath, int32_t pathLen) | 当用户打开预加载文件时，app调用该接口通知系统预加载命中，这将有助于提高预加载文件预测的准确性。 |
