# 如何使用DevEco Testing进行应用安装/卸载

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-deveco-testing-faq-11

#### 问题现象

DevEco Testing安装应用支持哪些种类的安装包？如何进行应用安装/卸载？
 
 

#### 背景知识

DevEco Testing是一款专项集成测试工具，提供了多项测试能力。DevEco Testing将测试能力以测试服务卡片的形式呈现给用户，无需复杂的配置，即可一键执行测试任务，同时提供了测试报告和分析，辅助开发者发现应用和产品问题，提升应用质量。
 
 

#### 解决方案

DevEco Testing目前支持安装hap、zip类型的[调试证书](https://developer.huawei.com/consumer/cn/doc/app/agc-help-debug-cert-0000002283256797)签名安装包。
 1. 应用安装：
连接设备，DevEco Testing选择实用工具-设备投屏。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/7Vuab4hfQwmNiMyT0oIU-Q/zh-cn_image_0000002628404180.png?HW-CC-KV=V1&HW-CC-Date=20260730T072727Z&HW-CC-Expire=86400&HW-CC-Sign=D8A45A04E2B0ECF7F759F9C725926F50A79665F00E3C29CA7E4817CEF25AF678)

2. 点击开始投屏，然后工具栏点击安装应用。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/Z-8Esk8_T6KOgPiiqeBZsw/zh-cn_image_0000002628564082.png?HW-CC-KV=V1&HW-CC-Date=20260730T072727Z&HW-CC-Expire=86400&HW-CC-Sign=49C862C74C11FE48FD1A2F1B5FB73E3EFC661343BFB65F91ECD06195CB197652)

3. 本地文件路径点击选择，弹框可选择应用包的类型。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/E-0cm1iCRsme3-WHqdJo9Q/zh-cn_image_0000002658923393.png?HW-CC-KV=V1&HW-CC-Date=20260730T072727Z&HW-CC-Expire=86400&HW-CC-Sign=DAFA601782D5BC61D75C19229F53B93332525FEC12E63D6CEFA07B70BA3C353C)

4. 选择安装包，点击确定，执行日志可以看到安装成功，如果安装失败，可以看到报错信息。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/1EHV6ObGRwiEn8RDwKp3KA/zh-cn_image_0000002658803445.png?HW-CC-KV=V1&HW-CC-Date=20260730T072727Z&HW-CC-Expire=86400&HW-CC-Sign=90CC66453CF6FBB68C320B634E65C3BCD328FC71B874CB64DF9723EB47135F02)

5. 应用卸载：
连接设备，DevEco Testing选择实用工具-设备投屏，工具栏点击卸载应用。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/gFwjYv_fQfu_7MJFAwWNRw/zh-cn_image_0000002628404182.png?HW-CC-KV=V1&HW-CC-Date=20260730T072727Z&HW-CC-Expire=86400&HW-CC-Sign=04DD9B460C27D66644E7896C926A9458333F3B816E240AEE7AF370504911CB4D)

6. 下拉框选择对应的应用，点击确定。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/-2uwr5nLSR69vQ19UqcY_Q/zh-cn_image_0000002628564084.png?HW-CC-KV=V1&HW-CC-Date=20260730T072727Z&HW-CC-Expire=86400&HW-CC-Sign=BAEDF38B388FD1826F5E9C9C46B394C9858EDDE0C7BD9867FCA0997EC927A941)

7. 弹出的对话框，点击确定卸载。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/r7BCHZR2RT-HgH-rMh78-A/zh-cn_image_0000002658923397.png?HW-CC-KV=V1&HW-CC-Date=20260730T072727Z&HW-CC-Expire=86400&HW-CC-Sign=FE6CAC929187E379684EB189B247A80258F68BE0811587B7502BC2911725D02E)

8. toast提示应用卸载成功。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/ifjDLG5cTICMgEBExpyLOw/zh-cn_image_0000002658803447.png?HW-CC-KV=V1&HW-CC-Date=20260730T072727Z&HW-CC-Expire=86400&HW-CC-Sign=7DE5F755A330870D4BEC2E6DBD7A3436BF2C18D037D84D9626105A757A460955)

 
 

#### 常见FAQ

Q：DevEco Testing是否支持安装.app类型的安装包？
 
A：DevEco Testing暂不支持安装.app类型的安装包。
 
Q：DevEco Testing如何安装多包？
 
A：将hap、hsp包打包成zip格式文件，安装应用时文件类型选择*.zip，即可安装。
