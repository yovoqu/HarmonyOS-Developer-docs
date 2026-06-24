# open_file_boost.h

更新时间：2026-06-12 06:54:11

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost-open__file__boost_8h
**支持设备：** PC/2in1

#### 概述

**支持设备：** PC/2in1

声明文件打开加速的API集合。
 
**引用文件：** <PreviewKit/open_file_boost.h>
 
**库：** libopen_file_boost.so
 
**系统能力：** SystemCapability.PCService.OpenFileBoost
 
**起始版本：** 5.0.3(15)
 
**相关模块：** [Preview](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost_preview)
 
  

#### 汇总

**支持设备：** PC/2in1

  

#### 宏定义

**支持设备：** PC/2in1
 
| 名称 | 描述 |
| --- | --- |
| MAX_BUFFER_LENGTH 1024 | 沙箱路径最大长度。 |
 
 
  

#### 类型定义

**支持设备：** PC/2in1
 
| 名称 | 描述 |
| --- | --- |
| typedef OpenFileBoost_AppState(*HMS_OpenFileBoost_QueryAppState) (void) | 系统查询App状态的回调函数定义，该函数在调用HMS_OpenFileBoost_OnFilePreload推荐文件之前先回调App。该函数用于系统向App查询当前是否允许推荐文件给App。如果应用处于前台焦点或者某些特殊状态，不适合预加载文件，App返回特定枚举值拒绝预加载。 |
| typedef OpenFileBoost_CbErrCode(*HMS_OpenFileBoost_OnFilePreload) (void* fileInfo) | 系统向应用推荐或取消推荐预加载文件的回调函数定义。 系统预测用户可能打开的文件，并通过该回调函数通知App，另外在某些场景下，比如当前系统可用内存不足，或者有其他文件更有可能被用户打开，则系统会通知App取消某些文件的预加载。 |
| typedef struct FileScanBoost_ScanOption FileScanBoost_ScanOption | 文件扫描选项配置的不透明类型。 |
| typedef struct FileScanBoost_ScanResult FileScanBoost_ScanResult | 文件扫描结果的不透明类型。 |
| typedef FileScanBoost_CbErrCode(* HMS_Preview_FileScanBoost_OnFileScan) (int32_t fd, const char *path, uint32_t pathLen) | 文件扫描回调通知的函数指针类型。 系统调用此回调来发送扫描任务。此回调方法与扫描任务执行是异步的， 应用程序应在收到扫描任务后立即返回回调返回值，而不应阻塞回调。 并且扫描任务完成后的最终结果应使用HMS_Preview_FileScanBoost_ReportScanResult报告。 |
| typedef struct OpenFileBoost_SupportFile OpenFileBoost_SupportFile | 应用支持预加载的文件信息，用于描述一组符合预加载条件的文件特征。 开发者可以使用HMS_Preview_OpenFileBoost_SupportFileCreate创建该结构体， 配置哪些类型的文件可以被系统预加载。 |
| typedef struct OpenFileBoost_Options OpenFileBoost_Options | 应用支持预加载的文件信息和文件类型数量，用于向系统注册一批支持预加载的文件类型。 |
| typedef struct OpenFileBoost_FileOperationInfo OpenFileBoost_FileOperationInfo | 应用向系统传递的文件操作信息。 开发者可传递文件路径和该文件的操作信息，操作信息包括： 打开："open"， 关闭："close"， 导入/加载："import"， 导出："export"， TAB隐藏："tab_hidden"， TAB可见"tab_visible"， 保存："save"， 新建："create"， 云上传："upload"， 云下载："download"， 共享："share"， 打印："print"， 另存为："save_as"， 放映："play"。 开发者可以使用HMS_Preview_OpenFileBoost_FileOperationInfoCreate函数创建此结构体。 |
 
 
  

#### 枚举

**支持设备：** PC/2in1
 
