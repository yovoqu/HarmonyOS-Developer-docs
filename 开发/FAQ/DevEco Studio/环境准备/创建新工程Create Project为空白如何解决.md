# 创建新工程Create Project为空白如何解决

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-23

## 创建新工程Create Project为空白如何解决
 


##### 问题现象

- 创建新工程时，Create Project为空白。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/v4knCHoQSSu7KQIFv005nA/zh-cn_image_0000002628405062.png?HW-CC-KV=V1&HW-CC-Date=20260701T025909Z&HW-CC-Expire=86400&HW-CC-Sign=AF933717BC0F93A71C88555FD34A023BBF1C5E90E6E5B5DA6AD48D641CB313E5)

- 环境变量JAVA_HOME没有指向有效的jvm。
```text
The environment variable JAVA_HOME with the value of does not point to a valid JVM installation。
```
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/Q90qiVJ_RY6mKu4r9dmllg/zh-cn_image_0000002658924283.png?HW-CC-KV=V1&HW-CC-Date=20260701T025909Z&HW-CC-Expire=86400&HW-CC-Sign=900928EF1C8EF029A883D40BBFDF39BD85502580EA16F205233C55C576EE1D42)


 
 

##### 背景知识

[DevEco Studio](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-tools-overview?ha_source=sousuo&ha_sourceId=89000251)是基于IntelliJ IDEA Community开源版本打造，面向HarmonyOS应用/元服务开发场景的一站式集成开发环境。提供AI辅助编程、编译构建、UI实时预览、代码调试、性能调优、模拟器等功能，帮助高效开发HarmonyOS应用及元服务。
 
 

##### 问题定位

解决问题的核心思路就是jcef有没有打开，按照如下步骤进行排查：
 
- 检查DevEco Studio是否存在报错：Too many restarts of GPU-process (jcef)。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/7K2H1yeiTJmzIOg8ecHGkQ/zh-cn_image_0000002658804333.png?HW-CC-KV=V1&HW-CC-Date=20260701T025909Z&HW-CC-Expire=86400&HW-CC-Sign=8E7B67697B5A0C199EE9BB089D13EAC8C42CF345C4D59CF2AD3F88B5544E18C7)

- 查看DevEco Studio依赖的jbr路径下，jvm.dll与chrome_elf.dll是否存在，如果不存在很可能是被杀毒软件误删除了。jvm.dll路径：
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/hefRYuveRmmt1ZAP3OFVJg/zh-cn_image_0000002628564972.png?HW-CC-KV=V1&HW-CC-Date=20260701T025909Z&HW-CC-Expire=86400&HW-CC-Sign=7306192268BDB8875B9CCE6C4F9B992FA7A2A4AFD6E3949EA907E0E93EF4F41B)

 chrome_elf.dll路径：
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/anfkXI7WSvWrbaevRSqerg/zh-cn_image_0000002628405072.png?HW-CC-KV=V1&HW-CC-Date=20260701T025909Z&HW-CC-Expire=86400&HW-CC-Sign=FFCB815669BA68459E8E81D14C65561AC7215820BCE2128A3FC52CA8A045B086)

- 开发者的环境可能和沙箱环境是否冲突，检查ide.browser.jcef.sandbox.enable=false是否勾选。

 
 

##### 分析结论

- IntelliJ IDEA底层架构的jcef窗口组件的GPU兼容性问题。需要勾选jcef.gpu.disable选项。
- DevEco Studio依赖的jbr路径下没有jvm.dll与chrome_elf.dll文件。DevEco Studio的界面主要是两种swing和jcef，jcef就相当于在开发浏览器的预览，浏览器的预览功能需要依赖chrome的动态链接库，没有这个文件，所有的jcef都起不了。
- 开发者的环境可能和沙箱环境冲突。需要把沙箱屏蔽关掉，就可以正常的打开jcef：ide.browser.jcef.sandbox.enable=false。

 
 

##### 修改建议

根据如下建议修改，查看是否能解决问题（不是所有选项都要改掉）：
 
- 按照图示开启jcef.gpu.disable：help->find action，输入registry，点击生成registry界面；registry界面中勾选jcef.gpu.disable选项。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/LBZIX0sCQSO9fDmFVlT4UA/zh-cn_image_0000002658924287.png?HW-CC-KV=V1&HW-CC-Date=20260701T025909Z&HW-CC-Expire=86400&HW-CC-Sign=312DEEA7439179B231B80EDBF684269736A61A2EAB5F12DF0E7198FBBF55C75B)

- 找杀毒软件，将文件添加到白名单并恢复文件。或者重新安装应用，在杀毒软件提示拦截的时候放行。
- 直接添加ide.browser.jcef.sandbox.enable=false，通过Help -> Edit Custom Properties...打开对应的配置页面，在后面添加ide.browser.jcef.sandbox.enable=false即可。

 
 

##### 总结

DevEco Studio在运行过程中会遇到页面打开空白的情况，这个问题与GPU兼容性有关，特别是在使用Native调试堆栈可视化功能时，通常发生在电脑GPU不兼容或在云桌面环境下使用DevEco Studio的情况下。如果发现多数页面都空白，例如Create Project、Project Structure等页面，大概率是IDE的jcef配置有问题，着重从这方面开始排查问题即可。
