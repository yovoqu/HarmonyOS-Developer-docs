# context.h

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-context-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

提供上下文数据结构[AbilityRuntime_Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-abilityruntime-context)和相关接口用于获取当前上下文的应用文件路径、数据加密等级和进程名等信息。
 
**引用文件：** <AbilityKit/ability_runtime/context.h>
 
**库：** libability_runtime.so
 
**系统能力：** SystemCapability.Ability.AbilityRuntime.Core
 
**起始版本：** 24
 
**相关模块：** [AbilityRuntime](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 结构体

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| AbilityRuntime_Context | - | 定义AbilityRuntime_Context结构体类型。 |
| AbilityRuntime_Context* | AbilityRuntime_ContextHandle | 定义AbilityRuntime_Context对象指针。 |
 
 
  

##### 函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetCacheDir(AbilityRuntime_ContextHandle context, char* buffer, int32_t bufferSize, int32_t* writeLength) | 获取上下文的缓存目录。 |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetTempDir(AbilityRuntime_ContextHandle context, char* buffer, const int32_t bufferSize, int32_t* writeLength) | 获取上下文的临时文件目录。 |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetFilesDir(AbilityRuntime_ContextHandle context, char* buffer, const int32_t bufferSize, int32_t* writeLength) | 获取上下文的通用文件目录。 |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetDatabaseDir(AbilityRuntime_ContextHandle context, char* buffer, const int32_t bufferSize, int32_t* writeLength) | 获取上下文的数据库文件目录。 |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetPreferencesDir(AbilityRuntime_ContextHandle context, char* buffer, const int32_t bufferSize, int32_t* writeLength) | 获取上下文的首选项文件目录。 |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetBundleCodeDir(AbilityRuntime_ContextHandle context, char* buffer, const int32_t bufferSize, int32_t* writeLength) | 获取上下文的安装文件目录。 |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetDistributedFilesDir(AbilityRuntime_ContextHandle context, char* buffer, const int32_t bufferSize, int32_t* writeLength) | 获取上下文的分布式文件目录。 |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetResourceDir(AbilityRuntime_ContextHandle context, char* buffer, const int32_t bufferSize, int32_t* writeLength) | 获取上下文的资源目录。 |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetCloudFileDir(AbilityRuntime_ContextHandle context, char* buffer, const int32_t bufferSize, int32_t* writeLength) | 获取上下文的云文件目录。 |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetAreaMode(AbilityRuntime_ContextHandle context, AbilityRuntime_AreaMode* areaMode) | 获取上下文的数据加密等级。 |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_SetAreaMode(AbilityRuntime_ContextHandle context, AbilityRuntime_AreaMode areaMode) | 设置上下文的数据加密等级。 |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetLogFileDir(AbilityRuntime_ContextHandle context, char* buffer, const int32_t bufferSize, int32_t* writeLength) | 获取上下文的日志文件目录。 |
| AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetProcessName(AbilityRuntime_ContextHandle context, char* buffer, int32_t bufferSize, int32_t* writeLength) | 获取上下文所在的进程名称。 |
 
 
  

##### 函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### OH_AbilityRuntime_Context_GetCacheDir()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetCacheDir(
    AbilityRuntime_ContextHandle context, char* buffer, int32_t bufferSize, int32_t* writeLength)
```
 
**描述**
 
获取上下文的缓存目录。
 
**起始版本：** 24
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| AbilityRuntime_ContextHandle context | 要获取缓存目录的上下文。 |
| char* buffer | 指向缓冲区的指针，用于接收上下文的缓存目录。 |
| int32_t bufferSize | 缓冲区大小，单位为字节。 |
| int32_t* writeLength | 在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示实际写入到缓冲区的字符串长度，单位为字节。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | 返回执行结果。 ABILITY_RUNTIME_ERROR_CODE_NO_ERROR - 操作成功。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID - 入参buffer或writeLength为空或context为空，或缓冲区大小小于需要写入的大小。 ABILITY_RUNTIME_ERROR_CODE_CONTEXT_NOT_EXIST - 上下文不存在。 |
 
 
**示例代码：**
 
```text
#include <AbilityKit/ability_runtime/context.h>

