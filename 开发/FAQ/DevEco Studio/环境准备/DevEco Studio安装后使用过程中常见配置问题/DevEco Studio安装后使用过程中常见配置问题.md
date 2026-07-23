# DevEco Studio安装后使用过程中常见配置问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-45

#### 问题现象

问题一：当前代码不展示高亮，并且也不显示代码补全提示。
 
问题二：开发工具DevEco Studio安装后Tools下没有显示Device Manager选项，在设备预览下拉表中也没有Device Manager选项。
 
问题三：DevEco Studio开启后特别耗电，如何配置可以降低耗电。
 
问题四：使用DevEco Studio，新建工程、新建模块、Project Structure、Choose Process等页面显示空白。
 
 

#### 解决方案

 

#### 问题一

- 检查是否误操作关闭了该文件的语法检查，将OFF修改为All Problems查看代码是否恢复高亮，若未恢复高亮，则重启DevEco Studio重试：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/PXo9XAX9ROOLWerFY06Rkw/zh-cn_image_0000002658804709.png?HW-CC-KV=V1&HW-CC-Date=20260723T013909Z&HW-CC-Expire=86400&HW-CC-Sign=F01FE2D0176728660E1D669655B70BF87CC675B4F57AC9C908E0D26D0F162096)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/xLscucKNSN6uQxEc6mbtzQ/zh-cn_image_0000002628565342.png?HW-CC-KV=V1&HW-CC-Date=20260723T013909Z&HW-CC-Expire=86400&HW-CC-Sign=E681B113BD20305352094D75091060BDEA1E9E094BB4890B9B1C96E4AD13E753)

- 检查是否开启了省电模式，取消省电模式：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/M3urnYnsT0mLladuwnyJMQ/zh-cn_image_0000002628405440.png?HW-CC-KV=V1&HW-CC-Date=20260723T013909Z&HW-CC-Expire=86400&HW-CC-Sign=9CA8FCAEAC09700405285C85298D1B9E08D9A6370F9B8090FE01E4A4BA608261)

- 缓存问题，导致未正确索引该文件，清除缓存重新运行DevEco Studio：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/qtreozkWR3Sbtc_TRUnGsQ/zh-cn_image_0000002658924649.png?HW-CC-KV=V1&HW-CC-Date=20260723T013909Z&HW-CC-Expire=86400&HW-CC-Sign=A897D5FB4858DE6DCCA9F7DDDE15BFF759E964D9E3E3BBB60EF31474233B590E)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/Vo09bQ0WQNaxUfDXzZ7HHA/zh-cn_image_0000002658804711.png?HW-CC-KV=V1&HW-CC-Date=20260723T013909Z&HW-CC-Expire=86400&HW-CC-Sign=88B4D038F1ADDFD0B7CBB711A479CEC4B3C705A40214E41B2910BCF1DD2F537C)


 
 

#### 问题二

- 在DevEco Studio->Settings->OpenHarmony SDK检查是否安装SDK。没有SDK的话可以点击对应版本进行更新或者下载：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/ZE_4jF7wRFST_eTUT2yr_g/zh-cn_image_0000002628565344.png?HW-CC-KV=V1&HW-CC-Date=20260723T013909Z&HW-CC-Expire=86400&HW-CC-Sign=7B39BE509CADE77B34E986F00CAB3BA04C981221BA6B209D13F87F08C385C5C9)

- 模拟器当前仅支持在中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）使用，确认开发者账号是否满足，通过右上角图标登录或更换账号：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/uC_qY6sbTbqibtRLi53thQ/zh-cn_image_0000002628405442.png?HW-CC-KV=V1&HW-CC-Date=20260723T013909Z&HW-CC-Expire=86400&HW-CC-Sign=FDE682261EAA139A85B6DECB90354131061FEA9F5D830B64A13FA735C3F7DC0E)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/wYCgvnaRSfiuJVnMOjFo1A/zh-cn_image_0000002658924651.png?HW-CC-KV=V1&HW-CC-Date=20260723T013909Z&HW-CC-Expire=86400&HW-CC-Sign=C70E640CB6C9AEF30D2047BB73BC9CBA2AC3F5795726F36D7733966DCF51AD31)

- 检查用户目录下国家码配置是否为CN。路径C:\Users\XXX\AppData\Roaming\Huawei\DevEcoStudio6.0\options\country.region.xml，手动修改为CN重启DevEco Studio：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/TfJQo0c0RFCbWXENYBcWyg/zh-cn_image_0000002658804713.png?HW-CC-KV=V1&HW-CC-Date=20260723T013909Z&HW-CC-Expire=86400&HW-CC-Sign=2C63AB060058475894EAB672C14A240DE1562B81ECDC5C65EDA3408853F8CDD2)


 
 

#### 问题三

- 可以通过以下方案解决IDE高耗电:1. 开启IDE省电模式：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/iNprsR_OR7G_ZDwfjfKQkQ/zh-cn_image_0000002628565346.png?HW-CC-KV=V1&HW-CC-Date=20260723T013909Z&HW-CC-Expire=86400&HW-CC-Sign=5F88265A809FA2D4E834E32E20F6A6A28C83CF9C08B1E44D0B15E1791C60469A)


