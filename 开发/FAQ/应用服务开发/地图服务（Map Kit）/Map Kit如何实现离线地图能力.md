# Map Kit如何实现离线地图能力

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-25

## Map Kit如何实现离线地图能力
 


##### 问题现象

应用在使用地图时，可能存在特殊环境无网络情况，Map Kit如何实现离线地图能力。
 
 

##### 解决方案

HarmonyOS Next从API 20版本开始支持离线地图能力。
 
- 手机打开“地图”应用（Petal Maps）,选择“我的”-“离线地图”-“地图资源管理”-“地区列表”，下载“全球基础包”，如果需要更详细的城市地图，可在“地区列表”页面下载指定城市的离线地图。
- 开发应用时，按照[地图显示](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-presenting#section17751438104210)章节创建地图。应用运行后，在无网络情况下，自动使用步骤1下载的离线地图。