| 名称 | 描述 |
| --- | --- |
| OpenFileBoost_ErrCode { OPEN_FILE_BOOST_SUCCESS = 0, OPEN_FILE_BOOST_PERMISSION_NOT_GRANTED = 201, OPEN_FILE_BOOST_INVALID_PARAM = 401, OPEN_FILE_BOOST_CAPABILITY_NOT_SUPPORTED = 801, OPEN_FILE_BOOST_INTERNAL_ERROR = 1017200001, OPEN_FILE_BOOST_INSUFFICIENT_BUFFER = 1017200002, OPEN_FILE_BOOST_SERVICE_UNAVAILABLE = 1017200003, OPEN_FILE_BOOST_NO_MEMORY = 1017200004 } | 文件打开加速的错误码定义。 |
| OpenFileBoost_CbErrCode { OPEN_FILE_BOOST_CALLBACK_SUCCESS = 0, OPEN_FILE_BOOST_CALLBACK_FAILURE = 1017210000 } | 回调函数HMS_OpenFileBoost_OnFilePreload的错误码定义， 它用于App向系统返回回调函数执行结果。 |
| OpenFileBoost_AppState { OPEN_FILE_BOOST_APP_STATE_ALLOW_PRELOAD = 0, OPEN_FILE_BOOST_APP_STATE_REJECT_PRELOAD = 1, OPEN_FILE_BOOST_APP_STATE_FOREVER_REJECT_PRELOAD = 2, OPEN_FILE_BOOST_APP_STATE_EXCEL_TRANSACTION = 3 } | App状态，用于指示App当前是否允许系统推荐预加载文件。 |
| FileScanBoost_ErrCode { FILE_SCAN_BOOST_SUCCESS = 0, FILE_SCAN_BOOST_ERROR_PERMISSION_NOT_GRANTED = 201, FILE_SCAN_BOOST_ERROR_INVALID_PARAM = 401, FILE_SCAN_BOOST_ERROR_CAPABILITY_NOT_SUPPORTED = 801, FILE_SCAN_BOOST_ERROR_INTERNAL = 1017230001, FILE_SCAN_BOOST_ERROR_NOT_REGISTERED = 1017230002, FILE_SCAN_BOOST_ERROR_ALREADY_REGISTERED = 1017230003, FILE_SCAN_BOOST_ERROR_SERVICE_UNAVAILABLE = 1017230004, FILE_SCAN_BOOST_ERROR_FORMAT_NOT_SUPPORTED = 1017230005 } | 文件扫描加速功能返回的所有错误码的枚举。 |
| FileScanBoost_CbErrCode { FILE_SCAN_BOOST_CALLBACK_SUCCESS = 0, FILE_SCAN_BOOST_CALLBACK_ERROR_INTERNAL = 1017240001, FILE_SCAN_BOOST_CALLBACK_ERROR_FORMAT_NOT_SUPPORTED = 1017240002 } | 文件扫描回调特定错误码的枚举。 |
| FileScanBoost_ScanState { FILE_SCAN_BOOST_SCAN_STATE_SUCCESS = 0, FILE_SCAN_BOOST_SCAN_STATE_PROCESS_ERROR = 1, FILE_SCAN_BOOST_SCAN_STATE_FILE_ERROR = 2 } | 文件扫描后扫描状态的枚举。 |
 
 
  

#### 函数

**支持设备：** PC/2in1
 
