# 运维态高效处理Native泄漏

更新时间：2026-07-22 06:05:01

来源：https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-native-leak-in-operation

#### 概述

Native内存泄漏是一种常见的泄漏类型。本文档主要介绍在运维态下如何利用[APMS](https://developer.huawei.com/consumer/cn/doc/app/agc-help-apms-0000002235870062)平台完成Native内存泄漏的监控、分析、定位及修复全流程。
 
 

#### 运维态Native泄漏分析流程

 

#### 标准化排查流程

排查流程如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/TcQ9kEC0Ta2-7-_jUdlqcg/zh-cn_image_0000002645091436.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=0BE6CAA6E1682411C5111EB1250764E20E10C392739F875283F0380A9286DECD)

 
**排查步骤**
 1. APMS故障预警配置：在APMS平台配置Native泄漏监控告警规则，设置监控时段、频率和触发条件。
2. 问题查看与聚类：通过故障预警或主动分析页面，筛选PSS_MEMORY和RSS_LEAK类型的泄漏问题，查看Native泄漏趋势与TOP问题列表。
3. 根因定位与分析：分析故障模块、发生次数、影响设备数等关键信息，定位高优先级问题。查看问题详情，通过证据链、分配栈信息和符号表还原堆栈，深入分析泄漏原因。
4. 修复与验证闭环：根据修复建议优化代码，并验证修复效果，形成闭环。
 
具体排查操作步骤可参考：[APMS平台Native泄漏分析案例](#section14745785205)。
 
 

#### 指标监控与关键信息提取

**Native泄漏监控信息详情**
 
在故障分析页面中，APMS基于堆栈关键行对同类异常进行精准汇聚，将具有相同泄漏根因和主泄漏方法的异常报告自动聚合成同一类问题，并按照发生占比排序。开发者可查看应用的TOP问题列表，结合业务对问题进行描述，标记优先级与问题状态，高优先处理未修复的高优先级问题。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/JRXTgO8GQfOuIj2GMAMj3w/zh-cn_image_0000002644931526.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=FEC8A416F8391F606E416F84A1F9B72FF63C8C604B4922B5FE87EE37F74F463D)

 
**关键指标说明**
 
 
- 故障模块：发生泄漏的模块或组件，用于定位问题范围。
- 发生次数（占比）：泄漏问题发生的频率，帮助判断问题严重程度。
- 影响设备数（占比）：受影响的设备数量，评估问题影响面。

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/niqw9hESTjuAnMGgQG48mA/zh-cn_image_0000002675091233.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=A7EC2EE2D129A4AE304AB2BD76792F86EFC5099D946B494434AD118C6B9F115A)

 
**故障详情页关键信息提取**
 
故障详情页面可以通过证据链和堆栈信息进一步分析泄漏的原因。
 
- 证据链根据泄漏堆块的分配内存大小区分主次泄漏堆块。展示主次可疑泄漏方法详情以及对应的修复建议。排查优先从主泄漏堆块切入，核查主泄漏方法是否存在异常。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/FlfT33YST7yykWDbeI2Ptw/zh-cn_image_0000002675011391.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=3DD6C3893E0E36862BEECDE68842722880DD5345650E9A3EB0CC7AB751686123)

- 分配栈信息展示当前选中的泄漏堆块和泄漏方法对应的堆栈信息。通过堆栈分配详情、堆栈树分配和火焰树三种不同的形式展现，以便开发者更直观更便捷地查看分配栈信息。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/83YN4kiNSqWeHHjDxfrvpg/zh-cn_image_0000002645091438.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=6A37BA8D8052095A4EF012E960666A914EBC00FA20490ED62210D88184767264)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/rLI0rGFmRyqGcGqUz9tJyw/zh-cn_image_0000002644931528.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=3F8673EE2A62BF8C45F05464D674B126F5DBBE0E23E7E9569C2DC01E0065B9A0)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/GtngmJQPQUKE76BzlVaBnw/zh-cn_image_0000002675091235.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=152B368A91C01E80011EECB02D65A98AF3ED5C6502DFA1E95F19C1C3EF452F47)

