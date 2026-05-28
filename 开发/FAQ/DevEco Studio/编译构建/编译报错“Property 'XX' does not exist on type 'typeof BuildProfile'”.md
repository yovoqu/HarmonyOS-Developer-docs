# 编译报错“Property 'XX' does not exist on type 'typeof BuildProfile'”

更新时间：2026-03-17 00:56:02

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-42

**问题现象**
 
本地HSP模块对外提供的接口中使用了未在HAP中定义的自定义参数BuildProfileFields。HAP引用了HSP中的该接口，导致编译失败，提示“Property 'XX' does not exist on type 'typeof BuildProfile'”。
 

![](assets/编译报错“Property%20'XX'%20does%20not%20exist%20on%20type%20'typeof%20BuildProfile'”/file-20260515130112533-0.png)

 
**解决措施**
 
采用以下两种方式解决该问题：
 
- 在HAP中配置与HSP相同的自定义参数BuildProfileFields。
- 将与HSP相同的自定义参数BuildProfileFields配置到工程级build-profile.json5中。这种方法会使HSP中的自定义参数在全局生效。
