# ArkTS API错误码

更新时间：2026-06-12 06:54:11

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-errorcode

**支持设备：** Phone | PC/2in1 | Tablet

## ArkTS API错误码
 


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/CzKPT02kTr2a3GaGY7KFug/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260701T025451Z&HW-CC-Expire=86400&HW-CC-Sign=5D281662860B8F51A7693A70CF82B7DFF5F52AB439310FE6E925FC4E66A50192)
 
 
以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。
  

  

##### 1023100001 数组长度无效

**错误信息**
 
Array length invalid.
 
**错误描述**
 
数组长度无效。
 
**可能原因**
 
传入的采样点数组长度不足2个。
 
**处理步骤**
 
检查传入的samples数组是否包含至少2个数据点。