- 还原堆栈（符号表上传）通过上传SourceMap或.so符号表文件，可将混淆后的堆栈地址还原为可读的代码行号与函数名。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/YOuUGgJQS82gOYVOe1Ck8Q/zh-cn_image_0000002675011393.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=F01950C7C839FAD462B47C01D3DF732D36A0B7D134E5A589B4FE3802AF398E83)


 

#### APMS平台Native泄漏分析案例

 

#### 灰度任务创建

应用灰度特性是一种运维态功能，用于精准采集故障日志。开发者在端侧集成[应用灰度采集](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiretrieval-intro)功能后，该应用可参与应用灰度活动。通过云端平台进行[灰度采集](https://developer.huawei.com/consumer/cn/doc/app/agc-help-apms-gray-scale-collect-0000002619401669)，可圈选部分设备开启故障日志精准采集，帮助开发者快速定位故障。
 
 

#### APMS故障预警

可以在故障预警平台的告警规则页面，新建告警任务。结合实际业务场景，选择合适的监控时段、监控频率、告警触发条件及其他告警指标，其中Native泄漏对应的指标类型为MEMORY_LEAK。
 
建议配置以下告警规则：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/43n9R4tESKSIMW41UChPwg/zh-cn_image_0000002645091440.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=763E877B2CB7E69C94F3C44D8315DCF9E910F1CA37AD773CD3A9792252126CCB)

 
配置告警规则后，当应用触发Native泄漏事件，设备会上报故障信息。系统开始收集后台数据，满足告警触发条件后，系统将发出预警。可参照下图步骤查看故障告警：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/Xt4U7r9BQMK7O2B6RMmjvw/zh-cn_image_0000002644931530.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=9187EF003841FD300E7C8B0CC8F20A00E8D4DCB363D07E94B50F2B5C59595529)

 
收到预警后，可点击“查看”进入故障指标页面。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/IhbyzcRjQ9qK80i85B3_lA/zh-cn_image_0000002675091237.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=C5C82F8902D97708030F519FA1D41E5F31F6CBBD4AAF8CD1E64C9B897D65A287)

 
故障指标页面包含趋势分析、维度分布和TOP问题列表。开发者可以在界面设置不同的筛选条件对冻屏问题进行个性化分析。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/nFswnB5AQ9iauxa9-CzOag/zh-cn_image_0000002675011395.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=A71966D04B1FD108A53A423CAF8AB83ED1BD5C86CABF34C54294EB9494CC5F4F)

 
点击TOP问题列表中的查看，可以进入问题详情页查看问题详情，进一步分析。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/AexZhIbiT_ion_uC_Y75qg/zh-cn_image_0000002645091442.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=63BF89D75E9D8D3B7EBD3771E514A1010741BFBAA83CBE9E55FC5D322704BC92)

 
开发者也可直接点击故障分析页面，通过条件筛选查看具体的TOP问题列表，点击查询按钮进入问题详情页进行进一步分析。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/mGMajfx8R3O3Nopq0joMjw/zh-cn_image_0000002644931532.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=D18846815402DC00ED849D9763947070CB1EF2584E8E69BE788DE816CDC3077D)

 
 

#### 问题查看与聚类

**聚类规则说明**
 
平台根据以下规则进行问题聚类：
 
- 相同特征ID：将具有相同特征ID的问题聚合在一起。

 
**TOP根因聚类**
 
在问题列表中，每个问题都是同一类问题的汇总。APMS基于堆栈关键行进行准确的同类异常汇聚，将具有相同或相似泄漏堆栈的异常报告自动聚合成一个问题。开发者可点击“查看”进入问题详情页查看详情。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/2ePO_884SSeaajywduStzw/zh-cn_image_0000002675091239.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=A00F0DA67A2AAA6829918EF1D7A0C02D129470F695DE781B45FA1274094303E8)

 
 

