# 申请接入Wear Engine服务咨询

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-wear-engine-2

#### 问题现象

接入Wear Engine服务，填写申请中对选项疑问咨询。
 
问题一：针对与旧版本穿戴应用通信的手机移动应用的兼容选项存在疑问。
 
问题二：对权限中设备能力类的各个权限有疑惑。
 
问题三：对基本信息选项有疑惑。
 
问题四：运动表引入[Wear Engine SDK (Lite Wearable Devices)](https://developer.huawei.com/consumer/en/doc/connectivity-Library/litewearable-sdk-cn-0000001705004353)后编译报错，报错内容如下：
 
```text
<span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">hvigor </span><span style="color: rgb(181,106,1);">ERROR</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Failed </span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(181,106,1);">entry</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(0,0,255);">default</span><span style="color: rgb(181,106,1);">@</span><span style="color: rgb(0,0,255);">LegacyBuildJS</span><span style="color: rgb(181,106,1);">...</span>
<span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">hvigor </span><span style="color: rgb(181,106,1);">ERROR</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Tools execution failed</span><span style="color: rgb(181,106,1);">.</span>
<span style="color: rgb(0,0,255);">Module not </span><span style="color: rgb(181,106,1);">found</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(181,106,1);">Error</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Can</span><span style="color: rgb(255,0,170);">'t resolve '</span><span style="color: rgb(181,106,1);">@</span><span style="color: rgb(0,0,255);">system</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">wearengine</span><span style="color: rgb(255,0,170);">' in '</span>D<span style="color: rgb(181,106,1);">:</span>\<span style="color: rgb(0,0,255);">Demo</span>\<span style="color: rgb(0,0,255);">entry</span>\<span style="color: rgb(0,0,255);">src</span>\<span style="color: rgb(0,0,255);">main</span>\<span style="color: rgb(0,0,255);">js</span>\<span style="color: rgb(0,0,255);">MainAbility</span>\<span style="color: rgb(0,0,255);">pages</span>'
  <span style="color: rgb(181,106,1);">Detail</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Please check the message from tools</span><span style="color: rgb(181,106,1);">.</span>
<span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">hvigor ERROR BUILD FAILED </span>in <span style="color: rgb(255,0,0);">10 </span><span style="color: rgb(0,0,255);">s </span><span style="color: rgb(255,0,0);">445 </span><span style="color: rgb(0,0,255);">ms</span>
```
 
问题五：若智能表在申请Wear Engine服务时未申请佩戴状态服务，应当如何获取佩戴状态或传感器服务？
 
问题六：若开发者不计划接入Wear Engine SDK，应如何通过手机应用获取穿戴设备的传感器数据？
 
 

#### 解决方案

问题一：这里兼容的目的是让HarmonyOS Next手机应用与旧版本的的其他平台手表应用通信（系统内部会将HarmonyOS Next应用包名转为映射其他平台包名）。
 
问题二：权限可参考[权限说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wearengine_apply)。
 
问题三：
 
- 智能穿戴设备与轻量级穿戴设备的区别：
智能穿戴（Wearable）：如Watch3、Watch4系列智能表。
- 轻量级智能穿戴（Lite Wearable）：如HUAWEI WATCH GT系列、Watch D系列、Fit系列、Watch Ultimate系列。

 - 是否开发在该穿戴设备上的应用？
是，指的是开发手机、手表侧应用。
- 否，指的是只开发手机侧应用。

 
 
问题四：Wear Engine SDK只支持设备类型为：Lite Wearable，将deviceType中Wearable设备类型去掉即可。
 
问题五：可以参考[传感器服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sensor-service-kit)文档。
 
问题六：可以通过华为运动健康授权，调用运动健康相关接口，获取此类信息，参考[华为运动健康服务接入流程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-application-access)。
