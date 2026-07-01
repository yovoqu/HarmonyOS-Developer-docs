# 创建新工程Create Project为空白如何解决

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-23

#### 问题现象
1. 创建新工程时，Create Project为空白。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/v4knCHoQSSu7KQIFv005nA/zh-cn_image_0000002628405062.png?HW-CC-KV=V1&HW-CC-Date=20260701T041017Z&HW-CC-Expire=86400&HW-CC-Sign=408BAB79F17ECE3C23B1A08719369ECFC24BCFEDCCEAA615FFD728F3B5F77352)

2. 环境变量JAVA_HOME没有指向有效的jvm。
```bash
The environment variable JAVA_HOME with the value of does not point to a valid JVM installation。
```
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/Q90qiVJ_RY6mKu4r9dmllg/zh-cn_image_0000002658924283.png?HW-CC-KV=V1&HW-CC-Date=20260701T041017Z&HW-CC-Expire=86400&HW-CC-Sign=CA8B614ADE84F5A09FFDC1B671A02004EBC66490442AE1C853A431195465330B)

 
 

#### 背景知识

[DevEco Studio](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-tools-overview?ha_source=sousuo&ha_sourceId=89000251)是基于IntelliJ IDEA Community开源版本打造，面向HarmonyOS应用/元服务开发场景的一站式集成开发环境。提供AI辅助编程、编译构建、UI实时预览、代码调试、性能调优、模拟器等功能，帮助高效开发HarmonyOS应用及元服务。
 
 

#### 问题定位

解决问题的核心思路就是jcef有没有打开，按照如下步骤进行排查：
 1. 检查DevEco Studio是否存在报错：Too many restarts of GPU-process (jcef)。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/7K2H1yeiTJmzIOg8ecHGkQ/zh-cn_image_0000002658804333.png?HW-CC-KV=V1&HW-CC-Date=20260701T041017Z&HW-CC-Expire=86400&HW-CC-Sign=910690428FFF7D6E953BAD23333A44E5FACB894886FC7AB21E92EB4328253580)

2. 查看DevEco Studio依赖的jbr路径下，jvm.dll与chrome_elf.dll是否存在，如果不存在很可能是被杀毒软件误删除了。jvm.dll路径：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/hefRYuveRmmt1ZAP3OFVJg/zh-cn_image_0000002628564972.png?HW-CC-KV=V1&HW-CC-Date=20260701T041017Z&HW-CC-Expire=86400&HW-CC-Sign=F76C9D0E1E15F8E18096E87E5771E88C04DF2B33121F679E2A438A870A13596C)


  chrome_elf.dll路径：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/anfkXI7WSvWrbaevRSqerg/zh-cn_image_0000002628405072.png?HW-CC-KV=V1&HW-CC-Date=20260701T041017Z&HW-CC-Expire=86400&HW-CC-Sign=94BFBA5161CAA18192B39B00630FAEC4C7D89F196022ACDB264CFE6A0A462C81)

3. 开发者的环境可能和沙箱环境是否冲突，检查ide.browser.jcef.sandbox.enable=false是否勾选。
 
 

#### 分析结论

- IntelliJ IDEA底层架构的jcef窗口组件的GPU兼容性问题。需要勾选jcef.gpu.disable选项。
- DevEco Studio依赖的jbr路径下没有jvm.dll与chrome_elf.dll文件。DevEco Studio的界面主要是两种swing和jcef，jcef就相当于在开发浏览器的预览，浏览器的预览功能需要依赖chrome的动态链接库，没有这个文件，所有的jcef都起不了。
- 开发者的环境可能和沙箱环境冲突。需要把沙箱屏蔽关掉，就可以正常的打开jcef：ide.browser.jcef.sandbox.enable=false。

 
 

#### 修改建议

根据如下建议修改，查看是否能解决问题（不是所有选项都要改掉）：
 
- 按照图示开启jcef.gpu.disable：help->find action，输入registry，点击生成registry界面；registry界面中勾选jcef.gpu.disable选项。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/LBZIX0sCQSO9fDmFVlT4UA/zh-cn_image_0000002658924287.png?HW-CC-KV=V1&HW-CC-Date=20260701T041017Z&HW-CC-Expire=86400&HW-CC-Sign=0886EC284441B228A6E8C3EF0BDD1237F615ECFAAB3F6355DBD3298F45E228A8)

- 找杀毒软件，将文件添加到白名单并恢复文件。或者重新安装应用，在杀毒软件提示拦截的时候放行。
- 直接添加ide.browser.jcef.sandbox.enable=false，通过Help -> Edit Custom Properties...打开对应的配置页面，在后面添加ide.browser.jcef.sandbox.enable=false即可。

 
 

#### 总结

DevEco Studio在运行过程中会遇到页面打开空白的情况，这个问题与GPU兼容性有关，特别是在使用Native调试堆栈可视化功能时，通常发生在电脑GPU不兼容或在云桌面环境下使用DevEco Studio的情况下。如果发现多数页面都空白，例如Create Project、Project Structure等页面，大概率是IDE的jcef配置有问题，着重从这方面开始排查问题即可。
