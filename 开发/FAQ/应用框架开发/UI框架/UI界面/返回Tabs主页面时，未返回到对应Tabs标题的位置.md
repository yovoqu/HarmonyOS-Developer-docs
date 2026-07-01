# 返回Tabs主页面时，未返回到对应Tabs标题的位置

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1245

## 返回Tabs主页面时，未返回到对应Tabs标题的位置
 


##### 问题现象

返回Tabs主页面时，返回到Tabs标题的起始位置，而非预期的Tabs标题位置。
 
 

##### 背景知识

- [Tabs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs)：通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图。
- [TabsAnimationEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#tabsanimationevent11对象说明)：Tabs组件动画相关信息集合。枚举值如下：
- currentOffset：Tabs当前显示元素在主轴方向上，相对于Tabs起始位置的位移。单位vp，默认值为0。

 
 

##### 问题定位

- 使用DevEco Testing查看页面布局，确认页签实现基于Tabs组件。
- 排查是否在返回Tabs主页面时，将Tabs组件上的currentOffset值设置为0。
```text
@State swipeRatio = 0;
backToTabs(swipeRatio){
  // ...
  event.currentOffset = swipeRatio;
}
```


 
 

##### 分析结论

在返回Tabs主页面时，将Tabs组件上的currentOffset值设置为0，导致未返回到对应Tabs标题的位置，而是返回到起始位置。
 
 

##### 修改建议

在返回Tabs主页面时，将Tabs组件上的currentOffset值设置成对应Tabs标题的位置。
 
```text
@State swipeRatio =  `${Math.abs(this.tabsWidth / this.tabsIndex)}vp`;
backToTabs(swipeRatio){
  // ...
  event.currentOffset = swipeRatio;
}
```
