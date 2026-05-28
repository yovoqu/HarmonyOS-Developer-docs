# 编译报错“The local dependency below in module %s is invalid”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-143

**错误描述**
 
模块内添加本地依赖项无效。
 
**可能原因**
 
当设置"harLocalDependencyCheck": true时，若har模块添加模块外依赖，将触发该编译报错。
 

![](assets/编译报错“The%20local%20dependency%20below%20in%20module%20s%20is%20invalid”/file-20260515130157566-0.png)

 
**解决措施**
 
设置"harLocalDependencyCheck": true时，确保模块的oh-package.json5文件中，在dependencies和dynamicDependencies下指定的本地依赖都在当前模块目录下。
