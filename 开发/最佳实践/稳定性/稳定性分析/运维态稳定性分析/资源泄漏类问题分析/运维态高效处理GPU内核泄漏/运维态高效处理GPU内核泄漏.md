# 运维态高效处理GPU内核泄漏

更新时间：2026-08-10 06:55:01

来源：https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-handling-gpu-kernel-leaks

#### 概述

GPU内核泄漏是常见的泄漏类型，也是应用稳定性优化的重点方向。本文档主要介绍在运维态下通过[APMS平台](https://developer.huawei.com/consumer/cn/doc/app/agc-help-apms-0000002235870062)进行GPU内核泄漏的监控、分析、定位与修复的完整处理方法。
 
 

#### 运维态GPU内核泄漏分析流程

 

#### 标准化排查流程

**整体流程图**
 
整体排查流程如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/s_ue3sWVQTmikLJgIHypoA/zh-cn_image_0000002671626374.png?HW-CC-KV=V1&HW-CC-Date=20260811T010220Z&HW-CC-Expire=86400&HW-CC-Sign=C99574D2789AD79469F5B0F0FD9969D10618129648CF9897BED2C4B1CADFAA87)

 
**排查步骤**
 1. [创建灰度任务](#section15567161021317)：在端侧集成应用灰度采集功能，通过云端平台发布应用灰度任务，圈选设备开启故障日志精准采集。
2. [APMS 故障预警](#section0763145018135)：在APMS平台配置内核泄漏监控告警规则，设置监控时段、频率和触发条件。
3. [问题查看与聚类](#section1182182471617)：通过APMS故障指标、APMS故障分析页面，可筛选GPU内核泄漏的问题，查看泄漏趋势图与TOP问题列表。
4. [根因定位与分析](#section161116262205)：通过分析故障模块、发生次数、影响设备数与最大泄漏数等关键信息，定位高优先级问题。查看问题详情，通过证据链与现场数据，深入分析泄漏原因。
5. [修复建议验证与闭环](#section1150784112617)：根据修复建议优化代码，并验证修复效果，形成闭环。
 
具体排查操作步骤可参考：[APMS平台GPU内核泄漏问题分析案例](#section9116152181116)。
 
 

#### 指标监控与关键信息提取

**查找内核泄漏关键问题**
 
进入故障分析页面，单击资源泄漏，在泄漏类型处选择MEMORY_LEAK/GPU_LEAK，单击查询后再单击TOP问题即可查看GPU_LEAK类型的问题数据。开发者可选择问题状态为未解决或者处理中的问题进行处理。同时，开发者应关注如下指标，进一步分析问题。关键指标说明如下：
 
- 故障模块：发生GPU内核泄漏的模块或组件，用于定位问题范围
- 发生次数（占比）：GPU内核泄漏发生的次数及占比，帮助判断问题出现的概率
- 影响设备数（占比）：受影响的设备数量及占比，评估设备层面的影响
- 最大泄漏数：GPU内核泄漏的内存大小

 
如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/QOuBCM7hSGGgAUAxuU4y3g/zh-cn_image_0000002701226099.png?HW-CC-KV=V1&HW-CC-Date=20260811T010220Z&HW-CC-Expire=86400&HW-CC-Sign=240561D8C7C30CD71355EDDC33D858A61992BC31A4CFCB08A9974CB6D316B102)

 
TOP问题列表根据最大泄漏数进行排序，开发者可单击查看按钮进入故障详情页查看问题的详细信息，进一步分析问题。
 
**提取故障详情页关键信息**
 
进入故障详情页后，需要重点关注问题详情页的以下信息：
 
- 泄漏趋势图表进入问题详情页后，单击下钻分析可设置筛选条件查看当前根因的GPU内核泄漏在不同时间、不同版本、不同设备维度的发生频率。例如，某次版本更新后该类泄漏量激增，可以提示新引入的问题。如下图所示：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/IkAdyjXTTSqnDRfjHLyjLg/zh-cn_image_0000002701346199.png?HW-CC-KV=V1&HW-CC-Date=20260811T010220Z&HW-CC-Expire=86400&HW-CC-Sign=B6F054D331B0FCFA9FA6342B0241107193F10F147C597689FBDAF5D3CEBCE0E4)

- 分析报告分析报告包括设备信息、系统版本、应用版本、ROM版本、前后台状态等，帮助开发者判断GPU内核泄漏发生的具体环境。如下图所示：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/OHb90p6CRcm9ZR8vOJ9tVA/zh-cn_image_0000002671466522.png?HW-CC-KV=V1&HW-CC-Date=20260811T010220Z&HW-CC-Expire=86400&HW-CC-Sign=D30FA6A84DFA6F5DA9FC8DEB7BD402F49DD2B605A771A3EE7FD8FED0EC05B093)

- 证据链开发者可以通过单击证据链查看主泄漏堆块、主泄漏方法以及分配栈信息，其中疑似泄漏点会高亮标注，帮助快速定位泄漏信息。如下图所示：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/JVuDWrmRQpyDWkqLSXiqyQ/zh-cn_image_0000002671626376.png?HW-CC-KV=V1&HW-CC-Date=20260811T010220Z&HW-CC-Expire=86400&HW-CC-Sign=418E56A25513FBCE97B325EE7294FF68116F611E8D5034E56A7B333EFFABBA27)

- 现场数据单击现场数据可查看GPU内核泄漏的具体泄漏类型、图片大小、图片数据量以及总泄漏大小。开发者可结合证据链中的堆栈信息，对比图片数据分析泄漏原因，从而定位具体泄漏位置。如下图所示：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/P5nq25LlRJOoynf9QiQu9Q/zh-cn_image_0000002701226101.png?HW-CC-KV=V1&HW-CC-Date=20260811T010220Z&HW-CC-Expire=86400&HW-CC-Sign=4DE8E9EF7E1548D38C138CC87C34324EBB13BFE87048E54D2DF934BAB02D4DE6)

- 采样栈还原堆栈通过上传.map或.so符号表文件，可将混淆后的堆栈地址还原为可读的代码行号与函数名。如下图所示：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/xCmbrLSvS5GsVHATZEakpA/zh-cn_image_0000002701346201.png?HW-CC-KV=V1&HW-CC-Date=20260811T010220Z&HW-CC-Expire=86400&HW-CC-Sign=2169F5A644C875C0C448285C93235F56CE8BA837368C0ACCECE1C8792E1DF19A)


 
 

