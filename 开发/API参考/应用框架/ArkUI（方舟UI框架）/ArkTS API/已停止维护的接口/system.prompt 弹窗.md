# @system.prompt (弹窗)

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-prompt
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

创建并显示文本提示框、对话框和操作菜单。


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```ts
import prompt from '@system.prompt';
```


## prompt.showToast
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

showToast(options: ShowToastOptions): void

显示文本弹窗。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ShowToastOptions](#showtoastoptions) | 是 | 定义ShowToast的选项。 |


**示例：**


```ts
import prompt from '@system.prompt';
class A {
  showToast() {
    prompt.showToast({
      message: 'Message Info',
      duration: 2000,
    });
  }
}
export default new A();
```


## prompt.showDialog
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

showDialog(options: ShowDialogOptions): void

显示对话框。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ShowDialogOptions](#showdialogoptions) | 是 | 定义显示对话框的选项。 |


**示例：**


```ts
import prompt from '@system.prompt';
class B {
  showDialog() {
    prompt.showDialog({
      title: 'Title Info',
      message: 'Message Info',
      buttons: [
        {
          text: 'button',
          color: '#666666',
        },
      ],
      success: (data) => {
        console.info('dialog success callback，click button : ' + data.index);
      },
      cancel: () => {
        console.info('dialog cancel callback');
      },
    });
  }
}
export default new B();
```


## prompt.showActionMenu6+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

showActionMenu(options: ShowActionMenuOptions): void

显示操作菜单。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ShowActionMenuOptions](#showactionmenuoptions6) | 是 | 定义ShowActionMenu的选项。 |


**示例：**


```ts
import prompt from '@system.prompt';
class C {
  showActionMenu() {
    prompt.showActionMenu({
      title: 'Title Info',
      buttons: [
        {
          text: 'item1',
          color: '#666666',
        },
        {
          text: 'item2',
          color: '#000000',
        },
      ],
      success: (tapIndex) => {
        console.info('dialog success callback，click button : ' + tapIndex);
      },
      fail: (errMsg) => {
        console.info('dialog fail callback' + errMsg);
      },
    });
  }
}
export default new C();
```


## ShowToastOptions
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

定义ShowToast的选项。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 是 | 显示的文本信息。 |
| duration | number | 否 | 默认值1500ms，建议区间：1500ms-10000ms。若小于1500ms则取默认值，最大取值为10000ms。 |
| bottom5+ | string\|number | 否 | 设置弹窗边框距离屏幕底部的位置。 |


## Button
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

定义按钮的提示信息。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 定义按钮信息。 |
| color | string | 是 | 定义按钮颜色。 |


## ShowDialogSuccessResponse
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

定义ShowDialog的响应。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 定义数据的索引信息。 |


## ShowDialogOptions
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

定义显示对话框的选项。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| title | string | 否 | 标题文本。 |
| message | string | 否 | 文本内容。 |
| buttons | [[Button](#button), [Button](#button)?, [Button](#button)?] | 否 | 对话框中按钮的数组，结构为：{text:'button', color: '#666666'}，支持1-6个按钮。大于6个按钮时弹窗不显示。 |
| success | (data: [ShowDialogSuccessResponse](#showdialogsuccessresponse)) =&gt; void | 否 | 接口调用成功的回调函数。 |
| cancel | (data: string, code: string) =&gt; void | 否 | 接口调用失败的回调函数。 |
| complete | (data: string) =&gt; void | 否 | 接口调用结束的回调函数。 |


## ShowActionMenuOptions6+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

定义ShowActionMenu的选项。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| title | string | 否 | 标题文本。 |
| buttons | [[Button](#button), [Button](#button)?, [Button](#button)?, [Button](#button)?, [Button](#button)?, [Button](#button)?] | 是 | 对话框中按钮的数组，结构为：{text:'button', color: '#666666'}，支持1-6个按钮。 |
| success | (tapIndex: number, errMsg: string) =&gt; void | 否 | 弹出对话框时调用。 |
| fail | (errMsg: string) =&gt; void | 否 | 接口调用失败的回调函数。 |
| complete | (data: string) =&gt; void | 否 | 关闭对话框时调用。 |
