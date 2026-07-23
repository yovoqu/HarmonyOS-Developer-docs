# 创建新工程Create Project为空白如何解决

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-23

#### 问题现象
1. 创建新工程时，Create Project为空白。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/v4knCHoQSSu7KQIFv005nA/zh-cn_image_0000002628405062.png?HW-CC-KV=V1&HW-CC-Date=20260723T013903Z&HW-CC-Expire=86400&HW-CC-Sign=7AEB7178F3529117CECF83DD50B1B8D01F5A59C1EF708BA746357B3555EDDEF4)

2. 环境变量JAVA_HOME没有指向有效的jvm。
```bash
The environment variable JAVA_HOME with the value of does not point to a valid JVM installation。
```
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/Q90qiVJ_RY6mKu4r9dmllg/zh-cn_image_0000002658924283.png?HW-CC-KV=V1&HW-CC-Date=20260723T013903Z&HW-CC-Expire=86400&HW-CC-Sign=B17FF7643468AD575F13F6EA4193E50AE5013ADE1D362ABE7D035E43CB30066C)

 
 

#### 背景知识

[DevEco Studio](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-tools-overview?ha_source=sousuo&ha_sourceId=89000251)是基于IntelliJ IDEA Community开源版本打造，面向HarmonyOS应用/元服务开发场景的一站式集成开发环境。提供AI辅助编程、编译构建、UI实时预览、代码调试、性能调优、模拟器等功能，帮助高效开发HarmonyOS应用及元服务。
 
 

#### 问题定位

解决问题的核心思路就是jcef有没有打开，按照如下步骤进行排查：
 1. 检查DevEco Studio是否存在报错：Too many restarts of GPU-process (jcef)。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/7K2H1yeiTJmzIOg8ecHGkQ/zh-cn_image_0000002658804333.png?HW-CC-KV=V1&HW-CC-Date=20260723T013903Z&HW-CC-Expire=86400&HW-CC-Sign=AA552DE5A4E1E166880CAA5710B6F866E94B1A251AA0B4A952A8247D6D2B260B)

2. 查看DevEco Studio依赖的jbr路径下，jvm.dll与chrome_elf.dll是否存在，如果不存在很可能是被杀毒软件误删除了。jvm.dll路径：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/hefRYuveRmmt1ZAP3OFVJg/zh-cn_image_0000002628564972.png?HW-CC-KV=V1&HW-CC-Date=20260723T013903Z&HW-CC-Expire=86400&HW-CC-Sign=6E9D9BD340072B9C1BA4D63EF0C30ABD5FD91629A9C9EBC5F7B6EAFA3F98C208)


  chrome_elf.dll路径：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/anfkXI7WSvWrbaevRSqerg/zh-cn_image_0000002628405072.png?HW-CC-KV=V1&HW-CC-Date=20260723T013903Z&HW-CC-Expire=86400&HW-CC-Sign=4C5A752EB2C87CB48E0B689BC2D96C9D1BDB4F6C89B82A6C8AF44880C393171E)

3. 开发者的环境可能和沙箱环境是否冲突，检查ide.browser.jcef.sandbox.enable=false是否勾选。
 
 

#### 分析结论

- IntelliJ IDEA底层架构的jcef窗口组件的GPU兼容性问题。需要勾选jcef.gpu.disable选项。
- DevEco Studio依赖的jbr路径下没有jvm.dll与chrome_elf.dll文件。DevEco Studio的界面主要是两种swing和jcef，jcef就相当于在开发浏览器的预览，浏览器的预览功能需要依赖chrome的动态链接库，没有这个文件，所有的jcef都起不了。
- 开发者的环境可能和沙箱环境冲突。需要把沙箱屏蔽关掉，就可以正常的打开jcef：ide.browser.jcef.sandbox.enable=false。

 
 

#### 修改建议

根据如下建议修改，查看是否能解决问题（不是所有选项都要改掉）：
 
- 按照图示开启jcef.gpu.disable：help->find action，输入registry，点击生成registry界面；registry界面中勾选jcef.gpu.disable选项。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/LBZIX0sCQSO9fDmFVlT4UA/zh-cn_image_0000002658924287.png?HW-CC-KV=V1&HW-CC-Date=20260723T013903Z&HW-CC-Expire=86400&HW-CC-Sign=16806326BE28C5728930EE11017E5EE27D448A531694BA51F691BB787878523E)

- 找杀毒软件，将文件添加到白名单并恢复文件。或者重新安装应用，在杀毒软件提示拦截的时候放行。
- 直接添加ide.browser.jcef.sandbox.enable=false，通过Help -> Edit Custom Properties...打开对应的配置页面，在后面添加ide.browser.jcef.sandbox.enable=false即可。

 
 

#### 总结

DevEco Studio在运行过程中会遇到页面打开空白的情况，这个问题与GPU兼容性有关，特别是在使用Native调试堆栈可视化功能时，通常发生在电脑GPU不兼容或在云桌面环境下使用DevEco Studio的情况下。如果发现多数页面都空白，例如Create Project、Project Structure等页面，大概率是IDE的jcef配置有问题，着重从这方面开始排查问题即可。
