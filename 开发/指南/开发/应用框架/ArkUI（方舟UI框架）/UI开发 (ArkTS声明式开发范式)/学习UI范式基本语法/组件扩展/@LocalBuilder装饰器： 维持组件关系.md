# @LocalBuilder装饰器： 维持组件关系

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-localbuilder

当开发者使用局部@Builder进行引用数据传递时，需要考虑组件的父子关系。然而在使用.bind(this)的方式更改函数调用上下文后，会出现组件的父子关系与状态管理的父子关系不一致的问题。为了解决这一问题，引入[@LocalBuilder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-localbuilder#localbuilder)装饰器。@LocalBuilder拥有和局部@Builder相同的功能，且比局部@Builder能够更好的确定组件的父子关系和状态管理的父子关系。

在阅读本文档前，建议提前阅读：[@Builder](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builder)。

> [!NOTE]
> 从API version 12开始支持。 从API version 12开始，该装饰器支持在ArkTS卡片中使用。 从API version 12开始，该装饰器支持在元服务中使用。



#### 装饰器使用说明



#### 自定义组件内自定义构建函数

定义的语法：

```ArkTS
@LocalBuilder
myBuilderFunction() {
  // ···
}
```

使用方法：

```ArkTS
this.myBuilderFunction()
```

 - 允许在自定义组件内定义一个或多个@LocalBuilder函数，该函数被视为是该组件的私有、特殊类型的成员函数。
 - 自定义构建函数可以在所属组件的build函数和其他自定义构建函数中调用，但不允许在组件外调用。
 - 在自定义函数体中，this指代当前所属组件，组件的状态变量可以在自定义构建函数内访问。建议通过this访问自定义组件的状态变量而不是参数传递。




#### @LocalBuilder和局部@Builder使用区别

跨组件传递局部@Builder函数时，会使用.bind(this)更改函数上下文，但这可能会导致组件的父子关系与状态管理的父子关系不一致。而@LocalBuilder无论是否使用.bind(this)，都不会改变组件的父子关系，即@LocalBuilder中定义组件所属的父组件是确定的，无法被改变。


![](assets/@LocalBuilder装饰器：%20维持组件关系/file-20260514130509123-1.gif)


> [!NOTE]
> bind()方法创建一个新的函数，称为绑定函数，当调用者绑定bind()时，该绑定函数会以创建时传入的第一个this作为原函数的this。


下方用例中，当函数componentBuilder被@Builder修饰时，显示效果为“Child”；当函数componentBuilder被@LocalBuilder修饰时，显示效果是“Parent”。

```ArkTS
@Component
struct Child {
  label: string = 'Child';
  @BuilderParam customBuilderParam: () => void;

  build() {
    Column() {
      this.customBuilderParam()
    }
    .width('100%')
  }
}

@Entry
@Component
struct Parent {
  label: string = 'Parent';

  @Builder
  componentBuilder() {
    Text(`${this.label}`) // @Builder内的this指向实际调用点的组件，在这个用例中因为调用点在Child组件内，所以this实际指向Child组件
      .fontSize(20)
      .margin(10)
  }

  @LocalBuilder
  componentLocalBuilder() {
    Text(`${this.label}`) // @LocalBuilder内的this指向声明@LocalBuilder函数Parent组件
      .fontSize(20)
      .margin(10)
  }

  build() {
    Column() {
      Child({ customBuilderParam: this.componentBuilder }) // Child组件内调用customBuilderParam显示字符串Child。
      Child({ customBuilderParam: this.componentLocalBuilder }) // 传递函数本身写法，Child组件内调用customBuilderParam显示字符串Parent。
      Child({
        customBuilderParam: () => {
          this.componentLocalBuilder()
        }
      }) // () => { 函数调用 }写法，Child组件内调用customBuilderParam显示字符串Parent。
    }
    .width('100%')
  }
}
```


![](assets/@LocalBuilder装饰器：%20维持组件关系/file-20260514130509123-3.png)




#### 限制条件

 - @LocalBuilder只能在所属组件内声明，不允许全局声明。
 - @LocalBuilder不能与内置装饰器或自定义装饰器一起使用。
 - 在自定义组件中，@LocalBuilder不能用来装饰静态函数。
 - 关于@LocalBuilder函数的传递方式，建议优先传递函数本身，或使用 () => { 函数调用 } 的形式，避免直接传递函数的执行结果。




#### 参数传递规则

@LocalBuilder函数的参数传递有[按回调传递](#按回调传递参数)，[按引用传递](#按引用传递参数)和[按值传递](#按值传递参数)，均需遵守以下规则：

 - 参数的类型必须与参数声明的类型一致，且不允许为undefined、null。
 - 在@LocalBuilder修饰的函数内部，不允许改变参数值。
 - @LocalBuilder内的UI语法遵循[UI语法规则](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-custom-components#build函数实现规则)。
 - 按回调传递和按引用传递时，支持@LocalBuilder函数内UI组件刷新。按引用传递只在传入一个参数且该参数直接传入对象字面量时生效，有多个参数时不支持@LocalBuilder函数内UI组件刷新。




#### 按回调传递参数

从API version 20开始，开发者可以通过使用UIUtils.makeBinding()函数、Binding类和MutableBinding类实现@Builder函数中状态变量的刷新。详情请参考[makeBinding](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-statemanagement#makebinding20)。

```ArkTS
import { UIUtils, Binding } from '@kit.ArkUI';

@Entry
@Component
struct Parent {
  @State variableValue: string = 'Hello World';

  @LocalBuilder
  citeLocalBuilder(params: Binding<string>) {
    Row() {
      Text(`UseStateVarByReference: ${params.value}`)
        .fontSize(20)
        .margin(10)
    }
  }

  build() {
    Column() {
      // 通过UIUtils.makeBinding()方法和Binding类，实现@LocalBuilder函数中状态变量的刷新
      this.citeLocalBuilder(UIUtils.makeBinding<string>(() => this.variableValue))
      Button('Click me')
        .width(300)
        .margin(10)
        .onClick(() => {
          this.variableValue = 'Hi World';
        })
    }
    .width('100%')
  }
}
```


![](assets/@LocalBuilder装饰器：%20维持组件关系/file-202607081039294d672d63.gif)




#### 按引用传递参数

按引用传递参数时，传递的参数可为状态变量，且状态变量的改变会引起@LocalBuilder函数内的UI刷新。

> [!NOTE]
> 若@LocalBuilder函数和$$参数一起使用，子组件调用父组件的@LocalBuilder函数，子组件传入的参数发生变化，不会引起@LocalBuilder函数内的UI刷新。见常见错误 @LocalBuilder函数和$$参数一起使用UI不刷新 。


组件Parent内的@LocalBuilder函数在build函数内调用，按键值对写法进行传值，当点击Click me时，@LocalBuilder内的Text文本内容会随着状态变量内容的改变而改变。

```ArkTS
class ReferenceType {
  paramString: string = '';
}

@Entry
@Component
struct Parent {
  @State variableValue: string = 'Hello World';

  @LocalBuilder
  citeLocalBuilder(params: ReferenceType) {
    Row() {
      Text(`UseStateVarByReference: ${params.paramString}`)
        .fontSize(20)
        .margin(10)
    }
  };

  build() {
    Column() {
      // 按键值对写法进行传值，传入的参数发生变化，会引起citeLocalBuilder内的UI刷新
      this.citeLocalBuilder({ paramString: this.variableValue })
      Button('Click me')
        .width(300)
        .margin(10)
        .onClick(() => {
          this.variableValue = 'Hi World';
        })
    }
    .width('100%')
  }
}
```


![](assets/@LocalBuilder装饰器：%20维持组件关系/file-2026070810392987c36db6.png)


按引用传递参数时，如果在@LocalBuilder函数内调用自定义组件，ArkUI提供$$作为按引用传递参数的范式。

组件Parent内的@LocalBuilder函数内调用自定义组件，且按照引用传递参数将值传递到自定义组件，当Parent组件内状态变量值发生变化时，@LocalBuilder函数内的自定义组件HelloComponent的message值也会随之更新。

```ArkTS
class ReferenceType {
  paramString: string = '';
}

@Component
struct HelloComponent {
  @Prop message: string;

  build() {
    Row() {
      Text(`HelloComponent===${this.message}`)
        .fontSize(20)
        .margin(10)
    }
  }
}

@Entry
@Component
struct Parent {
  @State variableValue: string = 'Hello World';

  @LocalBuilder
  citeLocalBuilder($$: ReferenceType) {
    Row() {
      Column() {
        Text(`citeLocalBuilder===${$$.paramString}`)
          .fontSize(20)
          .margin(10)
        HelloComponent({ message: $$.paramString })
      }
      .width('100%')
    }
  }

  build() {
    Column() {
      // 按引用传递参数，传入的参数发生变化，会引起citeLocalBuilder内的UI刷新
      this.citeLocalBuilder({ paramString: this.variableValue })
      Button('Click me')
        .width(300)
        .margin(10)
        .onClick(() => {
          this.variableValue = 'Hi World';
        })
    }
    .width('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/5EooPHp9SSqYnLeWuTFUEg/zh-cn_image_0000002685925499.gif?HW-CC-KV=V1&HW-CC-Date=20260730T071838Z&HW-CC-Expire=86400&HW-CC-Sign=23E6758844DB517EE3A6FD55A66E4A4C4F8DA31343D6DD67F752D44269708D93)


当子组件引用父组件的@LocalBuilder函数并传入状态变量时，状态变量的改变不会触发@LocalBuilder函数内的UI刷新。这是因为调用@LocalBuilder装饰的函数创建出来的组件绑定于父组件，而状态变量的刷新机制仅作用于当前组件及其子组件，对父组件无效。而使用@Builder修饰函数可触发UI刷新，原因在于@Builder改变了函数的this指向，使创建出来的组件绑定到子组件上，从而在子组件修改变量能够实现@Builder中的UI刷新。

下面示例中，组件Child将状态变量传递到Parent的@Builder和@LocalBuilder函数内。在@Builder函数内，this指向Child，参数变化能触发UI刷新。在@LocalBuilder函数内，this指向Parent，参数变化不会触发UI刷新。若@LocalBuilder函数内引用Parent的状态变量发生变化，UI能正常刷新。

```ArkTS
class Data {
  public size: number = 0;
}

@Entry
@Component
struct Parent {
  label: string = 'parent';
  @State data: Data = new Data();

  @Builder
  componentBuilder($$: Data) {
    // 点击Button 触发UI刷新
    Text('builder + $$')
      .fontSize(20)
      .margin(10)
    Text(`${'this -> ' + this.label}`)
      .fontSize(20)
      .margin(10)
    Text(`${'size : ' + $$.size}`)
      .fontSize(20)
      .margin(10)
  }

  @LocalBuilder
  componentLocalBuilder($$: Data) {
    // 点击Button 不会触发UI刷新
    Text('LocalBuilder + $$ data')
      .fontSize(20)
      .margin(10)
    Text(`${'this -> ' + this.label}`)
      .fontSize(20)
      .margin(10)
    Text(`${'size : ' + $$.size}`)
      .fontSize(20)
      .margin(10)
  }

  @LocalBuilder
  contentLocalBuilderNoArgument() {
    // 点击Button 触发UI刷新
    Text('LocalBuilder + local data')
      .fontSize(20)
      .margin(10)
    Text(`${'this -> ' + this.label}`)
      .fontSize(20)
      .margin(10)
    Text(`${'size : ' + this.data.size}`)
      .fontSize(20)
      .margin(10)
  }

  build() {
    Column() {
      Child({
        contentBuilder: this.componentBuilder,
        contentLocalBuilder: this.componentLocalBuilder,
        contentLocalBuilderNoArgument: this.contentLocalBuilderNoArgument,
        data: this.data
      })
    }
    .width('100%')
  }
}

@Component
struct Child {
  label: string = 'child';

  @Builder
  customBuilder() {
  };

  @BuilderParam contentBuilder: ((data: Data) => void) = this.customBuilder;
  @BuilderParam contentLocalBuilder: ((data: Data) => void) = this.customBuilder;
  @BuilderParam contentLocalBuilderNoArgument: (() => void) = this.customBuilder;
  @Link data: Data;

  build() {
    Column() {
      this.contentBuilder({ size: this.data.size })
      this.contentLocalBuilder({ size: this.data.size })
      this.contentLocalBuilderNoArgument()
      Button('add child size')
        .width(300)
        .margin(10)
        .onClick(() => {
          this.data.size += 1;
        })
    }
    .width('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/Z9MZFxqnSGyeIA_wUA7ZUQ/zh-cn_image_0000002656005820.gif?HW-CC-KV=V1&HW-CC-Date=20260730T071838Z&HW-CC-Expire=86400&HW-CC-Sign=2D6AB476C6A0BE2A22AB3620B7F1CAFAC363C62E25D5502D6F4E9E095809340B)




#### 按值传递参数

调用@LocalBuilder装饰的函数默认按值传递。当传递的参数为状态变量时，状态变量的改变不会引起@LocalBuilder函数内的UI刷新。所以当使用状态变量的时候，推荐使用[按回调传递](#按回调传递参数)或[按引用传递](#按引用传递参数)。

组件Parent将@State修饰的label值按照函数传参方式传递到@LocalBuilder函数内，此时@LocalBuilder函数获取到的值为普通变量值，所以改变@State修饰的label值时，@LocalBuilder函数内的值不会发生改变。

```ArkTS
@Entry
@Component
struct Parent {
  @State label: string = 'Hello';

  @LocalBuilder
  citeLocalBuilder(paramA1: string) {
    Row() {
      Text(`UseStateVarByValue: ${paramA1}`)
        .fontSize(20)
        .margin(10)
    }
    .height('100%')
  }

  build() {
    Column() {
      // 按值传递参数
      // 改变@State修饰的label值时，@LocalBuilder函数内的值不会发生改变
      this.citeLocalBuilder(this.label)
    }
    .width('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/ircy4ygoQRCBWzOth0lYUg/zh-cn_image_0000002655845900.png?HW-CC-KV=V1&HW-CC-Date=20260730T071838Z&HW-CC-Expire=86400&HW-CC-Sign=AD7FF77926C0E691C42629FD3101AED095501B03443D293665D8DEC59D9ED2FA)




#### 使用场景



#### @LocalBuilder在@ComponentV2修饰的自定义组件中使用

在[@ComponentV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-custom-components#componentv2)装饰的自定义组件中使用局部的@LocalBuilder，修改变量时会触发UI刷新。

```ArkTS
@ObservedV2
class Info {
  @Trace name: string = '';
  @Trace age: number = 0;
}

@ComponentV2
struct ChildPage {
  @Require @Param childInfo: Info;

  build() {
    Column() {
      Text(`Custom component name: ${this.childInfo.name}`)
        .fontSize(20)
        .fontWeight(FontWeight.Bold)
      Text(`Custom component age: ${this.childInfo.age}`)
        .fontSize(20)
        .fontWeight(FontWeight.Bold)
    }
    .margin(20)
  }
}

@Entry
@ComponentV2
struct ParentPage {
  info1: Info = { name: 'Tom', age: 25 };
  @Local info2: Info = { name: 'Tom', age: 25 };

  @LocalBuilder
  privateBuilder() {
    Column() {
      Text(`Local @LocalBuilder name: ${this.info1.name}`)
        .fontSize(20)
        .fontWeight(FontWeight.Bold)
      Text(`Local @LocalBuilder age: ${this.info1.age}`)
        .fontSize(20)
        .fontWeight(FontWeight.Bold)
    }
    .margin(20)
  }

  @LocalBuilder
  privateBuilderSecond() {
    Column() {
      Text(`Local @LocalBuilder name: ${this.info2.name}`)
        .fontSize(20)
        .fontWeight(FontWeight.Bold)
      Text(`Local @LocalBuilder age: ${this.info2.age}`)
        .fontSize(20)
        .fontWeight(FontWeight.Bold)
    }
    .margin(20)
  }

  build() {
    Column() {
      Text(`info1: ${this.info1.name}  ${this.info1.age}`) // Text1
        .fontSize(30)
        .fontWeight(FontWeight.Bold)
      this.privateBuilder() // 调用局部@LocalBuilder
      Text(`info2: ${this.info2.name}  ${this.info2.age}`) // Text2
        .fontSize(30)
        .fontWeight(FontWeight.Bold)
      this.privateBuilderSecond() // 调用局部@LocalBuilder
      Text(`info1: ${this.info1.name}  ${this.info1.age}`) // Text1
        .fontSize(30)
        .fontWeight(FontWeight.Bold)
      ChildPage({ childInfo: this.info1 }) // 调用自定义组件
      Text(`info2: ${this.info2.name}  ${this.info2.age}`) // Text2
        .fontSize(30)
        .fontWeight(FontWeight.Bold)
      ChildPage({ childInfo: this.info2 }) // 调用自定义组件
      Button('change info1&info2')
        .onClick(() => {
          this.info1 = { name: 'Cat', age: 18 }; // Text1不会刷新，原因是info1没被装饰器装饰，无法监听到值的改变。
          this.info2 = { name: 'Cat', age: 18 }; // Text2会刷新，原因是info2有装饰器装饰，可以监听到值的改变。
        })
    }
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/fs3Km1PgT5-77bUeyzGDVw/zh-cn_image_0000002686085329.gif?HW-CC-KV=V1&HW-CC-Date=20260730T071838Z&HW-CC-Expire=86400&HW-CC-Sign=1CDC8CDAA56CE308BE9A557498AE5F82337F26DD8BCB045D4C5F28D327F5BB79)




#### 常见问题



#### @LocalBuilder函数和$$参数一起使用UI不刷新

若@LocalBuilder函数和$$参数一起使用，子组件调用父组件的@LocalBuilder函数，子组件传入的参数发生变化，不会引起@LocalBuilder函数内的UI刷新。

【反例】

```ArkTS
class LayoutSize {
  public size: number = 0;
}

@Entry
@Component
struct Parent {
  label: string = 'parent';
  @State layoutSize: LayoutSize = { size: 0 };

  @LocalBuilder
  componentBuilder($$: LayoutSize) {
    Text(`this: ${this.label}`)
    Text(`size: ${$$.size}`)
  }

  build() {
    Column() {
      Child({
        customBuilder: this.componentBuilder,
        layoutSize: this.layoutSize
      })
    }
  }
}

@Component
struct Child {
  label: string = 'child';
  @BuilderParam customBuilder: ((layoutSize: LayoutSize) => void);
  @Link layoutSize: LayoutSize;

  build() {
    Column() {
      this.customBuilder({ size: this.layoutSize.size }) // 子组件调用父组件的@LocalBuilder函数
      Button('add child size')
        .onClick(() => {
          this.layoutSize.size += 1; // 子组件传入的参数发生变化，不会引起@LocalBuilder函数内的UI刷新
        })
    }
  }
}
```

【正例】

在声明@LocalBuilder的组件下创建状态变量并在@LocalBuilder函数内访问，可以在状态变量变化时更新@LocalBuilder内的UI组件。

```ArkTS
class LayoutSize {
  public size: number = 0;
}

@Entry
@Component
struct Parent {
  label: string = 'parent';
  @State layoutSize: LayoutSize = { size: 0 };

  @LocalBuilder
  componentBuilder() {
    Text(`this: ${this.label}`)
    Text(`size: ${this.layoutSize.size}`)
  }

  build() {
    Column() {
      Child({
        customBuilder: this.componentBuilder,
        layoutSize: this.layoutSize
      })
    }
  }
}

@Component
struct Child {
  label: string = 'child';
  @BuilderParam customBuilder: () => void;
  @Link layoutSize: LayoutSize;

  build() {
    Column() {
      this.customBuilder()
      Button('add child size')
        .onClick(() => {
          this.layoutSize.size += 1; // 子组件传入的参数发生变化，由@Link传入父组件@State，刷新父组件声明的@LocalBuilder函数的UI。
        })
    }
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/ujD2ljqbRrilmGDEdRiNzw/zh-cn_image_0000002685925501.gif?HW-CC-KV=V1&HW-CC-Date=20260730T071838Z&HW-CC-Expire=86400&HW-CC-Sign=52F90CBEE34E60114F0497D439511945AC3660563FDD1D309ABC538EC5B57E68)




#### @LocalBuilder函数在参数处直接调用出现布局错乱

@LocalBuilder装饰的函数作为参数时，直接传递函数的执行结果，会导致布局和预期效果有偏差。

【反例】

```ArkTS
@Entry
@Component
struct Page {
  @State message: string[] = ['1', '2', '3'];

  build() {
    List() {
      // 错误写法，直接传递itemFoot的执行结果。
      ListItemGroup({ space: 10, footer: this.itemFoot() }) {
        ForEach(this.message, (item: string, index: number) => {
          ListItem() {
            Stack() {
              Text(item)
                .fontSize(30)
            }
          }
        })
      }
    }
  }

  @LocalBuilder
  itemFoot() {
    Column() {
      Text('itemFoot')
        .fontSize(30)
    }
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/P_F43EDOQ3WmOF1vtoWwRg/zh-cn_image_0000002656005822.png?HW-CC-KV=V1&HW-CC-Date=20260730T071838Z&HW-CC-Expire=86400&HW-CC-Sign=E823D9B7887A0EC741E8E79BB5A0085EFF4F4315A1BB616EDF2EF6FF7F197945)


【正例】

@LocalBuilder装饰的函数作为参数时，使用 () => { 函数调用 } 的形式，布局能够符合预期效果。

```ArkTS
@Entry
@Component
struct Page {
  @State message: string[] = ['1', '2', '3'];

  build() {
    List() {
      // 正确写法，使用() => { 函数调用 }的形式。
      ListItemGroup({ space: 10, footer: () => { this.itemFoot() } }) {
        ForEach(this.message, (item: string, index: number) => {
          ListItem() {
            Stack() {
              Text(item)
                .fontSize(30)
            }
          }
        })
      }
    }
  }

  @LocalBuilder
  itemFoot() {
    Column() {
      Text('itemFoot')
        .fontSize(30)
    }
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/oVr2kce3Q1O7eXhV0nBunA/zh-cn_image_0000002655845902.png?HW-CC-KV=V1&HW-CC-Date=20260730T071838Z&HW-CC-Expire=86400&HW-CC-Sign=F4A635B1BFE0025EF70396038D230D29BDA64DBC7718F04B3710D26A801DFA69)
