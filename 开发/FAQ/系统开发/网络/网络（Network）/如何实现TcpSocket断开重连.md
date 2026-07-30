# 如何实现TcpSocket断开重连

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-125

#### 问题现象

TcpSocket异常断开连接后，如何实现循环重连？
 
 

#### 背景知识

建立TcpSocket连接前，需要通过[constructTCPSocketInstance](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-socket#socketconstructtcpsocketinstance7)创建tcp实例，然后才能调用[connect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-socket#connect)接口连接指定tcp服务。若是TcpSocket异常断开，需调用[close](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-socket#close-2)接口销毁之前的实例，然后重新创建TcpSocket实例，调用connect接口尝试重连。
 
 

#### 解决方案

TcpSocket不具备自动回连机制，开发者需要通过业务逻辑实现循环重连，具体实现可参考如下代码：
 
```json
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct TcpSocketReconnect {
  <em>// 1.tcpSocket实例</em>
  @State tcpSocket: socket.TCPSocket | null = null;

 <em> // 2.创建socket实例</em>
  createSocket() {
    this.tcpSocket = socket.constructTCPSocketInstance();
    this.registerEvents();
  }

<em>  // 3.注册事件监听</em>
  registerEvents() {
    this.tcpSocket?.on('close', () => {
      console.info('Connection closed');
      <em>// </em><em>获取当前tcpSocket连接状态</em>
      this.tcpSocket?.getState((err: BusinessError, data: socket.SocketStateBase) => {
        if (err) {
          console.error('getState fail');
          return;
        }
        console.info('getState success:', JSON.stringify(data));
      <em>  // 如果tcpSocket未关闭连接，释放旧连接，然后开始重连</em>
<em>        // 如果tcpSocket已关闭连接，说明用户需要主动断开，无需重连</em>
        if (data.isConnected) {
          try {
            this.tcpSocket?.close();
          } catch (err) {
            console.error('Close error:', JSON.stringify(data));
          }
          <em>// </em><em>触发重连。注：此处应根据开发者业务所需，判断是否需要触发重连</em>
          this.reconnect();
        }
      });
    });

    this.tcpSocket?.on('error', (err: BusinessError) => {
      console.error('Error occurred:', JSON.stringify(err));
      this.reconnect();<em> </em><em>// 错误时触发重连</em>
    });
  }

<em>  // 4.实现重连逻辑</em>
  reconnect() {
    console.info('Reconnecting...');
   <em> // 创建新连接</em>
    this.createSocket();
    this.connectToServer();

  }

  <em>// 5.建立连接</em>
  connectToServer() {
    let address: socket.NetAddress = {
      address: '36.137.xxx.xxx',
      port: 8080
    };
    this.tcpSocket?.connect({ address, timeout: 5000 }, (err: BusinessError) => {
      if (err) {
        console.error('Connect failed:', JSON.stringify(err));
        return;
      }
      console.info('Connect success');
    });
  }

  build() {
    Column() {
      Button('初始化实例/创建回连机制').onClick(() => {
        <em>// </em><em>初始化实例/创建回连机制</em>
        this.createSocket();
      }).margin(15);
      Button('建立连接').onClick(() => {
     <em>   // 建立连接</em>
        this.connectToServer();
      });
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.SpaceAround);
  }
}
```
