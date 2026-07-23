# AGC添加的公钥指纹信息和证书文件指纹信息不一致

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-23

#### 问题现象

在AGC中通过添加“公钥指纹(HarmonyOS API 9及以上)”入口添加的指纹信息为什么和下载下来的.cer文件指纹信息不一致？
 
AGC添加公钥指纹：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/1QZrsjbvTKKvKAGNI3YmUg/zh-cn_image_0000002658793855.png?HW-CC-KV=V1&HW-CC-Date=20260723T013827Z&HW-CC-Expire=86400&HW-CC-Sign=C83B4D3E7943108BDD78AA42F3AEEAFB6B05827EF002DE8F640262D3A9166F88)

 
证书管理页面：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/Xi_uspuaRzexVXXfVFO5yA/zh-cn_image_0000002628394584.png?HW-CC-KV=V1&HW-CC-Date=20260723T013827Z&HW-CC-Expire=86400&HW-CC-Sign=8C4388F334308236059B2778BFFEF52135CBB325B413D7A7B3C8482FB163CBAD)

 
证书里的指纹信息：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/AHqF2yJRS82TpGQpUmwhEw/zh-cn_image_0000002628554474.png?HW-CC-KV=V1&HW-CC-Date=20260723T013827Z&HW-CC-Expire=86400&HW-CC-Sign=32CBE1AA169979DFEAE3557E0B036A465E49962B6C3CB2952754E0FFA9A91E86)

 
在AGC中通过添加“公钥指纹(HarmonyOS API 9及以上)”入口添加的指纹信息为什么和下载下来的.cer文件指纹信息不一致？
 
 

#### 解决方案

通过添加“公钥指纹”入口所添加的指纹信息与下载的.cer文件中的指纹信息不一致，这是因为这两个指纹信息服务于不同的目的，且是由不同的文件生成的。
 
- **公钥指纹**：在HarmonyOS API 9及以上版本中，在AGC中添加的“公钥指纹”是基于csr（certificate Signing Request，证书签名请求）文件生成的。这个指纹主要用于应用的身份验证，确保应用能够与华为的服务进行正常的交互。特别是在集成华为账号服务时，这个公钥指纹被用来校验应用的真实性。
- **证书指纹**：从.cer文件中获取的指纹信息通常是用于应用的调试和发布过程中的安全认证。这个指纹可能在应用的不同生命周期阶段有所不同，特别是当证书过期或更新时，指纹也会随之变化。

 
由于这两个指纹信息是由不同的文件（csr和cer）生成的，它们在本质上是不同的。此外，公钥指纹通常更关注于应用运行时的身份验证，而证书指纹则涉及到应用的整个生命周期的安全管理。因此在AGC中看到的公钥指纹与从.cer文件中提取的证书指纹不一致是正常的现象。
