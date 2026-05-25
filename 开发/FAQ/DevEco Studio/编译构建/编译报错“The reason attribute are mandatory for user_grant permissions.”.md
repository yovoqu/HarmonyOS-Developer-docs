# 编译报错“The reason attribute are mandatory for user_grant permissions.”

更新时间：2026-05-15 02:49:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-159

**错误描述**
针对Har和Hsp模块，配置user_grant权限时必须包含reason属性。
**可能原因**
在module.json5文件中配置user_grant类型的权限时，必须包含reason属性。

![](assets/编译报错“The%20reason%20attribute%20are%20mandatory%20for%20user_grant%20permissions.”/file-20260525091134902-001.png)
**解决措施**
hap模块的module.json5文件中添加reason和usedScene字段。
在module.json5文件的requestPermissions中添加reason字段，用于har/hsp模块。
示例：

```ts
"requestPermissions": [
      {
        "name": "ohos.permission.READ_IMAGEVIDEO",
        "usedScene": {
          "abilities": [
            "FormAbility"
          ]
        },
        "reason":"$string:location_permission_reason"
      }
    ]
```
