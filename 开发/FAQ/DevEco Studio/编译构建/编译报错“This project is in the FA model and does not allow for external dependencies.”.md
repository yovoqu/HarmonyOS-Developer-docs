# 编译报错“This project is in the FA model and does not allow for external dependencies.”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-153

**错误描述**
 
FA模型项目不得依赖外部项目模块。
 
**可能原因**
 
在FA模型项目中，build-profile.json5文件的srcPath字段引用了外部项目模块。
 

![](assets/编译报错“This%20project%20is%20in%20the%20FA%20model%20and%20does%20not%20allow%20for%20external%20dependencies.”/file-20260515130202584-0.png)

 
**解决措施**
 
在项目根目录的build-profile.json5文件中，移除srcPath字段依赖的外部项目模块。
