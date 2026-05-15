# 如何使用AbilityStage的生命周期函数

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-2

DevEco Studio默认工程未包含AbilityStage。若需使用AbilityStage功能，可手动创建AbilityStage文件。具体步骤如下：

1. 在工程Module对应的ets目录下，右键选择“New > Directory”，新建一个目录，命名为myabilitystage。
2. 在myabilitystage目录中，右键选择“New > ArkTS File”，新建一个文件并命名为MyAbilityStage.ets。
3. 打开MyAbilityStage.ets文件，导入AbilityStage的依赖包，自定义类继承AbilityStage并添加所需的生命周期回调。示例中添加了onCreate()生命周期回调。
```ts
import { AbilityStage, Want } from '@kit.AbilityKit';

export default class MyAbilityStage extends AbilityStage {
  onCreate(): void {
    // When the HAP of the application is first loaded, initialize the operation for the module
  }

  onAcceptWant(want: Want): string {
    // Triggered only when UIAbility is configured in specified startup mode
    return 'MyAbilityStage';
  }
}
```
4. 在[module.json5配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)中，通过配置 srcEntry 参数来指定模块对应的代码路径，以作为HAP加载的入口。
```json
{
  "module": {
    "name": "entry",
    "type": "entry",
    "srcEntry": "./ets/myabilitystage/MyAbilityStage.ets"
    // ...
  }
}
```


AbilityStage拥有onCreate()、onDestroy()生命周期回调和onAcceptWant()、onConfigurationUpdate()、onMemoryLevel()事件回调等。
