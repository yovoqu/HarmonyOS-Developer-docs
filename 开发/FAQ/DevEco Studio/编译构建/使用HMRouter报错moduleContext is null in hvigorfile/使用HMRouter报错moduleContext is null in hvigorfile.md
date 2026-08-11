# 使用HMRouter报错moduleContext is null in hvigorfile

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-218

#### 问题现象

安装配置HMRouter，在添加plugins:[hapPlugin()]时，报错：
 
```text
<span style="color: rgb(0,0,255);">moduleContext is </span>null in <span style="color: rgb(0,0,255);">hvigorfile</span>
```
 
 

#### 背景知识

[HMRouter](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-hmrouter)是HarmonyOS上的一款页面跳转场景解决方案，主要用于解决应用中页面间的相互跳转问题。该路由器提供了多种功能特性，包括：
 
- 自定义注解实现路由跳转：开发者可以通过为页面添加@HMRouter注解来配置页面的跳转路径。
- 支持HAR/HSP：HMRouter支持处理不同的页面类型，如单例页面和Dialog页面。
- 路由拦截和生命周期管理：支持定义拦截器和生命周期，用于处理页面跳转前后的逻辑。
- 简化动画配置：允许开发者配置全局动画或特定页面的切换动画。

 
 

#### 问题定位

检查hapPlugin插件配置是否正确，是否配置在了entry模块的hvigorfile.ts文件中。
 
 

#### 分析结论

根据配置文件分析，hapPlugin插件配置在了工程根目录下的hvigorfile.ts ，会报错找不到hap模块的上下文。
 
 

#### 修改建议
1. 在工程根目录下hvigor下的hvigor-config.json5文件中配置HMRouter依赖。
```json
{
  <span style="color: rgb(132,63,161);">"modelVersion"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"6.0.0"</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(132,63,161);">"dependencies"</span><span style="color: rgb(181,106,1);">: </span>{
    <span style="color: rgb(132,63,161);">"@hadss/hmrouter-plugin"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"^1.0.0-rc.11"</span>
  }<span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(132,63,161);">"execution"</span><span style="color: rgb(181,106,1);">: </span>{
   <em> <span style="color: rgb(128,128,128);">// "analyze": "normal",                     /* Define the build analyze mode. Value: [ "normal" | "advanced" | "ultrafine" | false ]. Default: "normal" */</span></em>
<em><span style="color: rgb(128,128,128);">    // "daemon": true,                          /* Enable daemon compilation. Value: [ true | false ]. Default: true */</span></em>
<em><span style="color: rgb(128,128,128);">    // "incremental": true,                     /* Enable incremental compilation. Value: [ true | false ]. Default: true */</span></em>
<em><span style="color: rgb(128,128,128);">    // "parallel": true,                        /* Enable parallel compilation. Value: [ true | false ]. Default: true */</span></em>
<em><span style="color: rgb(128,128,128);">    // "typeCheck": false,                      /* Enable typeCheck. Value: [ true | false ]. Default: false */</span></em>
<em><span style="color: rgb(128,128,128);">    // "optimizationStrategy": "memory"         /* Define the optimization strategy. Value: [ "memory" | "performance" ]. Default: "memory" */</span></em>
  }<span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(132,63,161);">"logging"</span><span style="color: rgb(181,106,1);">: </span>{
    <em><span style="color: rgb(128,128,128);">// "level": "info"                          /* Define the log level. Value: [ "debug" | "info" | "warn" | "error" ]. Default: "info" */</span></em>
  }<span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(132,63,161);">"debugging"</span><span style="color: rgb(181,106,1);">: </span>{
    <em><span style="color: rgb(128,128,128);">// "stacktrace": false                      /* Disable stacktrace compilation. Value: [ true | false ]. Default: false */</span></em>
  }<span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(132,63,161);">"nodeOptions"</span><span style="color: rgb(181,106,1);">: </span>{
   <em> <span style="color: rgb(128,128,128);">// "maxOldSpaceSize": 8192                  /* Enable nodeOptions maxOldSpaceSize compilation. Unit M. Used for the daemon process. Default: 8192*/</span></em>
<em><span style="color: rgb(128,128,128);">    // "exposeGC": true                         /* Enable to trigger garbage collection explicitly. Default: true*/</span></em>
  }
}
```

2. 将工程根目录下hvigorfile.ts中的hapPlugin配置转移到entry目录下的hvigorfile.ts中。
```text
<em>// entry</em><em><span style="color: rgb(128,128,128);">模块的</span><span style="color: rgb(128,128,128);">hvigorfile.ts</span></em>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">hapTasks </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@ohos/hvigor-ohos-plugin'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">hapPlugin </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@hadss/hmrouter-plugin'</span><span style="color: rgb(181,106,1);">;</span>

export default <span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">system</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">hapTasks</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,255,255);">plugins</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(0,0,255);">hapPlugin</span><span style="color: rgb(255,0,170);">()] </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">使用</span><span style="color: rgb(128,128,128);">HMRouter</span></em><em>标签的模块均需要配置，与模块类型保持一致</em>
<span style="color: rgb(181,106,1);">}</span>
```
