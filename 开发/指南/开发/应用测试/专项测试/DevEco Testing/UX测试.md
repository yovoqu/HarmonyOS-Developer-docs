# UX测试

更新时间：2026-06-12 11:57:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ux-testing

#### 多设备布局对比测试

 
**环境准备**
 
**远程模拟器预置**
 
DevEco Studio开发工具安装：
 
请参考[DevEco Studio 指导文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-tools-overview)，点击下载并安装[DevEco Studio](https://developer.huawei.com/consumer/cn/download/deveco-studio)。
 
**hdc工具配置**
 
hdc默认安装在Testing客户端安装目录的**\app\resources\bin**路径下，MacOS系统的hdc位于Testing客户端安装目录的**\Contents\Resources\app\resources\bin**路径下。环境变量请参考[hdc指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hdc#可选命令行直接执行hdc程序)进行配置。
 
**模拟器创建和启动**
 
请参考[模拟器概述](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-emulator)，创建并启动模拟器。
 
**获取远程模拟器的SN**
 
启动模拟器后通过**hdc list targets**命令，查询已启动模拟器SN。模拟器的SN通常为127.0.0.1:port的形式（port默认为5555，端口冲突则依次加2递增）。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/jzAY8Wz0Ru24ALdZ2mentg/zh-cn_image_0000002622164203.png?HW-CC-KV=V1&HW-CC-Date=20260701T041500Z&HW-CC-Expire=86400&HW-CC-Sign=E0AE61028C5BDC17BBE214282CE29183CB038BC868D349DFF12ECB6954DC8C7B)

 
若未配置hdc环境变量，需要先切换到hdc文件目录（hdc安装目录获取参考hdc工具配置），Windows通过** .\hdc list targets**命令，查询已启动模拟器SN。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/fMAIovyGQcyXMcsJliE29w/zh-cn_image_0000002591764530.png?HW-CC-KV=V1&HW-CC-Date=20260701T041500Z&HW-CC-Expire=86400&HW-CC-Sign=EDEEC9F610A7569A472F1BDF87FDDDA0647E8A72A3BF80ED7F742CCB7CB0C692)

 
Mac需要在hdc安装目录下打开命令行，运行**./hdc list targets**命令查询已启动模拟器SN，如下图：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/_kKSheJiS866D1a8n2N8Zg/zh-cn_image_0000002625543585.png?HW-CC-KV=V1&HW-CC-Date=20260701T041500Z&HW-CC-Expire=86400&HW-CC-Sign=F20E82F7B48E4AE9CA2FD8216948EE1B48FCE6FA96201B1CC05A340B2DE7F0C1)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/z6QhyNe-QTq4ErGMavTIwg/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260701T041500Z&HW-CC-Expire=86400&HW-CC-Sign=D964CD23C8F4AAA3FAEC83011760B9C0437998BEBF53F3FA3495F3493707AEF3)
 

模拟器的SN随着启动顺序改变可能会存在改变。
 

 
**获取模拟器所在PC的IP**
 
**Windows**
 
启动windows命令行，输入**ipconfig /all**命令，获取模拟器所在PC的IP。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/TbI8X1E0S0-ugatscbQ5fQ/zh-cn_image_0000002625448575.png?HW-CC-KV=V1&HW-CC-Date=20260701T041500Z&HW-CC-Expire=86400&HW-CC-Sign=4A28B975815A0D3E08DC9B395E4C0EF2E0833A5C91B33450D01910CB81AA436A)

 
**Mac**
 
启动Mac命令行，输入**ifconfig**命令，获取模拟器所在PC的IP。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/-KRdaIDeS12oaYHmcdCUkw/zh-cn_image_0000002595174720.png?HW-CC-KV=V1&HW-CC-Date=20260701T041500Z&HW-CC-Expire=86400&HW-CC-Sign=5DEEA09C53E04D56DB0541F2B27AA01B30CA029FD64CE5F2F334A1AD249F8B79)

 
**远程模拟器启动hdc服务**
 
