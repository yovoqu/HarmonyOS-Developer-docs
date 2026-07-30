# Hypium中，如何判断当前屏幕为横屏或竖屏

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-74

#### 问题现象

Hypium中，执行视频类应用的全屏或者游戏类应用横屏时，应当如何判断当前为横屏还是竖屏？
 
 

#### 背景知识

[DevEco Testing Hypium](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hypium-python-guidelines#section16890204264419)是HarmonyOS平台的UI自动化测试框架，支持开发者使用Python语言为应用编写UI自动化测试脚本，主要包含以下特性：
 1. Hypium提供了控件/图像/比例坐标等多种控件定位能力，支持多窗口操作以及触摸屏/鼠标/键盘等多种模拟输入功能，支持多设备并行操作，能够覆盖各类场景和多种形态设备上的自动化用例编写需求。
2. Hypium包含配套用例编写辅助插件,支持控件查看/投屏操作等多种用例开发辅助功能，提升用例开发体验和效率。
3. Hypium能够为执行的用例生成详细的用例执行报告，并且自动记录设备日志以及执行步骤截图，为开发者和测试人员提供高效和专业的测试用例执行和结果分析体验。
 
参考[窗口旋转说明](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-landscape-and-portrait-development#section388473115175)，窗口旋转形态有以下四种，分别为顺时针方向旋转0度（竖屏），旋转90度（反向横屏），旋转270度（横屏），旋转180度（反向竖屏）。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/hIEECqOvSdCaZ-wysLO1ag/zh-cn_image_0000002628569338.png?HW-CC-KV=V1&HW-CC-Date=20260730T072720Z&HW-CC-Expire=86400&HW-CC-Sign=C9DBB1C297278D095B43B63AFE03C73991BC9FDD78410BB76D8D7B92501EA525)

 
 

#### 解决方案

```text
<em># -*- coding: utf-8 -*-</em>
<span style="color: rgb(181,106,1);">from </span>devicetest.core.test_case <span style="color: rgb(181,106,1);">import </span>TestCase, Step
<span style="color: rgb(181,106,1);">from </span>hypium <span style="color: rgb(181,106,1);">import </span>UiDriver
<span style="color: rgb(181,106,1);">class </span>TC_001(TestCase):
    <span style="color: rgb(181,106,1);">def </span><span style="color: rgb(255,0,170);">__init__</span>(<span style="color: rgb(255,0,170);">self</span>, configs):
        <span style="color: rgb(255,0,170);">self</span>.TAG = <span style="color: rgb(255,0,170);">self</span>.__class__.<span style="color: rgb(255,0,170);">__name__</span>
        <span style="color: rgb(0,0,255);">super</span>().<span style="color: rgb(255,0,170);">__init__</span>(<span style="color: rgb(255,0,170);">self</span>.TAG, configs)
        <span style="color: rgb(255,0,170);">self</span>.driver = UiDriver(<span style="color: rgb(255,0,170);">self</span>.device1)
        <span style="color: rgb(255,0,170);">self</span>.driver_width, <span style="color: rgb(255,0,170);">self</span>.driver_height = <span style="color: rgb(255,0,170);">self</span>.driver.get_display_size()
    <span style="color: rgb(181,106,1);">def </span><span style="color: rgb(0,0,255);">setup</span>(<span style="color: rgb(255,0,170);">self</span>):
        Step(<span style="color: rgb(80,160,79);">"</span><span style="color: rgb(80,160,79);">预制条件</span><span style="color: rgb(80,160,79);">"</span>)
    <span style="color: rgb(181,106,1);">def </span><span style="color: rgb(0,0,255);">process</span>(<span style="color: rgb(255,0,170);">self</span>):
        Step(<span style="color: rgb(80,160,79);">"</span><span style="color: rgb(80,160,79);">方法一：使用</span><span style="color: rgb(80,160,79);">driver.get_display_size()</span><span style="color: rgb(80,160,79);">方法获取当前屏幕的宽和高，当宽</span><span style="color: rgb(80,160,79);">></span><span style="color: rgb(80,160,79);">高时，即为横屏，反之为竖屏。</span><span style="color: rgb(80,160,79);">"</span>)
     <em>   <span style="color: rgb(128,128,128);"># </span><span style="color: rgb(128,128,128);">获取当前屏幕尺寸</span></em>
        display = <span style="color: rgb(255,0,170);">self</span>.driver.get_display_size()
      <em>  <span style="color: rgb(128,128,128);"># </span><span style="color: rgb(128,128,128);">屏幕宽度（像素）</span></em>
        width = display[<span style="color: rgb(0,0,255);">0</span>]
     <em>   <span style="color: rgb(128,128,128);"># </span><span style="color: rgb(128,128,128);">屏幕高度（像素）</span></em>
        height = display[<span style="color: rgb(0,0,255);">1</span>]
     <em>   <span style="color: rgb(128,128,128);"># </span><span style="color: rgb(128,128,128);">当屏幕宽度</span><span style="color: rgb(128,128,128);">></span><span style="color: rgb(128,128,128);">屏幕高度，表示当前为横屏观看</span><span style="color: rgb(128,128,128);">,</span><span style="color: rgb(128,128,128);">否则为竖屏</span></em>
        <span style="color: rgb(181,106,1);">if </span>width > height:
            current_orientation = <span style="color: rgb(80,160,79);">"landscape"</span>
        <span style="color: rgb(181,106,1);">else</span>:
            current_orientation = <span style="color: rgb(80,160,79);">"portrait"</span>
        <span style="color: rgb(0,0,255);">print</span>(<span style="color: rgb(80,160,79);">f"</span><span style="color: rgb(80,160,79);">当前屏幕方向</span><span style="color: rgb(80,160,79);">: </span><span style="color: rgb(181,106,1);">{</span>current_orientation<span style="color: rgb(181,106,1);">}</span><span style="color: rgb(80,160,79);">"</span>)
        Step(<span style="color: rgb(80,160,79);">"</span><span style="color: rgb(80,160,79);">方法二：使用</span><span style="color: rgb(80,160,79);">driver.get_display_rotation()</span><span style="color: rgb(80,160,79);">方法获取当前手机方向</span><span style="color: rgb(80,160,79);">"</span>)
       <em> <span style="color: rgb(128,128,128);"># </span><span style="color: rgb(128,128,128);">获取当前屏幕方向，正常横屏值为：</span><span style="color: rgb(128,128,128);">DisplayRotation.ROTATION_270</span><span style="color: rgb(128,128,128);">、</span><span style="color: rgb(128,128,128);">DisplayRotation.ROTATION_90</span><span style="color: rgb(128,128,128);">，竖屏为：</span><span style="color: rgb(128,128,128);">DisplayRotation.ROTATION_0</span></em>
        current_orientation = <span style="color: rgb(255,0,170);">self</span>.driver.get_display_rotation()
        <span style="color: rgb(0,0,255);">print</span>(<span style="color: rgb(80,160,79);">f"</span><span style="color: rgb(80,160,79);">当前屏幕方向</span><span style="color: rgb(80,160,79);">: </span><span style="color: rgb(181,106,1);">{</span>current_orientation<span style="color: rgb(181,106,1);">}</span><span style="color: rgb(80,160,79);">"</span>)
    <span style="color: rgb(181,106,1);">def </span><span style="color: rgb(0,0,255);">teardown</span>(<span style="color: rgb(255,0,170);">self</span>):
        Step(<span style="color: rgb(80,160,79);">"</span><span style="color: rgb(80,160,79);">收尾工作</span><span style="color: rgb(80,160,79);">xxxx"</span>)
```
