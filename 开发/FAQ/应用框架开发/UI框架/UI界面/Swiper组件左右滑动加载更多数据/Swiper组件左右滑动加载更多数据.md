# Swiper组件左右滑动加载更多数据

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-598

#### 问题现象

使用Swiper组件动态加载数据：
 
- 当用户从第一页向右滑动时，在数据列表的最前面添加新数据。
- 当用户从最后一页向左滑动时，在数据列表的最后面添加新数据。

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/TQyb-8tXQ5uNA2iTY8Yn5Q/zh-cn_image_0000002628392706.png?HW-CC-KV=V1&HW-CC-Date=20260730T072459Z&HW-CC-Expire=86400&HW-CC-Sign=529A138B5790ED3972DEAA88254293A9B3C6A0F964E5504AF2E26651BC539998)

 
 

#### 背景知识

- 在Swiper组件中，当页面切换时会触发[onAnimationStart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#onanimationstart9)回调函数，用于监听动画的开始事件。该回调函数可提供当前页码index、目标页码targetIndex以及额外信息extraInfo，可用于判断滑动方向。
- [cryptoFramework](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework)：对于安全要求比较高的场景，推荐使用加解密算法库框架[@ohos.security.cryptoFramework](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework)包生成安全随机数。

 
 

#### 解决方案

在Swiper组件的onAnimationStart回调中，通过index和targetIndex判断滑动方向，并在相应条件下加载新数据：
 
- 当index === 0且targetIndex === 0时，表示从第一页向右滑动，此时在数据列表的最前面添加新数据。
- 当index === this.data.totalCount() - 1时，表示从最后一页向左滑动，此时在数据列表的最后面添加新数据。

 
完整示例参考如下：
 
```text
import cryptoFramework from '@ohos.security.cryptoFramework';

<em>// </em><em>数据源，支持对数据的增删改查，并通知UI更新</em>
class MyDataSource implements IDataSource {
  private list: number[] = [];
  private listeners: DataChangeListener[] = [];

  constructor(list: number[]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): number {
    return this.list[index];
  }

 <em> // 数组末尾添加数据</em>
  pushData(element: number) {
    this.list.push(element);
    this.notifyDataReload();
  }

 <em> // 数组开头添加数据</em>
  unshiftData(element: number) {
    this.list.unshift(element);
    this.notifyDataAdd(0);
  }

  deleteData(index: number) {
    this.list.splice(index, 1);
    this.notifyDataReload();
  }

  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener) < 0) {
      console.info('add listener');
      this.listeners.push(listener);
    }
  }

  unregisterDataChangeListener(listener: DataChangeListener) {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      console.info('remove listener');
      this.listeners.splice(pos, 1);
    }
  }

 <em> // 通知LazyForEach组件需要重载所有子组件</em>
  notifyDataReload(): void {
    this.listeners.forEach(listener => {
      listener.onDataReloaded();
    });
  }

  <em>// </em><em>通知LazyForEach组件需要在index对应索引处添加子组件</em>
  notifyDataAdd(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataAdd(index);
    });
  }

<em>  // 通知LazyForEach组件在index对应索引处数据有变化，需要重建该子组件</em>
  notifyDataChange(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataChange(index);
    });
  }

 <em> // 通知LazyForEach组件需要在index对应索引处删除该子组件</em>
  notifyDataDelete(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataDelete(index);
    });
  }

 <em> // 通知LazyForEach组件将from索引和to索引处的子组件进行交换</em>
  notifyDataMove(from: number, to: number): void {
    this.listeners.forEach(listener => {
      listener.onDataMove(from, to);
    });
  }
}


@Entry
@Component
struct SwiperExample {
  private swiperController: SwiperController = new SwiperController();
  private data: MyDataSource = new MyDataSource([]);

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
            .backgroundColor(0xAFEEEE)
            .textAlign(TextAlign.Center)
            .fontSize(30);
        }, (item: string) => item);
      }
      .cachedCount(2)
      .index(0)
      .loop(false)
      .itemSpace(5)
      .curve(Curve.Linear)
      .onAnimationStart((index: number, targetIndex: number, extraInfo: SwiperAnimationEvent) => {
        console.info('extraInfo', extraInfo);
       <em> // 下标为0时，向右滑动，模拟拉取新数据</em>
        if (index === 0 && targetIndex === 0 && extraInfo.currentOffset > 0) {
          let rand = cryptoFramework.createRandom();
       <em>   // 设置生成随机数的字节长度为1</em>
          let randData = rand.generateRandomSync(1);
        <em>  // 自定义范围(0-10之内)</em>
          let num: number = Math.round(randData.data[0] * 10 / 255);
          this.data.unshiftData(num);
          this.swiperController.changeIndex(1);
        }
     <em>   // 下标为数组最后一个时，向左滑动，模拟拉取新数据</em>
        if (index === this.data.totalCount() - 1 && targetIndex === index && extraInfo.currentOffset < 0) {
          let rand = cryptoFramework.createRandom();
          let randData = rand.generateRandomSync(1);
          let num: number = Math.round(randData.data[0] * 10 / 255);
          this.data.pushData(num);
        }
      })
      .onAnimationEnd((index: number, extraInfo: SwiperAnimationEvent) => {
        console.info(`index:\n${index}`);
        console.info(`velocity:\n${extraInfo.velocity}`);
        console.info(`target offset:\n${extraInfo.targetOffset}`);
        console.info(`current offset::\n${extraInfo.currentOffset}`);
      })
      .maintainVisibleContentPosition(true);

      Row({ space: 5 }) {
        Button('FAST 0')
          .onClick(() => {
            this.swiperController.changeIndex(0, SwiperAnimationMode.FAST_ANIMATION);
          });
      };

      Row() {
        Button('FAST LAST')
          .onClick(() => {
            this.swiperController.changeIndex(this.data.totalCount() - 1, SwiperAnimationMode.FAST_ANIMATION);
          });
      };

      Row() {
        Button('顶部添加数据')
          .onClick(() => {
            let rand = cryptoFramework.createRandom();
            let randData = rand.generateRandomSync(1);
            let num: number = Math.round(randData.data[0] * 10 / 255);
            this.data.unshiftData(num);
          });
      };

      Row() {
        Button('尾部添加数据')
          .onClick(() => {
            let rand = cryptoFramework.createRandom();
            let randData = rand.generateRandomSync(1);
            let num: number = Math.round(randData.data[0] * 10 / 255);
            this.data.pushData(num);
          });
      };

      Row() {
        Button('删除第一个')
          .onClick(() => {
            this.data.deleteData(0);
          });
      };
    }.width('100%');
  }
}
```
