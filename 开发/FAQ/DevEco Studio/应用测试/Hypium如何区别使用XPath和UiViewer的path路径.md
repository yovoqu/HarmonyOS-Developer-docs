# Hypium如何区别使用XPath和UiViewer的path路径

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-42

## Hypium如何区别使用XPath和UiViewer的path路径
 


##### 问题现象

XPath中的下标（索引）从1开始，而不是从0开始。但是Hypium插件中UiViewer提供的XPath路径是从下标0开始，导致无法使用。
 
 

##### 背景知识

自动化测试部分控件没有唯一定位的属性，同时通过相对定位的方式也无法准确定位，此时可以使用XPath语法来进行更精确的控件定位。具体语法链接参考[API使用方法](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hypium-python-guidelines#section4598236435)控件查看。
 
 

##### 解决方案

XPath是W3C标准，节点是从[1]开始。UiViewer提供的path下标是从[0]开始。两者不等同，不同的API使用的路径也是不同的。如图点击选中框位置。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/2IZeCbAGRVqCk1wqsgcANw/zh-cn_image_0000002628569544.png?HW-CC-KV=V1&HW-CC-Date=20260701T025924Z&HW-CC-Expire=86400&HW-CC-Sign=9FE37D3156C9EF9B9A66B9E67E6B96EC3DAEDEC05A3C72CDF565978CC5E82FEB)

 
- XPath语法定位控件。使用BY.xpath匹配器可以支持通过XPath语法来查找控件。注意XPath不能和其他匹配器一起使用。
 
```text
# -*- coding: utf-8 -*-
from devicetest.core.test_case import TestCase, Step, CheckPoint
from hypium import BY, UiDriver

class TC_001(TestCase):

    def __init__(self, configs):
        self.TAG = self.__class__.__name__
        super().__init__(self.TAG, configs)
        self.driver = UiDriver(self.device1)
        self.driver_width, self.driver_height = self.driver.get_display_size()

    def setup(self):
        Step('1.回到桌面')
        self.driver.swipe_to_home()

    def process(self):
        Step('2.启动设置应用')
        self.driver.start_app("com.huawei.hmos.settings")
        # 点击设置页面WLAN
        self.driver.touch(BY.text("WLAN"))
        comp = self.driver.find_component(
            BY.xpath("//*[@text='可用 WLAN']/ancestor::List/ListItemGroup/ListItem[1]//Text/following::Image"))
        comp.click()        

    def teardown(self):
        Step('3.关闭设置应用')
        self.driver.stop_app("com.huawei.hmos.settings")
```

- UiViewer提供的path路径定位控件。UiViewer提供的path路径定位控件可以在不同的API中使用，API参数path为UiViewer查看的路径。
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/W_j-stLWQAWofPX5bF4AwQ/zh-cn_image_0000002658928869.png?HW-CC-KV=V1&HW-CC-Date=20260701T025924Z&HW-CC-Expire=86400&HW-CC-Sign=B0F9EDE4D79F8A8536DC2125966F4C8C043BC0BB55B06B9A8812851C33B9F9CE)

 
```text
# -*- coding: utf-8 -*-
from devicetest.core.test_case import TestCase, Step, CheckPoint
from hypium import BY, UiDriver

class TC_002(TestCase):

    def __init__(self, configs):
        self.TAG = self.__class__.__name__
        super().__init__(self.TAG, configs)
        self.driver = UiDriver(self.device1)
        self.driver_width, self.driver_height = self.driver.get_display_size()

    def setup(self):
        Step('1.回到桌面')
        self.driver.swipe_to_home()

    def process(self):
        Step('2.启动设置应用')
        self.driver.start_app("com.huawei.hmos.settings")
        # 点击设置页面WLAN
        self.driver.touch(BY.text("WLAN"))
        comp = self.driver.UiTree.find_component_by_path(
            "/root/Navigation/NavigationContent/NavDestination/NavDestinationContent\
            /Stack/List/ListItemGroup[0]/ListItem/Column/Row/Row/Column[1]/Row/Image")
        self.driver.touch(comp.center)

    def teardown(self):
        Step('3.关闭设置应用')
        self.driver.stop_app("com.huawei.hmos.settings")
```


 
 

##### 常见FAQ

Q：如何通过UiViewer插件中生成的非标准绝对路径查找控件？
 
A：可以通过self.driver.touch(BY.abspath("/root/Navigation/**"))方式，使用绝对路径查找控件。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/ONehAD6tTveyhNxQf-wKgg/zh-cn_image_0000002628409654.png?HW-CC-KV=V1&HW-CC-Date=20260701T025924Z&HW-CC-Expire=86400&HW-CC-Sign=F53A1AD128E618FF10CAE5A454CCF41FB8427DC06C830FE0B945126AAA967ED9)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/iHgy4zVMREeBq3jfj8r9ew/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260701T025924Z&HW-CC-Expire=86400&HW-CC-Sign=4F097B3E9FD4FA10F5385645FC5FAE4A68C8733D755BA9AFDAC00F94BBA21BD3)
 

abspath不能和其他查找方式同时使用，通过XPath查找的控件对象只支持读取控件属性以及click/longClick/doubleClick/inputText/clearText操作。
 

 
 

##### 总结

使用路径进行定位时需要确认API的参数中路径是指通过XPath语法编写还是UiViewer提供的路径。通过路径获取控件后的使用也需要参考API使用方法。