#### APMS平台GPU内核泄漏问题分析案例

 

#### 创建灰度任务

应用灰度特性是一种运维态功能，用于精准采集故障日志。开发者在端侧集成[应用灰度采集](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiretrieval-intro)功能后，该应用可参与应用灰度活动。通过云端平台进行[灰度采集](https://developer.huawei.com/consumer/cn/doc/app/agc-help-apms-gray-scale-collect-0000002619401669)，可圈选部分设备开启故障日志精准采集，帮助开发者快速定位故障。
 
 

#### APMS 故障预警
1. **配置告警规则**
 
在故障预警平台的告警规则页面创建告警。根据实际业务情况，选择合适的监控时段、监控频率、告警触发条件等。平台将GPU_LEAK归属到MEMORY_LEAK，因此开发者在配置告警规则时指标类型需要选择MEMORY_LEAK。配置完告警规则后，平台才会触发告警。如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/CwspOxssQ56srfX3s_O_Wg/zh-cn_image_0000002671466524.png?HW-CC-KV=V1&HW-CC-Date=20260811T010220Z&HW-CC-Expire=86400&HW-CC-Sign=5BADA9055152EF7F81360693F5854FCF69EAA02B68AFF52C3CAF28873D801A4E)

 1. **查看告警**
 
配置告警规则后，当应用触发MEMORY_LEAK事件后设备会进行上报故障信息。APMS平台会开始收集后台数据，当满足告警触发条件后，会触发预警。收到预警后，单击查看可进入故障指标页面。如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/nO-QrLFATVe0Im1qxj_8vg/zh-cn_image_0000002671626378.png?HW-CC-KV=V1&HW-CC-Date=20260811T010220Z&HW-CC-Expire=86400&HW-CC-Sign=E1A8A0EF20C6AF6D4E5180F00704395E18FA3FE830C57C612D2D4A226C66F209)

 1. **查看故障数据**
 
查看故障数据的方式有两种，分别是通过故障指标页查看故障数据和通过故障分析页查看故障数据。
 
