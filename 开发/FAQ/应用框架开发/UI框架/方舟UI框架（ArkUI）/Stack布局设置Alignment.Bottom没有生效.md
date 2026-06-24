# Stack布局设置Alignment.Bottom没有生效

更新时间：2026-06-15 08:43:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-160

**问题现象**
 
在build()中使用Stack作为容器，设置alignContent为Alignment.Bottom，同时设置align为Alignment.Center。但alignContent为Alignment.Bottom未生效。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/H4fSfkQQRaKl9rEqDFvpeA/zh-cn_image_0000002229604149.png?HW-CC-KV=V1&HW-CC-Date=20260624T020557Z&HW-CC-Expire=86400&HW-CC-Sign=01DEBC4D1D48BB6B054BF92AA1749F941F9AEA3ECFE4A1D326E5BDC3BB844AF0)

 
**解决措施**
 
由于Stack布局默认采用单一对齐策略，当同时设置alignContent与align属性时，后设置的值将生效。
