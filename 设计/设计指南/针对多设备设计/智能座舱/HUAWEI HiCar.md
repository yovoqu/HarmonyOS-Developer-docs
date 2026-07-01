# HUAWEI HiCar

更新时间：2026-06-12 09:08:30

来源：https://developer.huawei.com/consumer/cn/doc/design-guides/smart-cockpit-hicar-0000002592646358

#### 深色模式

应用需支持深、浅两种模式。
 
 

#### 沉浸式导航条

为便于显示时间等信息，并方便用户在桌面、常用应用中跳转，HUAWEI HiCar 设有常显的系统导航条。有以下特点：
 
1. 在设备屏幕高宽比大于 1/2 时，导航条位于屏幕左侧；小于 1/2 时，位于屏幕底部。
 
2. 应用的内容区域可包括导航条宽度，以呈现出沉浸式效果，但重要信息、功能（如应用导航），应避开系统导航条。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/xLLADdzoSTONDYCB00KEPQ/zh-cn_image_0000002592669342.png?HW-CC-KV=V1&HW-CC-Date=20260701T041520Z&HW-CC-Expire=86400&HW-CC-Sign=53127C4DD90BC16D9304D9B949F9744BB4F4272453616D107A8252ECA07E07F5)

 
 

#### 导航与其他应用分屏

 
为便于导航与应用并行的场景，系统支持导航与其他应用分屏呈现，对于不同的屏幕，有以下分屏规则：
 
1. 9 寸以下的小屏、扁屏不支持分屏。
 
2. 常规矩形屏支持左右窗口 1:2 的分屏，应用窗口宽高比约为 9:5。
 
3. 竖屏和较小的屏幕，使用左右窗口 1:1 的分屏。
 
强烈建议应用可支持无级调节窗口大小。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/h17kG17MTQOtDsWjaU_A5g/zh-cn_image_0000002622988861.png?HW-CC-KV=V1&HW-CC-Date=20260701T041520Z&HW-CC-Expire=86400&HW-CC-Sign=F0D3667214A3054C9CBBECFA7A6FF2079353A641DF1EDAFB93461E7C336AE97F)
