# 如何定位UX测试结果不通过问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ux-basic-quality-test-1

#### 问题现象

- 问题一：使用DevEco Testing执行UX测试结果显示“条件依赖”，报“arklayout文件存储失败”或“arklayout文件依赖调试版本应用”：测试结果：条件依赖。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/piqsw--uQESH8Spwud5Rew/zh-cn_image_0000002628563632.png?HW-CC-KV=V1&HW-CC-Date=20260723T014024Z&HW-CC-Expire=86400&HW-CC-Sign=A68FB029E9B81E9167C5C1DEB177DD5179A8F3424A15246E8A3E9AFC9618256C)


  原因说明：arklayout文件存储失败。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/i4bTzWqRQr-tHPDuj9aubw/zh-cn_image_0000002658922937.png?HW-CC-KV=V1&HW-CC-Date=20260723T014024Z&HW-CC-Expire=86400&HW-CC-Sign=FF3E76E6BE5232486F4D56AE4C23AE9CDD0F924B3F127E5982AFF5CE3135956B)


  原因说明：arklayout文件依赖调试版本应用。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/3QEjao7FSq6yTJ8V9w0j1Q/zh-cn_image_0000002658802983.png?HW-CC-KV=V1&HW-CC-Date=20260723T014024Z&HW-CC-Expire=86400&HW-CC-Sign=A1AB63332F10C18CF0864F5ED199FACCE902FF320468BA434A59FFD8BB154356)

- 问题二：UX检测结果显示“条件依赖”，报“应用包不存在”是什么原因？原因显示说明：应用包不存在。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/2OIanelbQgKa0bohLaIi4w/zh-cn_image_0000002628403724.png?HW-CC-KV=V1&HW-CC-Date=20260723T014024Z&HW-CC-Expire=86400&HW-CC-Sign=0679F4FBB67AFC56A44F8BD2229E1DA600DC0D506D48990C1B63D2E0D0558E85)

- 问题三：UX检测结果显示“元服务胶囊热区冲突”不通过，导航栏过宽该如何解决？
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/41YfuJdRS427M9x5s6v4rQ/zh-cn_image_0000002628563634.png?HW-CC-KV=V1&HW-CC-Date=20260723T014024Z&HW-CC-Expire=86400&HW-CC-Sign=AF8FF75F7BCF26AA083DFAF8D88B3DCB37956CCC50CF28787DD0821FC9BE44EC)

- 问题四：UX检测结果显示“不涉及”该如何处理？
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/J2Ws_FaaQliPl4tMzMn9Aw/zh-cn_image_0000002658922939.png?HW-CC-KV=V1&HW-CC-Date=20260723T014024Z&HW-CC-Expire=86400&HW-CC-Sign=283436DC164378CC0B3B185E8FCD1C822575D89841E2B07B98BD101CDF96019B)

- 问题五：UX检测结果显示“不通过”，如何定位和修复？
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/YGEb3aTTTRGzAgaG_tkbmQ/zh-cn_image_0000002658802985.png?HW-CC-KV=V1&HW-CC-Date=20260723T014024Z&HW-CC-Expire=86400&HW-CC-Sign=4763946770C564D4DC73D5EA5DA012AB4B9543BC42AD7C6107EEB246FEDEBB6A)


 
 

#### 解决方案

- 问题一解决方案：UX检测时部分规则依赖debug版本应用进行测试，请安装应用的debug签名版本重启手机后重新测试。
- 问题二解决方案：UX检测时部分规则依赖应用包完成，如果手机上已安装了应用，UX测试的部分结果会提示应用包不存在，请通过DevEco Testing进行应用的安装和测试。
- 问题三解决方案：应用UX体验建议中关于热区的标准可参考[适用范围](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/experience-suggestions-ux#section1541617350183)中“点击热区”，使用[AtomicServiceNavigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-atomicservice-atomicservicenavigation#atomicservicenavigation-1)设置导航栏的宽度。
- 问题四解决方案：检测结果为不涉及代表测试用例的执行条件不满足，不会执行相关的测试场景，可以点击不涉及前面的“查看”进行详细查看。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/ZPLtJzYYR8iisPoM7ryxvA/zh-cn_image_0000002628403726.png?HW-CC-KV=V1&HW-CC-Date=20260723T014024Z&HW-CC-Expire=86400&HW-CC-Sign=42C80F9704FA1FE780FCA73FF44DB29C163459A6901F3739DA2665A5E2DD0953)

- 问题五解决方案：举例“典型手势时长设计”测试不通过，点击对应的“不通过数”->查看定位日志和修复指南。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/yzqhQ_iaRLyQDvKtCmppwQ/zh-cn_image_0000002628563636.png?HW-CC-KV=V1&HW-CC-Date=20260723T014024Z&HW-CC-Expire=86400&HW-CC-Sign=F6D18E7960D04EED7DD61A743C31B1A42A306A2A36E6170EBACAEEB621A99ECC)


  定位日志查看：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/N23R9Rs7TyaeoJputlqoNw/zh-cn_image_0000002658922941.png?HW-CC-KV=V1&HW-CC-Date=20260723T014024Z&HW-CC-Expire=86400&HW-CC-Sign=B8858D514B21079005BCD44841AA440483A05408B6A2C527283FA518EE514DC9)


  修复指南查看：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/MqY_im-qSw2GIGs0r0L_eA/zh-cn_image_0000002658802987.png?HW-CC-KV=V1&HW-CC-Date=20260723T014024Z&HW-CC-Expire=86400&HW-CC-Sign=577D08B4D5D3F13EA8B51E85284CF28C2868FDC51136A3BC111371F6FEC9DB95)