#### 根因定位与分析

**基础信息定位**
 
点击问题列表中的某个问题进入详情页后，APMS 将提供以下核心分析信息，帮助开发者高效定位根因。
 
问题概要：展示问题的核心身份信息，包括故障类型、故障模块，帮助开发者快速判断崩溃的基本属性。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/sLrPka8FQDiXqyEVy1udew/zh-cn_image_0000002675011397.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=450417ADBFC62D5CBFCD30EF789F93C4E1B4D3097FFC41E906C357C4AFA9B56B)

 
聚类数据：基于堆栈关键行和过滤筛选跳转聚类同类故障，帮助开发者评估问题的影响范围与严重程度。
 
分析报告：提供问题发生时的完整上下文，包括环境信息（设备型号、系统版本、ROM版本、前后台状态等）、堆栈信息、日志文件，并基于分析结果给出修复建议，辅助开发者高效完成问题排查与闭环。此处demo展示的故障模块是leak_thread。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/WrP11CZhRKORotSR1XpsYw/zh-cn_image_0000002645091444.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=2220C5A8005A6E8602C8648E223B7F60D75453A46B93E4FCB50B26CDF8A1735A)

 
**证据链分析**
 
证据链展示主泄漏和次泄漏具体方法位置。开发者可根据平台解析出的泄漏堆栈和故障原因，参照优化建议定位问题代码，完成修复与验证。
 
根据故障详情分析得出：可以看出规格为4096B的堆块为核心泄漏堆块，libanon.so为核心泄漏库，leak thread为核心泄漏方法。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/riWeTxgzSx-y3sAZt02KxA/zh-cn_image_0000002644931534.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=E7A96D6B681A7DC0360B201BDB4D9D347529EFF2E8A02860CD225BEFBCE0E69C)

 
堆栈信息分析：三种形式（堆栈分配详情、堆栈树分配和火焰树）用于查看方法调用关系和疑似泄漏故障处。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/BvGSHgFCRvmcPuoQ3luhxw/zh-cn_image_0000002675091241.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=9E99FE4C04F426431BC3AB6B611C04BA12C58FC652EC8780D192B3159B114368)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/b8mZwipDQvuljIlp6-IXdg/zh-cn_image_0000002675011401.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=F33A853B839B150B70CC6299CC6C0F4F50734CFF2D3579F2DA17B5470AA8B4B1)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/w20XAu6MQje8Yv9104dTyQ/zh-cn_image_0000002645091446.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=95E2C14FC3304A2CD43D2E525BF89381680308147613FFFB11F1803C25B9074A)

 
**下钻分析**
 
下钻分析的核心逻辑是从一个汇总的指标或表象问题出发，将其拆分成多个组成部分，然后挑出最关键的线索继续向下拆分，不断重复这个过程，直到定位到具体的根因。平台会根据故障特征ID进行聚类并筛选TOP应用版本，系统版本以及设备型号。开发者可根据此重点关注问题高发的版本及设备，更精确的定位问题。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/4Sx5Wkm_Remff-xDnjNWcw/zh-cn_image_0000002644931536.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=7EF48921D53C1A4FE5BE8658803A3E7EE91CCA175A77FFB9D2856B2EC6EB945E)

 
 

#### 修复与验证闭环

**修复建议**
 
故障详情页面会提供修复建议，开发者可根据建议优化代码。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/kfz2MMr8QzSruxpli4i9wg/zh-cn_image_0000002675091245.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=3628DE56B10CFF67F5AF9932029F44A543B8C837479954BD6B2869A25878B265)

 
**修复建议与闭环**
 1. 修改问题之后，可以在分析页面对应的泄漏对象标记已修改，并关注新版本的崩溃数据。
2. 对比修复前后的问题发生率，确认修复是否有效。
 
**故障模式库**
 
