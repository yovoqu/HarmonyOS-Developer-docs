# 使用HMRouter跳转后Radio无法保持选中状态

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-845

#### 问题现象

使用HMRouter跳转其他组件再返回，当前组件Radio未保持选中状态，问题代码如下：
 
- 终端中执行ohpm命令安装HMRouter。
```text
ohpm install @hadss/hmrouter
```

- 配置编译插件，修改工程根目录下的hvigor/hvigor-config.json5文件，加入路由编译插件。
```json
{
  "dependencies": {
    "@hadss/hmrouter-plugin": "^1.2.0"  <em>// 使用npm仓版本号</em>
  },
}
```

- 修改工程根目录下的hvigorfile.ts，使用路由编译插件。
```text
<em>// 工程根目录/hvigorfile.ts</em>
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { appPlugin } from '@hadss/hmrouter-plugin';

export default {
  system: appTasks,
  plugins: [appPlugin({ ignoreModuleNames: [ /** 不需要扫描的模块 **/ ] })]
};
```

- 在UIAbility中初始化路由框架。
```text
export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    <em>// 日志开启需在init之前调用，否则会丢失初始化日志</em>
    HMRouterMgr.openLog('INFO')
    HMRouterMgr.init({
      context: this.context
    })
  }
}
```


 
```ArkTS
<em>// Index.ets</em>
import { HMDefaultGlobalAnimator, HMNavigation, HMRouterMgr } from '@hadss/hmrouter';
import { AttributeUpdater } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  modifier: NavModifier = new NavModifier();

  build() {
    Column() {
      HMNavigation({
        navigationId: 'mainNavigation', options: {
          standardAnimator: HMDefaultGlobalAnimator.STANDARD_ANIMATOR,
          dialogAnimator: HMDefaultGlobalAnimator.DIALOG_ANIMATOR,
          modifier: this.modifier
        }
      }) {

        Column({ space: 20 }) {
          Row() {
            Radio({ value: '1', group: 'radioGroup' })
              .checked(true)
              .radioStyle({
                checkedBackgroundColor: '#OD5AF5'
              })
              .height(20)
              .width('5%')
          }

          Row() {
            Radio({ value: '1', group: 'radioGroup' })
              .checked(false)
              .radioStyle({
                checkedBackgroundColor: '#OD5AF5'
              })
              .height(20)
              .width('5%')
          }

          Button('click')
            .onClick(() => {
              HMRouterMgr.push({
                navigationId: 'mainNavigation',
                pageUrl: 'TwoPage'
              })
            })
        }.justifyContent(FlexAlign.Center)
        .width('100%')
        .height('100%')
      }
    }
    .height('100%')
    .width('100%')
  }
}

class NavModifier extends AttributeUpdater<NavigationAttribute> {
  initializeModifier(instance: NavigationAttribute): void {
    instance.mode(NavigationMode.Stack);
    instance.navBarWidth('100%');
  }
}
```
 
```ArkTS
<em>// TwoPage.ets</em>
import { HMRouter, HMRouterMgr } from '@hadss/hmrouter'

@HMRouter({ pageUrl: 'TwoPage' })
@Component
export struct TwoPage {
  @State isShow: boolean = true

  build() {
    Column({ space: 20 }) {
      Row() {
        Radio({ value: '2', group: 'radioGroup' })
          .checked(this.isShow)
          .radioStyle({
            checkedBackgroundColor: Color.Green
          })
          .height(20)
          .width(20)
          .margin({ bottom: '10px' })
          .onChange((isChecked: boolean) => {
            if (isChecked) {
            }
          })

      }.margin(10);

      Button('Back')
        .width('80%')
        .onClick(() => {
          this.isShow = false
          HMRouterMgr.pop({
            navigationId: 'mainNavigation',
          })
        })
    }.justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%')
  }
}
```
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/TMkDsQxbSuuOOTlpRymQ9w/zh-cn_image_0000002658917857.png?HW-CC-KV=V1&HW-CC-Date=20260811T005654Z&HW-CC-Expire=86400&HW-CC-Sign=0EDFE4D5C87E4B13E432BCBCC93B762BDBEE8BE495A5F4CDA3C843EC2D503946)

 
 

#### 背景知识

- [HMRouter](https://gitee.com/harmonyos_samples/HMRouter)：HMRouter底层对系统Navigation进行封装，集成了Navigation、NavDestination、NavPathStack的系统能力，提供了可复用的路由拦截、页面生命周期、自定义转场动画，并且在跳转传参、额外的生命周期、服务型路由方面对系统能力进行了扩展。
- [Radio](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-radio-button)：Radio是单选框组件，通常用于提供相应的用户交互选择项，同一组的Radio中只有一个可以被选中。

 
 

#### 问题定位

根据RadioOptions的group的描述，相同group的Radio只能有一个被选中，观察上述代码虽然处于不同组件但group一致。
 
 

#### 分析结论

HMRouter基于Navigation封装属于组件路由，而RadioOptions的group是缓存在页面中的，所以当两个组件中的Radio的group一致时会相互影响。
 
 

#### 修改建议

修改两个组件中的group为不同值即可解决问题。完整代码如下：
 
```text
import { HMDefaultGlobalAnimator, HMNavigation, HMRouterMgr } from '@hadss/hmrouter';
import { AttributeUpdater } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  modifier: NavModifier = new NavModifier();

  build() {
    Column() {
      HMNavigation({
        navigationId: 'mainNavigation', options: {
          standardAnimator: HMDefaultGlobalAnimator.STANDARD_ANIMATOR,
          dialogAnimator: HMDefaultGlobalAnimator.DIALOG_ANIMATOR,
          modifier: this.modifier
        }
      }) {

        Column({ space: 20 }) {
          Row() {
            Radio({ value: '1', group: 'radioGroup' })
              .checked(true)
              .radioStyle({
                checkedBackgroundColor: '#0D5AF5'
              })
              .height(20)
              .width('5%');
          };

          Row() {
            Radio({ value: '1', group: 'radioGroup' })
              .checked(false)
              .radioStyle({
                checkedBackgroundColor: '#0D5AF5'
              })
              .height(20)
              .width('5%');
          };

          Button('click')
            .onClick(() => {
              HMRouterMgr.push({
                navigationId: 'mainNavigation',
                pageUrl: 'TwoPage'
              });
            });
        }.justifyContent(FlexAlign.Center)
        .width('100%')
        .height('100%');
      };
    }
    .height('100%')
    .width('100%');
  }
}

class NavModifier extends AttributeUpdater<NavigationAttribute> {
  initializeModifier(instance: NavigationAttribute): void {
    instance.mode(NavigationMode.Stack);
    instance.navBarWidth('100%');
  }
}
```
 
```text
import { HMRouter, HMRouterMgr } from '@hadss/hmrouter';

@HMRouter({ pageUrl: 'TwoPage' })
@Component
export struct TwoPage {
  @State isShow: boolean = true;

  build() {
    Column({ space: 20 }) {
      Row() {
        Radio({ value: '2', group: 'radioGroup1' })
          .checked(this.isShow)
          .radioStyle({
            checkedBackgroundColor: Color.Green
          })
          .height(20)
          .width(20)
          .margin({ bottom: '10px' })
          .onChange((isChecked: boolean) => {
            if (isChecked) {
            }
          });

      }.margin(10);

      Button('Back')
        .width('80%')
        .onClick(() => {
          this.isShow = false;
          HMRouterMgr.pop({
            navigationId: 'mainNavigation',
          });
        });
    }.justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%');
  }
}
```
