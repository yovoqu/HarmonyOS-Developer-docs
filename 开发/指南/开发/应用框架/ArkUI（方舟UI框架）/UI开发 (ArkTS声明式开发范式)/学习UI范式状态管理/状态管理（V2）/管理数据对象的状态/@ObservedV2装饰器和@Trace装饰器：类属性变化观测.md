# @ObservedV2装饰器和@Trace装饰器：类属性变化观测

更新时间：2026-08-03 11:34:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-observedv2-and-trace

为了增强状态管理框架对类对象中属性的观测能力，开发者可以使用[@ObservedV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management-observedv2#observedv2)装饰器和[@Trace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management-trace#trace)装饰器装饰类以及类中的属性。

@ObservedV2和@Trace提供了对嵌套类对象属性变化直接观测的能力，是状态管理V2中相对核心的能力之一。在阅读本文档前，建议提前阅读：[状态管理概述](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-overview)来了解状态管理V2整体的能力架构。

> [!NOTE]
> @ObservedV2与@Trace装饰器从API version 12开始支持。 从API version 12开始，@ObservedV2与@Trace装饰器支持在ArkTS卡片中使用。 从API version 12开始，@ObservedV2与@Trace装饰器支持在元服务中使用。



#### 概述

@ObservedV2装饰器与@Trace装饰器用于装饰类以及类中的属性，使得被装饰的类和属性具有深度观测的能力：

 - @ObservedV2装饰器与@Trace装饰器需要配合使用，单独使用@ObservedV2装饰器或@Trace装饰器没有任何作用。
 - 被@Trace装饰器装饰的属性property变化时，仅会通知property关联的组件进行刷新。
 - 在嵌套类中，嵌套类中的属性property被@Trace装饰且嵌套类被@ObservedV2装饰时，才具有触发UI刷新的能力。
 - 在继承类中，父类或子类中的属性property被@Trace装饰且该property所在类被@ObservedV2装饰时，才具有触发UI刷新的能力。
 - 未被@Trace装饰的属性用在UI中无法感知到变化，也无法触发UI刷新。
 - 使用@ObservedV2与@Trace装饰器的类，需通过new操作符实例化后，才具备被观测变化的能力。




#### 状态管理V1版本对嵌套类对象属性变化直接观测的局限性

现有状态管理V1版本无法实现对嵌套类对象属性变化的直接观测。

```ArkTS
@Observed
class Father {
  public son: Son;

  constructor(name: string, age: number) {
    this.son = new Son(name, age);
  }
}

@Observed
class Son {
  public name: string;
  public age: number;

  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
  }
}

@Entry
@Component
struct Index {
  @State father: Father = new Father('John', 8);

  build() {
    Row() {
      Column() {
        Text(`name: ${this.father.son.name} age: ${this.father.son.age}`)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            // 嵌套类对象属性变化无法观测
            this.father.son.age++;
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```


![](assets/@ObservedV2装饰器和@Trace装饰器：类属性变化观测/file-20260514130524688-1.gif)


在上述代码中，点击Text组件增加age的值时，不会触发UI刷新。原因在于现有的状态管理框架无法观测到嵌套类中属性age的值变化。V1版本的解决方案是使用[@ObjectLink装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-observed-and-objectlink)与自定义组件来实现观测。

```ArkTS
@Observed
class Father {
  public son: Son;

  constructor(name: string, age: number) {
    this.son = new Son(name, age);
  }
}

@Observed
class Son {
  public name: string;
  public age: number;

  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
  }
}

@Component
struct Child {
  // @Observed对象与@ObjectLink一起使用，实现对嵌套类对象属性的观测能力
  @ObjectLink son: Son;

  build() {
    Row() {
      Column() {
        Text(`name: ${this.son.name} age: ${this.son.age}`)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .margin(10)
          .onClick(() => {
            this.son.age++;
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

@Entry
@Component
struct Index {
  @State father: Father = new Father('John', 8);

  build() {
    Column() {
      Child({ son: this.father.son })
    }
    .width('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/lBQKq32eTtiUqkpybMYELg/zh-cn_image_0000002674631902.gif?HW-CC-KV=V1&HW-CC-Date=20260813T095706Z&HW-CC-Expire=86400&HW-CC-Sign=B81E167EBF44578899E6F0626AA67223F792686D98368E6BCCCF49DD4DB8AECB)


通过这种方式虽然能够实现对嵌套类中属性变化的观测，但是当嵌套层级较深时，代码将会变得十分复杂，易用性差。因此推出类装饰器@ObservedV2与成员变量装饰器@Trace，增强对嵌套类中属性变化的观测能力。



#### 装饰器说明

| @ObservedV2类装饰器 | 说明 |
| --- | --- |
| 装饰器参数 | 无。 |
| 类装饰器 | 装饰class。需要放在class的定义前，使用new创建类对象。 |


| @Trace成员变量装饰器 | 说明 |
| --- | --- |
| 装饰器参数 | 无。 |
| 可装饰的变量 | class中成员属性。属性的类型可以为number、string、boolean、class、Array、Date、Map、Set等类型。@Trace不支持观察Function类型的数据，修改@Trace装饰的Function类型的数据，UI不会刷新。 |




#### 观察变化

使用@ObservedV2装饰的类中被@Trace装饰的属性具有被观测变化的能力，当该属性值变化时，会触发该属性绑定的UI组件刷新。

 - 在嵌套类中使用@Trace装饰的属性具有被观测变化的能力。


```ArkTS
@ObservedV2
class Son {
  @Trace public age: number = 100;
}

class Father {
  public son: Son = new Son();
}

@Entry
@ComponentV2
struct Index {
  father: Father = new Father();

  build() {
    Column() {
      // 当点击改变age时，Text组件会刷新
      Text(`${this.father.son.age}`)
        .fontSize(20)
        .margin(10)
        .onClick(() => {
          this.father.son.age++;
        })
    }
    .width('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/-7nyAG7ATnKms3oojx4N7A/zh-cn_image_0000002704271857.gif?HW-CC-KV=V1&HW-CC-Date=20260813T095706Z&HW-CC-Expire=86400&HW-CC-Sign=48A1679BF0FC60FF98CE549238051C2AA14A98CA8EC9E687A0C1DB4450780683)


 - 在继承类中使用@Trace装饰的属性具有被观测变化的能力。


```ArkTS
@ObservedV2
class Father {
  @Trace public name: string = 'Tom';
}

class Son extends Father {
}

@Entry
@ComponentV2
struct Index {
  son: Son = new Son();

  build() {
    Column() {
      // 当点击改变name时，Text组件会刷新
      Text(`${this.son.name}`)
        .fontSize(20)
        .margin(10)
        .onClick(() => {
          this.son.name = 'Jack';
        })
    }
    .width('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/EhJUU7ATSyCRNR5LA27Ojg/zh-cn_image_0000002674472058.gif?HW-CC-KV=V1&HW-CC-Date=20260813T095706Z&HW-CC-Expire=86400&HW-CC-Sign=0ECDC3E3B4D7B7425FF9C8F5D5EA8A4F409AD50CE25D6442637B33D885524F2B)


 - 类中使用@Trace装饰的静态属性具有被观测变化的能力。


```ArkTS
@ObservedV2
class Manager {
  @Trace public static count: number = 1;
}

@Entry
@ComponentV2
struct Index {
  build() {
    Column() {
      // 当点击改变count时，Text组件会刷新
      Text(`${Manager.count}`)
        .fontSize(20)
        .margin(10)
        .onClick(() => {
          Manager.count++;
        })
    }
    .width('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/YEV0fADWTvG2WOSxasWrzQ/zh-cn_image_0000002704392027.gif?HW-CC-KV=V1&HW-CC-Date=20260813T095706Z&HW-CC-Expire=86400&HW-CC-Sign=81E03E7590AB74C141EE30EE4FE2490926C3199766C065F0B3A56C12F4A7594C)


 - @Trace装饰内置类型时，可以观测各自API导致的变化：

| 类型 | 可观测变化的API |

| --- | --- |

| Array | push、pop、shift、unshift、splice、copyWithin、fill、reverse、sort |

| Date | setFullYear, setMonth, setDate, setHours, setMinutes, setSeconds, setMilliseconds, setTime, setUTCFullYear, setUTCMonth, setUTCDate, setUTCHours, setUTCMinutes, setUTCSeconds, setUTCMilliseconds |

| Map | set, clear, delete |

| Set | add, clear, delete |




#### 使用限制

@ObservedV2与@Trace装饰器存在以下使用限制：

 - 非@Trace装饰的成员属性用在UI上无法触发UI刷新。


```ArkTS
@ObservedV2
class Person {
  public id: number = 0;
  @Trace public age: number = 8;
}

@Entry
@ComponentV2
struct Index {
  person: Person = new Person();

  build() {
    Column() {
      // age被@Trace装饰，用在UI中可以触发UI刷新
      Text(`${this.person.age}`)
        .fontSize(20)
        .margin(10)
        .onClick(() => {
          this.person.age++; // 点击会触发UI刷新
        })
      // id未被@Trace装饰，用在UI中不会触发UI刷新
      Text(`${this.person.id}`) // 当id变化时不会刷新
        .fontSize(20)
        .margin(10)
        .onClick(() => {
          this.person.id++; // 点击不会触发UI刷新
        })
    }
    .width('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/yn3uZYGASxu8yC1PLwuX8w/zh-cn_image_0000002674631904.gif?HW-CC-KV=V1&HW-CC-Date=20260813T095706Z&HW-CC-Expire=86400&HW-CC-Sign=20390C1E0325A17251FBBE99609817662C6E1B182DE3F0EB04B4082FAB3F3A56)


 - @ObservedV2仅能装饰class，无法装饰自定义组件。


```text
@ObservedV2 // 错误用法，编译时报错
struct Index {
  build() {
  }
}
```

 - @Trace不能用在没有被@ObservedV2装饰的class上。


```text
class User {
  id: number = 0;
  @Trace name: string = 'Tom'; // 错误用法，编译时报错
}
```

 - @Trace是class中属性的装饰器，不能用在struct中。


```text
@ComponentV2
struct Comp {
  @Trace message: string = 'Hello World'; // 错误用法，编译时报错

  build() {
  }
}
```

 - @ObservedV2、@Trace不能与[@Observed](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-observed-and-objectlink)、[@Track](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-track)混合使用。


```text
@Observed
class User {
  @Trace name: string = 'Tom'; // 错误用法，编译时报错
}

@ObservedV2
class Person {
  @Track name: string = 'Jack'; // 错误用法，编译时报错
}
```

 - 使用@ObservedV2与@Trace装饰的类不能和[@State](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state)等V1的装饰器混合使用，编译时报错。


```ArkTS
// 以@State装饰器为例
@ObservedV2
class Job {
  @Trace public jobName: string = 'Teacher';
}

@ObservedV2
class Info {
  @Trace public name: string = 'Tom';
  @Trace public age: number = 25;
  public job: Job = new Job();
}

@Entry
@ComponentV2
struct Index {
  // @State info: Info = new Info(); 无法混用，编译时报错
  @Local info: Info = new Info();

  build() {
    Column() {
      Text(`name: ${this.info.name}`)
        .fontSize(20)
        .margin(10)
      Text(`age: ${this.info.age}`)
        .fontSize(20)
        .margin(10)
      Text(`jobName: ${this.info.job.jobName}`)
        .fontSize(20)
        .margin(10)
      Button('change age')
        .width(300)
        .margin(10)
        .onClick(() => {
          this.info.age++;
        })
      Button('Change job')
        .width(300)
        .margin(10)
        .onClick(() => {
          this.info.job.jobName = 'Doctor';
        })
    }
    .width('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/iLI0AkRBToaJD__cbtw0uA/zh-cn_image_0000002704271859.gif?HW-CC-KV=V1&HW-CC-Date=20260813T095706Z&HW-CC-Expire=86400&HW-CC-Sign=724683ECC514AC55D023C9A627C34C02481B9DBCB43723A39D9132A97DD6AA0B)


 - 继承自@ObservedV2的类无法和@State等V1的装饰器混用，运行时报错。


```ArkTS
// 以@State装饰器为例
@ObservedV2
class Job {
  @Trace public jobName: string = 'Teacher';
}

@ObservedV2
class Info {
  @Trace public name: string = 'Tom';
  @Trace public age: number = 25;
  public job: Job = new Job();
}

class Message extends Info {
  constructor() {
    super();
  }
}

@Entry
@Component
struct Index {
  // @State message: Message = new Message();  无法混用，运行时报错
  message: Message = new Message();

  build() {
    Column() {
      Text(`name: ${this.message.name}`)
        .fontSize(20)
        .margin(10)
      Text(`age: ${this.message.age}`)
        .fontSize(20)
        .margin(10)
      Text(`jobName: ${this.message.job.jobName}`)
        .fontSize(20)
        .margin(10)
      Button('change age')
        .width(300)
        .margin(10)
        .onClick(() => {
          this.message.age++;
        })
      Button('Change job')
        .width(300)
        .margin(10)
        .onClick(() => {
          this.message.job.jobName = 'Doctor';
        })
    }
    .width('100%')
  }
}
```

 - 使用@ObservedV2与@Trace装饰器的类，需通过new操作符实例化后，才具备被观测变化的能力。
 - @ObservedV2的类实例无法直接使用JSON.parse反序列化获得（直接使用JSON.parse反序列化获得的对象无法观察属性变化），可搭配三方库[class-transformer](https://gitcode.com/CPF-ApplicationTPC/openharmony_tpc_samples/tree/master/class-transformer)实现反序列化后可观察，示例请参考[@ObservedV2装饰对象的序列化与反序列化](#observedv2装饰对象的序列化与反序列化)。




#### 使用场景



#### 嵌套类场景

在下面的嵌套类场景中，Pencil类是Son类中最里层的类，Pencil类被@ObservedV2装饰且属性length被@Trace装饰，此时length的变化能够被观测到。

@Trace装饰器与现有状态管理框架的[@Track](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-track)与[@State](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state)装饰器的能力不同，@Track使class具有属性级更新的能力，但并不具备深度观测的能力；而@State只能观测到对象本身以及第一层的变化，对于多层嵌套场景只能通过封装自定义组件，搭配[@Observed](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-observed-and-objectlink)和[@ObjectLink](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-observed-and-objectlink)来实现观测。

 - 点击Button('change length')，length是被@Trace装饰的属性，它的变化可以触发关联的UI组件，即UINode (1)的刷新，并输出"id: 1 renderTimes: x"的日志，其中x根据点击次数依次增长。
 - 自定义组件Page中的son是常规变量，因此点击Button('assign Son')并不会观测到变化。
 - 当点击Button('assign Son')后，再点击Button('change length')并不会引起UI刷新。因为此时son的地址改变，其关联的UI组件并没有关联到最新的son。


```ArkTS
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0001;
const TAG = 'ArktsObservedV2AndTrace';

@ObservedV2
class Pencil {
  @Trace public length: number = 21; // 当length变化时，会刷新关联的组件
}

class Bag {
  public width: number = 50;
  public height: number = 60;
  public pencil: Pencil = new Pencil();
}

class Son {
  public age: number = 5;
  public school: string = 'some';
  public bag: Bag = new Bag();
}

@Entry
@ComponentV2
struct Page {
  son: Son = new Son();
  renderTimes: number = 0;

  isRender(id: number): number {
    hilog.info(DOMAIN, TAG, `id: ${id} renderTimes: ${this.renderTimes}`);
    this.renderTimes++;
    return 40;
  }

  build() {
    Column() {
      Text('pencil length' + this.son.bag.pencil.length)
        .fontSize(this.isRender(1)) // UINode (1)
        .margin(10)
      Button('change length')
        .width(300)
        .margin(10)
        .onClick(() => {
          // 点击更改length值，UINode（1）会刷新
          this.son.bag.pencil.length += 100;
        })
      Button('assign Son')
        .width(300)
        .margin(10)
        .onClick(() => {
          // 由于变量son非状态变量，因此无法刷新UINode（1）
          this.son = new Son();
        })
    }
    .width('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/pQOQIKzZT5ak3KjL8G5NBA/zh-cn_image_0000002674472060.gif?HW-CC-KV=V1&HW-CC-Date=20260813T095706Z&HW-CC-Expire=86400&HW-CC-Sign=DC2816C8C36443733478F0348EF39AA7733D272B10D66A4A00EFC33171B8930A)




#### 继承类场景

@Trace支持在类的继承场景中使用，无论是在基类还是继承类中，只有被@Trace装饰的属性才具有被观测变化的能力。

以下例子中，声明class GrandFather、Father、Uncle、Son、Cousin，继承关系如下图。


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/XvD6ZQP6SCK4fs6nCk0Bzw/zh-cn_image_0000002704392029.png?HW-CC-KV=V1&HW-CC-Date=20260813T095706Z&HW-CC-Expire=86400&HW-CC-Sign=8BF472FED1B665F0DE8F0B2FA388E95746E479E302338CBBD8E8D4DE0BBCC60E)


创建类Son和类Cousin的实例，点击Button('change Son age')和Button('change Cousin age')可以触发UI的刷新。

```ArkTS
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0001;
const TAG = 'ArktsObservedV2AndTrace';

@ObservedV2
class GrandFather {
  // 被@Trace装饰的属性具有被观测变化的能力
  @Trace public age: number = 0;

  constructor(age: number) {
    this.age = age;
  }
}

class Father extends GrandFather {
  constructor(father: number) {
    super(father);
  }
}

class Uncle extends GrandFather {
  constructor(uncle: number) {
    super(uncle);
  }
}

class Son extends Father {
  constructor(son: number) {
    super(son);
  }
}

class Cousin extends Uncle {
  constructor(cousin: number) {
    super(cousin);
  }
}

@Entry
@ComponentV2
struct Index {
  son: Son = new Son(0);
  cousin: Cousin = new Cousin(0);
  renderTimes: number = 0;

  isRender(id: number): number {
    hilog.info(DOMAIN, TAG, `id: ${id} renderTimes: ${this.renderTimes}`);
    this.renderTimes++;
    return 40;
  }

  build() {
    Row() {
      Column() {
        Text(`Son ${this.son.age}`)
          .fontSize(this.isRender(1))
          .fontWeight(FontWeight.Bold)
          .margin(10)
        Text(`Cousin ${this.cousin.age}`)
          .fontSize(this.isRender(2))
          .fontWeight(FontWeight.Bold)
          .margin(10)
        Button('change Son age')
          .width(300)
          .margin(10)
          .onClick(() => {
            this.son.age++;
          })
        Button('change Cousin age')
          .width(300)
          .margin(10)
          .onClick(() => {
            this.cousin.age++;
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/VZlhqI6yR92ktJ_2dC6-bQ/zh-cn_image_0000002674631906.gif?HW-CC-KV=V1&HW-CC-Date=20260813T095706Z&HW-CC-Expire=86400&HW-CC-Sign=EBE3A94C347D50181DEB11A457D9278DB3A33436191A243640B45E7078216888)




#### @Trace装饰基础类型的数组

@Trace装饰数组时，使用支持的API能够观测到变化。支持的API见[观察变化](#观察变化)。

在下面的示例中@ObservedV2装饰的Arr类中的属性numberArr是@Trace装饰的数组，当使用数组API操作numberArr时，可以观测到对应的变化。注意使用数组长度进行判断以防越界访问。

```ArkTS
let nextId: number = 0;

@ObservedV2
class Arr {
  public id: number = 0;
  @Trace public numberArr: number[] = [];

  constructor() {
    this.id = nextId++;
    this.numberArr = [0, 1, 2];
  }
}

@Entry
@ComponentV2
struct Index {
  arr: Arr = new Arr();

  build() {
    Column() {
      Text(`length: ${this.arr.numberArr.length}`)
        .fontSize(40)
        .margin(10)
      Divider()
      if (this.arr.numberArr.length >= 3) {
        Text(`${this.arr.numberArr[0]}`)
          .fontSize(40)
          .margin(10)
          .onClick(() => {
            this.arr.numberArr[0]++;
          })
        Text(`${this.arr.numberArr[1]}`)
          .fontSize(40)
          .margin(10)
          .onClick(() => {
            this.arr.numberArr[1]++;
          })
        Text(`${this.arr.numberArr[2]}`)
          .fontSize(40)
          .margin(10)
          .onClick(() => {
            this.arr.numberArr[2]++;
          })
      }

      Divider()

      ForEach(this.arr.numberArr, (item: number, index: number) => {
        Text(`${index} ${item}`)
          .fontSize(40)
          .margin(10)
      })

      // numberArr是@Trace装饰的数组
      // 使用数组API操作numberArr时，可以观测到对应的变化
      Button('push')
        .width(300)
        .margin(10)
        .onClick(() => {
          this.arr.numberArr.push(50);
        })

      Button('pop')
        .width(300)
        .margin(10)
        .onClick(() => {
          this.arr.numberArr.pop();
        })

      Button('shift')
        .width(300)
        .margin(10)
        .onClick(() => {
          this.arr.numberArr.shift();
        })

      Button('splice')
        .width(300)
        .margin(10)
        .onClick(() => {
          this.arr.numberArr.splice(1, 0, 60);
        })

      Button('unshift')
        .width(300)
        .margin(10)
        .onClick(() => {
          this.arr.numberArr.unshift(100);
        })

      Button('copywithin')
        .width(300)
        .margin(10)
        .onClick(() => {
          this.arr.numberArr.copyWithin(0, 1, 2);
        })

      Button('fill')
        .width(300)
        .margin(10)
        .onClick(() => {
          this.arr.numberArr.fill(0, 2, 4);
        })

      Button('reverse')
        .width(300)
        .margin(10)
        .onClick(() => {
          this.arr.numberArr.reverse();
        })

      Button('sort')
        .width(300)
        .margin(10)
        .onClick(() => {
          this.arr.numberArr.sort();
        })
    }
    .width('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/RbgSBz2PSgSucNXPTTppCg/zh-cn_image_0000002704271861.gif?HW-CC-KV=V1&HW-CC-Date=20260813T095706Z&HW-CC-Expire=86400&HW-CC-Sign=2CB02CF8F31B0DBB5F15DB19E443C8241C8F12845598855A35A024F88734DF75)




#### @Trace装饰对象数组

 - @Trace装饰对象数组personList以及Person类中的age属性，因此当personList、age改变时均可以观测到变化。
 - 点击Text组件更改age时，Text组件会刷新。


```ArkTS
let nextId: number = 0;

@ObservedV2
class Person {
  // @Trace装饰Person类中的age属性，使age可以被观测
  @Trace public age: number = 0;

  constructor(age: number) {
    this.age = age;
  }
}

@ObservedV2
class Info {
  public id: number = 0;
  @Trace public personList: Person[] = [];

  constructor() {
    this.id = nextId++;
    this.personList = [new Person(0), new Person(1), new Person(2)];
  }
}

@Entry
@ComponentV2
struct Index {
  info: Info = new Info();

  build() {
    Column() {
      Text(`length: ${this.info.personList.length}`)
        .fontSize(40)
        .margin(10)
      Divider()
      if (this.info.personList.length >= 3) {
        Text(`${this.info.personList[0].age}`)
          .fontSize(40)
          .margin(10)
          .onClick(() => {
            this.info.personList[0].age++;
          })

        Text(`${this.info.personList[1].age}`)
          .fontSize(40)
          .margin(10)
          .onClick(() => {
            this.info.personList[1].age++;
          })

        Text(`${this.info.personList[2].age}`)
          .fontSize(40)
          .margin(10)
          .onClick(() => {
            this.info.personList[2].age++;
          })
      }

      Divider()

      ForEach(this.info.personList, (item: Person, index: number) => {
        Text(`${index} ${item.age}`)
          .fontSize(40)
          .margin(10)
      })
    }
    .width('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/t3rUtHxHQemk0n53-pRO6A/zh-cn_image_0000002674472062.gif?HW-CC-KV=V1&HW-CC-Date=20260813T095706Z&HW-CC-Expire=86400&HW-CC-Sign=9D746B0104CEAF65D1ED4750302B1608E23CB92FF111C587FBA864724AA1EC89)




#### @Trace装饰Map类型

 - 被@Trace装饰的Map类型属性可以观测到调用API带来的变化，包括 set、clear、delete。
 - 因为Info类被@ObservedV2装饰且属性memberMap被@Trace装饰，点击Button('init map')对memberMap赋值也可以观测到变化。


```ArkTS
@ObservedV2
class Info {
  @Trace public memberMap: Map<number, string> = new Map([[0, 'a'], [1, 'b'], [3, 'c']]);
}

@Entry
@ComponentV2
struct MapSample {
  info: Info = new Info();

  build() {
    Row() {
      Column() {
        ForEach(Array.from(this.info.memberMap.entries()), (item: [number, string]) => {
          Text(`${item[0]}`)
            .fontSize(30)
            .margin(10)
          Text(`${item[1]}`)
            .fontSize(30)
            .margin(10)
          Divider()
        })
        // 被@Trace装饰的Map类型属性可以观测到调用API带来的变化
        Button('init map')
          .width(300)
          .margin(10)
          .onClick(() => {
            this.info.memberMap = new Map([[0, 'a'], [1, 'b'], [3, 'c']]);
          })
        Button('set new one')
          .width(300)
          .margin(10)
          .onClick(() => {
            this.info.memberMap.set(4, 'd');
          })
        Button('clear')
          .width(300)
          .margin(10)
          .onClick(() => {
            this.info.memberMap.clear();
          })
        Button('set the key: 0')
          .width(300)
          .margin(10)
          .onClick(() => {
            this.info.memberMap.set(0, 'aa');
          })
        Button('delete the first one')
          .width(300)
          .margin(10)
          .onClick(() => {
            this.info.memberMap.delete(0);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/cc9r_5fgTIeoZK6SArLvhQ/zh-cn_image_0000002704392031.gif?HW-CC-KV=V1&HW-CC-Date=20260813T095706Z&HW-CC-Expire=86400&HW-CC-Sign=7793F39334FF4D95D18FEB8F5DC8D5C2BB33B87324C8C11346B8E630C7AD945F)




#### @Trace装饰Set类型

 - 被@Trace装饰的Set类型属性可以观测到调用API带来的变化，包括 add、clear和delete。
 - 因为Info类被@ObservedV2装饰且属性memberSet被@Trace装饰，点击Button('init set')对memberSet赋值也可以观测到变化。


```ArkTS
@ObservedV2
class Info {
  @Trace public memberSet: Set<number> = new Set([0, 1, 2, 3, 4]);
}

@Entry
@ComponentV2
struct SetSample {
  info: Info = new Info();

  build() {
    Row() {
      Column() {
        ForEach(Array.from(this.info.memberSet.entries()), (item: [number, number]) => {
          Text(`${item[0]}`)
            .fontSize(30)
            .margin(10)
          Divider()
        })
        // 被@Trace装饰的Set类型属性可以观测到调用API带来的变化
        Button('init set')
          .width(300)
          .margin(10)
          .onClick(() => {
            this.info.memberSet = new Set([0, 1, 2, 3, 4]);
          })
        Button('set new one')
          .width(300)
          .margin(10)
          .onClick(() => {
            this.info.memberSet.add(5);
          })
        Button('clear')
          .width(300)
          .margin(10)
          .onClick(() => {
            this.info.memberSet.clear();
          })
        Button('delete the first one')
          .width(300)
          .margin(10)
          .onClick(() => {
            this.info.memberSet.delete(0);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/YNYqqQuUTrWlBhKhLb0_3A/zh-cn_image_0000002674631908.gif?HW-CC-KV=V1&HW-CC-Date=20260813T095706Z&HW-CC-Expire=86400&HW-CC-Sign=577D40235EFAAF3806AB565E2281A0CB2ED65A514D160BE17454A1AB9A354987)




#### @Trace装饰Date类型

 - @Trace装饰的Date类型属性可以观测调用API带来的变化，包括 setFullYear、setMonth、setDate、setHours、setMinutes、setSeconds、setMilliseconds、setTime、setUTCFullYear、setUTCMonth、setUTCDate、setUTCHours、setUTCMinutes、setUTCSeconds、setUTCMilliseconds。
 - 因为Info类被@ObservedV2装饰且属性selectedDate被@Trace装饰，点击Button('set selectedDate to 2023-07-08')对selectedDate赋值也可以观测到变化。


```ArkTS
@ObservedV2
class Info {
  @Trace public selectedDate: Date = new Date('2021-08-08');
}

@Entry
@ComponentV2
struct DateSample {
  info: Info = new Info();

  build() {
    Column() {
      // @Trace装饰的Date类型属性可以观测调用API带来的变化
      Button('set selectedDate to 2023-07-08')
        .width(300)
        .margin(10)
        .onClick(() => {
          this.info.selectedDate = new Date('2023-07-08');
        })
      Button('increase the year by 1')
        .width(300)
        .margin(10)
        .onClick(() => {
          this.info.selectedDate.setFullYear(this.info.selectedDate.getFullYear() + 1);
        })
      Button('increase the month by 1')
        .width(300)
        .margin(10)
        .onClick(() => {
          this.info.selectedDate.setMonth(this.info.selectedDate.getMonth() + 1);
        })
      Button('increase the day by 1')
        .width(300)
        .margin(10)
        .onClick(() => {
          this.info.selectedDate.setDate(this.info.selectedDate.getDate() + 1);
        })
      DatePicker({
        start: new Date('1970-1-1'),
        end: new Date('2100-1-1'),
        selected: this.info.selectedDate
      })
    }
    .width('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/zYnZKw0rRsWjLYDnM-j8Dw/zh-cn_image_0000002704271863.gif?HW-CC-KV=V1&HW-CC-Date=20260813T095706Z&HW-CC-Expire=86400&HW-CC-Sign=F1A250BB02A0A8475A40A2FB13E3D4E86BBD9114A97E1DF22AF86BB60F5E2B75)




#### 常见问题



#### @ObservedV2装饰对象的序列化与反序列化

@ObservedV2装饰的对象序列化后会为@Trace装饰的属性添加__ob_前缀。

```json
@ObservedV2
class Info {
  @Trace name: string = 'Tom';
  @Trace age: number = 24;
}

let realInfo: Info = new Info();
let jsonResult: string = JSON.stringify(realInfo); // '{"__ob_name":"Tom","__ob_age":24}'
```

将@ObservedV2装饰的对象通过JSON.stringify序列化后，再通过JSON.parse反序列化，将失去观察能力。

```json
@ObservedV2
class Info {
  @Trace name: string = 'Tom';
  @Trace age: number = 24;
}

let realInfo: Info = new Info();
let jsonResult: string = JSON.stringify(realInfo); // '{"__ob_name":"Tom","__ob_age":24}'
let parseInfo: Info = JSON.parse(jsonResult);

// 与直接通过new操作符创建的对象不同，JSON.parse获得的对象实际并不是Info的实例，所以无属性观察能力
let isInfoByNew: boolean = realInfo instanceof Info; // true
let isInfoByParse: boolean = parseInfo instanceof Info; // false
```

可以配合三方库[class-transformer](https://gitcode.com/CPF-ApplicationTPC/openharmony_tpc_samples/tree/master/class-transformer)实现反序列化后可观察。

class-transformer可以通过如下命令安装。

```text
ohpm install class-transformer
```

```json
import { plainToInstance } from 'class-transformer'; // 导入三方库
@ObservedV2
class Info {
  @Trace name: string = 'Tom';
  @Trace age: number = 24;
}
let realInfo: Info = new Info();
let jsonResult: string = JSON.stringify(realInfo); // '{"__ob_name":"Tom","__ob_age":24}'
let parseInfo: Info = JSON.parse(jsonResult);

let transformedInfo: Info = plainToInstance(Info, parseInfo);
let isInfoByTransformed: boolean = transformedInfo instanceof Info; // true
```

若为多层对象嵌套场景，需要进行额外处理，包括：

 - 去除序列化结果中的__ob_前缀，否则内层对象无法被正确转换。
 - 使用class-transformer库中提供的@Type装饰器（为与状态管理V2的[@Type装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-type)区分，示例中重命名为TypeFromLibrary）标记里层对象的类型。


使用三方库的@Type装饰器需要安装[reflect-metadata](https://gitcode.com/CPF-ApplicationTPC/openharmony_tpc_samples/tree/master/reflect-metadata)。

reflect-metadata可以通过如下命令安装。

```text
ohpm install reflect-metadata@0.2.1
```

```json
import { plainToInstance, Type as TypeFromLibrary} from 'class-transformer'; // 导入三方库
import 'reflect-metadata'; // 三方库的@Type装饰器需要使用
@ObservedV2
class Info {
  @Trace name: string = 'Tom';
  @Trace age: number = 24;
}
@ObservedV2
class InfoWrapper {
  // 使用三方库的@Type装饰器（重命名为TypeFromLibrary）标记内层属性的类型
  @TypeFromLibrary(() => Info)
  @Trace info: Info = new Info();
}
let realWrapper: InfoWrapper = new InfoWrapper();
let infoWrapperJson: string = JSON.stringify(realWrapper); // '{"__ob_info":{"__ob_name":"Tom","__ob_age":24}}'
// 去除属性key的'__ob_'前缀，此处仅做演示，开发者需根据实际类型定义情况完成去除key中的'__ob_'前缀
let jsonHandled = infoWrapperJson.replaceAll('__ob_', ''); // '{"info":{"name":"Tom","age":24}}'
let wrapperHandled = plainToInstance(InfoWrapper, JSON.parse(jsonHandled));

let isWrapper: boolean = wrapperHandled instanceof InfoWrapper; // true
let isInfo: boolean = (wrapperHandled.info) instanceof Info; // true
```

在UI中使用的完整示例如下。

```ArkTS
import { plainToInstance, Type as TypeFromLibrary } from 'class-transformer'; // 导入三方库
import 'reflect-metadata'; // 三方库的@Type装饰器需要使用

// 模拟json键值对对象
let testJSON: Record<string, ESObject> = {
  'id': 1,
  'info': {
    'name': 'Tom',
    'age': 24
  },
  'friends': [
    {
      'name': 'John',
      'age': 23
    },
    {
      'name': 'Mary',
      'age': 24
    }
  ]
}

@ObservedV2
class Info {
  @Trace public name?: string;
  @Trace public age?: number;
}

@ObservedV2
class Person {
  public id?: number;
  // 使用三方库的@Type装饰器（重命名为TypeFromLibrary）标记内层属性的类型
  @TypeFromLibrary(() => Info)
  @Trace public info?: Info;
  // 使用三方库的@Type装饰器（重命名为TypeFromLibrary）标记内层属性的类型
  @TypeFromLibrary(() => Info)
  @Trace public friends?: Info[];
}

@Entry
@ComponentV2
struct SerializationAndDeserialization {
  @Local person: Person | undefined = undefined;
  aboutToAppear(): void {
    this.person = plainToInstance(Person, testJSON); // 直接将对象通过plainToInstance转为Person实例
  }

  build() {
    Column() {
      Text(`name: ${this.person?.info?.name}, age: ${this.person?.info?.age}`)
        .fontSize(20)
        .margin(10)
        .onClick(() => {
          if (this.person?.info?.age) {
            this.person!.info!.age++; // 修改可观察
          }
        })
      ForEach(this.person?.friends, (item: Info) => {
        Text(`friend name: ${item.name}, age: ${item.age}`)
          .fontSize(20)
          .margin(10)
          .onClick(() => {
            if (item.age) {
              item.age++; // 修改可观察
            }
          })
      })

      Button('Refresh Info')
        .width(300)
        .margin(10)
        .onClick(() => {
          let json: string =
            `{
              "id":12,
                "__ob_info":
                  {
                    "__ob_name":"Jimmy",
                    "__ob_age":35
                   },
              "__ob_friends":[
                {
                  "__ob_name":"Bob",
                  "__ob_age":30
                },
                {
                  "__ob_name":"Kevin",
                  "__ob_age":33
                }
              ]
            }`;
          // 去除'__ob_'前缀后通过JSON.parse与plainToInstance将json字符串转化成Person对象
          this.person = plainToInstance(Person, JSON.parse(json.replaceAll('__ob_', '')));
        })
    }
    .width('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/s-l6MK0IQ5mY6lMdF6WI7A/zh-cn_image_0000002674472064.gif?HW-CC-KV=V1&HW-CC-Date=20260813T095706Z&HW-CC-Expire=86400&HW-CC-Sign=18EDFC059610BA89BBAE22658375D20930048B549D59B98026E0019770A66AAD)




#### router传递的@ObservedV2类型显示异常

用router传递的@ObservedV2类，由于经过序列化生成的属性名称与类中的原始属性名称不一致，不能直接通过as类型转换成@ObservedV2的实例，需要反序列化重新生成@ObservedV2实例。反序列化相关内容请参考[@ObservedV2装饰对象的序列化与反序列化](#observedv2装饰对象的序列化与反序列化)。

【反例】

```ArkTS
// 文件pages/faqs/RouterIndex.ets内容

@ObservedV2
export class RouterModel {
  @Trace id: number = -1;
  @Trace info: string = 'default';
}

@Entry
@ComponentV2
struct RouterIndex {
  @Local paramsInfo: RouterModel = new RouterModel();
  onJumpClick(): void {
    this.paramsInfo.id = 0;
    this.paramsInfo.info = 'RouterModel';
    this.getUIContext().getRouter().pushUrl({
      url: 'pages/faqs/ChildPage',
      params: this.paramsInfo // 传递@ObservedV2实例到子页面
    }, (err) => {
      if (err) {
        console.error(`Invoke pushUrl failed, code is ${err.code}, message is ${err.message}`);
        return;
      }
      console.info('Invoke pushUrl succeeded.');
    })
  }

  build() {
    Column() {
      Text('Parent page')
        .fontSize(20)
        .margin(10)
      Button('Jump')
        .width(300)
        .margin(10)
        .onClick(() => {
          this.onJumpClick();
        })
    }
    .width('100%')
  }
}
```

```ArkTS
// 文件pages/faqs/ChildPage.ets内容

import { RouterModel } from './RouterIndex';

@Entry
@ComponentV2
struct Detail {
  @Local params?: RouterModel
  aboutToAppear(): void {
    // 错误使用方式！@ObservedV2类型通过router传递无法直接类型转换
    this.params = this.getUIContext().getRouter().getParams() as RouterModel;
  }
  build() {
    Column() {
      Text(`Detail Page: ${this.params?.id} ${this.params?.info}`) // 由于传递数据失败，这里会显示undefined
        .fontSize(20)
        .margin(10)
    }
    .width('100%')
  }
}
```

【正例】

```ArkTS
@ObservedV2
export class RouterModel {
  @Trace public id: number = -1;
  @Trace public info: string = 'default';
}

@Entry
@ComponentV2
struct RouterIndex {
  @Local paramsInfo: RouterModel = new RouterModel();
  onJumpClick(): void {
    this.paramsInfo.id = 0;
    this.paramsInfo.info = 'RouterModel';
    this.getUIContext().getRouter().pushUrl({
      url: 'pages/faqs/ChildPage',
      params: this.paramsInfo // 传递@ObservedV2实例到子页面
    }, (err) => {
      if (err) {
        console.error(`Invoke pushUrl failed, code is ${err.code}, message is ${err.message}`);
        return;
      }
      console.info('Invoke pushUrl succeeded.');
    })
  }

  build() {
    Column() {
      Text('Parent page')
        .fontSize(20)
        .margin(10)
      Button('Jump')
        .width(300)
        .margin(10)
        .onClick(() => {
          this.onJumpClick();
        })
    }
    .width('100%')
  }
}
```

```ArkTS
import { RouterModel } from './RouterIndex';
import { plainToInstance } from 'class-transformer'; // 导入三方库

@Entry
@ComponentV2
struct Detail {
  @Local params?: RouterModel
  aboutToAppear(): void {
    this.params =
      plainToInstance(RouterModel, JSON.parse(JSON.stringify(this.getUIContext().getRouter().getParams())));
  }
  build() {
    Column() {
      Text(`Detail Page: ${this.params?.id} ${this.params?.info}`)
        .fontSize(20)
        .margin(10)
    }
    .width('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/XAorVRYKSqGhNnZQ6jZh2A/zh-cn_image_0000002704392033.gif?HW-CC-KV=V1&HW-CC-Date=20260813T095706Z&HW-CC-Expire=86400&HW-CC-Sign=63E7BF1230B0A3FB70C789F176E2C45509801EEF3008885D077046FD1824DFDC)
