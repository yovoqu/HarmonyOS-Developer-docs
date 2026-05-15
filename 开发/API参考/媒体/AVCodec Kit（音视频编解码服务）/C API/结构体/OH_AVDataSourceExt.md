# OH_AVDataSourceExt

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-codecbase-oh-avdatasourceext
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
typedef struct OH_AVDataSourceExt {...} OH_AVDataSourceExt
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

用户自定义数据源，回调支持通过userData传递用户自定义数据。

**起始版本：** 20

**相关模块：** [CodecBase](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-codecbase)

**所在头文件：** [native_avcodec_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avcodec-base-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| int64_t size | 数据源的总大小。 |
| [OH_AVDataSourceReadAtExt](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avcodec-base-h#oh_avdatasourcereadatext) readAt | 数据源的数据回调。 |
