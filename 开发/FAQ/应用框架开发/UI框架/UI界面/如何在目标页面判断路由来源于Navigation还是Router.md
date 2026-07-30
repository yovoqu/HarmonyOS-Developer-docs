# 如何在目标页面判断路由来源于Navigation还是Router

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1455

#### 问题现象

同时使用Navigation和router进行路由跳转，如何在目标页面判断路由来源？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/UFb2u7uOSzKuFHJbmC-HWw/zh-cn_image_0000002658963487.gif?HW-CC-KV=V1&HW-CC-Date=20260701T041158Z&HW-CC-Expire=86400&HW-CC-Sign=EC5F54413DF4E2FF1E3D63F5F3FF29D83670AB1A1FEADA025B344A69F0B1CBE1)

 
 

#### 背景知识

- [Navigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation)组件是路由导航的根视图容器，一般作为Page页面的根容器使用，其内部默认包含了标题栏、内容区和工具栏，其中内容区默认首页显示导航内容（Navigation的子组件）或非首页显示（NavDestination的子组件），首页和非首页通过路由进行切换。
- HarmonyOS提供的[router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)模块实现通过不同的url访问不同的页面，包括跳转到应用内的指定页面、同应用内的某个页面替换当前页面、返回上一页面或指定的页面等功能。

 
 

#### 解决方案
1. 在主页面使用NavPathStack的pushPathByName方法进行Navigation路由跳转，使用router的pushUrl进行router路由跳转。
2. 在目标页面的NavDestination组件的onReady回调函数中进行路由来源判断，若当前页面UIContext中Router对象获取参数为undefined，则表明该页面由Navigation组件跳转而来，并通过NavPathStack的getParamByName方法获取传递的参数并显示在页面上；反之则表明该页面由router跳转而来，通过getParams方法获取参数并显示。
 
```text
export class RouterParams {
  text: string;

  constructor(str: string) {
    this.text = str;
  }
}

@Entry
@Component
struct NavigationRouterDemo {
  pageInfos: NavPathStack = new NavPathStack();

  build() {
    Navigation(this.pageInfos) {
      Column({ space: 20 }) {
        Button('Navigation跳转', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .onClick(() => {
         <em>   // navigation路由跳转</em>
            const info = new RouterParams('以Navigation方式进行跳转');
            this.pageInfos.pushPathByName('PageD', info);
          });
        Button('Router跳转', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .onClick(() => {
          <em>  // router路由跳转</em>
            this.getUIContext()
              .getRouter()
              .pushUrl({ url: 'pages/PageD', params: new RouterParams('以Router方式进行跳转') });
          });
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Center)
      .padding('20vp');
    }
    .title('Navigation-Router跳转时判断路由来源');
  }
}
```
 
pageD页面代码如下：
 
```json
import { RouterParams } from './NavigationRouterDemo';

@Builder
export function PageDBuilder() {
  PageD();
}

@Entry
@Component
struct PageD {
  pageInfos: NavPathStack = new NavPathStack();
  @State message: string = 'test';

  build() {
    NavDestination() {
      Column({ space: 20 }) {
        Text(this.message);
      }
      .justifyContent(FlexAlign.Center)
      .height('100%')
      .width('100%');
    }
    .title('PageD')
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
      if (JSON.stringify(this.getUIContext().getRouter().getParams()) === undefined) {
        this.message = JSON.stringify(this.pageInfos.getParamByName('PageD'));
        console.info('navigation 跳转');
      } else {
        this.message = (this.getUIContext().getRouter().getParams() as RouterParams).text;
        console.info('router 跳转');
      }
    });
  }
}
```
 
路由表router_map.json如下：
 
```ArkTS
{
  "routerMap": [
    {
      "name": "PageD",
      "pageSourceFile": "src/main/ets/pages/PageD.ets",
      "buildFunction": "PageDBuilder",
      "data": {
        "description": "this is PageD"
      }
    }
  ]
}
```
 
 

#### 总结

router配合@Entry的路由方式存在一些弊端：页面与页面之间相互独立，无法产生关联，在页面之间元素进行共享互动的场景下很难实现复杂动效等，故推荐使用Navigation组件作为应用路由框架。