// 接收一个context 对象
void testGetCacheDir(AbilityRuntime_ContextHandle context)
{
    char buffer[1024] = {0};
    int32_t cacheDirSize = 0;
    AbilityRuntime_ErrorCode errorCode = ABILITY_RUNTIME_ERROR_CODE_NO_ERROR;
    errorCode = OH_AbilityRuntime_Context_GetCacheDir(context, buffer, 1024, &cacheDirSize);
    if (errorCode != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 正常业务处理
}
```
 
  

##### OH_AbilityRuntime_Context_GetTempDir()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetTempDir(
    AbilityRuntime_ContextHandle context, char* buffer, const int32_t bufferSize, int32_t* writeLength)
```
 
**描述**
 
获取上下文的临时文件目录。
 
**起始版本：** 24
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| AbilityRuntime_ContextHandle context | 要获取临时文件目录的上下文。 |
| char* buffer | 指向缓冲区的指针，用于接收上下文的临时文件目录。 |
| const int32_t bufferSize | 缓冲区大小，单位为字节。 |
| int32_t* writeLength | 在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示实际写入到缓冲区的字符串长度，单位为字节。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | 返回执行结果。 ABILITY_RUNTIME_ERROR_CODE_NO_ERROR - 操作成功。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID - 入参buffer或writeLength为空或context为空，或缓冲区大小小于需要写入的大小。 ABILITY_RUNTIME_ERROR_CODE_CONTEXT_NOT_EXIST - 上下文不存在。 |
 
 
**示例代码：**
 
```text
#include <AbilityKit/ability_runtime/context.h>

// 接收一个context 对象
void testGetTempDir(AbilityRuntime_ContextHandle context)
{
    char buffer[1024] = {0};
    int32_t tempDirSize = 0;
    AbilityRuntime_ErrorCode errorCode = ABILITY_RUNTIME_ERROR_CODE_NO_ERROR;
    errorCode = OH_AbilityRuntime_Context_GetTempDir(context, buffer, 1024, &tempDirSize);
    if (errorCode != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 正常业务处理
}
```
 
  

##### OH_AbilityRuntime_Context_GetFilesDir()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetFilesDir(
    AbilityRuntime_ContextHandle context, char* buffer, const int32_t bufferSize, int32_t* writeLength)
```
 
**描述**
 
获取上下文的通用文件目录。
 
**起始版本：** 24
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| AbilityRuntime_ContextHandle context | 要获取通用文件目录的上下文。 |
| char* buffer | 指向缓冲区的指针，用于接收上下文的通用文件目录。 |
| const int32_t bufferSize | 缓冲区大小，单位为字节。 |
| int32_t* writeLength | 在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示实际写入到缓冲区的字符串长度，单位为字节。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | 返回执行结果。 ABILITY_RUNTIME_ERROR_CODE_NO_ERROR - 操作成功。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID - 入参buffer或writeLength为空或context为空，或缓冲区大小小于需要写入的大小。 ABILITY_RUNTIME_ERROR_CODE_CONTEXT_NOT_EXIST - 上下文不存在。 |
 
 
**示例代码：**
 
```text
#include <AbilityKit/ability_runtime/context.h>

