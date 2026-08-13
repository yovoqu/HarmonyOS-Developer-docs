# wrapBuilder：封装全局@Builder

更新时间：2026-08-03 11:34:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-wrapbuilder

当在一个struct内使用多个全局@Builder函数实现UI的不同效果时，代码维护将变得非常困难，且页面不够整洁。此时，可以使用[wrapBuilder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-wrapbuilder)封装全局@Builder。

在阅读本文档前，建议阅读：[@Builder](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builder)。

> [!NOTE]
> 从API version 11开始支持。 从API version 12开始，wrapBuilder支持在元服务中使用。 从API version 22开始，推荐开发者使用 mutableBuilder ，支持二次赋值后刷新UI。


当@Builder方法赋值给变量或者数组后，在UI方法中无法使用。

```text
@Builder
function builderElement() {}

let builderArr: Function[] = [builderElement];
@Builder
function testBuilder() {
  // builderElement赋值给变量或者数组后，在UI方法中无法使用
  ForEach(builderArr, (item: Function) => {
    item();
  })
}
```

在上述代码中，builderArr是一个由@Builder方法组成的数组。在ForEach循环中取每个@Builder方法时，会出现@Builder方法在UI方法中无法使用的问题。

为了解决这一问题，引入wrapBuilder作为全局@Builder封装函数。wrapBuilder返回WrappedBuilder对象，用于[全局@Builder](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builder#全局自定义构建函数)的赋值和传递。


#### 接口说明

wrapBuilder是一个模板函数，返回一个WrappedBuilder对象。

```text
declare function wrapBuilder<Args extends Object[]>(builder: (...args: Args) => void): WrappedBuilder<Args>;
```

同时 WrappedBuilder对象也是一个模板类。

```text
declare class WrappedBuilder<Args extends Object[]> {
  builder: (...args: Args) => void;

  constructor(builder: (...args: Args) => void);
}
```

> [!NOTE]
> 模板参数Args extends Object[]需要匹配@Builder函数参数的类型。


使用方法：

```text
let builderVar: WrappedBuilder<[string, number]> = wrapBuilder(MyBuilder);
let builderArr: WrappedBuilder<[string, number]>[] = [wrapBuilder(MyBuilder)]; // 可以放入数组
```



#### 限制条件
1. wrapBuilder方法只能传入[全局@Builder](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builder#全局自定义构建函数)方法。
2. WrappedBuilder对象的builder属性方法仅限在struct内部使用。



#### @Builder方法赋值给变量

使用@Builder装饰器装饰的方法myBuilder作为wrapBuilder的参数，然后将wrapBuilder的返回值赋值给变量globalBuilder，以解决@Builder方法赋值给变量后无法使用的问题。

```ArkTS
@Builder
function myBuilder(value: string, size: number) {
  Text(value)
    .fontSize(size)
    .margin(10)
}

// 使用wrapBuilder封装myBuilder，并赋值给globalBuilder变量
let globalBuilder: WrappedBuilder<[string, number]> = wrapBuilder(myBuilder);

@Entry
@Component
struct TestIndex {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        globalBuilder.builder(this.message, 50);
      }
      .width('100%')
    }
    .height('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/CuDZ0wRhTEKRkv8bT17kqg/zh-cn_image_0000002704391941.png?HW-CC-KV=V1&HW-CC-Date=20260813T095701Z&HW-CC-Expire=86400&HW-CC-Sign=1A64445BA2D2D6EED622B431082D0EF8BB318A2BBFA3A24039D4E1BEE682BD70)




#### @Builder方法赋值给变量在UI语法中使用

自定义组件IndexItem使用ForEach进行不同@Builder函数的渲染，可以使用builderArr声明的wrapBuilder数组来实现不同的@Builder函数的效果。整体代码会更加整洁。

```ArkTS
@Builder
function myBuilder0(value: string, size: number) {
  Text(value)
    .fontSize(size)
    .fontColor(Color.Blue)
    .margin(10)
}

@Builder
function yourBuilder(value: string, size: number) {
  Text(value)
    .fontSize(size)
    .fontColor(Color.Pink)
    .margin(10)
}

const builderArr: WrappedBuilder<[string, number]>[] = [wrapBuilder(myBuilder0), wrapBuilder(yourBuilder)];

@Entry
@Component
struct IndexItem {
  @Builder
  IndexItem() {
    // IndexItem使用ForEach进行不同@Builder函数的渲染
    ForEach(builderArr, (item: WrappedBuilder<[string, number]>) => {
      item.builder('Hello World', 30);
    })
  }

  build() {
    Row() {
      Column() {
        this.IndexItem();
      }
      .width('100%')
    }
    .height('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/j4z9KAGwQCeo_EIYJWYVhw/zh-cn_image_0000002674631818.png?HW-CC-KV=V1&HW-CC-Date=20260813T095701Z&HW-CC-Expire=86400&HW-CC-Sign=FBA2E2E3FF176DCF484DC539D183F6708ECA67AA29761C516C6639F372A8355A)




#### @Builder方法赋值给类或者接口的属性

使用@Builder装饰器装饰的方法myBuilder作为wrapBuilder的参数，然后将wrapBuilder的返回值赋值给接口ChildOptions中的属性，可以以数据的形式传递给其他子组件调用。

```ArkTS
@Builder
function myBuilder(value: string, size: number) {
  Text(value)
    .fontSize(size)
    .margin(10)
}

interface ChildOptions {
  wrappedBuilder: WrappedBuilder<[string, number]>; // 类型为WrappedBuilder的属性可以传递@Builder函数
}

@Entry
@Component
struct Index {
  childOptions: ChildOptions = {
    wrappedBuilder: wrapBuilder(myBuilder)
  };

  build() {
    Row() {
      Column() {
        Child({ options: this.childOptions })
      }
      .width('100%')
    }
    .height('100%')
  }
}

@Component
struct Child {
  @Prop options: ChildOptions;
  build() {
    this.options.wrappedBuilder.builder('Hello', 20);
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/I0FGrs7USBWBp2_ZFHRyag/zh-cn_image_0000002704271773.png?HW-CC-KV=V1&HW-CC-Date=20260813T095701Z&HW-CC-Expire=86400&HW-CC-Sign=6AD380801F16F9F72CECF6087FA853AFFDC274120EECCE04F96D7C0C294C1250)




#### 引用传递

按引用传递参数时，状态变量的改变会引起@Builder方法内的UI刷新。

```ArkTS
class Tmp {
  public paramA2: string = 'hello';
}

@Builder
function overBuilder(param: Tmp) {
  Column() {
    Text(`wrapBuildervalue:${param.paramA2}`)
      .fontSize(20)
      .margin(10)
  }
  .width('100%')
}

const wBuilder: WrappedBuilder<[Tmp]> = wrapBuilder(overBuilder);

@Entry
@Component
struct Parent {
  @State label: Tmp = new Tmp();

  build() {
    Column() {
      // 引用传递参数，label.paramA2的改变会引起overBuilder内的UI刷新
      wBuilder.builder({ paramA2: this.label.paramA2 });
      Button('Click me')
        .width(300)
        .margin(10)
        .onClick(() => {
          this.label.paramA2 = 'ArkUI';
        })
    }
    .width('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/MiiT8C6sRfmHaa_WeomxPg/zh-cn_image_0000002674471974.gif?HW-CC-KV=V1&HW-CC-Date=20260813T095701Z&HW-CC-Expire=86400&HW-CC-Sign=6B20C07655C7740390E48B27F1493437DFE926009817AE75D727125CBF16A958)




#### 常见问题



#### 重复定义wrapBuilder失效

在同一个自定义组件内，同一个wrapBuilder只能初始化一次。例如，builderObj通过wrapBuilder(myBuilderFirst)初始化后，再次对builderObj赋值wrapBuilder(myBuilderSecond)将不会生效。

```ArkTS
@Builder
function myBuilderFirst(value: string, size: number) {
  Text('MyBuilderFirst：' + value)
    .fontSize(size)
    .margin(10)
}

@Builder
function myBuilderSecond(value: string, size: number) {
  Text('MyBuilderSecond：' + value)
    .fontSize(size)
    .margin(10)
}

interface BuilderModel {
  globalBuilder: WrappedBuilder<[string, number]>;
}

@Entry
@Component
struct TestBuilderIndex {
  @State message: string = 'Hello World';
  @State builderObj: BuilderModel = { globalBuilder: wrapBuilder(myBuilderFirst) };

  aboutToAppear(): void {
    setTimeout(() => {
      // wrapBuilder(myBuilderSecond) 不会生效
      this.builderObj.globalBuilder = wrapBuilder(myBuilderSecond);
    }, 1000);
  }

  build() {
    Row() {
      Column() {
        this.builderObj.globalBuilder.builder(this.message, 20);
      }
      .width('100%')
    }
    .height('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/jbyibByZTOWS2TRu4XaYPg/zh-cn_image_0000002704391943.png?HW-CC-KV=V1&HW-CC-Date=20260813T095701Z&HW-CC-Expire=86400&HW-CC-Sign=FE26BBA7F84011E59FCD8F8835AD8E427124DD946B64411FF120019446263F0D)
