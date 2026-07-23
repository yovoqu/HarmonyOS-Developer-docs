# 运维态高效处理Native泄漏

更新时间：2026-07-22 06:05:01

来源：https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-native-leak-in-operation

#### 概述

Native内存泄漏是一种常见的泄漏类型。本文档主要介绍在运维态下如何利用[APMS](https://developer.huawei.com/consumer/cn/doc/app/agc-help-apms-0000002235870062)平台完成Native内存泄漏的监控、分析、定位及修复全流程。
 
 

#### 运维态Native泄漏分析流程

 

#### 标准化排查流程

排查流程如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/xwB24EUfRkm-rpVRnZP8zA/zh-cn_image_0000002645091436.png?HW-CC-KV=V1&HW-CC-Date=20260723T014110Z&HW-CC-Expire=86400&HW-CC-Sign=3E03DB25CEF71D8788A5768382F0D4F1850B529174BD8251909CD9B5C5DD8768)

 
**排查步骤**
 1. APMS故障预警配置：在APMS平台配置Native泄漏监控告警规则，设置监控时段、频率和触发条件。
2. 问题查看与聚类：通过故障预警或主动分析页面，筛选PSS_MEMORY和RSS_LEAK类型的泄漏问题，查看Native泄漏趋势与TOP问题列表。
3. 根因定位与分析：分析故障模块、发生次数、影响设备数等关键信息，定位高优先级问题。查看问题详情，通过证据链、分配栈信息和符号表还原堆栈，深入分析泄漏原因。
4. 修复与验证闭环：根据修复建议优化代码，并验证修复效果，形成闭环。
 
具体排查操作步骤可参考：[APMS平台Native泄漏分析案例](#section14745785205)。
 
 

#### 指标监控与关键信息提取

**Native泄漏监控信息详情**
 
在故障分析页面中，APMS基于堆栈关键行对同类异常进行精准汇聚，将具有相同泄漏根因和主泄漏方法的异常报告自动聚合成同一类问题，并按照发生占比排序。开发者可查看应用的TOP问题列表，结合业务对问题进行描述，标记优先级与问题状态，高优先处理未修复的高优先级问题。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/6o3dESa8QUez_VOuMRpnVQ/zh-cn_image_0000002644931526.png?HW-CC-KV=V1&HW-CC-Date=20260723T014110Z&HW-CC-Expire=86400&HW-CC-Sign=E67FCF1D3C357AB6BBDEA8D621701BF53DE11557DE4D2AA6332683FDF8CF656B)

 
**关键指标说明**
 
 
- 故障模块：发生泄漏的模块或组件，用于定位问题范围。
- 发生次数（占比）：泄漏问题发生的频率，帮助判断问题严重程度。
- 影响设备数（占比）：受影响的设备数量，评估问题影响面。

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/tv4L5Vk_SHyhiDHZDVARww/zh-cn_image_0000002675091233.png?HW-CC-KV=V1&HW-CC-Date=20260723T014110Z&HW-CC-Expire=86400&HW-CC-Sign=F87C5F09DECBFF76991FD0CB5A10D7C57459850E810D13FF66F6E9F89122A7F9)

 
**故障详情页关键信息提取**
 
故障详情页面可以通过证据链和堆栈信息进一步分析泄漏的原因。
 
- 证据链根据泄漏堆块的分配内存大小区分主次泄漏堆块。展示主次可疑泄漏方法详情以及对应的修复建议。排查优先从主泄漏堆块切入，核查主泄漏方法是否存在异常。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/X6pNT_uhQ32GlxNcmf9vNQ/zh-cn_image_0000002675011391.png?HW-CC-KV=V1&HW-CC-Date=20260723T014110Z&HW-CC-Expire=86400&HW-CC-Sign=4BEDC4D3FF4507B5502EBFFBD78CBD36C053F7B884C60D99832910CF949F681C)

