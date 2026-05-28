# 如何在系统深色模式下使用getColorSync(resource)返回深色颜色值

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-354

目前有两种方案可供参考：
 1. 传递资源ID。
```ArkTS
this.getUIContext().getHostContext()?.resourceManager.getColorSync($r('app.color.xxx').id);
```

2. 在配置了dark限定词目录的包的module.json5文件中添加配置。
```json
"metadata": [
  {
    "name": "ContextResourceConfigLoadFromParentTemp",
    "value": "true"
  }
],
```