| 名称 | 描述 |
| --- | --- |
| OpenFileBoost_ErrCode HMS_OpenFileBoost_GetFdFromPreloadFileInfo (void* fileInfo, int32_t* fd) | 获取文件描述符信息。 |
| OpenFileBoost_ErrCode HMS_OpenFileBoost_GetSandboxPathFromPreloadFileInfo (void* fileInfo, char* sandboxPath, int32_t pathLen) | 获取沙箱路径信息。 |
| OpenFileBoost_ErrCode HMS_OpenFileBoost_RegisterFilePreload (HMS_OpenFileBoost_QueryAppState queryAppState, HMS_OpenFileBoost_OnFilePreload filePreload, HMS_OpenFileBoost_OnFilePreload cancelFilePreload) | 注册预加载回调。 |
| OpenFileBoost_ErrCode HMS_OpenFileBoost_UnregisterFilePreload (void) | 取消注册预加载回调。 |
| OpenFileBoost_ErrCode HMS_OpenFileBoost_NotifyPreloadHit (int32_t fd, char* sandboxPath, int32_t pathLen) | 当用户打开预加载文件时，App调用该接口通知系统预加载命中，这将有助于提高预加载文件预测的准确性。 |
| FileScanBoost_ErrCode HMS_Preview_FileScanBoost_ScanOptionCreate (FileScanBoost_ScanOption **outOption) | 创建FileScanBoost_ScanOption实例。 |
| void HMS_Preview_FileScanBoost_ScanOptionDestroy (FileScanBoost_ScanOption *option) | 销毁FileScanBoost_ScanOption实例。 |
| FileScanBoost_ErrCode HMS_Preview_FileScanBoost_ScanOptionAddSupportFile (FileScanBoost_ScanOption *option, const char *suffix, uint32_t suffixLen) | 向扫描选项添加支持的文件类型。 |
| FileScanBoost_ErrCode HMS_Preview_FileScanBoost_ScanResultCreate (FileScanBoost_ScanResult **outResult) | 创建FileScanBoost_ScanResult实例。 |
| void HMS_Preview_FileScanBoost_ScanResultDestroy (FileScanBoost_ScanResult *result) | 销毁FileScanBoost_ScanResult实例。 |
| FileScanBoost_ErrCode HMS_Preview_FileScanBoost_ScanResultSetState (FileScanBoost_ScanResult *result, FileScanBoost_ScanState state) | 在结果中设置扫描状态。 |
| FileScanBoost_ErrCode HMS_Preview_FileScanBoost_ScanResultSetMaxAtomicTime (FileScanBoost_ScanResult *result, int64_t maxAtomicTime) | 在结果中设置最大原子时间。 |
| FileScanBoost_ErrCode HMS_Preview_FileScanBoost_ScanResultSetMemSize (FileScanBoost_ScanResult *result, int64_t memSize) | 在结果中设置内存大小。 |
| FileScanBoost_ErrCode HMS_Preview_FileScanBoost_RegisterFileScan (HMS_Preview_FileScanBoost_OnFileScan fileScanCb, FileScanBoost_ScanOption *option) | 使用扩展名过滤方式注册多文件类型的回调函数。 在上一次注册结果注销之前，请勿重复注册。 重复注册将返回错误码FILE_SCAN_BOOST_ERROR_ALREADY_REGISTERED， 且仅首次注册的信息生效。 |
| FileScanBoost_ErrCode HMS_Preview_FileScanBoost_UnregisterFileScan (void) | 移除已注册的文件扫描回调函数。注意，注销意味着该应用程序所有未报告扫描结果的扫描任务均失效。 同时，在发起注销之前，应用程序需要清理未完成的扫描任务。 |
| FileScanBoost_ErrCode HMS_Preview_FileScanBoost_ReportScanResult (const char *path, uint32_t pathLen, FileScanBoost_ScanResult *result) | 报告文件扫描操作的完成结果。 |
| OpenFileBoost_ErrCode HMS_Preview_OpenFileBoost_SupportFileCreate (const char *suffix, uint32_t suffixLen, uint64_t lowerLimitKb, uint64_t upperLimitKb, OpenFileBoost_SupportFile **outSupportFile) | 创建OpenFileBoost_SupportFile。 |
| OpenFileBoost_ErrCode HMS_Preview_OpenFileBoost_SupportFileDestroy (OpenFileBoost_SupportFile *supportFile) | 销毁OpenFileBoost_SupportFile。 |
| OpenFileBoost_ErrCode HMS_Preview_OpenFileBoost_OptionsCreate (OpenFileBoost_Options **outOptions) | 创建一个空的OpenFileBoost_Options。 使用HMS_Preview_OpenFileBoost_OptionsAddSupportFile添加文件。 |
| OpenFileBoost_ErrCode HMS_Preview_OpenFileBoost_OptionsAddSupportFile (OpenFileBoost_Options *options, const OpenFileBoost_SupportFile *supportFile) | 向OpenFileBoost_Options添加支持预加载的文件类型。 |
| OpenFileBoost_ErrCode HMS_Preview_OpenFileBoost_OptionsDestroy (OpenFileBoost_Options *options) | 销毁OpenFileBoost_Options。 |
| OpenFileBoost_ErrCode HMS_Preview_OpenFileBoost_RegisterFilePreloadWithOption (HMS_OpenFileBoost_QueryAppState queryAppState, HMS_OpenFileBoost_OnFilePreload filePreload, HMS_OpenFileBoost_OnFilePreload cancelFilePreload, OpenFileBoost_Options *options) | 注册预加载回调，允许应用传入支持预加载的文件信息。 |
| bool HMS_Preview_OpenFileBoost_IsEnabled (void) | 查询应用加速特性是否使能。 |
| OpenFileBoost_ErrCode HMS_Preview_OpenFileBoost_FileOperationInfoCreate (const char *path, uint32_t pathLen, const char *operation, uint32_t operationLen, OpenFileBoost_FileOperationInfo **outFileOperationInfo) | 创建OpenFileBoost_FileOperationInfo。 |
| OpenFileBoost_ErrCode HMS_Preview_OpenFileBoost_FileOperationInfoDestroy (OpenFileBoost_FileOperationInfo *fileOperationInfo) | 销毁OpenFileBoost_FileOperationInfo。 |
| OpenFileBoost_ErrCode HMS_Preview_OpenFileBoost_NotifyFileOperation (OpenFileBoost_FileOperationInfo *fileOperationInfo) | 当用户对文件进行操作时，App调用该接口通知系统文件操作类型，这将有助于提高预加载文件预测的准确性。 |
