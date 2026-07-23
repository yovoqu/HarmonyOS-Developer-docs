# MDM设置网络白名单功能异常

更新时间：2026-07-09 10:22:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-mdm-3

#### 问题现象

通过[addAllowedWifiList()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-wifimanager#wifimanageraddallowedwifilist19)设置Wi-Fi白名单不生效。
 
 

#### 背景知识

MDM应用可以通过[addAllowedWifiList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-wifimanager#wifimanageraddallowedwifilist19)添加Wi-Fi白名单，Wi-Fi的ssid+BSSID作为参数传递，添加成功后当前设备仅允许连接该名单下的Wi-Fi。
 
以下情况下，调用本接口会报策略冲突：
 
- 已经通过[setDisallowedPolicy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-restrictions#restrictionssetdisallowedpolicy)接口禁用了设备Wi-Fi能力。通过[setDisallowedPolicy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-restrictions#restrictionssetdisallowedpolicy)解除Wi-Fi禁用后，可解除冲突。
- 已经通过[addDisallowedWifiList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-wifimanager#wifimanageradddisallowedwifilist19)接口添加了Wi-Fi禁用名单。通过[removeDisallowedWifiList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-wifimanager#wifimanagerremovedisallowedwifilist19)移除Wi-Fi禁用名单后，可解除冲突。

 
 

#### 问题定位

有问题的操作步骤如下：
 1. 确保[restrictions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-restrictions)中启用Wi-Fi，wifiManager确保没有[Disallowed](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-wifimanager#wifimanageradddisallowedwifilist19)和[Allowed](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-wifimanager#wifimanageraddallowedwifilist19)的Wi-Fi。
2. 使用[addAllowedWifiList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-wifimanager#wifimanageraddallowedwifilist19)添加一个Wi-Fi白名单，其参数类似[{"ssid":"mate60","BSSID":"92:EF:1C:F1:21:81"}]，BSSID值在此处获取：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/jWg97mpiStmHNOpVr_99dw/zh-cn_image_0000002633616294.png?HW-CC-KV=V1&HW-CC-Date=20260723T013523Z&HW-CC-Expire=86400&HW-CC-Sign=0B98D11E2B60C509EE2263D27F134E75B39A40657B24C446DA422FC644771223)

3. 设置后，Wi-Fi白名单未生效。
 
分析以上操作步骤，发现Wi-Fi白名单未生效的原因是**未正确传递BSSID值**。
 
BSSID的正确获取方法：
 1. 打开“开发者选项”-->"开启wlan详细日志记录"：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/IMirVKWqTYOqGKZruiAqbQ/zh-cn_image_0000002633456400.png?HW-CC-KV=V1&HW-CC-Date=20260723T013523Z&HW-CC-Expire=86400&HW-CC-Sign=0D7FF265E5B38E5081C60B5EDD4B365D37D502E8A8A4F7CC43F6AF221D7B9BB6)

2. 查看BSSID：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/a6PUkImwT3OMO88QPD7j_Q/zh-cn_image_0000002663855485.png?HW-CC-KV=V1&HW-CC-Date=20260723T013523Z&HW-CC-Expire=86400&HW-CC-Sign=5809BA4A54032BD28D5735267152D19DD3C66C848D7F5BC0F517393CB4E85EC0)

 
 

#### 分析结论
1. BSSID比较隐晦，需要专门的指引，用户才能正确获取BSSID。
2. MAC和BSSID的格式类似，容易误用，导致功能不正常。
 
 

#### 修改建议
1. 正确获取BSSID。
2. [addAllowedWifiList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-wifimanager#wifimanageraddallowedwifilist19)接口中，传递BSSID。
