# OH_NativeBuffer

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

提供NativeBuffer功能，通过提供的接口，可以实现共享内存的申请、使用、属性查询、释放等操作。
 
**起始版本：** 9
 
  

##### 文件汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| buffer_common.h | 提供NativeBuffer模块的公共类型定义。 从API version 12开始，部分类型定义从native_buffer.h移动至此头文件统一呈现，对于此类类型，API version 12之前即支持使用，各版本均可正常使用。 引用文件：<native_buffer/buffer_common.h> |
| native_buffer.h | 定义获取和使用NativeBuffer的相关函数。 引用文件：<native_buffer/native_buffer.h> |
