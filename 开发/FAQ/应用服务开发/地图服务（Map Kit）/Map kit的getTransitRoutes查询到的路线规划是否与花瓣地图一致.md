# Map kit的getTransitRoutes查询到的路线规划是否与花瓣地图一致

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-51

## Map kit的getTransitRoutes查询到的路线规划是否与花瓣地图一致
 


##### 问题现象

Map Kit的getTransitRoutes查询到路线规划与花瓣地图查询结果相同吗？
 
 

##### 解决方案

通过Map Kit的getTransitRoutes查询到的路线规划结果与花瓣地图一致，均使用相同的内部查询接口。正常getTransitRoutes会返回多条路线，如result = await navi.getTransitRoutes(this.getUIContext().getHostContext(), params)，此时result.routes为所有返回路线规划的列表，遍历列表可以查看所有路线规划。
