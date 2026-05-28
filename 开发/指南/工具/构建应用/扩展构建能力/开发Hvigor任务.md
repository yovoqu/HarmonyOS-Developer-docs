# 开发Hvigor任务

更新时间：2026-04-20 06:32:02

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-task

#### 了解任务

任务是Hvigor构建过程中的基本执行单元，通常包含一段可执行代码；一个任务可以依赖其他多个任务。Hvigor任务调度执行时通过解析依赖关系确定任务执行时序。
 

 
UP-TO-DATE
 
任务标识，表示任务未实际执行。Hvigor任务增量跳过机制，在二次执行任务时检测任务输入输出条件未发生变化，则任务跳过执行提高构建效率。
 
示例：
 
```text
> hvigor UP-TO-DATE ::PackageApp...
```
 

 
Finished
 
任务执行完成标识，表示任务已执行完成。
 
示例：
 
```text
> hvigor Finished ::PackageApp... after 310 ms
```
 

 
 

#### 注册任务

使用HvigorNode节点对象注册任务。
 1. 编辑工程下hvigorfile.ts文件。

  
```text
// 导入模块
import <span style="color: rgb(250,162,61);">{ </span><span style="color: rgb(255,255,255);">getNode, HvigorNode, HvigorTask </span><span style="color: rgb(250,162,61);">} </span>from <span style="color: rgb(170,125,252);">'@ohos/hvigor'</span><span style="color: rgb(226,218,144);">;</span>
```

2. 编写任务代码。

  
```text
<span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取当前</span><span style="color: rgb(128,128,128);">hvigorNode</span><span style="color: rgb(128,128,128);">节点对象</span>
const <span style="color: rgb(0,0,255);">node</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">HvigorNode </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">getNode</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">__filename</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">注册</span><span style="color: rgb(128,128,128);">Task</span>
<span style="color: rgb(0,0,255);">node</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">registerTask</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'customTask'</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(0,0,255);">run</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">log</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'this is Task'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
```

3. 执行任务。

  使用hvigor命令行工具执行任务：

  
```bash
hvigorw customTask
```

4. 查看任务执行结果。

  
![](assets/开发Hvigor任务/file-20260514133112813-0.png)
