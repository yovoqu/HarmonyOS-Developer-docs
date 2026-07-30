# wukong测试中的常见问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-33

#### 问题现象
1. 执行命令：
```text
<span style="color: rgb(255,255,255);">wukong exec </span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,255,255);">s </span><span style="color: rgb(80,160,79);">10 </span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,255,255);">i </span><span style="color: rgb(80,160,79);">1000 </span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,255,255);">a </span><span style="color: rgb(80,160,79);">0.28 </span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,255,255);">t </span><span style="color: rgb(80,160,79);">0.72 </span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,255,255);">c </span><span style="color: rgb(80,160,79);">100</span>
```
 报错信息：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/ZeYiGpJlRmWjzc0Slb9C9A/zh-cn_image_0000002628569520.png?HW-CC-KV=V1&HW-CC-Date=20260730T072723Z&HW-CC-Expire=86400&HW-CC-Sign=AA5B06417C6AC41A1BAC351CD48E3CE8E83FC5FBAB98B25A84D23932E5B06220)

2. 运行单元测试时报错"Error in testUiExample, Can not connect to AAMS"。
 
 

#### 背景知识

[wukong](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wukong-guidelines#功能介绍)、[Hypium](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hypium-python-guidelines#section16890204264419)、[DevEco Testing](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deveco-testing)等软件都依赖无障碍子系统，无障碍当前同一时间只允许一个程序进行连接，所以当发生冲突时，会出现报错。
 
 

#### 解决方案
1. 重启手机。
2. 终止不需要执行的进程。比如，要终止对应的单元测试进程，具体步骤如下：

  
```bash
<span style="color: rgb(255,255,255);">hdc shell</span>
<span style="color: rgb(255,255,255);">ps </span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,255,255);">ef </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(255,255,255);">grep uitest</span>
<span style="color: rgb(255,255,255);">kill </span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(80,160,79);">9 </span><span style="color: rgb(255,255,255);">uitest</span><span style="color: rgb(255,255,255);">的进程号</span>
```
 如果要终止对应的DevEco Testing进程，可以按下面步骤执行：

  
```bash
<span style="color: rgb(255,255,255);">hdc shell</span>
<span style="color: rgb(255,255,255);">ps </span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,255,255);">ef </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(255,255,255);">grep uitest</span>
<span style="color: rgb(255,255,255);">kill </span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(80,160,79);">9 </span><span style="color: rgb(255,255,255);">uitest start</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(255,255,255);">daemon singleness</span><span style="color: rgb(255,255,255);">的进程号</span>
```

 
 

#### 常见FAQ

Q：wukong测试时出现Errorcode:(4005)或Errorcode:(4007)报错，该如何处理？
 
A：因屏幕显示区域大小变化，导致无障碍获取页面信息失败。该错误不影响测试流程，无需处理。
 
Q：wukong测试时出现Crash reporting enabled for process:XXX是什么含义？
 
A：Crash reporting enabled for process:{进程类型}表示crashpad初始化完成，以及进程类型。
 
渲染/GPU进程创建或销毁：
  
| 级别 | domain/Tag | 文件名 | 日志内容 | 日志含义 |
| --- | --- | --- | --- | --- |
| INFO | C04500/chromium | crash_reporting.cc | Crash reporting enabled for process:{进程类型} | crashpad初始化完成，以及进程类型。 |
 
 
Q：wukong工具测试过程中如何停止测试？
 
A：建议在wukong测试执行前提前设置好测试次数、总时长等参数，避免任务长时间执行。执行过程中需要停止wukong测试任务的话，可以使用键盘Ctrl+C进行停止任务，或者使用以下hdc命令重启测试设备：hdc shell reboot。
