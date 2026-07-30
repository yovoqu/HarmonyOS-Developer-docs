# game_device.h

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-game-device-h
**支持设备：** Phone | PC/2in1 | Tablet | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | TV

定义游戏设备的接口。
 
**引用文件：** <GameControllerKit/game_device.h>
 
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
| GameDevice_AllDeviceInfos | GameDevice_AllDeviceInfos | 定义OH_GameDevice_GetAllDeviceInfos接口的调用结果。 |
 
 
  

#### 函数

**支持设备：** Phone | PC/2in1 | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| GameController_ErrorCode OH_GameDevice_GetAllDeviceInfos(GameDevice_AllDeviceInfos** allDeviceInfos) | 获取所有在线设备的信息。 |
| GameController_ErrorCode OH_GameDevice_RegisterDeviceMonitor(GameDevice_DeviceMonitorCallback deviceMonitorCallback) | 注册设备状态变化事件的监听回调。 |
| GameController_ErrorCode OH_GameDevice_UnregisterDeviceMonitor(void) | 取消注册设备状态变化事件的监听回调。 |
| GameController_ErrorCode OH_GameDevice_DestroyAllDeviceInfos(GameDevice_AllDeviceInfos** allDeviceInfos) | 销毁所有设备信息实例。 |
| GameController_ErrorCode OH_GameDevice_AllDeviceInfos_GetCount(const struct GameDevice_AllDeviceInfos* allDeviceInfos, int32_t* count) | 获取设备数量。 |
| GameController_ErrorCode OH_GameDevice_AllDeviceInfos_GetDeviceInfo(const struct GameDevice_AllDeviceInfos* allDeviceInfos, const int32_t index, GameDevice_DeviceInfo** deviceInfo) | 获取指定索引的设备信息。 |
 
 
  

#### 函数说明

**支持设备：** Phone | PC/2in1 | Tablet | TV

  

#### OH_GameDevice_GetAllDeviceInfos()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GameDevice_GetAllDeviceInfos(GameDevice_AllDeviceInfos** allDeviceInfos)
```
 
**描述**
 
获取所有在线设备的信息。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| GameDevice_AllDeviceInfos** allDeviceInfos | 输出参数。二级指针指向GameDevice_AllDeviceInfos实例，不能为空。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数allDeviceInfos为null，返回GAME_CONTROLLER_PARAM_ERROR。 如果查询多模输入中所有设备信息失败，返回GAME_CONTROLLER_MULTIMODAL_INPUT_ERROR。 |
 
 
  

#### OH_GameDevice_RegisterDeviceMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GameDevice_RegisterDeviceMonitor(GameDevice_DeviceMonitorCallback deviceMonitorCallback)
```
 
**描述**
 
注册设备状态变化事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| GameDevice_DeviceMonitorCallback deviceMonitorCallback | 回调函数GameDevice_DeviceMonitorCallback，不能为空。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数deviceMonitorCallback为null，返回GAME_CONTROLLER_PARAM_ERROR。 |
 
 
  

#### OH_GameDevice_UnregisterDeviceMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GameDevice_UnregisterDeviceMonitor(void)
```
 
**描述**
 
取消注册设备状态变化事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 |
 
 
  

#### OH_GameDevice_DestroyAllDeviceInfos()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GameDevice_DestroyAllDeviceInfos(GameDevice_AllDeviceInfos** allDeviceInfos)
```
 
**描述**
 
销毁所有设备信息实例。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| GameDevice_AllDeviceInfos** allDeviceInfos | 二级指针指向GameDevice_AllDeviceInfos实例，不能为空。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数allDeviceInfos为null，返回GAME_CONTROLLER_PARAM_ERROR。 |
 
 
  

#### OH_GameDevice_AllDeviceInfos_GetCount()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GameDevice_AllDeviceInfos_GetCount(const struct GameDevice_AllDeviceInfos* allDeviceInfos, int32_t* count)
```
 
**描述**
 
获取设备数量。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| const struct GameDevice_AllDeviceInfos* allDeviceInfos | 指针指向GameDevice_AllDeviceInfos实例，不能为空。 |
| int32_t* count | 输出参数，设备数量。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数allDeviceInfos为null，返回GAME_CONTROLLER_PARAM_ERROR。 |
 
 
  

#### OH_GameDevice_AllDeviceInfos_GetDeviceInfo()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GameDevice_AllDeviceInfos_GetDeviceInfo(const struct GameDevice_AllDeviceInfos* allDeviceInfos, const int32_t index, GameDevice_DeviceInfo** deviceInfo)
```
 
**描述**
 
获取指定索引的设备信息。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| const struct GameDevice_AllDeviceInfos* allDeviceInfos | 指针指向GameDevice_AllDeviceInfos实例，不能为空。 |
| const int32_t index | 指定设备索引。 |
| GameDevice_DeviceInfo** deviceInfo | 输出参数，二级指针指向设备信息。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数allDeviceInfos为null，或index小于0或大于等于设备总数，返回GAME_CONTROLLER_PARAM_ERROR。 |
