# Reader Kit中PageDataInfo的startDomPos或endDomPos值的含义是什么

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-reader-2

## Reader Kit中PageDataInfo的startDomPos或endDomPos值的含义是什么
 


##### 问题现象

获取到PageDataInfo中的startDomPos，其中数字及符号的含义是什么？
 
 

##### 解决方案

domPos可以简单理解为某个元素在DOM树中的位置，也就是根节点如何到该元素的路径。
 
完整的domPos格式如下：
 
章节标识=子节点索引=子孙节点索引#文字索引;@;进度。
