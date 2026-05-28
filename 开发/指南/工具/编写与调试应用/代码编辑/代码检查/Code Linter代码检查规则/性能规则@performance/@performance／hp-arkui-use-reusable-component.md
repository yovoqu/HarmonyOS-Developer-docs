# @performance/hp-arkui-use-reusable-component

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-use-reusable-component

建议复杂组件的定义，尽量使用组件复用。
 
滑动丢帧场景下，建议优先修改。
 

##### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    <span style="color: rgb(135,16,148);">"@performance/hp-arkui-use-reusable-component"</span>: <span style="color: rgb(6,125,23);">"warn"</span>,
  }
}
```
 
 

##### 选项

该规则无需配置额外选项。
 
 

##### 正例

```text
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';
import { GoodItems } from './data/DataEntry';

@Reusable
@Component
struct GoodItemComponent {
  @State introduce: string = ''
  @State price: string = ''
  @State numb: string = ''

  aboutToReuse(params: Record<string, ESObject>) {
    this.introduce = params.introduce
    this.price = params.price
    this.numb = params.numb
  }

  build() {
    Column() {
      Text(this.introduce)
        .fontSize(14)
        .padding({ left: 5, right: 5 })
        .margin({ top: 5 })
      Row() {
        Text('￥')
          .fontSize(10)
          .fontColor(Color.Red)
          .baselineOffset(-4)
        Text(this.price)
          .fontSize(16)
          .fontColor(Color.Red)
        Text(this.numb)
          .fontSize(10)
          .fontColor(Color.Gray)
          .baselineOffset(-4)
          .margin({ left: 5 })

      }
      .width('100%')
      .justifyContent(FlexAlign.SpaceBetween)
      .padding({ left: 5, right: 5 })
      .margin({ top: 15 })
    }
  }
}

@Entry
@Component
struct MyComponent{
  private data: MyDataSource = new MyDataSource([]);

  build() {
    Column() {
      LazyForEach(this.data, (item: GoodItems, index) => {
        GridItem() {
          GoodItemComponent({
            introduce: item.data.introduce,
            price: item.data.price,
            numb: item.data.numb,
          }).reuseId(item.numb)
        }
      }, (item: GoodItems) => item.index)
    }
  }
}
```
 
 

##### 反例

```text
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';
import { GoodItems } from './data/DataEntry';

@Entry
@Component
struct MyComponent{
  private data: MyDataSource = new MyDataSource([]);

  build() {
    Column() {
      LazyForEach(this.data, (item: GoodItems) => {
        GridItem() {
          Column() {
            Text(item.introduce)
              .fontSize(14)
              .padding({ left: 5, right: 5 })
              .margin({ top: 5 })
            Row() {
              Text('￥')
                .fontSize(10)
                .fontColor(Color.Red)
                .baselineOffset(-4)
              Text(item.price)
                .fontSize(16)
                .fontColor(Color.Red)
              Text(item.numb)
                .fontSize(10)
                .fontColor(Color.Gray)
                .baselineOffset(-4)
                .margin({ left: 5 })

            }
            .width('100%')
            .justifyContent(FlexAlign.SpaceBetween)
            .padding({ left: 5, right: 5 })
            .margin({ top: 15 })
          }
          .borderRadius(10)
          .backgroundColor(Color.White)
          .clip(true)
          .width('100%')
          .height(290)
        }
      }, (item: GoodItems) => item.index)
    }
  }
}
```
 
 

##### 规则集

```text
<span style="color: rgb(106,135,89);">plugin:@performance/recommended</span>
plugin:@performance/all
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
