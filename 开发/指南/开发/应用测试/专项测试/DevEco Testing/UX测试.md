# UX测试

更新时间：2026-06-12 11:57:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ux-testing

## UX测试
 


##### 多设备布局对比测试

 
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
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/jzAY8Wz0Ru24ALdZ2mentg/zh-cn_image_0000002622164203.png?HW-CC-KV=V1&HW-CC-Date=20260701T025444Z&HW-CC-Expire=86400&HW-CC-Sign=94F3EC4831D5DAAAF3152734E70A0259EB0C5A12BA734AF4CB895F6474439165)

 
若未配置hdc环境变量，需要先切换到hdc文件目录（hdc安装目录获取参考hdc工具配置），Windows通过** .\hdc list targets**命令，查询已启动模拟器SN。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/fMAIovyGQcyXMcsJliE29w/zh-cn_image_0000002591764530.png?HW-CC-KV=V1&HW-CC-Date=20260701T025444Z&HW-CC-Expire=86400&HW-CC-Sign=C431E01508A83D0810DC19B4CD7372E07C741C6FDB5A4AA396A908E567A321C1)

 
Mac需要在hdc安装目录下打开命令行，运行**./hdc list targets**命令查询已启动模拟器SN，如下图：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/_kKSheJiS866D1a8n2N8Zg/zh-cn_image_0000002625543585.png?HW-CC-KV=V1&HW-CC-Date=20260701T025444Z&HW-CC-Expire=86400&HW-CC-Sign=D108223CB13854E6E11F6403E8A5254C95B07A54F00D035684D076BCD1A1D999)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/z6QhyNe-QTq4ErGMavTIwg/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260701T025444Z&HW-CC-Expire=86400&HW-CC-Sign=F2D89772456B81C7EF101F6D7F3ECBD08D72E1A22A743DFD9E6B8A2E4E219959)
 

模拟器的SN随着启动顺序改变可能会存在改变。
 

 
**获取模拟器所在PC的IP**
 
**Windows**
 
启动windows命令行，输入**ipconfig /all**命令，获取模拟器所在PC的IP。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/TbI8X1E0S0-ugatscbQ5fQ/zh-cn_image_0000002625448575.png?HW-CC-KV=V1&HW-CC-Date=20260701T025444Z&HW-CC-Expire=86400&HW-CC-Sign=FA2E4DF273C5145069C80FBF2AE126C40BD95E48DB174ABCCD44BD4B7E1343B7)

 
**Mac**
 
启动Mac命令行，输入**ifconfig**命令，获取模拟器所在PC的IP。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/-KRdaIDeS12oaYHmcdCUkw/zh-cn_image_0000002595174720.png?HW-CC-KV=V1&HW-CC-Date=20260701T025444Z&HW-CC-Expire=86400&HW-CC-Sign=F72F8B616609B2C945E4D68EFDF3E47EDF1BC677FA97777AACAA58CDC6CFD9AE)

 
**远程模拟器启动hdc服务**
 
外部需要通过hdc服务对模拟器进行远程访问，服务器启动命令为hdc kill && hdc -s IP:8710 -e IP -m（其中IP为模拟器所在PC的IP，下同）。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/4XXaFyONSfmnjY5j1hoMlA/zh-cn_image_0000002591764532.png?HW-CC-KV=V1&HW-CC-Date=20260701T025444Z&HW-CC-Expire=86400&HW-CC-Sign=3DF5E79025926F97AEA928DC1CBEAED6B31EA038E455C44F5C6C1E5393CE4090)

 
若未配置hdc环境变量，需要先切换到hdc文件目录（hdc安装目录获取参考hdc工具配置），Windows命令为 .\hdc kill && .\hdc -s ip:8710 -e ip -m。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/xCco6ubRTXOzwoFdPjYvUA/zh-cn_image_0000002622244073.png?HW-CC-KV=V1&HW-CC-Date=20260701T025444Z&HW-CC-Expire=86400&HW-CC-Sign=BAAB7E5B06FC8E347EB6567385406461C9C5ACB6A74E24FC7A9CFF6DA26A75A8)

 
Mac需要在hdc安装目录下打开命令行，运行命令 ./hdc kill && ./hdc -s ip:8710 -e ip -m启动服务。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/m4uWyJHLQ4ex4MWQ4vXicQ/zh-cn_image_0000002595183340.png?HW-CC-KV=V1&HW-CC-Date=20260701T025444Z&HW-CC-Expire=86400&HW-CC-Sign=2BE856286F0E7ADAF86BFEF25F31BC56B0C8D9AB4FE2377AA3FC5273D681A139)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/J8hnPNP-QWy9viUWR0lZVw/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260701T025444Z&HW-CC-Expire=86400&HW-CC-Sign=296433647C285C2FAD9899559B1DB1C5162FCBFA2AF529B77BFDB8695C8461C4)
 

