# 如何通过Hypium脚本实现多端连续滑动

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-68

#### 问题现象

如何利用Hypium实现UI自动化脚本，实现多端连续滑动，类似解锁图形密码操作？
 
 

#### 背景知识

[应用UI测试（基于Python）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hypium-python-guidelines)：DevEco Testing Hypium(以下简称Hypium)是HarmonyOS平台的UI自动化测试框架，支持开发者使用python语言为应用编写UI自动化测试脚本，主要包含以下特性：
 
- Hypium提供了控件、图像、比例坐标等多种控件定位能力，支持多窗口操作以及触摸屏、鼠标、键盘等多种模拟输入功能，支持多设备并行操作，能够覆盖各类场景和多种形态设备上的自动化用例编写需求。
- Hypium包含配套用例编写辅助插件，支持控件查看、投屏操作等多种用例开发辅助功能，提升用例开发体验和效率。
- Hypium能够为执行的用例生成详细的用例执行报告，并且自动记录设备日志以及执行步骤截图，为开发者和测试人员提供高效和专业的测试用例执行和结果分析体验。

 
 

#### 解决方案

通过手势对象的move_to方法进行移动实现连续滑动效果。
 
```text
from devicetest.core.test_case import TestCase
from hypium import Gesture, Point, UiDriver
class TC_001(TestCase):
    def __init__(self, controllers):
        self.TAG = self.__class__.__name__
        super().__init__(self.TAG, controllers)
        self.driver = UiDriver(self.device1)
    def setup(self):
      <em>  # 创建手势对象</em>
        gesture = Gesture()
       <em> # 起始位置, 长按2秒</em>
        gesture.start(Point(360, 500).to_tuple(), 2)
      <em>  # 停留2秒</em>
        gesture.pause(2)
    <em>    # 移动到(100, 500)的位置</em>
        gesture.move_to(Point(100, 500).to_tuple())
     <em>   # 停留2秒结束</em>
        gesture.pause(2)
     <em>   # 移动到(300, 500)的位置</em>
        gesture.move_to(Point(300, 500).to_tuple())
     <em>   # 停留2秒结束</em>
        gesture.pause(2)
       <em> # 执行gesture对象描述的操作</em>
        self.driver.inject_gesture(gesture)
```
