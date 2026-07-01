# 如何使用ListItemGroup和LazyForEach结合并实现组件复用

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-321

可参考如下代码：
 
```text
@Entry
@Component
struct ListItemGroupAndReusable {
  data: DataSrc2 = new DataSrc2();

  @Builder
  itemHead(text: string) {
    Text(text)
      .fontSize(20)
      .backgroundColor(0xAABBCC)
      .width('100%')
      .padding(10)
  }

  aboutToAppear() {
    for (let i = 0; i < 10000; i++) {
      let currentData = new DataSrc1();
      for (let j = 0; j < 12; j++) {
        currentData.Data.push(`Test Data Test Data Test Data: ${i} - ${j}`);
      }
      this.data.Data.push(currentData);
    }
  }

  build() {
    Stack() {
      List() {
        LazyForEach(this.data, (item: DataSrc1, index: number) => {
          ListItemGroup({ header: this.itemHead(index.toString()) }) {
            LazyForEach(item, (ii: string, index: number) => {
              ListItem() {
                Inner({ str: ii })
              }
            })
          }
          .width('100%')
          .height('60vp')
        })
      }
      .cachedCount(10)
    }
    .width('100%')
    .height('100%')
  }
}


@Reusable
@Component
struct Inner {
  @State str: string = '';

  aboutToReuse(param: ESObject) {
    this.str = param.str;
  }

  build() {
    Text(this.str)
  }
}


class DataSrc1 implements IDataSource {
  listeners: DataChangeListener[] = [];
  Data: string[] = [];

 <em> // data count</em>
  public totalCount(): number {
    return this.Data.length;
  }

  <em>// get data by index</em>
  public getData(index: number): string {
    return this.Data[index];
  }

<em>  // This method is called on the framework side to add listener listening to the LazyForEach component at its data source</em>
  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener) < 0) {
      this.listeners.push(listener);
    }
  }

  <em>// This method is called on the framework side to remove listener listening for the corresponding LazyForEach component at the data source</em>
  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      this.listeners.splice(pos, 1);
    }
  }
}


class DataSrc2 implements IDataSource {
  listeners: DataChangeListener[] = [];
  Data: DataSrc1[] = [];

  <em>// data count</em>
  public totalCount(): number {
    return this.Data.length;
  }

  <em>// get data by index</em>
  public getData(index: number): DataSrc1 {
    return this.Data[index];
  }

 <em> // This method is called on the framework side to add listener listening to the LazyForEach component at its data source</em>
  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener) < 0) {
      this.listeners.push(listener);
    }
  }

  <em>// This method is called on the framework side to remove listener listening for the corresponding LazyForEach component at the data source</em>
  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      this.listeners.splice(pos, 1);
    }
  }
}
```
