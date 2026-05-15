# AIP

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-aip
**支持设备：** Phone / PC/2in1 / Tablet


## 概述
**支持设备：** Phone / PC/2in1 / Tablet

智慧化数据平台（AIP）为应用提供构建端侧智慧化解决方案，提供向量化、知识检索和知识问答的能力。

**起始版本：** 6.0.0(20)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet


### 文件
**支持设备：** Phone / PC/2in1 / Tablet


| 名称 | 描述 |
| --- | --- |
| [aip_error_code.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-aip-error-code) | 描述错误码信息。 |


### 类型定义
**支持设备：** Phone / PC/2in1 / Tablet


| 名称 | 描述 |
| --- | --- |
| typedef enum [OH_Aip_ErrCode](#oh_aip_errcode-1) [OH_Aip_ErrCode](#oh_aip_errcode-1) | 错误码。 |


### 枚举
**支持设备：** Phone / PC/2in1 / Tablet


| 名称 | 描述 |
| --- | --- |
| [OH_Aip_ErrCode](#oh_aip_errcode-1) { AIP_OK = 0, AIP_E_EXEC_ERR = 1021200005, AIP_E_OUT_OF_RANGE = 1021200006, AIP_E_NO_SUCH_FIELD = 1021200007, AIP_E_OVER_LIMIT = 1021200008, AIP_E_CONDITION_OVER_LIMIT = 1021200009, AIP_E_INVALID_ARGS = 1021200010, AIP_E_EMBEDDING_ERR = 1021200012 } | 错误码信息。 |


## 类型定义说明
**支持设备：** Phone / PC/2in1 / Tablet


### OH_Aip_ErrCode
**支持设备：** Phone / PC/2in1 / Tablet


```text
typedef enum OH_Aip_ErrCode OH_Aip_ErrCode;
```

**描述**

错误码信息。

**起始版本：** 6.0.0(20)


## 枚举类型说明
**支持设备：** Phone / PC/2in1 / Tablet


### OH_Aip_ErrCode
**支持设备：** Phone / PC/2in1 / Tablet


```text
enum OH_Aip_ErrCode;
```

**描述**

错误码信息。

**起始版本：** 6.0.0(20)


| 枚举值 | 描述 |
| --- | --- |
| AIP_OK | 操作成功。 |
| AIP_E_EXEC_ERR | 执行报错。 |
| AIP_E_OUT_OF_RANGE | 下标越界。 |
| AIP_E_NO_SUCH_FIELD | 不存在该字段。 |
| AIP_E_OVER_LIMIT | 数组超过最大长度512字节。 |
| AIP_E_CONDITION_OVER_LIMIT | 条件数量超过上限1。 |
| AIP_E_INVALID_ARGS | 无效参数。 |
| AIP_E_EMBEDDING_ERR | 无法生成嵌入向量。 |
