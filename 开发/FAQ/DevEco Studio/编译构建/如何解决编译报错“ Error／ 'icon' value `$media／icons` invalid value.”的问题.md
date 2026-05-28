# 如何解决编译报错“ Error: 'icon' value `$media:icons` invalid value.”的问题

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-122

**问题现象**
 
编译报错。
 
```json
ERROR: Failed :entry:default@CompileResource...
ERROR: Tools execution failed.
Error: ref `$media:icons` don't be defined.
Error: 'icon' value `$media:icons` invalid value.
at D:\project\process_profile\default\module.json
Detail: Please check the message from tools.
```
 
**报错原因**
 
引用的资源不存在时，编译错误指向build目录中的文件路径。
 
**常见场景**
 1. 资源文件未添加。
2. 资源文件被意外删除。
 
**解决方案**
 
根据报错的资源ID全局搜索，使用右上角的查找按钮，确认报错的资源是否存在。
 

![](assets/如何解决编译报错“%20Error／%20'icon'%20value%20`$media／icons`%20invalid%20value.”的问题/file-20260515130145262-0.png)
