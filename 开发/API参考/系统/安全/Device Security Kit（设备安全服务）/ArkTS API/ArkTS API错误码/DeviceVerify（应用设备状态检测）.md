# DeviceVerify（应用设备状态检测）

更新时间：2026-06-12 06:54:11

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-devicesecurity-deviceverify

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

## DeviceVerify（应用设备状态检测）
   
    
     
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/_7dsy_8TTJGDaav_LOxGxw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260701T025448Z&HW-CC-Expire=86400&HW-CC-Sign=342466BFA8C94535E4A82B5DB9E15E44D7A62192D2A28F832946D77218D1BBE3)
      
      
以下仅介绍本模块特有错误码，通用错误码请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。
     
    
    
          
##### 201 权限校验失败
     
**错误信息**
     
has no permission.
     
**错误描述**
     
权限校验失败。
     
**可能原因**
     
应用hap未开通Device Security服务。
     
**处理步骤**
     
 - 请参见[开通Device Security服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-deviceverify-activateservice)在AppGallery Connect开启“应用设备状态检测”开关。
 - 重新[申请调试Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-add-debugprofile-0000001914423102)，将新申请到的Profile作为工程的签名文件后重试。
     
    
    
          
##### 1003300005 内部异常
     
**错误信息**
     
internal error.
     
**错误描述**
     
内部异常。
     
**可能原因**
     
接口执行流程中调用系统其它接口出现异常。
     
**处理步骤**
     
请优先重试，若重试不成功，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)申请帮助。
    
    
          
##### 1003300006 访问云端服务器异常
     
**错误信息**
     
access cloud server fail.
     
**错误描述**
     
访问云端服务器异常。
     
**可能原因**
     
设备未联网或设备网络不稳定。
     
**处理步骤**
     
如未联网，请连接网络后重新发起请求，如联网，可能是网络不稳定，请重试。
