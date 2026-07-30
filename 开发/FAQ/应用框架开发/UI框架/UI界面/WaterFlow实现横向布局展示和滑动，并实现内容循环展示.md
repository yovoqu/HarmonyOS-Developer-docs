# WaterFlow实现横向布局展示和滑动，并实现内容循环展示

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-519

#### 问题现象

WaterFlow瀑布流默认是纵向布局展示，本方案实现横向布局展示和横向滑动。
 
 

#### 背景知识

- [layoutDirection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow#layoutdirection)属性，设置布局的主轴方向，即WaterFlow的滑动方向。
- [onReachEnd](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow#onreachend)，瀑布流内容到达末尾位置时触发回调。

 
 

#### 解决方案
1. 设置WaterFlow的layoutDirection为FlexDirection.Row，实现横向滑动，并设置展示几行，如下方示例，设置为展示2行。
```text
.layoutDirection(FlexDirection.Row)
.columnsTemplate('1fr 1fr 1fr')
.rowsTemplate('1fr 1fr')
```

2. 配置FlowItem和展示图片内容的高度为100%。此时已经可以实现横向展示和滑动。
```text
FlowItem() {
  Column() {
    Text(`N${item}`).fontSize(12).height('16')
   <em> // 存在对应的jpg文件才会显示图片</em>
    Image(`res/waterFlowTest(${item % 5}).jpg`)
      .objectFit(ImageFit.Fill)
      .height('100%')
      .layoutWeight(1)
  }
}
.width(this.itemWidthArray[item % 100])
.height('100%')
.backgroundColor(this.colors[item % 3])
```

3. 设计内容循环，初始化this.dataSource数量大于内容数量，加载图片内容名称固定格式以数字序号区分，加载图片时按图片序号和图片总数取余，实现无限依次加载图片。
```text
Image(`res/waterFlowTest(${item % 5}).jpg`)
  .objectFit(ImageFit.Fill)
  .height('100%')
  .layoutWeight(1)
```

4. WaterFlow滑动时，通过onReachEnd回调，给this.dataSource再次增加数量。
```text
.onReachEnd(() => {
  console.info('onReachEnd');
  for (let i = 0; i < 100; i++) {
    this.dataSource.addLastItem();
  }
})
```

5. 完整示例参考如下：

  Index页面：
```text
import { WaterFlowDataSource } from '../DataSource/WaterFlowDataSource';

@Entry
@Component
struct WaterFlowDemo {
  private minSize: number = 80;
  private maxSize: number = 180;
  @State colors: number[] = [0x86C5E3, 0x61CFBE, 0x8981F7, 0x86C5E3, 0x61CFBE];
  scroller: Scroller = new Scroller();
  dataSource: WaterFlowDataSource = new WaterFlowDataSource();
  private itemWidthArray: number[] = [];

  <em>// </em><em>设置FlowItem的宽/高数组</em>
  setItemSizeArray() {
    for (let i = 0; i < 100; i++) {
      if (i === 0) {
        this.itemWidthArray.push(this.minSize);
      }
      this.itemWidthArray.push(this.maxSize);
    }
  }

  aboutToAppear() {
    this.setItemSizeArray();
  }

  build() {
    Column({ space: 2 }) {
      WaterFlow() {
        LazyForEach(this.dataSource, (item: number) => {
          FlowItem() {
            Column() {
              Text(`N${item}`).fontSize(12).height('16')
            <em>  // 存在对应的jpg文件才会显示图片</em>
              Image(`res/waterFlowTest(${item % 5}).jpg`)
                .objectFit(ImageFit.Fill)
                .height('100%')
                .layoutWeight(1)
            }
          }
          .width(this.itemWidthArray[item % 100])
          .height('100%')
          .backgroundColor(this.colors[item % 3])
        }, (item: string) => item)
      }
      .layoutDirection(FlexDirection.Row)
      .columnsTemplate('1fr 1fr 1fr')
      .rowsTemplate('1fr 1fr')
      .columnsGap(10)
      .rowsGap(5)
      .backgroundColor(0xFAEEE0)
      .width('100%')
      .height('100%')
     <em> // 触底加载数据</em>
      .onReachEnd(() => {
        console.info('onReachEnd');
        for (let i = 0; i < 100; i++) {
          this.dataSource.addLastItem();
        }
      })
    }
  }
}
```


  dataSource类页面：
```text
export class WaterFlowDataSource implements IDataSource {
  private dataArray: number[] = [];
  private listeners: DataChangeListener[] = [];

  constructor() {
    for (let i = 0; i < 100; i++) {
      this.dataArray.push(i);
    }
  }

 <em> // 获取索引对应的数据</em>
  public getData(index: number): number {
    return this.dataArray[index];
  }

 <em> // 通知控制器数据重新加载</em>
  notifyDataReload(): void {
    this.listeners.forEach(listener => {
      listener.onDataReloaded();
    });
  }

  <em>// 通知控制器数据增加</em>
  notifyDataAdd(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataAdd(index);
    });
  }

 <em> // 通知控制器数据变化</em>
  notifyDataChange(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataChange(index);
    });
  }

<em>  // 通知控制器数据删除</em>
  notifyDataDelete(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataDelete(index);
    });
  }

<em>  // 通知控制器数据位置变化</em>
  notifyDataMove(from: number, to: number): void {
    this.listeners.forEach(listener => {
      listener.onDataMove(from, to);
    });
  }

 <em> // 通知控制器数据批量修改</em>
  notifyDatasetChange(operations: DataOperation[]): void {
    this.listeners.forEach(listener => {
      listener.onDatasetChange(operations);
    });
  }

  <em>// 获取数据总数</em>
  public totalCount(): number {
    return this.dataArray.length;
  }

 <em> // 注册改变数据的控制器</em>
  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener) < 0) {
      this.listeners.push(listener);
    }
  }

<em>  // 注销改变数据的控制器</em>
  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      this.listeners.splice(pos, 1);
    }
  }

 <em> // 增加数据</em>
  public add1stItem(): void {
    this.dataArray.splice(0, 0, this.dataArray.length);
    this.notifyDataAdd(0);
  }

<em>  // 在数据尾部增加一个元素</em>
  public addLastItem(): void {
    this.dataArray.splice(this.dataArray.length, 0, this.dataArray.length);
    this.notifyDataAdd(this.dataArray.length - 1);
  }

 <em> // 在指定索引位置增加一个元素</em>
  public addItem(index: number): void {
    this.dataArray.splice(index, 0, this.dataArray.length);
    this.notifyDataAdd(index);
  }

 <em> // 删除第一个元素</em>
  public delete1stItem(): void {
    this.dataArray.splice(0, 1);
    this.notifyDataDelete(0);
  }

 <em> // 删除第二个元素</em>
  public delete2ndItem(): void {
    this.dataArray.splice(1, 1);
    this.notifyDataDelete(1);
  }

  <em>// 删除最后一个元素</em>
  public deleteLastItem(): void {
    this.dataArray.splice(-1, 1);
    this.notifyDataDelete(this.dataArray.length);
  }

 <em> // 在指定索引位置删除一个元素</em>
  public deleteItem(index: number): void {
    this.dataArray.splice(index, 1);
    this.notifyDataDelete(index);
  }

 <em> // 重新加载数据</em>
  public reload(): void {
    this.dataArray.splice(1, 1);
    this.dataArray.splice(3, 2);
    this.notifyDataReload();
  }
}
```