// 接收一个context 对象
void testGetFilesDir(AbilityRuntime_ContextHandle context)
{
    char buffer[1024] = {0};
    int32_t filesDirSize = 0;
    AbilityRuntime_ErrorCode errorCode = ABILITY_RUNTIME_ERROR_CODE_NO_ERROR;
    errorCode = OH_AbilityRuntime_Context_GetFilesDir(context, buffer, 1024, &filesDirSize);
    if (errorCode != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 正常业务处理
}
```
 
  

##### OH_AbilityRuntime_Context_GetDatabaseDir()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetDatabaseDir(
    AbilityRuntime_ContextHandle context, char* buffer, const int32_t bufferSize, int32_t* writeLength)
```
 
**描述**
 
获取上下文的数据库文件目录。
 
**起始版本：** 24
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| AbilityRuntime_ContextHandle context | 要获取数据库文件目录的上下文。 |
| char* buffer | 指向缓冲区的指针，用于接收上下文的数据库文件目录。 |
| const int32_t bufferSize | 缓冲区大小，单位为字节。 |
| int32_t* writeLength | 在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示实际写入到缓冲区的字符串长度，单位为字节。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | 返回执行结果。 ABILITY_RUNTIME_ERROR_CODE_NO_ERROR - 操作成功。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID - 入参buffer或writeLength为空或context为空，或缓冲区大小小于需要写入的大小。 ABILITY_RUNTIME_ERROR_CODE_CONTEXT_NOT_EXIST - 上下文不存在。 |
 
 
**示例代码：**
 
```text
#include <AbilityKit/ability_runtime/context.h>

// 接收一个context 对象
void testGetDatabaseDir(AbilityRuntime_ContextHandle context)
{
    char buffer[1024] = {0};
    int32_t databaseDirSize = 0;
    AbilityRuntime_ErrorCode errorCode = ABILITY_RUNTIME_ERROR_CODE_NO_ERROR;
    errorCode = OH_AbilityRuntime_Context_GetDatabaseDir(context, buffer, 1024, &databaseDirSize);
    if (errorCode != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 正常业务处理
}
```
 
  

##### OH_AbilityRuntime_Context_GetPreferencesDir()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetPreferencesDir(
    AbilityRuntime_ContextHandle context, char* buffer, const int32_t bufferSize, int32_t* writeLength)
```
 
**描述**
 
获取上下文的首选项文件目录。
 
**起始版本：** 24
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| AbilityRuntime_ContextHandle context | 要获取首选项文件目录的上下文。 |
| char* buffer | 指向缓冲区的指针，用于接收上下文的首选项文件目录。 |
| const int32_t bufferSize | 缓冲区大小，单位为字节。 |
| int32_t* writeLength | 在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示实际写入到缓冲区的字符串长度，单位为字节。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | 返回执行结果。 ABILITY_RUNTIME_ERROR_CODE_NO_ERROR - 操作成功。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID - 入参buffer或writeLength为空或context为空，或缓冲区大小小于需要写入的大小。 ABILITY_RUNTIME_ERROR_CODE_CONTEXT_NOT_EXIST - 上下文不存在。 |
 
 
**示例代码：**
 
```text
#include <AbilityKit/ability_runtime/context.h>

// 接收一个context 对象
void testGetPreferencesDir(AbilityRuntime_ContextHandle context)
{
    char buffer[1024] = {0};
    int32_t preferencesDirSize = 0;
    AbilityRuntime_ErrorCode errorCode = ABILITY_RUNTIME_ERROR_CODE_NO_ERROR;
    errorCode = OH_AbilityRuntime_Context_GetPreferencesDir(context, buffer, 1024, &preferencesDirSize);
    if (errorCode != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 正常业务处理
}
```
 
  

##### OH_AbilityRuntime_Context_GetBundleCodeDir()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetBundleCodeDir(
    AbilityRuntime_ContextHandle context, char* buffer, const int32_t bufferSize, int32_t* writeLength)
```
 
**描述**
 
获取上下文的安装文件目录。
 
**起始版本：** 24
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| AbilityRuntime_ContextHandle context | 要获取安装文件目录的上下文。 |
| char* buffer | 指向缓冲区的指针，用于接收上下文的安装文件目录。 |
| const int32_t bufferSize | 缓冲区大小，单位为字节。 |
| int32_t* writeLength | 在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示实际写入到缓冲区的字符串长度，单位为字节。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | 返回执行结果。 ABILITY_RUNTIME_ERROR_CODE_NO_ERROR - 操作成功。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID - 入参buffer或writeLength为空或context为空，或缓冲区大小小于需要写入的大小。 ABILITY_RUNTIME_ERROR_CODE_CONTEXT_NOT_EXIST - 上下文不存在。 |
 
 
**示例代码：**
 
```text
#include <AbilityKit/ability_runtime/context.h>

// 接收一个context 对象
void testGetBundleCodeDir(AbilityRuntime_ContextHandle context)
{
    char buffer[1024] = {0};
    int32_t bundleCodeDirSize = 0;
    AbilityRuntime_ErrorCode errorCode = ABILITY_RUNTIME_ERROR_CODE_NO_ERROR;
    errorCode = OH_AbilityRuntime_Context_GetBundleCodeDir(context, buffer, 1024, &bundleCodeDirSize);
    if (errorCode != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 正常业务处理
}
```
 
  

##### OH_AbilityRuntime_Context_GetDistributedFilesDir()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetDistributedFilesDir(
    AbilityRuntime_ContextHandle context, char* buffer, const int32_t bufferSize, int32_t* writeLength)
