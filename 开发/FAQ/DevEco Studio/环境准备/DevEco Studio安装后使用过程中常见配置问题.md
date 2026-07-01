# DevEco Studio安装后使用过程中常见配置问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-45

## DevEco Studio安装后使用过程中常见配置问题
 


##### 问题现象

问题一：当前代码不展示高亮，并且也不显示代码补全提示。
 
问题二：开发工具DevEco Studio安装后Tools下没有显示Device Manager选项，在设备预览下拉表中也没有Device Manager选项。
 
问题三：DevEco Studio开启后特别耗电，如何配置可以降低耗电。
 
问题四：使用DevEco Studio，新建工程、新建模块、Project Structure、Choose Process等页面显示空白。
 
 

##### 解决方案

 

##### [h2]问题一

- 检查是否误操作关闭了该文件的语法检查，将OFF修改为All Problems查看代码是否恢复高亮，若未恢复高亮，则重启DevEco Studio重试：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/PXo9XAX9ROOLWerFY06Rkw/zh-cn_image_0000002658804709.png?HW-CC-KV=V1&HW-CC-Date=20260701T025911Z&HW-CC-Expire=86400&HW-CC-Sign=C60B1BB8A2FED5C9E4E884472BD6EF1913AE4F01F9614BBD13FD4E84CA3CCC07)

 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/xLscucKNSN6uQxEc6mbtzQ/zh-cn_image_0000002628565342.png?HW-CC-KV=V1&HW-CC-Date=20260701T025911Z&HW-CC-Expire=86400&HW-CC-Sign=4CB823419446709BFD47BE7E1478267E821D5D94CDF82A6CB08D9BB9F602D73F)

- 检查是否开启了省电模式，取消省电模式：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/M3urnYnsT0mLladuwnyJMQ/zh-cn_image_0000002628405440.png?HW-CC-KV=V1&HW-CC-Date=20260701T025911Z&HW-CC-Expire=86400&HW-CC-Sign=B912EAD46B001613EAF279C6DB2644F69B47DCA5287BBE2692546DE5CD56AD5F)

- 缓存问题，导致未正确索引该文件，清除缓存重新运行DevEco Studio：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/qtreozkWR3Sbtc_TRUnGsQ/zh-cn_image_0000002658924649.png?HW-CC-KV=V1&HW-CC-Date=20260701T025911Z&HW-CC-Expire=86400&HW-CC-Sign=7F35A0B4C69FBC7EF0BBFF0E10E82292ACF650119B9330BEA02495365CB18C55)

 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/Vo09bQ0WQNaxUfDXzZ7HHA/zh-cn_image_0000002658804711.png?HW-CC-KV=V1&HW-CC-Date=20260701T025911Z&HW-CC-Expire=86400&HW-CC-Sign=889428298DD578FDF9F9CB745D7BF6162D8953E54E0BFB4039607D42A518F4B8)


 
 

##### [h2]问题二

- 在DevEco Studio->Settings->OpenHarmony SDK检查是否安装SDK。没有SDK的话可以点击对应版本进行更新或者下载：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/ZE_4jF7wRFST_eTUT2yr_g/zh-cn_image_0000002628565344.png?HW-CC-KV=V1&HW-CC-Date=20260701T025911Z&HW-CC-Expire=86400&HW-CC-Sign=C47687031F852794FCAA34F775EBCE2061FE1331B23BDD4A543929532DB79647)

- 模拟器当前仅支持在中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）使用，确认开发者账号是否满足，通过右上角图标登录或更换账号：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/uC_qY6sbTbqibtRLi53thQ/zh-cn_image_0000002628405442.png?HW-CC-KV=V1&HW-CC-Date=20260701T025911Z&HW-CC-Expire=86400&HW-CC-Sign=90EE647C8C512D6C0686145C84525C20CD8001CCCF1EF82B7AD36EB9EA1CB5EA)

 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/wYCgvnaRSfiuJVnMOjFo1A/zh-cn_image_0000002658924651.png?HW-CC-KV=V1&HW-CC-Date=20260701T025911Z&HW-CC-Expire=86400&HW-CC-Sign=506191E7540CC5856024BD5C9DA6EF3251DE9D492A135829CABBF1130D18933E)

- 检查用户目录下国家码配置是否为CN。路径C:\Users\XXX\AppData\Roaming\Huawei\DevEcoStudio6.0\options\country.region.xml，手动修改为CN重启DevEco Studio：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/TfJQo0c0RFCbWXENYBcWyg/zh-cn_image_0000002658804713.png?HW-CC-KV=V1&HW-CC-Date=20260701T025911Z&HW-CC-Expire=86400&HW-CC-Sign=5DB0724586FC39A97A07B7FEC264C20F1EC73E0B4BA2A9B2D0C7B3626430D6FD)


 
 

##### [h2]问题三

- 可以通过以下方案解决IDE高耗电:
开启IDE省电模式：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/iNprsR_OR7G_ZDwfjfKQkQ/zh-cn_image_0000002628565346.png?HW-CC-KV=V1&HW-CC-Date=20260701T025911Z&HW-CC-Expire=86400&HW-CC-Sign=71A3F37159BB5C011AD58B3DAE74F33AE96835F2D9B42113A01988EE4F7470CB)

