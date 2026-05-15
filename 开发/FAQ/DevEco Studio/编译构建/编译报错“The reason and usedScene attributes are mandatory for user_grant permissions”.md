# 编译报错“The reason and usedScene attributes are mandatory for user_grant permissions”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-38

问题现象

DevEco Studio编译失败，提示“The reason and usedScene attributes are mandatory for user_grant permissions”。


![](assets/编译报错“The%20reason%20and%20usedScene%20attributes%20are%20mandatory%20for%20user_grant%20permissions”/file-20260515130110686-0.png)


问题原因

从DevEco Studio NEXT Developer Preview 2版本开始，新增规则：APP包中，所有entry和feature hap的module下的requestPermissions权限清单必须指定（可以为空，若非空则name必填；user_grant权限则必填reason和usedScene字段）。

解决措施

进入对应module.json5文件中，补齐requestPermissions字段下的reason和usedScene字段。如以下示例：

```json
"requestPermissions": [
{
"name": "ohos.permission.READ_IMAGEVIDEO",
"reason": "$string:module_desc",
"usedScene": {
"abilities": [
"EntryAbility"
],
"when": "inuse"
}
}
],
```
