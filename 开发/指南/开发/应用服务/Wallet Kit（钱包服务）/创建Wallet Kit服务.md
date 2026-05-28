# 创建Wallet Kit服务

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-preparations

请先参考“[应用开发准备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-dev-overview)”完成基本准备工作和指纹配置，再继续以下开发活动。
 1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“我的项目”。
2. 点击进入对应的项目，在左侧“项目设置”页签，上侧导航选择“开放能力管理”，打开华为钱包的开关。用于钱包对车钥匙管理台向钱包服务器发起http/https请求时的权限控制。关闭状态下，开发者服务器将访问不了钱包服务器。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/lNpkHRx7TbattEt4qygJuQ/zh-cn_image_0000002611755231.png?HW-CC-KV=V1&HW-CC-Date=20260528T014434Z&HW-CC-Expire=86400&HW-CC-Sign=CE96F917252B00D50A4372906B0C6A9C092A89D9432E930DA9C9AEF26C0AD894)

3. 在“项目设置”页签，左侧导航选择“盈利 > 华为钱包”，点击“申请Wallet Kit服务”，进入申请Wallet Kit服务。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/5B9lFb6RS6uwJS9TOCQKlw/zh-cn_image_0000002581435292.png?HW-CC-KV=V1&HW-CC-Date=20260528T014434Z&HW-CC-Expire=86400&HW-CC-Sign=D3F96868AFABEC26CB1BDB97D32DC241BE83857BBBFD74F15844406F445472C5)

4. 点击“产品接入华为钱包服务”的“点击申请”按钮。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/A2sNOTM-QtupvowQG3KGag/zh-cn_image_0000002611835123.png?HW-CC-KV=V1&HW-CC-Date=20260528T014434Z&HW-CC-Expire=86400&HW-CC-Sign=1A3E68918D69E4814072F721BBE8DB6BC07C7C4BA904AF5A5719AD7FDFBE1F6D)

5. 各业务场景对应的参数有差异，具体参数请参考各业务的Wallet Kit服务基本信息。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/sP9lbdxkSeysyms4BWwSHQ/zh-cn_image_0000002581275376.png?HW-CC-KV=V1&HW-CC-Date=20260528T014434Z&HW-CC-Expire=86400&HW-CC-Sign=ECDBD5F6846CE31A94458646535AF2ACDB99EB1700787F31E99DE51D58927D7F)


| Wallet Kit服务参数名称 | 参数值 |

| --- | --- |

| 服务类型 | 分为卡、票、券、钥匙等，暂时只支持车钥匙，交通卡服务接入请参考接入交通卡。 |

| 服务项目 | 服务项目依赖所选择的服务类型，不同的服务类型，有不同的服务项目。例如当服务类型选择“卡”时，对应的服务项目有：“会员卡”、“礼品卡”等。 |

| 服务名称 | Wallet Kit首页列表展示该开发者所有创建的服务时，服务名称用于区分不同的服务。 |

| 服务号 | 用于Wallet Kit服务器区分不同的服务且保证唯一性。 |

| 接入方式 | 国内支持三种接入方式，App接入，云端接入，代理接入。商户可以根据自己的需求选择适合自己类型的接入方式。选择云端接入时用户需要填写“回调地址”、“用户公钥”二项资料，选择App接入则只需要上传证书请求文件生成证书即可，选择代理接入时用户需要填写“回调地址”一项资料，而用户公钥则会发送默认值到Wallet Kit服务器。 |

| 回调地址 | 开发者提供给Wallet Kit的地址，用于Wallet Kit回调开发者，用户领卡成功或删卡时回调开发者。 注：如果不需要Wallet Kit通知开发者用户领卡或删卡的状态，可以不填该字段。 |

| 用户公钥 | 开发者将生成的公钥复制粘贴到此处，后续该公钥将作为Wallet Kit服务器认证开发者身份的方式，参考如下公钥生成方式。 |

  **公钥生成方式：**

  （1）配置好node执行环境并使用文本编辑器新建文件，拷贝以下代码到文件中并保存命名为generateKeyPair.js。

  
```text
const crypto = require('crypto');
// 生成密钥对
const { publicKey, privateKey } = crypto.generateKeyPairSync('rsa', {
  modulusLength: 4096, // 密钥长度，不少于4096
  publicKeyEncoding: {
    type: 'spki', // 公钥编码格式
    format: 'der' // 公钥输出格式
  },
  privateKeyEncoding: {
    type: 'pkcs8', // 私钥编码格式
    format: 'der' // 私钥输出格式
  }
});
console.info('生成的公钥：');
console.info(publicKey.toString('base64'));
console.info('生成的私钥：');
console.info(privateKey.toString('base64'));
```
  （2）打开命令行工具，执行**node generateKeyPair.js**命令。

  （3）从结果中拷贝生成的公私钥并保存。结果如下图所示：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/N1BjBjGYSd-lJ2ddyGEY6A/zh-cn_image_0000002611755233.png?HW-CC-KV=V1&HW-CC-Date=20260528T014434Z&HW-CC-Expire=86400&HW-CC-Sign=56FDBFDF29F7C99F148AC9E942B9C477369AB391221A8CEE0E62B68EBC7F6498)

6. 点击“下一步”，进入NFC参数设置页面，各业务场景对应的参数有差异，具体参数请参考各业务的NFC参数。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/9GkOqcmbQpG9HpDgNKxHVg/zh-cn_image_0000002581435294.png?HW-CC-KV=V1&HW-CC-Date=20260528T014434Z&HW-CC-Expire=86400&HW-CC-Sign=42193A341E1138B197D07732CDDC9CE7DD0DF10A67B6B25B20EC7671AC082FFF)


| NFC参数名称 | 参数值 |

| --- | --- |

| 是否支持跨移动设备同步 | 用户领取卡券后可通过此能力在同一账号下的多设备中共享此卡券。商户默认选择“否”即可。 |

| 是否开通NFC能力 | 服务类型为门钥匙、一卡通、门禁卡、社会保障卡、港澳通行证、护照时，需要开通NFC能力，同时需要配置应用号和文件参数。其余的服务类型可以选择不开通NFC能力。 |

| 应用ID | 通过“获取AID”按钮创建新应用ID，内容格式为16进制数（字符为 0-F），最大长度为32（推荐32位），建议以“A000000048575041590100”开头。 |

| 外部认证密钥 | 用于离线读写卡时外部认证校验。内容格式为16进制数（字符为 0-F），最大长度为32（推荐32位）。 |

| 文件参数定义 | 密钥信息，用于对指定文件区域读写权限的控制。内容格式为16进制数（字符为 0-F），最大长度为32（推荐32位）。 |
7. 点击“下一步”，创建完成后，返回Wallet Kit服务创建页面，可对所创建的服务进行查看、修改和删除。
