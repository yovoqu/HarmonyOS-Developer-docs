# 编译报错“Duplicate 'routerMap' object names detected.”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-161

**错误描述**
 
routerMap配置中存在重复名称。
 
**可能原因**
 
当前模块的router_map.json文件中存在name重复的routerMap配置，或者当前模块与依赖模块之间存在name重复的routerMap配置。
 

![](assets/编译报错“Duplicate%20'routerMap'%20object%20names%20detected.”/file-20260515130206180-0.png)

 
**解决措施**
 
修改router_map.json文件中的name字段，确保其值唯一。
