# 配置Client ID

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/configuration_client_id

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)平台，在“开发与服务”中选择目标应用，获取“项目设置 > 常规 > 应用”的Client ID。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/YXNEWaLdTqqKCMmCAt731Q/zh-cn_image_0000002581434578.png?HW-CC-KV=V1&HW-CC-Date=20260528T014544Z&HW-CC-Expire=86400&HW-CC-Sign=F4EC8EE116836FE5B6D709D858A2F27F9CC61C6D7B3560A52AF474C3520422D9)

2. 在工程中entry模块的module.json5文件中，新增metadata，配置name为client_id，value为上一步获取的Client ID的值，如下所示：

  
```json
{
  "module": {
    "name": "xxxx",
    "type": "entry",
    "description": "xxxx",
    "mainElement": "xxxx",
    "deviceTypes": [],
    "pages": "xxxx",
    "abilities": [],
    "metadata": [
      // 配置如下信息
      {
        "name": "client_id",
        "value": "xxxxxx"
      }
    ]
  }
}
```
