# 如何使用EventHub替代EventBus实现事件通信

更新时间：2026-07-22 11:59:07

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-176

#### 问题现象

在HarmonyOS应用开发中，当需要进行组件间或模块间的事件发布与订阅以实现解耦通信时，部分三方库（如EventBus）可能未提供HarmonyOS适配版本。开发者需要寻找系统提供的替代方案来实现基于发布-订阅模式的事件通信机制。
 
 

#### 背景知识

EventHub是HarmonyOS系统提供的基于发布-订阅模式实现的事件通信机制。通过事件名，实现了发送方和订阅方之间的解耦，支持不同业务模块间的高效数据传递和状态同步。更多参考请参见[EventHub](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-eventhub)。
 
 

#### 解决方案

使用系统提供的EventHub替代EventBus。通过UIAbilityContext获取EventHub实例，使用on方法订阅事件，使用emit方法发送事件，并在Ability销毁时调用off方法取消订阅以避免内存泄漏。在ArkUI组件中，可通过getContext(this)获取UIAbilityContext，从而在组件侧使用EventHub进行事件通信。
 
以下示例在EntryAbility中演示事件的订阅、发送与取消订阅，并提取统一的错误处理函数以减少代码重复：
```text
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  value: number = 12;

  <em>// 统一错误处理函数</em>
  handleEventError(e: BusinessError) {
    let code: number = e.code;
    let msg: string = e.message;
    console.error(`EventHub error, code: ${code}, msg: ${msg}`);
  }

  onCreate() {
    try {
      <em>// 支持使用匿名函数订阅事件</em>
      this.context.eventHub.on('myEvent', () => {
        console.info(`anonymous eventFunc is called, value: ${this.value}`);
      });
    } catch (e) {
      this.handleEventError(e as BusinessError);
    }
  }

  onForeground() {
    try {
      <em>// 结果：</em>
      <em>// anonymouseventFunciscalled, value: 12</em>
      this.context.eventHub.emit('myEvent');
    } catch (e) {
      this.handleEventError(e as BusinessError);
    }
  }

  onDestroy() {
    <em>// 销毁时取消事件订阅，避免内存泄漏</em>
    try {
      this.context.eventHub.off('myEvent');
    } catch (e) {
      this.handleEventError(e as BusinessError);
    }
  }
}
```
 
 
以下示例在ArkUI组件中通过getContext(this)获取UIAbilityContext，演示组件侧的事件订阅与发送：
```text
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  value: number = 10;

  aboutToAppear() {
    <em>// 在组件中通过getContext(this)获取UIAbilityContext</em>
    let context = getContext(this) as common.UIAbilityContext;
    try {
      context.eventHub.on('componentEvent', () => {
        console.info(`componentEvent is called, value: ${this.value}`);
      });
    } catch (e) {
      let code: number = (e as BusinessError).code;
      let msg: string = (e as BusinessError).message;
      console.error(`subscribe componentEvent failed, code: ${code}, msg: ${msg}`);
    }
  }

  aboutToDisappear() {
    <em>// 组件销毁时取消订阅，避免内存泄漏</em>
    let context = getContext(this) as common.UIAbilityContext;
    try {
      context.eventHub.off('componentEvent');
    } catch (e) {
      let code: number = (e as BusinessError).code;
      let msg: string = (e as BusinessError).message;
      console.error(`unsubscribe componentEvent failed, code: ${code}, msg: ${msg}`);
    }
  }

  build() {
    Column() {
      Button('发送事件')
        .onClick(() => {
          let context = getContext(this) as common.UIAbilityContext;
          try {
            context.eventHub.emit('componentEvent');
          } catch (e) {
            let code: number = (e as BusinessError).code;
            let msg: string = (e as BusinessError).message;
            console.error(`emit componentEvent failed, code: ${code}, msg: ${msg}`);
          }
        })
    }
  }
}
```
