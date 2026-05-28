# 编译报错“The 'tag' keyword is not allowed for 'version' at 'xxx/oh-package.json5'”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-149

**错误描述**
 
oh-package.json5文件中的version字段不能包含tag标签。
 
**可能原因**
 
使用parameterFile参数化配置版本号时，oh-package.json5文件中的version字段不能包含tag标签。
 

![](assets/编译报错“The%20'tag'%20keyword%20is%20not%20allowed%20for%20'version'%20at%20'xxx／oh-package.json5'”/file-20260515130200961-0.png)

 
**解决措施**
 
当oh-package.json5文件中的version字段引用parameterFile时，开发者不应使用tag标签。
