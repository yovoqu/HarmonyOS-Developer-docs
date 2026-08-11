# 运维态高效处理FD资源泄漏

更新时间：2026-08-10 06:55:01

来源：https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-efficiently-handle-fd-leaks

#### 概述

FD（全称：File Descriptor，文件描述符）资源泄漏是一种比较常见的泄漏类型，也是应用稳定性优化的重要问题。本文档主要介绍在运维态下如何通过[应用质量管理（APMS）](https://developer.huawei.com/consumer/cn/doc/app/agc-help-apms-0000002235870062)平台进行FD资源泄漏的监控、分析、定位与修复整套处理方法。
 
 

#### 运维态FD资源泄漏分析流程

 

#### 标准化排查流程

**整体流程图**
 
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/vp0GHtIfQ4aZIaqwub6oRQ/zh-cn_image_0000002671650762.png?HW-CC-KV=V1&HW-CC-Date=20260811T010221Z&HW-CC-Expire=86400&HW-CC-Sign=DA5CA3CD5256F7D0E9629BD75E711E3ABFCE58966B5118147F5CDDA1695FD4A9)

 
**排查步骤**
 1. **故障预警配置：**在APMS平台配置FD泄漏监控告警规则，设置监控时段、频率和触发条件。
2. **问题发现与筛选：**通过故障预警或主动分析页面，筛选FD_LEAK类型的泄漏问题。
3. **关键信息提取**：分析故障模块、发生次数、影响设备数等关键信息，定位高优问题。
4. **根因定位**：通过证据链、持有链分布和现场数据，深入分析泄漏原因。
5. **修复与验证：**根据修复建议优化代码，并验证修复效果，形成闭环。
 

#### 指标监控与关键信息提取

**资源泄漏监控信息详情**
 
故障分析表格会将相同根因类型的故障聚类并排序。表格会展示故障模块、发生次数（占比）、影响设备数（占比）等关键信息，开发者可以通过发生占比和故障模块结合业务实际情况找出高优的问题，并在问题状态和优先级这一栏做出标记，优先解决高优先级的问题。
 
如下图所示，页面入口：故障分析->资源泄漏->资源泄漏信息详情。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/WdlrafCKSWS7g3a9OiOFqg/zh-cn_image_0000002701370585.png?HW-CC-KV=V1&HW-CC-Date=20260811T010221Z&HW-CC-Expire=86400&HW-CC-Sign=1E6604398913D19389380FA5EBADDEB23AE1E1F43D6F339943EE01E0358F278E)

 
**关键指标说明**
 
- 问题特征ID：故障模块的哈希值，同类故障模块会聚类到一起。

 
- 故障模块：发生泄漏的模块或组件，用于定位问题范围。
- 发生次数（占比）：泄漏问题发生的频率，帮助判断问题严重程度。
- 影响设备数（占比）：受影响的设备数量，评估问题影响面。
- 最大泄漏数：单次泄漏的最大句柄数。

 

 
**故障详情页面介绍**
 
通过点击查看按钮，进入到故障详情页面。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/RJcl_lpnSsieMESV1S2n5g/zh-cn_image_0000002701250493.png?HW-CC-KV=V1&HW-CC-Date=20260811T010221Z&HW-CC-Expire=86400&HW-CC-Sign=067CF128723A095E980901AD38D98A10E6D254AE9F60CD10CAB3BCA2A45AEB87)

 
故障详情页面可以通过证据链、现场数据、句柄栈信息进一步深入分析泄漏的原因。
 

 
**证据链**
 
证据链列表根据泄漏数量的大小排序，优先查看泄漏数量最大的句柄名称。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/IJQFshC6TtGCW7Wfd4sDXA/zh-cn_image_0000002671490912.png?HW-CC-KV=V1&HW-CC-Date=20260811T010221Z&HW-CC-Expire=86400&HW-CC-Sign=63FF526F0187F63DDF017CDE1A58DACEC90AC289E1F3BF5C6D190D486D4C516F)

 
**现场数据**
 
现场数据展示了当前FD泄漏的Top10的句柄名称，可结合代码、日志分析对应的FD泄漏对象。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/VdfswQeqSWK5sTLIdcNORw/zh-cn_image_0000002671650764.png?HW-CC-KV=V1&HW-CC-Date=20260811T010221Z&HW-CC-Expire=86400&HW-CC-Sign=791629BB5C5B64D9F976BE00D50B36FC93FAAA57D6FCD6FED16D9A5F5968896D)

 
**句柄栈信息**
 
句柄栈信息中可查看对应的堆栈信息，以及疑似泄漏点。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/vhEDLNQbTYO0ujvoGRX0zg/zh-cn_image_0000002701370587.png?HW-CC-KV=V1&HW-CC-Date=20260811T010221Z&HW-CC-Expire=86400&HW-CC-Sign=215948996CDBBE0B7EAC6BF3F0F70156522E07672B0B50B0F0176263A6901EEF)

 
 

#### APMS平台FD泄漏分析案例

 

#### 灰度任务创建

