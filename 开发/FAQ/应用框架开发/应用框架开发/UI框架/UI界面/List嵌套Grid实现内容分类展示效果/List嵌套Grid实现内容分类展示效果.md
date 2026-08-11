# List嵌套Grid实现内容分类展示效果

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1222

#### 问题现象

如何使用List嵌套Grid实现内容分类展示效果？如何实现这种组合布局？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/HxhjgNXESY2BsDMOVUs6QQ/zh-cn_image_0000002658833271.gif?HW-CC-KV=V1&HW-CC-Date=20260811T005643Z&HW-CC-Expire=86400&HW-CC-Sign=3513627FE686DD866A6DF284A18BE547B867C90C084D6CCDA5442EC3119ACFD7)

 
 

#### 背景知识

- [List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)组件包含一系列相同宽度的列表项。适合连续、多行呈现同类数据，例如图片和文本。
- [Grid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid)网格容器，由“行”和“列”分割的单元格所组成，通过指定“项目”所在的单元格做出各种各样的布局。
- [aboutToAppear](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-lifecycle#abouttoappear)函数在创建自定义组件的新实例后，在执行其build()函数之前执行。

 
 

#### 解决方案
1. ListGridDemo.ets：
定义状态变量curIndex用于跟踪当前选中的标签索引，以及tabItem数组用于存储各个分类的名称。
2. 实现tabBuilder方法，用于构建每个标签的样式，即选中时的字体变化。
3. ForEach循环遍历tabItem数组，为每个标签创建TabContent。每个TabContent内部是一个Scroll组件，里面嵌入ItemsPageView组件，并传递tabBarIndex参数。
4. ItemsPageView.ets：
定义两个数据模型gridItems和listItems，分别用于网格和列表布局。
5. 使用ListItemAdapter管理数据，在aboutToAppear方法中将gridItems和listItems添加到Adapter中。
6. 使用LazyForEach遍历Adapter中的每个数据项，根据itemType字段决定渲染ListComponent还是GridComponent。
7. ListItemAdapter.ets：
实现一个泛型类，实现IDataSource接口。
8. 维护一个列表listItems和数据变更的监听器listeners。
 
 

#### 常见FAQ

Q：怎样在此场景上实现下拉刷新功能？
 
A：下拉刷新可以使用Refresh嵌套List来实现，刷新逻辑在onRefreshing回调方法里面执行，具体参考[官方文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-278)。
