# 如何解决网络连接状态变化的公共事件返回内容为"NetType":1的问题

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-60

返回"NetType":1枚举值表示为NET_CONN_STATE_IDLE网络空闲状态。
 
如果是监听网络变化，建议使用@ohos.net.connection的能力，请参考[@ohos.net.connection (网络连接管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection)。
 
代码示例如下：
 
```json
import { connection } from '@kit.NetworkKit';
import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';

function  listen_network() {
  let netSpecifier: connection.NetSpecifier = {
    netCapabilities: {
      <em>// Assuming the current default network is WiFi, a cellular network connection needs to be created, and the network type can be specified as cellular network</em>
      bearerTypes: [connection.NetBearType.BEARER_CELLULAR, connection.NetBearType.BEARER_WIFI],
    },
  };
  let conn = connection.createNetConnection(netSpecifier);

  conn.register((err: BusinessError, data: void) => {
    console.warn('register Network ' + JSON.stringify(err))
  });

  <em>// Subscription event, network available</em>
  conn.on('netAvailable', ((data: connection.NetHandle) => {
    console.warn('Network available, netId is ' + data.netId);
  }));

  <em>// Subscription event, network available</em>
  conn.on('netCapabilitiesChange', ((data: connection.NetCapabilityInfo) => {
    console.warn('Network netCapabilitiesChange bearerTypes ' + data.netCap.bearerTypes);
    console.warn('Network netCapabilitiesChange networkCap ' + data.netCap.networkCap);
  }));

  <em>// Subscription event, network unavailable</em>
  conn.on('netUnavailable', ((data: void) => {
    console.warn('The network is unavailable, data is ' + JSON.stringify(data));
  }));

  <em>// Subscription event, network disconnection</em>
  conn.on('netLost', ((data: connection.NetHandle) => {
    console.warn('Network lost, netId is ' + data.netId);
  }));
}

<em>// After monitoring an event, it is necessary to obtain the network status through a network interface</em>
function sub_network() {
  console.warn('into sub_network')
  <em>// Public event monitoring code:</em>
  let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
    <em>// Subscription message exception public event</em>
    events: ['usual.event.CONNECTIVITY_CHANGE']
  }

  <em>// Create subscriber callback</em>
  commonEventManager.createSubscriber(subscribeInfo, (err: BusinessError, subscriber: commonEventManager.CommonEventSubscriber) => {
    if (err) {
      console.warn(`Failed to create netWorkSubscribeInfo. Code is ${err.code}, message is ${err.message}`);
      return;
    }
    if (subscribeInfo && subscribeInfo != null) {
      <em>// Subscribe to public event callbacks</em>
      commonEventManager.subscribe(subscriber, (err: BusinessError, data: commonEventManager.CommonEventData) => {
        if (err) {
          console.warn(`Failed to netWorkSubscribe common event. Code is ${err.code}, message is ${err.message}`);
          return;
        }
        console.warn('NET_CONNECTIVITY_CHANGE：' + JSON.stringify(data.parameters));

        setTimeout(async () => {
          connection.getDefaultNet((error, data) => {
            console.log(JSON.stringify(error))
            console.log(JSON.stringify(data))
          }) }, 500);
        <em>// The log printed here is{'NetType':1,'moduleName':''}</em>
      })
    }
  })
}

@Entry
@Component
struct NetWork {
  build() {
    Row() {
      Column() {
        Button('Monitor the network').onClick(() => {
          listen_network()
        })
        Button('Obtain the network status').onClick(() => {
          sub_network()
        })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
