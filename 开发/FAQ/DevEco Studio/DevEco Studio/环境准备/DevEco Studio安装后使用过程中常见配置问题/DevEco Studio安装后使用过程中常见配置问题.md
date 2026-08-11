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
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/PXo9XAX9ROOLWerFY06Rkw/zh-cn_image_0000002658804709.png?HW-CC-KV=V1&HW-CC-Date=20260811T005522Z&HW-CC-Expire=86400&HW-CC-Sign=B2A9042DFE323C0923F954D7FD119D6E15C8A8FDA186C410FD0372146C8F71C1)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/xLscucKNSN6uQxEc6mbtzQ/zh-cn_image_0000002628565342.png?HW-CC-KV=V1&HW-CC-Date=20260811T005522Z&HW-CC-Expire=86400&HW-CC-Sign=A373B749FFA1A1C9F2E037DF11F6028FC169047ADC6835F0C5381222381C7C0E)

- 检查是否开启了省电模式，取消省电模式：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/M3urnYnsT0mLladuwnyJMQ/zh-cn_image_0000002628405440.png?HW-CC-KV=V1&HW-CC-Date=20260811T005522Z&HW-CC-Expire=86400&HW-CC-Sign=76680B61CAFF1F456165E8222CF92DEB277627D04105E6D81A358E4D3159D315)

- 缓存问题，导致未正确索引该文件，清除缓存重新运行DevEco Studio：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/qtreozkWR3Sbtc_TRUnGsQ/zh-cn_image_0000002658924649.png?HW-CC-KV=V1&HW-CC-Date=20260811T005522Z&HW-CC-Expire=86400&HW-CC-Sign=6019DEEB9197497A5A0A5BA240F79A7153F59A8701CE299F16C8E9D238BB3819)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/Vo09bQ0WQNaxUfDXzZ7HHA/zh-cn_image_0000002658804711.png?HW-CC-KV=V1&HW-CC-Date=20260811T005522Z&HW-CC-Expire=86400&HW-CC-Sign=E823A1E3F4437398A93C5194A7CB0A97B2083E91299F90B9ED324D204D428CB5)


 
 

#### 问题二

- 在DevEco Studio->Settings->OpenHarmony SDK检查是否安装SDK。没有SDK的话可以点击对应版本进行更新或者下载：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/ZE_4jF7wRFST_eTUT2yr_g/zh-cn_image_0000002628565344.png?HW-CC-KV=V1&HW-CC-Date=20260811T005522Z&HW-CC-Expire=86400&HW-CC-Sign=B39DA2C864EA206AFE612652EEFEA2F9408317BF2815DEF2F0453DCB0895895D)

- 模拟器当前仅支持在中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）使用，确认开发者账号是否满足，通过右上角图标登录或更换账号：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/uC_qY6sbTbqibtRLi53thQ/zh-cn_image_0000002628405442.png?HW-CC-KV=V1&HW-CC-Date=20260811T005522Z&HW-CC-Expire=86400&HW-CC-Sign=236E525739872EB33EE46B8836BCB5F72270FDBC201662BC1AA395EFD4C1324B)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/wYCgvnaRSfiuJVnMOjFo1A/zh-cn_image_0000002658924651.png?HW-CC-KV=V1&HW-CC-Date=20260811T005522Z&HW-CC-Expire=86400&HW-CC-Sign=542AF6D575043AF0B66B186881004F3563049629CA44B880E1DC09972C79E50B)

- 检查用户目录下国家码配置是否为CN。路径C:\Users\XXX\AppData\Roaming\Huawei\DevEcoStudio6.0\options\country.region.xml，手动修改为CN重启DevEco Studio：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/TfJQo0c0RFCbWXENYBcWyg/zh-cn_image_0000002658804713.png?HW-CC-KV=V1&HW-CC-Date=20260811T005522Z&HW-CC-Expire=86400&HW-CC-Sign=E64AF5197110A635B7D57D3975BAB8B583B53B78D7A6C32067B11F02EB3085F7)


 
 

#### 问题三

- 可以通过以下方案解决IDE高耗电:1. 开启IDE省电模式：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/iNprsR_OR7G_ZDwfjfKQkQ/zh-cn_image_0000002628565346.png?HW-CC-KV=V1&HW-CC-Date=20260811T005522Z&HW-CC-Expire=86400&HW-CC-Sign=DD244800B06D408C3C59561ECED87D7F2940ACAF05DBA321E866E02D0AB16340)


2. 禁用CodeGlance（缩略图）等非必需插件，减少图形渲染负担：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/zFF4ho5mSg26GE3YhwQz0g/zh-cn_image_0000002628405444.png?HW-CC-KV=V1&HW-CC-Date=20260811T005522Z&HW-CC-Expire=86400&HW-CC-Sign=C80D8D795AC00F4395848CAEF85819C6FD3D2CF02E037F9904ADA016D8441FFE)