```
 
**描述**
 
获取上下文的分布式文件目录。
 
**起始版本：** 24
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| AbilityRuntime_ContextHandle context | 要获取分布式文件目录的上下文。 |
| char* buffer | 指向缓冲区的指针，用于接收上下文的分布式文件目录。 |
| const int32_t bufferSize | 缓冲区大小，单位为字节。 |
| int32_t* writeLength | 在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示实际写入到缓冲区的字符串长度，单位为字节。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | 返回执行结果。 ABILITY_RUNTIME_ERROR_CODE_NO_ERROR - 操作成功。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID - 入参buffer或writeLength为空或context为空，或缓冲区大小小于需要写入的大小。 ABILITY_RUNTIME_ERROR_CODE_CONTEXT_NOT_EXIST - 上下文不存在。 |
 
 
**示例代码：**
 
```text
#include <AbilityKit/ability_runtime/context.h>

// 接收一个context 对象
void testGetDistributedFilesDir(AbilityRuntime_ContextHandle context)
{
    char buffer[1024] = {0};
    int32_t distributedFilesDirSize = 0;
    AbilityRuntime_ErrorCode errorCode = ABILITY_RUNTIME_ERROR_CODE_NO_ERROR;
    errorCode = OH_AbilityRuntime_Context_GetDistributedFilesDir(context, buffer, 1024, &distributedFilesDirSize);
    if (errorCode != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 正常业务处理
}
```
 
  

##### OH_AbilityRuntime_Context_GetResourceDir()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetResourceDir(
    AbilityRuntime_ContextHandle context, char* buffer, const int32_t bufferSize, int32_t* writeLength)
```
 
**描述**
 
获取上下文的资源目录。
 
**起始版本：** 24
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| AbilityRuntime_ContextHandle context | 要获取资源目录的上下文。 |
| char* buffer | 指向缓冲区的指针，用于接收上下文的资源目录。 |
| const int32_t bufferSize | 缓冲区大小，单位为字节。 |
| int32_t* writeLength | 在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示实际写入到缓冲区的字符串长度，单位为字节。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | 返回执行结果。 ABILITY_RUNTIME_ERROR_CODE_NO_ERROR - 操作成功。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID - 入参buffer或writeLength为空或context为空，或缓冲区大小小于需要写入的大小。 ABILITY_RUNTIME_ERROR_CODE_CONTEXT_NOT_EXIST - 上下文不存在。 |
 
 
**示例代码：**
 
```text
#include <AbilityKit/ability_runtime/context.h>

// 接收一个context 对象
void testGetResourceDir(AbilityRuntime_ContextHandle context)
{
    char buffer[1024] = {0};
    int32_t resourceDirSize = 0;
    AbilityRuntime_ErrorCode errorCode = ABILITY_RUNTIME_ERROR_CODE_NO_ERROR;
    errorCode = OH_AbilityRuntime_Context_GetResourceDir(context, buffer, 1024, &resourceDirSize);
    if (errorCode != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 正常业务处理
}
```
 
  

##### OH_AbilityRuntime_Context_GetCloudFileDir()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetCloudFileDir(
    AbilityRuntime_ContextHandle context, char* buffer, const int32_t bufferSize, int32_t* writeLength)
