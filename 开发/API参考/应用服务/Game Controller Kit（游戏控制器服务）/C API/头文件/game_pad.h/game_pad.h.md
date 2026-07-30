# game_pad.h

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-game-pad-h
**支持设备：** Phone | PC/2in1 | Tablet | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | TV

定义游戏手柄的接口。
 
**引用文件：** <GameControllerKit/game_pad.h>
 
**库：** libohgame_controller.z.so
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**相关模块：** [GameController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-gamecontroller)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | TV

  

#### 函数

**支持设备：** Phone | PC/2in1 | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| GameController_ErrorCode OH_GamePad_LeftShoulder_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback) | 注册LeftShoulder按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_LeftShoulder_UnregisterButtonInputMonitor(void) | 取消注册LeftShoulder按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_RightShoulder_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback) | 注册RightShoulder按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_RightShoulder_UnregisterButtonInputMonitor(void) | 取消注册RightShoulder按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_LeftTrigger_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback) | 注册LeftTrigger按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_LeftTrigger_UnregisterButtonInputMonitor(void) | 取消注册LeftTrigger按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_LeftTrigger_RegisterAxisInputMonitor(GamePad_AxisInputMonitorCallback inputMonitorCallback) | 注册LeftTrigger轴事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_LeftTrigger_UnregisterAxisInputMonitor(void) | 取消注册LeftTrigger轴事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_RightTrigger_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback) | 注册RightTrigger按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_RightTrigger_UnregisterButtonInputMonitor(void) | 取消注册RightTrigger按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_RightTrigger_RegisterAxisInputMonitor(GamePad_AxisInputMonitorCallback inputMonitorCallback) | 注册RightTrigger轴事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_RightTrigger_UnregisterAxisInputMonitor(void) | 取消注册RightTrigger轴事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_ButtonMenu_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback) | 注册Menu按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_ButtonMenu_UnregisterButtonInputMonitor(void) | 取消注册Menu按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_ButtonHome_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback) | 注册Home按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_ButtonHome_UnregisterButtonInputMonitor(void) | 取消注册Home按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_ButtonA_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback) | 注册A按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_ButtonA_UnregisterButtonInputMonitor(void) | 取消注册A按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_ButtonB_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback) | 注册B按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_ButtonB_UnregisterButtonInputMonitor(void) | 取消注册B按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_ButtonX_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback) | 注册X按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_ButtonX_UnregisterButtonInputMonitor(void) | 取消注册X按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_ButtonY_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback) | 注册Y按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_ButtonY_UnregisterButtonInputMonitor(void) | 取消注册Y按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_ButtonC_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback) | 注册C按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_ButtonC_UnregisterButtonInputMonitor(void) | 取消注册C按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_Dpad_LeftButton_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback) | 注册方向按键的向左按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_Dpad_LeftButton_UnregisterButtonInputMonitor(void) | 取消注册方向按键的向左按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_Dpad_RightButton_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback) | 注册方向按键的向右按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_Dpad_RightButton_UnregisterButtonInputMonitor(void) | 取消注册方向按键的向右按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_Dpad_UpButton_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback) | 注册方向按键的向上按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_Dpad_UpButton_UnregisterButtonInputMonitor(void) | 取消注册方向按键的向上按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_Dpad_DownButton_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback) | 注册方向按键的向下按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_Dpad_DownButton_UnregisterButtonInputMonitor(void) | 取消注册方向按键的向下按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_Dpad_RegisterAxisInputMonitor(GamePad_AxisInputMonitorCallback inputMonitorCallback) | 注册方向按键轴事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_Dpad_UnregisterAxisInputMonitor(void) | 取消注册方向按键轴事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_LeftThumbstick_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback) | 注册LeftThumbstick按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_LeftThumbstick_UnregisterButtonInputMonitor(void) | 取消注册LeftThumbstick按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_LeftThumbstick_RegisterAxisInputMonitor(GamePad_AxisInputMonitorCallback inputMonitorCallback) | 注册LeftThumbstick轴事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_LeftThumbstick_UnregisterAxisInputMonitor(void) | 取消注册LeftThumbstick轴事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_RightThumbstick_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback) | 注册RightThumbstick按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_RightThumbstick_UnregisterButtonInputMonitor(void) | 取消注册RightThumbstick按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_RightThumbstick_RegisterAxisInputMonitor(GamePad_AxisInputMonitorCallback inputMonitorCallback) | 注册RightThumbstick轴事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_RightThumbstick_UnregisterAxisInputMonitor(void) | 取消注册RightThumbstick轴事件的监听回调。 |
 
 
  