- 分配栈信息展示当前选中的泄漏堆块和泄漏方法对应的堆栈信息。通过堆栈分配详情、堆栈树分配和火焰树三种不同的形式展现，以便开发者更直观更便捷地查看分配栈信息。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/rrcVfqluQTqdoZh6bTO6WA/zh-cn_image_0000002645091438.png?HW-CC-KV=V1&HW-CC-Date=20260723T014110Z&HW-CC-Expire=86400&HW-CC-Sign=0765D7120BF81AF8BD14917034D37DD4E14B7696357110CDE545D3F99F27C511)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/3S2Csw40RY6L7DKR0DLONg/zh-cn_image_0000002644931528.png?HW-CC-KV=V1&HW-CC-Date=20260723T014110Z&HW-CC-Expire=86400&HW-CC-Sign=869B9739FB0D4E2D96A2E65027719AE60C0F41E5398FF0EE13689CFBDF58A518)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/GYiIBopFRpKThV3cd-p9eA/zh-cn_image_0000002675091235.png?HW-CC-KV=V1&HW-CC-Date=20260723T014110Z&HW-CC-Expire=86400&HW-CC-Sign=C14E4305E2685D28E950FDD136F471710F40E67ACC7BAFA3037DB4BE5AAF63F3)

- 还原堆栈（符号表上传）通过上传SourceMap或.so符号表文件，可将混淆后的堆栈地址还原为可读的代码行号与函数名。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/lsWKgw8TSKyu5YwSjjFeDg/zh-cn_image_0000002675011393.png?HW-CC-KV=V1&HW-CC-Date=20260723T014110Z&HW-CC-Expire=86400&HW-CC-Sign=F29B9550144D8F0521D7C4AE136891686B580AAD249177DCF345A1C57AD73C36)


 

#### APMS平台Native泄漏分析案例

 

#### 灰度任务创建

应用灰度特性是一种运维态功能，用于精准采集故障日志。开发者在端侧集成[应用灰度采集](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiretrieval-intro)功能后，该应用可参与应用灰度活动。通过云端平台进行[灰度采集](https://developer.huawei.com/consumer/cn/doc/app/agc-help-apms-gray-scale-collect-0000002619401669)，可圈选部分设备开启故障日志精准采集，帮助开发者快速定位故障。
 
 

#### APMS故障预警

可以在故障预警平台的告警规则页面，新建告警任务。结合实际业务场景，选择合适的监控时段、监控频率、告警触发条件及其他告警指标，其中Native泄漏对应的指标类型为MEMORY_LEAK。
 
建议配置以下告警规则：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/yzytE_1JRhyUN2XahAtJ9w/zh-cn_image_0000002645091440.png?HW-CC-KV=V1&HW-CC-Date=20260723T014110Z&HW-CC-Expire=86400&HW-CC-Sign=2F1547198D7C83FCD929CFF41862BB47F7CE808E97772D99DB702EFCCAEB67B8)

 
配置告警规则后，当应用触发Native泄漏事件，设备会上报故障信息。系统开始收集后台数据，满足告警触发条件后，系统将发出预警。可参照下图步骤查看故障告警：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/yOjzXcZpQsKh_uRpvmUn1w/zh-cn_image_0000002644931530.png?HW-CC-KV=V1&HW-CC-Date=20260723T014110Z&HW-CC-Expire=86400&HW-CC-Sign=D9F43749D3C2E81FDC4D058582A37053F83D2C5ED989CF95499E1826FEAB2461)

 
收到预警后，可点击“查看”进入故障指标页面。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/WPlUtM9XRaiIA5-gAZYVrw/zh-cn_image_0000002675091237.png?HW-CC-KV=V1&HW-CC-Date=20260723T014110Z&HW-CC-Expire=86400&HW-CC-Sign=7A97159C06BF1EEEA6C7D53713DAB568DC26E19AD5202D25B7C5E8E1301ABF6B)

 
故障指标页面包含趋势分析、维度分布和TOP问题列表。开发者可以在界面设置不同的筛选条件对冻屏问题进行个性化分析。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/B19gl5-7QVOL1WNSI5H2Vg/zh-cn_image_0000002675011395.png?HW-CC-KV=V1&HW-CC-Date=20260723T014110Z&HW-CC-Expire=86400&HW-CC-Sign=02E3846CF90BF8CB609A339FBDBA5E1E615E98B5D452F5CE5ADAD9B6BAE69F4F)

 
点击TOP问题列表中的查看，可以进入问题详情页查看问题详情，进一步分析。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/7toPmu05SBCYLPvYnR6hqw/zh-cn_image_0000002645091442.png?HW-CC-KV=V1&HW-CC-Date=20260723T014110Z&HW-CC-Expire=86400&HW-CC-Sign=3AC0AE4134EE889513359140A5382E0EE343FB67518C14BB1381075A1828A211)

 
开发者也可直接点击故障分析页面，通过条件筛选查看具体的TOP问题列表，点击查询按钮进入问题详情页进行进一步分析。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/N4CgGwEkSr6E5C3L8pOWKA/zh-cn_image_0000002644931532.png?HW-CC-KV=V1&HW-CC-Date=20260723T014110Z&HW-CC-Expire=86400&HW-CC-Sign=13AA666D7091C0A509B5B072F84ECBD476139613F99A46C1BACD01C85BAE5F75)

 
 