服务启动后，在本机执行 hdc list targets 命令会查询不到已启动的设备；可在其他PC通过 hdc -s IP:8710 list targets查询设备。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/z1ZK5VJ3RgaNru9PorM5sQ/zh-cn_image_0000002622164209.png?HW-CC-KV=V1&HW-CC-Date=20260701T025444Z&HW-CC-Expire=86400&HW-CC-Sign=100E9A3AB31A023D7D48C530F61D8BD5B234C1EE78B412710F414CC691BEE5C6)

 

 

 
DevEco Testing连接远程模拟器
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/Se2hAt5gRIuF5sc_xu3P1g/zh-cn_image_0000002595001312.png?HW-CC-KV=V1&HW-CC-Date=20260701T025444Z&HW-CC-Expire=86400&HW-CC-Sign=7EE71A2F2EBF092FF518F7DF6CA4FA14D226C1E8C57BD5E785AE40EBB15347B2)

 
步骤 1：安装DevEco Testing后，左边菜单栏选择“设置”，开启支持模拟器。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/ZnZ6MmuBSfiR_IgvBwFZpw/zh-cn_image_0000002595161626.png?HW-CC-KV=V1&HW-CC-Date=20260701T025444Z&HW-CC-Expire=86400&HW-CC-Sign=6BD65D1B5B227DE7C8D813EB599C0561E1211841B9ED2AD96575B13E2C4D1104)

 
步骤 2：选择“远程设备管理”，输入远程设备信息，并建立连接。
 
①远程主机IP：待测设备所在PC的IP地址。
 
②HDC端口：远程PC启动的hdc服务端口，默认为 8710。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/a2YD_N_DQweSBXXLxl83WQ/zh-cn_image_0000002625525937.png?HW-CC-KV=V1&HW-CC-Date=20260701T025444Z&HW-CC-Expire=86400&HW-CC-Sign=35CA221D97E994DBAD819857A0055F64C8519818B8EA8F6CA09EDE2822F15EFC)

 
步骤3：点击连接远程模拟器，输入远程模拟器的SN与远程模拟器建立连接。
 
远程主机IP：输入目标远程设备的IP地址。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/dSzlAm7ZTFCJG59ZjeA0uQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260701T025444Z&HW-CC-Expire=86400&HW-CC-Sign=0A69DC703126F307E488240FF67E91AEA59365E43AFA11F08923A59980840FB2)
 

在尝试通过DevEco Testing与远程设备建立连接之前，必须先在目标IP 地址的远程设备上，成功启动需要连接的模拟器实例并启动远程hdc服务。
 

 

 
**创建任务**
 
步骤 1：与远程模拟器建立连接后，左边菜单栏选择“测试服务”，选择“多设备布局对比测试”，点击服务卡片，即进入任务创建界面。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/UGpyejuQRBq5yv6Z8BtRSQ/zh-cn_image_0000002595031352.png?HW-CC-KV=V1&HW-CC-Date=20260701T025444Z&HW-CC-Expire=86400&HW-CC-Sign=4D40A2DC58C4F2997C6CE4E8E9AF8A5C37D59ED0203A8F330280317588D01461)

 
步骤 2：进入任务创建界面，配置任务参数。
 
①任务名称：用于标识任务，系统会根据时间生成默认任务名，支持自定义修改。
 
②备注信息：按需填写任务备注信息，便于快速筛选报告。
 
③选择应用：选择需要安装应用，即在远程模拟器上安装新的应用包。
 
④测试设备：选择待测设备。同种类型的设备只支持选择一个，最多可以选择台设备并发执行任务。
 
⑤测试模式：支持自定义选择竖屏、折叠、横屏三种测试模式，建议全选，可以全面覆盖设备在不同形态下的页面表现。
 
⑥测试时长：支持自定义检测时长，建议小时，可以充分提高页面覆盖率。
 
