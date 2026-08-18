# NavPathStack如何在自己封装的公共类中使用

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-761

#### 问题现象

NavPathStack能在子组件中使用或者自己封装的公共类中使用吗，如何使用？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/bDEWbxwXT624J4Li6sTtOQ/zh-cn_image_0000002628395798.gif?HW-CC-KV=V1&HW-CC-Date=20260811T005644Z&HW-CC-Expire=86400&HW-CC-Sign=05549769093AA3EDBD36C7E6F63D2186B613C970998E27F1CFA36051E59B7C7B)

 
 

#### 背景知识

- [AppStorage](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-appstorage)：应用全局的UI状态存储。
- [Navigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#navigation-1)：Navigation组件是路由导航的根视图容器，一般作为Page页面的根容器使用，其内部默认包含了标题栏、内容区和工具栏，其中内容区默认首页显示导航内容（Navigation的子组件）或非首页显示（[NavDestination](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination)的子组件），首页和非首页通过路由进行切换。

 
 

#### 解决方案
1. 新增PublicUtils文件并定义跳转页面的公共方法。
```text
export class Tmp {
  pushPath(name: string) {
    (AppStorage.get('pathStack') as NavPathStack).pushPath({ name: name });
  }
}
```

2. 将NavPathStack缓存起来。
```ArkTS
// Index.ets
import { Tmp } from './PublicUtils';

@Entry
@Component
struct Index {
  // 创建一个页面栈对象并传入Navigation
  private pathStack: NavPathStack = new NavPathStack();
  private InfoTmp: Tmp = new Tmp();

  aboutToAppear(): void {
    // 存储pathStack
    AppStorage.setOrCreate('pathStack', this.pathStack);
  }

  build() {
    Navigation(this.pathStack) {
      Button('click')
        .onClick(() => {
          // 调用pushPath方法并跳转到对应页面
          this.InfoTmp.pushPath('PageOne');
        });
    }
    .title('Main');
  }
}
```

3. PageOne页面：
```text
@Builder
export function PageOneBuilder() {
  PageOne();
}

@Component
export struct PageOne {
  build() {
    NavDestination() {
      Button('setInteractive');
    }
    .width('100%')
    .height('100%');
  }
}
```

4. 在src/main目录下的工程配置文件module.json5中的module字段里配置"routerMap": "$profile:router_map"，并在src/main/resources/base/profile目录下新增router_map.json。router_map.json示例参考如下：
```ArkTS
{
  "routerMap": [
    {
      "name": "PageOne",
      "pageSourceFile": "src/main/ets/pages/PageOne.ets",
      "buildFunction": "PageOneBuilder"
    }
  ]
}
```
