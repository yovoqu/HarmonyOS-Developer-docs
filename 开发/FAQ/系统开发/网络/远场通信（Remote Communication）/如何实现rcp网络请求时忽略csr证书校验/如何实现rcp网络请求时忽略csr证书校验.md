# 如何实现rcp网络请求时忽略csr证书校验

更新时间：2026-07-30 01:55:38

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-remote-communication-6

#### 问题现象

在开发测试阶段，连接自签证书服务器或测试环境时，因无法通过系统默认的证书链校验导致请求失败。开发者需要在使用[rcp 数据请求](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-rcp)时，临时忽略或跳过服务端的证书校验。
 
 

#### 背景知识

[Remote Communication Kit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-api)提供了网络数据请求功能。相较于传统HTTP请求能力，它拥有更优的性能表现与更丰富的配置项。
 
针对证书校验，Remote Communication Kit提供了两种灵活的规避/自定义校验机制：
 1. 自定义配置 [ValidationCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-rcp#validationcallback)：通过重写验证回调，手动控制校验逻辑。
2. 直接显式跳过（Skip）：将[SecurityConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-rcp#securityconfiguration)中的安全配置项remoteValidation设为 'skip'，由底座直接放行。
 
 

#### 解决方案

- **方案一：**自定义requestConfig对象，重写[ValidationCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-rcp#validationcallback)。remoteValidation在实际的证书验证中，这个函数会检查证书的有效性等信息，这里返回true来忽略证书校验，样例代码如下：

  
```text
const requestConfig: rcp.Configuration = {
  security: {
    remoteValidation: () => {
    <em>  // 重写ValidationCallback，直接返回true表示验证通过</em>
      console.info('[index]证书验证');
      return true;
    }
  }
```

- **方案二：**设置remoteValidation参数为skip，用于跳过证书验证，样例代码如下：

  
```text
const securityConfig: rcp.SecurityConfiguration = {
  remoteValidation: 'skip'
};
```
 完整示例代码集成了两种方案处理证书校验，代码如下：

  
```text
import { BusinessError } from '@ohos.base';
import promptAction from '@ohos.promptAction';
import { rcp } from '@kit.RemoteCommunicationKit';
import { util } from '@kit.ArkTS';

@Entry
@Component
struct RcpConnection {
  build() {
    RelativeContainer() {
      Button('自定义证书验证')
        .id('btn1')
        .fontSize(14)
        .fontWeight(FontWeight.Bold)
        .width('60%')
        .height('50vp')
        .padding({
          left: '16vp',
          right: '16vp',
          top: '12vp',
          bottom: '12vp'
        })
        .alignRules({
          middle: { anchor: '__container__', align: HorizontalAlign.Center },
          bottom: { anchor: 'btn2', align: VerticalAlign.Top }
        })
        .margin({ bottom: '20vp' })
        .onClick(() => {
          this.testRcpConnection();
        });

      Button('跳过证书验证')
        .id('btn2')
        .fontSize(14)
        .fontWeight(FontWeight.Bold)
        .width('60%')
        .height('50vp')
        .padding({
          left: '16vp',
          right: '16vp',
          top: '12vp',
          bottom: '12vp'
        })
        .alignRules({
          middle: { anchor: '__container__', align: HorizontalAlign.Center },
          center: { anchor: '__container__', align: VerticalAlign.Center }
        })
        .onClick(() => {
          this.testRcpConnection2();
        });
    }
    .height('100%')
    .width('100%');
  }

  async testRcpConnection() {
    try {
      const requestConfig: rcp.Configuration = {
        security: {
          remoteValidation: () => {
         <em>   // 重写ValidationCallback，直接返回true表示验证通过</em>
            console.info('[index]证书验证');
            return true;
          }
        }
      };

   <em>   // 服务器地址</em>
      const kHttpServerAddress = 'xx.xx.xx';
   <em>   // 创建一个get请求对象</em>
      const request = new rcp.Request(kHttpServerAddress, 'GET');
    <em>  // 传入自定义的配置项，处理请求</em>
      const session = rcp.createSession({ requestConfiguration: requestConfig });
      const resp = await session.fetch(request);
      let decoder: util.TextDecoder = util.TextDecoder.create('utf-8');
      let body: string = decoder.decodeToString(new Uint8Array(resp.body));
   <em>   // 显示提示信息，包含响应成功的消息和响应体内容</em>
      promptAction.openToast({ message: '连接成功' });
      console.info('连接成功: ' + body);
    } catch (error) {
      let err = error as BusinessError;
      promptAction.openToast({ message: `错误: ${err.message}` });
      console.error('[index]连接错误:', err);
    }
  }


  async testRcpConnection2() {
    try {
      const securityConfig: rcp.SecurityConfiguration = {
        remoteValidation: 'skip'
      };

   <em>   // 服务器地址</em>
      const kHttpServerAddress = 'xx.xx.xx';
   <em>   // 创建一个get请求对象</em>
      const request = new rcp.Request(kHttpServerAddress, 'GET');
      <em>// 传入自定义的配置项，处理请求</em>
      const sessionWithSecurityConfig = rcp.createSession({ requestConfiguration: { security: securityConfig } });
      const resp = await sessionWithSecurityConfig.fetch(request);
      let decoder: util.TextDecoder = util.TextDecoder.create('utf-8');
      let body: string = decoder.decodeToString(new Uint8Array(resp.body));
     <em> // 显示提示信息，包含响应成功的消息和响应体内容</em>
      promptAction.openToast({ message: '连接成功' });
      console.info('连接成功: ' + body);
    } catch (error) {
      let err = error as BusinessError;
      promptAction.openToast({ message: `错误: ${err.message}` });
      console.error('[index]连接错误:', err);
    }
  }

}
```
