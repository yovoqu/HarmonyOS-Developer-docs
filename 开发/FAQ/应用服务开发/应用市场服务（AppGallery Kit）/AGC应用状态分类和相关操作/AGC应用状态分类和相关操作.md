# AGC应用状态分类和相关操作

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-99

#### 问题现象

在AGC创建的应用，有哪几种状态，都可以进行什么操作？
 
 

#### 解决方案

应用状态涵盖应用信息和版本信息，分为以下几种：
 1. 准备提交：创建完的应用在未提交审核时状态为“准备提交”，“准备提交”状态一般也称为草稿态；草稿态的应用可以编辑，但是不能删除。如在应用信息下面修改支持的设备类型，修改应用名称和语言；在版本信息下面修改应用介绍，更换发布素材等。“准备提交”的应用状态标识如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/LgrTuxkGT8CFZAcPKXzHbA/zh-cn_image_0000002628554598.png?HW-CC-KV=V1&HW-CC-Date=20260730T072705Z&HW-CC-Expire=86400&HW-CC-Sign=432292D669A37B1917468A6279E0606CB0373DC8C41DDCC14C6167230E212822)

2. 正在审核：完成应用信息和版本信息填写后，可以提交应用审核，此时应用状态为“正在审核”，“正在审核”状态的应用的无法编辑，如果需要修改应用信息或版本信息，可以撤销审核后再编辑。“正在审核”的应用状态标识如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/S0VprO_dSBu9B9kCmd3CKw/zh-cn_image_0000002658913921.png?HW-CC-KV=V1&HW-CC-Date=20260730T072705Z&HW-CC-Expire=86400&HW-CC-Sign=022E20AB24D29E41A4CCFC2DC8B65CEB70F45FEF56B33B8BBA69C21E095946E2)

3. 待修改：应用提交审核被驳回后，应用状态为“待修改”，“待修改”状态的应用可以编辑，但是不能删除。需要根据审核意见完成修改后重新提交审核。“待修改”的应用状态标识如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/MycWpRpAQeugn4iJXb1d4g/zh-cn_image_0000002628394708.png?HW-CC-KV=V1&HW-CC-Date=20260730T072705Z&HW-CC-Expire=86400&HW-CC-Sign=BAF7C05AE5C879DAA512E8DAB93F4363963A1049CFF00A1F978BEF8B0B512A66)

4. 待上架：如果应用提交审核时[设置了上架时间](https://developer.huawei.com/consumer/cn/doc/app/agc-help-release-app-review-time-0000002293233458)，审核通过时未到达上架时间，应用状态为“待上架”，“待上架”状态的应用无法编辑应用信息和版本信息，但可以编辑上架时间或者[手动发布待上架的应用](https://developer.huawei.com/consumer/cn/doc/app/agc-help-release-app-review-time-0000002293233458#section0726113812279)。“待修改”的应用状态标识如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/gaRLkWEaQbq4sz8KG8b43A/zh-cn_image_0000002658793979.png?HW-CC-KV=V1&HW-CC-Date=20260730T072705Z&HW-CC-Expire=86400&HW-CC-Sign=19750229B41951F80B4E0DA2917C3C55A8EBA6EDAFF10F9BA95F419A5421F099)

5. 已上架：如果提交审核时上架时间选择的“审核通过立即上架”，或者“待上架”的应用已经达到了上架时间，审核通过后应用状态为“已上架”。“已上架”状态的应用的无法编辑，如果需要修改应用信息或版本信息，可以下架后再编辑。“已上架”的应用状态标识如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/nZiCmdmwR0ys2-XBUba9CA/zh-cn_image_0000002628554602.png?HW-CC-KV=V1&HW-CC-Date=20260730T072705Z&HW-CC-Expire=86400&HW-CC-Sign=28B8D3CF41770C661F8020FA46B8F7CDB60AF6B53AF2FE79D052D12D61EDD8D5)

6. 已撤销上架：应用处于“待上架”状态时，如果不想再上架该应用，可以点击“撤销上架”，撤销上架操作不需要人工审核，撤销上架后应用状态为“已撤销上架”，“已撤销上架”状态应用可以编辑后重新上架。“已撤销上架”的应用状态标识如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/Z4rKTIL_RN6yfeOOa77rGw/zh-cn_image_0000002658913925.png?HW-CC-KV=V1&HW-CC-Date=20260730T072705Z&HW-CC-Expire=86400&HW-CC-Sign=FE3973379CC6085AB5B435036F5137DAD65C4296AF0860C4A896DEC65684C1BD)

7. 下架处理中：处于“已上架”状态的应用可以选择申请下架，申请下架需要审核，此时应用状态为“下架处理中”，“下架处理中”的应用在等待审核过程中，还可以选择[撤销下架申请](https://developer.huawei.com/consumer/cn/doc/app/agc-help-maintain-remove-0000002274058145#section7906639512)。“下架处理中”的应用状态标识如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/WPm8TcwDRuCvUR_2urUSGw/zh-cn_image_0000002628394714.png?HW-CC-KV=V1&HW-CC-Date=20260730T072705Z&HW-CC-Expire=86400&HW-CC-Sign=AC135E67361836DF854615D2A1940D11F6656A7486823BFE58332B875886DD3A)

8. 被开发者下架：申请下架的应用审核通过后，应用状态将变为“被开发者下架”。下架的应用可以编辑信息后重新提交上架。“被开发者下架”的应用状态标识如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/wuOmOI29QpKtv6WUbu3eeA/zh-cn_image_0000002658793987.png?HW-CC-KV=V1&HW-CC-Date=20260730T072705Z&HW-CC-Expire=86400&HW-CC-Sign=62309B7452E641901078E9D8D5774075483EF1C0138939ABE6128C073037ED24)

9. 被下架：应用上架后如果华为应用市场发现应用存在恶意违规情况，会发起应用下架操作，下架成功后应用状态为“被下架”，“被下架”的应用状态标识如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/Fvdg_mPXSmCCoX_EJhsi6Q/zh-cn_image_0000002628554608.png?HW-CC-KV=V1&HW-CC-Date=20260730T072705Z&HW-CC-Expire=86400&HW-CC-Sign=CDF484FEA114F0C7D006BA19030E1D04790CA835977E507A599D54118D70C705)

 
 

#### 总结

应用状态无法删除。审核中和已上架的应用信息和版本信息无法编辑，如果需要编辑可以通过[升级版本](https://developer.huawei.com/consumer/cn/doc/app/agc-help-maintain-upgrade-0000002236494386)或[更新应用信息](https://developer.huawei.com/consumer/cn/doc/app/agc-help-maintain-update-0000002271413697)的方式更新。
