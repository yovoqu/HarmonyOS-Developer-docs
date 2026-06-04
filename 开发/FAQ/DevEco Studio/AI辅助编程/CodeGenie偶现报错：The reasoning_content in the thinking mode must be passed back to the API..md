# CodeGenie偶现报错：The reasoning_content in the thinking mode must be passed back to the API.

更新时间：2026-05-22 09:48:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-codegenie-3

**问题现象**
 
DevEco Studio 6.1.0 Release（6.1.0.850）及以上版本，在CodeGenie中通过URL方式配置deepseek-v4模型后，过程中界面提示“The reasoning_content in the thinking mode must be passed back to the API.”。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/CDfiAu6aTJ-h7J-utJ-kTA/zh-cn_image_0000002579793908.png?HW-CC-KV=V1&HW-CC-Date=20260604T013000Z&HW-CC-Expire=86400&HW-CC-Sign=222F955B159E92CAD17553F0F2955E872CF67EB99E5588BD35FD0593153DB2BF)

 
**解决措施**
 
使用Service Provider（服务提供商）方式配置模型，并在使用过程中打开深度思考。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/OmXuBzu6TGCr_a98pt8q1w/zh-cn_image_0000002610073801.png?HW-CC-KV=V1&HW-CC-Date=20260604T013000Z&HW-CC-Expire=86400&HW-CC-Sign=986E0BAB23C63F81DF165CB8A98240B4B8347F469C6F18A278D2FC5F60BF1AA6)
