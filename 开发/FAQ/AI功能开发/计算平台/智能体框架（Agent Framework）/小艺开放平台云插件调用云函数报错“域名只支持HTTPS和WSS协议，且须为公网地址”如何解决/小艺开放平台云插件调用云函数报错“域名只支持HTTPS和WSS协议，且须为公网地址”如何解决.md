# 小艺开放平台云插件调用云函数报错“域名只支持HTTPS和WSS协议，且须为公网地址”如何解决

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-agent-framework-6

#### 问题现象
1. 小艺开放平台中使用云插件调用云函数报错“域名只支持HTTPS和WSS协议，且须为公网地址”，域名可通过apifox测试。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/_-qVYF29RG-RVNEN4EWgNg/zh-cn_image_0000002628394846.png?HW-CC-KV=V1&HW-CC-Date=20260723T014052Z&HW-CC-Expire=86400&HW-CC-Sign=738E7B733A63AF60DE41BCA14EB89280912D8F9B4E0320A4952B2EDF564BA97E)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/DpnjQCXlQ2-SqhqnvoZRaA/zh-cn_image_0000002628554742.png?HW-CC-KV=V1&HW-CC-Date=20260723T014052Z&HW-CC-Expire=86400&HW-CC-Sign=A72D621FF75AFCBA24D3EC1A20470319ED0F030C217A79F44CC8680776F450A8)

2. 小艺开放平台调用云函数，填写URL后报错“域名只支持HTTPS和WSS协议，且须为公网地址”。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/IgQ-fNG6RUeupDFYmcnSKg/zh-cn_image_0000002658914067.png?HW-CC-KV=V1&HW-CC-Date=20260723T014052Z&HW-CC-Expire=86400&HW-CC-Sign=A67AF420DA0A2F41E4EDAECAAEB8C083BF29960FDA648B90BBE297F6FD14671D)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/fNBLhsEeTlawlcspU4l1Fw/zh-cn_image_0000002658794113.png?HW-CC-KV=V1&HW-CC-Date=20260723T014052Z&HW-CC-Expire=86400&HW-CC-Sign=22FCFB00F8A62EE8D23EFE8D72AC57C92D1CF145EFED48B10F345B5CE28275D9)

 
 

#### 解决方案
1. 云插件URL是强制匹配，在apifox成功的前提下，URL后面不可以带任何多余字符串，若URL后存在空格，则会报错“域名只支持HTTPS和WSS协议，且须为公网地址”，删除URL路径中空格后正常请求云函数：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/uhJK63suQqK0Lojx6HnrMg/zh-cn_image_0000002628394848.png?HW-CC-KV=V1&HW-CC-Date=20260723T014052Z&HW-CC-Expire=86400&HW-CC-Sign=3C386F295752AE235ECA98539703249C5D4B86E584D10879A4291CBACE245156)

2. API URL地址和工具路径拼起来需要是一个完整的API地址，同时也是要跟最终需要的函数地址相同，正确填写URL后可正常调用云函数。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/UrzLUcjlQRWJ9s6zOvE5qw/zh-cn_image_0000002628554744.png?HW-CC-KV=V1&HW-CC-Date=20260723T014052Z&HW-CC-Expire=86400&HW-CC-Sign=F852BCD018D471A882DFCA01BF3D50D409C3BFD31758D1D1EE42DC45D51FDA4B)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/eXpHT-E0SXed0xfWeLDHwg/zh-cn_image_0000002658914069.png?HW-CC-KV=V1&HW-CC-Date=20260723T014052Z&HW-CC-Expire=86400&HW-CC-Sign=B50725F731EC740125B59A4A06CC52617CF12C63E9A1680FC93D75CDAA0C6048)
