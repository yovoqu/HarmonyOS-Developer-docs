# Emitter线程间通信对象传递问题

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-63

#### 问题现象

Emitter发送的数据中如果包含复杂对象，在订阅回调中无法获取复杂对象的属性。
 
 

#### 背景知识

- [使用Emitter进行线程间通信](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/itc-with-emitter)。
- [sendable使用场景](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sendable-guide)。

 
 

#### 解决方案

线程间通信共享对象，需封装成sendable对象。代码示例如下：
 
```text
import { emitter } from '@kit.BasicServicesKit';

@Sendable
class Sample {
  constructor() {
    this.count = 100;
  }

  printCount() {
    console.info('Print count : ' + this.count);
  }

  count: number;
}

class SelfEventData implements emitter.EventData {
  data: Sample = new Sample();
}

let options: emitter.Options = {
  priority: emitter.EventPriority.HIGH
};

let eventData = new SelfEventData();

<em>// 订阅事件</em>
emitter.on('eventId', (eventData: SelfEventData) => {
  console.log('Event received:', eventData.data);
  eventData.data.printCount();
});

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button('点击')
        .onClick(() => {
          console.log('Button clicked');
         <em> // 点击后打印当前 count 值</em>
          console.log('Current count:', eventData.data.count);
        <em>  // 发送事件</em>
          emitter.emit('eventId', options, eventData);
        });
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```
