# Wi-Fi始终连接，如何感知Wi-Fi本身从无网络到有网络的状态

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-97

#### 问题现象

手机连接到未认证的Wi-Fi，认证后无法感知到认证成功，即网络连接成功。
 
 

#### 背景知识

- 设备从无网络到有网络会触发netAvailable事件、netCapabilitiesChange事件和netConnectionPropertiesChange事件。
- 设备从有网络到无网络状态会触发netLost事件。
- 设备从Wi-Fi到蜂窝会触发netLost事件（Wi-Fi丢失）之后触发netAvailable事件（蜂窝可用）。

 
 

#### 解决方案

- 实测该场景不会发送[netAvailable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection#onnetavailable)或[netLost](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection#onnetlost)事件。
- 需要监听[netCapabilitiesChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection#onnetcapabilitieschange)事件，判断connection.NetCapabilityInfo中的[NetCap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection#netcap)类型。若包含NET_CAPABILITY_PORTAL=17（还没有认证时会返回），则表示还没有进行认证，当前网络不可用。

 
先在module.json5文件中配置网络权限[ohos.permission.INTERNET](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/permissions-for-all#ohospermissioninternet)和允许应用获取数据网络信息[ohos.permission.GET_NETWORK_INFO](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/permissions-for-all#ohospermissionget_network_info)。
 
完整示例参考如下：
 
```json
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let netCon: connection.NetConnection = connection.createNetConnection();

@Entry
@Component
struct Connection {
  aboutToAppear(): void {
  <em>  // 先使用register接口注册订阅事件</em>
    netCon.register((error: BusinessError) => {
      console.error(JSON.stringify(error));
    });
  }

  build() {
    Column() {
      Text('开始检测网络状态')
        .onClick(() => {
       <em>   // 订阅网络丢失事件</em>
          netCon.on('netLost', (data: connection.NetHandle) => {
            console.info(`网络丢失: ${data.netId}`);
          });
      <em>    // 订阅网络能力变化事件</em>
          netCon.on('netCapabilitiesChange', (data: connection.NetCapabilityInfo) => {
            console.info(`订阅网络能力变化: ${data.netCap.bearerTypes}`);
          });

       <em>   // 订阅网络可用事件</em>
          netCon.on('netAvailable', (data: connection.NetHandle) => {
            console.info(`网络可用: ${data.netId}`);
          });
        })
    }
  }
}
```
 
 

#### 常见FAQ

Q：开发预下载的功能，需要判断当前app的网络请求为闲时进行下载，是否有相关API可以进行判断？
 
A：可以使用connection模块的[on('netBlockStatusChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection#onnetblockstatuschange)监听事件判断当前网络的阻塞状态。