#### 问题查看与聚类

**聚类规则说明**
 
平台根据以下规则进行问题聚类：
 
- 相同特征ID：将具有相同特征ID的问题聚合在一起。

 
**TOP根因聚类**
 
在问题列表中，每个问题都是同一类问题的汇总。APMS基于堆栈关键行进行准确的同类异常汇聚，将具有相同或相似泄漏堆栈的异常报告自动聚合成一个问题。开发者可点击“查看”进入问题详情页查看详情。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/sXDk5bIYQ6eV5lNdnijMZQ/zh-cn_image_0000002675091239.png?HW-CC-KV=V1&HW-CC-Date=20260723T014110Z&HW-CC-Expire=86400&HW-CC-Sign=27C502EF97E6360D30A50A36B32CFBDD301A4606945B08D517B6107259C78F91)

 
 

#### 根因定位与分析

**基础信息定位**
 
点击问题列表中的某个问题进入详情页后，APMS 将提供以下核心分析信息，帮助开发者高效定位根因。
 
问题概要：展示问题的核心身份信息，包括故障类型、故障模块，帮助开发者快速判断崩溃的基本属性。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/x8yj8s3-Ri2Iafc-7cdibg/zh-cn_image_0000002675011397.png?HW-CC-KV=V1&HW-CC-Date=20260723T014110Z&HW-CC-Expire=86400&HW-CC-Sign=DD1D6A3C556A68CD35291D6978EA462349AB024614C5DBBE628EB9C896558D3E)

 
聚类数据：基于堆栈关键行和过滤筛选跳转聚类同类故障，帮助开发者评估问题的影响范围与严重程度。
 
分析报告：提供问题发生时的完整上下文，包括环境信息（设备型号、系统版本、ROM版本、前后台状态等）、堆栈信息、日志文件，并基于分析结果给出修复建议，辅助开发者高效完成问题排查与闭环。此处demo展示的故障模块是leak_thread。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/jO9PpAbSQyi9SrsY8ZB-zQ/zh-cn_image_0000002645091444.png?HW-CC-KV=V1&HW-CC-Date=20260723T014110Z&HW-CC-Expire=86400&HW-CC-Sign=4B2F2AAF43FED185E811FE7F77A552ABE808314F31ACEA1B515BFEC1F7A8EFA0)

 
**证据链分析**
 
证据链展示主泄漏和次泄漏具体方法位置。开发者可根据平台解析出的泄漏堆栈和故障原因，参照优化建议定位问题代码，完成修复与验证。
 
