# 编译报错“The reason and usedScene attributes are mandatory for user_grant permissions.”

更新时间：2026-05-15 02:49:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-158

**错误描述**
 
针对Hap模块，配置user_grant权限时必须包含reason和usedScene属性。
 
**可能原因**
 
在module.json5文件中配置user_grant类型的权限时，必须包含reason和usedScene属性。
 

![](assets/编译报错“The%20reason%20and%20usedScene%20attributes%20are%20mandatory%20for%20user_grant%20permissions.”/file-20260515130204158-0.png)

 
**解决措施**
 
对于Hap模块，在module.json5文件的requestPermissions中添加reason和usedScene字段。
 
对于Har/Hsp模块，在module.json5文件的requestPermissions中添加reason字段。
 
示例：
 
```json
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
