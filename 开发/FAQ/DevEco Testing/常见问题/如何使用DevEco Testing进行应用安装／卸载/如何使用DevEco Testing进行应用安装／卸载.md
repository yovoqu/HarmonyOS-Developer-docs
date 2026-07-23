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
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/7Vuab4hfQwmNiMyT0oIU-Q/zh-cn_image_0000002628404180.png?HW-CC-KV=V1&HW-CC-Date=20260723T014021Z&HW-CC-Expire=86400&HW-CC-Sign=14A1576025D83BE0B08E5040C1866A3513CC9F2C32B33B6F85CF03F7DFFFBB90)

2. 点击开始投屏，然后工具栏点击安装应用。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/Z-8Esk8_T6KOgPiiqeBZsw/zh-cn_image_0000002628564082.png?HW-CC-KV=V1&HW-CC-Date=20260723T014021Z&HW-CC-Expire=86400&HW-CC-Sign=BD293F902FF3CD4EB02F0C3B3294C2694342684D6D6FDE36114ACA92195150F1)

3. 本地文件路径点击选择，弹框可选择应用包的类型。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/E-0cm1iCRsme3-WHqdJo9Q/zh-cn_image_0000002658923393.png?HW-CC-KV=V1&HW-CC-Date=20260723T014021Z&HW-CC-Expire=86400&HW-CC-Sign=B24508E5EC65A1EB42820B4A4FDB8659AED5F45BC304DE331557AA11B59BE2CA)

4. 选择安装包，点击确定，执行日志可以看到安装成功，如果安装失败，可以看到报错信息。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/1EHV6ObGRwiEn8RDwKp3KA/zh-cn_image_0000002658803445.png?HW-CC-KV=V1&HW-CC-Date=20260723T014021Z&HW-CC-Expire=86400&HW-CC-Sign=ADD12F84B58FBBFF76CC79A1E6C743A20D3ED2F0E61FA3582C2468F7230C61D0)

5. 应用卸载：
连接设备，DevEco Testing选择实用工具-设备投屏，工具栏点击卸载应用。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/gFwjYv_fQfu_7MJFAwWNRw/zh-cn_image_0000002628404182.png?HW-CC-KV=V1&HW-CC-Date=20260723T014021Z&HW-CC-Expire=86400&HW-CC-Sign=15BA0BC31E8D74236394C9B4122E44B020325A149D56B4767317EAB7F0D59422)

6. 下拉框选择对应的应用，点击确定。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/-2uwr5nLSR69vQ19UqcY_Q/zh-cn_image_0000002628564084.png?HW-CC-KV=V1&HW-CC-Date=20260723T014021Z&HW-CC-Expire=86400&HW-CC-Sign=7EEE1C70EFF351DF6F62465DFD7536B06AF0DEE02E56C437FF806C19F68B5C0D)

7. 弹出的对话框，点击确定卸载。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/r7BCHZR2RT-HgH-rMh78-A/zh-cn_image_0000002658923397.png?HW-CC-KV=V1&HW-CC-Date=20260723T014021Z&HW-CC-Expire=86400&HW-CC-Sign=C1152550192C011EE1DF421BBA402E124733D6096C2A59287AA5EC9FA42DEEF6)

8. toast提示应用卸载成功。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/ifjDLG5cTICMgEBExpyLOw/zh-cn_image_0000002658803447.png?HW-CC-KV=V1&HW-CC-Date=20260723T014021Z&HW-CC-Expire=86400&HW-CC-Sign=2F30E1C4308C63E28AA29ACBB62B86ACC1DC4512D43E5FF103EEAA8206D3EA39)

 
 

#### 常见FAQ

Q：DevEco Testing是否支持安装.app类型的安装包？
 
A：DevEco Testing暂不支持安装.app类型的安装包。
 
Q：DevEco Testing如何安装多包？
 
A：将hap、hsp包打包成zip格式文件，安装应用时文件类型选择*.zip，即可安装。
