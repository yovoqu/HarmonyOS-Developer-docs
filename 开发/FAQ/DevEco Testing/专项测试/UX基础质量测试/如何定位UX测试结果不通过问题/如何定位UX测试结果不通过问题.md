# 如何定位UX测试结果不通过问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ux-basic-quality-test-1

#### 问题现象

- 问题一：使用DevEco Testing执行UX测试结果显示“条件依赖”，报“arklayout文件存储失败”或“arklayout文件依赖调试版本应用”：测试结果：条件依赖。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/piqsw--uQESH8Spwud5Rew/zh-cn_image_0000002628563632.png?HW-CC-KV=V1&HW-CC-Date=20260811T005529Z&HW-CC-Expire=86400&HW-CC-Sign=3411BA3024C4CD5A3E440B55E3746D0749DA1F3B3F62D7E642DE000F65893C01)


  原因说明：arklayout文件存储失败。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/i4bTzWqRQr-tHPDuj9aubw/zh-cn_image_0000002658922937.png?HW-CC-KV=V1&HW-CC-Date=20260811T005529Z&HW-CC-Expire=86400&HW-CC-Sign=4665D466B681CCE6387C692AEFEE1A3A07D14D3E7D710EF54F231580B9442F72)


  原因说明：arklayout文件依赖调试版本应用。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/3QEjao7FSq6yTJ8V9w0j1Q/zh-cn_image_0000002658802983.png?HW-CC-KV=V1&HW-CC-Date=20260811T005529Z&HW-CC-Expire=86400&HW-CC-Sign=3F615019B47AFAF054422B6E05473CF593730219FF4105DE66FA542C330FE0FE)

- 问题二：UX检测结果显示“条件依赖”，报“应用包不存在”是什么原因？原因显示说明：应用包不存在。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/2OIanelbQgKa0bohLaIi4w/zh-cn_image_0000002628403724.png?HW-CC-KV=V1&HW-CC-Date=20260811T005529Z&HW-CC-Expire=86400&HW-CC-Sign=D7CE960FEA44B2D9B54B16DFCCF944A0492080BACE876D5737EB7F212A9B4D39)

- 问题三：UX检测结果显示“元服务胶囊热区冲突”不通过，导航栏过宽该如何解决？
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/41YfuJdRS427M9x5s6v4rQ/zh-cn_image_0000002628563634.png?HW-CC-KV=V1&HW-CC-Date=20260811T005529Z&HW-CC-Expire=86400&HW-CC-Sign=5B4411228E19B80B85DEC8C3D805B3C2F3FFB8A678707F155B21491DA905458C)

- 问题四：UX检测结果显示“不涉及”该如何处理？
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/J2Ws_FaaQliPl4tMzMn9Aw/zh-cn_image_0000002658922939.png?HW-CC-KV=V1&HW-CC-Date=20260811T005529Z&HW-CC-Expire=86400&HW-CC-Sign=A3EC57D0EA2DDDDD35FE8E8D83B14F3A8EB6032788E78B8FFD3544F7A942A16C)

- 问题五：UX检测结果显示“不通过”，如何定位和修复？
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/YGEb3aTTTRGzAgaG_tkbmQ/zh-cn_image_0000002658802985.png?HW-CC-KV=V1&HW-CC-Date=20260811T005529Z&HW-CC-Expire=86400&HW-CC-Sign=F9F5222CD80CE3D1680D4D686412E62D01C3B84A78A9889A3BCDE2424722FD58)


 
 

#### 解决方案

- 问题一解决方案：UX检测时部分规则依赖debug版本应用进行测试，请安装应用的debug签名版本重启手机后重新测试。
- 问题二解决方案：UX检测时部分规则依赖应用包完成，如果手机上已安装了应用，UX测试的部分结果会提示应用包不存在，请通过DevEco Testing进行应用的安装和测试。
- 问题三解决方案：应用UX体验建议中关于热区的标准可参考[适用范围](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/experience-suggestions-ux#section1541617350183)中“点击热区”，使用[AtomicServiceNavigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-atomicservice-atomicservicenavigation#atomicservicenavigation-1)设置导航栏的宽度。
- 问题四解决方案：检测结果为不涉及代表测试用例的执行条件不满足，不会执行相关的测试场景，可以点击不涉及前面的“查看”进行详细查看。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/ZPLtJzYYR8iisPoM7ryxvA/zh-cn_image_0000002628403726.png?HW-CC-KV=V1&HW-CC-Date=20260811T005529Z&HW-CC-Expire=86400&HW-CC-Sign=EA7B432D876D7EB39C166BB0B28EC645D900DD20AE0A8221F3D36A30CC3D4C47)

- 问题五解决方案：举例“典型手势时长设计”测试不通过，点击对应的“不通过数”->查看定位日志和修复指南。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/yzqhQ_iaRLyQDvKtCmppwQ/zh-cn_image_0000002628563636.png?HW-CC-KV=V1&HW-CC-Date=20260811T005529Z&HW-CC-Expire=86400&HW-CC-Sign=D40B3445284968B6D02C766248514D4067EC12D3AC915876739424AF5B479DD1)


  定位日志查看：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/N23R9Rs7TyaeoJputlqoNw/zh-cn_image_0000002658922941.png?HW-CC-KV=V1&HW-CC-Date=20260811T005529Z&HW-CC-Expire=86400&HW-CC-Sign=24D0538909047AB8DE9F0770AE243ED40C59E7955A78B22B12FA7E7E1A1E9A53)


  修复指南查看：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/MqY_im-qSw2GIGs0r0L_eA/zh-cn_image_0000002658802987.png?HW-CC-KV=V1&HW-CC-Date=20260811T005529Z&HW-CC-Expire=86400&HW-CC-Sign=791B9EEBE7B652203B5D2AB1794291C8F8A4E6ADC860F9BE39BC015B63650703)
