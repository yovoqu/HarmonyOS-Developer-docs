# 小艺开放平台云插件调用云函数报错“域名只支持HTTPS和WSS协议，且须为公网地址”如何解决

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-agent-framework-6

## 小艺开放平台云插件调用云函数报错“域名只支持HTTPS和WSS协议，且须为公网地址”如何解决
 


##### 问题现象

- 小艺开放平台中使用云插件调用云函数报错“域名只支持HTTPS和WSS协议，且须为公网地址”，域名可通过apifox测试。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/_-qVYF29RG-RVNEN4EWgNg/zh-cn_image_0000002628394846.png?HW-CC-KV=V1&HW-CC-Date=20260701T025934Z&HW-CC-Expire=86400&HW-CC-Sign=1868FABBC7CC2C59526DB25A7E93E912FBB876223C54226F996ACC6E3B054EBC)

 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/DpnjQCXlQ2-SqhqnvoZRaA/zh-cn_image_0000002628554742.png?HW-CC-KV=V1&HW-CC-Date=20260701T025934Z&HW-CC-Expire=86400&HW-CC-Sign=A775ED458A365BB56054F2254C6C7949709D82D4887ACE8984E94BBFB95D1019)

- 小艺开放平台调用云函数，填写URL后报错“域名只支持HTTPS和WSS协议，且须为公网地址”。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/IgQ-fNG6RUeupDFYmcnSKg/zh-cn_image_0000002658914067.png?HW-CC-KV=V1&HW-CC-Date=20260701T025934Z&HW-CC-Expire=86400&HW-CC-Sign=134EDA5114EF1A0A5463CDE732B32CB61479141F7BD7654176650AB38BE5CBFC)

 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/fNBLhsEeTlawlcspU4l1Fw/zh-cn_image_0000002658794113.png?HW-CC-KV=V1&HW-CC-Date=20260701T025934Z&HW-CC-Expire=86400&HW-CC-Sign=B6DAC077A83D6D647C0BB9CDE53B1AE1BDD52861D31C5DD8FF7BF5CDCFA8A02D)


 
 

##### 解决方案

- 云插件URL是强制匹配，在apifox成功的前提下，URL后面不可以带任何多余字符串，若URL后存在空格，则会报错“域名只支持HTTPS和WSS协议，且须为公网地址”，删除URL路径中空格后正常请求云函数：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/uhJK63suQqK0Lojx6HnrMg/zh-cn_image_0000002628394848.png?HW-CC-KV=V1&HW-CC-Date=20260701T025934Z&HW-CC-Expire=86400&HW-CC-Sign=F52407246C214034131A30321F31640DDC399AB4CA1DB52DFF98B5862B0A1369)

- API URL地址和工具路径拼起来需要是一个完整的API地址，同时也是要跟最终需要的函数地址相同，正确填写URL后可正常调用云函数。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/UrzLUcjlQRWJ9s6zOvE5qw/zh-cn_image_0000002628554744.png?HW-CC-KV=V1&HW-CC-Date=20260701T025934Z&HW-CC-Expire=86400&HW-CC-Sign=7CBD8FF2AA27F091B389564171148D9A8812063386572B37CDBB8F669CCEAFEF)

 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/eXpHT-E0SXed0xfWeLDHwg/zh-cn_image_0000002658914069.png?HW-CC-KV=V1&HW-CC-Date=20260701T025934Z&HW-CC-Expire=86400&HW-CC-Sign=9801E6BADF9D7F260CD0EA2AEDB6951F4301E46A51D6C82E99D46152AB74BD3D)