根据故障详情分析得出：可以看出规格为4096B的堆块为核心泄漏堆块，libanon.so为核心泄漏库，leak thread为核心泄漏方法。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/K8irb9bCShanv8EPkRIIHA/zh-cn_image_0000002644931534.png?HW-CC-KV=V1&HW-CC-Date=20260723T014110Z&HW-CC-Expire=86400&HW-CC-Sign=A5A03BCDADCF50D134060A16E37F03802D180CDA1FCD4D8AA5AB92D28FD436FF)

 
堆栈信息分析：三种形式（堆栈分配详情、堆栈树分配和火焰树）用于查看方法调用关系和疑似泄漏故障处。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/WrAIz4ghSbinKA-zRfrB_Q/zh-cn_image_0000002675091241.png?HW-CC-KV=V1&HW-CC-Date=20260723T014110Z&HW-CC-Expire=86400&HW-CC-Sign=53D5D9D4B088C65A8245C4A3B861E6773F80280B80DDF11336EDF0F6A0EB1E31)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/7nauXRetS5eeX9F2x9cmUA/zh-cn_image_0000002675011401.png?HW-CC-KV=V1&HW-CC-Date=20260723T014110Z&HW-CC-Expire=86400&HW-CC-Sign=BC924D4960DA086A2F50D2F3E15ED539F0C91803620AD622FB74AB39CD5546BB)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/5Fg9jQ5fR0yVcLeWaoD5gA/zh-cn_image_0000002645091446.png?HW-CC-KV=V1&HW-CC-Date=20260723T014110Z&HW-CC-Expire=86400&HW-CC-Sign=783EDE38FA8E4F51D549475506A665E83219F95FB904098BCE9AE799E3CA9B64)

 
**下钻分析**
 
下钻分析的核心逻辑是从一个汇总的指标或表象问题出发，将其拆分成多个组成部分，然后挑出最关键的线索继续向下拆分，不断重复这个过程，直到定位到具体的根因。平台会根据故障特征ID进行聚类并筛选TOP应用版本，系统版本以及设备型号。开发者可根据此重点关注问题高发的版本及设备，更精确的定位问题。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/epG_v4sHROSRMml0vKf6tg/zh-cn_image_0000002644931536.png?HW-CC-KV=V1&HW-CC-Date=20260723T014110Z&HW-CC-Expire=86400&HW-CC-Sign=65279A67EEA6869CD03D862CBA55637FC440264746B22C9E1F3044950AD89C04)

 
 

#### 修复与验证闭环

**修复建议**
 
故障详情页面会提供修复建议，开发者可根据建议优化代码。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/Pah486ohTcy4exjMtSaLHw/zh-cn_image_0000002675091245.png?HW-CC-KV=V1&HW-CC-Date=20260723T014110Z&HW-CC-Expire=86400&HW-CC-Sign=ACDC58B11D12B49794669F26112BFBE57E24E4A603E980A484B1A386856E5319)

 
**修复建议与闭环**
 1. 修改问题之后，可以在分析页面对应的泄漏对象标记已修改，并关注新版本的崩溃数据。
2. 对比修复前后的问题发生率，确认修复是否有效。
 
**故障模式库**
 
故障模式库中会收录常见的Native泄漏事件，针对不同的Native泄漏事件提供最佳实践和修复方案，并且还会提供案例库、收录Native泄漏问题案例和解决过程。开发者可以根据故障匹配到对应的案例，更方便高效的优化问题。
 
 

#### 基于Operation Analyzer平台分析

Operation Analyzer是DevEco Studio的插件，通过该插件可查看应用故障数据，数据与APMS平台一致。
 
 

#### Operation Analyzer平台入口

打开DevEco Studio后，在左侧可看到Operation Analyzer图标，点击后选择应用，再点击资源泄漏即可查看该类故障数据。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/gppFQ1QhTYSOIzVBaw4vOg/zh-cn_image_0000002675011403.png?HW-CC-KV=V1&HW-CC-Date=20260723T014110Z&HW-CC-Expire=86400&HW-CC-Sign=338D7ECCA18687BD274108EF3513538808A1D42738651BF825F332A6C20868AE)

 
 

#### 问题分析

**Operation Analyzer平台问题查看**
 
