# 如何让事件只在一个UIAbility实例中传递

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-notification-kit-2

在UIAbility中使用EventHub订阅事件，EventHub模块提供了事件中心，订阅、取消订阅、触发事件的能力。
 
参考代码如下：
 
```text
import { UIAbility } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    this.context.eventHub.on('myEvent', this.eventFunc);
   <em> // result：</em>
<em>    // eventFunc is called,undefined,undefined</em>
    this.context.eventHub.emit('myEvent');
  <em>  // result：</em>
<em>    // eventFunc is called,1,undefined</em>
    this.context.eventHub.emit('myEvent', 1);
  <em>  // result：</em>
<em>    // eventFunc is called,1,2</em>
    this.context.eventHub.emit('myEvent', 1, 2);
  }

  eventFunc(argOne: number, argTwo: number) {
    console.log(`eventFunc is called, ${argOne}, ${argTwo}`);
  }
}
```
 

#### 参考链接

[使用EventHub进行数据通信](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-data-sync-with-ui#使用eventhub进行数据通信)
