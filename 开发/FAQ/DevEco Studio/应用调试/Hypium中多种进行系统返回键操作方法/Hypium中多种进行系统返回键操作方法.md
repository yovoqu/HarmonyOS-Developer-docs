# Hypium中多种进行系统返回键操作方法

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-75

#### 问题现象

使用[Hypium](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hypium-python-guidelines#section16890204264419)编写UI自动化用例时，如果某个页面没有返回键按钮，如何模拟系统返回键进行返回操作？
 
 

#### 解决方案

```text
<em># -*- coding: utf-8 -*-</em>
<span style="color: rgb(181,106,1);">from </span>devicetest.core.test_case <span style="color: rgb(181,106,1);">import </span>TestCase, Step
<span style="color: rgb(181,106,1);">from </span>hypium <span style="color: rgb(181,106,1);">import </span>UiDriver, KeyCode
<span style="color: rgb(181,106,1);">from </span>hypium.model <span style="color: rgb(181,106,1);">import </span>UiParam
<span style="color: rgb(181,106,1);">class </span>TC_001(TestCase):
    <span style="color: rgb(181,106,1);">def </span><span style="color: rgb(255,0,170);">__init__</span>(<span style="color: rgb(255,0,170);">self</span>, configs):
        <span style="color: rgb(255,0,170);">self</span>.TAG = <span style="color: rgb(255,0,170);">self</span>.__class__.<span style="color: rgb(255,0,170);">__name__</span>
        <span style="color: rgb(0,0,255);">super</span>().<span style="color: rgb(255,0,170);">__init__</span>(<span style="color: rgb(255,0,170);">self</span>.TAG, configs)
        <span style="color: rgb(255,0,170);">self</span>.driver = UiDriver(<span style="color: rgb(255,0,170);">self</span>.device1)
        <span style="color: rgb(255,0,170);">self</span>.driver_width, <span style="color: rgb(255,0,170);">self</span>.driver_height = <span style="color: rgb(255,0,170);">self</span>.driver.get_display_size()
    <span style="color: rgb(181,106,1);">def </span><span style="color: rgb(0,0,255);">setup</span>(<span style="color: rgb(255,0,170);">self</span>):
        Step(<span style="color: rgb(80,160,79);">'1.</span><span style="color: rgb(80,160,79);">回到桌面</span><span style="color: rgb(80,160,79);">'</span>)
        <span style="color: rgb(255,0,170);">self</span>.driver.swipe_to_home()
    <span style="color: rgb(181,106,1);">def </span><span style="color: rgb(0,0,255);">process</span>(<span style="color: rgb(255,0,170);">self</span>):
        Step(<span style="color: rgb(80,160,79);">'2.</span><span style="color: rgb(80,160,79);">多种系统返回操作方法</span><span style="color: rgb(80,160,79);">'</span>)
       <em> <span style="color: rgb(128,128,128);"># </span><span style="color: rgb(128,128,128);">方法一</span><span style="color: rgb(128,128,128);">,</span><span style="color: rgb(128,128,128);">通过</span><span style="color: rgb(128,128,128);">swipe_to_back()</span><span style="color: rgb(128,128,128);">方法返回</span></em>
        <span style="color: rgb(255,0,170);">self</span>.driver.start_app(<span style="color: rgb(80,160,79);">"com.huawei.hmos.browser"</span>)
        <span style="color: rgb(255,0,170);">self</span>.driver.wait(<span style="color: rgb(0,0,255);">3</span>)
        <span style="color: rgb(255,0,170);">self</span>.driver.swipe_to_back()
      <em>  <span style="color: rgb(128,128,128);"># </span><span style="color: rgb(128,128,128);">方法二</span><span style="color: rgb(128,128,128);">,</span><span style="color: rgb(128,128,128);">通过</span><span style="color: rgb(128,128,128);">go_back()</span><span style="color: rgb(128,128,128);">方法返回</span></em>
        <span style="color: rgb(255,0,170);">self</span>.driver.start_app(<span style="color: rgb(80,160,79);">"com.huawei.hmos.browser"</span>)
        <span style="color: rgb(255,0,170);">self</span>.driver.wait(<span style="color: rgb(0,0,255);">3</span>)
        <span style="color: rgb(255,0,170);">self</span>.driver.go_back()
      <em>  <span style="color: rgb(128,128,128);"># </span><span style="color: rgb(128,128,128);">方法三</span><span style="color: rgb(128,128,128);">,</span><span style="color: rgb(128,128,128);">通过</span><span style="color: rgb(128,128,128);">press_key(KeyCode.BACK)</span><span style="color: rgb(128,128,128);">方法返回</span></em>
        <span style="color: rgb(255,0,170);">self</span>.driver.start_app(<span style="color: rgb(80,160,79);">"com.huawei.hmos.browser"</span>)
        <span style="color: rgb(255,0,170);">self</span>.driver.wait(<span style="color: rgb(0,0,255);">3</span>)
        <span style="color: rgb(255,0,170);">self</span>.driver.press_key(KeyCode.BACK)
      <em>  <span style="color: rgb(128,128,128);"># </span><span style="color: rgb(128,128,128);">方法四</span><span style="color: rgb(128,128,128);">,</span><span style="color: rgb(128,128,128);">通过模拟屏幕边缘向左或向右滑动手势返回，设置起点的相对坐标尽量靠近屏幕边缘，防止操作页面内的控件左滑或右滑</span></em>
        <span style="color: rgb(255,0,170);">self</span>.driver.start_app(<span style="color: rgb(80,160,79);">"com.huawei.hmos.browser"</span>)
        <span style="color: rgb(255,0,170);">self</span>.driver.wait(<span style="color: rgb(0,0,255);">3</span>)
        <span style="color: rgb(255,0,170);">self</span>.driver.swipe(UiParam.RIGHT, <span style="color: rgb(181,106,1);">distance</span>=<span style="color: rgb(0,0,255);">30</span>, <span style="color: rgb(181,106,1);">start_point</span>=(<span style="color: rgb(0,0,255);">0.01</span>, <span style="color: rgb(0,0,255);">0.5</span>))
        <span style="color: rgb(255,0,170);">self</span>.driver.start_app(<span style="color: rgb(80,160,79);">"com.huawei.hmos.browser"</span>)
        <span style="color: rgb(255,0,170);">self</span>.driver.wait(<span style="color: rgb(0,0,255);">3</span>)
        <span style="color: rgb(255,0,170);">self</span>.driver.swipe(UiParam.LEFT, <span style="color: rgb(181,106,1);">distance</span>=<span style="color: rgb(0,0,255);">30</span>, <span style="color: rgb(181,106,1);">start_point</span>=(<span style="color: rgb(0,0,255);">0.99</span>, <span style="color: rgb(0,0,255);">0.5</span>))
    <span style="color: rgb(181,106,1);">def </span><span style="color: rgb(0,0,255);">teardown</span>(<span style="color: rgb(255,0,170);">self</span>):
        Step(<span style="color: rgb(80,160,79);">'3.</span><span style="color: rgb(80,160,79);">关闭华为浏览器</span><span style="color: rgb(80,160,79);">'</span>)
        <span style="color: rgb(255,0,170);">self</span>.driver.stop_app(<span style="color: rgb(80,160,79);">"com.huawei.hmos.browser"</span>)
```
