# ddk_api.h

更新时间：2026-04-28 03:31:56

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ddk-api-h
**支持设备：** PC/2in1


## 概述
**支持设备：** PC/2in1

声明主机侧访问的Base DDK接口。

**引用文件：** <ddk/ddk_api.h>

**库：** libddk_base.z.so

**系统能力：** SystemCapability.Driver.DDK.Extension

**起始版本：** 12

**相关模块：** [Ddk](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-baseddk)


## 汇总
**支持设备：** PC/2in1


### 函数
**支持设备：** PC/2in1


| 名称 | 描述 |
| --- | --- |
| [DDK_RetCode OH_DDK_CreateAshmem(const uint8_t *name, uint32_t size, DDK_Ashmem **ashmem)](#oh_ddk_createashmem) | 创建共享内存。为了防止资源泄漏，通过调用[OH_DDK_DestroyAshmem](#oh_ddk_destroyashmem)接口来销毁不再需要的共享内存。 |
| [DDK_RetCode OH_DDK_MapAshmem(DDK_Ashmem *ashmem, const uint8_t ashmemMapType)](#oh_ddk_mapashmem) | 映射创建的共享内存到用户空间。通过调用[OH_DDK_UnmapAshmem](#oh_ddk_unmapashmem)接口取消映射不需要的共享内存。 |
| [DDK_RetCode OH_DDK_UnmapAshmem(DDK_Ashmem *ashmem)](#oh_ddk_unmapashmem) | 取消映射共享内存。 |
| [DDK_RetCode OH_DDK_DestroyAshmem(DDK_Ashmem *ashmem)](#oh_ddk_destroyashmem) | 销毁共享内存。 |


## 函数说明
**支持设备：** PC/2in1


### OH_DDK_CreateAshmem()
**支持设备：** PC/2in1


```text
DDK_RetCode OH_DDK_CreateAshmem(const uint8_t *name, uint32_t size, DDK_Ashmem **ashmem)
```

**描述**

创建共享内存。为了防止资源泄漏，通过调用[OH_DDK_DestroyAshmem](#oh_ddk_destroyashmem)接口来销毁不再需要的共享内存。

**起始版本：** 12

**参数：**


| 参数项 | 描述 |
| --- | --- |
| const uint8_t *name | 指向要创建的共享内存的指针。 |
| uint32_t size | 共享内存对应的缓冲区大小。 |
| [DDK_Ashmem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-baseddk-ddk-ashmem) **ashmem | 指向创建的共享内存的指针。 |


**返回：**


| 类型 | 说明 |
| --- | --- |
| [DDK_RetCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ddk-types-h#ddk_retcode) | [DDK_SUCCESS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ddk-types-h#ddk_retcode) 调用接口成功。  [DDK_INVALID_PARAMETER](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ddk-types-h#ddk_retcode) 入参name为空指针，size的大小为0或者入参ashmem是空指针。  [DDK_FAILURE](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ddk-types-h#ddk_retcode) 创建共享内存失败或者创建结构体DDK_Ashmem失败。 |


### OH_DDK_MapAshmem()
**支持设备：** PC/2in1


```text
DDK_RetCode OH_DDK_MapAshmem(DDK_Ashmem *ashmem, const uint8_t ashmemMapType)
```

**描述**

映射创建的共享内存到用户空间。通过调用[OH_DDK_UnmapAshmem](#oh_ddk_unmapashmem)接口取消映射不需要的共享内存。

**起始版本：** 12

**参数：**


| 参数项 | 描述 |
| --- | --- |
| [DDK_Ashmem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-baseddk-ddk-ashmem) *ashmem | 要映射的共享内存指针。 |
| const uint8_t ashmemMapType | 共享内存的保护权限值。 |


**返回：**


| 类型 | 说明 |
| --- | --- |
| [DDK_RetCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ddk-types-h#ddk_retcode) | [DDK_SUCCESS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ddk-types-h#ddk_retcode) 调用接口成功。  [DDK_NULL_PTR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ddk-types-h#ddk_retcode) 入参ashmem为空指针。  [DDK_FAILURE](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ddk-types-h#ddk_retcode) 共享内存的文件描述符无效。  [DDK_INVALID_OPERATION](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ddk-types-h#ddk_retcode) 调用接口MapAshmem失败。 |


### OH_DDK_UnmapAshmem()
**支持设备：** PC/2in1


```text
DDK_RetCode OH_DDK_UnmapAshmem(DDK_Ashmem *ashmem)
```

**描述**

取消映射共享内存。

**起始版本：** 12

**参数：**


| 参数项 | 描述 |
| --- | --- |
| [DDK_Ashmem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-baseddk-ddk-ashmem) *ashmem | 要取消映射的共享内存指针。 |


**返回：**


| 类型 | 说明 |
| --- | --- |
| [DDK_RetCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ddk-types-h#ddk_retcode) | [DDK_SUCCESS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ddk-types-h#ddk_retcode) 调用接口成功。  [DDK_NULL_PTR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ddk-types-h#ddk_retcode) 入参ashmem为空指针。  [DDK_FAILURE](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ddk-types-h#ddk_retcode) 共享内存的文件描述符无效。 |


### OH_DDK_DestroyAshmem()
**支持设备：** PC/2in1


```text
DDK_RetCode OH_DDK_DestroyAshmem(DDK_Ashmem *ashmem)
```

**描述**

销毁共享内存。

**起始版本：** 12

**参数：**


| 参数项 | 描述 |
| --- | --- |
| [DDK_Ashmem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-baseddk-ddk-ashmem) *ashmem | 要销毁的共享内存指针。 |


**返回：**


| 类型 | 说明 |
| --- | --- |
| [DDK_RetCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ddk-types-h#ddk_retcode) | [DDK_SUCCESS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ddk-types-h#ddk_retcode) 调用接口成功。  [DDK_NULL_PTR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ddk-types-h#ddk_retcode) 入参ashmem为空指针。  [DDK_FAILURE](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ddk-types-h#ddk_retcode) 共享内存的文件描述符无效。 |
