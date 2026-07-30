# DrawableDescriptor错误码

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-drawable-descriptor
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

> [!NOTE]
> 以下仅介绍本模块特有错误码，通用错误码请参考 通用错误码 。



#### 111001 资源加载失败

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**错误信息**

resource loading failed.

**错误描述**

该错误码在资源加载失败时被触发。

**可能原因**

路径不存在，资源不存在或者文件已损坏。

**处理步骤**

检查资源是否存在或文件是否损坏。



#### 111002 资源已释放

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**错误信息**

The native memory referenced by the drawableDescriptor has been released.

**错误描述**

该错误码在DrawableDescriptor引用的native内存已被释放时被触发。当调用[release](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#release)方法释放资源后，再调用[getPixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#getpixelmap)、[getForeground](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#getforeground)、[getBackground](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#getbackground)、[getMask](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#getmask)、[loadSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#loadsync21)、[load](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#load21)等接口时会触发此错误。

**可能原因**

在调用[release](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#release)释放DrawableDescriptor资源后，继续调用该对象的其他接口。

**处理步骤**
1. 在调用getPixelMap等接口前，通过[isReleased](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#isreleased)检查对象是否已释放。
2. 避免在[release](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor#release)后继续使用该DrawableDescriptor对象。
