# 如何使用TaskPool在子线程调用对象成员函数

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-120

通过将对象Sendable化来使用对象中的方法。具体可参考如下示例代码：
 
```ArkTS
<em>// TestClass.ets</em>
@Sendable
export class TestClass {
  value: number = 888;

  GetValue(): number {
    return this.value;
  }

  Print(): void {
    console.info('value:' + this.value);
  }
}
```
 
```ArkTS
<em>// xxx.ets:</em>
import { taskpool } from '@kit.ArkTS';
import { TestClass } from './TestClass';

<em>// Step 1: Define concurrent functions and internally call synchronization methods</em>
@Concurrent
function func(num: number): number {
 <em> // Call synchronous wait call implemented in static class objects</em>
  let testClass = new TestClass();
  let sum = testClass.GetValue() + num;
  return sum;
}

<em>// Step 2: Create a task and execute it</em>
function asyncGet(): void {
  <em>// Create a task and pass it in the function func</em>
  let task: taskpool.Task = new taskpool.Task(func, 1);
 <em> // Execute task and operate on the synchronized logic results</em>
  taskpool.execute(task).then((result: object) => {
    console.info('testTag result:' + result);
  });
}

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
           <em> // Step 3: Perform concurrent operations</em>
            asyncGet();
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
