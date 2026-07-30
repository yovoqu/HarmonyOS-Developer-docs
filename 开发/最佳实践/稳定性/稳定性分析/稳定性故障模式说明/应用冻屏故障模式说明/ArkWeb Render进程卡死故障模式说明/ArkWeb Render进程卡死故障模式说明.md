# ArkWeb Render进程卡死故障模式说明

更新时间：2026-07-14 02:11:31

来源：https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-arkweb-render-freeze

#### 概述

本文旨在指导HarmonyOS应用开发者如何定位因render卡死导致的应用冻屏（AppFreeze）问题。关于应用冻屏（AppFreeze）问题的检测原理和日志说明可先阅读[AppFreeze（应用冻屏）检测](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appfreeze-guidelines)。
 
 

#### 线程执行繁忙

 

#### 根因描述

 
该问题通常由于业务下发任务过多，导致线程执行繁忙，甚至出现应用卡死。
 

#### 问题分析思路

 
请参考[栈顶在方舟运行时的应用冻屏问题定位实践](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-app-freeze-ark-runtime#section1699914012816)。此类问题通常因业务下发的任务过多，需业务减少下发任务的数量。
 

#### 关键字

 
应用执行过慢甚至卡死闪退，生成的AppFreeze日志中，Total size of Immediate/High/Low events部分数值过高，一般来说，这三者的任务数总量相加超过400，应用就有发生freeze的风险。
 

#### 案例分析

 
以下构造任务下发过多的示例进行分析。
 
**问题现象**
 
应用卡顿甚至卡死，页面无法滑动，点击无响应。
 
**问题分析**
 
首先看AppFreeze日志，找到关键字Total size of Immediate/High/Low events，此时发现下发的任务过多。
 
```text
Total size of Immediate events : <span style="color: rgb(80,160,79);">14392</span>
 High priority <span style="color: rgb(0,0,255);">event</span> queue information:
 Total size of High events : <span style="color: rgb(80,160,79);">1</span>
 Low priority <span style="color: rgb(0,0,255);">event</span> queue information:
 Total size of Low events : <span style="color: rgb(80,160,79);">11</span>
 Idle priority <span style="color: rgb(0,0,255);">event</span> queue information:
 Total size of Idle events : <span style="color: rgb(80,160,79);">1</span>
 Total <span style="color: rgb(0,0,255);">event</span> size : <span style="color: rgb(80,160,79);">14470</span>
Main handler dump end time: <span style="color: rgb(80,160,79);">2026</span>-<span style="color: rgb(80,160,79);">02</span>-<span style="color: rgb(80,160,79);">04</span> <span style="color: rgb(80,160,79);">11</span>:<span style="color: rgb(80,160,79);">29</span>:<span style="color: rgb(80,160,79);">31.124</span>
```
 
开启ffrt抓取trace（可参考[hitrace](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hitrace)抓取trace），从trace分析定位，搜索onSubmitUV找到相关的trace点，即可定位业务抛任务的任务名称。业务就可以根据任务名称排查任务过多的位置。
 
trace分析如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/_o9om5jqS0unSL542HK2QQ/zh-cn_image_0000002666120049.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=9F311C465229C351DCE2937D4F353B3071387DE5C239263DC40AE00AC28F074F)

 
在业务代码中搜索任务名称，可确定抛出任务过多的位置，从而减少抛出此类任务的数量。
 
**排查建议**
 
查找下发次数过多的任务，需要业务根据实际情况减少这类任务调用次数。
 

#### 执行耗时JS

 

#### 根因描述

执行耗时的JS代码，可能会导致render进程卡死，表现为页面冻结，无法响应滑动、点击等操作。
 
 

#### 问题分析思路

 
此类问题首先需要分析JS堆栈，开发者可以通过接入[onRenderProcessNotResponding()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onrenderprocessnotresponding12)接口来获取完整的JS堆栈查看根因。
 

#### 案例分析

本案例通过构造一个可以触发耗时JS操作的应用来进行问题说明。案例如下图：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/1HnhaPqGR7iM3sErSPYu8Q/zh-cn_image_0000002635680956.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=9BF3F3AC1C474BE7AC4CF36DC4A2905E2593431EDEDF2E275009FCC4D8B6F125)

 
**问题现象**
 
 
点击执行耗时JS按钮，触发耗时JS业务，此时页面卡死，无法框选示例文字，滑动等操作被阻塞。
 
**问题分析**
 
根据onRenderProcessNotResponding的回调函数，可以看到具体的JS堆栈。
 
```text
05-27 16:17:58.866   24005-24005   A03D00/com.tes..._freeze/JSAPP  com.test.js_freeze    I     onRenderProcessNotResponding: [jsStack]= startInfiniteLoop (resource://rawfile/test.html:28:9)
                                                                                               executeHeavyJS (resource://rawfile/test.html:25:9)
                                                                                               <anonymous>:1:1, [process]=24151, [reason]=0、
```
 
查看对应的JS代码可知耗时代码如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/FXTHWakXQ5KS3WBW_Bf0kw/zh-cn_image_0000002635840876.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=0E376C4CE364A37784A94EEC90BDB710C65876886F2B7B91444136DE1C2579BD)

 
**排查建议**
 
建议应用使用Web组件的[onRenderProcessNotResponding()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onrenderprocessnotresponding12)接口，再根据JS堆栈定位耗时的JS代码。
