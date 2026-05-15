# HandWrite_HistoricalPoint

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-handwrite-struct-historicalpoint
**支持设备：** Phone / PC/2in1 / Tablet


## 概述
**支持设备：** Phone / PC/2in1 / Tablet

定义历史触摸点信息的结构体。

**系统能力：** SystemCapability.Stylus.HandWrite

**起始版本：** 6.0.0(20)

**相关模块：** [HandWrite](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-handwrite-c)

**所在头文件：** [native_handwrite_api.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-handwrite-headerfile-declare)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet


| 名称 | 描述 |
| --- | --- |
| float [x](#x) | 历史触摸点的X坐标，相对于被触摸元素左边缘，单位：像素。 |
| float [y](#y) | 历史触摸点的Y坐标，相对于被触摸元素上边缘，单位：像素。 |
| int64_t [timeStamp](#timestamp) | 当前历史触摸点的时间戳，单位：ns。 |
| float [force](#force) | 当前历史触摸点的压力值。 |


## 结构体成员变量说明
**支持设备：** Phone / PC/2in1 / Tablet


### x
**支持设备：** Phone / PC/2in1 / Tablet


```text
float HandWrite_HistoricalPoint::x
```

**描述**

历史触摸点的X坐标，相对于被触摸元素左边缘。


### y
**支持设备：** Phone / PC/2in1 / Tablet


```text
float HandWrite_HistoricalPoint::y
```

**描述**

历史触摸点的Y坐标，相对于被触摸元素上边缘。


### timeStamp
**支持设备：** Phone / PC/2in1 / Tablet


```text
int64_t HandWrite_HistoricalPoint::timeStamp
```

**描述**

当前历史触摸点的时间戳，单位为ns。


### force
**支持设备：** Phone / PC/2in1 / Tablet


```text
float HandWrite_HistoricalPoint::force
```

**描述**

当前历史触摸点的压力值。
