# 小艺开放平台云插件调用云函数报错“域名只支持HTTPS和WSS协议，且须为公网地址”如何解决

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-agent-framework-6

#### 问题现象
1. 小艺开放平台中使用云插件调用云函数报错“域名只支持HTTPS和WSS协议，且须为公网地址”，域名可通过apifox测试。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/_-qVYF29RG-RVNEN4EWgNg/zh-cn_image_0000002628394846.png?HW-CC-KV=V1&HW-CC-Date=20260730T072734Z&HW-CC-Expire=86400&HW-CC-Sign=AB54C2DEF2735D97F8CD6AEA788423741F5BB875863E6B8EBDFA864EFE81652E)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/DpnjQCXlQ2-SqhqnvoZRaA/zh-cn_image_0000002628554742.png?HW-CC-KV=V1&HW-CC-Date=20260730T072734Z&HW-CC-Expire=86400&HW-CC-Sign=FFFF40D950B7249DC226BBD9ABCD4B78D5992A4310B502B2B9F6BFA0186CACF7)

2. 小艺开放平台调用云函数，填写URL后报错“域名只支持HTTPS和WSS协议，且须为公网地址”。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/IgQ-fNG6RUeupDFYmcnSKg/zh-cn_image_0000002658914067.png?HW-CC-KV=V1&HW-CC-Date=20260730T072734Z&HW-CC-Expire=86400&HW-CC-Sign=03C664A84C7414EE14EAA83099527C987F1341DA80B1636E95B8EC2C4A8F208A)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/fNBLhsEeTlawlcspU4l1Fw/zh-cn_image_0000002658794113.png?HW-CC-KV=V1&HW-CC-Date=20260730T072734Z&HW-CC-Expire=86400&HW-CC-Sign=1856AB10219F6BDFCEC3B20E0B43B7D3ADEB4495EFA9450D84FDD5018C4984AA)

 
 

#### 解决方案
1. 云插件URL是强制匹配，在apifox成功的前提下，URL后面不可以带任何多余字符串，若URL后存在空格，则会报错“域名只支持HTTPS和WSS协议，且须为公网地址”，删除URL路径中空格后正常请求云函数：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/uhJK63suQqK0Lojx6HnrMg/zh-cn_image_0000002628394848.png?HW-CC-KV=V1&HW-CC-Date=20260730T072734Z&HW-CC-Expire=86400&HW-CC-Sign=8D4C92D5A333462D1EC68BF0611E5CE31FCE6BCB0BED060C62F094F26509AF1E)

2. API URL地址和工具路径拼起来需要是一个完整的API地址，同时也是要跟最终需要的函数地址相同，正确填写URL后可正常调用云函数。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/UrzLUcjlQRWJ9s6zOvE5qw/zh-cn_image_0000002628554744.png?HW-CC-KV=V1&HW-CC-Date=20260730T072734Z&HW-CC-Expire=86400&HW-CC-Sign=543760CCE24988C3FF6F1730BEFAC4F20F2A1A94690D499A53A28AF9EE74ED0F)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/eXpHT-E0SXed0xfWeLDHwg/zh-cn_image_0000002658914069.png?HW-CC-KV=V1&HW-CC-Date=20260730T072734Z&HW-CC-Expire=86400&HW-CC-Sign=DC5E298DB503F058B306E1600782E55544071328A9ACF28A98A7ED4D0CED9C76)