开发者可自定义筛选条件筛选需要查看的问题，可点击功能列表下具体的问题进一步查看问题详情。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/ZxUPyS_SSIa_bYEr1_Grww/zh-cn_image_0000002645091448.png?HW-CC-KV=V1&HW-CC-Date=20260723T014110Z&HW-CC-Expire=86400&HW-CC-Sign=BFFEC07BEB054E5D967A57F46A94F231E83D3B13ADD4A9B99183AC7CD134EC20)

 
 
**Operation Analyzer平台问题详情**
 
平台的问题详情页同APMS平台功能相同，开发者可查看故障分析与修复建议排查问题。如果修复建议不能支撑解决问题，可进一步查看证据链、现场数据进行具体分析，符号表页签支持上传符号表，还原堆栈信息。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/v5O9yu2zR0-GbH19wzvblw/zh-cn_image_0000002644931538.png?HW-CC-KV=V1&HW-CC-Date=20260723T014110Z&HW-CC-Expire=86400&HW-CC-Sign=415E688E45525777430D974E32FB61984AC59CAD86BAEA9A5AFF6E0D0E333544)

 
开发者也可以查看问题分布图表，定位问题高发的应用版本、设备型号与系统版本，辅助进一步分析。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/iSkHeKW4QJWevgcXMciuuA/zh-cn_image_0000002675091247.png?HW-CC-KV=V1&HW-CC-Date=20260723T014110Z&HW-CC-Expire=86400&HW-CC-Sign=5E87F0282D61CF9A8B3D00079BE30C4D2A6309DD955F16C1A196D59738161187)

 
**Operation Analyzer关联离线符号表**
 
Operation Analyzer平台提供了堆栈还原的能力，可以通过上传符号表（.so/.map/.json文件）完成堆栈还原，辅助分析问题。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/Lztysn0vT_KtW7sqDUJcnQ/zh-cn_image_0000002675011405.png?HW-CC-KV=V1&HW-CC-Date=20260723T014110Z&HW-CC-Expire=86400&HW-CC-Sign=D5AF80CAC09AE7528D1E0BE0A3155B26D590D138F708A7CE26268CE5339242B3)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/RbfXZ-AGRBe7wIggcG_dhA/zh-cn_image_0000002645091450.png?HW-CC-KV=V1&HW-CC-Date=20260723T014110Z&HW-CC-Expire=86400&HW-CC-Sign=CE34D6C611DA3934605B5856250A04F8BA68751BBB5678928E6C4A60A34EEAE4)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/THHekJi4TOWibn6mJlQFTA/zh-cn_image_0000002644931540.png?HW-CC-KV=V1&HW-CC-Date=20260723T014110Z&HW-CC-Expire=86400&HW-CC-Sign=8DB733E04EE0AEC28BB90655FE8195BE33D0FBC932314C4EBCEE540459DECEE3)

 
**Operation Analyzer关联代码**
 
堆栈还原后，Operation Analyzer平台可将故障处与项目代码相关联，点击故障处可跳转到对应源码中，可辅助开发者更高效的定位问题。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/v9iO9f_NQbazN2AwwpzAZw/zh-cn_image_0000002675091249.png?HW-CC-KV=V1&HW-CC-Date=20260723T014110Z&HW-CC-Expire=86400&HW-CC-Sign=4ED288886F21D7A5DBC86A04B7CE752A8A627C999EF091EADA700377A656A6A0)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/o0E0WF3NQuq-RLBCG-GrKw/zh-cn_image_0000002675011407.png?HW-CC-KV=V1&HW-CC-Date=20260723T014110Z&HW-CC-Expire=86400&HW-CC-Sign=803E9C0478662E866ADC1364D3AD45401E5580202CA71C5FA64D1A4A404CC46C)

 

#### 问题修复

Operation Analyzer平台会给出泄漏堆块、泄漏函数与修复建议，开发者可根据修复建议修复问题代码。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/wmnR0AIBTcqTVjZaDa7Z3Q/zh-cn_image_0000002645091452.png?HW-CC-KV=V1&HW-CC-Date=20260723T014110Z&HW-CC-Expire=86400&HW-CC-Sign=E54B8CF1F58AEC2DCAE7DBA6A0B288A6581FFA3451EE91BC3AE1F6C1688D3852)
