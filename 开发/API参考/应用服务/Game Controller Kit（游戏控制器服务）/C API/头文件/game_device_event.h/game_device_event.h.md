# game_device_event.h

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-game-device-event-h
**支持设备：** Phone | PC/2in1 | Tablet | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | TV

定义游戏设备事件的接口。
 
**引用文件：** <GameControllerKit/game_device_event.h>
 
**库：** libohgame_controller.z.so
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**相关模块：** [GameController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-gamecontroller)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | TV

  

#### 结构体

**支持设备：** Phone | PC/2in1 | Tablet | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| GameDevice_DeviceInfo | GameDevice_DeviceInfo | 定义设备信息。 |
| GameDevice_DeviceEvent | GameDevice_DeviceEvent | 定义设备状态变化事件。 |
 
 
  

#### 枚举

**支持设备：** Phone | PC/2in1 | Tablet | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| GameDevice_StatusChangedType | GameDevice_StatusChangedType | 此枚举定义设备的状态变化类型。 |
| GameDevice_DeviceType | GameDevice_DeviceType | 此枚举定义设备类型。 |
 
 
  

#### 函数

**支持设备：** Phone | PC/2in1 | Tablet | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| typedef void(*GameDevice_DeviceMonitorCallback)(const struct GameDevice_DeviceEvent* deviceEvent) | GameDevice_DeviceMonitorCallback | 定义OH_GameDevice_RegisterDeviceMonitor中使用的回调函数。当设备上线或下线时，该回调函数将被调用。 |
| GameController_ErrorCode OH_GameDevice_DeviceEvent_GetChangedType(const struct GameDevice_DeviceEvent* deviceEvent, GameDevice_StatusChangedType* statusChangedType) | - | 从设备状态变化事件中获取状态变化类型。 |
| GameController_ErrorCode OH_GameDevice_DeviceEvent_GetDeviceInfo(const struct GameDevice_DeviceEvent* deviceEvent, GameDevice_DeviceInfo** deviceInfo) | - | 从设备状态变化事件中获取设备信息。 |
| GameController_ErrorCode OH_GameDevice_DestroyDeviceInfo(GameDevice_DeviceInfo** deviceInfo) | - | 销毁设备信息实例。 |
| GameController_ErrorCode OH_GameDevice_DeviceInfo_GetDeviceId(const struct GameDevice_DeviceInfo* deviceInfo, char** deviceId) | - | 从设备信息中获取设备ID。 |
| GameController_ErrorCode OH_GameDevice_DeviceInfo_GetName(const struct GameDevice_DeviceInfo* deviceInfo, char** name) | - | 从设备信息中获取设备名称。 |
| GameController_ErrorCode OH_GameDevice_DeviceInfo_GetProduct(const struct GameDevice_DeviceInfo* deviceInfo, int32_t* product) | - | 从设备信息中获取产品信息。 |
| GameController_ErrorCode OH_GameDevice_DeviceInfo_GetVersion(const struct GameDevice_DeviceInfo* deviceInfo, int32_t* version) | - | 从设备信息中获取版本信息。 |
| GameController_ErrorCode OH_GameDevice_DeviceInfo_GetPhysicalAddress(const struct GameDevice_DeviceInfo* deviceInfo, char** physicalAddress) | - | 从设备信息中获取物理地址。 |
| GameController_ErrorCode OH_GameDevice_DeviceInfo_GetDeviceType(const struct GameDevice_DeviceInfo* deviceInfo, GameDevice_DeviceType* deviceType) | - | 从设备信息中获取设备类型。 |
 
 
  

#### 枚举类型说明

**支持设备：** Phone | PC/2in1 | Tablet | TV

  

#### GameDevice_StatusChangedType

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
enum GameDevice_StatusChangedType
```
 
**描述**
 
此枚举定义设备的状态变化类型。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
  
| 枚举项 | 描述 |
| --- | --- |
| OFFLINE = 0 | 设备下线。 起始版本： 21 |
| ONLINE = 1 | 设备上线。 起始版本： 21 |
 
 
  

#### GameDevice_DeviceType

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
enum GameDevice_DeviceType
```
 
**描述**
 
此枚举定义设备类型。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
  
| 枚举项 | 描述 |
| --- | --- |
| UNKNOWN = 0 | 未知。 起始版本： 21 |
| GAME_PAD = 1 | 游戏手柄。 起始版本： 21 |
 
 
  

#### 函数说明

**支持设备：** Phone | PC/2in1 | Tablet | TV

  

#### GameDevice_DeviceMonitorCallback()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
typedef void(*GameDevice_DeviceMonitorCallback)(const struct GameDevice_DeviceEvent* deviceEvent)
```
 
**描述**
 
定义[OH_GameDevice_RegisterDeviceMonitor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-game-device-h#oh_gamedevice_registerdevicemonitor)中使用的回调函数。当设备上线或下线时，该回调函数将被调用。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| (const struct GameDevice_DeviceEvent* deviceEvent) | 输出参数。设备状态变化事件GameDevice_DeviceEvent。 |
 
 
  

#### OH_GameDevice_DeviceEvent_GetChangedType()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GameDevice_DeviceEvent_GetChangedType(const struct GameDevice_DeviceEvent* deviceEvent, GameDevice_StatusChangedType* statusChangedType)
```
 
