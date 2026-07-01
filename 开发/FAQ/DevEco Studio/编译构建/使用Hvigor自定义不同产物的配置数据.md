# 使用Hvigor自定义不同产物的配置数据

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-213

#### 问题现象

在HarmonyOS应用开发中，如何根据不同的编译产物，动态配置不同模块中的metadata参数？
 
 

#### 背景知识

- [扩展构建](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-build-expanding)允许开发者通过配置任务的形式，在编译过程中对配置参数进行自定义修改。通过扩展构建，开发者可以灵活地调整构建流程和输出结果。
- [插件上下文](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-build-expanding-context)是扩展构建中的核心概念，它提供了获取当前构建环境信息的接口。通过插件上下文，开发者可以获取当前产物信息（如Debug/Release版本）、遍历模块信息，并对模块配置进行动态调整。

 
 

#### 解决方案
1. 需要获取产物名称，根据产物配置对应的模块参数，因此应在最外层配置hvigorfile.ts文件。
2. 根据如下代码获取应用配置参数，获取其中配置的产物名称。
```text
const <span style="color: rgb(255,255,255);">appNode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">HvigorNode </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">getNode</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">__filename</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
const <span style="color: rgb(255,255,255);">appContext </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">appNode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getContext</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">OhosPluginId</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">OHOS_APP_PLUGIN</span><span style="color: rgb(255,0,170);">) </span>as <span style="color: rgb(181,106,1);">OhosAppContext</span><span style="color: rgb(181,106,1);">;</span>
const <span style="color: rgb(255,255,255);">bundleProduct </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">appContext</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getCurrentProduct</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
const <span style="color: rgb(255,255,255);">productName </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">bundleProduct</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">productName</span><span style="color: rgb(181,106,1);">;</span>
```

3. 使用subNodes接口获取所有模块的环境信息，然后通过getContext接口分别获取hap包配置信息。
```text
<em>// </em><em><span style="color: rgb(128,128,128);">获取</span><span style="color: rgb(128,128,128);">hap</span><span style="color: rgb(128,128,128);">模块上下文信息</span></em>
const <span style="color: rgb(255,255,255);">hapContext </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">hapNode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getContext</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">OhosPluginId</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">OHOS_HAP_PLUGIN</span><span style="color: rgb(255,0,170);">) </span>as <span style="color: rgb(181,106,1);">OhosHapContext</span><span style="color: rgb(181,106,1);">;</span>
```

4. 根据第2步获取的包名和第三步获取到的环境信息，使用getModuleJsonOpt获取对应模块下的module.json5配置，修改后，使用setModuleJsonOpt将修改后的配置信息写入。
```json
if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">moduleNameExample </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,255,255);">moduleName</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
  const <span style="color: rgb(255,255,255);">moduleJsonOpt </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">hapContext</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">getModuleJsonOpt</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">moduleJsonOpt</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">根据产物变更参数值</span></em>
    <span style="color: rgb(255,255,255);">moduleJsonOpt</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">module</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">metadata </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">productName </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,255,255);">productNameExample </span>?
      <span style="color: rgb(255,0,170);">[</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(132,63,161);">"name"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">"client_id"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">"value"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">"TestIdNo1" </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">] </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(132,63,161);">"name"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">"client_id"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">"value"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">"TestIdNo2" </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">;</span>
 <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">将</span><span style="color: rgb(128,128,128);">obj</span><span style="color: rgb(128,128,128);">对象设置回上下文对象以使能到构建的过程与结果中</span></em>
    <span style="color: rgb(255,255,255);">hapContext</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setModuleJsonOpt</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">moduleJsonOpt</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```

5. 总体配置文件hvigorfile.ts，配置参考如下：
```json
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">appTasks</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">OhosHapContext</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">OhosAppContext</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">OhosPluginId </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@ohos/hvigor-ohos-plugin'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">getNode</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">hvigor</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">HvigorNode </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@ohos/hvigor'</span><span style="color: rgb(181,106,1);">;</span>


<em>// </em><em><span style="color: rgb(128,128,128);">待修改的产物名</span></em>
const <span style="color: rgb(255,255,255);">productNameExample </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'default'</span>
<em>// </em><em><span style="color: rgb(128,128,128);">待修改的模块名</span></em>
const <span style="color: rgb(255,255,255);">moduleNameExample </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'entry'</span>


<span style="color: rgb(255,255,255);">hvigor</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">nodesEvaluated</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
  const <span style="color: rgb(255,255,255);">appNode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">HvigorNode </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">getNode</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">__filename</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  const <span style="color: rgb(255,255,255);">appContext </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">appNode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getContext</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">OhosPluginId</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">OHOS_APP_PLUGIN</span><span style="color: rgb(255,0,170);">) </span>as <span style="color: rgb(181,106,1);">OhosAppContext</span><span style="color: rgb(181,106,1);">;</span>
  const <span style="color: rgb(255,255,255);">bundleProduct </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">appContext</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getCurrentProduct</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  const <span style="color: rgb(255,255,255);">productName </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">bundleProduct</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">productName</span><span style="color: rgb(181,106,1);">;</span>

 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">遍历子节点</span></em>
  <span style="color: rgb(255,255,255);">appNode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">subNodes</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">hapNode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">HvigorNode</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取</span><span style="color: rgb(128,128,128);">hap</span><span style="color: rgb(128,128,128);">模块上下文信息</span></em>
    const <span style="color: rgb(255,255,255);">hapContext </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">hapNode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getContext</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">OhosPluginId</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">OHOS_HAP_PLUGIN</span><span style="color: rgb(255,0,170);">) </span>as <span style="color: rgb(181,106,1);">OhosHapContext</span><span style="color: rgb(181,106,1);">;</span>
    const <span style="color: rgb(255,255,255);">moduleName </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">hapContext</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">getModuleName</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">moduleNameExample </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,255,255);">moduleName</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      const <span style="color: rgb(255,255,255);">moduleJsonOpt </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">hapContext</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">getModuleJsonOpt</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
      if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">moduleJsonOpt</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    <em>    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">根据产物变更参数值</span></em>
        <span style="color: rgb(255,255,255);">moduleJsonOpt</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">module</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">metadata </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">productName </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,255,255);">productNameExample </span>?
          <span style="color: rgb(255,0,170);">[</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(132,63,161);">"name"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">"client_id"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">"value"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">"TestIdNo1" </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">] </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(132,63,161);">"name"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">"client_id"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">"value"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">"TestIdNo2" </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">;</span>
    <em>    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">将</span><span style="color: rgb(128,128,128);">obj</span><span style="color: rgb(128,128,128);">对象设置回上下文对象以使能到构建的过程与结果中</span></em>
        <span style="color: rgb(255,255,255);">hapContext</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setModuleJsonOpt</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">moduleJsonOpt</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">    }</span>
<span style="color: rgb(181,106,1);">  }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

export default <span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">system</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">appTasks</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,255,255);">plugins</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">[]</span>
<span style="color: rgb(181,106,1);">}</span>
```

 
 

#### 总结

通过HarmonyOS的扩展构建功能，开发者可以在编译阶段动态配置模块的参数。具体来说：
 
- 全局配置：若配置信息涉及多个模块或需要跨模块操作（如根据产物名称动态调整参数），建议将配置逻辑放在项目根目录下的hvigorfile.ts文件中。
- 模块级配置：若仅需配置单个模块的metadata参数，且无需跨模块操作，则可以直接在模块目录中进行配置。
