# 是否有让进程睡眠的API

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-function-flow-runtime-2

#### 问题现象

HarmonyOS中是否有让进程睡眠的API？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/PLQD5NteSWujekbW5MzmQg/zh-cn_image_0000002628899080.gif?HW-CC-KV=V1&HW-CC-Date=20260701T041136Z&HW-CC-Expire=86400&HW-CC-Sign=A4166BC66AF107DC08930D19794D920722E770EC8999323D92BB36C296381F8A)

 
 

#### 背景知识

[setTimeout](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-timer#settimeout)可以设置一个定时器，该定时器在定时器到期后执行一个函数。
 
 

#### 解决方案

HarmonyOS中未直接提供进程睡眠的API。
 
方案一：可以通过setTimeout方法间接实现睡眠效果，参考如下sleep方法。
 
方案二：使用Atomics.wait来达到sleep效果，参考如下sleepAtomics方法。
 
```text
@Entry
@Component
struct SleepPage {
  @State message: string = 'Hello World';

<em>  // 睡眠等待方法，time为睡眠时间，单位毫秒</em>
  sleep(time: number): Promise<void> {
    return new Promise(resolve => setTimeout(resolve, time));
  }

  sleepAtomics(time: number) {
    let sharedBuf = new SharedArrayBuffer(4);
    let sharedArr = new Int32Array(sharedBuf);
    Atomics.wait(sharedArr, 0, 0, time);
    this.message = 'Atomics 3000';
  }

  build() {
    Column() {
      Text(this.message)
        .id('SleepPageHelloWorld')
        .fontSize('50fp')
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.message = 'Welcome';
        })
      Button('Sleep修改message')
        .onClick(async () => {
        <em>  // 等待3秒</em>
          await this.sleep(3000);
          this.message = 'SLEEP 3000';
        })
        .margin({ top: 20 });

      Button('sleepAtomics修改message')
        .onClick(async () => {
        <em>  // 等待3秒</em>
          this.sleepAtomics(3000);
        })
        .margin({ top: 20 });
    }
    .height('100%')
    .width('100%');
  }
}
```
