# 警告弹窗 (AlertDialog)

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-alert-dialog-box
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

显示警告弹窗组件，可设置文本内容与响应回调。

> [!TIP]
> 从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。 本模块功能依赖UI的执行上下文，不可在 UI上下文不明确 的地方使用，参见 UIContext 说明。



##### AlertDialogParam对象说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

警告弹窗的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | ResourceStr | 否 | 是 | 弹窗标题。 API version 20之前，弹窗标题的对齐方式为左对齐。 API version 20及之后，弹窗标题的对齐方式为居中对齐。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| subtitle10+ | ResourceStr | 否 | 是 | 弹窗副标题。 API version 20之前，弹窗副标题的对齐方式为左对齐。 API version 20及之后，弹窗副标题的对齐方式为居中对齐。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| message | ResourceStr | 否 | 否 | 弹窗内容。 API version 20之前，弹窗内容的对齐方式为左对齐。 API version 20及之后，弹窗内容的对齐方式为居中对齐。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| autoCancel | boolean | 否 | 是 | 点击遮障层时，是否关闭弹窗，true表示关闭弹窗。false表示不关闭弹窗。 默认值：true 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| cancel | VoidCallback | 否 | 是 | 点击遮障层关闭dialog时的回调。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| alignment | DialogAlignment | 否 | 是 | 弹窗在竖直方向上的对齐方式。 默认值：DialogAlignment.Default 元服务API： 从API version 11开始，该接口支持在元服务中使用。 说明： 若在UIExtension中设置showInSubWindow为true，弹窗将基于UIExtension的宿主窗口对齐。 |
| offset | Offset | 否 | 是 | 弹窗相对alignment所在位置的偏移量。 默认值：{ dx: 0 , dy: 0 } 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| gridCount | number | 否 | 是 | 弹窗容器宽度所占用栅格数。 默认值：4 取值范围：大于等于0的整数。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| maskRect10+ | Rectangle | 否 | 是 | 弹窗遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。 默认值：{ x: 0, y: 0, width: '100%', height: '100%' } 说明： showInSubWindow为true时，maskRect不生效。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| showInSubWindow11+ | boolean | 否 | 是 | 某弹窗需要显示在主窗口之外时，是否在子窗口显示此弹窗。值为true表示在子窗口显示弹窗。 默认值：false，弹窗显示在应用内，而非独立子窗口。 说明：showInSubWindow为true的弹窗无法触发显示另一个showInSubWindow为true的弹窗。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| isModal11+ | boolean | 否 | 是 | 弹窗是否为模态窗口，模态窗口有蒙层，非模态窗口无蒙层。值为false时，弹窗为非模态窗口，无蒙层。 默认值：true，此时弹窗有蒙层。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundColor11+ | ResourceColor | 否 | 是 | 弹窗背板颜色。 默认值：Color.Transparent 说明： backgroundColor会与模糊属性backgroundBlurStyle叠加产生效果，如果不符合预期，可将backgroundBlurStyle设置为BlurStyle.NONE，即可取消模糊。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundBlurStyle11+ | BlurStyle | 否 | 是 | 弹窗背板模糊材质。 默认值：BlurStyle.COMPONENT_ULTRA_THICK 说明： 设置为BlurStyle.NONE即可关闭背景虚化。当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，否则颜色显示将不符合预期效果。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundBlurStyleOptions19+ | BackgroundBlurStyleOptions | 否 | 是 | 背景模糊效果。默认值请参考BackgroundBlurStyleOptions类型说明。 元服务API： 从API version 19开始，该接口支持在元服务中使用。 |
| backgroundEffect19+ | BackgroundEffectOptions | 否 | 是 | 背景效果参数。默认值请参考BackgroundEffectOptions类型说明。 元服务API： 从API version 19开始，该接口支持在元服务中使用。 |
| onWillDismiss12+ | Callback&lt;DismissDialogAction&gt; | 否 | 是 | 交互式关闭回调函数。 说明： 1.当用户执行点击遮障层关闭、侧滑（左滑/右滑）、三键back、键盘ESC关闭交互操作时，如果注册该回调函数，则不会立刻关闭弹窗。在回调函数中可以通过reason得到阻拦关闭弹窗的操作类型，从而根据原因选择是否能关闭弹窗。当前组件返回的reason中，暂不支持CLOSE_BUTTON的枚举值。 2.在onWillDismiss回调中，不能再做onWillDismiss拦截。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| cornerRadius12+ | Dimension \| BorderRadiuses \| LocalizedBorderRadiuses | 否 | 是 | 设置背板的圆角半径。 可分别设置4个圆角的半径。 默认值：{ topLeft: '32vp', topRight: '32vp', bottomLeft: '32vp', bottomRight: '32vp' } 圆角大小受组件尺寸限制，最大值为组件宽或高的一半，若值为负，则按照默认值处理。 百分比参数方式：以父元素弹窗宽和高的百分比来设置弹窗的圆角。 说明： 当cornerRadius属性类型为LocalizedBorderRadiuses时，支持随语言习惯改变布局顺序。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| transition12+ | TransitionEffect | 否 | 是 | 设置弹窗显示和退出的过渡效果。 说明： 1.如果不设置，则使用默认的显示/退出动效。 2.显示动效中按back键，打断显示动效，执行退出动效，动画效果为显示动效与退出动效的曲线叠加后的效果。 3.退出动效中按back键，不会打断退出动效，退出动效继续执行，继续按back键退出应用。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| width12+ | Dimension | 否 | 是 | 设置弹窗背板的宽度。 说明： - 弹窗宽度默认最大值：400vp。 - 百分比参数方式：弹窗参考宽度为所在窗口的宽度，在此基础上调小或调大。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| height12+ | Dimension | 否 | 是 | 设置弹窗背板的高度。 说明： - 弹窗高度默认最大值：0.9 *（窗口高度 - 安全区域）。 - 百分比参数方式：弹窗参考高度为（窗口高度 - 安全区域），在此基础上调小或调大。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| borderWidth12+ | Dimension \| EdgeWidths \| LocalizedEdgeWidths | 否 | 是 | 可分别设置4个边框宽度。 默认值：0 百分比参数方式：以父元素弹窗宽的百分比来设置弹窗的边框宽度。 当弹窗左边框和右边框大于弹窗宽度，弹窗上边框和下边框大于弹窗高度，显示可能不符合预期。 说明： 当borderWidth属性类型为LocalizedEdgeWidths时，支持随语言习惯改变布局顺序。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| borderColor12+ | ResourceColor \| EdgeColors \| LocalizedEdgeColors | 否 | 是 | 设置弹窗背板的边框颜色。 默认值：Color.Black 如果使用borderColor属性，需要和borderWidth属性一起使用。 说明： 当borderColor属性类型为LocalizedEdgeColors时，支持随语言习惯改变布局顺序。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| borderStyle12+ | BorderStyle \| EdgeStyles | 否 | 是 | 设置弹窗背板的边框样式。 默认值：BorderStyle.Solid 如果使用borderStyle属性，需要和borderWidth属性一起使用。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| shadow12+ | ShadowOptions \| ShadowStyle | 否 | 是 | 设置弹窗背板的阴影。 当设备为2in1时，默认场景下获焦阴影值为ShadowStyle.OUTER_FLOATING_MD，失焦为ShadowStyle.OUTER_FLOATING_SM。其他设备默认无阴影。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| textStyle12+ | TextStyle | 否 | 是 | 设置弹窗message内容的文本样式。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| enableHoverMode14+ | boolean | 否 | 是 | 是否响应悬停态，值为true时，响应悬停态。 默认值：false，默认不响应。 说明： PC/2in1设备弹窗默认显示在上半屏，在enableHoverMode设置为true时，可以通过设置hoverModeArea参数显示在下半屏。其他设备弹窗在enableHoverMode设置为true时默认显示在下半屏，可以通过设置hoverModeArea参数显示在上半屏。 元服务API： 从API version 14开始，该接口支持在元服务中使用。 |
| hoverModeArea14+ | HoverModeAreaType | 否 | 是 | 悬停态下弹窗默认展示区域。 默认值：HoverModeAreaType.BOTTOM_SCREEN。 元服务API： 从API version 14开始，该接口支持在元服务中使用。 |
| onWillAppear19+ | Callback&lt;void&gt; | 否 | 是 | 弹窗显示动效前的事件回调。 说明： 1.正常时序依次为：onWillAppear >> onDidAppear >> onWillDisappear >> onDidDisappear。 2.在onWillAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。 元服务API： 从API version 19开始，该接口支持在元服务中使用。 |
| onDidAppear19+ | Callback&lt;void&gt; | 否 | 是 | 弹窗弹出后的事件回调。 说明： 1.正常时序依次为：onWillAppear >> onDidAppear >> onWillDisappear >> onDidDisappear。 2.在onDidAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。 3.快速点击弹出，关闭弹窗时，onWillDisappear在onDidAppear前生效。 4.弹窗入场动效未完成时彻底关闭弹窗，动效打断，onDidAppear不会触发。 元服务API： 从API version 19开始，该接口支持在元服务中使用。 |
| onWillDisappear19+ | Callback&lt;void&gt; | 否 | 是 | 弹窗退出动效前的事件回调。 说明： 正常时序依次为：onWillAppear >> onDidAppear >> onWillDisappear >> onDidDisappear。 元服务API： 从API version 19开始，该接口支持在元服务中使用。 |
| onDidDisappear19+ | Callback&lt;void&gt; | 否 | 是 | 弹窗消失后的事件回调。 说明： 正常时序依次为：onWillAppear >> onDidAppear >> onWillDisappear >> onDidDisappear。 元服务API： 从API version 19开始，该接口支持在元服务中使用。 |
| levelMode15+ | LevelMode | 否 | 是 | 设置弹窗显示层级。 说明： - 默认值：LevelMode.OVERLAY。 - 当且仅当showInSubWindow属性设置为false时生效。 元服务API： 从API version 15开始，该接口支持在元服务中使用。 |
| levelUniqueId15+ | number | 否 | 是 | 设置页面级弹窗需要显示的层级下的节点UniqueID。仅在levelMode属性设置为LevelMode.EMBEDDED时生效。 取值范围：大于等于0的数字。 元服务API： 从API version 15开始，该接口支持在元服务中使用。 |
| immersiveMode15+ | ImmersiveMode | 否 | 是 | 设置页面内弹窗蒙层效果。 说明： - 默认值：ImmersiveMode.DEFAULT - 当且仅当levelMode属性设置为LevelMode.EMBEDDED时生效。 元服务API： 从API version 15开始，该接口支持在元服务中使用。 |
| levelOrder18+ | LevelOrder | 否 | 是 | 设置弹窗显示的顺序。 说明： - 默认值：LevelOrder.clamp(0) - 不支持动态刷新顺序。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |




