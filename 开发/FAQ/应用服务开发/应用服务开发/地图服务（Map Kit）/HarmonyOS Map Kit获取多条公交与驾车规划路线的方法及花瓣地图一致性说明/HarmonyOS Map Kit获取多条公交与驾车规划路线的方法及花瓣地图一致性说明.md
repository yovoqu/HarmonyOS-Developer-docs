# HarmonyOS Map Kit获取多条公交与驾车规划路线的方法及花瓣地图一致性说明

更新时间：2026-07-30 01:03:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-51

#### 问题现象

场景一：Map Kit的getTransitRoutes查询到路线规划与花瓣地图查询结果相同吗？
 
场景二：调用getDrivingRoutes只返回一条驾车路线，如何获取多条备选路线？
 
 

#### 解决方案

 

#### 场景一

通过Map Kit的getTransitRoutes查询到的路线规划结果与花瓣地图一致，均使用相同的内部查询接口。正常getTransitRoutes会返回多条路线，如result = await navi.getTransitRoutes(this.getUIContext().getHostContext(), params)，此时result.routes为所有返回路线规划的列表，遍历列表可以查看所有路线规划。
 
 

#### 场景二

在[DrivingRouteParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-navi-api#drivingrouteparams)中将alternatives设置为true，即可返回多条备选路线。alternatives默认为false，表示不返回多条备选路线。[getDrivingRoutes](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-navi-api#getdrivingroutes)最多可返回3条路线，但是否有多条还取决于服务端实际规划结果。
 
示例代码如下：
```text
let params: navi.DrivingRouteParams = {
  origins: [{ latitude: 31.98, longitude: 120.27 }],
  destination: { latitude: 31.98, longitude: 120.32 },
  language: 'zh_CN',
  alternatives: true
};
try {
  const result = await navi.getDrivingRoutes(params);
  if (result && result.routes) {
    console.info(`result.routes.length: ${result.routes.length}`);
  }
} catch (error) {
  console.error(`getDrivingRoutes error: ${error}`);
}
```
 
 
调用后查看result.routes.length获取实际返回的路线数量。
