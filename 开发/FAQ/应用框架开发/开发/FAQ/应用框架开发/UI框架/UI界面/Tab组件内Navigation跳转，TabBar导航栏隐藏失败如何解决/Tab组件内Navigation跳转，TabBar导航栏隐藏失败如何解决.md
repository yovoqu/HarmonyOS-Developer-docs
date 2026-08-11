# Tab组件内Navigation跳转，TabBar导航栏隐藏失败如何解决

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-904

#### 问题现象

在“我的”页面点击“跳转设置页”按钮跳转到设置页面，底部的TabBar导航栏仍然存在。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/XN0I7Qu9RWeKUJGfYj8PxQ/zh-cn_image_0000002658918977.png?HW-CC-KV=V1&HW-CC-Date=20260811T005650Z&HW-CC-Expire=86400&HW-CC-Sign=64304525349C33137222628ED64F7FA63886CAB1C1A814C1D5A1367DEED77F4C)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/Q3EdubCPQ76R5XOWPuo6yQ/zh-cn_image_0000002628399756.png?HW-CC-KV=V1&HW-CC-Date=20260811T005650Z&HW-CC-Expire=86400&HW-CC-Sign=B4537F49AE2D72B9CA27A5D868DD328160DF27E8489435D9FA7D795EFEF13982)

 
主页面有“首页”、“我的”两个Tab页面，部分代码如下：
 
```text
@Entry
@Component
struct TabsNavPage {
  build() {
    Tabs() {
      TabContent() {
        MinePage()
      }
      .tabBar(BottomTabBarStyle.of($r('sys.media.ohos_app_icon'), '我的'))

      TabContent() {
        Text('首页')
      }
      .tabBar(BottomTabBarStyle.of($r('sys.media.ohos_app_icon'), '首页'))
    }
    .barPosition(BarPosition.End)
  }
}

@Component
struct MinePage {
  @Provide('pathStack') pathStack: NavPathStack = new NavPathStack();

  @Builder
  PagesMap(name: string) {
    if (name === 'Settings') {
      Settings();
    }
  }

  build() {
    Navigation(this.pathStack) {
      Row(){
        Column() {
          Button('跳转设置页')
            .onClick(() => {
              this.pathStack.pushPathByName('Settings', null);
            })
        }
      }
    }
    .hideTitleBar(true)
    .navDestination(this.PagesMap)
  }
}

@Component
struct Settings {
  @Consume('pathStack') pathStack: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Button('返回')
        .onClick(() => {
          this.pathStack.pop();
        });
    }.title('设置')
  }
}
```
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/un0ap7csQJCKg7_JS0p0uQ/zh-cn_image_0000002658799025.png?HW-CC-KV=V1&HW-CC-Date=20260811T005650Z&HW-CC-Expire=86400&HW-CC-Sign=EC560F18649536A53F8CA079BB390F3609A0CBD0B512C5B6021331CDFE09B1EB)

 
 

#### 背景知识

- [Navigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation)组件是路由导航的根视图容器，一般作为Page页面的根容器使用，其内部默认包含了标题栏、内容区和工具栏，其中内容区默认首页显示导航内容（Navigation的子组件）或非首页显示（[NavDestination](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination)的子组件），首页和非首页通过路由进行切换。
- [@Provide装饰器和@Consume装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-provide-and-consume)：应用于与后代组件的双向数据同步、状态数据在多个层级之间传递的场景。

 
 

#### 解决方案

问题现象中是用Tab组件包裹Navigation组件，跳转Navigation子组件并不会影响到外层的Tab组件。
 
将Navigation组件作为根容器包括Tab组件，为保证子组件都共享一个NavPathStack实例，可以使用@Provide和@Consume装饰器将导航控制器对象[NavPathStack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#navpathstack10)传递给Tabs内的子组件使用。
 
```text
@Entry
@Component
struct TabsNavPage {
 <em> // 使用@Provide将路由栈对象传递给TabContent内的组件</em>
  @Provide('pathStack') pathStack: NavPathStack = new NavPathStack();

  @Builder
  PagesMap(name: string) {
    if (name === 'Settings') {
      Settings();
    }
  }

  build() {
   <em> // 使用Navigation包裹Tabs，Tabs子页使用同一个路由栈对象</em>
    Navigation(this.pathStack) {
      Tabs() {
        TabContent() {
          MinePage();
        }
        .tabBar(BottomTabBarStyle.of($r('sys.media.ohos_app_icon'), '我的'))

        TabContent() {
          Text('首页').fontColor('40fp');
        }
        .tabBar(BottomTabBarStyle.of($r('sys.media.ohos_app_icon'), '首页'))
      }
      .barPosition(BarPosition.End);
    }
    .hideTitleBar(true)
    .navDestination(this.PagesMap)
  }
}

@Component
struct MinePage {
 <em> // 获取Navigation的路由栈对象</em>
  @Consume('pathStack') pathStack: NavPathStack;

  build() {
    Column() {
      Button('跳转设置页')
        .onClick(() => {
          this.pathStack.pushPathByName('Settings', null);
        });
    };
  }
}

@Component
struct Settings {
  @Consume('pathStack') pathStack: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Button('返回')
        .onClick(() => {
          this.pathStack.pop();
        });
    }.title('设置')
  }
}
```