#### 函数说明

**支持设备：** Phone | PC/2in1 | Tablet | TV

  

#### OH_GamePad_LeftShoulder_RegisterButtonInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_LeftShoulder_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```
 
**描述**
 
注册LeftShoulder按键事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| GamePad_ButtonInputMonitorCallback inputMonitorCallback | 回调函数GamePad_ButtonInputMonitorCallback，不能为空。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数inputMonitorCallback为null，返回GAME_CONTROLLER_PARAM_ERROR。 |
 
 
  

#### OH_GamePad_LeftShoulder_UnregisterButtonInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_LeftShoulder_UnregisterButtonInputMonitor(void)
```
 
**描述**
 
取消注册LeftShoulder按键事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 |
 
 
  

#### OH_GamePad_RightShoulder_RegisterButtonInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_RightShoulder_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```
 
**描述**
 
注册RightShoulder按键事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| GamePad_ButtonInputMonitorCallback inputMonitorCallback | 回调函数GamePad_ButtonInputMonitorCallback，不能为空。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数inputMonitorCallback为null，返回GAME_CONTROLLER_PARAM_ERROR。 |
 
 
  

#### OH_GamePad_RightShoulder_UnregisterButtonInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_RightShoulder_UnregisterButtonInputMonitor(void)
```
 
**描述**
 
取消注册RightShoulder按键事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 |
 
 
  

#### OH_GamePad_LeftTrigger_RegisterButtonInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_LeftTrigger_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```
 
**描述**
 
注册LeftTrigger按键事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| GamePad_ButtonInputMonitorCallback inputMonitorCallback | 回调函数GamePad_ButtonInputMonitorCallback，不能为空。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数inputMonitorCallback为null，返回GAME_CONTROLLER_PARAM_ERROR。 |
 
 
  

#### OH_GamePad_LeftTrigger_UnregisterButtonInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_LeftTrigger_UnregisterButtonInputMonitor(void)
```
 
**描述**
 
取消注册LeftTrigger按键事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 |
 
 
  

#### OH_GamePad_LeftTrigger_RegisterAxisInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_LeftTrigger_RegisterAxisInputMonitor(GamePad_AxisInputMonitorCallback inputMonitorCallback)
```
 
**描述**
 
注册LeftTrigger轴事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| GamePad_AxisInputMonitorCallback inputMonitorCallback | 回调函数GamePad_AxisInputMonitorCallback，不能为空。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数inputMonitorCallback为null，返回GAME_CONTROLLER_PARAM_ERROR。 |
 
 
  

#### OH_GamePad_LeftTrigger_UnregisterAxisInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_LeftTrigger_UnregisterAxisInputMonitor(void)
```
 
**描述**
 
取消注册LeftTrigger轴事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 |
 
 
  

#### OH_GamePad_RightTrigger_RegisterButtonInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_RightTrigger_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```
 
**描述**
 
注册RightTrigger按键事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| GamePad_ButtonInputMonitorCallback inputMonitorCallback | 回调函数GamePad_ButtonInputMonitorCallback，不能为空。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数inputMonitorCallback为null，返回GAME_CONTROLLER_PARAM_ERROR。 |
 
 
  

