# 添加Page

更新时间：2026-04-30 02:42:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-add-page

在ArkTS语言的工程中，支持添加Page。Page是表示应用/元服务的一个页面。应用/元服务可以设计为多个功能页面，每个页面进行单独的文件管理，并通过路由API实现页面的调度管理，以实现应用内功能的解耦。ArkTS语言的工程添加Page后，会在pages文件夹下生成一个新的ets文件。
 
从DevEco Studio 6.1.0 Beta2版本开始，在API 23及以上工程，支持Car设备添加Map Page和Payment Page。
 

##### 操作步骤
1. 在Stage工程中选中ets文件夹下的**pages**，单击鼠标右键，选择**New > Page**，当前提供如下Page类型：

  
Empty Page：创建一个普通页面，展示基础的Hello World功能；
2. Map Page：创建一个地图页面，展示地图视图功能，当前仅支持在Phone和Car设备中使用；
3. Payment Page：创建一个支付页面，可以实现点击按钮唤起支付弹窗，当前仅支持在Phone和Car设备中使用；
4. Iap Page：IAP Kit场景化模板，支持快速创建应用内支付购买虚拟数字商品相关代码。
5. 输入Page name（由大小写字母、数字和下划线组成），单击**Finish**完成添加。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/eklyozzAQJ6VH4Hr0rjTHQ/zh-cn_image_0000002602066499.png?HW-CC-KV=V1&HW-CC-Date=20260528T015015Z&HW-CC-Expire=86400&HW-CC-Sign=5EF79E1CFA6D2027EBC498BEE68979033224084C0116D69FEDE417C7B594780B)
