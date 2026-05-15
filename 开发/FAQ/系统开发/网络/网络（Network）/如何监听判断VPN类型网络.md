# 如何监听判断VPN类型网络

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-67

VPN类型可使用getNetCapabilities方法获取到bearerTypes，当bearerTypes的值是4时表示使用了VPN。需要权限：ohos.permission.INTERNET、ohos.permission.GET_NETWORK_INFO。

参考代码如下：

```ts
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
export struct JudeNetType {
getNetType() {
connection.getAllNets((error: BusinessError, allNets: connection.NetHandle[]) => {
if (error) {
console.error(`Failed to get getAllNets. Code: ${error.code}, message: ${error.message}`);
return;
}
for (let netHandle of allNets) {
connection.getNetCapabilities(netHandle, (error: BusinessError, data: connection.NetCapabilities) => {
if (error) {
console.error(`Failed to get capabilities. Code: ${error.code}, message: ${error.message}`);
return;
}
if (data.bearerTypes[0] == connection.NetBearType.BEARER_VPN) {
console.info('The VPN network is connected');
}
})
}
});
}

build() {
Column({ space: 10 }) {
Button('Obtain the type of network connection').onClick(() => {
this.getNetType()
})
}.alignItems(HorizontalAlign.Center)
.height('100%')
.width('100%')
}
}
```

参考文档：网络连接管理
