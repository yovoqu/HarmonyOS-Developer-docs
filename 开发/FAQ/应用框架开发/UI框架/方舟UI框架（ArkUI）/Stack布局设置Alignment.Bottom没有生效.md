# Stack布局设置Alignment.Bottom没有生效

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-160

**问题现象**
 
在build()中使用Stack作为容器，设置alignContent为Alignment.Bottom，同时设置align为Alignment.Center。但alignContent为Alignment.Bottom未生效。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/WnQvOBGITZKJEa8rZ7K2hg/zh-cn_image_0000002229604149.png?HW-CC-KV=V1&HW-CC-Date=20260528T013311Z&HW-CC-Expire=86400&HW-CC-Sign=8ACB9CEC35E46FA24F0BBE7BCA3758FA9E1304EA6E00FA93389AC1B273E9BF73)

 
**解决措施**
 
由于Stack布局默认采用单一对齐策略，当同时设置alignContent与align属性时，后设置的值将生效。
