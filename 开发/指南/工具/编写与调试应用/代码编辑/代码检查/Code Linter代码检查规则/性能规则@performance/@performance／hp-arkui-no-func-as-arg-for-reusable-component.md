# @performance/hp-arkui-no-func-as-arg-for-reusable-component

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-no-func-as-arg-for-reusable-component

避免使用函数作为复用的自定义组件创建时的入参。

 滑动丢帧场景下，建议优先修改。


## 规则配置


```text
// code-linter.json5
{
  "rules": {
    "@performance/hp-arkui-no-func-as-arg-for-reusable-component": "warn",
  }
}
```


## 选项

该规则无需配置额外选项。

## 正例


```text
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';

@Reusable
@Component
struct ChildComponent {
  @State desc: string = '';
  @State sum: number = 0;

  aboutToReuse(params: Record): void {
    this.desc = params.desc as string;
    this.sum = params.sum as number;
  }

  build() {
    Column() {
      Text('子组件' + this.desc)
        .fontSize(30)
        .fontWeight(30)
      Text('结果' + this.sum)
        .fontSize(30)
        .fontWeight(30)
    }
  }
}

@Entry
@Component
struct MyComponent{
  private data: MyDataSource = new MyDataSource();
  @State sum: number = 0;

  aboutToAppear(): void {
    for (let index = 0; index  {
          ListItem() {
            // 子组件的传参通过状态变量进行
            ChildComponent({ desc: item, sum: this.sum })
          }
          .width('100%')
          .height(100)
        }, (item: string) => item)
      }
      .width('100%')
      .height('100%')
    }
  }
}
```


## 反例


```text
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';

// 此处为复用的自定义组件
@Reusable
@Component
struct ChildComponent {
  @State desc: string = '';
  @State sum: number = 0;

  aboutToReuse(params: Record): void {
    this.desc = params.desc as string;
    this.sum = params.sum as number;
  }

  build() {
    Column() {
      Text('子组件' + this.desc)
        .fontSize(30)
        .fontWeight(30)
      Text('结果' + this.sum)
        .fontSize(30)
        .fontWeight(30)
    }
  }
}

@Entry
@Component
struct MyComponent{
  private data: MyDataSource = new MyDataSource();

  aboutToAppear(): void {
    for (let index = 0; index  {
          ListItem() {
            // 此处sum参数是函数获取的，实际开发场景无法预料该函数可能出现的耗时操作，每次进行组件复用都会重复触发此函数的调用
            ChildComponent({ desc: item, sum: this.count() })
          }
          .width('100%')
          .height(100)
        }, (item: string) => item)
      }
      .height('100%')
      .width('100%')
    }
  }
}
```


## 规则集


```text
plugin:@performance/recommended
plugin:@performance/all
```

 Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