#### OH_GamePad_RightTrigger_UnregisterButtonInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_RightTrigger_UnregisterButtonInputMonitor(void)
```
 
**描述**
 
取消注册RightTrigger按键事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 |
 
 
  

#### OH_GamePad_RightTrigger_RegisterAxisInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_RightTrigger_RegisterAxisInputMonitor(GamePad_AxisInputMonitorCallback inputMonitorCallback)
```
 
**描述**
 
注册RightTrigger轴事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| GamePad_AxisInputMonitorCallback inputMonitorCallback | 回调函数GamePad_AxisInputMonitorCallback，不能为空。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数inputMonitorCallback为null，返回GAME_CONTROLLER_PARAM_ERROR。 |
 
 
  

#### OH_GamePad_RightTrigger_UnregisterAxisInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_RightTrigger_UnregisterAxisInputMonitor(void)
```
 
**描述**
 
取消注册RightTrigger轴事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 |
 
 
  

#### OH_GamePad_ButtonMenu_RegisterButtonInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_ButtonMenu_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```
 
**描述**
 
注册Menu按键事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| GamePad_ButtonInputMonitorCallback inputMonitorCallback | 回调函数GamePad_ButtonInputMonitorCallback，不能为空。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数inputMonitorCallback为null，返回GAME_CONTROLLER_PARAM_ERROR。 |
 
 
  

#### OH_GamePad_ButtonMenu_UnregisterButtonInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_ButtonMenu_UnregisterButtonInputMonitor(void)
```
 
**描述**
 
取消注册Menu按键事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 |
 
 
  

#### OH_GamePad_ButtonHome_RegisterButtonInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_ButtonHome_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```
 
**描述**
 
注册Home按键事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| GamePad_ButtonInputMonitorCallback inputMonitorCallback | 回调函数GamePad_ButtonInputMonitorCallback，不能为空。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数inputMonitorCallback为null，返回GAME_CONTROLLER_PARAM_ERROR。 |
 
 
  

#### OH_GamePad_ButtonHome_UnregisterButtonInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_ButtonHome_UnregisterButtonInputMonitor(void)
```
 
**描述**
 
取消注册Home按键事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 |
 
 
  

#### OH_GamePad_ButtonA_RegisterButtonInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_ButtonA_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```
 
**描述**
 
注册A按键事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| GamePad_ButtonInputMonitorCallback inputMonitorCallback | 回调函数GamePad_ButtonInputMonitorCallback，不能为空。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数inputMonitorCallback为null，返回GAME_CONTROLLER_PARAM_ERROR。 |
 
 
  

#### OH_GamePad_ButtonA_UnregisterButtonInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_ButtonA_UnregisterButtonInputMonitor(void)
```
 
**描述**
 
取消注册A按键事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 |
 
 
  

#### OH_GamePad_ButtonB_RegisterButtonInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_ButtonB_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```
 
**描述**
 
注册B按键事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| GamePad_ButtonInputMonitorCallback inputMonitorCallback | 回调函数GamePad_ButtonInputMonitorCallback，不能为空。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数inputMonitorCallback为null，返回GAME_CONTROLLER_PARAM_ERROR。 |
 
 
  

#### OH_GamePad_ButtonB_UnregisterButtonInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_ButtonB_UnregisterButtonInputMonitor(void)
```
 
**描述**
 
取消注册B按键事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 |
 
 
  

#### OH_GamePad_ButtonX_RegisterButtonInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_ButtonX_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```
 
**描述**
 
注册X按键事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| GamePad_ButtonInputMonitorCallback inputMonitorCallback | 回调函数GamePad_ButtonInputMonitorCallback，不能为空。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数inputMonitorCallback为null，返回GAME_CONTROLLER_PARAM_ERROR。 |
 
 
  

