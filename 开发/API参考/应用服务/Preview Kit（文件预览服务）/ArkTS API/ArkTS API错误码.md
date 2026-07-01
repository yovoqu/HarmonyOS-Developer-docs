# ArkTS API错误码

更新时间：2026-06-12 06:54:11

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-preview

**支持设备：** PC/2in1

## ArkTS API错误码
 


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/zyrvtPpdSG6LNuH2DsQZ-A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260701T025455Z&HW-CC-Expire=86400&HW-CC-Sign=E8655FEE57382E8FEFB2D777240CEC5C79563FF76E6C3193BFABAA7D97A9EF0F)
 
 
以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。
  

  

##### 1017220001 内部失败

**错误信息**
 
Internal failure.
 
**错误描述**
 
调用接口时，返回未知内部错误。
 
**可能原因**
 
系统处理异常返回的未定义的错误。
 
**处理步骤**
 
出现的情况不明确，建议尝试重新创建业务，或者过一段时间重试，并做好相关的逻辑判断。如果仍无法解决请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。
 
  

##### 1017220002 服务不可用

**错误信息**
 
Service unavailable.
 
**错误描述**
 
IPC服务处理异常。
 
**可能原因**
 
系统处理异常，比如系统服务重启、跨进程调用异常等。
 
**处理步骤**
 
出现的情况不明确，建议尝试重新创建业务，或者过一段时间重试，并做好相关的逻辑判断。如果仍无法解决请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。
 
  

##### 1017220003 添加的文件个数超过上限

**错误信息**
 
The number of files exceeds the upper limit.
 
**错误描述**
 
添加的文件个数超过上限。
 
**可能原因**
 
- 没有先调用[on('filePreloadStateChanged')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/preview-arkts-openfileboost-api#openfileboostonfilepreloadstatechangeddeprecated)接口注册，直接调用[openFileBoost.addFile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/preview-arkts-openfileboost-api#openfileboostaddfiledeprecated)接口添加文件。
- 调用[openFileBoost.addFile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/preview-arkts-openfileboost-api#openfileboostaddfiledeprecated)接口添加文件个数太多（当前一个进程最多添加50个文件）。

 
**处理步骤**
 
- 确认在已经调用了[on('filePreloadStateChanged')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/preview-arkts-openfileboost-api#openfileboostonfilepreloadstatechangeddeprecated)的情况下，再调用[openFileBoost.addFile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/preview-arkts-openfileboost-api#openfileboostaddfiledeprecated)接口。
- 不需要再监听预加载状态的文件时，调用[openFileBoost.removeFile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/preview-arkts-openfileboost-api#openfileboostremovefiledeprecated)接口，删除对应文件的监听再重试。