外部需要通过hdc服务对模拟器进行远程访问，服务器启动命令为hdc kill && hdc -s IP:8710 -e IP -m（其中IP为模拟器所在PC的IP，下同）。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/4XXaFyONSfmnjY5j1hoMlA/zh-cn_image_0000002591764532.png?HW-CC-KV=V1&HW-CC-Date=20260701T041500Z&HW-CC-Expire=86400&HW-CC-Sign=ADE924204F8F12B0E1C9D658A84F79D7374C48B91B543A76A82574C67F0F4573)

 
若未配置hdc环境变量，需要先切换到hdc文件目录（hdc安装目录获取参考hdc工具配置），Windows命令为 .\hdc kill && .\hdc -s ip:8710 -e ip -m。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/xCco6ubRTXOzwoFdPjYvUA/zh-cn_image_0000002622244073.png?HW-CC-KV=V1&HW-CC-Date=20260701T041500Z&HW-CC-Expire=86400&HW-CC-Sign=B74683D14E631F31EC2D0EE14BD98954390C5FF1DC0FC47BD0926B6A513F39D7)

 
Mac需要在hdc安装目录下打开命令行，运行命令 ./hdc kill && ./hdc -s ip:8710 -e ip -m启动服务。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/m4uWyJHLQ4ex4MWQ4vXicQ/zh-cn_image_0000002595183340.png?HW-CC-KV=V1&HW-CC-Date=20260701T041500Z&HW-CC-Expire=86400&HW-CC-Sign=F5F4366FDE950C26912F9DF17A6C4C3F5F2B2C114FB23CA59B42B0DA85BC5294)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/J8hnPNP-QWy9viUWR0lZVw/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260701T041500Z&HW-CC-Expire=86400&HW-CC-Sign=6D540D08430211EEB5D4499E7CE5EFA67A9A6189DBC393A30E3A37E34DE86F3C)
 

服务启动后，在本机执行 hdc list targets 命令会查询不到已启动的设备；可在其他PC通过 hdc -s IP:8710 list targets查询设备。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/z1ZK5VJ3RgaNru9PorM5sQ/zh-cn_image_0000002622164209.png?HW-CC-KV=V1&HW-CC-Date=20260701T041500Z&HW-CC-Expire=86400&HW-CC-Sign=83F417488ED0B8D962D4080EAF570A9692B8A26401A421F160CA4F5ADB3BCEBB)

 

 

 
DevEco Testing连接远程模拟器
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/Se2hAt5gRIuF5sc_xu3P1g/zh-cn_image_0000002595001312.png?HW-CC-KV=V1&HW-CC-Date=20260701T041500Z&HW-CC-Expire=86400&HW-CC-Sign=A5C614765E07FA061EB83C11AA8D42205A9F4D75C0603821D4E842BD024D5959)

 
步骤 1：安装DevEco Testing后，左边菜单栏选择“设置”，开启支持模拟器。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/ZnZ6MmuBSfiR_IgvBwFZpw/zh-cn_image_0000002595161626.png?HW-CC-KV=V1&HW-CC-Date=20260701T041500Z&HW-CC-Expire=86400&HW-CC-Sign=043910D8EC19DAD2D0A1055D2AAB656C9D05E6CD3052067C512A3F2FF12C86BA)

 
步骤 2：选择“远程设备管理”，输入远程设备信息，并建立连接。
 
①远程主机IP：待测设备所在PC的IP地址。
 
②HDC端口：远程PC启动的hdc服务端口，默认为 8710。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/a2YD_N_DQweSBXXLxl83WQ/zh-cn_image_0000002625525937.png?HW-CC-KV=V1&HW-CC-Date=20260701T041500Z&HW-CC-Expire=86400&HW-CC-Sign=6AC061B1986BD36AABCA41266418061D25D19056FECC4037B289A4FD04A960F2)

 
步骤3：点击连接远程模拟器，输入远程模拟器的SN与远程模拟器建立连接。
 
远程主机IP：输入目标远程设备的IP地址。
 
> [!NOTE]
> 在尝试通过DevEco Testing与远程设备建立连接之前，必须先在目标IP 地址的远程设备上，成功启动需要连接的模拟器实例并启动远程hdc服务。

 

 
**创建任务**
 
步骤 1：与远程模拟器建立连接后，左边菜单栏选择“测试服务”，选择“多设备布局对比测试”，点击服务卡片，即进入任务创建界面。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/UGpyejuQRBq5yv6Z8BtRSQ/zh-cn_image_0000002595031352.png?HW-CC-KV=V1&HW-CC-Date=20260701T041500Z&HW-CC-Expire=86400&HW-CC-Sign=CEB6BE3A15DAF4B604FC68DFDDDC5B69BAC5498CD0853B58C0BEA0BA26521F60)

 
步骤 2：进入任务创建界面，配置任务参数。
 
①任务名称：用于标识任务，系统会根据时间生成默认任务名，支持自定义修改。
 
②备注信息：按需填写任务备注信息，便于快速筛选报告。
 
③选择应用：选择需要安装应用，即在远程模拟器上安装新的应用包。
 
④测试设备：选择待测设备。同种类型的设备只支持选择一个，最多可以选择台设备并发执行任务。
 
⑤测试模式：支持自定义选择竖屏、折叠、横屏三种测试模式，建议全选，可以全面覆盖设备在不同形态下的页面表现。
 
⑥测试时长：支持自定义检测时长，建议小时，可以充分提高页面覆盖率。
 
