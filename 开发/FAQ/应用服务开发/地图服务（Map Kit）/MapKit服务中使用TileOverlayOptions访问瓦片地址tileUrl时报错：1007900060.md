# MapKit服务中使用TileOverlayOptions访问瓦片地址tileUrl时报错：1007900060

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-23

## MapKit服务中使用TileOverlayOptions访问瓦片地址tileUrl时报错：1007900060
 


##### 问题现象

在MapKit服务中使用TileOverlayOptions访问瓦片地址tileUrl时报错SSL peer certificate or SSH remote key was not OK，code:1007900060请问如何才能正确的设置证书或者在测试阶段绕过证书验证？
 
 

##### 解决方案

在线下载瓦片图层方法，当前仅支持传出URL，不支持配置RCP策略，默认使用系统CA配置。
 
如果需要自行配置RCP策略，可以使用[本地加载](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-tile#section392813231836)瓦片图层方法，需要您在指导中的tileProviderMethod方法中自行实现配置定制化RCP策略访问URL，下载瓦片并加载。
