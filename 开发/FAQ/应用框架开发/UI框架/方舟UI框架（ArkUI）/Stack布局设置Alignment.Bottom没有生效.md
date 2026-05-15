# Stack布局设置Alignment.Bottom没有生效

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-160

问题现象

在build()中使用Stack作为容器，设置alignContent为Alignment.Bottom，同时设置align为Alignment.Center。但alignContent为Alignment.Bottom未生效。


![图片](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/SnQfbOcOTIiyf6uiEaQfYQ/zh-cn_image_0000002229604149.png?HW-CC-KV=V1&HW-CC-Date=20260515T045749Z&HW-CC-Expire=86400&HW-CC-Sign=216BE0C8F79040C47028BDF3890A91C9178DEF1C2D21BA41916E40E1F407CC06)


解决措施

由于Stack布局默认采用单一对齐策略，当同时设置alignContent与align属性时，后设置的值将生效。