步骤 3：创建任务。参数配置完成后，点击“创建任务”即开始测试。
 

 
**测试执行**
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/kzI6j2yXSTiwzhxIgWVRpA/zh-cn_image_0000002625433427.png?HW-CC-KV=V1&HW-CC-Date=20260701T041500Z&HW-CC-Expire=86400&HW-CC-Sign=DFDDC4E04BE897DB8CB1C644E9E8144312DEA8481587583F3344581AB0AF5535)

 
创建任务后，将会跳转到执行页，测试过程中，在测试页面可以看到累计发现问题汇总、当前页面问题汇总、测试进度，点击查看详情可以实时查看。执行页实时展示测试进度、预计执行时间、预计剩余时间、设备实时投屏、累计发现问题汇总和当前页面问题汇总等信息。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/Aaia8fX5SNWTvPDIrdO22A/zh-cn_image_0000002625489561.png?HW-CC-KV=V1&HW-CC-Date=20260701T041500Z&HW-CC-Expire=86400&HW-CC-Sign=4A0C9C51691ED5E4ED1FFEFD5C83CD22E1F797EDEF1CDDDF663A188E9FBA6EF7)

 
在执行页点击右上角“查看详情”按钮跳转到问题详情页，该页面实时展示检测设备已检测信息，包括累计问题数、检测项（包括检测中和待检测）。通过点击设备信息切换不同设备的检测信息详情。点击各检测项的“不通过数|通过数”对应值可查看该检测项详细检测结果。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/2OK_ONskRrSp0VZkH6Jh5g/zh-cn_image_0000002625539041.png?HW-CC-KV=V1&HW-CC-Date=20260701T041500Z&HW-CC-Expire=86400&HW-CC-Sign=E5394BEF7DAD695ADA64591A757B20D2C2C2476CC9879149650C40800CAC50B5)

 

 
**测试报告**
 
测试完成后，自动生成测试报告。报告包含任务信息、测试结果、问题统计、检测规则。
 
任务信息中，可查看当前应用信息、任务执行时长，及详细的环境参数（配置信息及环境信息），支持导出html的报告文件。
 
测试概览中，包含测试总览、检测机型、结果统计及多设备对比，可直观查看本次任务中，测试项检测结果。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/FkNdLj5DSTmaqhiZhwbO8w/zh-cn_image_0000002591608282.png?HW-CC-KV=V1&HW-CC-Date=20260701T041500Z&HW-CC-Expire=86400&HW-CC-Sign=543BE0DC513C05F06959E8C3DE6D531904D1D79C3D71BD04A399B72B3CD447E7)

 
**测试总览信息解读：**
 
**问题详情****：**累计问题数
 
**视觉风格：**累计视觉风格问题数
 
**系统特性适配：**累计动效问题数
 
**界面布局****：**累计界面布局问题数
 
检测机型页面包含被测设备的基础信息、问题汇总和问题详情等信息。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/bzowpMz9TjeIKITPMP2bbg/zh-cn_image_0000002625490273.png?HW-CC-KV=V1&HW-CC-Date=20260701T041500Z&HW-CC-Expire=86400&HW-CC-Sign=71C0A12C6B3FF22673B5AEFA84C85DFD3B446AF677A6F0733930F6CB6DA446FE)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/PHC8Zb4-ThWT-GATX4YYxQ/zh-cn_image_0000002595211044.png?HW-CC-KV=V1&HW-CC-Date=20260701T041500Z&HW-CC-Expire=86400&HW-CC-Sign=ABBCC663EAFAA848E2FE5844611170AA41B4816578159E9E6FCF78E1C245BFE1)

 
检测不通过或检测异常的规则项，点击查看详情即可查看异常问题详情，包含检测项概览、测试截图、问题列表、详细的问题描述、问题等级和修复指南等信息。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/BOlhZui5TWSoioncUojH5A/zh-cn_image_0000002625491291.png?HW-CC-KV=V1&HW-CC-Date=20260701T041500Z&HW-CC-Expire=86400&HW-CC-Sign=40973B205404B5331CF3CC7C4B1A6D77CDF6C526C07E0679CD1BF6F4375CB557)

 
多设备对比页用于展示同一页面在不同设备上的布局效果。当页面检测未通过时，图片下方将显示当前页面的问题详情。同时运行三个及以上设备时，即使某个设备未能匹配上，也会正常展示该页面数据，未匹配上设备显示为空白。
 
可根据问题描述针对性优化应用UX问题，参考资料：[UX体验标准](https://developer.huawei.com/consumer/cn/doc/design-guides/ux-guidelines-general-0000001760708152)。
 
> [!NOTE]
> 更多测试服务详情，请前往DevEco Testing客户端->测试服务->UX测试->多设备布局对比测试->任务创建页->测试指南中查询。
