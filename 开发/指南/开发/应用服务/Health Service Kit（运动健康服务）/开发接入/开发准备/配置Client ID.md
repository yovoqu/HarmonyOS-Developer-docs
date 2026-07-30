# 配置Client ID

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-configuration-client-id

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)平台，在“开发与服务”中选择目标应用，获取“项目设置 > 常规 > 应用”的Client ID。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/V2aS5TU2Q8qD6Q3OQp8xfQ/zh-cn_image_0000002656007586.png?HW-CC-KV=V1&HW-CC-Date=20260730T072004Z&HW-CC-Expire=86400&HW-CC-Sign=22482B22208A4B5C6B8B9B3FDE8E2AB9BDAFC9137C723619C3EA84AB66641562)

2. 在工程中entry模块的module.json5文件中，新增metadata，配置name为client_id，value为上一步获取的Client ID的值，如下所示：

  
```json
"module": {
  "name": "xxxx",
  "type": "entry",
  "description": "xxxx",
  "mainElement": "xxxx",
  "deviceTypes": [],
  "pages": "xxxx",
  "abilities": [],
  "metadata": [
    {
      "name": "client_id",
      "value": "xxxxxx"
    }
  ]
}
```
