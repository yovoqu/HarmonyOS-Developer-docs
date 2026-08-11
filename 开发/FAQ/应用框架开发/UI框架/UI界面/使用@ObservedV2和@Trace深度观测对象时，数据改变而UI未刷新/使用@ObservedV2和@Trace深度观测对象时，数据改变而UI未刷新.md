# 使用@ObservedV2和@Trace深度观测对象时，数据改变而UI未刷新

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1011

#### 问题现象

在开发过程中，当我们想对一个嵌套对象实现深度观测时，通常会使用V2版本的@ObservedV2和@Trace装饰器。但是常常会出现对象对应的实例数据变化了，而对应的UI未刷新的情况。一般有下面几种常见的问题场景：
  
| 常见问题场景 | 问题描述 |
| --- | --- |
| 场景一 | @ObservedV2装饰的对象属性的值改变了，对应的UI未刷新。 |
| 场景二 | @ObservedV2装饰的对象中使用了三方包中的类，三方包中类的实例数据变化了，对应的UI未刷新。 |
| 场景三 | @ObservedV2装饰的对象经过序列化和反序列化之后，失去观察能力。 |
 
1. **场景一**：@ObservedV2装饰的对象属性的值改变了，对应的UI未刷新。案例如下：
```text
@ObservedV2
class ItemModel {
<em>  // 需要修改的属性值</em>
  @Trace value: string = '';
}

class ListModel {
<em>  // 通过静态数据直接初始化</em>
  static data: ItemModel[] = [
    {
      value: '修改前的值为：A'
    }
  ];
}

@ObservedV2
class ListViewModel {
<em>  // 数据赋值给listData</em>
  @Trace listData: ItemModel[] = ListModel.data;
}

@Entry
@ComponentV2
struct Index {
  @Local listViewModel: ListViewModel = new ListViewModel();

  build() {
    Row() {
      ForEach(this.listViewModel.listData, (item: ItemModel) => {
        Column() {
          Text(item.value)
            .fontSize(30)
            .fontWeight(FontWeight.Bold)
          Button('修改value值')
            .onClick(()=>{
              item.value = '修改后的值为：B';
            })
        }.width('100%')
      })
    }.height('100%')
  }
}
```

2. **场景二**：@ObservedV2装饰的对象中使用了三方包中的类，三方包中类的实例数据变化了，对应的UI未刷新。案例如下：
```text
<em>// PhoneInfo类定义在三方包中，无法使用@ObservedV2/@Trace</em>
class PhoneInfo {
  phone: string = '';

  constructor(phone: string) {
    this.phone = phone;
  }
}

@ObservedV2
class Person {
  name: string = '';
  @Trace age: number = 0;
  @Trace phoneInfo: PhoneInfo = new PhoneInfo('');

  constructor(name: string, age:number, phoneInfo: PhoneInfo) {
    this.name = name;
    this.age = age;
    this.phoneInfo = phoneInfo;
  }
}

@Entry
@ComponentV2
struct Index2 {
  @Local person: Person = new Person('小明', 18, new PhoneInfo('188****8888'));

  build() {
    Row() {
      Column() {
        Text(`name: ${this.person.name}`)
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
        Text(`age: ${this.person.age}`)
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
        Text(`phone: ${this.person.phoneInfo.phone}`)
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
        Button('模拟接口获取数据')
          .onClick(() => {
          <em>  // 模拟接口获取数据</em>
            this.person.age = 19;
            this.person.phoneInfo.phone = '199****9999';
          })
      }.width('100%')
    }.height('100%')
  }
}
```

3. **场景三**：@ObservedV2装饰的对象经过序列化和反序列化之后，失去观察能力。
 
 

#### 背景知识

