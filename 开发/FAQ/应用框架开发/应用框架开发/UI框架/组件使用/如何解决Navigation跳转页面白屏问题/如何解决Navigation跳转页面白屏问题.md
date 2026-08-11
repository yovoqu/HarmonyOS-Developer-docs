# 如何解决Navigation跳转页面白屏问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1018

#### 问题现象

使用Navigation进行页面跳转或返回时，页面出现白屏现象，该如何解决？
 
场景一：打开应用并加载Navigation页面时，页面显示白屏。
 
场景二：执行pop或clear返回操作时，页面显示白屏。
 
场景三：点击跳转后，目标页面显示白屏。
 
场景四：在平板的分栏模式下，点击左侧导航区域进行跳转后，右侧页面显示白屏。
 
场景五：使用预览器调试时，Navigation跳转到子页面，子页面显示白屏。
 
 

#### 背景知识

- [Navigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation)：Navigation组件是路由导航的根视图容器，一般作为Page页面的根容器使用，其内部默认包含了标题栏、内容区和工具栏，其中内容区默认首页显示导航内容（Navigation的子组件）或非首页显示（NavDestination的子组件），首页和非首页通过路由进行切换。
- [NavPathStack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#navpathstack10)：Navigation导航控制器，以栈的数据结构管理Navigation中所有的子页面，并提供栈操作的方法用于控制Navigation中子页面的切换。
- [NavDestination](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination)：作为子页面的根容器，用于显示Navigation的内容区。

 
 

#### 解决方案

**场景一和场景二**：
 
排查是否设置了Navigation的[hideNavBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#hidenavbar9)属性为true。设置为true时，隐藏Navigation的导航页，包括标题栏、内容区和工具栏。如果此时路由栈中存在NavDestination页面，则直接显示栈顶NavDestination页面，反之显示空白。
 
有以下两种解决方案可供参考：
 
- 设置hideNavBar属性为false。
- 在Navigation所在页面的aboutToAppear函数中跳转NavDestination子页，并使用[setInterception](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#setinterception12)设置路由拦截，当通过执行pop/clear操作导致回到NavBar时，跳转至指定NavDestination子页。

  HideNavBarPage页面代码如下，Entry页面需在resources/base/profile/main_pages.json配置，参考[pages标签](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#pages标签)。NavDesOne页面代码和路由表配置见下文的系统路由表的2、3点。
```text
@Entry
@Component
struct HideNavBarPage {
  pathStack: NavPathStack = new NavPathStack(); <em>// </em><em>导航控制器对象</em>

  aboutToAppear(): void {
    <em>// 进入主页面时直接 push 一个子页面，这个子页面就作为 APP 的主页面</em>
    this.pathStack.pushPathByName('NavDesOne', undefined, false); <em>// 注意关闭转场动画效果</em>
    <em>// 使用路由拦截功能</em>
    this.pathStack.setInterception({
      willShow: (from: NavDestinationContext | NavBar, to: NavDestinationContext | NavBar,
        operation: NavigationOperation, isAnimated: boolean) => {
        console.info(`${from} ${to} ${operation} ${isAnimated}`);
     <em>   // 如果要返回到主页面，就 push 名为 NavDesOne 的子页面</em>
        if (to == 'navBar') {
        <em>  // 注意关闭转场动画效果，NavDesOne需自行创建并配置</em>
          this.pathStack.pushPathByName('NavDesOne', undefined, false);
        }
      }
    });
  }

  build() {
    Navigation(this.pathStack) {
    }
    .hideNavBar(true) <em>// NavBar页面不显示</em>
    .height('100%').width('100%');
  }
}
```


 
**场景三和场景四**：
 
排查路由表配置是否正常，可参考[系统路由表](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-cross-package#系统路由表)和[自定义路由表](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-cross-package#自定义路由表)。
 
- 系统路由表：1. 检查是否在entry模块的src/main/module.json5引用路由表。
```json
"routerMap": "$profile:route_map",
```


2. 检查使用[pushPath](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#pushpath10)等方法跳转时，入参的页面名称需和系统路由表src/main/resources/base/profile/route_map.json中配置的名称一致，**特别注意大小写**。
```ArkTS
{
  "routerMap": [
    {
      "name": "NavDesOne",
      "pageSourceFile": "src/main/ets/pages/NavDesOne.ets",
      "buildFunction": "NavDesBuilder"
    }
  ]
}
```
 RouterMapDemo页面代码如下，Entry页面需在resources/base/profile/main_pages.json配置，参考[pages标签](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#pages标签)。

  
```text
@Entry
@Component
struct RouterMapDemo {
  pathStack: NavPathStack = new NavPathStack(); <em>// 导航控制器对象</em>

  build() {
    <em>// 根节点使用Navigation组件</em>
    Navigation(this.pathStack) { <em>// 将导航控制器对象和Navigation绑定</em>
      Column({ space: 24 }) {
        Text('这是Navigation根页面');
        Button('跳转NavDestination子页')
          .onClick(() => {
            <em>// 通过name（需要和路由表route_map设置的name保持一致）指定子页</em>
            this.pathStack.pushPath({ name: 'NavDesOne' }, true);
          });
      }.width('100%').height('100%');
    }
    .hideToolBar(true) <em>// 隐藏工具栏</em>
    .height('100%').width('100%');
  }
}
```


3. 检查子页面的根节点是否使用NavDestination包裹。子页NavDesOne代码如下：
```text
@Builder
export function NavDesBuilder() {
  NavDesOne();
}

@Component
struct NavDesOne {
  pathStack: NavPathStack = new NavPathStack(); <em>// 导航控制器对象</em>

  build() {
    NavDestination() {
      Column({ space: 24 }) {
        Text('Hello World').fontSize(36);
      }.width('100%').height('100%').justifyContent(FlexAlign.Center);
    }
    .onReady((ctx: NavDestinationContext) => {
     <em> // 通过NavDestination上下文信息获取到导航控制器对象</em>
<em>      // Navigation及其所有子页的pathStack需保证为同一个</em>
      this.pathStack = ctx.pathStack;
    });
  }
}
```

- 自定义路由表：1. 检查是否使用[navDestination](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#navdestination10)注册路由表。

2. 检查使用[pushPath](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#pushpath10)等方法跳转时，入参的页面名称需和自定义路由表中配置的名称一致，**特别注意大小写**。

3. 检查自定义路由表的函数是否用[@Builder](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builder)装饰。

4. 检查子页面的根节点是否使用NavDestination包裹。NavDesMapDemo代码如下，Entry页面需在resources/base/profile/main_pages.json配置，参考[pages标签](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#pages标签)。NavDesOne代码见上文系统路由表第3点。

  
```text
import { NavDesBuilder } from './NavDesOne'; <em>// 静态import导入页面</em>

@Entry
@Component
struct NavDesMapDemo {
  pathStack: NavPathStack = new NavPathStack();<em> </em><em>// 导航控制器对象</em>

  build() {
  <em>  // 根节点使用Navigation组件</em>
    Navigation(this.pathStack) { <em>// 将导航控制器对象和Navigation绑定</em>
      Column({ space: 24 }) {
        Text('这是Navigation根页面');
        Button('跳转NavDestination子页')
          .onClick(() => {
           <em> // 通过name（需要和自定义路由表设置的name保持一致）指定子页</em>
            this.pathStack.pushPath({ name: 'NavDesOne' }, true);
          });
      };
    }
    .navDestination(this.pageMap)<em> </em><em>// 注册路由表</em>
    .hideToolBar(true) <em>// 隐藏工具栏</em>
    .height('100%').width('100%');
  }

 <em> // 自定义路由表：根据子页名称寻址</em>
  @Builder
  pageMap(name: string) {
    if (name === 'NavDesOne') {
      NavDesBuilder();
    }
  }
}
```


 
**场景五**：
 
预览器不支持Navigation路由跳转，建议使用模拟器或真机进行调试。
 
 

#### 常见FAQ

Q：跳转HAR包页面显示白屏，如何处理？
 
A：按照上述方案排查，并确认在需要引入三方库的模块的oh-package.json5中设置三方包依赖。参考[引用及管理共享包](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-har-import)。
