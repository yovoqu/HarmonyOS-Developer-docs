# @ohos.selectionInput.SelectionPanel (划词面板)

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-selectioninput-selectionpanel
**支持设备：** PC/2in1

本模块提供划词面板的属性信息和类型。


## 导入模块
**支持设备：** PC/2in1


```ts
import { PanelInfo, PanelType } from '@kit.BasicServicesKit';
```


## PanelInfo
**支持设备：** PC/2in1

划词面板属性信息。

**系统能力：** SystemCapability.SelectionInput.Selection

**模型约束：** 此接口仅可在Stage模型下使用。


| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| panelType | [PanelType](#paneltype) | 否 | 否 | 划词面板类型。 |
| x | number | 否 | 否 | 划词面板左上角的x轴坐标，单位为px。 |
| y | number | 否 | 否 | 划词面板左上角的y轴坐标，单位为px。 |
| width | number | 否 | 否 | 划词面板宽度，单位为px。 |
| height | number | 否 | 否 | 划词面板高度，单位为px。 |


## PanelType
**支持设备：** PC/2in1

划词面板类型枚举。

**系统能力：** SystemCapability.SelectionInput.Selection

**模型约束：** 此接口仅可在Stage模型下使用。


| 名称 | 值 | 说明 |
| --- | --- | --- |
| MENU_PANEL | 1 | 菜单面板类型。 |
| MAIN_PANEL | 2 | 主面板类型。 |