- 通过故障指标页查看故障数据故障指标页面包含了趋势分析，维度分布和TOP问题列表。开发者可以在界面选择GPU_LEAK泄漏类型并设置筛选条件，以过滤出GPU内核泄漏数据，从而进行个性化分析。TOP问题列表根据最大泄漏数进行排序，开发者可结合问题状态筛选需要优先处理的问题。如下图所示：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/DqELAFbCQWmRvO8tA_VDPA/zh-cn_image_0000002701226103.png?HW-CC-KV=V1&HW-CC-Date=20260811T010220Z&HW-CC-Expire=86400&HW-CC-Sign=C1B877F2F78D1A563F9F9857A5632B8CE916F20C73A82566E2F90B3FB3FDBACC)

- 通过故障分析页查看故障数据开发者也可以直接单击故障分析页面，经过条件筛选后可查看具体的TOP问题列表。如下图所示：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/HHucO04RTZ6VtKqw6hicHQ/zh-cn_image_0000002701346203.png?HW-CC-KV=V1&HW-CC-Date=20260811T010220Z&HW-CC-Expire=86400&HW-CC-Sign=FCBBBDC17EA554176EC18E4D47705C8F3F028A40973CE144A3E7151028FCD172)


 
 

#### 问题查看与聚类

**聚类规则说明**
 
相同特征ID：平台会将GPU内核泄漏的数据根据相同故障模块聚合成一条记录，生成问题特征ID。
 
**TOP问题查看**
 
筛选GPU内核泄漏问题范围：在界面可以设置不同的筛选条件对GPU内核泄漏问题进行个性化分析。筛选条件设置完成后单击“查询”，即可查看指定时间范围和条件下的三类指标数据的变化趋势，包括泄漏率、泄漏次数、泄漏设备数。如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/uszS903FTl2WoDDlXuC06g/zh-cn_image_0000002671466528.png?HW-CC-KV=V1&HW-CC-Date=20260811T010220Z&HW-CC-Expire=86400&HW-CC-Sign=FEC885A48FDBF2CD612CE8C298AA7A1FA26634ADA5F20F86E9196416BDBC8732)

 
**TOP根因聚类**
 
完成筛选后，开发者可进一步查看TOP问题列表，在问题列表中，每个问题都是同一类问题的汇总。APMS平台会将具有相同特征ID的问题聚合成一个，并按照发生次数进行排序，开发者可高优先级处理TOP问题。单击“查看”进入问题详情页，进一步查看问题详情。如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/3OZ9dZXSQCCNS7GtX5mWuw/zh-cn_image_0000002671626380.png?HW-CC-KV=V1&HW-CC-Date=20260811T010220Z&HW-CC-Expire=86400&HW-CC-Sign=75BEF3368240A90A5D2A00EC797617747500A830D61B241115A865A32739148A)

 
 

#### 根因定位与分析

单击资源泄漏信息详情列表某个问题进入详情页后，开发者可按照如下步骤定位问题根因。
 
**基础定位信息分析**
 1. 查看问题概要：问题概要会展示问题的核心身份信息，包括问题特征ID、故障原因、故障模块，帮助开发者快速判断GPU内核泄漏的基本属性。如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/b8Oed2u6QnCIS-98Mql6iQ/zh-cn_image_0000002701226107.png?HW-CC-KV=V1&HW-CC-Date=20260811T010220Z&HW-CC-Expire=86400&HW-CC-Sign=00CF380F32D673BA2665163A4A1BA565C89847D1B68091C4FD5CF7983341FD11)

 1. 查看分析报告：分析报告会提供问题发生时的完整上下文，包括环境信息（设备型号、系统版本、ROM版本、前后台状态等）、堆栈信息、日志文件，并基于分析结果给出修复建议，辅助开发者高效完成问题排查与闭环。如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/xWTPgC3IQjmgOTiW3sk0yg/zh-cn_image_0000002701346205.png?HW-CC-KV=V1&HW-CC-Date=20260811T010220Z&HW-CC-Expire=86400&HW-CC-Sign=5E7AA11ECC13D4A8B85A715FB057856718E5F7B3360DE60C8CCD05F47D541BE9)

 1. 查看故障详情：开发者可根据平台给出的修复建议定位代码问题，完成问题修复。如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/ab_bCjVSSFOBmWKVLAK7Vw/zh-cn_image_0000002671466530.png?HW-CC-KV=V1&HW-CC-Date=20260811T010220Z&HW-CC-Expire=86400&HW-CC-Sign=9FDF6947FEABCF4270E2DD3FBABFAAB6E9177BEC916E8C40E06662FE46F685B8)

 1. 查看证据链：开发者可以通过证据链查看主泄漏堆块、主泄漏方法以及分配栈信息，其中疑似泄漏点会高亮标注。开发者可结合分配栈中的方法信息定位到业务代码中的泄漏处。如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/lkwfN-X5SsquWqhH-aQzjg/zh-cn_image_0000002671626382.png?HW-CC-KV=V1&HW-CC-Date=20260811T010220Z&HW-CC-Expire=86400&HW-CC-Sign=34C06AFBA0FAEF88C093933226AC7D078A6C3BD3E1248B6F94552713C25F13EA)

 1. 查看现场数据：现场数据展示了GPU内核泄漏的具体泄漏类型、图片大小、图片数据量以及总泄漏大小。开发者可结合证据链中的堆栈信息，对比图片数据分析泄漏原因，从而定位具体泄漏位置。如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/0fV_hYUgTLCuuHIvaLJmkg/zh-cn_image_0000002701226109.png?HW-CC-KV=V1&HW-CC-Date=20260811T010220Z&HW-CC-Expire=86400&HW-CC-Sign=E400E01EF71E546FB4C1F6F155D444851CC7921AD71E64D9AB74C43F5C96CB48)

 1. 查看采样栈信息：通过上传SourceMap或.so符号表文件，可将混淆后的堆栈地址还原为可读的代码行号与函数名。如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/6qOTDBNHS02hi5ryvSdwiA/zh-cn_image_0000002701346207.png?HW-CC-KV=V1&HW-CC-Date=20260811T010220Z&HW-CC-Expire=86400&HW-CC-Sign=8E22B809AEFA01EA3F76B4537498DA94E5E2099FEAD84790D166B2B2AD6EAD14)

 