##### LevelOrder18+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

type LevelOrder = LevelOrder

弹窗的显示顺序。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| LevelOrder | 设置弹窗的显示顺序。 |




##### AlertDialogParamWithConfirm对象说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

继承自[AlertDialogParam](#alertdialogparam对象说明)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| confirm | AlertDialogButtonBaseOptions | 否 | 是 | 确认Button的使能状态、默认焦点、按钮风格、文本内容、文本色、按钮背景色和点击回调。在弹窗获焦且未进行tab键走焦时，该按钮默认响应Enter键。多重弹窗情况下，可自动获焦并连续响应。默认响应Enter键能力在defaultFocus为true时不生效。 |


confirm参数优先级：fontColor、backgroundColor > style > defaultFocus

| backgroundColor | fontColor | style | defaultFocus | 效果 |
| --- | --- | --- | --- | --- |
| 绿底 | 红字 | - | - | 绿底红字 |
| 绿底 | - | DialogButtonStyle.HIGHLIGHT | - | 绿底白字 |
| 绿底 | - | DialogButtonStyle.DEFAULT | - | 绿底蓝字 |
| 绿底 | - | - | TRUE | 绿底白字 |
| 绿底 | - | - | FALSE/- | 绿底蓝字 |
| - | 红字 | DialogButtonStyle.HIGHLIGHT | - | 蓝底红字 |
| - | 红字 | DialogButtonStyle.DEFAULT | - | 白底红字 |
| - | 红字 | - | TRUE | 蓝底红字 |
| - | 红字 | - | FALSE/- | 白底红字 |
| - | - | DialogButtonStyle.HIGHLIGHT | - | 蓝底白字 |
| - | - | DialogButtonStyle.DEFAULT | - | 白底蓝字 |
| - | - | - | TRUE | 蓝底白字 |
| - | - | - | FALSE/- | 白底蓝字 |




##### AlertDialogParamWithButtons对象说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

继承自[AlertDialogParam](#alertdialogparam对象说明)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| primaryButton | AlertDialogButtonBaseOptions | 否 | 否 | 主要Button的使能状态、默认焦点、按钮风格、文本内容、文本色、按钮背景色和点击回调。在弹窗获焦且未进行tab键走焦时，该按钮默认响应Enter键，且多重弹窗可自动获焦连续响应。默认响应Enter键能力在defaultFocus为true时不生效。 具体使用方式请参考示例7 。 |
| secondaryButton | AlertDialogButtonBaseOptions | 否 | 否 | 次要Button的使能状态、默认焦点、按钮风格、文本内容、文本色、按钮背景色和点击回调。 |




##### AlertDialogParamWithOptions10+对象说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

继承自[AlertDialogParam](#alertdialogparam对象说明)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| buttons | Array&lt;AlertDialogButtonOptions&gt; | 否 | 否 | 弹窗容器中的多个按钮。 |
| buttonDirection | DialogButtonDirection | 否 | 是 | 按钮排布方向默认为DialogButtonDirection.AUTO。建议3个以上按钮使用Auto模式（两个以上按钮会切换为纵向模式，通常能显示更多按钮）。非Auto模式下，3个以上按钮可能会显示不全，超出显示范围的按钮会被截断。 |




##### AlertDialogButtonOptions10+对象说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

继承自[AlertDialogButtonBaseOptions](#alertdialogbuttonbaseoptions18对象说明)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| primary12+ | boolean | 否 | 是 | 在弹窗获焦且未进行tab键走焦时，按钮是否默认响应Enter键。多个Button时，只允许一个Button的该字段配置为true，否则所有Button均不响应。多重弹窗可自动获焦连续响应。在defaultFocus为true时不生效。值为true表示按钮默认响应Enter键，值为false时，按钮不默认响应Enter键。 默认值：false 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |




##### AlertDialogButtonBaseOptions18+对象说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

警告弹窗中按钮的样式。

> [!NOTE]
> 为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。


**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enabled10+ | boolean | 否 | 是 | 点击Button是否响应，默认值true。 值为true时，Button可以响应。值为false时，Button不可以响应。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| defaultFocus10+ | boolean | 否 | 是 | 设置Button是否是默认焦点，默认值false。值为true表示Button为默认焦点，值为false表示Button不为默认焦点。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| style10+ | DialogButtonStyle | 否 | 是 | 设置Button的风格样式，默认值DialogButtonStyle.DEFAULT。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| value10+ | ResourceStr | 否 | 否 | Button的文本内容，若值为null，则该按钮不显示。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| fontColor10+ | ResourceColor | 否 | 是 | Button的文本颜色。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| backgroundColor10+ | ResourceColor | 否 | 是 | Button背景颜色。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| action10+ | VoidCallback | 否 | 否 | Button选中时的回调。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |




##### DialogButtonDirection10+枚举说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

警告弹窗中按钮的对齐方式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUTO | 0 | 两个及以下按钮水平排布，两个以上为竖直排布。 |
| HORIZONTAL | 1 | 按钮水平布局。 |
| VERTICAL | 2 | 按钮竖直布局。 |




##### DialogAlignment枚举说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

警告弹窗的对齐方式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Top | 0 | 垂直顶部对齐。 |
| Center | 1 | 垂直居中对齐。 |
| Bottom | 2 | 垂直底部对齐。 |
| Default | 3 | 默认对齐。 |
| TopStart8+ | 4 | 左上对齐。 |
| TopEnd8+ | 5 | 右上对齐。 |
| CenterStart8+ | 6 | 左中对齐。 |
| CenterEnd8+ | 7 | 右中对齐。 |
| BottomStart8+ | 8 | 左下对齐。 |
| BottomEnd8+ | 9 | 右下对齐。 |




##### Rectangle8+类型说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

Rectangle是各种Dialog中maskRect参数的类型。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | Length | 否 | 是 | 弹窗遮蔽层区域相对于窗口左上角的x轴坐标。 默认值：0vp |
| y | Length | 否 | 是 | 弹窗遮蔽层区域相对于窗口左上角的y轴坐标。 默认值：0vp |
| width | Length | 否 | 是 | 弹窗遮蔽层区域的宽度。 默认值：'100%' |
| height | Length | 否 | 是 | 弹窗遮蔽层区域的高度。 默认值：'100%' |


> [!NOTE]
> x和y可以设置正负值百分比。当x设置为'100%'时表示遮蔽层区域往右偏移窗口本身宽度大小，当x设置为'-100%'时表示遮蔽层区域往左偏移窗口本身宽度大小。当y设置为'100%'时表示遮蔽层区域往下偏移窗口本身高度大小，当y设置为'-100%'时表示遮蔽层区域往上偏移窗口本身高度大小。 width和height只能设置正值，支持百分比，如果设置为负值，那么该值将被重置为默认值。 百分比相对于窗口自身宽高进行计算。




##### DismissDialogAction12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

Dialog关闭的信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full



##### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dismiss | Callback&lt;void&gt; | 否 | 否 | Dialog关闭回调函数。开发者需要退出时调用，不需要退出时无需调用。 |
| reason | DismissReason | 否 | 否 | Dialog无法关闭原因。根据开发者需要选择不同操作下，Dialog是否需要关闭。 |




##### TextStyle12+对象说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

弹窗中message的截断方式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| wordBreak | WordBreak | 否 | 是 | 弹窗message内容的文本截断方式。 默认值：WordBreak.BREAK_ALL |




##### AlertDialog

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV



##### show(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

static show(value: AlertDialogParamWithConfirm | AlertDialogParamWithButtons | AlertDialogParamWithOptions)

定义警告弹窗并弹出。

> [!NOTE]
> 从API version 7开始支持，从API version 18开始废弃，建议使用 showAlertDialog 替代。showAlertDialog需先获取 UIContext 实例后再进行调用。 从API version 10开始，可以通过使用 UIContext 中的 showAlertDialog 来明确UI的执行上下文。


**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | AlertDialogParamWithConfirm \| AlertDialogParamWithButtons \| AlertDialogParamWithOptions10+ | 是 | 定义并显示AlertDialog组件。 |




##### 示例

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

> [!NOTE]
> 直接使用AlertDialog可能导致 UI上下文不明确 的问题，建议使用getUIContext()获取 UIContext 实例，并使用 showAlertDialog 调用绑定实例的AlertDialog.show()。




##### 示例1（弹出多个按钮的弹窗）

该示例通过[AlertDialogParamWithConfirm](#alertdialogparamwithconfirm对象说明)、[AlertDialogParamWithButtons](#alertdialogparamwithbuttons对象说明)和[AlertDialogParamWithOptions](#alertdialogparamwithoptions10对象说明)实现了分别弹出一、二、三个按钮的弹窗。

```ArkTS
// xxx.ets
@Entry
@Component
struct AlertDialogExample {
  build() {
    Column({ space: 5 }) {
      Button('one button dialog')
        .onClick(() => {
          this.getUIContext().showAlertDialog(
            {
              title: 'title',
              message: 'text',
              autoCancel: true,
              alignment: DialogAlignment.Bottom,
              offset: { dx: 0, dy: -20 },
              gridCount: 3,
              confirm: {
                value: 'button',
                action: () => {
                  console.info('Button-clicking callback');
                }
              },
              cancel: () => {
                console.info('Closed callbacks');
              },
              onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
                console.info(`reason= ${dismissDialogAction.reason}`);
                console.info('AlertDialog onWillDismiss');
                if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
                  dismissDialogAction.dismiss();
                }
                if (dismissDialogAction.reason === DismissReason.TOUCH_OUTSIDE) {
                  dismissDialogAction.dismiss();
                }
              }
            }
          )
        })
        .backgroundColor(0x317aff)
      Button('two button dialog')
        .onClick(() => {
          this.getUIContext().showAlertDialog(
            {
              title: 'title',
              subtitle: 'subtitle',
              message: 'text',
              autoCancel: true,
              alignment: DialogAlignment.Bottom,
              gridCount: 4,
              offset: { dx: 0, dy: -20 },
              primaryButton: {
                value: 'cancel',
                action: () => {
                  console.info('Callback when the first button is clicked');
                }
              },
              secondaryButton: {
                enabled: true,
                defaultFocus: true,
                style: DialogButtonStyle.HIGHLIGHT,
                value: 'ok',
                action: () => {
                  console.info('Callback when the second button is clicked');
                }
              },
              cancel: () => {
                console.info('Closed callbacks');
              },
              onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
                console.info(`reason= ${dismissDialogAction.reason}`);
                console.info('AlertDialog onWillDismiss');
                if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
                  dismissDialogAction.dismiss();
                }
                if (dismissDialogAction.reason === DismissReason.TOUCH_OUTSIDE) {
                  dismissDialogAction.dismiss();
                }
              }
            }
          )
        }).backgroundColor(0x317aff)
      Button('three button dialog')
        .onClick(() => {
          this.getUIContext().showAlertDialog(
            {
              title: 'title',
              subtitle: 'subtitle',
              message: 'text',
              autoCancel: true,
              alignment: DialogAlignment.Bottom,
              gridCount: 4,
              offset: { dx: 0, dy: -20 },
              buttonDirection: DialogButtonDirection.HORIZONTAL,
              buttons: [
                {
                  value: '按钮',
                  action: () => {
                    console.info('Callback when button1 is clicked');
                  }
                },
                {
                  value: '按钮',
                  action: () => {
                    console.info('Callback when button2 is clicked');
                  }
                },
                {
                  value: '按钮',
                  enabled: true,
                  defaultFocus: true,
                  style: DialogButtonStyle.HIGHLIGHT,
                  action: () => {
                    console.info('Callback when button3 is clicked');
                  }
                },
              ],
              cancel: () => {
                console.info('Closed callbacks');
              },
              onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
                console.info(`reason= ${dismissDialogAction.reason}`);
                console.info('AlertDialog onWillDismiss');
                if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
                  dismissDialogAction.dismiss();
                }
                if (dismissDialogAction.reason === DismissReason.TOUCH_OUTSIDE) {
                  dismissDialogAction.dismiss();
                }
              }
            }
          )
        }).backgroundColor(0x317aff)
    }.width('100%').margin({ top: 5 })
  }
}
```


![](assets/警告弹窗%20AlertDialog/file-20260514164132946-5.gif)




##### 示例2（可在主窗外弹出的弹窗）

在2in1设备上设置[AlertDialogParam](#alertdialogparam对象说明)中showInSubWindow属性的值为true时，可以弹出在主窗外显示的弹窗。

```ArkTS
// xxx.ets
@Entry
@Component
struct AlertDialogExample {
  build() {
    Column({ space: 5 }) {
      Button('one button dialog')
        .onClick(() => {
          this.getUIContext().showAlertDialog(
            {
              title: 'title',
              subtitle: 'subtitle',
              message: 'text',
              autoCancel: true,
              alignment: DialogAlignment.Center,
              gridCount: 4,
              showInSubWindow: true,
              isModal: true,
              offset: { dx: 0, dy: -20 },
              buttonDirection: DialogButtonDirection.HORIZONTAL,
              buttons: [
                {
                  value: '按钮',
                  action: () => {
                    console.info('Callback when button1 is clicked');
                  }
                },
                {
                  value: '按钮',
                  action: () => {
                    console.info('Callback when button2 is clicked');
                  }
                },
                {
                  value: '按钮',
                  enabled: true,
                  defaultFocus: true,
                  style: DialogButtonStyle.HIGHLIGHT,
                  action: () => {
                    console.info('Callback when button3 is clicked');
                  }
                },
              ],
              cancel: () => {
                console.info('Closed callbacks');
              },
              onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
                console.info(`reason= ${dismissDialogAction.reason}`);
                console.info('AlertDialog onWillDismiss');
                if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
                  dismissDialogAction.dismiss();
                }
                if (dismissDialogAction.reason === DismissReason.TOUCH_OUTSIDE) {
                  dismissDialogAction.dismiss();
                }
              }
            })
        })
    }.width('100%').margin({ top: 5 })
  }
}
```


![](assets/警告弹窗%20AlertDialog/file-20260514164132946-6.png)




##### 示例3（设置弹窗的动画）

该示例通过配置[AlertDialogParam](#alertdialogparam对象说明)中的transition属性来实现弹窗的显示和消失动画。

```ArkTS
// xxx.ets
@Entry
@Component
struct AlertDialogExample {
  build() {
    Column({ space: 5 }) {
      Button('AlertDialog Set Duration')
        .onClick(() => {
          this.getUIContext().showAlertDialog(
            {
              title: 'AlertDialog 1',
              message: 'Set Animation Duration open 3 second, close 100ms',
              autoCancel: true,
              alignment: DialogAlignment.Top,
              offset: { dx: 0, dy: -20 },
              gridCount: 3,
              transition: TransitionEffect.asymmetric(TransitionEffect.OPACITY
                .animation({ duration: 3000, curve: Curve.Sharp })
                .combine(TransitionEffect.scale({ x: 1.5, y: 1.5 }).animation({ duration: 3000, curve: Curve.Sharp })),
                TransitionEffect.OPACITY.animation({ duration: 100, curve: Curve.Smooth })
                  .combine(TransitionEffect.scale({ x: 0.5, y: 0.5 })
                    .animation({ duration: 100, curve: Curve.Smooth }))),
              confirm: {
                value: 'button',
                action: () => {
                  console.info('Button-clicking callback');
                }
              },
              cancel: () => {
                console.info('Closed callbacks');
              }
            }
          )
        })
        .backgroundColor(0x317aff).height('88px')
    }.width('100%').margin({ top: 5 })
  }
}
```


![](assets/警告弹窗%20AlertDialog/file-20260514164132946-7.png)




##### 示例4（设置弹窗的样式）

示例定义了AlertDialog的样式，包括宽度、高度、背景色、阴影等。

```ArkTS
// xxx.ets
@Entry
@Component
struct AlertDialogExample {
  build() {
    Column({ space: 5 }) {
      Button('one button dialog')
        .onClick(() => {
          this.getUIContext().showAlertDialog(
            {
              title: 'title',
              message: 'text',
              autoCancel: true,
              alignment: DialogAlignment.Center,
              offset: { dx: 0, dy: -20 },
              gridCount: 3,
              width: 300,
              height: 200,
              cornerRadius: 20,
              borderWidth: 1,
              borderStyle: BorderStyle.Dashed, // 使用borderStyle属性，需要和borderWidth属性一起使用
              borderColor: Color.Blue, // 使用borderColor属性，需要和borderWidth属性一起使用
              backgroundColor: Color.White,
              shadow: ({
                radius: 20,
                color: Color.Grey,
                offsetX: 50,
                offsetY: 0
              }),
              textStyle: { wordBreak: WordBreak.BREAK_ALL },
              confirm: {
                value: 'button',
                action: () => {
                  console.info('Button-clicking callback');
                }
              },
              cancel: () => {
                console.info('Closed callbacks');
              },
              onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
                console.info(`reason= ${dismissDialogAction.reason}`);
                console.info('AlertDialog onWillDismiss');
                if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
                  dismissDialogAction.dismiss();
                }
                if (dismissDialogAction.reason === DismissReason.TOUCH_OUTSIDE) {
                  dismissDialogAction.dismiss();
                }
              }
            }
          )
        })
        .backgroundColor(0x317aff)
    }.width('100%').margin({ top: 5 })
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/ILyLAPlnQqe4ZrOsghhkSQ/zh-cn_image_0000002581436172.gif?HW-CC-KV=V1&HW-CC-Date=20260528T024203Z&HW-CC-Expire=86400&HW-CC-Sign=67DADF59F9EC723F9C0BE051E5F63CFB1A28ACFDBE1F4FA4EA2F153E360D4CCB)




##### 示例5（悬停态弹窗）

该示例展示了在折叠屏悬停态下设置dialog布局区域的效果。

```ArkTS
// xxx.ets
@Entry
@Component
struct AlertDialogExample {
  build() {
    Column({ space: 5 }) {
      Button('one button dialog')
        .onClick(() => {
          this.getUIContext().showAlertDialog(
            {
              title: 'title',
              message: 'text',
              autoCancel: true,
              alignment: DialogAlignment.Bottom,
              gridCount: 3,
              confirm: {
                value: 'button',
                action: () => {
                  console.info('Button-clicking callback');
                }
              },
              cancel: () => {
                console.info('Closed callbacks');
              },
              onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
                console.info(`reason= ${dismissDialogAction.reason}`);
                console.info('AlertDialog onWillDismiss');
                if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
                  dismissDialogAction.dismiss();
                }
                if (dismissDialogAction.reason === DismissReason.TOUCH_OUTSIDE) {
                  dismissDialogAction.dismiss();
                }
              },
              enableHoverMode: true,
              hoverModeArea: HoverModeAreaType.TOP_SCREEN
            }
          )
        })
        .backgroundColor(0x317aff)
    }.width('100%').margin({ top: 5 })
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/7mjagJ6xTjaBEs2kNXJiGQ/zh-cn_image_0000002611836003.gif?HW-CC-KV=V1&HW-CC-Date=20260528T024203Z&HW-CC-Expire=86400&HW-CC-Sign=0AD245B8E711CD8FC5ED7AC56B92109CC0D8011724E562604A893A514D4F05AF)




##### 示例6（弹窗生命周期）

该示例展示了弹窗生命周期的相关接口的使用方法。

```ArkTS
// xxx.ets
@Entry
@Component
struct Example2 {
  @State log: string = 'Log information:';

  build() {
    Column({ space: 5 }) {
      Button('AlertDialog')
        .onClick(() => {
          this.getUIContext().showAlertDialog({
            title: 'AlertDialog',
            message: 'message',
            autoCancel: true,
            alignment: DialogAlignment.Bottom,
            offset: { dx: 0, dy: -20 },
            confirm: {
              value: 'button',
              action: () => {
                console.info('AlertDialog Button-clicking callback');
              }
            },
            cancel: () => {
              console.info('Closed callbacks');
            },
            onDidAppear: () => {
              this.log += '# onDidAppear';
              console.info('AlertDialog,is onDidAppear!');
            },
            onDidDisappear: () => {
              this.log += '# onDidDisappear';
              console.info('AlertDialog,is onDidDisappear!');
            },
            onWillAppear: () => {
              this.log = 'Log information:onWillAppear';
              console.info('AlertDialog,is onWillAppear!');
            },
            onWillDisappear: () => {
              this.log += '# onWillDisappear';
              console.info('AlertDialog,is onWillDisappear!');
            }
          })
        })
      Text(this.log).fontSize(30).margin({ top: 200 })
    }.width('100%').margin({ top: 5 })
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/_y24HFxQTLWWe4Gb8PjrMA/zh-cn_image_0000002581276256.gif?HW-CC-KV=V1&HW-CC-Date=20260528T024203Z&HW-CC-Expire=86400&HW-CC-Sign=95D2BA345C7E72C800F8B4C5BC5AC3FABFA8CB7F4807C7358985F3414026DCD5)




##### 示例7（自定义背景模糊效果参数）

该示例通过配置[AlertDialogParam](#alertdialogparam对象说明)中的backgroundBlurStyleOptions属性，实现了自定义背景模糊效果。

从API version 19开始，在AlertDialogParam中新增了backgroundBlurStyleOptions属性。

```text
@Entry
@Component
struct AlertDialogExample {
  build() {
    Stack({ alignContent: Alignment.Top }) {
      // $r('app.media.bg')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.bg'))
      Column() {
        Button("AlertDialog")
          .margin(20)
          .onClick(() => {
            this.getUIContext().showAlertDialog({
              title: 'AlertDialog Title',
              message: 'AlertDialog Text',
              primaryButton: {
                value: '确定',
                action: () => {
                  console.info('primaryButton');
                }
              },
              secondaryButton: {
                value: '取消',
                action: () => {
                  console.info('secondaryButton');
                }
              },
              backgroundColor: undefined,
              backgroundBlurStyle: BlurStyle.Thin,
              backgroundBlurStyleOptions: {
                colorMode: ThemeColorMode.LIGHT,
                adaptiveColor: AdaptiveColor.AVERAGE,
                scale: 1,
                blurOptions: { grayscale: [20, 20] },
              },
            });
          })
      }.width('100%')
    }
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/zxZikaQlToSEm4jZmfBmmg/zh-cn_image_0000002611756111.png?HW-CC-KV=V1&HW-CC-Date=20260528T024203Z&HW-CC-Expire=86400&HW-CC-Sign=83AE68056A508DDFA444A52C9458D903F5C0BC5107F551FA9329E6DD5E46AE81)




##### 示例8（自定义背景效果参数）

该示例通过配置[AlertDialogParam](#alertdialogparam对象说明)中的backgroundEffect属性，实现自定义背景效果。

从API version 19开始，在AlertDialogParam中新增了backgroundEffect属性。

```text
@Entry
@Component
struct AlertDialogExample {
  build() {
    Stack({ alignContent: Alignment.Top }) {
      // $r('app.media.bg')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.bg'))
      Column() {
        Button("AlertDialog")
          .margin(20)
          .onClick(() => {
            this.getUIContext().showAlertDialog({
              title: 'AlertDialog Title',
              message: 'AlertDialog Text',
              primaryButton: {
                value: '确定',
                action: () => {
                  console.info('primaryButton');
                }
              },
              secondaryButton: {
                value: '取消',
                action: () => {
                  console.info('secondaryButton');
                }
              },
              backgroundColor: undefined,
              backgroundBlurStyle: BlurStyle.Thin,
              backgroundEffect: {
                radius: 60,
                saturation: 0,
                brightness: 1,
                color: Color.White,
                blurOptions: { grayscale: [20, 20] }
              },
            });
          })
      }.width('100%')
    }
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/ep_HVjW7QqiRz8z5ttexfQ/zh-cn_image_0000002581436174.png?HW-CC-KV=V1&HW-CC-Date=20260528T024203Z&HW-CC-Expire=86400&HW-CC-Sign=84433C34516EECD7F22C8A13F67A0AC482170A262CBEAE094C524E53B75BFD85)
