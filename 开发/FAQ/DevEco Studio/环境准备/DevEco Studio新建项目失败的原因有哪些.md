# DevEco Studio新建项目失败的原因有哪些

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-33

## DevEco Studio新建项目失败的原因有哪些
 


##### 问题现象

DevEco Studio新建项目失败，如何定位修复。
 
 

##### 背景知识

HUAWEI DevEco Studio（获取工具请单击[链接下载](https://developer.huawei.com/consumer/cn/download/deveco-studio)，以下简称DevEco Studio）是基于IntelliJ IDEA Community开源版本打造，面向HarmonyOS应用/元服务开发场景的一站式集成开发环境。提供AI辅助编程、编译构建、UI实时预览、代码调试、性能调优、模拟器等功能，帮助你高效开发HarmonyOS应用及元服务。
 
DevEco Studio提供开箱即用的开发体验，将HarmonyOS SDK、Node.js、Hvigor、OHPM、模拟器平台等进行合一打包，简化DevEco Studio安装配置流程。
 
 

##### 问题定位

- DevEco Studio新建项目失败，可能有多种现象和原因，汇总如下： 
| 问题现象 | 问题原因 |
| --- | --- |
| 运行报错ROR:node。 | Node环境出现问题。 |
| 新建项目时，出现npm报错。 | npm SSL证书验证问题。 |
| 新建项目窗口无任何内容。 | 安装过程出现问题。 |
| 新建项目时，出现Cannot detect a launch configuration。 | 项目配置或构建设置问题。 |
- **场景一**：运行报错ROR:node。
排查PC设备是否存在多Node，命令行输入node -v，排查Node版本是否低于18。
- 查看NODE_HOME是否配置：
Windows环境：在系统或者用户的PATH变量中查看NODE_HOME。
- MacOS环境：终端输入echo $SHELL。

 
 - **场景二**：新建项目时，出现npm报错，如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/-Q1t9uOvT8yg9sB4sK3GEg/zh-cn_image_0000002628565012.png?HW-CC-KV=V1&HW-CC-Date=20260701T025910Z&HW-CC-Expire=86400&HW-CC-Sign=F47CF9B1602F80B07DCB1864C0DD3065340D9EC8A73B906818E17ED3E4EE1517)

- **场景三**：新建项目窗口无任何内容，如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/YklHCP4PT4yAFTgXfbb8yg/zh-cn_image_0000002628405106.png?HW-CC-KV=V1&HW-CC-Date=20260701T025910Z&HW-CC-Expire=86400&HW-CC-Sign=590342F2823EBA612F54531F560E9D52B5F06993E9FB52E39DAD53DC0FDEC101)

- **场景四**：新建项目时，出现Cannot detect a launch configuration，如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/GQfb9vewT6yEBZgTi07JRQ/zh-cn_image_0000002658924327.png?HW-CC-KV=V1&HW-CC-Date=20260701T025910Z&HW-CC-Expire=86400&HW-CC-Sign=F369DE45E14FB1776B74A7E49B6240A23102D20C10064B87BE1BB7995B5C7704)


 
 

##### 分析结论

- **场景一**：可以得出如下结论：
Mac中Node.js版本与IDE自带的Node.js 18.x有冲突。
- 未配置Node环境。

 - **场景二**：根据报错信息分析是npm SSL证书验证问题。
- **场景三**：新建项目界面空白，可能是相关配置问题或者是安装过程出现问题。
- **场景四**：出现 “Cannot detect a launch configuration” 错误，通常与项目配置或构建设置有关。

 
 

##### 修改建议

- **场景一**：尝试如下方案：
重新下载一个Node.js18的版本。
- 找到IDE的安装目录，bin文件夹下的idea.properties文件，打开文件搜索ide.node.location，将node的bin目录配置上去，或者通过Help-Edit Custom Properties打开ide.node.location，参考如下：
Windows环境：Windows存放在node目录下。
- MacOS环境：Linux和MacOS存放在node/bin目录下。

 
 - **场景二**：尝试如下方案：
**方案一**：执行npm config set strict-ssl false命令，禁用SSL证书验证。
- **方案二**：进入“C:\Users\用户名目录”，打开.npmrc文件，修改SSL证书验证，在文件末尾添加strict-ssl=false。

 - **场景三**：尝试如下方案：
**方案一**：
help>find action>输入registry，点击界面生成registry界面。
- 点击界面，输入jcef.gpu，在弹出的registry界面中，勾选jcef.gpu.disable，禁用。

 - **方案二**：可能是安装过程出现了问题，尝试卸载DevEco Studio然后重新安装。

 - **场景四**：尝试如下方案：
下载安装最新的DevEco Studio版本。
- 任务管理器中查找所有devecostudio64.exe并终止。
- 如果启动了杀毒软件，暂时禁用杀毒软件。
- 以管理员身份启动程序。
- 添加ide.browser.jcef.sandbox.enable=false。在DevEco Studio的安装路径下的“bin/idea.properties”后面添加字段ide.browser.jcef.sandbox.enable=false。