故障模式库中会收录常见的Native泄漏事件，针对不同的Native泄漏事件提供最佳实践和修复方案，并且还会提供案例库、收录Native泄漏问题案例和解决过程。开发者可以根据故障匹配到对应的案例，更方便高效的优化问题。
 
 

#### 基于Operation Analyzer平台分析

Operation Analyzer是DevEco Studio的插件，通过该插件可查看应用故障数据，数据与APMS平台一致。
 
 

#### Operation Analyzer平台入口

打开DevEco Studio后，在左侧可看到Operation Analyzer图标，点击后选择应用，再点击资源泄漏即可查看该类故障数据。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/4fxL_NY-SrGs6YQ-KCpSRg/zh-cn_image_0000002675011403.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=96BF8DF6949D87B1EAA2747F1B85DA38E214A4A25EBF5FEE314ED72DFE503BF4)

 
 

#### 问题分析

**Operation Analyzer平台问题查看**
 
开发者可自定义筛选条件筛选需要查看的问题，可点击功能列表下具体的问题进一步查看问题详情。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/9O5UKho7QyGtlajFJVdyQw/zh-cn_image_0000002645091448.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=1F9D3869EA10D066B145A2571823A34EB850E43B33C1C1C6A25B6A073852FAD7)

 
 
**Operation Analyzer平台问题详情**
 
平台的问题详情页同APMS平台功能相同，开发者可查看故障分析与修复建议排查问题。如果修复建议不能支撑解决问题，可进一步查看证据链、现场数据进行具体分析，符号表页签支持上传符号表，还原堆栈信息。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/l51X8uCgRFqoOrYMOlG-lw/zh-cn_image_0000002644931538.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=4F7786212414CC4007B55453862F4C6BC4DEA7E97DEF372F73830D83FB107985)

 
开发者也可以查看问题分布图表，定位问题高发的应用版本、设备型号与系统版本，辅助进一步分析。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/tOQQYtczRK2IibJFECYbdg/zh-cn_image_0000002675091247.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=43064009473BA0B8D9911C0E6D5D4DD056A20B200937567CA40A79312A42498C)

 
**Operation Analyzer关联离线符号表**
 
Operation Analyzer平台提供了堆栈还原的能力，可以通过上传符号表（.so/.map/.json文件）完成堆栈还原，辅助分析问题。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/UuWA0glMSPm_6QD_tI9riw/zh-cn_image_0000002675011405.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=76F05AD819686DEF88F038C64B697185F4C3342DC393CA0CEA5745FC86FDE105)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/p4C9LCbpSdaXVX9lpOel_g/zh-cn_image_0000002645091450.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=6570DFC89E3A4F03B4B685D62B94409034EFD0E36536D7DAA30D5F38FE1972D1)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/MWEA_dUPQzGH7RuXXOqDCg/zh-cn_image_0000002644931540.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=3D652CC106A74E9FA092F5E0C9D07B433AD78179653545462D678C1F32878051)

 
**Operation Analyzer关联代码**
 
堆栈还原后，Operation Analyzer平台可将故障处与项目代码相关联，点击故障处可跳转到对应源码中，可辅助开发者更高效的定位问题。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/tRQ91LMWRC6XyNDbN0PuSA/zh-cn_image_0000002675091249.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=7706A1740AFDD3A824728BA86802BFE11B1CCE54F35B799F1EF9E9AC7B94601E)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/4i9Gt6mfTQmOYwfX9LbBzw/zh-cn_image_0000002675011407.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=E5E3D0F6C722AF768E7CDA35A8113EBE7216050D60F2ADA81070B6CC0F675412)

 

#### 问题修复

Operation Analyzer平台会给出泄漏堆块、泄漏函数与修复建议，开发者可根据修复建议修复问题代码。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/rfQbd3TsSduMugXM6x_9qA/zh-cn_image_0000002645091452.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=C6987DB5EF12E524064306CE160EE3C05AF777764DDCE2938B672100CCBF38EA)
