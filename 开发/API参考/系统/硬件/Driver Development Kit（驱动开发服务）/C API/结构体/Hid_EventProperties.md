# Hid_EventProperties

更新时间：2026-04-28 03:31:56

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-eventproperties
**支持设备：** PC/2in1


```text
typedef struct Hid_EventProperties {...} Hid_EventProperties
```


## 概述
**支持设备：** PC/2in1

设备关注事件属性。

**起始版本：** 11

**相关模块：** [HidDdk](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk)

**所在头文件：** [hid_ddk_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hid-ddk-types-h)


## 汇总
**支持设备：** PC/2in1


### 成员变量
**支持设备：** PC/2in1


| 名称 | 描述 |
| --- | --- |
| struct [Hid_EventTypeArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-eventtypearray) hidEventTypes | 事件类型属性编码数组 |
| struct [Hid_KeyCodeArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-keycodearray) hidKeys | 键值属性编码数组 |
| struct [Hid_AbsAxesArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-absaxesarray) hidAbs | 绝对坐标属性编码数组 |
| struct [Hid_RelAxesArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-relaxesarray) hidRelBits | 相对坐标属性编码数组 |
| struct [Hid_MscEventArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-msceventarray) hidMiscellaneous | 其它特殊事件属性编码数组 |
| int32_t hidAbsMax[64] | 绝对坐标属性最大值 |
| int32_t hidAbsMin[64] | 绝对坐标属性最小值 |
| int32_t hidAbsFuzz[64] | 绝对坐标属性模糊值 |
| int32_t hidAbsFlat[64] | 绝对坐标属性固定值 |
