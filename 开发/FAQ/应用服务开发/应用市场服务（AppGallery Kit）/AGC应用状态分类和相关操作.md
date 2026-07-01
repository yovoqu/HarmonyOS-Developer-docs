# AGC应用状态分类和相关操作

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-99

## AGC应用状态分类和相关操作
 


##### 问题现象

在AGC创建的应用，有哪几种状态，都可以进行什么操作？
 
 

##### 解决方案

应用状态涵盖应用信息和版本信息，分为以下几种：
 
- 准备提交：创建完的应用在未提交审核时状态为“准备提交”，“准备提交”状态一般也称为草稿态；草稿态的应用可以编辑，但是不能删除。如在应用信息下面修改支持的设备类型，修改应用名称和语言；在版本信息下面修改应用介绍，更换发布素材等。“准备提交”的应用状态标识如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/w7edghFKRdej66MdtwNpdA/zh-cn_image_0000002628554598.png?HW-CC-KV=V1&HW-CC-Date=20260701T025905Z&HW-CC-Expire=86400&HW-CC-Sign=E61746426BD3065A6999BC929E62CAE6A08EE0450838D9AECBA49CC94529EC37)

- 正在审核：完成应用信息和版本信息填写后，可以提交应用审核，此时应用状态为“正在审核”，“正在审核”状态的应用的无法编辑，如果需要修改应用信息或版本信息，可以撤销审核后再编辑。“正在审核”的应用状态标识如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/r_IlP_sZShKIDewgR18pcw/zh-cn_image_0000002658913921.png?HW-CC-KV=V1&HW-CC-Date=20260701T025905Z&HW-CC-Expire=86400&HW-CC-Sign=D8725FEE943EE576E5896185A48229A0DC41FDF5E31D0AA255E327BD72CAA05D)

- 待修改：应用提交审核被驳回后，应用状态为“待修改”，“待修改”状态的应用可以编辑，但是不能删除。需要根据审核意见完成修改后重新提交审核。“待修改”的应用状态标识如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/gF1pxraXT6OQv0SYW5ysxg/zh-cn_image_0000002628394708.png?HW-CC-KV=V1&HW-CC-Date=20260701T025905Z&HW-CC-Expire=86400&HW-CC-Sign=0D0A8A002AF6688AA826B04C189843880DCD0A5316816C1CDB649AC2F88263AC)

- 待上架：如果应用提交审核时[设置了上架时间](https://developer.huawei.com/consumer/cn/doc/app/agc-help-release-app-review-time-0000002293233458)，审核通过时未到达上架时间，应用状态为“待上架”，“待上架”状态的应用无法编辑应用信息和版本信息，但可以编辑上架时间或者[手动发布待上架的应用](https://developer.huawei.com/consumer/cn/doc/app/agc-help-release-app-review-time-0000002293233458#section0726113812279)。“待修改”的应用状态标识如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/x6vw_Zy7StWQGTyvQjpxPA/zh-cn_image_0000002658793979.png?HW-CC-KV=V1&HW-CC-Date=20260701T025905Z&HW-CC-Expire=86400&HW-CC-Sign=249A310CE09DB477E4D16FF37CE1B30F387F1175ED1C5CF1AFD8F4E49B456871)

- 已上架：如果提交审核时上架时间选择的“审核通过立即上架”，或者“待上架”的应用已经达到了上架时间，审核通过后应用状态为“已上架”。“已上架”状态的应用的无法编辑，如果需要修改应用信息或版本信息，可以下架后再编辑。“已上架”的应用状态标识如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/GW3p5d3nQSqwaCyUpqr9Bw/zh-cn_image_0000002628554602.png?HW-CC-KV=V1&HW-CC-Date=20260701T025905Z&HW-CC-Expire=86400&HW-CC-Sign=24234A805668013ACD965AD5AF1DCB3A16F0F4A152F4FE5A57B75C987314D6E3)

- 已撤销上架：应用处于“待上架”状态时，如果不想再上架该应用，可以点击“撤销上架”，撤销上架操作不需要人工审核，撤销上架后应用状态为“已撤销上架”，“已撤销上架”状态应用可以编辑后重新上架。“已撤销上架”的应用状态标识如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/zfmL7zvRR_yy-7a4rFJ37A/zh-cn_image_0000002658913925.png?HW-CC-KV=V1&HW-CC-Date=20260701T025905Z&HW-CC-Expire=86400&HW-CC-Sign=54708561AE082CDC8240006BF66B55001B9805FF9AF351D1DE14A77BC263A491)

- 下架处理中：处于“已上架”状态的应用可以选择申请下架，申请下架需要审核，此时应用状态为“下架处理中”，“下架处理中”的应用在等待审核过程中，还可以选择[撤销下架申请](https://developer.huawei.com/consumer/cn/doc/app/agc-help-maintain-remove-0000002274058145#section7906639512)。“下架处理中”的应用状态标识如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/FCteYQ3wQ_-kO8lcsBUEjg/zh-cn_image_0000002628394714.png?HW-CC-KV=V1&HW-CC-Date=20260701T025905Z&HW-CC-Expire=86400&HW-CC-Sign=FEFE29C015E4383B9DF5BC08202AC63A340DCCE78ED7B1FB22D0C65429D701C9)

- 被开发者下架：申请下架的应用审核通过后，应用状态将变为“被开发者下架”。下架的应用可以编辑信息后重新提交上架。“被开发者下架”的应用状态标识如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/8y7yKFXrQYSDJotAsM2eLg/zh-cn_image_0000002658793987.png?HW-CC-KV=V1&HW-CC-Date=20260701T025905Z&HW-CC-Expire=86400&HW-CC-Sign=230ABB9836FDB072E19A7796E78FD1B8326138D181AC79DEFAD5162966853DAF)

- 被下架：应用上架后如果华为应用市场发现应用存在恶意违规情况，会发起应用下架操作，下架成功后应用状态为“被下架”，“被下架”的应用状态标识如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/dnV1o0CtTLCtWEMM4THAhw/zh-cn_image_0000002628554608.png?HW-CC-KV=V1&HW-CC-Date=20260701T025905Z&HW-CC-Expire=86400&HW-CC-Sign=7830E1D77312AF31E2718A66F1958AFBB390A1E75D3F6CE1CF501BA1BA24D524)


 
 

##### 总结

应用状态无法删除。审核中和已上架的应用信息和版本信息无法编辑，如果需要编辑可以通过[升级版本](https://developer.huawei.com/consumer/cn/doc/app/agc-help-maintain-upgrade-0000002236494386)或[更新应用信息](https://developer.huawei.com/consumer/cn/doc/app/agc-help-maintain-update-0000002271413697)的方式更新。
