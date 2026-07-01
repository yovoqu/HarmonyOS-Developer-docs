# Navigation如何携带参数返回首页

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-708

## Navigation如何携带参数返回首页
 


##### 问题现象

使用Navigation实现页面导航功能，从首页跳转到其他非首页之后，再次返回首页，如何将数据传递回首页？
 
 

##### 背景知识

- [Navigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation)组件是路由导航的根视图容器，一般作为Page页面的根容器使用，其内部可分为首页和子页。首页又称为导航栏（NavBar），由三部分组成：标题栏、内容区（Navigation子组件）、工具栏。
 子页则通过[NavDestination](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination)承载，由两部分组成：标题栏、内容区（NavDestination子组件）。
- Navigation路由相关的操作都是基于页面栈[NavPathStack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#navpathstack10)提供的方法进行，每个Navigation都需要创建并传入一个NavPathStack对象，用于管理页面。主要涉及页面跳转、页面返回、页面替换、页面删除、参数获取、路由拦截等功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/pdvwKig0RH6Km5zoBE9zrw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260701T025543Z&HW-CC-Expire=86400&HW-CC-Sign=4D81FEDAF442FD802EF8B7E2D4A777FB9CE00F4AC499DD1769334F51650C3FC0)
 
首页并不属于路由栈（NavPathStack）管理，路由栈只能控制NavDestination页面的入栈出栈。
- [pushPathByName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#pushpathbyname11)：将name指定的NavDestination页面信息入栈，传递的数据为param，添加onPop回调接收入栈页面出栈时的返回结果，并进行处理。
- [@ohos.events.emitter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-emitter)：支持持续订阅事件、单次订阅事件、取消订阅事件及发送事件到事件队列。
- [hideNavBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#hidenavbar9)：设置是否隐藏导航栏。设置为true时，隐藏Navigation的导航栏，包括标题栏、内容区和工具栏。如果此时路由栈中存在NavDestination页面，则直接显示栈顶NavDestination页面，反之显示空白。

 
返回首页一般存在两种方式：
 
- 通过NavPathStack的pop方法一步步回退至首页，最简单的场景是：首页->PageOne->首页。
- 首页跳转至其他页面之后，经过其他页面多次跳转，再立马返回首页。一个简单的场景是：首页->PageOne->PageTwo->首页。

 
 

##### 解决方案

- **场景一：**从其他页面一步步回退至首页。直接在首页通过pushPathByName等方法跳转到PageOne页面，同时添加onPop回调接收PageOne页面返回的参数即可。
 
```text
@Entry
@Component
struct NavPopSolution {
  pathStack: NavPathStack = new NavPathStack();
  @State message: string = '展示返回参数';

  @Builder
  pageMap(name: string) {
    if (name === 'PageOne') {
      PageOne();
    }
  }

  build() {
    Navigation(this.pathStack) {
      Column({ space: 16 }) {
        Text(this.message);
        Button('跳转到PageOne', { stateEffect: true, type: ButtonType.Capsule })
          .onClick(() => {
            this.pathStack.pushPathByName('PageOne', '', (data) => {
              // 用于页面出栈时触发该回调处理返回结果。
              this.message = JSON.stringify(data.result);
            });
          });
      };
    }.title('首页')
    .navDestination(this.pageMap);
  }
}

@Component
struct PageOne {
  pathStack: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Column() {
        Button('携带参数回退首页', { stateEffect: true, type: ButtonType.Capsule })
          .onClick(() => {
            this.pathStack.pop({ 'content': 'c' });
          });
      };
    }.title('PageOne')
    .onReady((context: NavDestinationContext) => {
      this.pathStack = context.pathStack;
    });
  }
}
```
 效果预览：
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/2FJuhdcmTFezVGRJYS3BCA/zh-cn_image_0000002628394992.png?HW-CC-KV=V1&HW-CC-Date=20260701T025543Z&HW-CC-Expire=86400&HW-CC-Sign=9F2EDC51C2E1853BC0B64DFB3C3BE9F9FCA240717B9E7FF6D108E1005CE57875)

- **场景二**：首页跳转至其他页面之后，经过其他页面多次跳转，再立马返回首页。由于需要立马返回首页，无法一步步将路由栈中页面逐个出栈，所以无法通过出栈时的onPop回调，拿到上一个页面出栈时携带的参数。且首页无法推入路由栈，不能使用push类方法跳转，也没有onReady生命周期，所以也无法在onReady接收其他子页的传参。
 现提供两种方式完成跳转，并将参数携带回首页。
 
**方案一**：不使用默认的首页，将一个NavDestination自定义为首页。在返回自定义首页MainPage时，先调用[clear](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#clear10)方法清除路由栈中的页面，然后重新将MainPage页入栈，即可在MainPage页[onReady](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#onready11)方法中接收返回的参数。
在Navigation首页设置hideNavBar为true，在aboutToAppear方法中将MainPage入栈，设置为自定义首页。通过[setInterception](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#setinterception12)拦截所有返回到Navigation首页的操作，重定向到自定义首页。
- 从PageTwo页面跳转至MainPage，先使用clear()清除路由栈，再主动调用pushPath跳转到自定义首页MainPage。MainPage页面通过onReady方法获取传递参数。
```text
@Entry
@Component
struct NavMainPageExample {
  pathStack: NavPathStack = new NavPathStack();

  aboutToAppear() {
    // 将MainPage设置成自定义首页
    this.pathStack.pushPathByName('MainPage', '', false);
    // 设置Navigation页面跳转拦截回调
    this.pathStack.setInterception({
      willShow: (from: NavDestinationContext | 'navBar', to: NavDestinationContext | 'navBar',
        operation: NavigationOperation, animated: boolean) => {
        console.info(`${from} ${to} ${operation} ${animated}`);
        // 如果要返回到首页，就push名为MainPage的子页面
        if (to === 'navBar') {
          this.pathStack.pushPathByName('MainPage', '', false);
        }
      }
    });
  }

  @Builder
  pageMap(name: string) {
    if (name === 'MainPage') {
      MainPage();
    } else if (name === 'PageOne') {
      PageOne();
    } else if (name === 'PageTwo') {
      PageTwo();
    }
  }

  build() {
    Navigation(this.pathStack) {
    }.hideNavBar(true) // 隐藏首页
    .navDestination(this.pageMap);
  }
}

// NavDestination作为首页
@Component
struct MainPage {
  @State message: string = '';
  pathStack: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Column({ space: 16 }) {
        Text(this.message);
        Button('跳转到PageOne', { stateEffect: true, type: ButtonType.Capsule })
          .onClick(() => {
            this.pathStack.pushPathByName('PageOne', null, true);
          });
      };
    }.title('MainPage')
    .onReady((ctx: NavDestinationContext) => {
      this.pathStack = ctx.pathStack;
      this.message = JSON.stringify(this.pathStack.getParamByName('MainPage'));
    });
  }
}

@Component
export struct PageOne {
  pathStack: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Column() {
        Button('跳转到PageTwo', { stateEffect: true, type: ButtonType.Capsule })
          .onClick(() => {
            this.pathStack.pushPathByName('PageTwo', null, true);
          });
      };
    }.title('PageOne')
    .onReady((context: NavDestinationContext) => {
      this.pathStack = context.pathStack;
    });
  }
}

@Component
struct PageTwo {
  pathStack: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Column() {
        Button('携带参数回退首页', { stateEffect: true, type: ButtonType.Capsule })
          .onClick(() => {
            this.pathStack.clear(); // 清除路由栈
            this.pathStack.pushPath({ name: 'MainPage', param: 'context' }); // 跳转到自定义首页
          });
      };
    }.title('PageTwo')
    .onReady((context: NavDestinationContext) => {
      this.pathStack = context.pathStack;
    });
  }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/XtjlNUuWTumTxYRM2rq47g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260701T025543Z&HW-CC-Expire=86400&HW-CC-Sign=36C2FF2E5F32BB940F83B135CDAC49A1695F223643ECAA905FA6F11226CBB900)
 
连续调用多个页面栈操作方法时，中间过程会被忽略，显示最终的栈操作结果。
 

 效果预览：
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/1jlaw3eJReKa3dUO_V3C8A/zh-cn_image_0000002658794257.png?HW-CC-KV=V1&HW-CC-Date=20260701T025543Z&HW-CC-Expire=86400&HW-CC-Sign=F1E6D91E8DC9CA6E885D7FA4E5FC2B3F90D624B8D175D545359E938FA5B4F87E)


 - **方案二**：在首页的aboutToAppear订阅事件，在clear清除路由栈时通过订阅的事件将参数传递回首页。
```text
import emitter from '@ohos.events.emitter';

@Entry
@Component
struct EmitterSolution {
  pathStack: NavPathStack = new NavPathStack();
  @State message: emitter.EventData = {};

  aboutToAppear() {
    // 监听back事件，获取参数
    emitter.on('back', (data) => {
      this.message = data;
    });
  }

  aboutToDisappear() {
    emitter.off('back'); // 取消监听
  }

  @Builder
  pageMap(name: string) {
    if (name === 'PageOne') {
      PageOne();
    } else if (name === 'PageTwo') {
      PageTwo();
    }
  }

  build() {
    Navigation(this.pathStack) {
      Column({ space: 16 }) {
        Text(JSON.stringify(this.message));
        Button('跳转到PageOne', { stateEffect: true, type: ButtonType.Capsule })
          .onClick(() => {
            this.pathStack.pushPathByName('PageOne', null, true);
          });
      };
    }.title('首页')
    .navDestination(this.pageMap);
  }
}

@Component
struct PageOne {
  pathStack: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Column() {
        Button('跳转到PageTwo', { stateEffect: true, type: ButtonType.Capsule })
          .onClick(() => {
            this.pathStack.pushPathByName('PageTwo', null, true);
          });
      };
    }.title('PageOne')
    .onReady((context: NavDestinationContext) => {
      this.pathStack = context.pathStack;
    });
  }
}

@Component
struct PageTwo {
  pathStack: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Column() {
        Button('回退到首页，通过emitter传递参数', { stateEffect: true, type: ButtonType.Capsule })
          .onClick(() => {
            this.pathStack.clear();
            let eventData: emitter.EventData = { data: { 'content': 'c', 'id': '1' } };
            emitter.emit('back', eventData); // 传递back事件给首页
          });
      };
    }.title('pageTwo').onReady((context: NavDestinationContext) => {
      this.pathStack = context.pathStack;
    });
  }
}
```
 效果预览：
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/bLvbPWA5TIiOu1Yzk-pO_Q/zh-cn_image_0000002628554896.png?HW-CC-KV=V1&HW-CC-Date=20260701T025543Z&HW-CC-Expire=86400&HW-CC-Sign=5BF01BD80CE290D25F73A4C575FA29E396B1553E13B9057EF3F4C00E99C21DE0)


 
 
 

##### 常见FAQ

Q：Navigation如何直接返回首页？
 
A：首页不存在页面栈中，可看作在栈中的位置为-1，使用this.pathStack.clear()清空栈即可返回首页。
 
 

##### 总结
 
| 场景 | 方案 | 说明 |
| --- | --- | --- |
| 从其他页面一步步回退至首页 | 使用onPop回调链式接收 | 适合页面逐级返回的场景。 |
| 多次跳转之后立马返回 | 自定义首页 | 无法适配导航栏分栏显示模式。需要对自定义首页进行路由管理。导航栏等需要自定义实现。 |
| 多次跳转之后立马返回 | 事件订阅 | 页面销毁时未正确销毁监听，可能会导致内存泄露。需要新增一个订阅事件，造成订阅事件过多。 |
