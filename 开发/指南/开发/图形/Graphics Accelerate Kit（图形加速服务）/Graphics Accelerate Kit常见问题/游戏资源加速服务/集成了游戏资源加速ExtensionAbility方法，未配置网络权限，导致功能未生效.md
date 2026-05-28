# 集成了游戏资源加速ExtensionAbility方法，未配置网络权限，导致功能未生效

更新时间：2026-05-08 09:27:50

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-assetdownload-faq-3

未配置网络权限将出现如下异常日志：
 
```text
ohos.permission.INTERNET check failed
```
 
请开发者在“src/main/module.json5”的requestPermissions层级中添加网络权限。
 
```text
{
  "module": {
    // ...
    "requestPermissions": [
      {
        "name": "ohos.permission.INTERNET"
      }
    ]
  }
}
```
