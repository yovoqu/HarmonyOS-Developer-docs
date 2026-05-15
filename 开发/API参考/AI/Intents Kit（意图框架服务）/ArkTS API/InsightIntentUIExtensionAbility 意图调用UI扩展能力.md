# InsightIntentUIExtensionAbility (意图调用UI扩展能力)

更新时间：2026-04-29 07:35:50

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/intents-arkts-api-insightintent-uiextension
**支持设备：** Phone / PC/2in1 / Tablet

InsightIntentUIExtensionAbility用于小艺对话过程中的意图调用时的信息展示，为意图调用UI扩展能力，应用可以声明一个或多个InsightIntentUI来展示其意图的窗口化界面，继承自[UIExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiextensionability)。

**起始版本：** 5.0.0(12)


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet


```text
import { InsightIntentUIExtensionAbility } from '@kit.IntentsKit';
```


## InsightIntentUIExtensionAbility
**支持设备：** Phone / PC/2in1 / Tablet

**模型约束：** 该类仅可在Stage模型下使用。

**系统能力：** SystemCapability.AI.InsightIntent

**起始版本：** 5.0.0(12)

**示例：**


```text
import { InsightIntentUIExtensionAbility } from '@kit.IntentsKit';
import { UIExtensionContentSession, Want } from '@kit.AbilityKit';

const TAG: string = 'TestUiExtAbility';

// 此处以TestUiExtAbility继承InsightIntentUIExtensionAbility为例
export default class TestUiExtAbility extends InsightIntentUIExtensionAbility {
onCreate() {
console.info(TAG, `onCreate`);
}
onForeground() {
console.info(TAG, `onForeground`);
}
onBackground() {
console.info(TAG, `onBackground`);
}
onDestroy() {
console.info(TAG, `onDestroy`);
}
onSessionCreate(want: Want, session: UIExtensionContentSession) {
console.info(TAG, `onSessionCreate, want: ${JSON.stringify(want)}`);
session.loadContent('pages/Index');
}
onSessionDestroy(session: UIExtensionContentSession) {
console.info(TAG, `onSessionDestroy`);
}
}
```
