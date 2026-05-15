# DeviceSecurityMode

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-devicesecuritymode
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

DeviceSecurityMode模块用于管理设备安全模式。

**系统能力：** SystemCapability.Security.SafetyDetect

**起始版本：** 5.0.1(13)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


### 文件
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


| 名称 | 描述 |
| --- | --- |
| [device_security_mode.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-device-security-mode-8h) | 定义与设备安全模式相关的函数。 |


### 类型定义
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


| 名称 | 描述 |
| --- | --- |
| typedef enum [DSM_DeviceSecurityMode](#dsm_devicesecuritymode-1) [DSM_DeviceSecurityMode](#dsm_devicesecuritymode) | 设备安全模式枚举类型定义。 |


### 枚举
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


| 名称 | 描述 |
| --- | --- |
| [DSM_DeviceSecurityMode](#dsm_devicesecuritymode-1) { DSM_NORMAL_MODE = 0, DSM_SECURE_SHIELD_MODE = 1 } | 设备安全模式枚举值。 |


### 函数
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


| 名称 | 描述 |
| --- | --- |
| [DSM_DeviceSecurityMode](#dsm_devicesecuritymode-1) [HMS_DSM_GetDeviceSecurityMode()](#hms_dsm_getdevicesecuritymode) | 查询当前设备安全模式。 |


## 类型定义说明
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


### DSM_DeviceSecurityMode
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


```cpp
typedef enum DSM_DeviceSecurityMode DSM_DeviceSecurityMode
```

**描述**

设备安全模式枚举类型定义。

**起始版本：** 5.0.1(13)


## 枚举说明
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


### DSM_DeviceSecurityMode
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


```cpp
enum DSM_DeviceSecurityMode
```

**描述**

枚举设备安全模式。

**起始版本：** 5.0.1(13)


| 枚举值 | 描述 |
| --- | --- |
| DSM_NORMAL_MODE | 一般模式，为设备默认的安全模式。 |
| DSM_SECURE_SHIELD_MODE | 坚盾守护模式，坚盾守护模式用于保护设备不被复杂网络攻击，此模式下部分网页的浏览功能和网络技术会受到限制。 |


## 函数说明
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


### HMS_DSM_GetDeviceSecurityMode()
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


```cpp
DSM_DeviceSecurityMode HMS_DSM_GetDeviceSecurityMode(void)
```

**描述**

查询当前设备的安全模式。

**起始版本：** 5.0.1(13)

**返回：**

返回结果参见枚举类型[DSM_DeviceSecurityMode](#dsm_devicesecuritymode-1)。