**下钻分析**
 
下钻分析的核心逻辑是从一个汇总的指标或表象问题出发，将其拆分成多个组成部分。然后筛选出最关键的线索继续向下拆分，不断重复这个过程，直到定位到具体的根因。平台会根据故障特征ID进行聚类并筛选TOP应用版本、系统版本以及设备型号。开发者可根据此重点关注问题高发的版本及设备，更精确地定位问题。如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/gB--ed8IS4e_SuBKqOw0Mw/zh-cn_image_0000002671466532.png?HW-CC-KV=V1&HW-CC-Date=20260811T010220Z&HW-CC-Expire=86400&HW-CC-Sign=E9CC6E412599AE1294CB2C968732F88938C61E62E4E03431247C41038F95B74B)

 
 

#### 修复建议验证与闭环

**修复建议**
 
故障详情页面会给到修复建议，开发者可以通过给出的建议优化代码。如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/xO39f6gSRiu35a0GA0bc8A/zh-cn_image_0000002671626384.png?HW-CC-KV=V1&HW-CC-Date=20260811T010220Z&HW-CC-Expire=86400&HW-CC-Sign=021815375B6825640F0D84E5B22003851D94B3BCD14690ABF925909F60659AC3)

 
**修复建议与闭环**
 1. 修改问题之后，可以在分析页面的问题列表中，将对应的问题处标记已修改，并关注新版本的GPU内核泄漏数据。
2. 应用发布后，可在故障分析页面筛选新版本数据和旧版本数据，对比修复前后的泄漏率，确认修复是否有效。如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/ii-mlkroSI6sO-52NoaOyw/zh-cn_image_0000002701226111.png?HW-CC-KV=V1&HW-CC-Date=20260811T010220Z&HW-CC-Expire=86400&HW-CC-Sign=5B586C8635FFA7970A7DEF8C76FD316AEFE60523842911EF6F760ADA70E00F0D)

 
 

#### 基于Operation Analyzer平台分析

 
Operation Analyzer平台是指DevEco Studio的Operation Analyzer插件。在DevEco Studio上可以通过此插件查看到应用对应的故障数据，数据和APMS平台上一致。
 
**Operation Analyzer平台入口**
 
打开DevEco Studio后，在左侧可看到Operation Analyzer图标，单击后选择应用，再单击资源泄漏，查看GPU_LEAK类型的数据。如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/ZxK4GN28ShuG-Gr4JZQxWg/zh-cn_image_0000002701346209.png?HW-CC-KV=V1&HW-CC-Date=20260811T010220Z&HW-CC-Expire=86400&HW-CC-Sign=874E56AEB65C4ADD7BD35D13913A64A2E5331FD6FD45127FD8E6ADD237A51CE2)

 
如果左侧没有出现Operation Analyzer平台图标，也可通过上方导航栏的视图窗口进入。如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/b6rQJIAtSo2H2OSwqORNtQ/zh-cn_image_0000002671466534.png?HW-CC-KV=V1&HW-CC-Date=20260811T010220Z&HW-CC-Expire=86400&HW-CC-Sign=38A218B66122A20EF68EEBEAFF440EE3C022D34564EC891AD6BFF31E19ECCA2A)

 
**问题分析**
 