3. 禁用GPU渲染:在idea.properties文件中添加sun.java2d.opengl=false，idea.properties位于DevEco Studio安装目录的bin目录下。

 
 

#### 问题四

- 关闭jcef的GPU渲染：1. 点击右上角的放大镜图标，搜索配置项：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/5oH_cm75TpucKmha9n_hlQ/zh-cn_image_0000002658924653.png?HW-CC-KV=V1&HW-CC-Date=20260811T005522Z&HW-CC-Expire=86400&HW-CC-Sign=08FFD8F888FC42C46B8CBE8819E30C0994B13814B8C0DF452504DE39BB9C4FD2)


2. 输入registry，点击下面的Registry...选项：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/PxnxyNbPT0GynFUY7ZdVKA/zh-cn_image_0000002658804715.png?HW-CC-KV=V1&HW-CC-Date=20260811T005522Z&HW-CC-Expire=86400&HW-CC-Sign=C2AC791F693884CB567CAC72DA0C0559DB66D824AC639B95CBA2A5ACE0B1EAFE)


3. 直接输入gpu进行查找，勾选ide.browser.jcef.gpu.disable这一项，重启IDE：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/jsvu0sQBRTCMnPpx9O_6iA/zh-cn_image_0000002628565348.png?HW-CC-KV=V1&HW-CC-Date=20260811T005522Z&HW-CC-Expire=86400&HW-CC-Sign=46B3CD6C3E9E6162B8C308766A8364B54748F1E1B8F033093A49C6A648E168A4)

- 可能是DevEco Studio权限不足导致，以管理员身份启动DevEco Studio：1. 在DevEco Studio安装目录的bin目录找到DevEco Studio的启动图标：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/obAj_N7QRCCXpQothlSWTw/zh-cn_image_0000002628405446.png?HW-CC-KV=V1&HW-CC-Date=20260811T005522Z&HW-CC-Expire=86400&HW-CC-Sign=BD4F69B8903804701D4032594D77BFA8A966733710A39C0A78C089AF31377B6B)


2. 选中启动图标右键->属性->兼容性->以管理员身份运行此程序->确定，启动DevEco Studio：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/_FJRlECTRvCfV8_enmOh5g/zh-cn_image_0000002658924655.png?HW-CC-KV=V1&HW-CC-Date=20260811T005522Z&HW-CC-Expire=86400&HW-CC-Sign=DA44CC22F704F55CC23713D53027529E795AF30980B44D6261E89FC8268D6FEA)

- jcef文件缺失导致：检查jbr/bin/server/jvm.dll及jbr/bin/chrome_elf.dll是否存在，jcef文件缺失，导致jcef进程无法拉起，如果不存在，则需要重新安装DevEco Studio：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/-GoDNaxAQNiJfP7yVsGiGQ/zh-cn_image_0000002658804717.png?HW-CC-KV=V1&HW-CC-Date=20260811T005522Z&HW-CC-Expire=86400&HW-CC-Sign=EF31F1C9612956D94DD0B43243B2151DECEF9DC68DB4D02D874C0F051AF92784)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/aB6JbO4ESKivclD4Plbt8w/zh-cn_image_0000002628565350.png?HW-CC-KV=V1&HW-CC-Date=20260811T005522Z&HW-CC-Expire=86400&HW-CC-Sign=46D82A0954C5B34949D9F14E54282ED9A1EA9EECFCCE9BE559F5ABC471925E1B)

- jcef沙箱环境与当前电脑环境冲突，导致jcef无法正常工作，关闭jcef沙盒功能：1. 点击右上角的放大镜图标，搜索配置项：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/Xnyn-0hEQ2ySG5Z2GRRQXQ/zh-cn_image_0000002628405448.png?HW-CC-KV=V1&HW-CC-Date=20260811T005522Z&HW-CC-Expire=86400&HW-CC-Sign=798B07FCB9D0133CD9A69862DA8A501CC5A371FA34AF6F1F5E00A73C3343D4DC)


2. 输入registry，点击下面的Registry...选项：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/LyEC69rlQiO2ZZveK4ob1Q/zh-cn_image_0000002658924673.png?HW-CC-KV=V1&HW-CC-Date=20260811T005522Z&HW-CC-Expire=86400&HW-CC-Sign=B3D37D860994C30A7E82F74BE11DB3840E93E25B0F173B6704627FF0ABE128AB)


3. 直接输入sandbox进行查找，取消勾选ide.browser.jcef.sandbox.enable这一项，重启IDE：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/Yjs2PlDRQVq-HhwOEEpArg/zh-cn_image_0000002658804735.png?HW-CC-KV=V1&HW-CC-Date=20260811T005522Z&HW-CC-Expire=86400&HW-CC-Sign=153CCA634166E4CCE7DD016FC0572A748C46F437B64FC721E5C5089403BAD8E0)
