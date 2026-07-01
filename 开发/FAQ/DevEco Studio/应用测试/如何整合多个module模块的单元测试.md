# 如何整合多个module模块的单元测试

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-37

## 如何整合多个module模块的单元测试
 


##### 问题现象

在开发多module模块项目时，如果多个模块均开发单元测试，如何将不同模块的单元测试进行汇总执行，达到快速验证的效果。
 
 

##### 背景知识

[Local Test](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-local-test)：测试用例存放在test测试目录下，不需要运行在设备或模拟器上。Local Test支持ArkTS语言，仅支持Stage模型，不支持测试C/C++方法及系统API。
 
 

##### 解决方案

如果要联合多个Local Test进行集中测试验证，需要创建Compound并关联上所有的Local Test测试用例，直接运行Compound即可对所有的Local Test进行测试验证：
 
- 在工具栏主菜单点击Run->Edit Configurations。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/AXG8xQ9eTKCfcG7aDxXJrg/zh-cn_image_0000002628409646.png?HW-CC-KV=V1&HW-CC-Date=20260701T025923Z&HW-CC-Expire=86400&HW-CC-Sign=F5CBF5B2734EAFF902FEE1B05F073EA7616A73D4F04AA35BD11056068BC09212)

- 点击Add New Configuration，即左上角的+，选择Local Test，给所有要测试的模块创建LocalTest。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/-RpibBTETdO_hQ7UwrtBXQ/zh-cn_image_0000002658808907.png?HW-CC-KV=V1&HW-CC-Date=20260701T025923Z&HW-CC-Expire=86400&HW-CC-Sign=D01B44A1EF6BA87175B2FAF167766A7BA70A572446961F8B3C303EAAC5C09913)

 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/lLOmgJ0TQuqw_OhfoTsglw/zh-cn_image_0000002628569538.png?HW-CC-KV=V1&HW-CC-Date=20260701T025923Z&HW-CC-Expire=86400&HW-CC-Sign=802837A477A28116D7B340455B6190C640D34437588BCE45ED626A73653E1AB0)

- 点击Add New Configuration，即左上角的+，选择Compound，创建Compound复合类型将多个子SDK的所有单元测试都加进去，之后再点击应用，点击确认。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/uNXSGx0tSOeFM6dvjQ-u4Q/zh-cn_image_0000002658928863.png?HW-CC-KV=V1&HW-CC-Date=20260701T025923Z&HW-CC-Expire=86400&HW-CC-Sign=62938B46715E5B06828A2269C0ACFFC29515E8294F954FD27CB38333141FF699)

- 选中刚才编辑好的复合类型名称，点击运行即可执行整合的单元测试。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/B-9L_Hz3RhKBAx4cK8lYsw/zh-cn_image_0000002628409648.png?HW-CC-KV=V1&HW-CC-Date=20260701T025923Z&HW-CC-Expire=86400&HW-CC-Sign=949511EEBA880FB49AFBA3BB894F851D268F5B8C2A6D1ACF274941DAF32C1EC1)


 
 

##### 常见FAQ

Q：单元测试报告，是否支持输出lcov.info格式文件，或者可以转化为lcov.info格式？
 
A：单元测试报告目前只有html+json格式。