#### OH_GamePad_ButtonX_UnregisterButtonInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_ButtonX_UnregisterButtonInputMonitor(void)
```
 
**描述**
 
取消注册X按键事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 |
 
 
  

#### OH_GamePad_ButtonY_RegisterButtonInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_ButtonY_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```
 
**描述**
 
注册Y按键事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| GamePad_ButtonInputMonitorCallback inputMonitorCallback | 回调函数GamePad_ButtonInputMonitorCallback，不能为空。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数inputMonitorCallback为null，返回GAME_CONTROLLER_PARAM_ERROR。 |
 
 
  

#### OH_GamePad_ButtonY_UnregisterButtonInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_ButtonY_UnregisterButtonInputMonitor(void)
```
 
**描述**
 
取消注册Y按键事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 |
 
 
  

#### OH_GamePad_ButtonC_RegisterButtonInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_ButtonC_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```
 
**描述**
 
注册C按键事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| GamePad_ButtonInputMonitorCallback inputMonitorCallback | 回调函数GamePad_ButtonInputMonitorCallback，不能为空。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数inputMonitorCallback为null，返回GAME_CONTROLLER_PARAM_ERROR。 |
 
 
  

#### OH_GamePad_ButtonC_UnregisterButtonInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_ButtonC_UnregisterButtonInputMonitor(void)
```
 
**描述**
 
取消注册C按键事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 |
 
 
  

#### OH_GamePad_Dpad_LeftButton_RegisterButtonInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_Dpad_LeftButton_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```
 
**描述**
 
注册方向按键的向左按键事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| GamePad_ButtonInputMonitorCallback inputMonitorCallback | 回调函数GamePad_ButtonInputMonitorCallback，不能为空。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数inputMonitorCallback为null，返回GAME_CONTROLLER_PARAM_ERROR。 |
 
 
  

#### OH_GamePad_Dpad_LeftButton_UnregisterButtonInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_Dpad_LeftButton_UnregisterButtonInputMonitor(void)
```
 
**描述**
 
取消注册方向按键的向左按键事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 |
 
 
  

#### OH_GamePad_Dpad_RightButton_RegisterButtonInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_Dpad_RightButton_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```
 
**描述**
 
注册方向按键的向右按键事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| GamePad_ButtonInputMonitorCallback inputMonitorCallback | 回调函数GamePad_ButtonInputMonitorCallback，不能为空。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数inputMonitorCallback为null，返回GAME_CONTROLLER_PARAM_ERROR。 |
 
 
  

#### OH_GamePad_Dpad_RightButton_UnregisterButtonInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_Dpad_RightButton_UnregisterButtonInputMonitor(void)
```
 
**描述**
 
取消注册方向按键的向右按键事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 |
 
 
  

#### OH_GamePad_Dpad_UpButton_RegisterButtonInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_Dpad_UpButton_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```
 
**描述**
 
注册方向按键的向上按键事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| GamePad_ButtonInputMonitorCallback inputMonitorCallback | 回调函数GamePad_ButtonInputMonitorCallback，不能为空。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数inputMonitorCallback为null，返回GAME_CONTROLLER_PARAM_ERROR。 |
 
 
  

#### OH_GamePad_Dpad_UpButton_UnregisterButtonInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_Dpad_UpButton_UnregisterButtonInputMonitor(void)
```
 
**描述**
 
取消注册方向按键的向上按键事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 |
 
 
  

#### OH_GamePad_Dpad_DownButton_RegisterButtonInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_Dpad_DownButton_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```
 
**描述**
 
注册方向按键的向下按键事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| GamePad_ButtonInputMonitorCallback inputMonitorCallback | 回调函数GamePad_ButtonInputMonitorCallback，不能为空。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数inputMonitorCallback为null，返回GAME_CONTROLLER_PARAM_ERROR。 |
 
 
  

