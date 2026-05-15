# Input_InterceptorEventCallback

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-interceptoreventcallback
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
typedef struct Input_InterceptorEventCallback {...} Input_InterceptorEventCallback
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

拦截回调事件结构体，拦截鼠标事件、触屏输入事件和轴事件。

**起始版本：** 12

**相关模块：** [input](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input)

**所在头文件：** [oh_input_manager.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-input-manager-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| Input_MouseEventCallback mouseCallback | 鼠标事件的回调函数。 起始版本： 12。 |
| Input_TouchEventCallback touchCallback | 触屏输入事件的回调函数。 起始版本： 12。 |
| Input_AxisEventCallback axisCallback | 轴事件的回调函数。 起始版本： 12。 |


### 成员函数
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (*Input_KeyEventCallback)(const Input_KeyEvent* keyEvent)](#input_keyeventcallback) | Input_KeyEventCallback() | 按键事件的回调函数，keyEvent的生命周期为回调函数内。 起始版本： 12。 |
| [typedef void (*Input_MouseEventCallback)(const Input_MouseEvent* mouseEvent)](#input_mouseeventcallback) | Input_MouseEventCallback() | 鼠标事件的回调函数，mouseEvent的生命周期为回调函数内。 起始版本： 12。 |
| [typedef void (*Input_TouchEventCallback)(const Input_TouchEvent* touchEvent)](#input_toucheventcallback) | Input_TouchEventCallback() | 触屏输入事件的回调函数，touchEvent的生命周期为回调函数内。 起始版本： 12。 |
| [typedef void (*Input_AxisEventCallback)(const Input_AxisEvent* axisEvent)](#input_axiseventcallback) | Input_AxisEventCallback() | 轴事件的回调函数，axisEvent的生命周期为回调函数内。 起始版本： 12。 |
| [typedef void (*Input_DeviceAddedCallback)(int32_t deviceId)](#input_deviceaddedcallback) | Input_DeviceAddedCallback() | 回调函数，用于回调输入设备的热插事件。 起始版本： 13。 |
| [typedef void (*Input_DeviceRemovedCallback)(int32_t deviceId)](#input_deviceremovedcallback) | Input_DeviceRemovedCallback() | 回调函数，用于回调输入设备的热拔事件。 起始版本： 13。 |


## 成员函数说明
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### Input_KeyEventCallback()
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
typedef void (*Input_KeyEventCallback)(const Input_KeyEvent* keyEvent)
```

**描述**

按键事件的回调函数，keyEvent的生命周期为回调函数内。

**起始版本：** 12

**参数：**


| 参数项 | 描述 |
| --- | --- |
| const [Input_KeyEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-keyevent)* keyEvent | 按键事件对象。 |


### Input_MouseEventCallback()
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
typedef void (*Input_MouseEventCallback)(const Input_MouseEvent* mouseEvent)
```

**描述**

鼠标事件的回调函数，mouseEvent的生命周期为回调函数内。

**起始版本：** 12

**参数：**


| 参数项 | 描述 |
| --- | --- |
| const [Input_MouseEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-mouseevent)* mouseEvent | 鼠标事件对象。 |


### Input_TouchEventCallback()
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
typedef void (*Input_TouchEventCallback)(const Input_TouchEvent* touchEvent)
```

**描述**

触屏输入事件的回调函数，touchEvent的生命周期为回调函数内。

**起始版本：** 12

**参数：**


| 参数项 | 描述 |
| --- | --- |
| const [Input_TouchEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-touchevent)* touchEvent | 触屏输入事件对象。 |


### Input_AxisEventCallback()
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
typedef void (*Input_AxisEventCallback)(const Input_AxisEvent* axisEvent)
```

**描述**

轴事件的回调函数，axisEvent的生命周期为回调函数内。

**起始版本：** 12

**参数：**


| 参数项 | 描述 |
| --- | --- |
| const [Input_AxisEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-axisevent)* axisEvent | 轴事件对象。 |


### Input_DeviceAddedCallback()
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
typedef void (*Input_DeviceAddedCallback)(int32_t deviceId)
```

**描述**

回调函数，用于回调输入设备的热插事件。

**起始版本：** 13

**参数：**


| 参数项 | 描述 |
| --- | --- |
| int32_t deviceId | 输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。 |


### Input_DeviceRemovedCallback()
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
typedef void (*Input_DeviceRemovedCallback)(int32_t deviceId)
```

**描述**

回调函数，用于回调输入设备的热拔事件。

**起始版本：** 13

**参数：**


| 参数项 | 描述 |
| --- | --- |
| int32_t deviceId | 输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。 |
