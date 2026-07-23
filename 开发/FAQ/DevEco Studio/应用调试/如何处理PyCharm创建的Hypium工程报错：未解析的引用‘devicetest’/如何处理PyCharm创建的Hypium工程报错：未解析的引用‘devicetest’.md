# 如何处理PyCharm创建的Hypium工程报错：未解析的引用‘devicetest’

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-73

#### 问题现象

Python已安装4个Hypium离线包，使用PyCharm创建的DevEco Testing Hypium工程报错，显示“未解析的引用'devicetest'”。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/303aZtytR9Gdp0t2f3BpCQ/zh-cn_image_0000002628409430.png?HW-CC-KV=V1&HW-CC-Date=20260723T013949Z&HW-CC-Expire=86400&HW-CC-Sign=1122FD632CE1A9D34874E77F3A3FF66E78167B174031B2C4763C62540A7B2DBD)

 
 

#### 背景知识

- [DevEco Testing Hypium](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hypium-python-guidelines#section16890204264419)是HarmonyOS平台的UI自动化测试框架，支持开发者使用Python语言为应用编写UI自动化测试脚本。
- Hypium安装对xdevice有依赖，优先安装xdevice。请参考[安装向导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hypium-python-guidelines#section191615399595)。

 
 

#### 问题定位

查看当前创建项目Python解释器环境是否成功安装如下包：
 
xdevice；
 
xdevice-aosp；
 
xdevice-devicetest；
 
xdevice-ohos；
 
- 方式一：打开PyCharm点击“File”>“Settings”在“Project:YourProjectName”>“Python Interpreter”部分。查看已安装包如下图：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/Kav5sNN7Rne2vwD9qTk-1A/zh-cn_image_0000002658808697.png?HW-CC-KV=V1&HW-CC-Date=20260723T013949Z&HW-CC-Expire=86400&HW-CC-Sign=ED5CA097EA91E20994B3EFACB239B6F84A52437A0089518E01A78EA7724BF0AF)

- 方式二：在PyCharm中，打开Terminal（底部工具栏的Terminal图标）PyCharm会自动引导到当前虚拟环境。通过pip list命令方式查看已安装包如下图：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/yhcV-QyyRXGp2Xy3oRUsrQ/zh-cn_image_0000002628569336.png?HW-CC-KV=V1&HW-CC-Date=20260723T013949Z&HW-CC-Expire=86400&HW-CC-Sign=D06E8231CCB2111830D3E00F9923556CB12BF5A765DC8E283596DBE32C6B8AB5)


 
 

#### 分析结论

按照安装向导执行命令python -m pip install XXXX，xdevice包会被全局安装放置在Python安装目录下的Lib\site-packages文件夹中，未安装到当前项目配置的虚拟环境导致依赖引用未解析。
 
 

#### 修改建议

xdevice包需要安装到当前项目配置的虚拟环境中，才能解析引用‘devicetest’。
 
- 方式一：在当前项目配置的虚拟环境安装xdevice包。打开Terminal执行命令，以下版本号仅做示例，请以实际版本号为准：python -m pip install xdevice-5.0.7.200.tar.gz

  python -m pip install xdevice-devicetest-5.0.7.200.tar.gz

  python -m pip install xdevice-ohos-5.0.7.200.tar.gz

  python -m pip install hypium-5.0.7.200.tar.gz

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/mhfOqzEnReiUgQkbF_sqLg/zh-cn_image_0000002658928655.png?HW-CC-KV=V1&HW-CC-Date=20260723T013949Z&HW-CC-Expire=86400&HW-CC-Sign=06DFDA41E146E3404A2C68D738E1EC09AB2778DFE0DE02F46938E57518490430)

- 方式二：切换已经安装xdevice包的虚拟环境。打开PyCharm点击“File” > “Settings”在“Project:YourProjectName” > “Python Interpreter”。右侧Python Interpreter下拉框中选择了已安装xdevice包的解释器，点击OK保存设置关闭窗口。PyCharm将会自动切换到选择的虚拟环境，并且所有包管理和运行配置都会基于这个新的解释器。

  
> [!NOTE]
> 此时命令行查看方式需要重启PyCharm。


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/v0J7YR_iRdiWM7SYaJC_Vw/zh-cn_image_0000002628409432.png?HW-CC-KV=V1&HW-CC-Date=20260723T013949Z&HW-CC-Expire=86400&HW-CC-Sign=9F7BAF317237F83950D67B3F0C2D32E07DB696D60FF30BF560BAD512A14E6BEB)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/tc7JWkX9Sn2ck2B4jOxDfw/zh-cn_image_0000002658808699.png?HW-CC-KV=V1&HW-CC-Date=20260723T013949Z&HW-CC-Expire=86400&HW-CC-Sign=FF2700AA460FAD6BA8422D8B92874F01006B0D4597C37C565DDD89D110F8A790)


 
 

#### 常见FAQ

Q：如何卸载xdevice？
 
A：cmd执行命令：python -m pip uninstall hypium xdevice xdevice-devicetest xdevice-aosp xdevice-ohos -y