2. 禁用CodeGlance（缩略图）等非必需插件，减少图形渲染负担：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/zFF4ho5mSg26GE3YhwQz0g/zh-cn_image_0000002628405444.png?HW-CC-KV=V1&HW-CC-Date=20260723T013909Z&HW-CC-Expire=86400&HW-CC-Sign=FBE7C8F6F12A5DBF7BC53E6D673CB29ED80766135861C48508568E959DAD6DDD)


3. 禁用GPU渲染:在idea.properties文件中添加sun.java2d.opengl=false，idea.properties位于DevEco Studio安装目录的bin目录下。

 
 

#### 问题四

- 关闭jcef的GPU渲染：1. 点击右上角的放大镜图标，搜索配置项：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/5oH_cm75TpucKmha9n_hlQ/zh-cn_image_0000002658924653.png?HW-CC-KV=V1&HW-CC-Date=20260723T013909Z&HW-CC-Expire=86400&HW-CC-Sign=B02126ADDAA0CB1F72C1E3D25A4ED2024D232D33EA5DB8D1AC91E59684CAB6CA)


2. 输入registry，点击下面的Registry...选项：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/PxnxyNbPT0GynFUY7ZdVKA/zh-cn_image_0000002658804715.png?HW-CC-KV=V1&HW-CC-Date=20260723T013909Z&HW-CC-Expire=86400&HW-CC-Sign=57B263C641B5E00F3C3F97860BC218C38FE4A491C1420F9D40356F6A8273E452)


3. 直接输入gpu进行查找，勾选ide.browser.jcef.gpu.disable这一项，重启IDE：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/jsvu0sQBRTCMnPpx9O_6iA/zh-cn_image_0000002628565348.png?HW-CC-KV=V1&HW-CC-Date=20260723T013909Z&HW-CC-Expire=86400&HW-CC-Sign=5C61851A411AC0761ABE0A0124C7BEDCB3C24959F46FE4AC1D1B7D7BC5059BF6)

- 可能是DevEco Studio权限不足导致，以管理员身份启动DevEco Studio：1. 在DevEco Studio安装目录的bin目录找到DevEco Studio的启动图标：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/obAj_N7QRCCXpQothlSWTw/zh-cn_image_0000002628405446.png?HW-CC-KV=V1&HW-CC-Date=20260723T013909Z&HW-CC-Expire=86400&HW-CC-Sign=5A39B4194A3D471E377A73A97F5F9D3C83FCA990ACF06321040DA29C9B6D7E34)


2. 选中启动图标右键->属性->兼容性->以管理员身份运行此程序->确定，启动DevEco Studio：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/_FJRlECTRvCfV8_enmOh5g/zh-cn_image_0000002658924655.png?HW-CC-KV=V1&HW-CC-Date=20260723T013909Z&HW-CC-Expire=86400&HW-CC-Sign=25F67F43FA8C4B82B007459D0771DBDD578EF129F13F00871604694EBDE9C707)

- jcef文件缺失导致：检查jbr/bin/server/jvm.dll及jbr/bin/chrome_elf.dll是否存在，jcef文件缺失，导致jcef进程无法拉起，如果不存在，则需要重新安装DevEco Studio：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/-GoDNaxAQNiJfP7yVsGiGQ/zh-cn_image_0000002658804717.png?HW-CC-KV=V1&HW-CC-Date=20260723T013909Z&HW-CC-Expire=86400&HW-CC-Sign=183650440CE175867818FBBAA7A9F4C7AADDDEF908DF8AAE450BAC934B383460)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/aB6JbO4ESKivclD4Plbt8w/zh-cn_image_0000002628565350.png?HW-CC-KV=V1&HW-CC-Date=20260723T013909Z&HW-CC-Expire=86400&HW-CC-Sign=CE0D460E355B4E95F2BA92694C16713DE37EA89F2647FD3DE3BF76E415901FD8)

- jcef沙箱环境与当前电脑环境冲突，导致jcef无法正常工作，关闭jcef沙盒功能：1. 点击右上角的放大镜图标，搜索配置项：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/Xnyn-0hEQ2ySG5Z2GRRQXQ/zh-cn_image_0000002628405448.png?HW-CC-KV=V1&HW-CC-Date=20260723T013909Z&HW-CC-Expire=86400&HW-CC-Sign=E5023D40E43E9AF2E9F7DDA6121B11A35EE26D2F6DF1F49DF45EF7D591392C15)


2. 输入registry，点击下面的Registry...选项：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/LyEC69rlQiO2ZZveK4ob1Q/zh-cn_image_0000002658924673.png?HW-CC-KV=V1&HW-CC-Date=20260723T013909Z&HW-CC-Expire=86400&HW-CC-Sign=2F9E4F5C1AF249007831F2722AB09B909F0D98A4C1828C0B55782B9B77DB444D)


3. 直接输入sandbox进行查找，取消勾选ide.browser.jcef.sandbox.enable这一项，重启IDE：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/Yjs2PlDRQVq-HhwOEEpArg/zh-cn_image_0000002658804735.png?HW-CC-KV=V1&HW-CC-Date=20260723T013909Z&HW-CC-Expire=86400&HW-CC-Sign=DA60345AABCE912A0AF5048CA9C22B5DBF3E23A7B49FCB8953F5AFC546347456)
