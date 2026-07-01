# 怎么获取被@ObservedV2观察的数据对应的原始数据

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-918

## 怎么获取被@ObservedV2观察的数据对应的原始数据
 


##### 问题现象

@ObservedV2装饰的对象中，被@Trace装饰的成员变量名前会被加上"__ob_"的前缀，怎样获取到原始的对象？
 
 

##### 背景知识

状态管理V2装饰器会为装饰的变量生成getter和setter方法，同时为原有变量名添加"__ob_"的前缀。出于性能考虑，getTarget接口不会对V2装饰器生成的前缀进行处理，因此向[getTarget](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-statemanagement#gettarget)接口传入[@ObservedV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-observedv2-and-trace)装饰的类对象实例时，返回的对象依旧为对象本身，且被@Trace装饰的属性名仍有"__ob_"前缀。
 
 

##### 解决方案

可以用状态管理V2对象初始化一个同结构的[状态管理V1的@Observed装饰器和@ObjectLink装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-observed-and-objectlink)对象，然后用getTarget接口获取V1对象的原始数据，这样获取的数据结构和V2对象的原始结构相同。详细步骤如下：
- 定义结构相同的V1、V2对象：
```text
@ObservedV2
class FormDataClassV2 {
  @Trace name: string = '';
  @Trace price: number = 0;
}

@Observed
class FormDataClassV1 {
  @Track name: string = '';
  @Track price: number = 0;

  constructor(v: FormDataClassV2) {
    this.name = v.name;
    this.price = v.price;
  }
}
```

- 用V2对象初始化V1对象：
```text
let dataV1: FormDataClassV1 = new FormDataClassV1(this.dataV2); // 用V2对象初始化V1对象
```

- 用getTarget接口获取原始数据：
```text
let rawV1 = UIUtils.getTarget(dataV1); // 用getTarget接口获取原始对象
```


 
 
完整示例参考如下：
 
```text
import { UIUtils } from '@kit.ArkUI';

@ObservedV2
class FormDataClassV2 {
  @Trace name: string = '';
  @Trace price: number = 0;
}

@Observed
class FormDataClassV1 {
  @Track name: string = '';
  @Track price: number = 0;

  constructor(v: FormDataClassV2) {
    this.name = v.name;
    this.price = v.price;
  }
}

@Entry
@ComponentV2
struct FormDataClassPage {
  @Local message: string = 'Hello World';
  @Local dataV2: FormDataClassV2 = new FormDataClassV2();

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          let dataV1: FormDataClassV1 = new FormDataClassV1(this.dataV2); // 用V2对象初始化V1对象
          let rawV1 = UIUtils.getTarget(dataV1); // 用getTarget接口获取原始对象
          console.info(JSON.stringify(rawV1)); // 此时打印的日志不带__ob_框架
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
 
 

##### 常见FAQ

Q：getTarget接口的使用场景有哪些？
 
A：getTarget可以获取代理对象的原始对象，修改原始对象数据，不会触发UI刷新。使用场景如下：
 
- 类型比较或者序列化场景，需要获取原始对象。
- 三方库集成场景，需要传原始对象数据。
- 大量修改数据场景，如数据排序等，对原始对象操作避免代理层性能开销。
