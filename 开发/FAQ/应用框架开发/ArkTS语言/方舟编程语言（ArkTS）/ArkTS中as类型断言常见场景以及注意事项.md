# ArkTS中as类型断言常见场景以及注意事项

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-182

#### 问题现象

- **场景一：** 使用as类型断言不能转换JSON.parse()方法解析的JSON字符串中成员属性的数据类型。举例说明：
```json
<em>// </em><em>用ItemModel类接收responseData中JSON字符串的内容</em>
let responseData = `{"id":123,"name":"Example","price":200}` <em>// </em><em>在responseData中的price值为number类型的200</em>

class ItemModel {
  id?: number;
  name?: string;
  price?: string; <em>// 作为接收类的ItemModel中price类型为string</em>
}

<em>// </em><em>调用JSON.parse()解析JSON字符串，并用as得到ItemModel类型实例</em>
let item = JSON.parse(responseData) as ItemModel;

<em>// </em><em>此时得到item.price类型为number而非定义的string</em>
console.info(`typeofprice: ${typeof item.price}`); <em>// 输出为typeofprice:number</em>
```

- **场景二：** 使用params为options赋值，但是as number未生效，options接收到的依旧是带引号的string类型。
```text
private options: mapCommon.MapOptions = {
  position: {
    target: {
      latitude: 0,
      longitude: 0,
    },
    zoom: 15,
  }
};

let params: Record<string, Object> = {
  'latitude': '39.9',
  'longitude': '116.4'
}

this.options.position.target.latitude = lat;
this.options.position.target.longitude = lon;
```
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/pt7CoDK6SHipRttT98n8MA/zh-cn_image_0000002629058992.png?HW-CC-KV=V1&HW-CC-Date=20260701T041130Z&HW-CC-Expire=86400&HW-CC-Sign=50543E9EA657930482440D1F901AEB5D0285397BF725D9D4149EA8B28024AD52)

- **场景三：** 对对象类型使用类型断言，DevEco Studio静态检查报错Object literal must correspond to some explicitly declared class or interface (arkts-no-untyped-obj-literals) &lt;ArkTSCheck&gt;：
```text
interface Test {
  a: string;
  b: string;
}

const a = {
  a: 'aa',
  b: 'bb',
  c: 'cc'
} as Test
```


 
 

#### 背景知识

- 在ArkTS中，as关键字是类型断言的一种语法，它不会在运行时改变值的类型，只是在编译阶段告知编译器以特定类型来处理这个值；
- 参考官方文档[JSON.parse()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-json#jsonparse)的用法和[构造函数](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/introduction-to-arkts#构造函数)的使用。

 
 

#### 解决方案

- **场景一：**
方案一：可以为ItemModel类定义构造函数，在构造函数中实现类型转换。示例代码如下：
```json
import { JSON } from '@kit.ArkTS';
@Builder
export function solution1Builder() {
  solution1()
}
class ItemModel {
  id?: number;
  name?: string;
  price?: string;

 <em> // 这里定义构造函数，将输入的price转为string类型</em>
  constructor(id: number, name: string, price: number) {
    this.id = id;
    this.name = name;
    this.price = JSON.stringify(price);
  }
}

<em>// </em><em>获取JSON字符串数据</em>
let responseData = `{"id":123,"name":"Example","price":200}`;
let obj = JSON.parse(responseData);

@Component
struct solution1 {
  public message: string = 'Click to test';
<em>  // 用new调用构造函数，构造新的ItemModel</em>
  public item: ItemModel =
    new ItemModel((obj as object)?.['id'], (obj as object)?.['name'], (obj as object)?.['price']);

  build() {
    NavDestination() {
      RelativeContainer() {
        Text(this.message)
          .id('Click to test')
          .fontSize($r('app.float.page_text_font_size'))
          .fontWeight(FontWeight.Bold)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onClick(() => {
          <em>  // 使用模型数据</em>
            console.info(`Item ID:${this.item.id}`); <em>// 输出:Item ID:123</em>
            console.info(`Item Name:${this.item.name}`);<em> </em><em>// 输出:Item Name:Example</em>
            console.info(`Item Price:${this.item.price}`); <em>// </em><em>输出:Item Price:200</em>
            console.info(`typeof Price:${typeof this.item.price}`);<em> </em><em>// 验证输出typeof Price:string</em>
          });
      }
      .height('100%')
      .width('100%');
    };
  }
}
```


 
- 方案二：利用JSON.parse的reviver参数，手动转换key为price时value的类型。示例代码如下：
```text
<em>// </em><em>新建ts文件，写入类型转换逻辑</em>
<em>// entry/src/main/ets/pages/test.ts</em>
export function reviverFunc(key, value) :string {
  if (key === "price") {
    let num_price = String(value)
    return num_price;
  }
  return value;
}
```
 
```json
import { JSON } from '@kit.ArkTS';
import { reviverFunc } from './test';<em> </em><em>// 导入reviverFunc</em>

@Builder
export function solution2Builder() {
  solution2();
}

class ItemModel {
  id?: number;
  name?: string;
  price?: string;
}

<em>// </em><em>获取JSON字符串数据</em>
let responseData = `{"id":123,"name":"Example","price":200}`;

@Component
struct solution2 {
  public message: string = 'Click to test';
  <em>// 调用JSON.parse和reviverFunc参数，创建item实例</em>
  public item = JSON.parse(responseData, reviverFunc) as ItemModel;

  build() {
    NavDestination() {
      RelativeContainer() {
        Text(this.message)
          .id('Click to test')
          .fontSize($r('app.float.page_text_font_size'))
          .fontWeight(FontWeight.Bold)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onClick(() => {
         <em>   // 使用模型数据</em>
            console.info(`Item ID:${this.item.id}`); <em>// 输出:Item ID:123</em>
            console.info(`Item Name:${this.item.name}`); <em>// 输出:Item Name:Example</em>
            console.info(`Item Price:${this.item.price}`);<em> </em><em>// 输出:Item Price:200</em>
            console.info(`typeof Price:${typeof this.item.price}`);<em> </em><em>// 验证输出typeof Price:string</em>
          });
      }
      .height('100%')
      .width('100%');
    };
  }
}
```


 
 
- **场景二：**将params类型改为Record<string, number>或者将value值去掉引号（''），在ArkTS中，as关键字是类型断言的一种语法，它不会在运行时改变值的类型，只是在编译阶段告知编译器以特定类型来处理这个值。
- **场景三：**断言类型Test与被断言对象的类型不完全一致，阅读示例代码发现类型Test缺少了一个名为c的属性，在类型Test中增加该属性的声明即可。