- [@ObservedV2和@Trace](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-observedv2-and-trace)提供了对嵌套类对象属性变化直接观测的能力，常用于复杂对象的深度观测。
- @ObservedV2与@Trace的[概述](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-observedv2-and-trace#概述)中提到：使用@ObservedV2与@Trace装饰器的类，需通过new操作符实例化后，才具备被观测变化的能力。
- [makeObserved](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-makeobserved)接口可以将普通不可观察数据变为可观察数据。

 
 

#### 解决方案

对于上述几种场景，解决方案总结如下：
  
| 常见问题场景 | 问题描述 | 解决方案 |
| --- | --- | --- |
| 场景一 | @ObservedV2装饰的对象属性的值改变了，对应的UI未刷新。 | 需通过new操作符实例化才能具备可观测能力。 |
| 场景二 | @ObservedV2装饰的对象中使用了三方包中的类，三方包中类的实例数据变化了，对应的UI未刷新。 | 使用makeObserved接口将不可观察的数据变为可观察。 |
| 场景三 | @ObservedV2装饰的对象经过序列化和反序列化之后，失去观察能力。 | 参考官网指南中的@ObservedV2装饰对象的序列化与反序列化。 |
 
 
下面将逐个分析上述案例和具体修改方案：
 1. **场景一**：@ObservedV2装饰的对象属性的值改变了，对应的UI未刷新。查看场景一的案例代码可以看到，ListModel.data是通过静态数据直接初始化的。联系背景知识中的说明，就知道问题所在了：ItemModel类的初始化没有通过new操作符实例化，所以不具备可被观测的能力。

  修改之后的完整代码如下：
```text
@ObservedV2
class ItemModel {
 <em> // 需要修改的属性值</em>
  @Trace value: string = '';

  constructor(value: string) {
    this.value = value;
  }
}

class ListModel {
 <em> // ItemModel需要使用new初始化</em>
  static data: ItemModel[] = [
    new ItemModel('修改前的值为：A')
  ];
}

@ObservedV2
class ListViewModel {
 <em> // 数据赋值给listData</em>
  @Trace listData: ItemModel[] = ListModel.data;
}

@Entry
@ComponentV2
struct Index1 {
  @Local listViewModel: ListViewModel = new ListViewModel();

  build() {
    Row() {
      ForEach(this.listViewModel.listData, (item: ItemModel) => {
        Column() {
          Text(item.value)
            .fontSize(30)
            .fontWeight(FontWeight.Bold)
          Button('修改value值')
            .onClick(() => {
              item.value = '修改后的值为：B';
            })
        }.width('100%')
      })
    }.height('100%')
  }
}
```


  运行效果如下：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/T5Ow_1JxQI2FFBl4kAiMIw/zh-cn_image_0000002628564680.png?HW-CC-KV=V1&HW-CC-Date=20260811T005654Z&HW-CC-Expire=86400&HW-CC-Sign=454C4FC1EB2BE05C444C46D896B59441463127F899E0ED8B7D61EF656758AC8E)

2. **场景二**：@ObservedV2装饰的对象中使用了三方包中的类，三方包中类的实例数据变化了，对应的UI未刷新。由于PhoneInfo类是一个三方包中的类，无法被@ObservedV2装饰，即便Person类中phoneInfo属性使用@Trace装饰，也不能进行深度观测。所以可以使用makeObserved接口将不可观察的数据变为可观察。

  
> [!NOTE]
> 使用了makeObserved之后，原来Person类也不需要使用@ObservedV2和@Trace装饰，不然会导致深度观测失效。因为makeObserved不支持传入被@ObservedV2装饰的类的实例。为了防止数据被双重代理，makeObserved发现入参为上述情况时则直接返回，不做处理。


  修改之后的完整代码如下：

  
```text
import { UIUtils } from '@kit.ArkUI';

<em>// PhoneInfo类定义在三方包中，无法使用@ObservedV2/@Trace</em>
class PhoneInfo {
  phone: string = '';

  constructor(phone: string) {
    this.phone = phone;
  }
}

class Person {
  name: string = '';
  age: number = 0;
  phoneInfo: PhoneInfo = new PhoneInfo('');

  constructor(name: string, age:number, phoneInfo: PhoneInfo) {
    this.name = name;
    this.age = age;
    this.phoneInfo = phoneInfo;
  }
}

@Entry
@ComponentV2
struct Index2 {
  @Local person: Person = UIUtils.makeObserved(new Person('小明', 18, new PhoneInfo('188****8888')));

  build() {
    Row() {
      Column() {
        Text(`name: ${this.person.name}`)
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
        Text(`age: ${this.person.age}`)
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
        Text(`phone: ${this.person.phoneInfo.phone}`)
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
        Button('模拟接口获取数据')
          .onClick(() => {
          <em>  // 模拟接口获取数据</em>
            this.person.age = 19;
            this.person.phoneInfo.phone = '199****9999';
          })
      }.width('100%')
    }.height('100%')
  }
}
```
 运行效果如下：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/MCUiruAlQCiNVpWrgsyF4w/zh-cn_image_0000002658923995.png?HW-CC-KV=V1&HW-CC-Date=20260811T005654Z&HW-CC-Expire=86400&HW-CC-Sign=793CA07E9F4D8FDA0CF76B8F795FE306F20E457337A741540A85471BBB40FF3A)

3. **场景三**：@ObservedV2装饰的对象经过序列化和反序列化之后，失去观察能力。@ObservedV2装饰的对象序列化后会为@Trace装饰的属性添加__ob_前缀，将@ObservedV2装饰的对象通过JSON.stringify序列化后，再通过JSON.parse反序列化，将失去观察能力。涉及到@ObservedV2装饰对象的序列化与反序列化，解决方案可以参考官网指南中的[@ObservedV2装饰对象的序列化与反序列化](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-observedv2-and-trace#observedv2装饰对象的序列化与反序列化)。
