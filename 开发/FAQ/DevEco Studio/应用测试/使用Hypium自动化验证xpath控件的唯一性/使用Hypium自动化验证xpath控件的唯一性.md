# 使用Hypium自动化验证xpath控件的唯一性

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-25

#### 问题现象

Hypium自动化在定位器中，通过XPath语法写的XPath路径，在定位器的哪里验证该XPath是否唯一？
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/tN7nnQO-R5WjV8RIbrWE0Q/zh-cn_image_0000002628569454.png?HW-CC-KV=V1&HW-CC-Date=20260730T072722Z&HW-CC-Expire=86400&HW-CC-Sign=C0B254A2D0E2D0C5B0CDB979EF78B0E931068A0CB10508B946884E5105F1BC78)

 
 

#### 背景知识

- [DevEco Testing Hypium](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hypium-python-guidelines#section16890204264419)插件会在PyCharm界面右边缘的ToolWindow区域生成UiViewer标签，点击后会展开UiViewer面板。UiViewer功能目前分为4个界面：设备选择界面、单设备控件查看界面、单设备投屏界面、双设备投屏界面。
- XPath方式查找匹配的控件：部分控件没有唯一定位的属性，同时通过相对定位的方式也无法准确定位，此时可以使用XPath语法来进行更精确的控件定位。使用BY.xpath匹配器可以支持通过XPath语法来查找控件。详情请参考[API使用方法](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hypium-python-guidelines#section4598236435)。

 
 

#### 解决方案

- 用户可以根据控件的key、text、type内容来搜索指定控件。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/tq0CPbjlSduaW-r_3NKnHQ/zh-cn_image_0000002658928773.png?HW-CC-KV=V1&HW-CC-Date=20260730T072722Z&HW-CC-Expire=86400&HW-CC-Sign=ACF782B7478C1E2AED7B32082CB117A6BCA5A50D5C06EFE6DEF78A11921F1A4E)

- 通过API方法实现XPath语法验证控件是否唯一。
```text
<span style="color: rgb(181,106,1);">from </span>devicetest.core.test_case <span style="color: rgb(181,106,1);">import </span>TestCase, Step, MESSAGE
<span style="color: rgb(181,106,1);">from </span>hypium <span style="color: rgb(181,106,1);">import </span>UiDriver, BY
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
        Step(<span style="color: rgb(80,160,79);">'2.</span><span style="color: rgb(80,160,79);">启动设置应用</span><span style="color: rgb(80,160,79);">'</span>)
        <span style="color: rgb(255,0,170);">self</span>.driver.start_app(<span style="color: rgb(80,160,79);">"com.huawei.hmos.settings"</span>)
        Step(<span style="color: rgb(80,160,79);">"</span><span style="color: rgb(80,160,79);">步骤</span><span style="color: rgb(80,160,79);">1:</span><span style="color: rgb(80,160,79);">验证控件是否存在且唯一</span><span style="color: rgb(80,160,79);">"</span>)
        comp = <span style="color: rgb(255,0,170);">self</span>.driver.find_all_components(BY.xpath(<span style="color: rgb(80,160,79);">"//*[@text='WLAN']"</span>))
        MESSAGE(<span style="color: rgb(80,160,79);">'component is ' </span>+ <span style="color: rgb(0,0,255);">str</span>(comp))
    <span style="color: rgb(181,106,1);">def </span><span style="color: rgb(0,0,255);">teardown</span>(<span style="color: rgb(255,0,170);">self</span>):
        <span style="color: rgb(181,106,1);">pass</span>
```


 
 

#### 常见FAQ

Q：WebView页面是否支持验证XPath表达式？
 
A：WebView页面可以通过浏览器自带的检测功能进行检测，按F12打开浏览器开发者工具按Ctrl+F键查找。
 
Q：使用“hdc shell uitest dumpLayout”指令获取到的控件树如何实现UI自动化？
 
A：控件树中类型为空串的节点代表当前的屏幕信息，类型为root和WindowScene和当前屏幕的对应关系可以通过UiViewer查看，如果想实现UI自动化，推荐使用[DevEco Testing Hypium](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hypium-python-guidelines#section16890204264419)的UiViewer插件，可以对控件树进行可视化和获取控件的信息。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/8qQAGBrARfClfmPd-uLxQA/zh-cn_image_0000002658808825.png?HW-CC-KV=V1&HW-CC-Date=20260730T072722Z&HW-CC-Expire=86400&HW-CC-Sign=2676209FDEC877B355C68940DC93D60048E210DD69B75192DA084001ED7A020D)
