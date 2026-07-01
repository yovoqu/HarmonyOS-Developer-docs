# 如何将类Java语言的线程模型（内存共享）的实现方式转换成在ArkTS的线程模型下（内存隔离）的实现方式

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-46

可以利用TaskPool接口转换，具体分为以下四个场景：
 
- 场景一：主线程将独立任务放到子线程执行。代码示例：共享内存写法：

  
```text
class Task {
  static run(args) {
   <em> // Do some independent tasks</em>
  }
}
let thread = new Thread(() => {
  let result = Task.run(args)
 <em> // deal with result</em>
})
```
 ArkTS写法：

  
```text
import { taskpool } from '@kit.ArkTS';

@Concurrent
function run(args: number) {
 <em> // Do some independent tasks</em>
}
let task: taskpool.Task = new taskpool.Task(run, 100); // 100: test number
taskpool.execute(task).then((res) => {
 <em> // Return result</em>
});
```

- 场景二：主线程在子线程使用类对象实例。代码示例：共享内存写法：

  
```text
class Material {
  action(args) {
  <em>  // Do some independent tasks</em>
  }
}
let material = new Material()
let thread = new Thread(() => {
  let result = material.action(args)
  <em>// deal with result</em>
})
```
 ArkTS写法：

  
```text
import { taskpool } from '@kit.ArkTS';

@Concurrent
function runner(material: Material): void {
  return material.action(100); <em>// 100: test number</em>
}
@Sendable
class Material {
  action(args: number) {
   <em> // Do some independent tasks</em>
  }
}
let material = new Material()
taskpool.execute(runner, material).then((ret) => {
<em>  // Return result</em>
})
```

- 场景三：子线程更新主线程状态。代码示例：共享内存写法：

  
```text
class Task {
    run(args) {
       <em> // deal with result</em>
        runOnUiThread(() => {
            UpdateUI(result)
        })
    }
}
let task = new Task()
let thread = new Thread(() => {
    let result = task.run(args)
  <em>  // Processing results</em>
})
```
 ArkTS写法：

  
```text
import taskpool from '@ohos.taskpool'

<em>// let result: Object[] | undefined = undefined</em>

@Concurrent
function runner(task:Task) {
  task.run()
}
@Sendable
class Task {
  run(args?: Object[] | undefined) {
   <em> // Do some independent tasks</em>
    taskpool.Task.sendData(JsResult)
  }
}
let task = new Task()
let run = new taskpool.Task(runner, task)
run.onReceiveData((result?: Function | undefined) => {
  UpdateUI(result)
})
taskpool.execute(run).then((ret) => {
 <em> // Return result</em>
})
```

- 场景四：子线程同步调用主线程接口。代码示例：
```text
class SdkU3d {
    static getInst() {
        return SdkMgr.getInst();
    }
    getPropStr(str: string) {
        return xx;
    }
}
let thread = new Thread(() => {
  <em>  // In the game thread</em>
    let sdk = SdkU3d.getInst()
    let ret = sdk.getPropStr("xx")
})
```
 ArkTS写法：

  
```text
import { MessageEvents, taskpool, worker } from '@kit.ArkTS';
class SdkU3d {
  static getInst(): Object {
    return SdkMgr.getInst();
  }
  getPropStr(str: string) { }
}
let workerInstance = new worker.ThreadWorker("xx/worker.ts");
workerInstance.registerGlobalCallObject("instance_xx", SdkU3d.getInst());
workerInstance.postMessage("start");
<em>// In the game worker thread</em>
const mainPort = worker.workerPort;
mainPort.onmessage = (e: MessageEvents): void => {
  let ret = mainPort.callGlobalCallObjectMethod("instance_xx", "getPropStr", 100); // 100: test number
}
```


 
**参考链接**
 
[并发概述](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/concurrency-overview)
