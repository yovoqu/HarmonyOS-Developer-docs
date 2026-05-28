# native_avmemory.h

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avmemory-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

声明了媒体数据结构AVMemory的定义。
 
**引用文件：** <multimedia/player_framework/native_avmemory.h>
 
**库：** libnative_media_core.so
 
**系统能力：** SystemCapability.Multimedia.Media.Core
 
**起始版本：** 9
 
**相关模块：** [Core](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-core)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 结构体

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_AVMemory | OH_AVMemory | 为音视频内存接口定义native层对象。 |
 
 
  

#### 函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| OH_AVMemory *OH_AVMemory_Create(int32_t size) | 创建OH_AVMemory实例的指针。 |
| uint8_t *OH_AVMemory_GetAddr(struct OH_AVMemory *mem) | 获取内存虚拟地址。 |
| int32_t OH_AVMemory_GetSize(struct OH_AVMemory *mem) | 获取内存长度。 |
| OH_AVErrCode OH_AVMemory_Destroy(struct OH_AVMemory *mem) | 释放OH_AVMemory实例指针的资源。 |
 
 
  

#### 函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### OH_AVMemory_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_AVMemory *OH_AVMemory_Create(int32_t size)
```
 
**描述**
 
创建OH_AVMemory实例的指针。
 
**系统能力：** SystemCapability.Multimedia.Media.Core
 
**起始版本：** 10
 
**废弃版本：** 11
 
**替代接口：** [OH_AVBuffer_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avbuffer-h#oh_avbuffer_create)
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| int32_t size | 创建内存的大小，单位字节。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_AVMemory * | 如果创建成功，返回OH_AVMemory实例的指针，如果失败，返回NULL。 使用结束后需要通过OH_AVMemory_Destroy释放内存。 可能的失败原因： 1. size <= 0。 2. 创建OH_AVMemory失败。 3. OH_AVMemory内存分配失败。 |
 
 
  

#### OH_AVMemory_GetAddr()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
uint8_t *OH_AVMemory_GetAddr(struct OH_AVMemory *mem)
```
 
**描述**
 
获取内存虚拟地址。
 
**系统能力：** SystemCapability.Multimedia.Media.Core
 
**起始版本：** 9
 
**废弃版本：** 11
 
**替代接口：** [OH_AVBuffer_GetAddr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avbuffer-h#oh_avbuffer_getaddr)
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| struct OH_AVMemory *mem | 指向OH_AVMemory实例的指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| uint8_t * | 如果内存有效，返回内存的虚拟地址，如果内存无效，返回NULL。 可能的失败原因： 1. 输入mem为空指针。 2. 输入mem参数结构校验失败。 3. 输入mem中内存为空指针。 |
 
 
  

#### OH_AVMemory_GetSize()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_AVMemory_GetSize(struct OH_AVMemory *mem)
```
 
**描述**
 
获取内存长度。
 
**系统能力：** SystemCapability.Multimedia.Media.Core
 
**起始版本：** 9
 
**废弃版本：** 11
 
**替代接口：** [OH_AVBuffer_GetCapacity](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avbuffer-h#oh_avbuffer_getcapacity)
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| struct OH_AVMemory *mem | 指向OH_AVMemory实例的指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 如果内存有效，返回内存长度，如果内存无效，返回-1。 可能的失败原因： 1. 输入mem为空指针。 2. 输入mem参数结构校验失败。 3. 输入mem中内存为空指针。 |
 
 
  

#### OH_AVMemory_Destroy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_AVErrCode OH_AVMemory_Destroy(struct OH_AVMemory *mem)
```
 
**描述**
 
释放OH_AVMemory实例指针的资源。
 
**系统能力：** SystemCapability.Multimedia.Media.Core
 
**起始版本：** 10
 
**废弃版本：** 11
 
**替代接口：** [OH_AVBuffer_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avbuffer-h#oh_avbuffer_destroy)
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| struct OH_AVMemory *mem | 指向OH_AVMemory实例的指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | AV_ERR_OK：释放成功。 AV_ERR_INVALID_VAL： 1. 输入mem为空指针。 2. 输入mem参数结构校验失败。 3. 输入mem不是开发者创建的。 |
