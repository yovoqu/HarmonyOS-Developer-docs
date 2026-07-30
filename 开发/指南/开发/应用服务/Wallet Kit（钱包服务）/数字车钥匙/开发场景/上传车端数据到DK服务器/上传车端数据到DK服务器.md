# 上传车端数据到DK服务器

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-carkey-scene-cloud

车端可通过钱包提供的通道上传自定义数据，用于获取DK服务器存储的钥匙状态、权限信息等云端数据，钱包作为中间桥梁透传交互数据，提供完整的业务闭环渠道。


#### 交互流程


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/Y3QFVw75Tn6Y18uOH7A0_g/zh-cn_image_0000002685927567.png?HW-CC-KV=V1&HW-CC-Date=20260730T072208Z&HW-CC-Expire=86400&HW-CC-Sign=D49A072B29A810AF2C03C058A43FF5C2CB3A2269E567A5646FEEBADEC48EA254)




#### 典型场景

当车辆的车钥匙**首次**开通且完成认证之后，车端需要上传数据给DK服务器，DK服务器处理之后返回结果给车端。可参考[上传车端数据到DK服务器](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wallet-rest-api-carkey#上传车端数据到dk服务器)进行适配。
