# 如何整合多个module模块的单元测试

更新时间：2026-07-22 12:10:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-37

#### 问题现象

在开发多module模块项目时，如果多个模块均开发单元测试，如何将不同模块的单元测试进行汇总执行，达到快速验证的效果。
 
 

#### 背景知识

[Local Test](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-local-test)：测试用例存放在Test测试目录下，不需要运行在设备或模拟器上。Local Test支持ArkTS语言，仅支持Stage模型，不支持测试C/C++方法及系统API。
 
 

#### 解决方案

如果要联合多个Local Test进行集中测试验证，需要创建Compound并关联上所有的Local Test测试用例，直接运行Compound即可对所有的Local Test进行测试验证：
 1. 在工具栏主菜单点击Run->Edit Configurations。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/HqVwuxxfSZS2ZF_e48mVnQ/zh-cn_image_0000002675023655.png?HW-CC-KV=V1&HW-CC-Date=20260730T072723Z&HW-CC-Expire=86400&HW-CC-Sign=36BB7AED6CB107E694C390286AB25A9DBF667BBA8B44583D1E1514C05A53C1BF)

2. 点击Add New Configuration，即左上角的+，选择Local Test，给所有要测试的模块创建LocalTest。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/Xcuu6xZwSaCwO4mzMcwPlA/zh-cn_image_0000002644943828.png?HW-CC-KV=V1&HW-CC-Date=20260730T072723Z&HW-CC-Expire=86400&HW-CC-Sign=10D34C73BA671C28E0B3442FD4712FD9580253DCDD5384EEDB4118AC13ACF60B)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/jCPywBpxT5inbXo8Jfa3Nw/zh-cn_image_0000002675103535.png?HW-CC-KV=V1&HW-CC-Date=20260730T072723Z&HW-CC-Expire=86400&HW-CC-Sign=13178DA70C0796A40AD9CD0757E38E67EC6DAD7A929267B94D4FB07C9FC23DD2)

3. 点击Add New Configuration，即左上角的+，选择Compound，创建Compound复合类型将多个子SDK的所有单元测试都加进去，之后再点击应用，点击确认。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/Nzk_ALVjS8CI1iVpgftImQ/zh-cn_image_0000002675103933.png?HW-CC-KV=V1&HW-CC-Date=20260730T072723Z&HW-CC-Expire=86400&HW-CC-Sign=B099FA2F91C1F82D26E4B7DD08A4ECBAB38E88B5643E43DD067CBFE4CF46A73B)

4. 选中刚才编辑好的复合类型名称，点击运行即可执行整合的单元测试。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/fQ2NEUl5SjOoZ93I-PCrrw/zh-cn_image_0000002645104202.png?HW-CC-KV=V1&HW-CC-Date=20260730T072723Z&HW-CC-Expire=86400&HW-CC-Sign=BA5738F22E304A0EFE4C1F60E57E387D091FADDE02AC240789E23FDC0AF12CF9)

 
 

#### 常见FAQ

Q：单元测试报告，是否支持输出lcov.info格式文件，或者可以转化为lcov.info格式？
 
A：单元测试报告目前只有html+json格式。
 
Q：多个module如何进行单元测试，测试代码希望能够复用？
 
A：多个module按照正常用例编写，测试代码如果不涉及mock，按照正常重构方法进行提取。
