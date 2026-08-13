# UX测试

更新时间：2026-08-04 01:38:00

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ux-testing

#### 多设备布局对比测试


![](assets/UX测试/file-20260708103708e2cedcd9.png)
 

多设备布局对比测试支持模拟器；下文将首先介绍如何在 DevEco Studio 中配置模拟器，如电脑已经配置模拟器，可跳过“环境准备”步骤。
 

 
 

#### 环境准备

 
**远程模拟器预置**
 
DevEco Studio开发工具安装：
 
请参考[DevEco Studio 指导文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-tools-overview)，点击下载并安装[DevEco Studio](https://developer.huawei.com/consumer/cn/download/deveco-studio)。
 
**hdc工具配置**
 
hdc默认安装在Testing客户端安装目录的**\app\resources\bin**路径下，MacOS系统的hdc位于Testing客户端安装目录的**\Contents\Resources\app\resources\bin**路径下。环境变量请参考[hdc指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hdc#可选命令行直接执行hdc程序)进行配置。
 
**模拟器创建和启动**
 
请参考[模拟器概述](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-emulator)，创建并启动模拟器。
 
**获取远程模拟器的SN**
 
启动模拟器后通过**hdc list targets**命令，查询已启动模拟器SN。模拟器的SN通常为127.0.0.1:port的形式（port默认为5555，端口冲突则依次加2递增）。
 

![](assets/UX测试/file-2026070810370925880d37.png)

 
若未配置hdc环境变量，需要先切换到hdc文件目录（hdc安装目录获取参考hdc工具配置），Windows通过** .\hdc list targets**命令，查询已启动模拟器SN。
 

![](assets/UX测试/file-202607081037098d2bd68a.png)

 
Mac需要在hdc安装目录下打开命令行，运行**./hdc list targets**命令查询已启动模拟器SN，如下图：
 

![](assets/UX测试/file-20260708103709e7f448b4.png)

 

![](assets/UX测试/file-20260708103710864a2979.png)
 

模拟器的SN随着启动顺序改变可能会存在改变。
 

 
**获取模拟器所在PC的IP**
 
**Windows**
 
启动windows命令行，输入**ipconfig /all**命令，获取模拟器所在PC的IP。
 

![](assets/UX测试/file-20260708103710869ffb4f.png)

 
**Mac**
 
启动Mac命令行，输入**ifconfig**命令，获取模拟器所在PC的IP。
 

![](assets/UX测试/file-202607081037113065990e.png)

 
**远程模拟器启动hdc服务**
 
外部需要通过hdc服务对模拟器进行远程访问，服务器启动命令为hdc kill && hdc -s IP:8710 -e IP -m（其中IP为模拟器所在PC的IP，下同）。
 

![](assets/UX测试/file-20260708103711dd55a6ed.png)

 
若未配置hdc环境变量，需要先切换到hdc文件目录（hdc安装目录获取参考hdc工具配置），Windows命令为 .\hdc kill && .\hdc -s ip:8710 -e ip -m。
 

![](assets/UX测试/file-202607081037120defa08e.png)

 
Mac需要在hdc安装目录下打开命令行，运行命令 ./hdc kill && ./hdc -s ip:8710 -e ip -m启动服务。
 

![](assets/UX测试/file-20260708103712bf75d6aa.png)

 

![](assets/UX测试/file-20260708103712e7f448b4.png)
 

服务启动后，在本机执行 hdc list targets 命令会查询不到已启动的设备；可在其他PC通过 hdc -s IP:8710 list targets查询设备。
 

![](assets/UX测试/file-202607081037136849782b.png)

 

 

 

#### DevEco Testing连接远程模拟器

 

![](assets/UX测试/file-20260708103713b12a04d9.png)

 
步骤 1：安装DevEco Testing后，左边菜单栏选择“设置”，开启支持模拟器。
 

![](assets/UX测试/file-20260708103714c6d50679.png)

 
步骤 2：选择“远程设备管理”，输入远程设备信息，并建立连接。
 
①远程主机IP：待测设备所在PC的IP地址。
 
②HDC端口：远程PC启动的hdc服务端口，默认为 8710。
 

![](assets/UX测试/file-202607081037156a772401.png)

 
步骤3：点击连接远程模拟器，输入远程模拟器的SN与远程模拟器建立连接。
 
远程主机IP：输入目标远程设备的IP地址。
 
> [!NOTE]
> 在尝试通过DevEco Testing与远程设备建立连接之前，必须先在目标IP 地址的远程设备上，成功启动需要连接的模拟器实例并启动远程hdc服务。

 

 

#### 开始使用多设备布局对比测试

 
**创建任务**
 
步骤 1：与远程模拟器建立连接后，左边菜单栏选择“测试服务”，选择“多设备布局对比测试”，点击服务卡片，即进入任务创建界面。
 

![](assets/UX测试/file-202607081037159c5b0727.png)

 
步骤 2：进入任务创建界面，配置任务参数。
 
①任务名称：用于标识任务，系统会根据时间生成默认任务名，支持自定义修改。
 
②备注信息：按需填写任务备注信息，便于快速筛选报告。
 
③选择应用：选择需要安装应用，即在远程模拟器上安装新的应用包。
 
④测试设备：选择待测设备。同种类型的设备只支持选择一个，最多可以选择台设备并发执行任务。
 
⑤测试模式：支持自定义选择竖屏、折叠、横屏三种测试模式，建议全选，可以全面覆盖设备在不同形态下的页面表现。
 
⑥测试时长：支持自定义检测时长，建议小时，可以充分提高页面覆盖率。
 
步骤 3：创建任务。参数配置完成后，点击“创建任务”即开始测试。
 

 
**测试执行**
 

![](assets/UX测试/file-202607081037161d82e8eb.png)

 
创建任务后，将会跳转到执行页，测试过程中，在测试页面可以看到累计发现问题汇总、当前页面问题汇总、测试进度，点击查看详情可以实时查看。执行页实时展示测试进度、预计执行时间、预计剩余时间、设备实时投屏、累计发现问题汇总和当前页面问题汇总等信息。
 

![](assets/UX测试/file-20260708103716578a26f3.png)

 
在执行页点击右上角“查看详情”按钮跳转到问题详情页，该页面实时展示检测设备已检测信息，包括累计问题数、检测项（包括检测中和待检测）。通过点击设备信息切换不同设备的检测信息详情。点击各检测项的“不通过数|通过数”对应值可查看该检测项详细检测结果。
 

![](assets/UX测试/file-2026070810371659144ed6.png)

 

 
**测试报告**
 
测试完成后，自动生成测试报告。报告包含任务信息、测试结果、问题统计、检测规则。
 
任务信息中，可查看当前应用信息、任务执行时长，及详细的环境参数（配置信息及环境信息），支持导出html的报告文件。
 
测试概览中，包含测试总览、检测机型、结果统计及多设备对比，可直观查看本次任务中，测试项检测结果。
 

![](assets/UX测试/file-20260708103717cb35de5d.png)

 
**测试总览信息解读：**
 
**问题详情****：**累计问题数
 
**视觉风格：**累计视觉风格问题数
 
**系统特性适配：**累计动效问题数
 
**界面布局****：**累计界面布局问题数
 
检测机型页面包含被测设备的基础信息、问题汇总和问题详情等信息。
 

![](assets/UX测试/file-2026070810371867d56515.png)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/y1RJesDtQLW2UAV7mv6j0w/zh-cn_image_0000002664012255.png?HW-CC-KV=V1&HW-CC-Date=20260813T095906Z&HW-CC-Expire=86400&HW-CC-Sign=09088D384A96A3EE240EF9E6AF3EE15CACA7AE2086BBA59B94408892E11B3D79)

 
检测不通过或检测异常的规则项，点击查看详情即可查看异常问题详情，包含检测项概览、测试截图、问题列表、详细的问题描述、问题等级和修复指南等信息。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/4c5fRtqlTV2XGjG67Nu-Bw/zh-cn_image_0000002663932185.png?HW-CC-KV=V1&HW-CC-Date=20260813T095906Z&HW-CC-Expire=86400&HW-CC-Sign=A48F99012E48FA549F8DE2ADCFE0806A3D6CB2CC801D1538C26891AB82694274)

 
多设备对比页用于展示同一页面在不同设备上的布局效果。当页面检测未通过时，图片下方将显示当前页面的问题详情。同时运行三个及以上设备时，即使某个设备未能匹配上，也会正常展示该页面数据，未匹配上设备显示为空白。
 
可根据问题描述针对性优化应用UX问题，参考资料：[UX体验标准](https://developer.huawei.com/consumer/cn/doc/design-guides/ux-guidelines-general-0000001760708152)。
 
> [!NOTE]
> 更多测试服务详情，请前往DevEco Testing客户端->测试服务->UX测试->多设备布局对比测试->任务创建页->测试指南中查询。