#### OH_GamePad_Dpad_DownButton_UnregisterButtonInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_Dpad_DownButton_UnregisterButtonInputMonitor(void)
```
 
**描述**
 
取消注册方向按键的向下按键事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 |
 
 
  

#### OH_GamePad_Dpad_RegisterAxisInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_Dpad_RegisterAxisInputMonitor(GamePad_AxisInputMonitorCallback inputMonitorCallback)
```
 
**描述**
 
注册方向按键轴事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| GamePad_AxisInputMonitorCallback inputMonitorCallback | 回调函数GamePad_AxisInputMonitorCallback，不能为空。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数inputMonitorCallback为null，返回GAME_CONTROLLER_PARAM_ERROR。 |
 
 
  

#### OH_GamePad_Dpad_UnregisterAxisInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_Dpad_UnregisterAxisInputMonitor(void)
```
 
**描述**
 
取消注册方向按键轴事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 |
 
 
  

#### OH_GamePad_LeftThumbstick_RegisterButtonInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_LeftThumbstick_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```
 
**描述**
 
注册LeftThumbstick按键事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| GamePad_ButtonInputMonitorCallback inputMonitorCallback | 回调函数GamePad_ButtonInputMonitorCallback，不能为空。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数inputMonitorCallback为null，返回GAME_CONTROLLER_PARAM_ERROR。 |
 
 
  

#### OH_GamePad_LeftThumbstick_UnregisterButtonInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_LeftThumbstick_UnregisterButtonInputMonitor(void)
```
 
**描述**
 
取消注册LeftThumbstick按键事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 |
 
 
  

#### OH_GamePad_LeftThumbstick_RegisterAxisInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_LeftThumbstick_RegisterAxisInputMonitor(GamePad_AxisInputMonitorCallback inputMonitorCallback)
```
 
**描述**
 
注册LeftThumbstick轴事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| GamePad_AxisInputMonitorCallback inputMonitorCallback | 回调函数GamePad_AxisInputMonitorCallback，不能为空。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数inputMonitorCallback为null，返回GAME_CONTROLLER_PARAM_ERROR。 |
 
 
  

#### OH_GamePad_LeftThumbstick_UnregisterAxisInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_LeftThumbstick_UnregisterAxisInputMonitor(void)
```
 
**描述**
 
取消注册LeftThumbstick轴事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 |
 
 
  

#### OH_GamePad_RightThumbstick_RegisterButtonInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_RightThumbstick_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```
 
**描述**
 
注册RightThumbstick按键事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| GamePad_ButtonInputMonitorCallback inputMonitorCallback | 回调函数GamePad_ButtonInputMonitorCallback，不能为空。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数inputMonitorCallback为null，返回GAME_CONTROLLER_PARAM_ERROR。 |
 
 
  

#### OH_GamePad_RightThumbstick_UnregisterButtonInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_RightThumbstick_UnregisterButtonInputMonitor(void)
```
 
**描述**
 
取消注册RightThumbstick按键事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 |
 
 
  

#### OH_GamePad_RightThumbstick_RegisterAxisInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_RightThumbstick_RegisterAxisInputMonitor(GamePad_AxisInputMonitorCallback inputMonitorCallback)
```
 
**描述**
 
注册RightThumbstick轴事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| GamePad_AxisInputMonitorCallback inputMonitorCallback | 回调函数GamePad_AxisInputMonitorCallback，不能为空。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 如果参数inputMonitorCallback为null，返回GAME_CONTROLLER_PARAM_ERROR。 |
 
 
  

#### OH_GamePad_RightThumbstick_UnregisterAxisInputMonitor()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
GameController_ErrorCode OH_GamePad_RightThumbstick_UnregisterAxisInputMonitor(void)
```
 
**描述**
 
取消注册RightThumbstick轴事件的监听回调。
 
**系统能力：** SystemCapability.Game.GameController
 
**起始版本：** 21
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GameController_ErrorCode | 如果执行成功，返回GAME_CONTROLLER_SUCCESS。 |
