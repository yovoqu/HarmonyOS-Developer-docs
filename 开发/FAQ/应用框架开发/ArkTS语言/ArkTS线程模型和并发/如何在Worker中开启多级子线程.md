# 如何在Worker中开启多级子线程

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-121

在Worker中开启多级子线程，具体可参考如下示例代码：
 
```ArkTS
import { ErrorEvent, MessageEvents, worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker('entry/ets/pages/Worker.ets');

<em>// The main thread passes information to the worker thread</em>
workerInstance.postMessage('123');

<em>// The main thread receives worker thread information</em>
workerInstance.onmessage = (e: MessageEvents): void => {
 <em> // Data: Information sent by the Worker thread</em>
  let data: string = e.data;
  console.info(`main thread onmessage, data:${data}`);
  const workerInstance1 = new worker.ThreadWorker('entry/ets/pages/Work.ets');
  workerInstance1.postMessage('123');
  workerInstance1.onmessage = (e: MessageEvents): void => {
   <em> // data：Information sent by worker threads</em>
    let data1: string = e.data;
    console.info(`main thread onmessage1, data:${data1}`);
  <em>  // Destroy Worker object</em>
    workerInstance1.terminate();
  }
 <em> // After calling terminate, execute onexit</em>
  workerInstance1.onexit = (code) => {
    console.info(`main thread terminate, code:${code}`);
  }
<em>  // Destroy Worker object</em>
  workerInstance.terminate();

}
<em>// After calling terminate, execute onexit</em>
workerInstance.onexit = (code) => {
  console.info(`main thread terminate, code:${code}`);
}

workerInstance.onerror = (err: ErrorEvent) => {
  console.error('main error message ' + err.message);
}
```
 
```ArkTS
<em>// Work.ets & Worker.ets</em>
import { ErrorEvent, MessageEvents, worker } from '@kit.ArkTS';

<em>// Create an object in the worker thread that communicates with the main thread</em>
const workerPort = worker.workerPort;

<em>// The worker thread receives information from the main thread</em>
workerPort.onmessage = (e: MessageEvents): void => {
 <em> // Data: Information sent by the main thread</em>
  let data: string = e.data;
  console.info(`Work.ets onmessage: data ${data}`);

 <em> // Worker thread sends information to main thread</em>
  workerPort.postMessage('123');
}

<em>// Callback for worker thread error</em>
workerPort.onerror = (err: ErrorEvent) => {
  console.info('Worker.ets onerror' + err.message);
}
```
 
```ArkTS
"buildOption": {
  "sourceOption": {
    "workers": [
      "./src/main/ets/pages/Worker.ets",
      "./src/main/ets/pages/Work.ets"
    ]
  }
},
```
 
**参考链接**
 
[@ohos.worker (启动一个Worker)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-worker)
