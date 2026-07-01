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
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/PXo9XAX9ROOLWerFY06Rkw/zh-cn_image_0000002658804709.png?HW-CC-KV=V1&HW-CC-Date=20260701T041016Z&HW-CC-Expire=86400&HW-CC-Sign=F81A2472CEA70C795A17154A56D0FF11334BDD6768D1294E6CE5672D7B9C5F9D)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/xLscucKNSN6uQxEc6mbtzQ/zh-cn_image_0000002628565342.png?HW-CC-KV=V1&HW-CC-Date=20260701T041016Z&HW-CC-Expire=86400&HW-CC-Sign=2F52F15BE538597226EAF9E4FF91B0F9044D5FE81634241D6890D5DD389C6CEA)

- 检查是否开启了省电模式，取消省电模式：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/M3urnYnsT0mLladuwnyJMQ/zh-cn_image_0000002628405440.png?HW-CC-KV=V1&HW-CC-Date=20260701T041016Z&HW-CC-Expire=86400&HW-CC-Sign=A85054B01D7B31C80A5593D291A5A1B630E4F444D3C6AE565913D92AFF2B1A1C)

- 缓存问题，导致未正确索引该文件，清除缓存重新运行DevEco Studio：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/qtreozkWR3Sbtc_TRUnGsQ/zh-cn_image_0000002658924649.png?HW-CC-KV=V1&HW-CC-Date=20260701T041016Z&HW-CC-Expire=86400&HW-CC-Sign=D4BA19AB6E71B135F7EA46974D8CB2D4909C374BCE48294119730E37B1DE1C93)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/Vo09bQ0WQNaxUfDXzZ7HHA/zh-cn_image_0000002658804711.png?HW-CC-KV=V1&HW-CC-Date=20260701T041016Z&HW-CC-Expire=86400&HW-CC-Sign=181CF92D9008E52C02280EA381219A113B65C8459C3A1E8E96080C2549420DC6)


 
 

#### 问题二

- 在DevEco Studio->Settings->OpenHarmony SDK检查是否安装SDK。没有SDK的话可以点击对应版本进行更新或者下载：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/ZE_4jF7wRFST_eTUT2yr_g/zh-cn_image_0000002628565344.png?HW-CC-KV=V1&HW-CC-Date=20260701T041016Z&HW-CC-Expire=86400&HW-CC-Sign=A26F316191DDD6844E22634B92ADB8F5894A1F396461308466BC4DBBCCA90AA1)

- 模拟器当前仅支持在中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）使用，确认开发者账号是否满足，通过右上角图标登录或更换账号：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/uC_qY6sbTbqibtRLi53thQ/zh-cn_image_0000002628405442.png?HW-CC-KV=V1&HW-CC-Date=20260701T041016Z&HW-CC-Expire=86400&HW-CC-Sign=6A5615717CFE441075672157A445E7DB76FDE7445773C325EAF7019C6ACE25E0)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/wYCgvnaRSfiuJVnMOjFo1A/zh-cn_image_0000002658924651.png?HW-CC-KV=V1&HW-CC-Date=20260701T041016Z&HW-CC-Expire=86400&HW-CC-Sign=3E114575B9498CB4E1A414FDD9EF2B85C15A01C364D367271E0EB641FB9BEE75)

- 检查用户目录下国家码配置是否为CN。路径C:\Users\XXX\AppData\Roaming\Huawei\DevEcoStudio6.0\options\country.region.xml，手动修改为CN重启DevEco Studio：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/TfJQo0c0RFCbWXENYBcWyg/zh-cn_image_0000002658804713.png?HW-CC-KV=V1&HW-CC-Date=20260701T041016Z&HW-CC-Expire=86400&HW-CC-Sign=7AD3AFB6223F87DD7F2CEB939FB4677B7BD6DE9C029ABE5790F761FB849B8559)


 
 

#### 问题三

- 可以通过以下方案解决IDE高耗电:1. 开启IDE省电模式：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/iNprsR_OR7G_ZDwfjfKQkQ/zh-cn_image_0000002628565346.png?HW-CC-KV=V1&HW-CC-Date=20260701T041016Z&HW-CC-Expire=86400&HW-CC-Sign=0ACF1E5D36B87D8AA21EE4689B9E710C114B0C66CC771992BF84F94F9BFEDDFA)


2. 禁用CodeGlance（缩略图）等非必需插件，减少图形渲染负担：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/zFF4ho5mSg26GE3YhwQz0g/zh-cn_image_0000002628405444.png?HW-CC-KV=V1&HW-CC-Date=20260701T041016Z&HW-CC-Expire=86400&HW-CC-Sign=A9A22E95092E5432D4141A55CB2F37EA50FBE2ABE39BF6A58ABFD49BC041BBCA)


