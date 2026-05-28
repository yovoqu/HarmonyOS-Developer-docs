# HandWrite

更新时间：2026-04-30 09:02:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-handwrite-c
**支持设备：** Phone | PC/2in1 | Tablet

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet

该模块对外提供手写能力。
 
**系统能力：** SystemCapability.Stylus.Handwrite
 
**起始版本：** 6.0.0(20)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet

  

##### 文件

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| native_handwrite_api.h | 声明用于对外提供手写能力。 |
 
 
  

##### 结构体

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| struct HandWrite_HistoricalPoint | 定义历史触摸点信息的结构体。 |
 
 
  

##### 枚举

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| enum Handwrite_ErrCode { E_NO_ERROR = 0, E_PARAMS = 401, E_INNER_ERROR = 1010400001 } | 定义手写错误码。 |
 
 
  

##### 函数

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 函数 |
| --- | --- |
| int32_t HMS_HandWrite_GetPredictPoint(const HandWrite_HistoricalPoint* event, int32_t size, float *predictPointX, float *predictPointY) | 此接口用于获取预测点。 |
 
 
  

##### 枚举类型说明

**支持设备：** Phone | PC/2in1 | Tablet

  

##### Handwrite_ErrCode

**支持设备：** Phone | PC/2in1 | Tablet

```text
enum Handwrite_ErrCode
```
 
**描述**
 
定义手写错误码。
 
**起始版本：** 6.0.0(20)
  
| 枚举值 | 描述 |
| --- | --- |
| E_NO_ERROR | 执行成功。 |
| E_PARAMS | 输入参数无效。 |
| E_INNER_ERROR | 系统内部错误，相关资源加载失败。 |
 
 
  

##### 函数说明

**支持设备：** Phone | PC/2in1 | Tablet

  

##### HMS_HandWrite_GetPredictPoint()

**支持设备：** Phone | PC/2in1 | Tablet

```text
int32_t HMS_HandWrite_GetPredictPoint(const HandWrite_HistoricalPoint* event,
    int32_t size, float *predictPointX, float *predictPointY)
```
 
**描述**
 
此接口用于获取预测点。
 
**起始版本：** 6.0.0(20)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| event | 指示输入的历史点。 |
| size | 历史点的个数。 |
| predictPointX | 接收预测点X坐标的指针。 |
| predictPointY | 接收预测点Y坐标的指针。 |
 
 
**返回：** 手写错误码HandWrite_ErrCode：
 
E_NO_ERROR 0 - 执行成功。
 
E_PARAMS 401 - 输入参数无效。
 
E_INNER_ERROR 1010400001 - 系统内部错误，相关资源加载失败。
