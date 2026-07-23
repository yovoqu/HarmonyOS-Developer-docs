# Navigation中如何关闭removeByName删除页面时的默认动画

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-776

#### 问题现象

Navigation中使用removeByName删除页面时存在从底部滑出的动画，API文档上未提供关闭动画的参数，如何关闭该动画？
 
目前效果如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/gMZ2ZD-yTxC_gXoSh8RnrA/zh-cn_image_0000002658915025.png?HW-CC-KV=V1&HW-CC-Date=20260723T013114Z&HW-CC-Expire=86400&HW-CC-Sign=0DE623DABE86F015CD6AAD543574BD378590D6C0EC40C0E0199423C18E0409B3)

 
 

#### 背景知识

[customNavContentTransition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#customnavcontenttransition11)：设置Navigation自定义转场动画，通过返回的from、to得到退场/进场Destination的页面，其中也包括NavDestination名称、序号等信息，可以区分不同的NavDestination页面。
 
 

#### 解决方案

可以通过[customNavContentTransition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#customnavcontenttransition11)设置自定义转场动画，设置退场时无动画实现关闭removeByName的默认动画，如：
 
Navigation中设置customNavContentTransition，通过返回的name区分页面：
 
```text
@Entry
@Component
struct Index {
  @Provide('pageInfos') pageInfo: NavPathStack = new NavPathStack();
  @State flag: boolean = false;


  aboutToAppear(): void {
    let eventhub = this.getUIContext().getHostContext()?.eventHub;
    eventhub!.on('removeByNameEvent', () => {
      this.flag = true;
    });
  }


  build() {
    Navigation(this.pageInfo) {
      Column({ space: 10 }) {
        Button('点我push第二页')
          .onClick(() => {
            this.pageInfo.pushPathByName('SubPage', null, false);
          });
      }
      .alignItems(HorizontalAlign.Center)
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('100%');
    }
    <em>// 设置自定义转场动画</em>
    .customNavContentTransition((from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) => {
      console.info(`current info: ${to.name}, index: ${to.index}, mode: ${to.mode}`);
      console.info(`pre info: ${from.name}, index: ${from.index}, mode: ${from.mode}`);
      console.info(`operation: ${operation}`);
    <em>  // 通过name区分具体的页面</em>
      if (from.name == 'SubPage' && this.flag === true) {
        this.flag = false;
        let customAnimation: NavigationAnimatedTransition = {
          onTransitionEnd: (isSuccess: boolean) => {
            console.info(`current transition result is ${isSuccess}`);
          },
          timeout: 100,
          <em>// 转场开始时系统调用该方法，并传入转场上下文代理对象</em>
          transition: () => {
            if (operation == NavigationOperation.POP) {
              this.getUIContext().animateTo({
                duration: 0, <em>// 持续时间设置为0</em>
              }, () => {
              });
            }
          }
        };
        return customAnimation;
      }
      return undefined;
    });
  }
}
```
 
注册SubPage页面：
 
```text
@Builder
export function RegisterBuilder(): void {
  SubPage();
}


@Component
struct SubPage {
  @Consume('pageInfo') pathStack: NavPathStack;


  build() {
    NavDestination() {
      Column({ space: 20 }) {
        Button('removeByName当前页面')
          .onClick(() => {
            let eventhub = this.getUIContext().getHostContext()?.eventHub;
          <em>  // 通过eventHub设置removeByName的区分标志区分removeByName和页面返回事件</em>
            eventhub!.emit('removeByNameEvent');
            this.pathStack.removeByName('SubPage');
          });
      }
      .width('100%')
      .height('100%')
      .alignItems(HorizontalAlign.Center)
      .justifyContent(FlexAlign.Center)
      .backgroundColor(Color.Transparent);
    }
    .title('第二页')
    .width('100%')
    .height('100%');
  }
}
```
 
在src/main目录下的工程配置文件module.json5中的module字段里配置"routerMap": "$profile:router_map"，并在src/main/resources/base/profile目录下新增router_map.json。router_map.json示例如下。
 
```ArkTS
{
  "routerMap": [
    {
      "name": "SubPage",
      "pageSourceFile": "src/main/ets/pages/SubPage.ets",
      "buildFunction": "RegisterBuilder"
    }
  ]
}
```
