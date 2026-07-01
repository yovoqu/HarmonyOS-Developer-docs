# ArkTS API错误码

更新时间：2026-06-13 03:51:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-ui-design

**支持设备：** Phone | PC/2in1 | Tablet | TV

## ArkTS API错误码
 


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/zqmFchdNTD6t0kQJkTpnGQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260701T025447Z&HW-CC-Expire=86400&HW-CC-Sign=886CE78D1303302954B817567910274F804A9203B66D176FEE509603A15C0529)
 
 
以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。
  

  

##### 1012600001 并发任务忙碌

**错误信息**
 
Task is busy.
 
**错误描述**
 
并发任务忙碌。
 
**可能原因**
 
上一个并发任务还没结束。
 
**处理步骤**
 
- 检查 [hdsDrawable.getHdsLayeredIcons](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsdrawable#hdsdrawablegethdslayeredicons)， [hdsDrawable.getHdsIcons](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsdrawable#hdsdrawablegethdsicons)的调用是否在对应返回结果后再执行，或者使用单次处理的API接口进行处理。
- 通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

 
  

##### 1012600002 资源大小超过规格限制

**错误信息**
 
Resource size error. The ttf resource out of size.
 
Resource size error. The json resource out of size.
 
**错误描述**
 
资源大小超过规格限制。
 
**可能原因**
 
用户传入的资源大小超过规格限制的大小，限制用户最多自定义10个图标。
 
**处理步骤**
 
裁剪接口传入的自定义Symbol图标个数以及配套动效参数个数。
 
  

##### 1012600003 资源解析失败

**错误信息**
 
Resource error. Parse the ttf resource failed.
 
Resource error. Parse the json resource failed.
 
**错误描述**
 
资源解析失败。
 
**可能原因**
 
用户传入的资源内容有误。
 
**处理步骤**
 
- 请检查传入的图标资源是否正确。
- 请检查传入的动效参数资源是否正确。
