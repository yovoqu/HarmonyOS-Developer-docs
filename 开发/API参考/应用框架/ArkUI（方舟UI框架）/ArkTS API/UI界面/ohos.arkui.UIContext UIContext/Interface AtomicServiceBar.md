# Interface (AtomicServiceBar)

更新时间：2026-04-28 03:31:56

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-atomicservicebar
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

提供设置元服务menuBar的属性。


## setVisible11+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setVisible(visible: boolean): void

通过该方法设置元服务menuBar是否可见。


> [!NOTE]
> 从API version 12开始，元服务menuBar默认隐藏并以悬浮按钮替代。**在元服务中调用setVisible()时，visible参数将被忽略，无法实现menuBar的显示或隐藏。**

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| visible | boolean | 是 | 元服务menuBar是否可见。true表示设置menuBar可见，false表示设置menuBar不可见。 |


**示例：**


```ts
import { UIAbility } from '@kit.AbilityKit';
import { UIContext, AtomicServiceBar, window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    // Main window is created, set main page for this ability
    hilog.info(0x0000, 'testTag', 'Ability onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err, data) => {
      let uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
      let atomicServiceBar: Nullable<AtomicServiceBar> =
        uiContext.getAtomicServiceBar();
      if (atomicServiceBar != undefined) {
        hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar Successfully.');
        atomicServiceBar.setVisible(false);
      } else {
        hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar failed.');
      }
    });
  }
}
```


## setBackgroundColor11+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setBackgroundColor(color:Nullable<Color | number | string>): void

通过该方法设置元服务menuBar的背景颜色。


> [!NOTE]
> 从API version 12开始，元服务menuBar背景默认隐藏。**在元服务中调用setBackgroundColor()时，color参数将被忽略，无法设置menuBar的背景颜色。**

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | Nullable&lt;[Color](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#color) \| number \| string&gt; | 是 | 通过该方法设置元服务menuBar的背景颜色，undefined代表使用默认颜色。number为HEX格式颜色，支持rgb或者argb，示例：0xffffff。string为rgb或者argb格式颜色，示例：'#ffffff'。 |


**示例：**


```ts
import { UIAbility } from '@kit.AbilityKit';
import { UIContext, AtomicServiceBar, window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    // Main window is created, set main page for this ability
    hilog.info(0x0000, 'testTag', 'Ability onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err, data) => {
      let uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
      let atomicServiceBar: Nullable<AtomicServiceBar> =
        uiContext.getAtomicServiceBar();
      if (atomicServiceBar != undefined) {
        hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar Successfully.');
        atomicServiceBar.setBackgroundColor(0x88888888);
      } else {
        hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar failed.');
      }
    });
  }
}
```


## setTitleContent11+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setTitleContent(content:string): void

通过该方法设置元服务menuBar的标题内容。


> [!NOTE]
> 从API version 12开始，元服务menuBar标题默认隐藏。**在元服务中调用setTitleContent()时，content参数将被忽略，无法设置menuBar的标题内容。**

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | string | 是 | 元服务menuBar中的标题内容。 |


**示例：**


```ts
import { UIAbility } from '@kit.AbilityKit';
import { UIContext, AtomicServiceBar, window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    // Main window is created, set main page for this ability
    hilog.info(0x0000, 'testTag', 'Ability onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err, data) => {
      let uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
      let atomicServiceBar: Nullable<AtomicServiceBar> =
        uiContext.getAtomicServiceBar();
      if (atomicServiceBar != undefined) {
        hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar Successfully.');
        atomicServiceBar.setTitleContent('text2');
      } else {
        hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar failed.');
      }
    });
  }
}
```


## setTitleFontStyle11+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setTitleFontStyle(font:FontStyle):void

通过该方法设置元服务menuBar的字体样式。


> [!NOTE]
> 从API version 12开始，元服务menuBar标题默认隐藏。**在元服务中调用setTitleFontStyle()时，font参数将被忽略，无法设置menuBar标题的字体样式，例如斜体显示。**

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full。

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| font | [FontStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#fontstyle) | 是 | 元服务menuBar中的字体样式。 |


**示例：**


```ts
import { UIAbility } from '@kit.AbilityKit';
import { UIContext, AtomicServiceBar, window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    // Main window is created, set main page for this ability
    hilog.info(0x0000, 'testTag', 'Ability onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err, data) => {
      let uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
      let atomicServiceBar: Nullable<AtomicServiceBar> =
        uiContext.getAtomicServiceBar();
      if (atomicServiceBar != undefined) {
        hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar Successfully.');
        atomicServiceBar.setTitleFontStyle(FontStyle.Normal);
      } else {
        hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar failed.');
      }
    });
  }
}
```


## setIconColor11+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setIconColor(color:Nullable<Color | number | string>): void

通过该方法设置元服务图标的颜色。


> [!NOTE]
> 从API version 12开始，元服务menuBar默认隐藏并以悬浮按钮替代。**在元服务中调用setIconColor()时，color参数将被忽略，无法设置menuBar图标颜色。**

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | Nullable&lt;[Color](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#color) \| number \| string&gt; | 是 | 元服务图标的颜色，undefined代表使用默认颜色。number为HEX格式颜色，支持rgb或者argb，示例：0xffffff。string为rgb或者argb格式颜色，示例：'#ffffff'。 |


**示例：**


```ts
import { UIAbility } from '@kit.AbilityKit';
import { UIContext, AtomicServiceBar, window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    // Main window is created, set main page for this ability
    hilog.info(0x0000, 'testTag', 'Ability onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err, data) => {
      let uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
      let atomicServiceBar: Nullable<AtomicServiceBar> =
        uiContext.getAtomicServiceBar();
      if (atomicServiceBar != undefined) {
        hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar Successfully.');
        atomicServiceBar.setIconColor(0x12345678);
      } else {
        hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar failed.');
      }
    });
  }
}
```


## getBarRect15+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getBarRect(): Frame

获取元服务menuBar相对窗口的布局信息。


> [!NOTE]
> 布局信息包含了元服务menuBar的左右margin。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**


| 类型 | 说明 |
| --- | --- |
| [Frame](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics#frame) | 元服务menuBar的大小和位置。 |


**示例：**


```ts
import { AtomicServiceBar } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  build() {
    Button("getBarRect")
    .onClick(() => {
      let uiContext: UIContext = this.getUIContext();
      let currentBar: Nullable<AtomicServiceBar> = uiContext.getAtomicServiceBar();
      if (currentBar != undefined) {
        let rect = currentBar.getBarRect();
        hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar Successfully. x:'
        + rect.x + ' y:' + rect.y + ' width:' + rect.width + ' height:' + rect.height);
      } else {
        hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar failed.');
      }
    })
  }
}
```
