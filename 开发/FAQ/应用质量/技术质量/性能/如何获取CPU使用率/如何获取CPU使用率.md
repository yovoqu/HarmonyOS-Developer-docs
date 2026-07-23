# 如何获取CPU使用率

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-50

#### 问题现象

如何分别获取系统、进程、线程的CPU使用率？
 
 

#### 解决方案

获取CPU使用率分为系统的CPU使用率、进程的CPU使用率和线程的CPU使用率三种情况。
 
- 获取[系统的CPU](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hidebug#hidebuggetsystemcpuusage12)资源占用情况。如当系统资源CPU占用为50%时，将返回0.5。
```text
let <span style="color: rgb(255,255,255);">systemCpuUsage </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">hidebug</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getSystemCpuUsage</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">获取系统的</span><span style="color: rgb(128,128,128);">CPU</span><span style="color: rgb(128,128,128);">资源占用情况</span></em>
```

- 获取[进程的CPU](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hidebug#hidebuggetcpuusage9)使用率，如占用率为50%，则返回0.5。
```text
let <span style="color: rgb(255,255,255);">cpuUsage</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">hidebug</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getCpuUsage</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取进程的</span><span style="color: rgb(128,128,128);">CPU</span><span style="color: rgb(128,128,128);">使用率</span></em>
```

- 获取应用[线程的CPU](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hidebug#hidebuggetappthreadcpuusage12)使用情况。返回当前应用进程下所有ThreadCpuUsage数组，数组中每个ThreadCpuUsage对象包含线程号和线程CPU使用率。
```text
let <span style="color: rgb(255,255,255);">appThreadCpuUsage</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">hidebug</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">ThreadCpuUsage</span><span style="color: rgb(255,0,170);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">hidebug</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getAppThreadCpuUsage</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取应用线程</span><span style="color: rgb(128,128,128);">CPU</span><span style="color: rgb(128,128,128);">使用情况</span></em>
let <span style="color: rgb(255,255,255);">threadCpuUsage </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">''</span><span style="color: rgb(181,106,1);">;</span>
for <span style="color: rgb(255,0,170);">(</span>let <span style="color: rgb(255,255,255);">i </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(255,255,255);">i </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(255,255,255);">appThreadCpuUsage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(255,255,255);">i</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">threadCpuUsage </span><span style="color: rgb(181,106,1);">=</span>
    <span style="color: rgb(255,255,255);">threadCpuUsage </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(132,63,161);">`threadId=</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">appThreadCpuUsage</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(255,255,255);">i</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">threadId</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">, cpuUsage=</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">appThreadCpuUsage</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(255,255,255);">i</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">cpuUsage</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">` </span><span style="color: rgb(181,106,1);">+</span>
      <span style="color: rgb(132,63,161);">'</span>\n<span style="color: rgb(132,63,161);">'</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>
```
