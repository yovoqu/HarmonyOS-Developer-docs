# 如何解决编译报错“ The inferred type of 'xxx' cannot be named without a reference to 'xxx'. This is likely not portable. A type annotation is necessary.”的问题

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-128

**问题现象**
 
编译报错“The inferred type of 'xxx' cannot be named without a reference to 'xxx'. This is likely not portable. A type annotation is necessary”。
 
**问题原因**
 
HSP生成的.d.ts声明文件缺少类型注解，因为原始文件中未注明类型。
 

![](assets/如何解决编译报错“%20The%20inferred%20type%20of%20'xxx'%20cannot%20be%20named%20without%20a%20reference%20to%20'xxx'.%20This%20is%20likely%20not%20portable.%20A%20type%20annotation%20is%20necessary.”的问题/file-20260515130148571-0.png)

 
**解决方案**
 
在报错位置添加类型注解。
