# 如何定位UX测试结果不通过问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ux-basic-quality-test-1

#### 问题现象

- 问题一：使用DevEco Testing执行UX测试结果显示“条件依赖”，报“arklayout文件存储失败”或“arklayout文件依赖调试版本应用”：测试结果：条件依赖。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/piqsw--uQESH8Spwud5Rew/zh-cn_image_0000002628563632.png?HW-CC-KV=V1&HW-CC-Date=20260730T072728Z&HW-CC-Expire=86400&HW-CC-Sign=0BCBAA9CA75A54059B0865F4D388E4560FB5BF0FEB5B2A289701041F29AFDA0F)


  原因说明：arklayout文件存储失败。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/i4bTzWqRQr-tHPDuj9aubw/zh-cn_image_0000002658922937.png?HW-CC-KV=V1&HW-CC-Date=20260730T072728Z&HW-CC-Expire=86400&HW-CC-Sign=59CB9EDDDE63FDEEC5F7ABA2D7DAAA08A22DCB4E8DC7A7B4FF828E29EDDBFE3C)


  原因说明：arklayout文件依赖调试版本应用。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/3QEjao7FSq6yTJ8V9w0j1Q/zh-cn_image_0000002658802983.png?HW-CC-KV=V1&HW-CC-Date=20260730T072728Z&HW-CC-Expire=86400&HW-CC-Sign=8159A3B3BF0EC9478696DCA496317F774D801768333A0CF135D4D02D222AC0D6)

- 问题二：UX检测结果显示“条件依赖”，报“应用包不存在”是什么原因？原因显示说明：应用包不存在。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/2OIanelbQgKa0bohLaIi4w/zh-cn_image_0000002628403724.png?HW-CC-KV=V1&HW-CC-Date=20260730T072728Z&HW-CC-Expire=86400&HW-CC-Sign=ADC25B7729300EA2C709F4C603AC63992C4349704F89A1EB5707439FF59162D9)

- 问题三：UX检测结果显示“元服务胶囊热区冲突”不通过，导航栏过宽该如何解决？
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/41YfuJdRS427M9x5s6v4rQ/zh-cn_image_0000002628563634.png?HW-CC-KV=V1&HW-CC-Date=20260730T072728Z&HW-CC-Expire=86400&HW-CC-Sign=96D514E592E27152937623A63067B9803CAC106AA1EDF9F75B30D1A86198D805)

- 问题四：UX检测结果显示“不涉及”该如何处理？
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/J2Ws_FaaQliPl4tMzMn9Aw/zh-cn_image_0000002658922939.png?HW-CC-KV=V1&HW-CC-Date=20260730T072728Z&HW-CC-Expire=86400&HW-CC-Sign=E16B6A76107CC17F8E43C7894B474905D796972F0BBDE31B8DDE5978AE971215)

- 问题五：UX检测结果显示“不通过”，如何定位和修复？
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/YGEb3aTTTRGzAgaG_tkbmQ/zh-cn_image_0000002658802985.png?HW-CC-KV=V1&HW-CC-Date=20260730T072728Z&HW-CC-Expire=86400&HW-CC-Sign=D4EE4BA5DA7C2D8DD002C50D0F99B6A76D93483EA8270C80483CA7FD0417AC01)


 
 

#### 解决方案

- 问题一解决方案：UX检测时部分规则依赖debug版本应用进行测试，请安装应用的debug签名版本重启手机后重新测试。
- 问题二解决方案：UX检测时部分规则依赖应用包完成，如果手机上已安装了应用，UX测试的部分结果会提示应用包不存在，请通过DevEco Testing进行应用的安装和测试。
- 问题三解决方案：应用UX体验建议中关于热区的标准可参考[适用范围](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/experience-suggestions-ux#section1541617350183)中“点击热区”，使用[AtomicServiceNavigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-atomicservice-atomicservicenavigation#atomicservicenavigation-1)设置导航栏的宽度。
- 问题四解决方案：检测结果为不涉及代表测试用例的执行条件不满足，不会执行相关的测试场景，可以点击不涉及前面的“查看”进行详细查看。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/ZPLtJzYYR8iisPoM7ryxvA/zh-cn_image_0000002628403726.png?HW-CC-KV=V1&HW-CC-Date=20260730T072728Z&HW-CC-Expire=86400&HW-CC-Sign=42DA487F1CCACB4954FA65419E7D8928B8B9A2063358CA335842D69F0386A628)

- 问题五解决方案：举例“典型手势时长设计”测试不通过，点击对应的“不通过数”->查看定位日志和修复指南。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/yzqhQ_iaRLyQDvKtCmppwQ/zh-cn_image_0000002628563636.png?HW-CC-KV=V1&HW-CC-Date=20260730T072728Z&HW-CC-Expire=86400&HW-CC-Sign=5B638A5E4B5E97DD061DE69B9E094AD5C563D30FBAA3EFF35EA22FA850BBAA26)


  定位日志查看：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/N23R9Rs7TyaeoJputlqoNw/zh-cn_image_0000002658922941.png?HW-CC-KV=V1&HW-CC-Date=20260730T072728Z&HW-CC-Expire=86400&HW-CC-Sign=6A4EC03481CCCD1ABE0AF115A833F4B613B5D6D03744F0671B0031EF1C891A06)


  修复指南查看：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/MqY_im-qSw2GIGs0r0L_eA/zh-cn_image_0000002658802987.png?HW-CC-KV=V1&HW-CC-Date=20260730T072728Z&HW-CC-Expire=86400&HW-CC-Sign=DDD70C8552E4DA8DB388F77A4E619F1113DCA63555C194D6641BD304D2562EB2)