- Operation Analyzer平台问题查看

 
开发者可自定义筛选条件，筛选需要查看的问题，单击TOP Issues，选择下方类型为GPU_LEAK的数据，单击即可查看当前GPU内核泄漏问题的详细信息。如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/Mc9bVBacQxymp-6cHyT0Dg/zh-cn_image_0000002671626386.png?HW-CC-KV=V1&HW-CC-Date=20260811T010220Z&HW-CC-Expire=86400&HW-CC-Sign=E2431A4B0BAED060A484F0D347C59CB77966787A9302129547704B78AD70FF4C)

 
平台的问题详情页同APMS平台功能相同，开发者可参考修复建议进行修复。如果修复建议不能支撑解决，可进一步查看证据链、现场数据进行具体分析。如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/NC0yQRfaQ3SNRBwp7IIPjA/zh-cn_image_0000002701226115.png?HW-CC-KV=V1&HW-CC-Date=20260811T010220Z&HW-CC-Expire=86400&HW-CC-Sign=D1392AFE917057D393A62C1C9D1B36057C3DAD7965397ED0D988E3A09677926F)

 
开发者也可以查看问题分布图表，定位问题高发的应用版本、设备型号与系统版本，辅助进一步分析。如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/-_uGejznTwGlntGe1WE0VA/zh-cn_image_0000002701346211.png?HW-CC-KV=V1&HW-CC-Date=20260811T010220Z&HW-CC-Expire=86400&HW-CC-Sign=F05166529899031FA9AD13130D6032DCECF3CF235F8C89278A2F14B741127A4D)

 
- Operation Analyzer关联离线符号表

 
Operation Analyzer平台提供了堆栈还原的能力，可以通过上传符号表（.so/.map/.json文件）完成堆栈还原，辅助分析问题。
 
选择本地符号表，如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/ARvqtcgAT_uiykjP-jU8PQ/zh-cn_image_0000002671466538.png?HW-CC-KV=V1&HW-CC-Date=20260811T010220Z&HW-CC-Expire=86400&HW-CC-Sign=D5B878ADBBF44EA95020F4437820282990A13895279A84AA3F9EE5C03DBAA4A9)

 
完成堆栈还原，如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/YszKRRH-THmFJuNycAqkSQ/zh-cn_image_0000002671626390.png?HW-CC-KV=V1&HW-CC-Date=20260811T010220Z&HW-CC-Expire=86400&HW-CC-Sign=5C4D694F1885203EA2AD725ADD4E53FFE71F5702B3BD83A53288FABC1F734544)

 
- Operation Analyzer关联代码

 
堆栈还原后，Operation Analyzer平台可将故障处与项目代码相关联，单击故障处可跳转到对应源码中，可辅助开发者更高效地定位问题。
 
关联项目代码，如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/qzHchRsLSWWLQRI5maqD9w/zh-cn_image_0000002701226117.png?HW-CC-KV=V1&HW-CC-Date=20260811T010220Z&HW-CC-Expire=86400&HW-CC-Sign=72ECE2B2E1FC4263BE765328C48F56CFE4BDCB7943F3CF44871975159B19CA20)

 
关联效果确认，如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/XoONMhKlTrWsWlg8ufzutg/zh-cn_image_0000002701346213.png?HW-CC-KV=V1&HW-CC-Date=20260811T010220Z&HW-CC-Expire=86400&HW-CC-Sign=D407BB9D7BD06EA779103CDFECC7D0F5F9E7126C22F771D5FDD8A443F555980F)

 
**问题修复**
 
Operation Analyzer平台会给出故障分析与修复建议，开发者可根据修复建议修复问题代码。如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/XTrTZ5uBRIWj-X8ykzxuTw/zh-cn_image_0000002671466544.png?HW-CC-KV=V1&HW-CC-Date=20260811T010220Z&HW-CC-Expire=86400&HW-CC-Sign=38AA7BA2654D3C41522649679754D8F555E9F4285799DDB1441759A7DA61BAF6)
