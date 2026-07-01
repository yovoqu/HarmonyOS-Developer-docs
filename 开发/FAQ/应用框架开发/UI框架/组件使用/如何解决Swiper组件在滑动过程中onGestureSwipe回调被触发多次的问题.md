# 如何解决Swiper组件在滑动过程中onGestureSwipe回调被触发多次的问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1228

#### 问题现象

Swiper组件在滑动过程中onGestureSwipe回调被触发多次，如何限制回调执行的次数？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/nNMIOPJzQBmeiTOGOOH59Q/zh-cn_image_0000002658833295.png?HW-CC-KV=V1&HW-CC-Date=20260701T041315Z&HW-CC-Expire=86400&HW-CC-Sign=AE21B2C99F669875C962818BAE716E373914F37A41C7814C7F3642DC4B10F39F)

 
 

#### 背景知识

[Swiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper)滑块视图容器，提供子组件滑动轮播显示的能力。在页面跟手滑动过程中，逐帧触发[onGestureSwipe](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#ongestureswipe10)回调。当Swiper组件包含多个子组件时，index为最左侧组件的索引。
 
 

#### 解决方案

onGestureSwipe逐帧触发回调，一般用于监听每帧移动距离。如需只触发一次事件，可采用如下两种防抖策略来解决onGestureSwipe多次触发的问题。
 
解决方案一：时间间隔防抖。记录上次处理滑动事件的时间戳；当新的滑动事件触发时，检查与上次事件的时间间隔；如果间隔小于设定阈值(300ms)，则忽略此次事件。示例代码如下：
 
```text
const currentTime = Date.now();
if (currentTime - this.lastSwipeTime < this.swipeThreshold) {
  return; <em>// 时间间隔过短，忽略此次事件</em>
}
this.lastSwipeTime = currentTime;
```
 
解决方案二：状态锁防抖。使用一个状态变量(isHandlingSwipe)标记当前是否正在处理滑动；当事件触发时，检查状态变量；如果正在处理中，则忽略此次事件；处理完成后重置状态。示例代码如下：
 
```text
if (this.isHandlingSwipe) {
  return; <em>// 正在处理中，忽略此次事件</em>
}
this.isHandlingSwipe = true;
<em>// 模拟处理延迟</em>
setTimeout(() => {
  this.isHandlingSwipe = false;
}, this.swipeThreshold);
```
 
完整示例代码如下：
 
```text
class MyDataSource implements IDataSource {
  private list: number[] = [];

  constructor(list: number[]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): number {
    return this.list[index];
  }

  registerDataChangeListener(): void {
  }

  unregisterDataChangeListener() {
  }
}

@Entry
@Component
struct SwiperGestureExample {
  private swiperController: SwiperController = new SwiperController();
  private data: MyDataSource = new MyDataSource([]);
  @State lastSwipeTime: number = 0;
  @State isHandlingSwipe: boolean = false; <em>// 用于标记当前是否正在处理滑动</em>
  swipeThreshold: number = 300; <em>// 防抖阈值(毫秒)</em>

  aboutToAppear(): void {
    let list: number[] = [];
    for (let i = 1; i <= 10; i++) {
      list.push(i);
    }
    this.data = new MyDataSource(list);
  }

  build() {
    Column({ space: 5 }) {
      Swiper(this.swiperController) {
        LazyForEach(this.data, (item: string) => {
          Text(item.toString())
            .width('90%')
            .height(160)
            .backgroundColor('#E5E5EA')
            .textAlign(TextAlign.Center)
            .fontSize(30);
        }, (item: string) => item);
      }
      .displayCount(3, false)
      .autoPlay(true)
      .interval(4000)
      .loop(true)
      .duration(2000)
      .itemSpace(10)
      .onGestureSwipe(() => {
      <em>  // 方案一:时间间隔防抖</em>
        const currentTime = Date.now();
        if (currentTime - this.lastSwipeTime < this.swipeThreshold) {
          return;<em> // 时间间隔过短，忽略此次事件</em>
        }
        this.lastSwipeTime = currentTime;

      <em>  // 方案二:状态锁防抖</em>
        if (this.isHandlingSwipe) {
          return;<em> // 正在处理中，忽略此次事件</em>
        }
        this.isHandlingSwipe = true;
       <em> // 模拟处理延迟</em>
        setTimeout(() => {
          this.isHandlingSwipe = false;
        }, this.swipeThreshold);
        console.info('onGestureSwipe回调被触发');
      });
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#F1F3F5')
    .justifyContent(FlexAlign.Center);
  }
}
```
