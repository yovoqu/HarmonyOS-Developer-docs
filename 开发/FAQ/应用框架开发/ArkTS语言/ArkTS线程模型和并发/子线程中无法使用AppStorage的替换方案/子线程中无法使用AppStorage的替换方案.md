# 子线程中无法使用AppStorage的替换方案

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-threading-model-5

#### 问题现象

在ArkTS并发开发过程中，子线程需要用到AppStorage这类UI资源时，子线程中无法直接访问，有无其他替换方案？（本文以taskpool中使用AppStorage为例说明）。
 
 

#### 背景知识

- [ArkTS的并发模型](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-thread-concurrency-overview#actor模型)： 和其他所有基于JS引擎的语言一样，都是基于Actor内存隔离的并发模型，每个线程都有自己独立的内存空间，线程之间通过消息传递机制进行通信，不会直接访问对方的内存空间。taskpool属于ArkTS提供的并发方案之一，Actor模型图如下所示：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/7oWO1fhkRlKy5MChTnZm0g/zh-cn_image_0000002659258287.png?HW-CC-KV=V1&HW-CC-Date=20260730T072305Z&HW-CC-Expire=86400&HW-CC-Sign=90E7A3A3B7D69FE5E9B815E46C7B6562C30B10B80CA8D3FCAE9BEB191020020B)

- [AppStorage](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-appstorage)是应用全局的UI状态存储，和应用的进程绑定，只能在UI主线程中使用，无法在子线程中使用、修改。
- [Emitter](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/itc-with-emitter)是一种作用在进程内的事件处理机制，为应用程序提供订阅事件、发布事件、取消事件订阅的能力。
- [共享用户首选项](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-sendablepreferences)为应用提供Key-Value键值型的数据处理能力，支持应用持久化轻量级数据，并对其修改和查询。

 
 

#### 解决方案

由上面的背景知识可知，AppStorage一般存放应用全局的UI状态，供UI主线程使用，taskpool子线程中无法直接使用，如果想要实现taskpool子线程访问全局UI状态，有以下三种方案：
 
- **方案一**：借助taskpool参数传递。1. 将需要在子线程中使用的数据从AppStorage中抽取出来，封装成类。

2. 在UI主线程新建taskpool时，通过初始化参数直接将AppStorage指定的值传递给taskpool子线程。

3. 如果taskpool子线程需要修改AppStorage值且通知UI主线程，可以通过taskpool.Task.sendData发送，UI主线程接收再处理UI刷新。

  
```text
import { taskpool } from '@kit.ArkTS';

@Concurrent
async function taskpoolFunc2(vaTmp: AppstorageTmpValues): Promise<AppstorageTmpValues> {
 <em> // 在taskpool子线程中直接读AppStorage里面的值,会报错ReferenceError: AppStorage is not defined</em>
  console.info('taskpool backupId:' + vaTmp.backupId); <em>// 输出22222</em>
  console.info('taskpool isLightMode:' + vaTmp.isLightMode); <em>// 输出true</em>
  taskpool.Task.sendData(vaTmp);
  vaTmp.backupId = '33333';
  vaTmp.isLightMode = false;
  taskpool.Task.sendData(vaTmp);
  return vaTmp;
}

async function mainFunc(): Promise<void> {
  AppStorage.setOrCreate('backupId', '22222');
  let appStateTmp: AppstorageTmpValues = {
    isLightMode: AppStorage.get('isLightMode') as boolean,
    backupId: AppStorage.get('backupId') as string
  };
<em>  // 直接将AppStorage指定值作为参数传递给taskpool子线程</em>
  let task2: taskpool.Task = new taskpool.Task(taskpoolFunc2, appStateTmp);
<em>  // 设置notice方法接收子线程发送的消息</em>
  task2.onReceiveData(notice);
  let res2: AppstorageTmpValues = await taskpool.execute(task2) as AppstorageTmpValues;
  console.info("ui main get backupId: " + res2.backupId); // 输出33333
  console.info("ui main get isLightMode: " + res2.isLightMode); // 输出false
}

function notice(data: AppstorageTmpValues): void {
  console.info("接收并解析子线程发出的消息");
  console.info('backupId:' + data.backupId);
  console.info('isLightMode:' + data.isLightMode);
  AppStorage.setOrCreate('backupId', data.backupId);
  AppStorage.setOrCreate('isLightMode', data.isLightMode);
}

@Entry
@Component
struct WayOne {
  @StorageLink('isLightMode') isLightMode: boolean = true;
  @StorageLink('backupId') backupId: string = '11111';

  aboutToAppear(): void {
    AppStorage.setOrCreate('isLightMode', true);
    AppStorage.setOrCreate('backupId', '11111');
  }

  build() {
    Row() {
      Column({ space: 10 }) {
        Text(`isLightMode:${this.isLightMode}`);
        Text(`backupId:${this.backupId}`);
        Button('taskpoolEmitterTest')
          .onClick(async () => {
            mainFunc();
          });
      }
      .width('100%')
      .height('100%');
    };
  }
}

export interface AppstorageTmpValues {
  isLightMode?: boolean;
  backupId?: string;
}
```

- **方案二**：借助进程不同线程间Emitter事件处理机制。这里以主线程通知子线程，在子线程中访问AppStorage为例说明：

1. 在主线程中将AppStorage中的数据读取到emitter.EventData，创建emitter事件。

2. 在主线程中将事件数据发送给子线程。

3. 在子线程中读取事件数据，进行使用。

  
```text
import { emitter } from '@kit.BasicServicesKit';
import { taskpool } from '@kit.ArkTS';

@Concurrent
async function taskpoolFunc(isLightModeTmp: boolean): Promise<string> {
  console.info('UI主线程过来数据isLightMode:' + isLightModeTmp);
  let backupIdTmp: string = '';
 <em> // 在taskpool子线程中直接读AppStorage里面的值,会报错ReferenceError: AppStorage is not defined</em>
  emitter.on("eventIdTmp", (eventData: emitter.EventData) => {
    let data = eventData?.data;
    if (data) {
      const isLightMode: boolean = data.isLightMode as boolean;
      backupIdTmp = data.backupId as string;
      console.info('通过emitter接收UI主线程的isLightMode:' + isLightMode);
      console.info('通过emitter接收UI主线程的backupId:' + backupIdTmp);
    }
  });
  return backupIdTmp;
}

async function mainFunc(): Promise<void> {
 <em> // 直接将AppStorage值作为参数传递给taskpool子线程</em>
  let task1: taskpool.Task = new taskpool.Task(taskpoolFunc, AppStorage.get('isLightMode') as boolean);
  let res1: string = await taskpool.execute(task1) as string;
 <em> // 调整AppStorage里面的值</em>
  AppStorage.setOrCreate('backupId', '8111122555');
  let eventData: emitter.EventData = {
    data: {
      "isLightMode": AppStorage.get('isLightMode'),
      "backupId": AppStorage.get('backupId'),
    }
  };
<em>  // 通过emitter将UI主线程的AppStorage作为消息发送给taskpool子线程</em>
  emitter.emit("eventIdTmp", eventData);
  console.info("taskpool: task res1 is: " + res1);
}

@Entry
@Component
struct WayTwo {
  aboutToAppear(): void {
    AppStorage.setOrCreate('isLightMode', true);
    AppStorage.setOrCreate('backupId', '8976756778');
  }

  build() {
    Row() {
      Column() {
        Button('taskpoolEmitterTest')
          .onClick(async () => {
            mainFunc();
          });
      }
      .width('100%')
      .height('100%');
    };
  }
}
```

- **方案三**：借助持久化方案sendablePreferences共享用户首选项。1. 将子线程需要使用的值，直接存储到sendablePreferences中。

2. 使用taskpool将sendablePreferences发送给子线程。

3. 在子线程中直接对sendablePreferences进行读取、访问数据。

  
```text
import { sendablePreferences } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';
import { lang, taskpool } from '@kit.ArkTS';

let preferences: sendablePreferences.Preferences;

@Concurrent
async function taskpoolFunc(preferences: sendablePreferences.Preferences): Promise<void> {
 <em> // taskpool子线程从共享用户首选项获取backupId</em><em>配置值，默认取不到返回空</em>
  let backupIdTmp: string = '';
  let backupIdPromise = preferences.get('backupId', '');
  backupIdPromise.then((data: lang.ISendable) => {
    backupIdTmp = data as string;
    console.info('taskpoolFunc backupIdTmp:' + backupIdTmp);
  }).catch((err: BusinessError) => {
    console.error(`Failed to get value of 'backupId'. code: ${err.code}, message: ${err.message}`);
  });
}

async function mainFunc(): Promise<void> {
<em>  // UI主线程中从共享用户首选项获取isLightMode</em><em>配置值，默认取不到返回</em>false
  let isLightModeTmp = false;
  let isLightModePromise = preferences.get('isLightMode', false);
  isLightModePromise.then((data: lang.ISendable) => {
    isLightModeTmp = data as boolean;
    console.info('mainFunc isLightModeTmp:' + isLightModeTmp);
  }).catch((err: BusinessError) => {
    console.error(`Failed to get value of 'isLightMode'. code: ${err.code}, message: ${err.message}`);
  });

 <em> // UI主线程中从共享用户首选项获取backupId配置值，默认取不到返回空</em>
  let backupIdTmp = '';
  let backupIdPromise = preferences.get('backupId', '');
  backupIdPromise.then((data: lang.ISendable) => {
    backupIdTmp = data as string;
    console.info('mainFunc backupIdTmp:' + backupIdTmp);
  }).catch((err: BusinessError) => {
    console.error(`Failed to get value of 'backupId'. code: ${err.code}, message: ${err.message}`);
  });

 <em> // 将共享首选项的preferences（继承自ISendable）引用传递给taskpool子线程</em>
  let task: taskpool.Task = new taskpool.Task(taskpoolFunc, preferences);
  await taskpool.execute(task);
}

@Entry
@Component
struct WayThree {
  aboutToAppear(): void {
  <em>  // 创建AppStorage</em>
    AppStorage.setOrCreate('isLightMode', true);
    AppStorage.setOrCreate('backupId', '8976756778');
 <em>   // 添加sendablePreferences相关项</em>
    let options: sendablePreferences.Options = { name: 'myStore' };
    let context = this.getUIContext().getHostContext()!;
    let promise = sendablePreferences.getPreferences(context, options);
    promise.then((object: sendablePreferences.Preferences) => {
      preferences = object;
   <em>   // 写入sendablePreferences首选项键值</em>
      preferences.put('isLightMode', AppStorage.get('isLightMode') as boolean);
      preferences.put('backupId', AppStorage.get('backupId') as string);
      console.info("Succeeded in getting preferences.");
    }).catch((err: BusinessError) => {
      console.error(`Failed to get preferences. code: ${err.code}, message: ${err.message}`);
    });
  }

  build() {
    Row() {
      Column() {
        Button('taskpoolSendablePreferenceTest')
          .onClick(async () => {
            mainFunc();
          });
      }
      .width('100%')
      .height('100%');
    };
  }
}
```


 
 

#### 常见FAQ

Q：使用Emitter方案，Uint8Array类型的成员变量，或者对象数组传递时会丢失吗？
 
A：发送事件时传递的数据，支持数据类型包括Array、ArrayBuffer、Boolean、DataView、Date、Error、Map、Number、Object、Primitive（除了symbol）、RegExp、Set、String、TypedArray，数据大小要求最大为16M。Uint8Array类型和对象数组支持传递。需注意发送接收是同一个事件id，同时确认支持传输的数据大小是否符合要求。
 
Q：taskpool.execute没有并行执行，系统卡住没反应？
 
A：属于taskpool基础语法问题，需要检查下待执行的并行方法有没有使用@Concurrent装饰器装饰。
 
Q：使用Emitter方案，如何立即触发emitter.once？
 
A：将[emitter.emit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-emitter#emitteremit12-1)接口的Options参数，设置为IMMEDIATE，表示事件被立即投递。
 
 

#### 总结
 
| 方案 | 优缺点 |
| --- | --- |
| 方案一 | 此方案简单快速，但子线程中接收的AppStorage相关组装对象非引用传递，修改完成需要主动通知主线程，该方案优先推荐。 |
| 方案二 | 此方案响应速度快，且事件处理机制提供了丰富的API调用，支持设置事件响应优先级，该方案优先推荐。 |
| 方案三 | 此方案可以把Preferences对象按引用传递给子线程，子线程中可以访问首选项的所有键值对，无需再次封装对象，但是共享用户首选项无法保证进程并发安全，会有文件损坏和数据丢失的风险，不建议在多线程场景下并发修改使用，以只读取方式使用较保险；此外较直接传AppStorage参数值或Emitter发送订阅事件，首选项方案读取较慢，对速度要求高的场景不是最优选择。 |
