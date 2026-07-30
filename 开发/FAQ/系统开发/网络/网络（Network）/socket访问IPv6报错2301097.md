# socket访问IPv6报错2301097

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-92

#### 问题现象

socket访问IPv6失败，会报错：{"code":2301097,"message":"Address family not supported by protocol"}。
 
 

#### 背景知识

socket模块支持通过[bind](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-socket#bind-2)接口显式绑定IPv6地址和端口。
 
 

#### 问题定位

排查目标地址信息[NetAddress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-socket#netaddress)中参数配置是否有误。
 
 

#### 分析结论

根据报错信息Address family not supported by protocol和代码示例可知，问题出在地址信息配置上面。由于NetAddress中family参数默认为IPv4，如果不重新配置family参数，使用的将会是IPv4网络。
 
 

#### 修改建议

将NetAddress中family参数设置为2，用以支持访问IPv6网络。
 
```json
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct TlsSocketBind {
 <em> // tlsSocket实例</em>
  @State tls: socket.TLSSocket = socket.constructTLSSocketInstance();

  <em>// </em><em>绑定tls</em>
  bind() {
   <em> // 网络协议类型，可选类型：</em>
<em>    // - 1：IPv4。默认为1。</em>
<em>    // - 2：IPv6。地址为IPV6类型，该字段必须被显式指定为2。</em>
<em>    // - 3：Domain。地址为Domain类型，该字段必须被显式指定为3。</em>
    let bindAddr: socket.NetAddress = {
      address: '::1', <em>// address需要根据实际地址进行填写</em>
      port: 8080,
      family: 2
    };
    this.tls.bind(bindAddr, (err: BusinessError) => {
      if (err) {
        console.info('绑定失败', JSON.stringify(err));
        return;
      }
      console.info('绑定成功');
    });
  }

  build() {
    Column() {
      Button('开始绑定tls').onClick(() => {
      <em>  // 开始绑定tls</em>
        this.bind();
      });
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.SpaceAround);
  }
}
```
