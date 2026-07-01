# ArkTS API错误码

更新时间：2026-06-12 06:54:11

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-natural-language

**支持设备：** Phone | PC/2in1 | Tablet

## ArkTS API错误码
 


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/M_3OmZSnQxuPMqVUFIzUig/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260701T025456Z&HW-CC-Expire=86400&HW-CC-Sign=E15E7254F5EBE413DBB9C8558332289EF1B0FEB644048C85E05608964EB37CBC)
 
 
以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。
  

  

##### 200 运行超时

**错误信息**
 
Run timed out, please try again later.
 
**错误描述**
 
运行超时，请重试。
 
**可能原因**
 
当前存在大量的请求，无法及时处理。
 
**处理步骤**
 
过一段时间重试，并做好相关的逻辑判断。
 
  

##### 1011200001 运行失败

**错误信息**
 
Failed to run, please try again.
 
**错误描述**
 
运行失败，请重试。
 
**可能原因**
 
输入不符合要求，或服务存在异常。
 
**处理步骤**
 
过一段时间重试，并做好相关的逻辑判断。
 
  

##### 1011200002 服务异常

**错误信息**
 
The service is abnormal.
 
**错误描述**
 
服务异常时，系统会产生此错误码。
 
**可能原因**
 
服务异常。
 
**处理步骤**
 
系统异常，建议重启设备重试。