步骤 3：创建任务。参数配置完成后，点击“创建任务”即开始测试。
 

 
**测试执行**
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/kzI6j2yXSTiwzhxIgWVRpA/zh-cn_image_0000002625433427.png?HW-CC-KV=V1&HW-CC-Date=20260701T025444Z&HW-CC-Expire=86400&HW-CC-Sign=DD9DD2A52F382D30F295CFC5C1F3F490CB20FDFE815B7BADC5CEA32BEA286BC7)

 
创建任务后，将会跳转到执行页，测试过程中，在测试页面可以看到累计发现问题汇总、当前页面问题汇总、测试进度，点击查看详情可以实时查看。执行页实时展示测试进度、预计执行时间、预计剩余时间、设备实时投屏、累计发现问题汇总和当前页面问题汇总等信息。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/Aaia8fX5SNWTvPDIrdO22A/zh-cn_image_0000002625489561.png?HW-CC-KV=V1&HW-CC-Date=20260701T025444Z&HW-CC-Expire=86400&HW-CC-Sign=0F23A0DA4424FB740B1039585177C003ADC824F26C07F58E31582023B1F6A9DE)

 
在执行页点击右上角“查看详情”按钮跳转到问题详情页，该页面实时展示检测设备已检测信息，包括累计问题数、检测项（包括检测中和待检测）。通过点击设备信息切换不同设备的检测信息详情。点击各检测项的“不通过数|通过数”对应值可查看该检测项详细检测结果。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/2OK_ONskRrSp0VZkH6Jh5g/zh-cn_image_0000002625539041.png?HW-CC-KV=V1&HW-CC-Date=20260701T025444Z&HW-CC-Expire=86400&HW-CC-Sign=E5180C7BA0807DF68C581DBBDC2D563F09E36BA412B1FED3819C16529CBD274F)

 

 
**测试报告**
 
测试完成后，自动生成测试报告。报告包含任务信息、测试结果、问题统计、检测规则。
 
任务信息中，可查看当前应用信息、任务执行时长，及详细的环境参数（配置信息及环境信息），支持导出html的报告文件。
 
测试概览中，包含测试总览、检测机型、结果统计及多设备对比，可直观查看本次任务中，测试项检测结果。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/FkNdLj5DSTmaqhiZhwbO8w/zh-cn_image_0000002591608282.png?HW-CC-KV=V1&HW-CC-Date=20260701T025444Z&HW-CC-Expire=86400&HW-CC-Sign=5CA7A0845E655BDD2F6ABD207BD63E77B7F90DAD054FD7FFA1E823AB44DFED29)

 
**测试总览信息解读：**
 
**问题详情****：**累计问题数
 
**视觉风格：**累计视觉风格问题数
 
**系统特性适配：**累计动效问题数
 
**界面布局****：**累计界面布局问题数
 
检测机型页面包含被测设备的基础信息、问题汇总和问题详情等信息。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/bzowpMz9TjeIKITPMP2bbg/zh-cn_image_0000002625490273.png?HW-CC-KV=V1&HW-CC-Date=20260701T025444Z&HW-CC-Expire=86400&HW-CC-Sign=9661B5DC71408FAB9C5786CFD00CD211EFB7F00BF67C3326D479E51BE652334A)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/PHC8Zb4-ThWT-GATX4YYxQ/zh-cn_image_0000002595211044.png?HW-CC-KV=V1&HW-CC-Date=20260701T025444Z&HW-CC-Expire=86400&HW-CC-Sign=79FECACBDE8B97732F07CC36F7D3A7DE2C8D4073C9E65764A084992C07E755D3)

 
检测不通过或检测异常的规则项，点击查看详情即可查看异常问题详情，包含检测项概览、测试截图、问题列表、详细的问题描述、问题等级和修复指南等信息。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/BOlhZui5TWSoioncUojH5A/zh-cn_image_0000002625491291.png?HW-CC-KV=V1&HW-CC-Date=20260701T025444Z&HW-CC-Expire=86400&HW-CC-Sign=E977130FA8313DC5BD930051F2377A276B3577F6A5F3212F195A1B0E670DB1B5)

 
多设备对比页用于展示同一页面在不同设备上的布局效果。当页面检测未通过时，图片下方将显示当前页面的问题详情。同时运行三个及以上设备时，即使某个设备未能匹配上，也会正常展示该页面数据，未匹配上设备显示为空白。
 
可根据问题描述针对性优化应用UX问题，参考资料：[UX体验标准](https://developer.huawei.com/consumer/cn/doc/design-guides/ux-guidelines-general-0000001760708152)。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/VdAI2WyRS1eXvbpFgDsJCA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260701T025444Z&HW-CC-Expire=86400&HW-CC-Sign=5A7B62F7B2A0E347123077443C9697ED637F32575B40B2EBFE568CB1D5E4B7A5)
 

更多测试服务详情，请前往DevEco Testing客户端->测试服务->UX测试->多设备布局对比测试->任务创建页->测试指南中查询。
