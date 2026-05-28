# 编译报错“Cannot depend on HAP modules outside of this project”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-155

**错误描述**
 
不要依赖项目外部的HAP模块。
 
**可能原因**
 
项目根目录下的build-profile.json5文件中，srcPath字段引用了项目外部的 HAP 模块。
 
**解决措施**
 
使用HSP或HAR模块来替代项目外的HAP模块。