```
 
**描述**
 
获取上下文的云文件目录。
 
**起始版本：** 24
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| AbilityRuntime_ContextHandle context | 要获取云文件目录的上下文。 |
| char* buffer | 指向缓冲区的指针，用于接收上下文的云文件目录。 |
| const int32_t bufferSize | 缓冲区大小，单位为字节。 |
| int32_t* writeLength | 在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示实际写入到缓冲区的字符串长度，单位为字节。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | 返回执行结果。 ABILITY_RUNTIME_ERROR_CODE_NO_ERROR - 操作成功。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID - 入参buffer或writeLength为空或context为空，或缓冲区大小小于需要写入的大小。 ABILITY_RUNTIME_ERROR_CODE_CONTEXT_NOT_EXIST - 上下文不存在。 |
 
 
**示例代码：**
 
```text
#include <AbilityKit/ability_runtime/context.h>

// 接收一个context 对象
void testGetCloudFileDir(AbilityRuntime_ContextHandle context)
{
    char buffer[1024] = {0};
    int32_t cloudFileDirSize = 0;
    AbilityRuntime_ErrorCode errorCode = ABILITY_RUNTIME_ERROR_CODE_NO_ERROR;
    errorCode = OH_AbilityRuntime_Context_GetCloudFileDir(context, buffer, 1024, &cloudFileDirSize);
    if (errorCode != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 正常业务处理
}
```
 
  

##### OH_AbilityRuntime_Context_GetAreaMode()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetAreaMode(
    AbilityRuntime_ContextHandle context, AbilityRuntime_AreaMode* areaMode)
```
 
**描述**
 
获取上下文的数据加密等级。
 
**起始版本：** 24
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| AbilityRuntime_ContextHandle context | 要获取数据加密等级的上下文。 |
| AbilityRuntime_AreaMode* areaMode | 指向接收数据加密等级的指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | 返回执行结果。 ABILITY_RUNTIME_ERROR_CODE_NO_ERROR - 操作成功。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID - 入参areaMode为空。 ABILITY_RUNTIME_ERROR_CODE_CONTEXT_NOT_EXIST - 上下文不存在。 |
 
 
**示例代码：**
 
```text
#include <AbilityKit/ability_runtime/context.h>

// 接收一个context 对象
void testGetAreaMode(AbilityRuntime_ContextHandle context)
{
    AbilityRuntime_AreaMode areaMode;
    AbilityRuntime_ErrorCode errorCode = ABILITY_RUNTIME_ERROR_CODE_NO_ERROR;
    errorCode = OH_AbilityRuntime_Context_GetAreaMode(context, &areaMode);
    if (errorCode != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 正常业务处理
}
```
 
  

##### OH_AbilityRuntime_Context_SetAreaMode()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_SetAreaMode(
    AbilityRuntime_ContextHandle context, AbilityRuntime_AreaMode areaMode)
```
 
**描述**
 
设置上下文的数据加密等级。
 
**起始版本：** 24
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| AbilityRuntime_ContextHandle context | 要设置数据加密等级的上下文。 |
| AbilityRuntime_AreaMode areaMode | 数据加密等级。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | 返回执行结果。 ABILITY_RUNTIME_ERROR_CODE_NO_ERROR - 操作成功。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID - 入参areaMode为空。 ABILITY_RUNTIME_ERROR_CODE_CONTEXT_NOT_EXIST - 上下文不存在。 |
 
 
**示例代码：**
 
```text
#include <AbilityKit/ability_runtime/context.h>