应用灰度特性是一种运维态功能，用于精准采集故障日志。开发者在端侧集成应用灰度采集功能（可参考：[应用灰度采集介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiretrieval-intro)）后，该应用可参与应用灰度活动。通过云端平台进行[灰度采集](https://developer.huawei.com/consumer/cn/doc/app/agc-help-apms-gray-scale-collect-0000002619401669)，可圈选部分设备开启故障日志精准采集，帮助开发者快速定位故障。
 
 

#### APMS故障预警

在故障预警平台的告警规则页面新建FD泄漏告警。根据实际的业务情况，选择合适监控时段、监控频率、告警触发条件以及其他告警指标，其中FD泄漏对应的指标类型为FD_LEAK。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/Dy28VCDgTSWjP-Ar5mjI0A/zh-cn_image_0000002701250495.png?HW-CC-KV=V1&HW-CC-Date=20260811T010221Z&HW-CC-Expire=86400&HW-CC-Sign=FBEB6CB71ECB3D6A1AF7E36B0952E1739C49B6A65CABF161B9B9AB3AF4BAD0A7)

 
创建告警之后，后台会开始收集数据。当达到设置的告警阈值后，会触发故障预警。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/rR8z0GoGSqGwhe3qVqo0Yg/zh-cn_image_0000002671490914.png?HW-CC-KV=V1&HW-CC-Date=20260811T010221Z&HW-CC-Expire=86400&HW-CC-Sign=9D6C5A27DE28F705E59B3A46EF473DE20EDE43C2E1DFDE5B87FAEFFC0CD1A716)

 
 

#### 问题查看与聚类

**聚类规则说明**
 
FD资源泄漏聚类规则请参考[句柄泄漏聚类规则](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/resource-leak-guidelines#句柄泄漏聚类规则)。
 
**问题查看**
 
- **Top问题查看**

 
通过故障告警的指引，在故障分析页面筛选出FD_LEAK的泄漏类型。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/UBY5JeeVQlmyqmpHEdiiww/zh-cn_image_0000002671650774.png?HW-CC-KV=V1&HW-CC-Date=20260811T010221Z&HW-CC-Expire=86400&HW-CC-Sign=F1E52A5244E578F1F53D2A37CB1A310C8A39573FBC4D43215A66210904B36C5F)

 
点击查看按钮，即可跳转到Top问题查看页签下的FD资源泄漏问题列表。
 

 
- **资源泄漏信息详情Top问题**

 
在左侧页面APMS菜单下的故障分析菜单中，在资源泄漏页签下选择泄漏类型为FD_LEAK，点击查询按钮，过滤出此应用的FD资源泄漏问题。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/l2KUEHNeSsW0_aGbJsZ-WA/zh-cn_image_0000002701370625.png?HW-CC-KV=V1&HW-CC-Date=20260811T010221Z&HW-CC-Expire=86400&HW-CC-Sign=FF55CA662AFAFC7BEAEDA3760A8B00919E25D75459611669315CF4F5861009D1)

 
在资源泄漏信息详情中，可查看当前应用的FD资源泄漏情况。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/TXXTl6C2SaKqGgvYJjXk3g/zh-cn_image_0000002701250559.png?HW-CC-KV=V1&HW-CC-Date=20260811T010221Z&HW-CC-Expire=86400&HW-CC-Sign=A3DF3B6D6E54C0A0B94D4125ED80D277070BAB264E635141158114204D396F0D)

 
 

#### 根因定位与分析

过滤出FD资源泄漏故障列表后，点击查看按钮，进入到问题个例分析详情页，可查看当前故障的分析报告，包含故障发生时间、泄漏句柄、故障模块、版本信息以及修复建议等。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/lOE6YNrITc6JMh-xbyHctw/zh-cn_image_0000002671490976.png?HW-CC-KV=V1&HW-CC-Date=20260811T010221Z&HW-CC-Expire=86400&HW-CC-Sign=42A089A78977C8181F7AC7F613ACD0B04682DE37787E3030C285936F6EF3AAC9)

 
**证据链分析**
 
证据链列表中按照泄漏数量倒序排序，将FD泄漏的句柄名称展示出来，开发者可根据泄漏数量较大的句柄名称，结合代码分析FD泄漏根因。同时提供了日志下载功能，便于进一步分析。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/q_xvTG11QNmnxmgmOpAB4g/zh-cn_image_0000002671650846.png?HW-CC-KV=V1&HW-CC-Date=20260811T010221Z&HW-CC-Expire=86400&HW-CC-Sign=FCCB11BC0EA176C265BFCAADF79AB8BE7B4E9A03F6F59952AA1476F6CC4BF7B0)

 
**现场数据分析**
 
现场数据页中，将展示Top10的泄漏句柄名称，开发者根据泄漏数量较大的句柄名称，并结合代码分析FD泄漏根因。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/279C1D7pR2-ckK2V-hYi6Q/zh-cn_image_0000002701370681.png?HW-CC-KV=V1&HW-CC-Date=20260811T010221Z&HW-CC-Expire=86400&HW-CC-Sign=B500869F65141BA31C87348F99FCDB502C20D8E753E1C00A0F529A8DEEBAE235)

 
**句柄栈信息****分析**
 