**描述**
 
从设备状态变化事件中获取状态变化类型。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| const struct GameDevice_DeviceEvent* deviceEvent | 指针指向GameDevice_DeviceEvent实例，不能为空。 |
| GameDevice_StatusChangedType* statusChangedType | 输出参数，设备状态变化类型。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数deviceEvent为null，返回GAME_CONTROLLER_PARAM_ERROR。 |
 
 
  

#### OH_GameDevice_DeviceEvent_GetDeviceInfo()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GameDevice_DeviceEvent_GetDeviceInfo(const struct GameDevice_DeviceEvent* deviceEvent, GameDevice_DeviceInfo** deviceInfo)
```
 
**描述**
 
从设备状态变化事件中获取设备信息。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| const struct GameDevice_DeviceEvent* deviceEvent | 指针指向GameDevice_DeviceEvent实例，不能为空。 |
| GameDevice_DeviceInfo** deviceInfo | 输出参数，二级指针指向设备信息。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数deviceEvent为null，返回GAME_CONTROLLER_PARAM_ERROR。 |
 
 
  

#### OH_GameDevice_DestroyDeviceInfo()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GameDevice_DestroyDeviceInfo(GameDevice_DeviceInfo** deviceInfo)
```
 
**描述**
 
销毁设备信息实例。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| GameDevice_DeviceInfo** deviceInfo | 二级指针指向GameDevice_DeviceInfo实例，不能为空。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数deviceInfo为null，返回GAME_CONTROLLER_PARAM_ERROR。 |
 
 
  

#### OH_GameDevice_DeviceInfo_GetDeviceId()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GameDevice_DeviceInfo_GetDeviceId(const struct GameDevice_DeviceInfo* deviceInfo, char** deviceId)
```
 
**描述**
 
从设备信息中获取设备ID。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| const struct GameDevice_DeviceInfo* deviceInfo | 指针指向GameDevice_DeviceInfo实例，不能为空。 |
| char** deviceId | 输出参数，二级指针指向设备ID。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数deviceInfo或deviceId为null，返回GAME_CONTROLLER_PARAM_ERROR。 如果设备内存不足，返回GAME_CONTROLLER_NO_MEMORY。 |
 
 
  

#### OH_GameDevice_DeviceInfo_GetName()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GameDevice_DeviceInfo_GetName(const struct GameDevice_DeviceInfo* deviceInfo, char** name)
```
 
**描述**
 
从设备信息中获取设备名称。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| const struct GameDevice_DeviceInfo* deviceInfo | 指针指向GameDevice_DeviceInfo实例，不能为空。 |
| char** name | 输出参数，二级指针指向设备名称。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数deviceInfo或name为null，返回GAME_CONTROLLER_PARAM_ERROR。 如果设备内存不足，返回GAME_CONTROLLER_NO_MEMORY。 |
 
 
  

#### OH_GameDevice_DeviceInfo_GetProduct()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GameDevice_DeviceInfo_GetProduct(const struct GameDevice_DeviceInfo* deviceInfo, int32_t* product)
```
 
**描述**
 
从设备信息中获取产品信息。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| const struct GameDevice_DeviceInfo* deviceInfo | 指针指向GameDevice_DeviceInfo实例，不能为空。 |
| int32_t* product | 输出参数，产品信息。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数deviceInfo为null，返回GAME_CONTROLLER_PARAM_ERROR。 |
 
 
  

#### OH_GameDevice_DeviceInfo_GetVersion()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GameDevice_DeviceInfo_GetVersion(const struct GameDevice_DeviceInfo* deviceInfo, int32_t* version)
```
 
**描述**
 
从设备信息中获取版本信息。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| const struct GameDevice_DeviceInfo* deviceInfo | 指针指向GameDevice_DeviceInfo实例，不能为空。 |
| int32_t* version | 输出参数，版本信息。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数deviceInfo为null，返回GAME_CONTROLLER_PARAM_ERROR。 |
 
 
  

#### OH_GameDevice_DeviceInfo_GetPhysicalAddress()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GameDevice_DeviceInfo_GetPhysicalAddress(const struct GameDevice_DeviceInfo* deviceInfo, char** physicalAddress)
```
 
**描述**
 
从设备信息中获取物理地址。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| const struct GameDevice_DeviceInfo* deviceInfo | 指针指向GameDevice_DeviceInfo实例，不能为空。 |
| char** physicalAddress | 输出参数，二级指针指向物理地址。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数deviceInfo或physicalAddress为null，返回GAME_CONTROLLER_PARAM_ERROR。 如果设备内存不足，返回GAME_CONTROLLER_NO_MEMORY。 |
 
 
  

#### OH_GameDevice_DeviceInfo_GetDeviceType()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GameDevice_DeviceInfo_GetDeviceType(const struct GameDevice_DeviceInfo* deviceInfo, GameDevice_DeviceType* deviceType)
```
 
**描述**
 
从设备信息中获取设备类型。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| const struct GameDevice_DeviceInfo* deviceInfo | 指针指向GameDevice_DeviceInfo实例，不能为空。 |
| GameDevice_DeviceType* deviceType | 输出参数，设备类型。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数deviceInfo为null，返回GAME_CONTROLLER_PARAM_ERROR。 |
