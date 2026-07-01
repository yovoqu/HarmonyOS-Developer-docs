# TaskPool创建多线程修改单例对象变量失败问题如何解决

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-threading-model-12

#### 问题现象

在TaskPool里对单例的成员变量进行了修改，主线程读取到的仍然是修改前的值。
 
 

#### 背景知识

- [共享模块](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable-module)是进程内只会加载一次的模块，使用"use shared"这一指令来标记一个模块是否为共享模块。
- [并发](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/concurrency-overview)指在同一时间内，多个任务同时执行。在多核设备上，任务可以在不同CPU上并行执行。
- [多线程并发](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-thread-concurrency-overview)是指在单个程序中同时运行多个线程，通过并行或交替执行任务来提升性能和资源利用率的编程模型。

 
 

#### 问题定位

当前ArkTS提供了[TaskPool](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/taskpool-async-task-guide)和[Worker](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/worker-introduction)两种并发能力，TaskPool和Worker都基于Actor并发模型实现。
 
在Actor并发模型中，不同线程不会使用同一个单例对象。每个线程都有自己独立的内存空间，线程之间通过消息传递机制进行通信，不会直接访问对方的内存空间，在TaskPool中对单例对象的成员变量进行修改后，主线程读取到未修改的值。
 
TaskPool和worker的多线程方案都是基于Actor并发模型实现的。每个线程都有自己独立的内存空间，修改一个线程的单例对象不会影响到其他线程中的同一个单例对象。
 
 

#### 分析结论

问题中TaskPool修改的单例，是当前Task线程的单例对象，而不同线程之间的单例是相互独立的，所以在当前线程中修改单例对象的成员变量不会影响其他线程的单例对象。如果需要实现多线程之间的单例对象共享，可以使用共享模块。
 
 

#### 修改建议

共享模块可在线程间共享，可以实现在不同线程间操作同一个单例对象。示例代码如下所示：
 1. 在共享模块中创建单例。
```text
import { ArkTSUtils } from '@kit.ArkTS';
import { hilog } from '@kit.PerformanceAnalysisKit';
'use shared' <em>// 启动共享模块</em>

@Sendable
export class TaskHandle {
  private static instance: TaskHandle = new TaskHandle();
  private asyncLock: ArkTSUtils.locks.AsyncLock = new ArkTSUtils.locks.AsyncLock();
  private testNum: number = 0;

  public async testTask(id: number) {
   <em> // 共享异步线程操作同一个数据</em>
    await this.asyncLock.lockAsync(async () => {
      hilog.info(0x0000, 'taskpool', `TaskHandle task id: ${id} , testNum: ${this.testNum}`);
      this.testNum++;
      await this.sleep(1000);
      hilog.info(0x0000, 'taskpool', `TaskHandle task id: ${id} , testNum: ${this.testNum}`);
    });
  }

  public getTestNum() {
   <em> // 获取测试数据</em>
    return this.testNum;
  }

  public sleep(time: number): Promise<void> {
   <em> // 模拟延时操作</em>
    return new Promise(resolve => setTimeout(resolve, time));
  }

  static getInstance(): TaskHandle {
    <em>// 单例方法</em>
    return TaskHandle.instance;
  }
}
```

2. 外部调用单例的入口。
```text
import { taskpool } from '@kit.ArkTS';
import { TaskHandle } from './SharedModule';
import { hilog } from '@kit.PerformanceAnalysisKit';

export class Test {
  async testTaskpool(): Promise<void> {
   <em> // 启动多个线程执行数据操作</em>
    let task1: taskpool.Task = new taskpool.Task(func, 1);
    let task2: taskpool.Task = new taskpool.Task(func, 2);
    let task3: taskpool.Task = new taskpool.Task(func, 3);

    await taskpool.execute(task1);
    await taskpool.execute(task2);
    await taskpool.execute(task3);
    hilog.info(0x0000, 'taskpool', `test task api: ${TaskHandle.getInstance().getTestNum()}`);
  }
}

@Concurrent
async function func(num: number): Promise<void> {
 <em> // 单个异步线程操作</em>
  await TaskHandle.getInstance().testTask(num);
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Text('Hello World')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .onClick(()=>{
         <em> // 启动线程操作</em>
          func(0);
          let a = new Test();
          a.testTaskpool();
        })
        .width('100%')
    }
    .height('100%')
  }
}
```
 **结果如下图所示：**

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/fjOpWsSYT96M5lzpuk46-g/zh-cn_image_0000002629058996.png?HW-CC-KV=V1&HW-CC-Date=20260701T041128Z&HW-CC-Expire=86400&HW-CC-Sign=D6B837FCF46086C41B2031B9230E115AD10DF5668B060C87647E287887FE31FF)

 
 

#### 常见FAQ

Q：在worker中使用单例对象，会报错：xxx not initialized，如何解决？
 
A：worker线程与主线程拥有不同的运行环境，所以在使用单例的时候需要重新实例化一下所使用的单例对象。
