# oh_device_manager.h

更新时间：2026-08-04 06:06:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-device-manager-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

提供访问可信设备和本地设备信息的接口。
 
**引用文件：** <distributedhardware/device_manager/oh_device_manager.h>
 
**库：** libdevicemanager_ndk.so
 
**系统能力：** SystemCapability.DistributedHardware.DeviceManager
 
**起始版本：** 20
 
**相关模块：** [DeviceManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-devicemanager)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| int32_t OH_DeviceManager_GetLocalDeviceName(char **localDeviceName, unsigned int &len) | 获取本地设备显示名。 设备显示名称涉及用户的隐私数据，需要应用提供相关隐私声明，声明设备显示名的用途。 |
| int32_t OH_DeviceManager_GetLocalDeviceNameC(char **localDeviceName, unsigned int *len) | 获取本地设备显示名。 设备显示名称涉及用户的隐私数据，需要应用提供相关隐私声明，声明设备显示名的用途。 |
 
 
  

#### 函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### OH_DeviceManager_GetLocalDeviceName()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_DeviceManager_GetLocalDeviceName(char **localDeviceName, unsigned int &len)
```
 
**描述**
 
获取本地设备显示名。
 
 设备显示名称涉及用户的隐私数据，需要应用提供相关隐私声明，声明设备显示名的用途。
 
**需要权限：** ohos.permission.READ_LOCAL_DEVICE_NAME
 
**起始版本：** 20
 
**废弃版本：** 26.0.0
 
**替代接口：** [OH_DeviceManager_GetLocalDeviceNameC](#oh_devicemanager_getlocaldevicenamec)
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| char **localDeviceName | 表示本地设备显示名字符串的地址指针。使用后需要手动释放空间资源。应用具备ohos.permission.READ_LOCAL_DEVICE_NAME权限，返回设备显示名称；否则返回设备默认名称。 |
| unsigned int &len | 表示本地设备显示名字符串的长度。单位：字节 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的错误码。错误码定义详见DeviceManager_ErrorCode。 返回ERR_OK，表示执行成功。 返回DM_ERR_FAILED，表示函数执行失败。 返回DM_ERR_OBTAIN_SERVICE，表示获取设备管理服务失败。 返回DM_ERR_OBTAIN_BUNDLE_NAME，表示获取bundleName失败。 返回ERR_INVALID_PARAMETER，表示参数localDeviceName是空指针或者*localDeviceName是非空指针。 |
 
 
  

#### OH_DeviceManager_GetLocalDeviceNameC()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_DeviceManager_GetLocalDeviceNameC(char **localDeviceName, unsigned int *len)
```
 
**描述**
 
获取本地设备显示名。
 
 设备显示名称涉及用户的隐私数据，需要应用提供相关隐私声明，声明设备显示名的用途。
 
**需要权限：** ohos.permission.READ_LOCAL_DEVICE_NAME
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| char **localDeviceName | 表示本地设备显示名字符串的地址指针。使用后需要手动释放空间资源。应用具备ohos.permission.READ_LOCAL_DEVICE_NAME权限，返回设备显示名称；否则返回设备默认名称。 |
| unsigned int *len | 表示本地设备显示名字符串长度的地址指针。使用后需要手动释放空间资源。单位：字节 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的错误码。错误码定义详见DeviceManager_ErrorCode。 返回ERR_OK，表示执行成功。 返回DM_ERR_FAILED，表示函数执行失败。 返回DM_ERR_OBTAIN_SERVICE，表示获取设备管理服务失败。 返回DM_ERR_OBTAIN_BUNDLE_NAME，表示获取bundleName失败。 返回ERR_INVALID_PARAMETER，表示参数localDeviceName是空指针或者*localDeviceName是非空指针或者len是空指针。 |
