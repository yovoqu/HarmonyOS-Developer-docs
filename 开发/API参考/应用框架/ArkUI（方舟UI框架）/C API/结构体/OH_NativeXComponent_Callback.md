# OH_NativeXComponent_Callback

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ent-native-xcomponent-oh-nativexcomponent-callback
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_NativeXComponent_Callback {...} OH_NativeXComponent_Callback
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

注册Surface生命周期和触摸事件回调。
 
**起始版本：** 8
 
**相关模块：** [OH_NativeXComponent Native XComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent)
 
**所在头文件：** [native_interface_xcomponent.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-xcomponent-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| void (*OnSurfaceCreated)(OH_NativeXComponent* component, void* window) | 创建Surface时调用。 |
| void (*OnSurfaceChanged)(OH_NativeXComponent* component, void* window) | 当Surface改变时调用。 |
| void (*OnSurfaceDestroyed)(OH_NativeXComponent* component, void* window) | 当Surface被销毁时调用。 |
| void (*DispatchTouchEvent)(OH_NativeXComponent* component, void* window) | 当触摸事件被触发时调用。 |
 
 
  

#### 成员函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### OnSurfaceCreated()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void (*OnSurfaceCreated)(OH_NativeXComponent* component, void* window)
```
 
**描述：**
 
创建Surface时调用。
 
**起始版本：** 8
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| void* window | 表示NativeWindow句柄。 通过XComponent生命周期获取的NativeWindow本身由系统侧持有了一次引用计数，并会在OnSurfaceDestroyed回调触发之后将引用计数减一，引用计数归零后NativeWindow将被释放。 |
 
 
  

#### OnSurfaceChanged()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void (*OnSurfaceChanged)(OH_NativeXComponent* component, void* window)
```
 
**描述：**
 
当Surface改变时调用。
 
**起始版本：** 8
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| void* window | 表示NativeWindow句柄。 |
 
 
  

#### OnSurfaceDestroyed()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void (*OnSurfaceDestroyed)(OH_NativeXComponent* component, void* window)
```
 
**描述：**
 
当Surface被销毁时调用。
 
**起始版本：** 8
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| void* window | 表示NativeWindow句柄。 |
 
 
  

#### DispatchTouchEvent()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void (*DispatchTouchEvent)(OH_NativeXComponent* component, void* window)
```
 
**描述：**
 
当触摸事件被触发时调用。
 
**起始版本：** 8
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| void* window | 表示NativeWindow句柄。 |