// 接收一个context 对象
void testSetAreaMode(AbilityRuntime_ContextHandle context)
{
    AbilityRuntime_AreaMode areaMode = ABILITY_RUNTIME_AREA_MODE_EL1;
    AbilityRuntime_ErrorCode errorCode = ABILITY_RUNTIME_ERROR_CODE_NO_ERROR;
    errorCode = OH_AbilityRuntime_Context_SetAreaMode(context, areaMode);
    if (errorCode != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 正常业务处理
}
```
 
  

##### OH_AbilityRuntime_Context_GetLogFileDir()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetLogFileDir(
    AbilityRuntime_ContextHandle context, char* buffer, const int32_t bufferSize, int32_t* writeLength)
```
 
**描述**
 
获取上下文的日志文件目录。
 
**起始版本：** 24
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| AbilityRuntime_ContextHandle context | 要获取日志文件目录的上下文。 |
| char* buffer | 指向缓冲区的指针，用于接收上下文的日志文件目录。 |
| const int32_t bufferSize | 缓冲区大小，单位为字节。 |
| int32_t* writeLength | 在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示实际写入到缓冲区的字符串长度，单位为字节。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | 返回执行结果。 ABILITY_RUNTIME_ERROR_CODE_NO_ERROR - 操作成功。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID - 入参buffer或writeLength为空或context为空，或缓冲区大小小于需要写入的大小。 ABILITY_RUNTIME_ERROR_CODE_CONTEXT_NOT_EXIST - 上下文不存在。 |
 
 
**示例代码：**
 
```text
#include <AbilityKit/ability_runtime/context.h>

// 接收一个context 对象
void testGetLogFileDir(AbilityRuntime_ContextHandle context)
{
    char buffer[1024] = {0};
    int32_t logFileDirSize = 0;
    AbilityRuntime_ErrorCode errorCode = ABILITY_RUNTIME_ERROR_CODE_NO_ERROR;
    errorCode = OH_AbilityRuntime_Context_GetLogFileDir(context, buffer, 1024, &logFileDirSize);
    if (errorCode != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 正常业务处理
}
```
 
  

##### OH_AbilityRuntime_Context_GetProcessName()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetProcessName(
    AbilityRuntime_ContextHandle context, char* buffer, int32_t bufferSize, int32_t* writeLength)
```
 
**描述**
 
获取上下文所在的进程名称。
 
**起始版本：** 24
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| AbilityRuntime_ContextHandle context | 要获取进程名称的上下文。 |
| char* buffer | 指向缓冲区的指针，用于接收进程名称。 |
| int32_t bufferSize | 缓冲区大小，单位为字节。 |
| int32_t* writeLength | 在返回ABILITY_RUNTIME_ERROR_CODE_NO_ERROR时，表示实际写入到缓冲区的字符串长度，单位为字节。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| AbilityRuntime_ErrorCode | 返回执行结果。 ABILITY_RUNTIME_ERROR_CODE_NO_ERROR - 操作成功。 ABILITY_RUNTIME_ERROR_CODE_PARAM_INVALID - 入参buffer或writeLength为空或context为空，或缓冲区大小小于需要写入的大小。 ABILITY_RUNTIME_ERROR_CODE_CONTEXT_NOT_EXIST - 上下文不存在。 |
 
 
**示例代码：**
 
```text
#include <AbilityKit/ability_runtime/context.h>

// 接收一个context 对象
void testGetProcessName(AbilityRuntime_ContextHandle context)
{
    char buffer[1024] = {0};
    int32_t processNameSize = 0;
    AbilityRuntime_ErrorCode errorCode = ABILITY_RUNTIME_ERROR_CODE_NO_ERROR;
    errorCode = OH_AbilityRuntime_Context_GetProcessName(context, buffer, 1024, &processNameSize);
    if (errorCode != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 正常业务处理
}
```
