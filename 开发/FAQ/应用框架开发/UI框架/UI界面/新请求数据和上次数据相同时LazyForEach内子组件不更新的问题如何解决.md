# 新请求数据和上次数据相同时LazyForEach内子组件不更新的问题如何解决

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1642

#### 问题现象

如何实现两次请求返回数据完全相同时也刷新LazyForEach相关的组件。因为，在第一次请求返回数据进行了业务逻辑处理和相关组件的刷新；第二次请求返回数据时，需要重置组件的状态。如果直接使用返回的相关数据作为LazyForEach的键值，不会触发相关组件的状态刷新，如何在数据完全相同时也刷新LazyForEach相关的组件？
 
 

#### 背景知识

- [键值生成规则](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-lazyforeach#键值生成规则)：在[LazyForEach](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-rendering-control-lazyforeach)循环渲染过程中，系统会为每个item生成一个唯一且持久的键值，用于标识对应的组件。当这个键值变化时，ArkUI框架将视为该数组元素已被替换或修改，并会基于新的键值创建一个新的组件。
- LazyForEach提供了keyGenerator参数，用于传入键值生成函数，可以通过它自定义键值的生成规则。如果没有定义keyGenerator函数，则ArkUI框架会使用默认的键值生成函数，即：(item: any, index: number) => { return viewId + '-' + index.toString(); }
- [组件创建规则](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-lazyforeach#组件创建规则)：在确定键值生成规则后，LazyForEach的第二个参数itemGenerator函数会根据组件创建规则为数据源的每个数组项创建组件。组件的创建包括两种情况：LazyForEach首次渲染和LazyForEach数据更新后的非首次渲染。

 
 

#### 解决方案

LazyForEach渲染的原理：只有当keyGenerator参数定义的键值发生变化时，ArkUI框架才会将该数组元素视为已被替换或修改，并会基于新的键值创建一个新的组件。
 
上述问题中，两次请求返回的数据完全相同时，使用返回数据作为键值将不会触发组件刷新。而业务要求只要有新的请求数据，就必须刷新对应的UI组件，即使数据是相同的。因此需要定义一个合适的keyGenerator参数，对相同元素也能产生不同的键值。
 
采用在键值生成中加入随机数的方法，示例代码如下：
 
```json
import { util } from '@kit.ArkTS';

@Entry
@Component
struct RefreshComponentsWhenDataIdentical {
  @State bol: boolean = true;
  @State debtData: CommonDataSource<Data> = new CommonDataSource([]);
  data1: Data[] = [new Data('分组1 name1', '分组1 code1'), new Data('分组1 name2', '分组1 code2')];

  aboutToAppear(): void {
    this.debtData.setNewData(this.data1);
  }

  build() {
    Column() {
      Button('重新请求数据')
        .width('60%')
        .height(40)
        .fontColor(Color.White)
        .onClick(() => {
          this.getDetData();
        })
        .margin({ top: 16, bottom: 16 });
      List() {
        LazyForEach(this.debtData, (data: Data) => {
          ListItem() {
            TestComponent({ data: data })
              .margin({ left: 16, right: 16 });
          }
          .height(80)
          .onClick(() => {
            data.stockCode = data.stockCode + 'ss';
          });
        }, (value: Data) => JSON.stringify(value) + util.generateRandomUUID(false));
      }
      .width('100%')
      .layoutWeight(1)
      .listDirection(Axis.Vertical)
      .divider({ strokeWidth: 5, color: 'app.color.dz_root_background' });
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center);
  }

 <em> // 获取数据</em>
  getDetData() {
    if (this.bol) {
      this.bol = false;
      this.debtData.setNewData([new Data('分组1 name1', '分组1 code1'), new Data('分组1 name2', '分组1 code2')]);
    } else {
      this.bol = true;
      this.debtData.setNewData([new Data('分组1 name1', '分组1 code1'), new Data('分组1 name2', '分组1 code2')]);
    }
  }
}

@Component
export struct TestComponent {
  @ObjectLink data: Data;

  build() {
    Text(this.data.stockCode).fontColor(Color.Black).fontSize(20);
  }
}

@Observed
export class Data {
  stockName: string = '';
  stockCode: string = '';

  constructor(name: string, code: string) {
    this.stockName = name;
    this.stockCode = code;
  }
}

export class CommonDataSource<T> implements IDataSource {
  private dataArray: T[] = [];
  private listeners: DataChangeListener[] = [];

  constructor(element: T[]) {
    this.dataArray = element;
  }

  <em>// 获取数据</em>
  public getData(index: number) {
    return this.dataArray[index];
  }

  public getDataList() {
    return this.dataArray;
  }

  public totalCount(): number {
    return this.dataArray.length;
  }

  public getIndex(data: T): number {
    return this.dataArray.indexOf(data);
  }

<em>  // 添加数据</em>
  public addArrayData(data: T[]): void {
    this.dataArray = this.dataArray.concat(data);
    this.notifyDataReload();
  }

  public setNewData(data: T[]): void {
    this.dataArray = [];
    this.addArrayData(data);
  }

  public addData(index: number, data: T[]): void {
    this.dataArray = this.dataArray.concat(data);
    this.notifyDataAdd(index);
  }

  public pushData(data: T): void {
    this.dataArray.push(data);
    this.notifyDataAdd(this.dataArray.length - 1);
  }

 <em> // 清除数据</em>
  public clearData(): void {
    this.dataArray = [];
  }

  <em>// 重新加载数据</em>
  public refresh(): void {
    this.notifyDataReload();
  }

  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      this.listeners.splice(pos, 1);
    }
  }

  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener) < 0) {
      this.listeners.push(listener);
    }
  }

  notifyDataReload(): void {
    this.listeners.forEach((listener: DataChangeListener) => {
      listener.onDataReloaded();
    });
  }

  notifyDataAdd(index: number): void {
    this.listeners.forEach((listener: DataChangeListener) => {
      listener.onDataAdd(index);
    });
  }

  notifyDataChange(index: number): void {
    this.listeners.forEach((listener: DataChangeListener) => {
      listener.onDataChange(index);
    });
  }

  notifyDataDelete(index: number): void {
    this.listeners.forEach((listener: DataChangeListener) => {
      listener.onDataDelete(index);
    });
  }

  notifyDataMove(from: number, to: number): void {
    this.listeners.forEach((listener: DataChangeListener) => {
      listener.onDataMove(from, to);
    });
  }
}
```
 
示例运行说明：
 
- 首次运行的代码的结果如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/raAVrcFARs6XZbQ7UHgIJA/zh-cn_image_0000002628821232.png?HW-CC-KV=V1&HW-CC-Date=20260701T041221Z&HW-CC-Expire=86400&HW-CC-Sign=E657911186C1C1A3191A0854D3CB44021D82A3FF75749B82FD6D536D1E33CFC7)

- 点击“分组1 code1”和“分组1 code2”，对应属性发生变化。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/wiDJKmygS_Cv_F19uWfV-w/zh-cn_image_0000002659020541.png?HW-CC-KV=V1&HW-CC-Date=20260701T041221Z&HW-CC-Expire=86400&HW-CC-Sign=62C3323B0BE19614FB82D15D1E1A529250089EAEA1CA5ECF9E8249646BFFB9F1)

- 接下来，点击“重新请求数据”，返回的数据和原始数据相同，对应的“分组1 code1ss”和“分组1 code2ss”应该恢复到原始状态，如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/oRK51UhgSs2QFAOkXFhbdw/zh-cn_image_0000002628661342.png?HW-CC-KV=V1&HW-CC-Date=20260701T041221Z&HW-CC-Expire=86400&HW-CC-Sign=061BBD9020687E784AF5A1C292C80E9CC8F82E562FBF5AC387CB43EB5D7A8079)
