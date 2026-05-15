# 构建报错“ERROR: Task xxx was not found in the project xxx”

更新时间：2026-04-27 09:10:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-37

问题现象

命令行手动执行构建命令时，如果构建失败并提示“ERROR: Task xxx was not found in the project xxx”，请检查以下内容：

- 确认任务名称是否正确。

- 确认项目中是否包含该任务。

- 确认项目路径是否正确。


![](assets/构建报错“ERROR／%20Task%20xxx%20was%20not%20found%20in%20the%20project%20xxx”/file-20260515130110188-0.png)


问题确认

1. 执行hvigor tasks命令，查看该命令是否存在。
2. 查看对应工程中module.json5文件中“type”字段是否为命令执行模块。比如图中执行assembleHar命令，是对工程中的har模块进行打包，若module.json5文件中的“type”字段不是"har"类型，则会出现上述错误提示。


解决措施

1. 执行正确命令。
2. 查看工程中 module.json5 文件的“type”字段，执行相应命令。
