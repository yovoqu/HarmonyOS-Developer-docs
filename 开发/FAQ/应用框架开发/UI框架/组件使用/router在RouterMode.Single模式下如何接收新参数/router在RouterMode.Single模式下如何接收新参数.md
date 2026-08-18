# router在RouterMode.Single模式下如何接收新参数

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-587

#### 问题现象

使用router的Single模式进行路由跳转时，跳转已存在的页面，如何接收参数？在页面的onPageShow生命周期函数中接收参数，切换后台会导致参数重置，如何处理？
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/cYoJSgNRRQ-21HltA2nQwQ/zh-cn_image_0000002658791771.png?HW-CC-KV=V1&HW-CC-Date=20260811T005757Z&HW-CC-Expire=86400&HW-CC-Sign=361FBD4553A078236367B59899C8AF5D7D13DCE1B030C66D2F641CA04ADF28DD)

 
 

#### 背景知识

[router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)进行应用内的页面跳转时，可以指定跳转页面使用的模式。其中，使用[RouterMode.Single](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-router#routermode9)模式时，如果目标页面的url已经在页面栈中存在，该页面会被移动到栈顶，而不会创建新的实例。如果不存在，才会按照默认的多实例模式进行跳转。
 
对于不同页面之间的参数传递，可以使用[AppStorage](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-appstorage)实现。AppStorage是应用全局的UI状态存储，与应用的进程绑定，由UI框架在应用程序启动时创建。使用[@StorageLink](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-appstorage#storagelink)(key)修饰符可以将组件中的属性与AppStorage中对应的属性建立双向数据同步。
 
 

#### 解决方案

- 方案一：在onPageShow中获取参数，使用AppStorage存储应用是否切换后台的标志位，通过标志位过滤返回参数为空和切后台返回的情况，避免参数重新读取。
PageOne.ets代码示例如下：
```text
import { router } from '@kit.ArkUI';

export class RouterParams {
  message: string = '';

  constructor(message: string) {
    this.message = message;
  }
}

@Entry
@Component
struct PageOne {
  build() {
    Column() {
      Text('PageOne')
        .fontSize(40)
        .onClick(() => {
          let params: RouterParams = new RouterParams('param from pageOne');
          this.getUIContext().getRouter().pushUrl({
            url: 'pages/PageTwo',
            params: params,
          }, router.RouterMode.Single);
        })
    }.height('100%').width('100%').justifyContent(FlexAlign.Center)
  }
}
```


 
- PageTwo.ets代码示例如下：
```text
import { router } from '@kit.ArkUI';
import { RouterParams } from './PageOne';

@Entry
@Component
struct PageTwo {
  @State params: RouterParams = this.getUIContext().getRouter().getParams() as RouterParams;

  onPageShow(): void {
    let param: RouterParams = this.getUIContext().getRouter().getParams() as RouterParams;
    // 过滤返回param为空和切后台
    if (param !== undefined && !AppStorage.get('fromBackground')) {
      this.params = param;
      console.info(`${param.message}`);
    }
    AppStorage.setOrCreate('fromBackground', false);
  }

  build() {
    Column({ space: 20 }) {
      Text(this.params.message)
        .fontSize(20)
        .onClick(() => {
          this.getUIContext().getRouter().pushUrl({
            url: 'pages/PageThree',
          }, router.RouterMode.Standard);
        })
      Button('ChangeParams')
        .fontSize(20)
        .onClick(() => {
          this.params.message = 'Change Params';
        })
    }.height('100%').width('100%').justifyContent(FlexAlign.Center)
  }
}
```


 
- PageThree.ets代码示例如下：
```text
import { RouterParams } from './PageOne';
import { router } from '@kit.ArkUI';

@Entry
@Component
struct PageThree {
  build() {
    Column() {
      Text('PageThree')
        .fontSize(40)
        .onClick(() => {
          let params: RouterParams = new RouterParams('param from pageThree');
          this.getUIContext().getRouter().pushUrl({
            url: 'pages/PageTwo',
            params: params,
          }, router.RouterMode.Single);
        })
    }.height('100%').width('100%').justifyContent(FlexAlign.Center)
  }
}
```


 
- EntryAbility.ets代码示例如下：
```text
onCreate(): void {
  AppStorage.setOrCreate('fromBackground', false);
}
onBackground(): void {
  // 切换后台，设置判断标志位true
  AppStorage.setOrCreate('fromBackground', true);
}
```


 - 方案二：不使用router进行参数传递，改用AppStorage实现跨页面参数传递，并用@StorageLink(key)和AppStorage中key对应的属性建立双向数据同步实现UI刷新。
AppStoragePageOne.ets代码示例如下：
```text
import { router } from '@kit.ArkUI';

export class RouterParams {
  message: string = '';

  constructor(message: string) {
    this.message = message;
  }
}

@Entry
@Component
struct AppStoragePageOne {
  build() {
    Column() {
      Text('PageOne')
        .fontSize(40)
        .onClick(() => {
          let params: RouterParams = new RouterParams('param from PageOne');
          AppStorage.setOrCreate('AppStoragePageTwoParam', params);
          this.getUIContext().getRouter().pushUrl({
            url: 'pages/AppStoragePageTwo',
          }, router.RouterMode.Single);
        })
    }.height('100%').width('100%').justifyContent(FlexAlign.Center)
  }
}
```


 
- AppStoragePageTwo.ets代码示例如下：
```text
import { router } from '@kit.ArkUI';
import { RouterParams } from './AppStoragePageOne';

@Entry
@Component
struct AppStoragePageTwo {
  @StorageLink('AppStoragePageTwoParam') params: RouterParams = new RouterParams('');

  build() {
    Column({ space: 20 }) {
      Text(this.params.message)
        .fontSize(20)
        .onClick(() => {
          this.getUIContext().getRouter().pushUrl({
            url: 'pages/AppStoragePageThree',
          }, router.RouterMode.Standard);
        })
      Button('ChangeParams')
        .fontSize(20)
        .onClick(() => {
          let params = (AppStorage.get('AppStoragePageTwoParam') as RouterParams);
          params.message = 'ChangeParams';
          AppStorage.setOrCreate('AppStoragePageTwoParam', params);
        })
    }.height('100%').width('100%').justifyContent(FlexAlign.Center)
  }
}
```

- AppStoragePageThree.ets代码示例如下：
```text
import { RouterParams } from './AppStoragePageOne';
import { router } from '@kit.ArkUI';

@Entry
@Component
struct AppStoragePageThree {
  build() {
    Column() {
      Text('PageThree')
        .fontSize(40)
        .onClick(() => {
          let params: RouterParams = new RouterParams('param from PageThree');
          AppStorage.setOrCreate('AppStoragePageTwoParam', params);
          this.getUIContext().getRouter().pushUrl({
            url: 'pages/AppStoragePageTwo',
          }, router.RouterMode.Single);
        })
    }.height('100%').width('100%').justifyContent(FlexAlign.Center)
  }
}
```


 
 
 

#### 总结

方案一、二均使用到AppStorage实现页面参数传递：
 
- 方案一在router传参的基础上，使用AppStorage存储标志位辅助判断，过滤前后台切换的情况。
- 方案二是直接使用AppStorage+@StorageLink替代router的传参功能。
