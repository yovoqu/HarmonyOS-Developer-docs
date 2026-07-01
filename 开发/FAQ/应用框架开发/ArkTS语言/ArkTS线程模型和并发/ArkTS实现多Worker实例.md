# ArkTS实现多Worker实例

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-103

实现多Worker并进行消息传递，使用registerGlobalCallObject方法传递对象及调用函数，获取缓冲区。注意：callGlobalCallObjectMethod方法在主线程中运行。
 1. 在MultipleWorkerInstances.ets文件中调用自定义函数。
```text
import { testMultyWorker } from './TestWorker'; <em>// Import Method</em>

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test workers')
          .onClick(() => {
            testMultyWorker(); <em>// Testing multiple workers</em>
          })
      }.width('100%')
    }.height('100%')
  }
}
```

2. 在TestWorker.ets文件中实现worker的管理调度。
```ArkTS
import { MessageEvents, worker } from '@kit.ArkTS';

const mainThreadTag: string = 'mainthread';

<em>// Initialize 2 workers, if closed or terminated, it cannot be used</em>
let worker1: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/worker1.ets', { name: 'worker1' });
let worker2: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/worker2.ets', { name: 'worker2' });

<em>// Custom Single Example</em>
class TestObj {
  private message: string = 'this is a message from TestObj';

  public getMessage(): string {
    console.log(mainThreadTag, 'worker call obj func: getMessage()');
    return this.message;
  }

  public getMessageWithInput(str: string): string {
    return this.message + 'with input:' + str;
  }

  public setSharedArrayBuffer() {
    let num = new Int16Array(this.sharedBuffer);
    num[0] = 20;
  }

  public getSharedArrayBuffer(): SharedArrayBuffer {
    return this.sharedBuffer;
  }

  static registerObj: TestObj = new TestObj();
  private sharedBuffer: SharedArrayBuffer = new SharedArrayBuffer(1024);
}

<em>// Worker's onMessage monitoring</em>
function onMessage(e: MessageEvents): void {
  switch (e.data.type as number) {
    case 0:
      console.log(mainThreadTag, 'received message type: 0, value is: %{public}s, next to post msg to worker2',
        e.data.value);
      worker2.postMessage('This is msg from mainthread switch');
      break;
    case 1:
      console.log(mainThreadTag, 'received message value %{public}d, next to post msg to worker1',
        e.data.value as number);
      worker1.postMessage({ 'type': 0 });
      break;
    default:
      console.log(mainThreadTag, 'invalid type, next to return');
  <em>  // Add a timer to reflect worker operation</em>
      setTimeout(() => {
        console.log(mainThreadTag, 'invalid type, next to return');
      }, 5000);
      break;
  }
}

<em>// Export function</em>
export function testMultyWorker() {
  TestObj.registerObj.setSharedArrayBuffer();
 <em> // Register registrant Obj on ThreadWorker instance</em>
  worker2.registerGlobalCallObject('myObj', TestObj.registerObj);
  worker1.registerGlobalCallObject('myObj', TestObj.registerObj);

  console.log(mainThreadTag, 'this is a msg to start worker');
  worker1.postMessage('this is a msg to start worker1');

  worker1.onmessage = onMessage;
  worker2.onmessage = onMessage;

  console.log(mainThreadTag, 'end');
  worker1.onexit = () => {
    console.log('main thread terminate worker1');
  }
  worker2.onexit = () => {
    console.log('main thread terminate worker2');
  }
}
```

3. Worker代码如下：Worker1.ets：

  
```text
import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker, process } from '@kit.ArkTS';

const worker1: string = 'worker1';
const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (e: MessageEvents) => {
  console.log(worker1,'enter worker1, process uid:%{public}d, pid:%{public}d, tid:%{public}d',
    process.uid,process.pid,process.tid);

  if (e.data.type === 0) {
    workerPort.postMessage({ 'type': 2 });
    console.log(worker1,'begin to end worker1');
  <em>  // workerPort.close()  // Do not allow reuse after closing, otherwise it may cause a crash</em>
    return;
  }

  try {
    let str1: string = workerPort.callGlobalCallObjectMethod('myObj','getMessage',0) as string;
    console.log(worker1,'call shared class to get func: getMessage(), return is: %{public}s',str1);
  } catch (e) {
    console.log(worker1,'call shared class getMessage get this %{public}s ,errcode %{public}d',e.message,e.code);
  }

  try {
    let res: SharedArrayBuffer =
      workerPort.callGlobalCallObjectMethod('myObj','getSharedArrayBuffer',0) as SharedArrayBuffer;
    let typedArr = new Int16Array(res);
    console.log(worker1,'call shared class func: getSharedArrayBuffer(), return is: %{public}d',typedArr[0]);
    typedArr[0] = 25;
    console.log(worker1,'work1 change the value to： %{public}d',typedArr[0]);
  } catch (e) {
    console.log(worker1,'call shared class getSharedArrayBuffer get this %{public}s',e.message);
  }

  workerPort.postMessage({ 'type': 0,'value': 'this is a msg from worker1 to main' });


  workerPort.onmessageerror = (e: MessageEvents) => {
    console.log(worker1,'received a message error');
  }

  workerPort.onerror = (e: ErrorEvent) => {
    console.log(worker1,'worker1 error');
  }
}
```
 Worker2.ets：

  
```text
import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker, process } from '@kit.ArkTS';

const worker2: string = 'worker2';
const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (e: MessageEvents) => {
  console.log(worker2, 'enter worker2, process update %{public}d,%{public}d,%{public}d', process.uid, process.pid,
    process.tid);
  let str: string = workerPort.callGlobalCallObjectMethod('myObj', 'getMessage', 0) as string;
  console.log(worker2, 'call shared class func get value: %{public}s', str);

  let res: SharedArrayBuffer =
    workerPort.callGlobalCallObjectMethod('myObj', 'getSharedArrayBuffer', 0) as SharedArrayBuffer;
  let typedArr = new Int16Array(res);
  console.log(worker2, 'call shared class func get value: %{public}d', typedArr[0]);
  workerPort.postMessage({ 'type': 1, 'value': typedArr[0] });
}

workerPort.onmessageerror = (e: MessageEvents) => {
  console.log(worker2, 'received a message error');
}

workerPort.onerror = (e: ErrorEvent) => {
  console.log(worker2, 'worker2 error');
}
```