3. 禁用GPU渲染:在idea.properties文件中添加sun.java2d.opengl=false，idea.properties位于DevEco Studio安装目录的bin目录下。

 
 

#### 问题四

- 关闭jcef的GPU渲染：1. 点击右上角的放大镜图标，搜索配置项：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/5oH_cm75TpucKmha9n_hlQ/zh-cn_image_0000002658924653.png?HW-CC-KV=V1&HW-CC-Date=20260701T041016Z&HW-CC-Expire=86400&HW-CC-Sign=A0977E1FDD1679C9C22F5A26FDC8FC6A602222708E78556A85CF19B662BB9E59)


2. 输入registry，点击下面的Registry...选项：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/PxnxyNbPT0GynFUY7ZdVKA/zh-cn_image_0000002658804715.png?HW-CC-KV=V1&HW-CC-Date=20260701T041016Z&HW-CC-Expire=86400&HW-CC-Sign=35CB9259128AE75C731A11305C63DAD5B836EAC7977E02B44FE206854AA1682F)


3. 直接输入gpu进行查找，勾选ide.browser.jcef.gpu.disable这一项，重启IDE：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/jsvu0sQBRTCMnPpx9O_6iA/zh-cn_image_0000002628565348.png?HW-CC-KV=V1&HW-CC-Date=20260701T041016Z&HW-CC-Expire=86400&HW-CC-Sign=5120DCCBDBBE23565C3DB6EFB88F3BBF0D6F7BD8F0BABBBEEAB176B59E7D35C5)

- 可能是DevEco Studio权限不足导致，以管理员身份启动DevEco Studio：1. 在DevEco Studio安装目录的bin目录找到DevEco Studio的启动图标：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/obAj_N7QRCCXpQothlSWTw/zh-cn_image_0000002628405446.png?HW-CC-KV=V1&HW-CC-Date=20260701T041016Z&HW-CC-Expire=86400&HW-CC-Sign=2E20A3C0CBAA60238856F3E053C4BE941AF58338106E844771197F61142D12C6)


2. 选中启动图标右键->属性->兼容性->以管理员身份运行此程序->确定，启动DevEco Studio：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/_FJRlECTRvCfV8_enmOh5g/zh-cn_image_0000002658924655.png?HW-CC-KV=V1&HW-CC-Date=20260701T041016Z&HW-CC-Expire=86400&HW-CC-Sign=DF2B0841852546206006360FDE792141089BE70A97E9E1FA0B8CE576D52F72A1)

- jcef文件缺失导致：检查jbr/bin/server/jvm.dll及jbr/bin/chrome_elf.dll是否存在，jcef文件缺失，导致jcef进程无法拉起，如果不存在，则需要重新安装DevEco Studio：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/-GoDNaxAQNiJfP7yVsGiGQ/zh-cn_image_0000002658804717.png?HW-CC-KV=V1&HW-CC-Date=20260701T041016Z&HW-CC-Expire=86400&HW-CC-Sign=5B4BA05ADFFF17AB1CB4998997C548D6AD111CA83486EDB3E06DF4F4856FE488)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/aB6JbO4ESKivclD4Plbt8w/zh-cn_image_0000002628565350.png?HW-CC-KV=V1&HW-CC-Date=20260701T041016Z&HW-CC-Expire=86400&HW-CC-Sign=27FE80A03671178D7DFFA934CF3941BDE7D91FDAA438EFC9997536FD835458AD)

- jcef沙箱环境与当前电脑环境冲突，导致jcef无法正常工作，关闭jcef沙盒功能：1. 点击右上角的放大镜图标，搜索配置项：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/Xnyn-0hEQ2ySG5Z2GRRQXQ/zh-cn_image_0000002628405448.png?HW-CC-KV=V1&HW-CC-Date=20260701T041016Z&HW-CC-Expire=86400&HW-CC-Sign=E20EF65814D660FE754D19393B12CB0C5D3D4FBF86380219D362FA97108D2DA2)


2. 输入registry，点击下面的Registry...选项：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/LyEC69rlQiO2ZZveK4ob1Q/zh-cn_image_0000002658924673.png?HW-CC-KV=V1&HW-CC-Date=20260701T041016Z&HW-CC-Expire=86400&HW-CC-Sign=8703859E0E5825BB260EC32BE6E9CDFFEE139685811A9B7482D90320AC25C379)


3. 直接输入sandbox进行查找，取消勾选ide.browser.jcef.sandbox.enable这一项，重启IDE：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/Yjs2PlDRQVq-HhwOEEpArg/zh-cn_image_0000002658804735.png?HW-CC-KV=V1&HW-CC-Date=20260701T041016Z&HW-CC-Expire=86400&HW-CC-Sign=A2E14377E7CB19F1E5A7D2B1E7EFF290DBBD14C423E0074D1FD100691DCC076A)