- 禁用CodeGlance（缩略图）等非必需插件，减少图形渲染负担：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/zFF4ho5mSg26GE3YhwQz0g/zh-cn_image_0000002628405444.png?HW-CC-KV=V1&HW-CC-Date=20260701T025911Z&HW-CC-Expire=86400&HW-CC-Sign=4E247BD802DCC68D2E9E5235AB548DF727FE25295594726D68C402FDB0171942)

- 禁用GPU渲染:在idea.properties文件中添加sun.java2d.opengl=false，idea.properties位于DevEco Studio安装目录的bin目录下。

 
 
 

##### [h2]问题四

- 关闭jcef的GPU渲染：
点击右上角的放大镜图标，搜索配置项：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/5oH_cm75TpucKmha9n_hlQ/zh-cn_image_0000002658924653.png?HW-CC-KV=V1&HW-CC-Date=20260701T025911Z&HW-CC-Expire=86400&HW-CC-Sign=A1F1982A1624FD5C9527A536137890008E03B77EB4511EBEE9BA1EEC58DC136F)

- 输入registry，点击下面的Registry...选项：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/PxnxyNbPT0GynFUY7ZdVKA/zh-cn_image_0000002658804715.png?HW-CC-KV=V1&HW-CC-Date=20260701T025911Z&HW-CC-Expire=86400&HW-CC-Sign=F742424B704CADBEF8B16BBE0834E57B44C8C07429C3619DB8510212A1CF8C62)

- 直接输入gpu进行查找，勾选ide.browser.jcef.gpu.disable这一项，重启IDE：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/jsvu0sQBRTCMnPpx9O_6iA/zh-cn_image_0000002628565348.png?HW-CC-KV=V1&HW-CC-Date=20260701T025911Z&HW-CC-Expire=86400&HW-CC-Sign=C3D2827DF6B8CCECCC28B3BD0FE8ED4734F00B4341495AF78ADF16C3181E1C55)


 - 可能是DevEco Studio权限不足导致，以管理员身份启动DevEco Studio：
在DevEco Studio安装目录的bin目录找到DevEco Studio的启动图标：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/obAj_N7QRCCXpQothlSWTw/zh-cn_image_0000002628405446.png?HW-CC-KV=V1&HW-CC-Date=20260701T025911Z&HW-CC-Expire=86400&HW-CC-Sign=ADBE68101633D6E5AD55DB72E8FE31A36760CC82EB874B0719D767CDDAAF66F8)

- 选中启动图标右键->属性->兼容性->以管理员身份运行此程序->确定，启动DevEco Studio：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/_FJRlECTRvCfV8_enmOh5g/zh-cn_image_0000002658924655.png?HW-CC-KV=V1&HW-CC-Date=20260701T025911Z&HW-CC-Expire=86400&HW-CC-Sign=A3722B0830B9C66DB15D74053AEC11DE56BE9D6ACE45323B7B8E6BDD413A226B)


 - jcef文件缺失导致：检查jbr/bin/server/jvm.dll及jbr/bin/chrome_elf.dll是否存在，jcef文件缺失，导致jcef进程无法拉起，如果不存在，则需要重新安装DevEco Studio：
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/-GoDNaxAQNiJfP7yVsGiGQ/zh-cn_image_0000002658804717.png?HW-CC-KV=V1&HW-CC-Date=20260701T025911Z&HW-CC-Expire=86400&HW-CC-Sign=850B6BE9C59C2A5EFAE10C495432CC6438DD2902A7D4C4C56D2BDF6D8FBF0378)

 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/aB6JbO4ESKivclD4Plbt8w/zh-cn_image_0000002628565350.png?HW-CC-KV=V1&HW-CC-Date=20260701T025911Z&HW-CC-Expire=86400&HW-CC-Sign=55F6168E068A2709661DC3B3603E3BE07835631F420439B289740EB59DF92BCC)

- jcef沙箱环境与当前电脑环境冲突，导致jcef无法正常工作，关闭jcef沙盒功能：
点击右上角的放大镜图标，搜索配置项：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/Xnyn-0hEQ2ySG5Z2GRRQXQ/zh-cn_image_0000002628405448.png?HW-CC-KV=V1&HW-CC-Date=20260701T025911Z&HW-CC-Expire=86400&HW-CC-Sign=573D39504A45A3D4484877A74C611CB8CF3EB3D94908A9E1EAE36D26964A114C)

- 输入registry，点击下面的Registry...选项：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/LyEC69rlQiO2ZZveK4ob1Q/zh-cn_image_0000002658924673.png?HW-CC-KV=V1&HW-CC-Date=20260701T025911Z&HW-CC-Expire=86400&HW-CC-Sign=B5212B77402C06FFFC365E06EB52FD0FE518B648D6AFBDAFDFB18113D63397F9)

- 直接输入sandbox进行查找，取消勾选ide.browser.jcef.sandbox.enable这一项，重启IDE：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/Yjs2PlDRQVq-HhwOEEpArg/zh-cn_image_0000002658804735.png?HW-CC-KV=V1&HW-CC-Date=20260701T025911Z&HW-CC-Expire=86400&HW-CC-Sign=91C43FD93B165594DEA4CAAF96560BE41A044D270FB5898BB7B1FBC55C97C1C2)
