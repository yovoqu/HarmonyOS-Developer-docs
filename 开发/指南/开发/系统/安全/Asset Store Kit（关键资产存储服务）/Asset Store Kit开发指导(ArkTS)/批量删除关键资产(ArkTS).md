# 批量删除关键资产(ArkTS)

更新时间：2026-06-12 06:54:11

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-js-batch-remove

#### 接口介绍

从版本26.0.0开始，系统提供异步接口[batchRemove](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-asset#assetbatchremove)以便开发者批量删除关键资产。

在批量删除关键资产时，关键资产属性的内容（AssetMap）参数如下表所示：


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/iR0WwFG3RK2tW9X_JZHRXA/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260701T041502Z&HW-CC-Expire=86400&HW-CC-Sign=D05A37A34CB831E884C732BBA1E5A93996DC20EA6D334CD1E4715F852508FD03)


下表中“ALIAS”和名称包含“DATA_LABEL”的关键资产属性，用于存储业务自定义信息，其内容不会被加密，请勿存放敏感个人数据。



| 属性名称（Tag） | 属性内容（Value） | 是否必选 | 说明 |
| --- | --- | --- | --- |
| ALIAS | 类型为Uint8Array，长度为1-256字节。 | 必选 | 关键资产别名，每条关键资产的唯一索引。 |
| REQUIRE_ATTR_ENCRYPTED14+ | 类型为boolean。 | 可选 | 是否删除业务自定义附属信息被加密的数据。为true时表示删除业务自定义附属信息加密存储的数据，为false时表示删除业务自定义附属信息不加密存储的数据。默认值为false。 |
| GROUP_ID18+ | 类型为Uint8Array，长度为7-127字节。 | 可选 | 待删除的关键资产所属群组，默认删除不属于任何群组的关键资产。 |




#### 约束和限制

批量删除的关键资产必须具有相同的[GROUP_ID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-asset#tag)和[REQUIRE_ATTR_ENCRYPTED](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-asset#tag)属性。

批量删除的关键资产数量最大值为100。



#### 开发步骤

> [!NOTE]
> 以下为批量刪除接口的使用示例。 在删除前，需确保已有关键资产，可参考 指南文档 新增关键资产，否则将抛出NOT_FOUND错误（错误码24000002）。


批量删除两条别名分别为demo_alias1和demo_alias2的关键资产。
1. 引用头文件，定义工具函数。

  
```ArkTS
import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}
```

2. 参考如下示例代码，进行业务功能开发。

  
```ArkTS
let assetsToBeRemoved: asset.AssetMap[] = [];
let query1: asset.AssetMap = new Map();
query1.set(asset.Tag.ALIAS, stringToArray('demo_alias1'));
assetsToBeRemoved.push(query1);
let query2: asset.AssetMap = new Map();
query2.set(asset.Tag.ALIAS, stringToArray('demo_alias2'));
assetsToBeRemoved.push(query2);

try {
  asset.batchRemove(assetsToBeRemoved).then(() => {
    console.info(`Succeeded in batch removing Asset.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to batch remove Asset. Code is ${err.code}, message is ${err.message}`);
  })
} catch (error) {
  let err = error as BusinessError;
  console.error(`Failed to batch remove Asset. Code is ${err.code}, message is ${err.message}`);
}
```
