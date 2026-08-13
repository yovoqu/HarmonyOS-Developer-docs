# HarmonyOS应用中如何关闭深色模式

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-156

#### 问题现象

HarmonyOS深色模式支持关闭吗？是否可以在APP中不使用深色模式？
 
 

#### 背景知识

- [ApplicationContext.setColorMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-applicationcontext#applicationcontextsetcolormode11)方法可以自定义应用的颜色模式，官网案例参考：[深色模式适配](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-dark-mode-adaptation)。该案例内有详细说明如何实现深浅色模式适配以及如何取消或跟随系统的深浅色切换。
- [setColorMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#setcolormode18)方法可以将[ColorMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-configurationconstant#colormode)设置不同的枚举，开发者可以使用这些预置枚举设置或获取系统/应用的深浅色模式。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COLOR_MODE_NOT_SET | -1 | 表示未设置颜色模式。 |
| COLOR_MODE_DARK | 0 | 表示深色模式。 |
| COLOR_MODE_LIGHT | 1 | 表示浅色模式。 |

 
 

#### 解决方案
1. 应用主动设置深浅色模式的场景。如果应用调用[setColorMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#setcolormode18)接口主动设置了深浅色，则以接口效果优先。

  EntryAbility.ets文件示例参考如下：

  
```json
import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
    } catch (err) {
      hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
    }
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
    console.info(`${want} + ${launchParam}`);
  }

  onDestroy(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
 <em>   // Main window is created, set main page for this ability</em>
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
    });

    let applicationContext = this.context.getApplicationContext();
    applicationContext.setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_LIGHT); <em>//</em><em>主动设置深浅色模式</em>
  }


  onWindowStageDestroy(): void {
  <em>  // Main window is destroyed, release UI related resources</em>
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
  <em>  // Ability has brought to foreground</em>
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
  <em>  // Ability has back to background</em>
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
  }

}
```

2. 应用未主动设置深浅色模式的场景。
如果应用工程dark目录下有深色资源，则系统内置组件在深色模式下会自动切换成为深色。
3. 如果应用工程dark目录下没有任何深色资源，则系统内置组件在深色模式下仍会保持浅色体验。
 
 

#### 常见FAQ

Q：在没有调用[setColorMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#setcolormode18)接口的情况下，如何修改状态栏的颜色？
 
A：可以在EntryAbility.ets中修改状态栏的颜色。
 
```json
import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
    } catch (err) {
      hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
    }
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
    console.info(`${want} + ${launchParam}`);
  }

  onDestroy(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  async onWindowStageCreate(windowStage: window.WindowStage): Promise<void> {
  <em>  // Main window is created, set main page for this ability</em>
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
    });

    (await windowStage.getMainWindow()).setWindowSystemBarProperties({
    <em>  // 设置状态栏颜色为其他颜色</em>
      statusBarColor: '#ffa28d8f',
   <em>   // 设置状态栏文本颜色为白色</em>
      statusBarContentColor: '#ffe30520'
    });
  }


  onWindowStageDestroy(): void {
   <em> // Main window is destroyed, release UI related resources</em>
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
 <em>   // Ability has brought to foreground</em>
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
   <em> // Ability has back to background</em>
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
  }

}
```