句柄栈信息是发生FD泄漏故障并达到一定条件后，系统从堆栈中抓取的堆栈信息，存在一定的滞后性。开发者可参考堆栈中的疑似泄漏点，进行堆栈还原后，结合代码分析具体的FD泄漏根因，并进行修复。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/ESVdqnb4TeKIsIwjVF6qDw/zh-cn_image_0000002701250593.png?HW-CC-KV=V1&HW-CC-Date=20260811T010221Z&HW-CC-Expire=86400&HW-CC-Sign=6A38F0CD242A8D9B421A4D0D2060D4DF33BFCE5CBE51B0987AA15C9C3F153ACA)

 
**下钻分析**
 
下钻分析的核心逻辑是从一个汇总的指标或表象问题出发，将其拆分成多个组成部分，然后挑出最关键的线索继续向下拆分，不断重复这个过程，直到定位到具体的根因。平台会根据故障特征ID进行聚类并筛选Top应用版本，系统版本以及设备型号。开发者可根据此重点关注问题高发的版本及设备，更精确的定位问题。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/WaFBdMMARKS_7_YZ8YTJzg/zh-cn_image_0000002671491006.png?HW-CC-KV=V1&HW-CC-Date=20260811T010221Z&HW-CC-Expire=86400&HW-CC-Sign=D9E59DAE98BAFDAF17F93C0392AAD3E35F18CD74EE7A65ED6EC0925A3CB66285)

 
 

#### 修复建议验证与闭环

**修复建议**
 
故障详情页面会提供修复建议，开发者可以通过给出的建议优化代码。
 
一般来说，开发者需要根据引用链尝试定位并断开应用侧的引用链路，释放对应的可疑泄漏对象。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/f9wjOlNrRQuANVLXwGLQPw/zh-cn_image_0000002671650858.png?HW-CC-KV=V1&HW-CC-Date=20260811T010221Z&HW-CC-Expire=86400&HW-CC-Sign=5B91F8CC3FAC9193C4FBCB7FC7968891D4598AF135AA8907DFEB510F1135A4ED)

 
**问题修复与闭环**
 
- **问题修改**

 
开发者根据修改建议，在工程中释放FD泄漏对象。
 
- **问题标记**

 
优化之后，可以在分析页面对对应的FD泄漏对象标记。
 
- **应用发布**

 
应用发布之后，更新平台告警规则，并持续关注新版本的FD资源泄漏数据。对比修复前后的问题发生率，确认修复是否有效。
 
 

#### 基于Operation Analyzer平台分析

 
Operation Analyzer平台是指DevEco Studio的Operation Analyzer插件，通过该插件查看到应用对应的故障数据，数据和APMS平台上一致，开发者使用该插件以相同的方式分析运维态的泄漏问题。
 

#### Operation Analyzer平台入口

 
打开DevEco Studio后，在Tool Windows栏的Operation Analyzer进入平台，点击后根据包名选择应用，再点击资源泄漏（Resource Leak）即可查看该类故障相关数据。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/yyX_P3zBS36Kt4W8c4EYcw/zh-cn_image_0000002701370683.png?HW-CC-KV=V1&HW-CC-Date=20260811T010221Z&HW-CC-Expire=86400&HW-CC-Sign=636A4F234952B40664E31AF420C0C9C04788D56BD4F7BB513D30C00D6B3C22B7)

 

#### 问题分析

**证据链****分析**
 
证据链列表中按照泄漏数量排序，将FD泄漏的句柄名称展示出来，开发者可根据泄漏数量较大的句柄名称，结合代码分析FD泄漏根因。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/Y4Ou4TrBQ5SWs_35c9dK7w/zh-cn_image_0000002701250595.png?HW-CC-KV=V1&HW-CC-Date=20260811T010221Z&HW-CC-Expire=86400&HW-CC-Sign=27B64955948642D70A1BE6E983483D79CA4B11DA4929FA65B4CA44E1BDB35DF6)

 
**现场数据****分析**
 
现场数据页面将展示Top10的泄漏句柄名称，开发者根据泄漏数量较大的句柄名称，并结合代码分析FD泄漏根因。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/nbo8_yDfSoil85V0ZVvvqA/zh-cn_image_0000002671491008.png?HW-CC-KV=V1&HW-CC-Date=20260811T010221Z&HW-CC-Expire=86400&HW-CC-Sign=5E558871F2B64074B7BF599D12BB84688994294D3E8956F63FDE500D874ED846)

 
**句柄栈****信息****分析**
 
句柄栈信息中将抓取的堆栈信息中疑似泄漏点进行展示，开发者进行堆栈还原后，结合代码分析具体的FD泄漏根因，并进行修复。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/vvOkwcYDR2OQaVlf0EiaMg/zh-cn_image_0000002671650860.png?HW-CC-KV=V1&HW-CC-Date=20260811T010221Z&HW-CC-Expire=86400&HW-CC-Sign=36206F16F1A1A23F8BCBAC15534385F3ED621A70179262A41DC3B4E958799213)
