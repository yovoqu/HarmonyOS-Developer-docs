# ArkTS API错误码

更新时间：2026-06-13 03:51:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-car

**支持设备：** Phone | Tablet

## ArkTS API错误码
 


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/AE4k4eqvSlepg3TYaRER-g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260701T025451Z&HW-CC-Expire=86400&HW-CC-Sign=3DDD68143395C3C2D08136AAA66573468662FE2575247863B5BA3907599DFD66)
 
 
以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。
  

  

##### 1003810001 参数值无效

**错误信息**
 
Invalid parameter value.
 
**错误描述**
 
无效的参数值。
 
**可能原因**
 
- 设置导航状态时目的地名称长度或途经点名称长度超出1024字节。
- 设置导航元数据时当前道路名或下一次进入的道路名的长度超出1024字节。
- 参数值超出范围，比如设置导航状态时经纬度值不在有效范围（纬度值的数值范围是[-90, 90]，经度值的有效范围是[-180, 180]）内。

 
**处理步骤**
 
在设置导航状态、导航元数据时请确保参数传递正确。
 
  

##### 1003810002 所有参数总大小超出限制

**错误信息**
 
The total size of all parameters exceeds the limit.
 
**错误描述**
 
所有参数总大小超出了限制。
 
**可能原因**
 
- 设置导航状态时添加的途经点太多。
- 设置导航元数据时当传入路口放大图时参数总大小可能会超出限制（200Kbytes）。

 
**处理步骤**
 
- 设置导航状态时检查添加途经点的数量，确保途经点的数量不超出20个。
- 设置导航元数据时如果要传入路口放大图，并且图片较大时，建议对图片做压缩处理。
