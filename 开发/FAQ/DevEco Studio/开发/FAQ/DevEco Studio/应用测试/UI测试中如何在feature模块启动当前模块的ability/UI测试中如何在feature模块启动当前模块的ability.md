# UI测试中如何在feature模块启动当前模块的ability

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-32

#### 问题现象

使用DevEco Studio进行UI测试，在feature模块下启动ability如何实现？
 
 

#### 背景知识

UI测试框架（UITest）为开发者提供UI界面查找和模拟操作能力，可覆盖UI自动化测试的关键场景，包括界面控件精准查找、UI交互操作（如点击、滑动、文本输入等），参考：[UI测试框架使用指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uitest-guidelines)。
 
 

#### 解决方案
1. 在项目工程中新建feature模块：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/BZrTzMaOTXyFMhaDRays0A/zh-cn_image_0000002658808887.png?HW-CC-KV=V1&HW-CC-Date=20260811T005517Z&HW-CC-Expire=86400&HW-CC-Sign=73DC9AEFCA5F2A7D6D59ECC5F04E750DF05F99D188E8E7FF6C207FEAD23A212F)

2. 打开feature\src\main\module.json5，查看abilities标签的name属性值，确认需要启动的abilityName：
```ArkTS
"abilities": [
  {
  "name": "FeatureAbility",
  "srcEntry": "./ets/featureability/FeatureAbility.ets",
  "description": "$string:FeatureAbility_desc",
  "icon": "$media:layered_image",
  "label": "$string:FeatureAbility_label",
  "startWindowIcon": "$media:startIcon",
  "startWindowBackground": "$color:start_window_background",
  "exported": true
  }
],
```

3. 在feature\src\ohosTest\ets\test\Ability.test.ets编写测试用例启动测试页面，代码示例如下：
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">describe</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">it</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">expect </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@ohos/hypium'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">abilityDelegatorRegistry </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.TestKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">Want </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.AbilityKit'</span><span style="color: rgb(181,106,1);">;</span>

const <span style="color: rgb(0,0,255);">delegator</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">abilityDelegatorRegistry</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">AbilityDelegator </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">abilityDelegatorRegistry</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getAbilityDelegator</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
const <span style="color: rgb(0,0,255);">bundleName </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">abilityDelegatorRegistry</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getArguments</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">bundleName</span><span style="color: rgb(181,106,1);">;</span>

function <span style="color: rgb(0,0,255);">sleep</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">time</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
  return new <span style="color: rgb(0,0,255);">Promise</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">void</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">resolve</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Function</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">setTimeout</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">resolve</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">time</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

export default function <span style="color: rgb(0,0,255);">abilityTest</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">describe</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'AbilityTest'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>

    <span style="color: rgb(0,0,255);">it</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'testStartFeatureTest'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span>async <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">done</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Function</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      const <span style="color: rgb(0,0,255);">want</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Want </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">bundleName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">bundleName</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">abilityName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'FeatureAbility'</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
      try <span style="color: rgb(255,0,170);">{</span>
        await <span style="color: rgb(0,0,255);">delegator</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">startAbility</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">want</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        await <span style="color: rgb(0,0,255);">sleep</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">1000</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

        const <span style="color: rgb(0,0,255);">ability </span><span style="color: rgb(181,106,1);">= </span>await <span style="color: rgb(0,0,255);">delegator</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getCurrentTopAbility</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">expect</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">ability</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">abilityInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">assertEqual</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'FeatureAbility'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

        <span style="color: rgb(0,0,255);">done</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`startAbility error. Code is </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, message is </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">.`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```
