# 使用状态管理V2实现Navigation页面路由

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1658

#### 问题现象

Navigation结合V2状态管理如何实现页面跳转和传参？
 
 

#### 背景知识

- [Navigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation)：路由导航的根视图容器。
- [NavDestination](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination)：显示Navigation的内容区。
- [onReady](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#onready11)：当NavDestination即将构建子组件之前会触发此回调。
- [@Provider装饰器和@Consumer装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-provider-and-consumer)：提供了跨组件层级数据双向同步的能力。
- [AppStorageV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-appstoragev2)：提供应用级全局共享状态变量的能力，开发者可以通过connect绑定同一个key，进行跨ability的数据共享。

 
 

#### 解决方案

**方案一：通过onReady实现路由跳转。**
 
onReady可获取[NavDestinationContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#navdestinationcontext11)上下文信息，其中包括pathInfo和pathStack，可通过pathStack获取页面传递的数据。参考代码如下所示：
 
```text
@Entry
@ComponentV2
struct OnReadyPage {
  @Local pageInfos: NavPathStack = new NavPathStack();
  @Local params: string = '使用V2传递的参数';

  @Builder
  pageMap(name: string) {
    if (name === 'ChildPage') {
      OnReadyChildPage();
    }
  }

  build() {
    Navigation(this.pageInfos) {
      Column() {
        Button('跳转下一页面')
          .onClick(() => {
            this.pageInfos.pushPathByName('ChildPage', this.params, true);
          });
      }
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('100%');
    }
    .navDestination(this.pageMap);
  }
}

@ComponentV2
struct OnReadyChildPage {
  @Local pageInfos: NavPathStack = new NavPathStack();
  @Local params: string = '';

  build() {
    NavDestination() {
      Column({ space: 16 }) {
        Text(this.params)
          .fontSize(18)
          .fontColor('#000000');
        Button('返回')
          .onClick(() => {
            this.pageInfos.pop();
          });
      }
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('100%');
    }
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
      this.params = context.pathInfo.param as string;
    });
  }
}
```
 
 
**方案二：通过@Provider和Consumer实现路由跳转。**
 
在Navigation根容器中使用@Provide装饰器提供NavPathStack实例，在子页面中使用@Consume装饰器消费该实例，但会带来一定的耦合性。通过[getParamByIndex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#getparambyindex10)获取参数。参考代码如下所示：
 
```text
@Entry
@ComponentV2
struct ProviderPage {
  @Provider('pageInfos') pageInfos: NavPathStack = new NavPathStack();
  @Local params: string = '使用V2传递的参数';

  @Builder
  pageMap(name: string) {
    if (name === 'ChildPage') {
      ConsumerChildPage();
    }
  }

  build() {
    Navigation(this.pageInfos) {
      Column() {
        Button('跳转下一页面')
          .onClick(() => {
            this.pageInfos.pushPathByName('ChildPage', this.params, true);
          });
      }
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('100%');
    }
    .navDestination(this.pageMap);
  }
}

@ComponentV2
struct ConsumerChildPage {
 <em> // 通过绑定同样的key获取其最近父节点的@Provider的数据</em>
  @Consumer('pageInfos') pageInfos: NavPathStack = new NavPathStack();
  @Local params: string = '';

  aboutToAppear(): void {
   <em> // getParamByIndex通过页面在路由栈中的索引位置获取参数（索引从栈底开始计算）</em>
    this.params = this.pageInfos.getParamByIndex(this.pageInfos.getAllPathName().length - 1) as string;
  }

  build() {
    NavDestination() {
      Column({ space: 16 }) {
        Text(this.params)
          .fontSize(18)
          .fontColor('#000000');
        Button('返回')
          .onClick(() => {
            this.pageInfos.pop();
          });
      }
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('100%');
    };
  }
}
```
 
**方案三：通过AppStorageV2实现路由跳转。**
 
将NavPathStack实例存入AppStorage中，在任意页面（包括子页面）中获取使用，该方法实现了全局访问，避免了组件间的强耦合。AppStorageV2进行传参只支持class类型，否则会抛出运行时报错。参考代码如下所示：
 
```text
import { AppStorageV2 } from '@kit.ArkUI';

@ObservedV2
class ParamData {
  @Trace param: string;

  constructor(param: string) {
    this.param = param;
  }
}

@Entry
@ComponentV2
struct AppStorageV2Page {
<em>  // 将key为NavPathStack，value为new NavPathStack()的键值对存入内存中，并赋值给pageInfos</em>
  @Local pageInfos: NavPathStack = AppStorageV2.connect<NavPathStack>(NavPathStack, () => new NavPathStack())!;
  @Local params: ParamData = new ParamData('使用V2传递的参数');

  @Builder
  pageMap(name: string) {
    if (name === 'ChildPage') {
      AppStorageV2ChildPage();
    }
  }

  aboutToAppear(): void {
 <em>   // AppStorageV2只支持class类型，否则会抛出运行时报错</em>
<em>    // 将key为ParamData，value为this.params的键值对存入内存</em>
    AppStorageV2.connect(ParamData, () => this.params);
  }

  build() {
    Navigation(this.pageInfos) {
      Column() {
        Button('跳转下一页面')
          .onClick(() => {
            this.pageInfos.pushPathByName('ChildPage', this.params, true);
          });
      }
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('100%');
    }
    .navDestination(this.pageMap);
  }
}

@ComponentV2
struct AppStorageV2ChildPage {
 <em> // key为NavPathStack已经在AppStorageV2中，将值返回给pageInfos</em>
  @Local pageInfos: NavPathStack = AppStorageV2.connect(NavPathStack) as NavPathStack;
 <em> // key为ParamData已经在AppStorageV2中，将值返回给params</em>
  @Local params: ParamData = AppStorageV2.connect(ParamData) as ParamData;

  build() {
    NavDestination() {
      Column({ space: 16 }) {
        Text(this.params.param)
          .fontSize(18)
          .fontColor('#000000');
        Button('返回')
          .onClick(() => {
            this.pageInfos.pop();
          });
      }
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('100%');
    };
  }
}
```
 
以上示例效果图如下所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/j6Qa6nbNToq4DlyD_Jy0OQ/zh-cn_image_0000002659060263.png?HW-CC-KV=V1&HW-CC-Date=20260723T013251Z&HW-CC-Expire=86400&HW-CC-Sign=A49B8F5C58F989A296589905C5F9A2DF1ABD9D773225C94705D3EB5A7265DA3D)

 

#### 总结
 
| 实现方案 | 适用场景 |
| --- | --- |
| 方案一：通过onReady实现路由跳转。 | 适用于接收路由跳转传递的参数、获取当前路由栈（NavPathStack）实例。 |
| 方案二：通过@Provider和Consumer实现路由跳转。 | 适用于导航容器内多个页面需要共享和控制同一状态。 |
| 方案三：通过AppStorageV2实现路由跳转。 | 适用于跨页面共享全局状态。 |
