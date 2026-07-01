# 小艺开放平台云插件调用云函数报错“域名只支持HTTPS和WSS协议，且须为公网地址”如何解决

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-agent-framework-6

#### 问题现象
1. 小艺开放平台中使用云插件调用云函数报错“域名只支持HTTPS和WSS协议，且须为公网地址”，域名可通过apifox测试。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/_-qVYF29RG-RVNEN4EWgNg/zh-cn_image_0000002628394846.png?HW-CC-KV=V1&HW-CC-Date=20260701T041005Z&HW-CC-Expire=86400&HW-CC-Sign=F8CE65EB3C0FA6F200725DC7172BE5E929EBB1B024450CEFB731774578C16DD4)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/DpnjQCXlQ2-SqhqnvoZRaA/zh-cn_image_0000002628554742.png?HW-CC-KV=V1&HW-CC-Date=20260701T041005Z&HW-CC-Expire=86400&HW-CC-Sign=ABF2C4AF223BCBF0B28E65F55D71ABB02FD8F40E09573170B46C084BD7A69BCD)

2. 小艺开放平台调用云函数，填写URL后报错“域名只支持HTTPS和WSS协议，且须为公网地址”。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/IgQ-fNG6RUeupDFYmcnSKg/zh-cn_image_0000002658914067.png?HW-CC-KV=V1&HW-CC-Date=20260701T041005Z&HW-CC-Expire=86400&HW-CC-Sign=36602C9CDF2D0ECC4056BAC51BFFE23DCD3811BC379429A66509A8B6179704F2)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/fNBLhsEeTlawlcspU4l1Fw/zh-cn_image_0000002658794113.png?HW-CC-KV=V1&HW-CC-Date=20260701T041005Z&HW-CC-Expire=86400&HW-CC-Sign=C1D5D4AF710157383B94AF7777E95A55A203AC062FF1250E79000F805B569F19)

 
 

#### 解决方案
1. 云插件URL是强制匹配，在apifox成功的前提下，URL后面不可以带任何多余字符串，若URL后存在空格，则会报错“域名只支持HTTPS和WSS协议，且须为公网地址”，删除URL路径中空格后正常请求云函数：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/uhJK63suQqK0Lojx6HnrMg/zh-cn_image_0000002628394848.png?HW-CC-KV=V1&HW-CC-Date=20260701T041005Z&HW-CC-Expire=86400&HW-CC-Sign=AD5B97BC2841F923931B19E33BAC977C2FE187AD9147DF9C8C0834FBF3E95D74)

2. API URL地址和工具路径拼起来需要是一个完整的API地址，同时也是要跟最终需要的函数地址相同，正确填写URL后可正常调用云函数。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/UrzLUcjlQRWJ9s6zOvE5qw/zh-cn_image_0000002628554744.png?HW-CC-KV=V1&HW-CC-Date=20260701T041005Z&HW-CC-Expire=86400&HW-CC-Sign=50CB72A21549B98E21D6353EE5C4658BFB61345F014B9F9DC3C6D4A799F035EF)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/eXpHT-E0SXed0xfWeLDHwg/zh-cn_image_0000002658914069.png?HW-CC-KV=V1&HW-CC-Date=20260701T041005Z&HW-CC-Expire=86400&HW-CC-Sign=363CD9AF5C5CB798684B309059C2E09D9FD2C4ADCCF541C19C90B3DF25FA1965)
