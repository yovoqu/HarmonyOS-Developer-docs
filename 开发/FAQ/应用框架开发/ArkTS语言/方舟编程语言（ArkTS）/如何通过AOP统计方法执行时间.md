# 如何通过AOP统计方法执行时间

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-99

为了统计执行时间，可以使用addBefore记录开始时间，使用addAfter记录结束时间。
 
示例如下：
 
```text
import { util } from '@kit.ArkTS';
import { systemDateTime } from '@kit.BasicServicesKit';

class Utils {
  Add(len: number): number {
    let num = 0;
    for (let index = 1; index <= len; index++) {
      num += index;
    }
    return num;
  }
}

let startTime = 0; <em>// Initialization start time</em>
let endTime = 0;<em> // Initialization end time</em>

util.Aspect.addBefore(Utils, 'Add', false, () => {
  startTime = systemDateTime.getTime(true); <em>// Return the start time in nanoseconds</em>
})

util.Aspect.addAfter(Utils, 'Add', false, () => {
  endTime = systemDateTime.getTime(true);<em> // Return the end time in nanoseconds</em>
})

let utilsObj = new Utils();
utilsObj.Add(1000);

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('get execution time')
          .onClick(() => {
            console.log('startTime:', startTime);
            console.log('endTime:', endTime);
            console.log('endTime - startTime = ', endTime - startTime);
          })
      }
      .width('100%')
    }.height('100%')
  }
}
```
