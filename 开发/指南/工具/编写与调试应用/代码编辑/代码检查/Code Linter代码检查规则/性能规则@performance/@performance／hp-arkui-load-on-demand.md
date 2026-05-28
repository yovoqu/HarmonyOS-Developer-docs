# @performance/hp-arkui-load-on-demand

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-load-on-demand

建议使用按需加载。
 
滑动丢帧场景下，建议优先修改。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    <span style="color: rgb(135,16,148);">"@performance/hp-arkui-load-on-demand"</span>: <span style="color: rgb(6,125,23);">"warn"</span>,
  }
}
```
 
 

#### 选项

该规则无需配置额外选项。
 
 

#### 正例

```text
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';

@Reusable
@Component
struct ItemComponent {
  @State introduce: string = ''

  aboutToReuse(params: Record<string, ESObject>) {
    this.introduce = params.introduce
  }

  build() {
    Text(this.introduce)
      .fontSize(14)
      .padding({ left: 5, right: 5 })
      .margin({ top: 5 })
  }
}

@Entry
@Component
struct MyComponent {
  private data: MyDataSource = new MyDataSource()

  build() {
    List() {
      LazyForEach(this.data, (item: string) => {
        ListItem() {
          // 使用reuseId对不同的自定义组件实例分别标注复用组，以达到最佳的复用效果
          ItemComponent({ introduce: item }).reuseId(item)
        }
      }, (item: string) => item)
    }
    .width('100%')
    .height('100%')
  }
}
```
 
 

#### 反例

```text
@Entry
@Component
struct MyComponent {
  @State arr: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

  build() {
    List() {
      // List中建议使用LazyForEach
      ForEach(this.arr, (item: number) => {
        ListItem() {
          Text(`item value: ${item}`)
        }
      }, (item: number) => item.toString())
    }
    .width('100%')
    .height('100%')
  }
}
```
 
 

#### 规则集

```text
<span style="color: rgb(106,135,89);">plugin:@performance/recommended</span>
plugin:@performance/all
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
