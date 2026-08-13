# native_type.h

更新时间：2026-08-11 11:13:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

提供NativeModule公共的类型定义。

**引用文件：** <arkui/native_type.h>

**库：** libace_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)

**相关示例：** [NativeTypeSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeTypeSample)



#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV



#### 结构体

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ArkUI_Node | - | 定义ArkUI Native组件实例对象，供ArkUI_NodeHandle指针在Native接口中标识和传递组件实例。 |
| ArkUI_ContextCallback | ArkUI_ContextCallback | 事件回调类型，用于定义回调函数及其用户自定义数据。使用该类型的接口触发回调时，会调用callback，并将userData作为参数传入。 |
| ArkUI_NumberValue | ArkUI_NumberValue | ArkUI 在 Native 侧使用的数字类型，用于通过统一类型承载浮点、有符号整型和无符号整型数值。 |
| ArkUI_ColorStop | ArkUI_ColorStop | 定义渐变色结构，用于配置组件的渐变效果，支持通过颜色数组与位置数组组合定义多种渐变样式。 |
| ArkUI_Rect | ArkUI_Rect | 定义遮罩屏蔽区域的范围结构体。 |
| ArkUI_IntSize | ArkUI_IntSize | 尺寸类型，用于描述组件的宽高。 |
| ArkUI_IntOffset | ArkUI_IntOffset | 偏移量，用于描述当前组件相对于父组件的位置。 |
| ArkUI_NativeDialog | - | 提供ArkUI在Native侧的自定义弹窗控制器对象定义。 |
| ArkUI_LayoutConstraint | ArkUI_LayoutConstraint | 布局约束，用于组件布局时进行尺寸范围限制。支持设置最小尺寸和最大尺寸约束，约束值为非负浮点数，在组件布局时，系统会根据约束值限定组件的最终尺寸范围，确保布局结果符合约束条件。适用于自定义布局容器时控制子组件的尺寸范围，如瀑布流布局中限制图片卡片的高度、网格布局中限制单元格尺寸，以及需要限制组件尺寸上下限的场景，如图片展示组件限制最大宽度防止拉伸、响应式布局中限制最小尺寸保证可读性。防止组件尺寸超出预期范围，实现更精确的布局控制，提高布局的可预测性和稳定性，增强界面的可控性。 |
| ArkUI_DrawContext | ArkUI_DrawContext | 定义组件绘制上下文类型结构，用于在自定义组件绘制过程中提供绘制上下文信息，可获取用于绘制的Canvas指针和可绘制区域大小。 |
| ArkUI_Node* | ArkUI_NodeHandle | 定义 ArkUI Native 组件实例对象指针，用于在 ArkUI Native 接口中标识和传递组件实例，例如创建、挂载、移除或销毁组件节点。 |
| ArkUI_NativeDialog* | ArkUI_NativeDialogHandle | 定义ArkUI在Native侧的自定义弹窗控制器对象指针。 |
| ArkUI_GestureCollectInterceptInfo | ArkUI_GestureCollectInterceptInfo | 定义手势收集拦截信息。 |
| ArkUI_ListItemSwipeActionItem | ArkUI_ListItemSwipeActionItem | 定义ListItemSwipeActionOption方法内Item的配置信息。 |
| ArkUI_ListItemSwipeActionOption | ArkUI_ListItemSwipeActionOption | 定义ListItemSwipeActionOption方法的配置信息。 |
| ArkUI_Context | ArkUI_Context | ArkUI native UI 的上下文实例对象，用于表示组件所在页面的 UIContext。其指针类型为 ArkUI_ContextHandle，开发者可通过 OH_ArkUI_GetContextByNode 获取对应上下文，并将其作为拖拽操作、动画、UI 任务调度等接口的上下文入参。 |
| ArkUI_Context* | ArkUI_ContextHandle | ArkUI 在 Native 侧的上下文实例对象指针，用于表示组件所在页面的 UIContext。开发者可通过OH_ArkUI_GetContextByNode或OH_ArkUI_GetContextFromNapiValue获取该指针，并将其作为 UI 任务调度、动画、焦点控制等接口的上下文入参。 |
| ArkUI_NodeContent* | ArkUI_NodeContentHandle | 定义ArkUI_NodeContent在Native侧的实例对象指针，用于在Native接口中引用和传递NodeContent实例。 |
| ArkUI_CustomProperty | ArkUI_CustomProperty | 定义自定义属性的ArkUI_CustomProperty结构体信息，用于表示组件的自定义属性。通过相关接口，可以为ArkUI组件添加、移除、获取自定义属性，并获取自定义属性的字符串值。 |
| ArkUI_HostWindowInfo | ArkUI_HostWindowInfo | 定义窗口属性的HostWindowInfo类信息。 |
| ArkUI_ActiveChildrenInfo | ArkUI_ActiveChildrenInfo | 定义ArkUI_ActiveChildrenInfo结构体，用于保存内部活跃状态为true的FrameNode子节点信息，支持查询子节点数量和按下标获取子节点。该结构体实例由OH_ArkUI_NodeUtils_GetActiveChildrenInfo生成，使用完毕后必须调用OH_ArkUI_ActiveChildrenInfo_Destroy销毁。 |
| ArkUI_CrossLanguageOption | ArkUI_CrossLanguageOption | 定义跨语言配置项，用于配置目标节点的跨语言访问能力，例如是否允许跨语言修改属性；从API version 26.0.0开始，还可配置节点树跨语言操作状态。 |
| ArkUI_AccessibilityState | ArkUI_AccessibilityState | 定义组件无障碍状态。 |
| ArkUI_AccessibilityValue | ArkUI_AccessibilityValue | 定义组件无障碍信息值。 |
| ArkUI_SystemFontStyleEvent | ArkUI_SystemFontStyleEvent | 系统字体样式变更事件定义，用于在系统字体大小或字体粗细发生变化时，向已注册的系统字体样式变更回调传递事件信息。 |
| ArkUI_SelectionOptions | ArkUI_SelectionOptions | 定义ArkUI中选择操作的配置选项，适用于应用内需要进行选择交互的场景，为开发者提供选择行为的定制能力。 |
| ArkUI_ContentTransitionEffect | ArkUI_ContentTransitionEffect | 内容过渡效果。 |
| ArkUI_SelectedDragPreviewStyle | ArkUI_SelectedDragPreviewStyle | 定义选中状态下文本拖拽预览样式，适用于需要在文本拖拽过程中展示选中状态预览效果的场景，可提升用户的拖拽交互体验。 |
| OH_ArkUI_LinearGradientOptions | OH_ArkUI_LinearGradientOptions | 定义线性渐变效果选项，用于描述UI组件的线性颜色渐变配置，支持设置渐变方向、角度和颜色配置，帮助开发者实现灵活的线性渐变效果，提升UI视觉呈现能力，适用于需要为组件应用线性渐变样式的场景 |
| OH_ArkUI_RadialGradientOptions | OH_ArkUI_RadialGradientOptions | 定义径向渐变选项，适用于UI组件中实现径向渐变效果的场景，可帮助开发者丰富界面的视觉层次。 |




#### 枚举

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ArkUI_CopyOptions | ArkUI_CopyOptions | 定义文本复制粘贴模式枚举值。 |
| ArkUI_AccessibilityCheckedState | ArkUI_AccessibilityCheckedState | 定义无障碍复选框状态类型枚举值。 |
| ArkUI_AccessibilityActionType | ArkUI_AccessibilityActionType | 定义无障碍操作类型。 |
| ArkUI_BorderStyle | ArkUI_BorderStyle | 边框线条样式枚举值。 |
| ArkUI_AccessibilityMode | ArkUI_AccessibilityMode | 定义无障碍辅助服务模式。 |
| ArkUI_AdaptiveColor | ArkUI_AdaptiveColor | 定义取色模式。 |
| ArkUI_ColorMode | ArkUI_ColorMode | 定义深浅色模式。 |
| ArkUI_SystemColorMode | ArkUI_SystemColorMode | 定义系统深浅色模式。 |
| ArkUI_LengthMetricUnit | ArkUI_LengthMetricUnit | 定义组件的单位模式。 |
| ArkUI_ListItemSwipeActionState | ArkUI_ListItemSwipeActionState | 定义Listitem组件swipeAction方法的显隐模式。 |
| ArkUI_ListItemSwipeEdgeEffect | ArkUI_ListItemSwipeEdgeEffect | 定义Listitem组件swipeAction方法的滚动模式。 |
| ArkUI_ListItemSwipeActionDirection | ArkUI_ListItemSwipeActionDirection | ListItem划出菜单的展开方向。 |
| ArkUI_SafeAreaType | ArkUI_SafeAreaType | 定义扩展安全区域的枚举值。 |
| ArkUI_KeyboardAvoidMode | ArkUI_KeyboardAvoidMode | 键盘避让模式。 |
| ArkUI_HoverModeAreaType | ArkUI_HoverModeAreaType | 悬停态显示区域。 |
| ArkUI_ExpandMode | ArkUI_ExpandMode | 定义子节点展开模式枚举值。 |
| ArkUI_FocusWrapMode | ArkUI_FocusWrapMode | 组件走焦换行规则。 |
| ArkUI_ItemFillPolicy | ArkUI_ItemFillPolicy | 为不同响应式断点规格指定列数。 |
| ArkUI_EdgeDirection | ArkUI_EdgeDirection | 定义矩形边方向。 |
| ArkUI_CornerDirection | ArkUI_CornerDirection | 定义角度方向。 |
| ArkUI_MenuPolicy | ArkUI_MenuPolicy | 菜单弹出策略。 |
| ArkUI_RenderStrategy | ArkUI_RenderStrategy | 定义组件绘制圆角的模式。 |
| OH_ArkUI_CrossLanguageOperatingStatus | OH_ArkUI_CrossLanguageOperatingStatus | 跨语言配置项的节点树操作状态。 |
| OH_ArkUI_NodeMountPolicy | OH_ArkUI_NodeMountPolicy | 子节点挂载策略类型枚举。 |




#### 函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ArkUI_LayoutConstraint* OH_ArkUI_LayoutConstraint_Create() | - | 创建布局约束。 |
| ArkUI_LayoutConstraint* OH_ArkUI_LayoutConstraint_Copy(const ArkUI_LayoutConstraint* Constraint) | - | 布局约束深拷贝。 |
| void* OH_ArkUI_LayoutConstraint_Dispose(ArkUI_LayoutConstraint* Constraint) | - | 销毁布局约束指针。 |
| int32_t OH_ArkUI_LayoutConstraint_GetMaxWidth(const ArkUI_LayoutConstraint* Constraint) | - | 通过布局约束获取最大宽度，单位为px。 |
| int32_t OH_ArkUI_LayoutConstraint_GetMinWidth(const ArkUI_LayoutConstraint* Constraint) | - | 通过布局约束获取最小宽度，单位为px。 |
| int32_t OH_ArkUI_LayoutConstraint_GetMaxHeight(const ArkUI_LayoutConstraint* Constraint) | - | 通过布局约束获取最大高度，单位为px。 |
| int32_t OH_ArkUI_LayoutConstraint_GetMinHeight(const ArkUI_LayoutConstraint* Constraint) | - | 通过布局约束获取最小高度，单位为px。 |
| int32_t OH_ArkUI_LayoutConstraint_GetPercentReferenceWidth(const ArkUI_LayoutConstraint* Constraint) | - | 通过布局约束获取宽度百分比基准。 |
| int32_t OH_ArkUI_LayoutConstraint_GetPercentReferenceHeight(const ArkUI_LayoutConstraint* Constraint) | - | 通过布局约束获取高度百分比基准。 |
| void OH_ArkUI_LayoutConstraint_SetMaxWidth(ArkUI_LayoutConstraint* Constraint, int32_t value) | - | 设置最大宽度。 |
| void OH_ArkUI_LayoutConstraint_SetMinWidth(ArkUI_LayoutConstraint* Constraint, int32_t value) | - | 设置最小宽度。 |
| void OH_ArkUI_LayoutConstraint_SetMaxHeight(ArkUI_LayoutConstraint* Constraint, int32_t value) | - | 设置最大高度。 |
| void OH_ArkUI_LayoutConstraint_SetMinHeight(ArkUI_LayoutConstraint* Constraint, int32_t value) | - | 设置最小高度。 |
| void OH_ArkUI_LayoutConstraint_SetPercentReferenceWidth(ArkUI_LayoutConstraint* Constraint, int32_t value) | - | 设置宽度百分比基准。 |
| void OH_ArkUI_LayoutConstraint_SetPercentReferenceHeight(ArkUI_LayoutConstraint* Constraint, int32_t value) | - | 设置高度百分比基准。 |
| void* OH_ArkUI_DrawContext_GetCanvas(ArkUI_DrawContext* context) | - | 获取绘制canvas指针，可以转换为图形库的OH_Drawing_Canvas指针进行绘制。 |
| ArkUI_IntSize OH_ArkUI_DrawContext_GetSize(ArkUI_DrawContext* context) | - | 获取可绘制区域大小。 |
| void OH_ArkUI_SwiperDigitIndicator_SetFontWeight(ArkUI_SwiperDigitIndicator *indicator, ArkUI_FontWeight fontWeight) | - | 设置Swiper组件数字导航指示器字体粗细属性。 |
| ArkUI_FontWeight OH_ArkUI_SwiperDigitIndicator_GetFontWeight(ArkUI_SwiperDigitIndicator* indicator) | - | 获取Swiper组件数字导航指示器字体粗细属性。 |
| void OH_ArkUI_SwiperDigitIndicator_SetSelectedFontWeight(ArkUI_SwiperDigitIndicator *indicator, ArkUI_FontWeight selectedFontWeight) | - | 设置被选中Swiper组件数字导航指示器字体粗细属性。 |
| ArkUI_FontWeight OH_ArkUI_SwiperDigitIndicator_GetSelectedFontWeight(ArkUI_SwiperDigitIndicator* indicator) | - | 获取被选中Swiper组件数字导航指示器字体粗细属性。 |
| ArkUI_ListItemSwipeActionItem* OH_ArkUI_ListItemSwipeActionItem_Create() | - | 创建ListItemSwipeActionItem接口设置的配置项。 |
| void OH_ArkUI_ListItemSwipeActionItem_Dispose(ArkUI_ListItemSwipeActionItem* item) | - | 销毁ListItemSwipeActionItem实例。 |
| void OH_ArkUI_ListItemSwipeActionItem_SetContent(ArkUI_ListItemSwipeActionItem* item, ArkUI_NodeHandle node) | - | 设置ListItemSwipeActionItem的布局内容。 |
| void OH_ArkUI_ListItemSwipeActionItem_SetActionAreaDistance(ArkUI_ListItemSwipeActionItem* item, float distance) | - | 设置组件长距离滑动删除距离阈值。 |
| float OH_ArkUI_ListItemSwipeActionItem_GetActionAreaDistance(ArkUI_ListItemSwipeActionItem* item) | - | 获取组件长距离滑动删除距离阈值。 |
| void OH_ArkUI_ListItemSwipeActionItem_SetOnEnterActionArea(ArkUI_ListItemSwipeActionItem* item, void (*callback)()) | - | 设置滑动条目进入删除区域时调用的事件。 |
| void OH_ArkUI_ListItemSwipeActionItem_SetOnEnterActionAreaWithUserData (ArkUI_ListItemSwipeActionItem* item,void* userData, void (*callback)(void* userData)) | - | 设置滑动条目进入删除区域时调用的事件，回调事件会传入用户自定义数据。 |
| void OH_ArkUI_ListItemSwipeActionItem_SetOnAction(ArkUI_ListItemSwipeActionItem* item, void (*callback)()) | - | 设置组件进入长距删除区后删除ListItem时调用的事件。 |
| void OH_ArkUI_ListItemSwipeActionItem_SetOnActionWithUserData(ArkUI_ListItemSwipeActionItem* item,void* userData, void (*callback)(void* userData)) | - | 设置组件进入长距删除区后删除ListItem时调用的事件，回调事件会传入用户自定义数据。 |
| void OH_ArkUI_ListItemSwipeActionItem_SetOnExitActionArea(ArkUI_ListItemSwipeActionItem* item, void (*callback)()) | - | 设置滑动条目退出删除区域时调用的事件。 |
| void OH_ArkUI_ListItemSwipeActionItem_SetOnExitActionAreaWithUserData (ArkUI_ListItemSwipeActionItem* item,void* userData, void (*callback)(void* userData)) | - | 设置滑动条目退出删除区域时调用的事件，回调事件会传入用户自定义数据。 |
| void OH_ArkUI_ListItemSwipeActionItem_SetOnStateChange (ArkUI_ListItemSwipeActionItem* item,void (*callback)(ArkUI_ListItemSwipeActionState swipeActionState)) | - | 设置列表项滑动状态变化时候触发的事件。 |
| void OH_ArkUI_ListItemSwipeActionItem_SetOnStateChangeWithUserData (ArkUI_ListItemSwipeActionItem* item,void* userData, void (*callback)(ArkUI_ListItemSwipeActionState swipeActionState, void* userData)) | - | 设置列表项滑动状态变化时候触发的事件，回调事件会传入用户自定义数据。 |
| ArkUI_ListItemSwipeActionOption* OH_ArkUI_ListItemSwipeActionOption_Create() | - | 创建ListItemSwipeActionOption接口设置的配置项。 |
| void OH_ArkUI_ListItemSwipeActionOption_Dispose(ArkUI_ListItemSwipeActionOption* option) | - | 销毁ListItemSwipeActionOption实例。 |
| void OH_ArkUI_ListItemSwipeActionOption_SetStart(ArkUI_ListItemSwipeActionOption* option, ArkUI_ListItemSwipeActionItem* item) | - | 设置ListItemSwipeActionItem的左侧（垂直布局）或上方（横向布局）布局内容。 |
| void OH_ArkUI_ListItemSwipeActionOption_SetEnd(ArkUI_ListItemSwipeActionOption* option, ArkUI_ListItemSwipeActionItem* item) | - | 设置ListItemSwipeActionItem的右侧（垂直布局）或下方（横向布局）布局内容。 |
| void OH_ArkUI_ListItemSwipeActionOption_SetEdgeEffect(ArkUI_ListItemSwipeActionOption* option, ArkUI_ListItemSwipeEdgeEffect edgeEffect) | - | 设置边缘滑动效果。 |
| int32_t OH_ArkUI_ListItemSwipeActionOption_GetEdgeEffect(ArkUI_ListItemSwipeActionOption* option) | - | 获取边缘滑动效果。 |
| void OH_ArkUI_ListItemSwipeActionOption_SetOnOffsetChange(ArkUI_ListItemSwipeActionOption* option, void (*callback)(float offset)) | - | 滑动操作偏移量更改时调用的事件。 |
| void OH_ArkUI_ListItemSwipeActionOption_SetOnOffsetChangeWithUserData (ArkUI_ListItemSwipeActionOption* option, void* userData, void (*callback)(float offset, void* userData)) | - | 滑动操作偏移量更改时调用的事件，回调事件会传入用户自定义数据。 |
| int32_t OH_ArkUI_ListItemSwipeAction_Expand(ArkUI_NodeHandle node, ArkUI_ListItemSwipeActionDirection direction) | - | 展开指定ListItem的划出菜单。 |
| int32_t OH_ArkUI_ListItemSwipeAction_Collapse(ArkUI_NodeHandle node) | - | 收起指定ListItem的划出菜单。 |
| ArkUI_AccessibilityState* OH_ArkUI_AccessibilityState_Create(void) | - | 创建无障碍状态。 |
| void OH_ArkUI_AccessibilityState_Dispose(ArkUI_AccessibilityState* state) | - | 销毁无障碍状态指针。 |
| void OH_ArkUI_AccessibilityState_SetDisabled(ArkUI_AccessibilityState* state, int32_t isDisabled) | - | 设置无障碍状态是否禁用。 |
| int32_t OH_ArkUI_AccessibilityState_IsDisabled(ArkUI_AccessibilityState* state) | - | 获取无障碍状态是否禁用。 |
| void OH_ArkUI_AccessibilityState_SetSelected(ArkUI_AccessibilityState* state, int32_t isSelected) | - | 设置无障碍状态是否选中。 |
| int32_t OH_ArkUI_AccessibilityState_IsSelected(ArkUI_AccessibilityState* state) | - | 获取无障碍状态是否选中。 |
| void OH_ArkUI_AccessibilityState_SetCheckedState(ArkUI_AccessibilityState* state, int32_t checkedState) | - | 设置无障碍状态复选框状态。 |
| int32_t OH_ArkUI_AccessibilityState_GetCheckedState(ArkUI_AccessibilityState* state) | - | 获取无障碍状态复选框状态。 |
| ArkUI_AccessibilityValue* OH_ArkUI_AccessibilityValue_Create(void) | - | 创建无障碍信息。 |
| void OH_ArkUI_AccessibilityValue_Dispose(ArkUI_AccessibilityValue* value) | - | 销毁无障碍信息指针。 |
| void OH_ArkUI_AccessibilityValue_SetMin(ArkUI_AccessibilityValue* value, int32_t min) | - | 设置无障碍最小值信息。 |
| int32_t OH_ArkUI_AccessibilityValue_GetMin(ArkUI_AccessibilityValue* value) | - | 获取无障碍最小值信息。 |
| void OH_ArkUI_AccessibilityValue_SetMax(ArkUI_AccessibilityValue* value, int32_t max) | - | 设置无障碍最大值信息。 |
| int32_t OH_ArkUI_AccessibilityValue_GetMax(ArkUI_AccessibilityValue* value) | - | 获取无障碍最大值信息。 |
| void OH_ArkUI_AccessibilityValue_SetCurrent(ArkUI_AccessibilityValue* value, int32_t current) | - | 设置无障碍当前值信息。 |
| int32_t OH_ArkUI_AccessibilityValue_GetCurrent(ArkUI_AccessibilityValue* value) | - | 获取无障碍当前值信息。 |
| void OH_ArkUI_AccessibilityValue_SetRangeMin(ArkUI_AccessibilityValue* value, int32_t rangeMin) | - | 设置范围组件的无障碍最小值信息。 |
| int32_t OH_ArkUI_AccessibilityValue_GetRangeMin(ArkUI_AccessibilityValue* value) | - | 获取范围组件的无障碍最小值信息。 |
| void OH_ArkUI_AccessibilityValue_SetRangeMax(ArkUI_AccessibilityValue* value, int32_t rangeMax) | - | 设置范围组件的无障碍最大值信息。 |
| int32_t OH_ArkUI_AccessibilityValue_GetRangeMax(ArkUI_AccessibilityValue* value) | - | 获取范围组件的无障碍最大值信息。 |
| void OH_ArkUI_AccessibilityValue_SetRangeCurrent(ArkUI_AccessibilityValue* value, int32_t rangeCurrent) | - | 用于设置范围组件的无障碍当前值信息。 |
| int32_t OH_ArkUI_AccessibilityValue_GetRangeCurrent(ArkUI_AccessibilityValue* value) | - | 用于获取范围组件的无障碍当前值信息。 |
| void OH_ArkUI_AccessibilityValue_SetText(ArkUI_AccessibilityValue* value, const char* text) | - | 设置无障碍文本描述信息。 |
| const char* OH_ArkUI_AccessibilityValue_GetText(ArkUI_AccessibilityValue* value) | - | 获取无障碍文本描述信息。 |
| void OH_ArkUI_CustomProperty_Destroy(ArkUI_CustomProperty* handle) | - | 销毁CustomProperty实例。 |
| const char* OH_ArkUI_CustomProperty_GetStringValue(ArkUI_CustomProperty* handle) | - | 获取自定义属性value信息。 |
| const char* OH_ArkUI_HostWindowInfo_GetName(ArkUI_HostWindowInfo* info) | - | 获取HostWindowInfo对象中的窗口名称。 |
| void OH_ArkUI_HostWindowInfo_Destroy(ArkUI_HostWindowInfo* info) | - | 销毁HostWindowInfo对象。 |
| void OH_ArkUI_ActiveChildrenInfo_Destroy(ArkUI_ActiveChildrenInfo* handle) | - | 销毁ArkUI_ActiveChildrenInfo实例，释放获取活跃子节点信息时分配的资源。 |
| ArkUI_NodeHandle OH_ArkUI_ActiveChildrenInfo_GetNodeByIndex(ArkUI_ActiveChildrenInfo* handle, int32_t index) | - | 获取ArkUI_ActiveChildrenInfo结构体中下标为index的子节点，适用于按下标遍历活跃子节点。 |
| int32_t OH_ArkUI_ActiveChildrenInfo_GetCount(ArkUI_ActiveChildrenInfo* handle) | - | 获取ArkUI_ActiveChildrenInfo结构体内的子节点数量，适用于遍历活跃子节点前确定数量。 |
| ArkUI_CrossLanguageOption* OH_ArkUI_CrossLanguageOption_Create(void) | - | 创建跨语言配置项实例。 |
| void OH_ArkUI_CrossLanguageOption_Destroy(ArkUI_CrossLanguageOption* option) | - | 销毁跨语言配置项实例。 |
| void OH_ArkUI_CrossLanguageOption_SetAttributeSettingStatus(ArkUI_CrossLanguageOption* option, bool enabled) | - | 设置配置项中是否允许跨语言修改属性。 |
| bool OH_ArkUI_CrossLanguageOption_GetAttributeSettingStatus(ArkUI_CrossLanguageOption* option) | - | 获取配置项中是否允许跨语言修改属性。 |
| void OH_ArkUI_CrossLanguageOption_SetTreeOperatingStatus(ArkUI_CrossLanguageOption* option, OH_ArkUI_CrossLanguageOperatingStatus status) | - | 设置跨语言配置项的节点树操作状态。 |
| OH_ArkUI_CrossLanguageOperatingStatus OH_ArkUI_CrossLanguageOption_GetTreeOperatingStatus(ArkUI_CrossLanguageOption* option) | - | 获取跨语言配置项的节点树操作状态。 |
| ArkUI_ContentTransitionEffect* OH_ArkUI_ContentTransitionEffect_Create(int32_t type) | - | 创建ContentTransitionEffect属性对象。 |
| ArkUI_SelectionOptions* OH_ArkUI_SelectionOptions_Create() | - | 创建选择选项。 |
| void OH_ArkUI_SelectionOptions_Dispose(ArkUI_SelectionOptions* options) | - | 释放选择选项对象。 |
| void OH_ArkUI_SelectionOptions_SetMenuPolicy(ArkUI_SelectionOptions* options, ArkUI_MenuPolicy menuPolicy) | - | 设置选择选项的菜单弹出策略。 |
| ArkUI_MenuPolicy OH_ArkUI_SelectionOptions_GetMenuPolicy(ArkUI_SelectionOptions* options) | - | 获取选择选项的菜单弹出策略。 |
| ArkUI_ErrorCode OH_ArkUI_TextMenuItem_SetContent(ArkUI_TextMenuItem* item, const char* content) | - | 设置文本菜单项标题。 |
| ArkUI_ErrorCode OH_ArkUI_TextMenuItem_GetContent(const ArkUI_TextMenuItem* item, char* buffer, int32_t bufferSize, int32_t* writeLength) | - | 获取文本菜单项标题。 |
| ArkUI_ErrorCode OH_ArkUI_TextMenuItem_SetIcon(ArkUI_TextMenuItem* item, const char* icon) | - | 设置文本菜单项图标路径。 |
| ArkUI_ErrorCode OH_ArkUI_TextMenuItem_GetIcon(const ArkUI_TextMenuItem* item, char* buffer, int32_t bufferSize, int32_t* writeLength) | - | 获取文本菜单项图标路径。 |
| ArkUI_ErrorCode OH_ArkUI_TextMenuItem_SetLabelInfo(ArkUI_TextMenuItem* item, const char* labelInfo) | - | 设置文本菜单项快捷键提示，例如“复制”菜单项的快捷键提示可以设置为“Ctrl+C”。 |
| ArkUI_ErrorCode OH_ArkUI_TextMenuItem_GetLabelInfo(const ArkUI_TextMenuItem* item, char* buffer, int32_t bufferSize, int32_t* writeLength) | - | 获取文本菜单项快捷键提示，例如“复制”菜单项的快捷键提示一般为“Ctrl+C”。 |
| ArkUI_ErrorCode OH_ArkUI_TextMenuItem_SetId(ArkUI_TextMenuItem* item, int32_t id) | - | 设置文本菜单项id。 |
| ArkUI_ErrorCode OH_ArkUI_TextMenuItem_GetId(const ArkUI_TextMenuItem* item, int32_t* id) | - | 获取文本菜单项id。 |
| ArkUI_ErrorCode OH_ArkUI_TextMenuItemArray_GetSize(ArkUI_TextMenuItemArray* items, int32_t* size) | - | 获取文本菜单项数组大小。 |
| ArkUI_ErrorCode OH_ArkUI_TextMenuItemArray_GetItem(ArkUI_TextMenuItemArray* items, int32_t index, ArkUI_TextMenuItem** item) | - | 获取文本菜单项数组中指定索引位置的文本菜单项。 |
| ArkUI_ErrorCode OH_ArkUI_TextMenuItemArray_Insert(ArkUI_TextMenuItemArray* items, ArkUI_TextMenuItem* item, int32_t index) | - | 在文本菜单项数组中指定索引位置插入一个文本菜单项。 |
| ArkUI_ErrorCode OH_ArkUI_TextMenuItemArray_Erase(ArkUI_TextMenuItemArray* items, int32_t index) | - | 删除文本菜单项数组中指定索引位置的文本菜单项。 |
| ArkUI_ErrorCode OH_ArkUI_TextMenuItemArray_Clear(ArkUI_TextMenuItemArray* items) | - | 清除文本菜单项数组中所有的文本菜单项。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditMenuOptions_RegisterOnCreateMenuCallback(ArkUI_TextEditMenuOptions* editMenuOptions, void* userData, ArkUI_TextCreateMenuCallback cb) | - | 注册文本菜单创建事件回调函数。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditMenuOptions_RegisterOnPrepareMenuCallback(ArkUI_TextEditMenuOptions* editMenuOptions, void* userData, ArkUI_TextPrepareMenuCallback cb) | - | 注册文本菜单准备事件回调函数。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditMenuOptions_RegisterOnMenuItemClickCallback(ArkUI_TextEditMenuOptions* editMenuOptions, void* userData, ArkUI_TextMenuItemClickCallback cb) | - | 注册文本菜单项点击事件回调函数。 |
| ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_SetSpanType(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, ArkUI_TextSpanType textSpanType) | - | 设置自定义文本选择菜单的文本识别类型。 |
| ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_GetSpanType(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, ArkUI_TextSpanType* spanType) | - | 获取自定义文本选择菜单的文本识别类型。 |
| ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_SetContentNode(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, ArkUI_NodeHandle node) | - | 设置自定义文本选择菜单的内容节点。 |
| ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_GetContentNode(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, ArkUI_NodeHandle* node) | - | 获取自定义文本选择菜单的内容节点。 |
| ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_SetResponseType(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, ArkUI_TextResponseType responseType) | - | 设置自定义文本选择菜单的响应类型。 |
| ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_GetResponseType(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, ArkUI_TextResponseType* responseType) | - | 获取自定义文本选择菜单的响应类型。 |
| ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_RegisterOnMenuShowCallback(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, void* userData, void (*callback)(int32_t start, int32_t end, void* userData)) | - | 注册自定义文本选择菜单显示事件回调。 |
| ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_RegisterOnMenuHideCallback(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, void* userData, void (*callback)(int32_t start, int32_t end, void* userData)) | - | 注册自定义文本选择菜单隐藏事件回调。 |
| ArkUI_ErrorCode OH_ArkUI_PickerIndicatorStyle_ConfigureBackground(ArkUI_PickerIndicatorStyle* style, ArkUI_PickerIndicatorBackground* background) | - | 设置背景样式参数，此接口仅当选择器选中项样式枚举类型为ARKUI_PICKER_INDICATOR_BACKGROUND时生效。 |
| ArkUI_ErrorCode OH_ArkUI_PickerIndicatorStyle_ConfigureDivider(ArkUI_PickerIndicatorStyle* style, ArkUI_PickerIndicatorDivider* divider) | - | 设置分割线样式参数，此接口仅当选择器选中项样式枚举类型为ARKUI_PICKER_INDICATOR_DIVIDER时生效。 |
| ArkUI_ErrorCode OH_ArkUI_DecorationStyleOptions_SetTextDecorationType(OH_ArkUI_DecorationStyleOptions* options, ArkUI_TextDecorationType type) | - | 设置装饰线样式的装饰类型。 |
| ArkUI_ErrorCode OH_ArkUI_DecorationStyleOptions_GetTextDecorationType(OH_ArkUI_DecorationStyleOptions* options, ArkUI_TextDecorationType* type) | - | 获取装饰线样式的装饰类型。 |
| ArkUI_ErrorCode OH_ArkUI_DecorationStyleOptions_SetColor(OH_ArkUI_DecorationStyleOptions* options, uint32_t color) | - | 设置装饰线的颜色。 |
| ArkUI_ErrorCode OH_ArkUI_DecorationStyleOptions_GetColor(OH_ArkUI_DecorationStyleOptions* options, uint32_t* color) | - | 获取装饰线的颜色。 |
| ArkUI_ErrorCode OH_ArkUI_DecorationStyleOptions_SetTextDecorationStyle(OH_ArkUI_DecorationStyleOptions* options, ArkUI_TextDecorationStyle style) | - | 设置装饰线的样式。 |
| ArkUI_ErrorCode OH_ArkUI_DecorationStyleOptions_GetTextDecorationStyle(OH_ArkUI_DecorationStyleOptions* options, ArkUI_TextDecorationStyle* style) | - | 获取装饰线的样式。 |
| ArkUI_ErrorCode OH_ArkUI_DecorationStyleOptions_SetThicknessScale(OH_ArkUI_DecorationStyleOptions* options, float thicknessScale) | - | 设置装饰线的粗细缩放比例。 |
| ArkUI_ErrorCode OH_ArkUI_DecorationStyleOptions_GetThicknessScale(OH_ArkUI_DecorationStyleOptions* options, float* thicknessScale) | - | 获取装饰线的粗细缩放比例。 |
| ArkUI_ErrorCode OH_ArkUI_TextDataDetectorConfig_SetTypes(OH_ArkUI_TextDataDetectorConfig* config, const ArkUI_TextDataDetectorType* types, int32_t length) | - | 设置文本实体识别配置的类型。 |
| ArkUI_ErrorCode OH_ArkUI_TextDataDetectorConfig_GetTypes(OH_ArkUI_TextDataDetectorConfig* config, ArkUI_TextDataDetectorType* buffer, int32_t bufferSize, int32_t* writeLength) | - | 获取文本实体识别配置的类型。 |
| ArkUI_ErrorCode OH_ArkUI_TextDataDetectorConfig_RegisterOnDetectResultUpdateCallback(OH_ArkUI_TextDataDetectorConfig* config, void* userData, void (*callback)(const char* result, int32_t length, void* userData)) | - | 设置文本实体识别结果更新回调。 |
| ArkUI_ErrorCode OH_ArkUI_TextDataDetectorConfig_SetColor(OH_ArkUI_TextDataDetectorConfig* config, uint32_t color) | - | 设置识别内容的颜色。 |
| ArkUI_ErrorCode OH_ArkUI_TextDataDetectorConfig_GetColor(OH_ArkUI_TextDataDetectorConfig* config, uint32_t* color) | - | 获取识别内容的颜色。 |
| ArkUI_ErrorCode OH_ArkUI_TextDataDetectorConfig_SetDecorationStyleOptions(OH_ArkUI_TextDataDetectorConfig* config, OH_ArkUI_DecorationStyleOptions* decoration) | - | 设置识别内容的装饰样式。 |
| ArkUI_ErrorCode OH_ArkUI_TextDataDetectorConfig_GetDecorationStyleOptions(OH_ArkUI_TextDataDetectorConfig* config, OH_ArkUI_DecorationStyleOptions* decoration) | - | 获取识别内容的装饰样式。 |
| ArkUI_ErrorCode OH_ArkUI_TextDataDetectorConfig_SetEnablePreviewMenu(OH_ArkUI_TextDataDetectorConfig* config, bool enablePreviewMenu) | - | 设置长按识别内容时是否显示预览菜单。 |
| ArkUI_ErrorCode OH_ArkUI_TextDataDetectorConfig_GetEnablePreviewMenu(OH_ArkUI_TextDataDetectorConfig* config, bool* enablePreviewMenu) | - | 获取长按识别内容时是否显示预览菜单。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorPlaceholderOptions_SetValue(OH_ArkUI_TextEditorPlaceholderOptions* options, const char* value) | - | 设置无输入时的提示文本选项的提示文字。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorPlaceholderOptions_GetValue(OH_ArkUI_TextEditorPlaceholderOptions* options, char* buffer, int32_t bufferSize, int32_t* writeLength) | - | 获取无输入时的提示文本选项的提示文字。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorPlaceholderOptions_SetFontSize(OH_ArkUI_TextEditorPlaceholderOptions* options, float fontSize) | - | 设置无输入时的提示文本选项的字体大小。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorPlaceholderOptions_GetFontSize(OH_ArkUI_TextEditorPlaceholderOptions* options, float* fontSize) | - | 获取无输入时的提示文本选项的字体大小。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorPlaceholderOptions_SetFontWeight(OH_ArkUI_TextEditorPlaceholderOptions* options, uint32_t fontWeight) | - | 设置无输入时的提示文本选项的字体粗细。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorPlaceholderOptions_GetFontWeight(OH_ArkUI_TextEditorPlaceholderOptions* options, uint32_t* fontWeight) | - | 获取无输入时的提示文本选项的字体粗细。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorPlaceholderOptions_SetFontFamily(OH_ArkUI_TextEditorPlaceholderOptions* options, const char* fontFamily) | - | 设置无输入时的提示文本选项的字体家族。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorPlaceholderOptions_GetFontFamily(OH_ArkUI_TextEditorPlaceholderOptions* options, char* buffer, int32_t bufferSize, int32_t* writeLength) | - | 获取无输入时的提示文本选项的字体家族。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorPlaceholderOptions_SetFontStyle(OH_ArkUI_TextEditorPlaceholderOptions* options, ArkUI_FontStyle fontStyle) | - | 设置无输入时的提示文本选项的字体样式。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorPlaceholderOptions_GetFontStyle(OH_ArkUI_TextEditorPlaceholderOptions* options, ArkUI_FontStyle* fontStyle) | - | 获取无输入时的提示文本选项的字体样式。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorPlaceholderOptions_SetFontColor(OH_ArkUI_TextEditorPlaceholderOptions* options, uint32_t fontColor) | - | 设置无输入时的提示文本选项的字体颜色。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorPlaceholderOptions_GetFontColor(OH_ArkUI_TextEditorPlaceholderOptions* options, uint32_t* fontColor) | - | 获取无输入时的提示文本选项的字体颜色。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorStyledStringController_SetCaretOffset(OH_ArkUI_TextEditorStyledStringController* controller, int32_t caretOffset) | - | 通过属性字符串控制器设置光标偏移量。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorStyledStringController_GetCaretOffset(OH_ArkUI_TextEditorStyledStringController* controller, int32_t* caretOffset) | - | 通过属性字符串控制器获取光标索引位置。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorStyledStringController_SetSelection(OH_ArkUI_TextEditorStyledStringController* controller, uint32_t start, uint32_t end, ArkUI_MenuPolicy menuPolicy) | - | 通过属性字符串控制器设置选中区域。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorStyledStringController_IsEditing(OH_ArkUI_TextEditorStyledStringController* controller, bool* isEditing) | - | 通过属性字符串控制器获取文本编辑器的编辑状态。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorStyledStringController_StopEditing(OH_ArkUI_TextEditorStyledStringController* controller) | - | 通过属性字符串控制器退出文本编辑器的编辑状态。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorStyledStringController_GetPreviewText(OH_ArkUI_TextEditorStyledStringController* controller, uint32_t* offset, char* buffer, int32_t bufferSize, int32_t* writeLength) | - | 通过属性字符串控制器获取预上屏文本内容。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorStyledStringController_GetCaretRect(OH_ArkUI_TextEditorStyledStringController* controller, ArkUI_Rect* rect) | - | 通过属性字符串控制器获取光标矩形区域。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorStyledStringController_DeleteBackward(OH_ArkUI_TextEditorStyledStringController* controller) | - | 通过属性字符串控制器删除字符。没有内容被选中时，删除当前光标位置前的1个字符。有内容被选中时，删除选中内容。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_SetTextAlign(OH_ArkUI_TextEditorParagraphStyle* style, ArkUI_TextAlignment align) | - | 设置段落样式中的文本对齐方式。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_GetTextAlign(OH_ArkUI_TextEditorParagraphStyle* style, ArkUI_TextAlignment* align) | - | 获取段落样式中的文本对齐方式。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_SetLeadingMarginPixelMap(OH_ArkUI_TextEditorParagraphStyle* style, struct OH_PixelmapNative* pixelmap) | - | 设置段落样式中段落缩进的像素图。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_GetLeadingMarginPixelMap(OH_ArkUI_TextEditorParagraphStyle* style, struct OH_PixelmapNative** pixelmap) | - | 获取段落样式中段落缩进的像素图。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_SetLeadingMarginWidth(OH_ArkUI_TextEditorParagraphStyle* style, uint32_t width) | - | 设置段落样式中段落缩进的宽度。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_GetLeadingMarginWidth(OH_ArkUI_TextEditorParagraphStyle* style, uint32_t* width) | - | 获取段落样式中段落缩进的宽度。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_SetLeadingMarginHeight(OH_ArkUI_TextEditorParagraphStyle* style, uint32_t height) | - | 设置段落样式中段落缩进的高度。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_GetLeadingMarginHeight(OH_ArkUI_TextEditorParagraphStyle* style, uint32_t* height) | - | 获取段落样式中段落缩进的高度。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_SetWordBreak(OH_ArkUI_TextEditorParagraphStyle* style, ArkUI_WordBreak wordBreak) | - | 设置段落样式的断字方式。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_GetWordBreak(OH_ArkUI_TextEditorParagraphStyle* style, ArkUI_WordBreak* wordBreak) | - | 获取段落样式的断字方式。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_SetLineBreakStrategy(OH_ArkUI_TextEditorParagraphStyle* style, OH_ArkUI_LineBreakStrategy lineBreakStrategy) | - | 设置段落样式的换行策略。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_GetLineBreakStrategy(OH_ArkUI_TextEditorParagraphStyle* style, OH_ArkUI_LineBreakStrategy* lineBreakStrategy) | - | 获取段落样式的换行策略。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_SetParagraphSpacing(OH_ArkUI_TextEditorParagraphStyle* style, uint32_t paragraphSpacing) | - | 设置段落样式的段落间距。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_GetParagraphSpacing(OH_ArkUI_TextEditorParagraphStyle* style, uint32_t* paragraphSpacing) | - | 获取段落样式的段落间距。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_SetTextVerticalAlign(OH_ArkUI_TextEditorParagraphStyle* style, ArkUI_TextVerticalAlignment verticalAlignment) | - | 设置段落样式的文本垂直对齐方式。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_GetTextVerticalAlign(OH_ArkUI_TextEditorParagraphStyle* style, ArkUI_TextVerticalAlignment* verticalAlignment) | - | 获取段落样式的文本垂直对齐方式。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_SetTextDirection(OH_ArkUI_TextEditorParagraphStyle* style, ArkUI_TextDirection textDirection) | - | 设置段落样式的文本方向。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_GetTextDirection(OH_ArkUI_TextEditorParagraphStyle* style, ArkUI_TextDirection* textDirection) | - | 获取段落样式的文本方向。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorStyledStringController_SetTypingParagraphStyle(OH_ArkUI_TextEditorStyledStringController* controller, OH_ArkUI_TextEditorParagraphStyle* style) | - | 通过属性字符串控制器设置预设段落样式。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_SetFontColor(OH_ArkUI_TextEditorTextStyle* style, uint32_t color) | - | 设置文本样式的字体颜色。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_GetFontColor(OH_ArkUI_TextEditorTextStyle* style, uint32_t* color) | - | 获取文本样式的字体颜色。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_SetFontSize(OH_ArkUI_TextEditorTextStyle* style, float size) | - | 设置文本样式的字体大小。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_GetFontSize(OH_ArkUI_TextEditorTextStyle* style, float* size) | - | 获取文本样式的字体大小。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_SetFontStyle(OH_ArkUI_TextEditorTextStyle* style, ArkUI_FontStyle fontStyle) | - | 设置文本样式的字体样式。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_GetFontStyle(OH_ArkUI_TextEditorTextStyle* style, ArkUI_FontStyle* fontStyle) | - | 获取文本样式的字体样式。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_SetFontWeight(OH_ArkUI_TextEditorTextStyle* style, uint32_t fontWeight) | - | 设置文本样式的字体粗细。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_GetFontWeight(OH_ArkUI_TextEditorTextStyle* style, uint32_t* fontWeight) | - | 获取文本样式的字体粗细。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_SetFontFamily(OH_ArkUI_TextEditorTextStyle* style, const char* fontFamily) | - | 设置文本样式的字体家族。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_GetFontFamily(OH_ArkUI_TextEditorTextStyle* style, char* buffer, int32_t bufferSize, int32_t* writeLength) | - | 获取文本样式的字体家族。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_SetDecoration(OH_ArkUI_TextEditorTextStyle* style, OH_ArkUI_DecorationStyleOptions* options) | - | 设置文本样式的文本装饰选项。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_GetDecoration(OH_ArkUI_TextEditorTextStyle* style, OH_ArkUI_DecorationStyleOptions* options) | - | 获取文本样式的文本装饰选项。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_SetTextShadows(OH_ArkUI_TextEditorTextStyle* style, const OH_ArkUI_ShadowOptions** options, int32_t length) | - | 设置文本样式的文本阴影选项。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_GetTextShadows(OH_ArkUI_TextEditorTextStyle* style, OH_ArkUI_ShadowOptions** shadowOptions, uint32_t shadowOptionsSize, uint32_t* writeLength) | - | 获取文本样式的文本阴影选项。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_SetLineHeight(OH_ArkUI_TextEditorTextStyle* style, int32_t lineHeight) | - | 设置文本样式的文本行高。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_GetLineHeight(OH_ArkUI_TextEditorTextStyle* style, int32_t* lineHeight) | - | 获取文本样式的文本行高。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_SetLetterSpacing(OH_ArkUI_TextEditorTextStyle* style, int32_t letterSpacing) | - | 设置文本样式的字符间距。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_GetLetterSpacing(OH_ArkUI_TextEditorTextStyle* style, int32_t* letterSpacing) | - | 获取文本样式的字符间距。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_SetFontFeature(OH_ArkUI_TextEditorTextStyle* style, const char* fontFeature) | - | 设置文本样式的文字特性效果，比如数字等宽的特性。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_GetFontFeature(OH_ArkUI_TextEditorTextStyle* style, char* buffer, int32_t bufferSize, int32_t* writeLength) | - | 获取文本样式的文字特性效果，比如数字等宽的特性。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_SetHalfLeading(OH_ArkUI_TextEditorTextStyle* style, bool halfLeading) | - | 设置文本样式中文本是否将行间距平分至行的顶部与底部。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_GetHalfLeading(OH_ArkUI_TextEditorTextStyle* style, bool* halfLeading) | - | 获取文本样式中文本是否将行间距平分至行的顶部与底部。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_SetTextBackgroundColor(OH_ArkUI_TextEditorTextStyle* style, uint32_t color) | - | 设置文本样式中的文本背景颜色。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_GetTextBackgroundColor(OH_ArkUI_TextEditorTextStyle* style, uint32_t* color) | - | 获取文本样式中的文本背景颜色。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_SetTextBackgroundRadius(OH_ArkUI_TextEditorTextStyle* style, float topLeft, float topRight, float bottomLeft, float bottomRight) | - | 设置文本样式中文本背景的圆角半径。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_GetTextBackgroundRadius(OH_ArkUI_TextEditorTextStyle* style, float* topLeft, float* topRight, float* bottomLeft, float* bottomRight) | - | 获取文本样式中文本背景的圆角半径。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorStyledStringController_SetTypingStyle(OH_ArkUI_TextEditorStyledStringController* controller, OH_ArkUI_TextEditorTextStyle* style) | - | 通过属性字符串控制器设置预设输入样式。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorStyledStringController_GetTypingStyle(OH_ArkUI_TextEditorStyledStringController* controller, OH_ArkUI_TextEditorTextStyle* style) | - | 通过属性字符串控制器获取预设输入样式。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorSelectionMenuOptions_SetSpanType(OH_ArkUI_TextEditorSelectionMenuOptions* options, OH_ArkUI_TextEditorSpanType textEditorSpanType) | - | 设置文本编辑器中文本选择菜单的span的类型。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorSelectionMenuOptions_GetSpanType(OH_ArkUI_TextEditorSelectionMenuOptions* options, OH_ArkUI_TextEditorSpanType* textEditorSpanType) | - | 获取文本编辑器中文本选择菜单的span的类型。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorSelectionMenuOptions_SetContentNode(OH_ArkUI_TextEditorSelectionMenuOptions* options, ArkUI_NodeHandle node) | - | 设置文本编辑器中文本选择菜单的内容节点。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorSelectionMenuOptions_GetContentNode(OH_ArkUI_TextEditorSelectionMenuOptions* options, ArkUI_NodeHandle* node) | - | 获取文本编辑器中文本选择菜单的内容节点。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorSelectionMenuOptions_SetResponseType(OH_ArkUI_TextEditorSelectionMenuOptions* options, OH_ArkUI_TextEditorResponseType responseType) | - | 设置文本编辑器中文本选择菜单的响应类型。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorSelectionMenuOptions_GetResponseType(OH_ArkUI_TextEditorSelectionMenuOptions* options, OH_ArkUI_TextEditorResponseType* responseType) | - | 获取文本编辑器中文本选择菜单的响应类型。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorSelectionMenuOptions_SetMenuType(OH_ArkUI_TextEditorSelectionMenuOptions* options, OH_ArkUI_TextMenuType menuType) | - | 设置文本编辑器中文本选择菜单的类型。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorSelectionMenuOptions_GetMenuType(OH_ArkUI_TextEditorSelectionMenuOptions* options, OH_ArkUI_TextMenuType* menuType) | - | 获取文本编辑器中文本选择菜单的类型。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorSelectionMenuOptions_RegisterOnMenuShowCallback(OH_ArkUI_TextEditorSelectionMenuOptions* options, void* userData, void (*callback)(int32_t start, int32_t end, void* callbackUserData)) | - | 设置文本选择菜单显示时触发的事件。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorSelectionMenuOptions_RegisterOnMenuHideCallback(OH_ArkUI_TextEditorSelectionMenuOptions* options, void* userData, void (*callback)(int32_t start, int32_t end, void* callbackUserData)) | - | 设置文本选择菜单隐藏时触发的事件。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorSelectionMenuOptions_RegisterOnMenuAppearCallback(OH_ArkUI_TextEditorSelectionMenuOptions* options, void* userData, void (*callback)(int32_t start, int32_t end, void* callbackUserData)) | - | 设置文本选择菜单出现时触发的事件。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorSelectionMenuOptions_RegisterOnMenuDisappearCallback(OH_ArkUI_TextEditorSelectionMenuOptions* options, void* userData, void (*callback)(void* callbackUserData)) | - | 设置文本选择菜单消失时触发的事件。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorSelectionMenuOptions_SetHapticFeedbackMode(OH_ArkUI_TextEditorSelectionMenuOptions* options, OH_ArkUI_HapticFeedbackMode mode) | - | 设置文本编辑器中文本选择菜单的触觉反馈模式。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorSelectionMenuOptions_GetHapticFeedbackMode(OH_ArkUI_TextEditorSelectionMenuOptions* options, OH_ArkUI_HapticFeedbackMode* mode) | - | 获取文本编辑器中文本选择菜单的触觉反馈模式。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorStyledStringController_CloseSelectionMenu(OH_ArkUI_TextEditorStyledStringController* controller) | - | 关闭文本编辑器属性字符串控制器的文本选择菜单。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorStyledStringController_GetSelection(const OH_ArkUI_TextEditorStyledStringController* controller, uint32_t* start, uint32_t* end) | - | 通过属性字符串控制器获取选中区域。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorStyledStringController_SetStyledString(const OH_ArkUI_TextEditorStyledStringController* controller, const ArkUI_StyledString_Descriptor* descriptor) | - | 通过属性字符串控制器设置显示的属性字符串。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorStyledStringController_GetStyledString(const OH_ArkUI_TextEditorStyledStringController* controller, ArkUI_StyledString_Descriptor* descriptor) | - | 通过属性字符串控制器获取显示的属性字符串。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorStyledStringController_SetStyledPlaceholder(const OH_ArkUI_TextEditorStyledStringController* controller, const ArkUI_StyledString_Descriptor* descriptor) | - | 通过属性字符串控制器设置属性字符串样式的提示文本。 |
| ArkUI_ErrorCode OH_ArkUI_TextEditorStyledStringController_ScrollToVisible(const OH_ArkUI_TextEditorStyledStringController* controller, int32_t start, int32_t end) | - | 通过属性字符串控制器使指定起始索引至结束索引范围内的内容滚动至可视区域。 |
| ArkUI_ErrorCode OH_ArkUI_TextController_SetStyledString(OH_ArkUI_TextController* controller, ArkUI_StyledString_Descriptor* descriptor) | - | 设置文本组件的属性字符串。 |
| OH_ArkUI_LinearGradientOptions* OH_ArkUI_LinearGradientOptions_Create() | - | 创建线性渐变效果选项对象。 |
| void OH_ArkUI_LinearGradientOptions_Destroy(OH_ArkUI_LinearGradientOptions* options) | - | 销毁线性渐变效果选项对象。 |
| ArkUI_ErrorCode OH_ArkUI_LinearGradientOptions_SetAngle(OH_ArkUI_LinearGradientOptions* options, float angle) | - | 设置线性渐变效果选项的角度。 |
| ArkUI_ErrorCode OH_ArkUI_LinearGradientOptions_GetAngle(const OH_ArkUI_LinearGradientOptions* options, float* angle) | - | 获取线性渐变效果选项的角度。 |
| ArkUI_ErrorCode OH_ArkUI_LinearGradientOptions_SetDirection(OH_ArkUI_LinearGradientOptions* options, ArkUI_LinearGradientDirection direction) | - | 设置线性渐变选项的方向。 |
| ArkUI_ErrorCode OH_ArkUI_LinearGradientOptions_GetDirection(const OH_ArkUI_LinearGradientOptions* options, ArkUI_LinearGradientDirection* direction) | - | 获取线性渐变选项的方向。 |
| ArkUI_ErrorCode OH_ArkUI_LinearGradientOptions_SetRepeating(OH_ArkUI_LinearGradientOptions* options, bool repeating) | - | 设置颜色是否在线性渐变选项中重复。 |
| ArkUI_ErrorCode OH_ArkUI_LinearGradientOptions_GetRepeating(const OH_ArkUI_LinearGradientOptions* options, bool* repeating) | - | 获取线性渐变选项中颜色是否重复。 |
| ArkUI_ErrorCode OH_ArkUI_LinearGradientOptions_SetColorStop(OH_ArkUI_LinearGradientOptions* options, const uint32_t* colors, const float* stops, int32_t colorsAndStopsSize) | - | 设置线性渐变选项的颜色停止点。 |
| ArkUI_ErrorCode OH_ArkUI_LinearGradientOptions_GetColorStop(const OH_ArkUI_LinearGradientOptions* options, uint32_t* colors, float* stops, int32_t colorsAndStopsSize, int32_t* writeLength) | - | 获取线性渐变选项的颜色停止点。 |
| OH_ArkUI_RadialGradientOptions* OH_ArkUI_RadialGradientOptions_Create() | - | 创建一个径向渐变选项对象。 |
| void OH_ArkUI_RadialGradientOptions_Destroy(OH_ArkUI_RadialGradientOptions* options) | - | 销毁一个径向渐变选项对象。 |
| ArkUI_ErrorCode OH_ArkUI_RadialGradientOptions_SetCenterX(OH_ArkUI_RadialGradientOptions* options, float centerX) | - | 设置径向渐变选项中心点的X坐标。 |
| ArkUI_ErrorCode OH_ArkUI_RadialGradientOptions_GetCenterX(const OH_ArkUI_RadialGradientOptions* options, float* centerX) | - | 获取径向渐变选项的中心点的X坐标。 |
| ArkUI_ErrorCode OH_ArkUI_RadialGradientOptions_SetCenterY(OH_ArkUI_RadialGradientOptions* options, float centerY) | - | 设置径向渐变选项中心点的Y坐标。 |
| ArkUI_ErrorCode OH_ArkUI_RadialGradientOptions_GetCenterY(const OH_ArkUI_RadialGradientOptions* options, float* centerY) | - | 获取径向渐变选项的中心点的Y坐标。 |
| ArkUI_ErrorCode OH_ArkUI_RadialGradientOptions_SetRadius(OH_ArkUI_RadialGradientOptions* options, float radius) | - | 设置径向渐变选项的半径。 |
| ArkUI_ErrorCode OH_ArkUI_RadialGradientOptions_GetRadius(const OH_ArkUI_RadialGradientOptions* options, float* radius) | - | 获取径向渐变选项的半径。 |
| ArkUI_ErrorCode OH_ArkUI_RadialGradientOptions_SetRepeating(OH_ArkUI_RadialGradientOptions* options, bool repeating) | - | 设置径向渐变选项中颜色是否重复。 |
| ArkUI_ErrorCode OH_ArkUI_RadialGradientOptions_GetRepeating(const OH_ArkUI_RadialGradientOptions* options, bool* repeating) | - | 获取径向渐变选项中颜色是否重复的设置。 |
| ArkUI_ErrorCode OH_ArkUI_RadialGradientOptions_SetColorStop(OH_ArkUI_RadialGradientOptions* options, const uint32_t* colors, const float* stops, int32_t colorsAndStopsSize) | - | 设置径向渐变选项的颜色停止点。 |
| ArkUI_ErrorCode OH_ArkUI_RadialGradientOptions_GetColorStop(const OH_ArkUI_RadialGradientOptions* options, uint32_t* colors, float* stops, int32_t colorsAndStopsSize, int32_t* writeLength) | - | 获取径向渐变选项的颜色停止点。 |




#### 枚举类型说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV



#### ArkUI_CopyOptions

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_CopyOptions
```

**描述：**

定义文本复制粘贴模式枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_COPY_OPTIONS_NONE = 0 | 不支持复制。 |
| ARKUI_COPY_OPTIONS_IN_APP = 1 | 支持应用内复制。 |
| ARKUI_COPY_OPTIONS_LOCAL_DEVICE = 2 | 支持设备内复制。 |
| ARKUI_COPY_OPTIONS_CROSS_DEVICE = 3 | 支持跨设备复制。 |




#### ArkUI_AccessibilityCheckedState

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_AccessibilityCheckedState
```

**描述：**

定义无障碍复选框状态类型枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_ACCESSIBILITY_UNCHECKED = 0 | 复选框未被选中。 |
| ARKUI_ACCESSIBILITY_CHECKED = 1 | 复选框被选中。 |




#### ArkUI_AccessibilityActionType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_AccessibilityActionType
```

**描述：**

定义无障碍操作类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_ACCESSIBILITY_ACTION_CLICK = 1 << 0 | 点击操作。 |
| ARKUI_ACCESSIBILITY_ACTION_LONG_CLICK = 1 << 1 | 长按操作。 |
| ARKUI_ACCESSIBILITY_ACTION_CUT = 1 << 2 | 剪切操作。 |
| ARKUI_ACCESSIBILITY_ACTION_COPY = 1 << 3 | 复制操作。 |
| ARKUI_ACCESSIBILITY_ACTION_PASTE = 1 << 4 | 粘贴操作。 |




#### ArkUI_BorderStyle

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_BorderStyle
```

**描述：**

边框线条样式枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_BORDER_STYLE_SOLID = 0 | 显示为一条实线，该值为默认值。 |
| ARKUI_BORDER_STYLE_DASHED = 1 | 显示为一系列短的方形虚线。 |
| ARKUI_BORDER_STYLE_DOTTED = 2 | 显示为一系列圆点。 |




#### ArkUI_AccessibilityMode

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_AccessibilityMode
```

**描述：**

定义无障碍辅助服务模式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_ACCESSIBILITY_MODE_AUTO = 0 | 根据组件不同会转换为“enabled”或者“disabled”。 |
| ARKUI_ACCESSIBILITY_MODE_ENABLED = 1 | 当前组件可被无障碍辅助服务所识别。 |
| ARKUI_ACCESSIBILITY_MODE_DISABLED = 2 | 当前组件不可被无障碍辅助服务所识别。 |
| ARKUI_ACCESSIBILITY_MODE_DISABLED_FOR_DESCENDANTS = 3 | 当前组件及其所有子组件不可被无障碍辅助服务所识别。 |




#### ArkUI_AdaptiveColor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_AdaptiveColor
```

**描述：**

定义取色模式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_ADAPTIVE_COLOR_DEFAULT = 0 | 不使用取色模糊。 |
| ARKUI_ADAPTIVE_COLOR_AVERAGE = 1 | 使用取色模糊。 |




#### ArkUI_ColorMode

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_ColorMode
```

**描述：**

定义深浅色模式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_COLOR_MODE_SYSTEM = 0 | 跟随系统深浅色模式。 |
| ARKUI_COLOR_MODE_LIGHT = 1 | 固定使用浅色模式。 |
| ARKUI_COLOR_MODE_DARK = 2 | 固定使用深色模式。 |




#### ArkUI_SystemColorMode

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_SystemColorMode
```

**描述：**

定义系统深浅色模式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_SYSTEM_COLOR_MODE_LIGHT = 0 | 浅色模式。 |
| ARKUI_SYSTEM_COLOR_MODE_DARK = 1 | 深色模式。 |




#### ArkUI_LengthMetricUnit

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_LengthMetricUnit
```

**描述：**

定义组件的单位模式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_LENGTH_METRIC_UNIT_DEFAULT = -1 | 默认，字体类单位为fp，非字体类单位为vp。 |
| ARKUI_LENGTH_METRIC_UNIT_PX = 0 | 单位为px。 |
| ARKUI_LENGTH_METRIC_UNIT_VP = 1 | 单位为vp。 |
| ARKUI_LENGTH_METRIC_UNIT_FP = 2 | 单位为fp。 |




#### ArkUI_ListItemSwipeActionState

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_ListItemSwipeActionState
```

**描述：**

定义[Listitem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-listitem#listitem10)组件[SwipeAction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-listitem#swipeaction9)方法的显隐模式，默认值为ARKUI_LIST_ITEM_SWIPE_ACTION_STATE_COLLAPSED。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_LIST_ITEM_SWIPE_ACTION_STATE_COLLAPSED = 0 | 收起状态，当ListItem与主轴方向相反滑动时操作项处于隐藏状态。 |
| ARKUI_LIST_ITEM_SWIPE_ACTION_STATE_EXPANDED = 1 | 展开状态，当ListItem与主轴方向相反滑动时操作项处于显示状态。 |
| ARKUI_LIST_ITEM_SWIPE_ACTION_STATE_ACTIONING = 2 | 长距离状态，当ListItem进入长距删除区后删除ListItem的状态。 |




#### ArkUI_ListItemSwipeEdgeEffect

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_ListItemSwipeEdgeEffect
```

**描述：**

定义Listitem组件[swipeAction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-listitem#swipeaction9)方法的滚动模式，默认值为ARKUI_LIST_ITEM_SWIPE_EDGE_EFFECT_SPRING。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_LIST_ITEM_SWIPE_EDGE_EFFECT_SPRING = 0 | ListItem划动距离超过划出组件大小后可以继续划动。 |
| ARKUI_LIST_ITEM_SWIPE_EDGE_EFFECT_NONE = 1 | ListItem划动距离不能超过划出组件大小。 |




#### ArkUI_ListItemSwipeActionDirection

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_ListItemSwipeActionDirection
```

**描述：**

ListItem划出菜单的展开方向。

**起始版本：** 21

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_LIST_ITEM_SWIPE_ACTION_DIRECTION_START = 0 | 当列表方向是垂直方向时，LTR模式下表示ListItem的左边，RTL模式下表示ListItem的右边。当列表是水平方向时，表示ListItem的上边。 |
| ARKUI_LIST_ITEM_SWIPE_ACTION_DIRECTION_END = 1 | 当列表方向是垂直方向时，LTR模式下表示ListItem的右边，RTL模式下表示ListItem的左边。当列表是水平方向时，表示ListItem的下边。 |




#### ArkUI_CrownSensitivity

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_CrownSensitivity
```

**描述：**

定义表冠灵敏度枚举值。

**起始版本：** 26.0.0

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_CROWN_SENSITIVITY_LOW = 0 | 低灵敏度。 |
| ARKUI_CROWN_SENSITIVITY_MEDIUM = 1 | 中等灵敏度。 |
| ARKUI_CROWN_SENSITIVITY_HIGH = 2 | 高灵敏度。 |




#### ArkUI_SafeAreaType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_SafeAreaType
```

**描述：**

定义扩展安全区域的枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_SAFE_AREA_TYPE_SYSTEM = 1 | 系统默认非安全区域，包括状态栏、导航栏，该值为默认值。 |
| ARKUI_SAFE_AREA_TYPE_CUTOUT = 1 << 1 | 设备的非安全区域，例如刘海屏或挖孔屏区域。 |
| ARKUI_SAFE_AREA_TYPE_KEYBOARD = 1 << 2 | 软键盘区域。 |




#### ArkUI_KeyboardAvoidMode

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_KeyboardAvoidMode
```

**描述：**

键盘避让模式。

**起始版本：** 15

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_KEYBOARD_AVOID_MODE_DEFAULT = 0 | 默认避让软键盘并在到达极限高度之后进行高度压缩。 |
| ARKUI_KEYBOARD_AVOID_MODE_NONE = 1 | 不避让键盘。 |




#### ArkUI_HoverModeAreaType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_HoverModeAreaType
```

**描述：**

悬停态显示区域。

**起始版本：** 15

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_HOVER_MODE_AREA_TYPE_TOP = 0 | 上半屏。 |
| ARKUI_HOVER_MODE_AREA_TYPE_BOTTOM = 1 | 下半屏。 |




#### ArkUI_ExpandMode

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_ExpandMode
```

**描述：**

定义子节点展开模式枚举值。

**起始版本：** 15

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_NOT_EXPAND = 0 | 不展开。 |
| ARKUI_EXPAND = 1 | 展开。 |
| ARKUI_LAZY_EXPAND = 2 | 懒展开，按需展开当前节点的子节点，节点展开条件可以参考LazyForEach：数据懒加载。 |




#### ArkUI_FocusWrapMode

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_FocusWrapMode
```

**描述：**

组件走焦换行规则。Grid、List组件默认值为ARKUI_FOCUS_WRAP_MODE_DEFAULT。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_FOCUS_WRAP_MODE_DEFAULT = 0 | 默认规则，使用方向键走焦不换行。 |
| ARKUI_FOCUS_WRAP_WITH_ARROW = 1 | 使用方向键走焦自动换行。 |




#### ArkUI_ItemFillPolicy

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_ItemFillPolicy
```

**描述：**

为不同响应式[断点规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-grid-layout#栅格容器断点)指定列数。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_ITEMFILLPOLICY_NONE = -1 | 没有设置响应式断点规格。 |
| ARKUI_ITEMFILLPOLICY_DEFAULT = 0 | 针对List和Swiper组件：在组件宽度属于sm及更小的断点区间时显示1列，属于md断点区间时显示2列，属于lg及更大的断点区间时显示3列。 针对Grid和WaterFlow组件：在组件宽度属于sm及更小的断点区间时显示2列，属于md断点区间时显示3列，属于lg及更大的断点区间时显示5列。 |
| ARKUI_ITEMFILLPOLICY_SM1MD2LG3 = 1 | 在组件宽度属于sm及更小的断点区间时显示1列，属于md断点区间时显示2列，属于lg及更大的断点区间时显示3列。 |
| ARKUI_ITEMFILLPOLICY_SM2MD3LG5 = 2 | 在组件宽度属于sm及更小的断点区间时显示2列，属于md断点区间时显示3列，属于lg及更大的断点区间时显示5列。 |




#### ArkUI_EdgeDirection

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_EdgeDirection
```

**描述：**

定义矩形边方向。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_EDGE_DIRECTION_ALL = 0 | 设置四个方向的内容。 |
| ARKUI_EDGE_DIRECTION_LEFT = 1 << 0 | 设置左侧方向内容。 |
| ARKUI_EDGE_DIRECTION_RIGHT = 1 << 1 | 设置右侧方向内容。 |
| ARKUI_EDGE_DIRECTION_TOP = 1 << 2 | 设置上侧方向内容。 |
| ARKUI_EDGE_DIRECTION_BOTTOM = 1 << 3 | 设置下侧方向内容。 |




#### ArkUI_CornerDirection

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_CornerDirection
```

**描述：**

定义角度方向。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_CORNER_DIRECTION_ALL = 0 | 设置四个角度方向的内容。 |
| ARKUI_CORNER_DIRECTION_TOP_LEFT = 1 << 0 | 设置左上侧方向内容。 |
| ARKUI_CORNER_DIRECTION_TOP_RIGHT = 1 << 1 | 设置右上侧方向内容。 |
| ARKUI_CORNER_DIRECTION_BOTTOM_LEFT = 1 << 2 | 设置左下侧方向内容。 |
| ARKUI_CORNER_DIRECTION_BOTTOM_RIGHT = 1 << 3 | 设置右下侧方向内容。 |




#### ArkUI_MenuPolicy

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_MenuPolicy
```

**描述：**

菜单弹出策略。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_MENU_POLICY_DEFAULT = 0 | 根据底层默认逻辑确定是否弹出菜单。 |
| ARKUI_MENU_POLICY_HIDE = 1 | 不弹出菜单。 |
| ARKUI_MENU_POLICY_SHOW = 2 | 弹出菜单。 |




#### ArkUI_RenderStrategy

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_RenderStrategy
```

**描述：**

定义组件绘制圆角的模式。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_RENDERSTRATEGY_FAST = 0 | 在线绘制模式。 |
| ARKUI_RENDERSTRATEGY_OFFSCREEN = 1 | 离屏绘制模式。 |




#### OH_ArkUI_CrossLanguageOperatingStatus

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum OH_ArkUI_CrossLanguageOperatingStatus
```

**描述**

跨语言配置项的节点树操作状态。

**起始版本：** 26.0.0

| 枚举项 | 描述 |
| --- | --- |
| OH_ARKUI_TREE_OPERATING_STATUS_UNDEFINED = 0 | 未定义，节点树操作状态的初始值。处于此状态的节点不支持跨语言节点树操作。 |
| OH_ARKUI_TREE_OPERATING_STATUS_ENABLE = 1 | 启用，表示当该配置项应用到节点时，节点的节点树操作状态将被启用。 |
| OH_ARKUI_TREE_OPERATING_STATUS_DISABLE = 2 | 禁用，表示当该配置项应用到节点时，节点的节点树操作状态将被禁用。 |




#### OH_ArkUI_NodeMountPolicy

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum OH_ArkUI_NodeMountPolicy
```

**描述**

子节点挂载策略类型枚举。

**起始版本：** 26.0.0

| 枚举项 | 描述 |
| --- | --- |
| OH_ARKUI_NODE_MOUNT_POLICY_SINGLE_IF_RENDER_NODE = 0 | 如果需要将RenderNode作为子节点挂载，此RenderNode必须是唯一子节点。 |
| OH_ARKUI_NODE_MOUNT_POLICY_MIXED = 1 | 允许同时挂载多个typeNode与RenderNode。 |




#### 函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV



#### OH_ArkUI_LayoutConstraint_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_LayoutConstraint* OH_ArkUI_LayoutConstraint_Create()
```

**描述：**

创建布局约束。创建的布局约束指针需在使用完毕后调用[OH_ArkUI_LayoutConstraint_Dispose](#oh_arkui_layoutconstraint_dispose)释放，未释放会导致内存泄漏。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_LayoutConstraint* | 创建布局约束的指针。 |




#### OH_ArkUI_LayoutConstraint_Copy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_LayoutConstraint* OH_ArkUI_LayoutConstraint_Copy(const ArkUI_LayoutConstraint* Constraint)
```

**描述：**

布局约束深拷贝。深拷贝返回的新布局约束指针与原指针相互独立，需在使用完毕后分别调用[OH_ArkUI_LayoutConstraint_Dispose](#oh_arkui_layoutconstraint_dispose)释放。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_LayoutConstraint* Constraint | 布局约束的指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_LayoutConstraint* | 新的布局约束指针。 |




#### OH_ArkUI_LayoutConstraint_Dispose()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void* OH_ArkUI_LayoutConstraint_Dispose(ArkUI_LayoutConstraint* Constraint)
```

**描述：**

销毁布局约束指针。必须与[OH_ArkUI_LayoutConstraint_Create](#oh_arkui_layoutconstraint_create)或[OH_ArkUI_LayoutConstraint_Copy](#oh_arkui_layoutconstraint_copy)配对使用，每个布局约束指针只能销毁一次，销毁后不应再使用该指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_LayoutConstraint* Constraint | 布局约束的指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| void* | 空指针。 |




#### OH_ArkUI_LayoutConstraint_GetMaxWidth()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_LayoutConstraint_GetMaxWidth(const ArkUI_LayoutConstraint* Constraint)
```

**描述：**

通过布局约束获取最大宽度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_LayoutConstraint* Constraint | 布局约束的指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| int32_t | 最大宽度，单位为px。 |




#### OH_ArkUI_LayoutConstraint_GetMinWidth()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_LayoutConstraint_GetMinWidth(const ArkUI_LayoutConstraint* Constraint)
```

**描述：**

通过布局约束获取最小宽度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_LayoutConstraint* Constraint | 布局约束的指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| int32_t | 最小宽度，单位为px。 |




#### OH_ArkUI_LayoutConstraint_GetMaxHeight()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_LayoutConstraint_GetMaxHeight(const ArkUI_LayoutConstraint* Constraint)
```

**描述：**

通过布局约束获取最大高度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_LayoutConstraint* Constraint | 布局约束的指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| int32_t | 最大高度，单位为px。 |




#### OH_ArkUI_LayoutConstraint_GetMinHeight()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_LayoutConstraint_GetMinHeight(const ArkUI_LayoutConstraint* Constraint)
```

**描述：**

通过布局约束获取最小高度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_LayoutConstraint* Constraint | 布局约束的指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| int32_t | 最小高度，单位为px。 |




#### OH_ArkUI_LayoutConstraint_GetPercentReferenceWidth()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_LayoutConstraint_GetPercentReferenceWidth(const ArkUI_LayoutConstraint* Constraint)
```

**描述：**

通过布局约束获取宽度百分比基准。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_LayoutConstraint* Constraint | 布局约束的指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| int32_t | 宽度百分比基准。 |




#### OH_ArkUI_LayoutConstraint_GetPercentReferenceHeight()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_LayoutConstraint_GetPercentReferenceHeight(const ArkUI_LayoutConstraint* Constraint)
```

**描述：**

通过布局约束获取高度百分比基准。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_LayoutConstraint* Constraint | 布局约束的指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| int32_t | 高度百分比基准。 |




#### OH_ArkUI_LayoutConstraint_SetMaxWidth()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_LayoutConstraint_SetMaxWidth(ArkUI_LayoutConstraint* Constraint, int32_t value)
```

**描述：**

设置最大宽度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_LayoutConstraint* Constraint | 布局约束的指针。 |
| int32_t value | 最大宽度，单位为px，取值范围：[0, +∞)。 |




#### OH_ArkUI_LayoutConstraint_SetMinWidth()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_LayoutConstraint_SetMinWidth(ArkUI_LayoutConstraint* Constraint, int32_t value)
```

**描述：**

设置最小宽度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_LayoutConstraint* Constraint | 布局约束的指针。 |
| int32_t value | 最小宽度，单位为px，取值范围：[0, +∞)。 |




#### OH_ArkUI_LayoutConstraint_SetMaxHeight()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_LayoutConstraint_SetMaxHeight(ArkUI_LayoutConstraint* Constraint, int32_t value)
```

**描述：**

设置最大高度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_LayoutConstraint* Constraint | 布局约束的指针。 |
| int32_t value | 最大高度，单位为px，取值范围：[0, +∞)。 |




#### OH_ArkUI_LayoutConstraint_SetMinHeight()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_LayoutConstraint_SetMinHeight(ArkUI_LayoutConstraint* Constraint, int32_t value)
```

**描述：**

设置最小高度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_LayoutConstraint* Constraint | 布局约束的指针。 |
| int32_t value | 最小高度，单位为px，取值范围：[0, +∞)。 |




#### OH_ArkUI_LayoutConstraint_SetPercentReferenceWidth()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_LayoutConstraint_SetPercentReferenceWidth(ArkUI_LayoutConstraint* Constraint, int32_t value)
```

**描述：**

设置宽度百分比基准。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_LayoutConstraint* Constraint | 布局约束的指针。 |
| int32_t value | 宽度百分比基准，取值范围：[0, +∞)。 |




#### OH_ArkUI_LayoutConstraint_SetPercentReferenceHeight()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_LayoutConstraint_SetPercentReferenceHeight(ArkUI_LayoutConstraint* Constraint, int32_t value)
```

**描述：**

设置高度百分比基准。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_LayoutConstraint* Constraint | 布局约束的指针。 |
| int32_t value | 高度百分比基准，取值范围：[0, +∞)。 |




#### OH_ArkUI_DrawContext_GetCanvas()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void* OH_ArkUI_DrawContext_GetCanvas(ArkUI_DrawContext* context)
```

**描述：**

获取绘制canvas指针，可以转换为图形库的[OH_Drawing_Canvas](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-canvas)指针进行绘制。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DrawContext* context | 绘制上下文。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| void* | 用于绘制的canvas指针。 |




#### OH_ArkUI_DrawContext_GetSize()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_IntSize OH_ArkUI_DrawContext_GetSize(ArkUI_DrawContext* context)
```

**描述：**

获取可绘制区域大小。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DrawContext* context | 绘制上下文。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_IntSize | 可绘制区域大小。 |




#### OH_ArkUI_SwiperDigitIndicator_SetFontWeight()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SwiperDigitIndicator_SetFontWeight(ArkUI_SwiperDigitIndicator *indicator, ArkUI_FontWeight fontWeight)
```

**描述：**

设置Swiper组件数字导航指示器字体粗细属性。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator *indicator | 数字导航指示器对象指针。 |
| ArkUI_FontWeight fontWeight | 字体粗细样式ArkUI_FontWeight。 |




#### OH_ArkUI_SwiperDigitIndicator_GetFontWeight()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_FontWeight OH_ArkUI_SwiperDigitIndicator_GetFontWeight(ArkUI_SwiperDigitIndicator* indicator)
```

**描述：**

获取Swiper组件数字导航指示器字体粗细属性。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_FontWeight | 字体粗细样式ArkUI_FontWeight。 |




#### OH_ArkUI_SwiperDigitIndicator_SetSelectedFontWeight()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SwiperDigitIndicator_SetSelectedFontWeight(ArkUI_SwiperDigitIndicator *indicator, ArkUI_FontWeight selectedFontWeight)
```

**描述：**

设置被选中Swiper组件数字导航指示器字体粗细属性。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator *indicator | 数字导航指示器对象指针。 |
| ArkUI_FontWeight selectedFontWeight | 字体粗细样式ArkUI_FontWeight。 |




#### OH_ArkUI_SwiperDigitIndicator_GetSelectedFontWeight()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_FontWeight OH_ArkUI_SwiperDigitIndicator_GetSelectedFontWeight(ArkUI_SwiperDigitIndicator* indicator)
```

**描述：**

获取被选中Swiper组件数字导航指示器字体粗细属性。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SwiperDigitIndicator* indicator | 数字导航指示器对象指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_FontWeight | 字体粗细样式ArkUI_FontWeight。 |




#### OH_ArkUI_ListItemSwipeActionItem_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ListItemSwipeActionItem* OH_ArkUI_ListItemSwipeActionItem_Create()
```

**描述：**

创建ListItemSwipeActionItem接口设置的配置项。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ListItemSwipeActionItem* | ListItemSwipeActionItem配置项实例。 |




#### OH_ArkUI_ListItemSwipeActionItem_Dispose()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_ListItemSwipeActionItem_Dispose(ArkUI_ListItemSwipeActionItem* item)
```

**描述：**

销毁ListItemSwipeActionItem实例。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionItem* item | 要销毁的ListItemSwipeActionItem实例。 |




#### OH_ArkUI_ListItemSwipeActionItem_SetContent()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_ListItemSwipeActionItem_SetContent(ArkUI_ListItemSwipeActionItem* item, ArkUI_NodeHandle node)
```

**描述：**

设置ListItemSwipeActionItem的布局内容。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionItem* item | ListItemSwipeActionItem实例。 |
| ArkUI_NodeHandle node | 布局信息。 |




#### OH_ArkUI_ListItemSwipeActionItem_SetActionAreaDistance()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_ListItemSwipeActionItem_SetActionAreaDistance(ArkUI_ListItemSwipeActionItem* item, float distance)
```

**描述：**

设置组件长距离滑动删除距离阈值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionItem* item | ListItemSwipeActionItem实例。 |
| float distance | 组件长距离滑动删除距离阈值，单位vp。 |




#### OH_ArkUI_ListItemSwipeActionItem_GetActionAreaDistance()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float OH_ArkUI_ListItemSwipeActionItem_GetActionAreaDistance(ArkUI_ListItemSwipeActionItem* item)
```

**描述：**

获取组件长距离滑动删除距离阈值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionItem* item | ListItemSwipeActionItem实例。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 组件长距离滑动删除距离阈值，单位vp，异常时返回值：0。 |




#### OH_ArkUI_ListItemSwipeActionItem_SetOnEnterActionArea()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_ListItemSwipeActionItem_SetOnEnterActionArea(ArkUI_ListItemSwipeActionItem* item, void (*callback)())
```

**描述：**

设置滑动条目进入删除区域时调用的事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionItem* item | ListItemSwipeActionItem实例。 |
| callback | 回调事件。 |




#### OH_ArkUI_ListItemSwipeActionItem_SetOnEnterActionAreaWithUserData()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_ListItemSwipeActionItem_SetOnEnterActionAreaWithUserData(ArkUI_ListItemSwipeActionItem* item,void* userData, void (*callback)(void* userData))
```

**描述：**

设置滑动条目进入删除区域时调用的事件，回调事件会传入用户自定义数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionItem* item | ListItemSwipeActionItem实例。 |
| void* userData | 用户自定义数据。 |
| callback | 回调事件。 |




#### OH_ArkUI_ListItemSwipeActionItem_SetOnAction()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_ListItemSwipeActionItem_SetOnAction(ArkUI_ListItemSwipeActionItem* item, void (*callback)())
```

**描述：**

设置组件进入长距删除区后删除[ListItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-listitem)时调用的事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionItem* item | ListItemSwipeActionItem实例。 |
| callback | 回调事件。 |




#### OH_ArkUI_ListItemSwipeActionItem_SetOnActionWithUserData()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_ListItemSwipeActionItem_SetOnActionWithUserData(ArkUI_ListItemSwipeActionItem* item,void* userData, void (*callback)(void* userData))
```

**描述：**

设置组件进入长距删除区后删除ListItem时调用的事件，回调事件会传入用户自定义数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionItem* item | ListItemSwipeActionItem实例。 |
| void* userData | 用户自定义数据。 |
| callback | 回调事件。 |




#### OH_ArkUI_ListItemSwipeActionItem_SetOnExitActionArea()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_ListItemSwipeActionItem_SetOnExitActionArea(ArkUI_ListItemSwipeActionItem* item, void (*callback)())
```

**描述：**

设置滑动条目退出删除区域时调用的事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionItem* item | ListItemSwipeActionItem实例。 |
| callback | 回调事件。 |




#### OH_ArkUI_ListItemSwipeActionItem_SetOnExitActionAreaWithUserData()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_ListItemSwipeActionItem_SetOnExitActionAreaWithUserData(ArkUI_ListItemSwipeActionItem* item,void* userData, void (*callback)(void* userData))
```

**描述：**

设置滑动条目退出删除区域时调用的事件，回调事件会传入用户自定义数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionItem* item | ListItemSwipeActionItem实例。 |
| void* userData | 用户自定义数据。 |
| callback | 回调事件。 |




#### OH_ArkUI_ListItemSwipeActionItem_SetOnStateChange()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_ListItemSwipeActionItem_SetOnStateChange(ArkUI_ListItemSwipeActionItem* item,void (*callback)(ArkUI_ListItemSwipeActionState swipeActionState))
```

**描述：**

设置列表项滑动状态变化时候触发的事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionItem* item | ListItemSwipeActionItem实例。 |
| callback | 回调事件。传入参数为swipeActionState，表示列表项滑动状态。 |




#### OH_ArkUI_ListItemSwipeActionItem_SetOnStateChangeWithUserData()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_ListItemSwipeActionItem_SetOnStateChangeWithUserData(ArkUI_ListItemSwipeActionItem* item,void* userData, void (*callback)(ArkUI_ListItemSwipeActionState swipeActionState, void* userData))
```

**描述：**

设置列表项滑动状态变化时候触发的事件，回调事件会传入用户自定义数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionItem* item | ListItemSwipeActionItem实例。 |
| void* userData | 用户自定义数据。 |
| callback | 回调事件。传入参数为swipeActionState，表示列表项滑动状态。 |




#### OH_ArkUI_ListItemSwipeActionOption_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ListItemSwipeActionOption* OH_ArkUI_ListItemSwipeActionOption_Create()
```

**描述：**

创建ListItemSwipeActionOption接口设置的配置项。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ListItemSwipeActionOption* | ListItemSwipeActionOption配置项实例。 |




#### OH_ArkUI_ListItemSwipeActionOption_Dispose()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_ListItemSwipeActionOption_Dispose(ArkUI_ListItemSwipeActionOption* option)
```

**描述：**

销毁ListItemSwipeActionOption实例。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionOption* option | 要销毁的ListItemSwipeActionOption实例。 |




#### OH_ArkUI_ListItemSwipeActionOption_SetStart()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_ListItemSwipeActionOption_SetStart(ArkUI_ListItemSwipeActionOption* option, ArkUI_ListItemSwipeActionItem* item)
```

**描述：**

设置ListItemSwipeActionItem的左侧（垂直布局）或上方（横向布局）布局内容。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionOption* option | ListItemSwipeActionOption实例。 |
| ArkUI_ListItemSwipeActionItem* item | 布局信息。 |




#### OH_ArkUI_ListItemSwipeActionOption_SetEnd()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_ListItemSwipeActionOption_SetEnd(ArkUI_ListItemSwipeActionOption* option,ArkUI_ListItemSwipeActionItem* item)
```

**描述：**

设置ListItemSwipeActionItem的右侧（垂直布局）或下方（横向布局）布局内容。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionOption* option | ListItemSwipeActionOption实例。 |
| ArkUI_ListItemSwipeActionItem* item | 布局信息。 |




#### OH_ArkUI_ListItemSwipeActionOption_SetEdgeEffect()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_ListItemSwipeActionOption_SetEdgeEffect(ArkUI_ListItemSwipeActionOption* option,ArkUI_ListItemSwipeEdgeEffect edgeEffect)
```

**描述：**

设置边缘滑动效果。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionOption* option | ListItemSwipeActionOption实例。 |
| ArkUI_ListItemSwipeEdgeEffect edgeEffect | 边缘滑动效果。 |




#### OH_ArkUI_ListItemSwipeActionOption_GetEdgeEffect()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_ListItemSwipeActionOption_GetEdgeEffect(ArkUI_ListItemSwipeActionOption* option)
```

**描述：**

获取边缘滑动效果。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionOption* option | ListItemSwipeActionOption实例。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| int32_t | 边缘滑动效果。默认返回值：ARKUI_LIST_ITEM_SWIPE_EDGE_EFFECT_SPRING。 |




#### OH_ArkUI_ListItemSwipeActionOption_SetOnOffsetChange()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_ListItemSwipeActionOption_SetOnOffsetChange(ArkUI_ListItemSwipeActionOption* option,void (*callback)(float offset))
```

**描述：**

滑动操作偏移量更改时调用的事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionOption* option | ListItemSwipeActionOption实例。 |
| callback | 回调事件。offset 滑动偏移量，单位vp。 |




#### OH_ArkUI_ListItemSwipeActionOption_SetOnOffsetChangeWithUserData()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_ListItemSwipeActionOption_SetOnOffsetChangeWithUserData(ArkUI_ListItemSwipeActionOption* option,void* userData, void (*callback)(float offset, void* userData))
```

**描述：**

滑动操作偏移量更改时调用的事件，回调事件会传入用户自定义数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ListItemSwipeActionOption* option | ListItemSwipeActionOption实例。 |
| void* userData | 用户自定义数据。 |
| callback | 回调事件。offset 滑动偏移量，单位vp。 |




#### OH_ArkUI_ListItemSwipeAction_Expand()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_ListItemSwipeAction_Expand(ArkUI_NodeHandle node, ArkUI_ListItemSwipeActionDirection direction)
```

**描述：**

展开指定ListItem的划出菜单。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | ListItem节点对象。 |
| ArkUI_ListItemSwipeActionDirection direction | ListItem划出菜单的展开方向。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 ARKUI_ERROR_CODE_PARAM_ERROR 传入的节点对象类型错误。 ARKUI_ERROR_CODE_NODE_NOT_ON_MAIN_TREE 传入的节点未挂载到组件树上。 |


> [!NOTE]
> 如果List组件NODE_LIST_CACHED_COUNT属性设置显示预加载ListItem，List显示区域外已预加载完成的ListItem支持展开，否则List显示区域外节点不支持展开。




#### OH_ArkUI_ListItemSwipeAction_Collapse()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_ListItemSwipeAction_Collapse(ArkUI_NodeHandle node)
```

**描述：**

收起指定ListItem的划出菜单。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | ListItem节点对象。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 ARKUI_ERROR_CODE_PARAM_ERROR 传入的节点对象类型错误。 ARKUI_ERROR_CODE_NODE_NOT_ON_MAIN_TREE 传入的节点未挂载到组件树上。 |




#### OH_ArkUI_AccessibilityState_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_AccessibilityState* OH_ArkUI_AccessibilityState_Create(void)
```

**描述：**

创建无障碍状态。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_AccessibilityState* | 无障碍状态对象指针。如果对象返回空指针，表示创建失败，失败的可能原因是应用地址空间满。 |




#### OH_ArkUI_AccessibilityState_Dispose()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_AccessibilityState_Dispose(ArkUI_AccessibilityState* state)
```

**描述：**

销毁无障碍状态指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityState* state | 无障碍状态对象指针。 |




#### OH_ArkUI_AccessibilityState_SetDisabled()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_AccessibilityState_SetDisabled(ArkUI_AccessibilityState* state, int32_t isDisabled)
```

**描述：**

设置无障碍状态是否禁用。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityState* state | 无障碍状态对象指针。 |
| int32_t isDisabled | 无障碍状态是否禁用， 1表示禁用，0表示不禁用，默认为0。 |




#### OH_ArkUI_AccessibilityState_IsDisabled()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_AccessibilityState_IsDisabled(ArkUI_AccessibilityState* state)
```

**描述：**

获取无障碍状态是否禁用。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityState* state | 无障碍状态对象指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| int32_t | 是否禁用， 1表示禁用，0表示未禁用，默认为0; 若state为空，返回默认值。 |




#### OH_ArkUI_AccessibilityState_SetSelected()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_AccessibilityState_SetSelected(ArkUI_AccessibilityState* state, int32_t isSelected)
```

**描述：**

设置无障碍状态是否选中。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityState* state | 无障碍状态对象指针。 |
| int32_t isSelected | 是否被选中， 1表示选中，0表示未选中，默认为0。 |




#### OH_ArkUI_AccessibilityState_IsSelected()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_AccessibilityState_IsSelected(ArkUI_AccessibilityState* state)
```

**描述：**

获取无障碍状态是否选中。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityState* state | 无障碍状态对象指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| int32_t | 是否被选中， 1表示选中，0表示未选中，默认为0; 若state为空，返回默认值。 |




#### OH_ArkUI_AccessibilityState_SetCheckedState()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_AccessibilityState_SetCheckedState(ArkUI_AccessibilityState* state, int32_t checkedState)
```

**描述：**

设置无障碍状态复选框状态。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityState* state | 无障碍状态对象指针。 |
| int32_t checkedState | 复选框状态，参数类型ArkUI_AccessibilityCheckedState, 默认值：ARKUI_ACCESSIBILITY_UNCHECKED。 |




#### OH_ArkUI_AccessibilityState_GetCheckedState()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_AccessibilityState_GetCheckedState(ArkUI_AccessibilityState* state)
```

**描述：**

获取无障碍状态复选框状态。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityState* state | 无障碍状态对象指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| int32_t | 复选框状态，参数类型ArkUI_AccessibilityCheckedState, 默认值：ARKUI_ACCESSIBILITY_UNCHECKED; 若函数参数异常，返回默认值。 |




#### OH_ArkUI_AccessibilityValue_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_AccessibilityValue* OH_ArkUI_AccessibilityValue_Create(void)
```

**描述：**

创建无障碍信息。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_AccessibilityValue* | 无障碍信息对象指针。 |




#### OH_ArkUI_AccessibilityValue_Dispose()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_AccessibilityValue_Dispose(ArkUI_AccessibilityValue* value)
```

**描述：**

销毁无障碍信息指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityValue* value | 无障碍信息对象指针。 |




#### OH_ArkUI_AccessibilityValue_SetMin()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_AccessibilityValue_SetMin(ArkUI_AccessibilityValue* value, int32_t min)
```

**描述：**

设置无障碍最小值信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityValue* value | 无障碍信息对象指针。 |
| int32_t min | 基于范围组件的最小值, 默认为-1。 |




#### OH_ArkUI_AccessibilityValue_GetMin()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_AccessibilityValue_GetMin(ArkUI_AccessibilityValue* value)
```

**描述：**

获取无障碍最小值信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityValue* value | 无障碍信息对象指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| int32_t | 基于范围组件的最小值, 默认为-1; 若函数参数异常，返回-1。 |




#### OH_ArkUI_AccessibilityValue_SetMax()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_AccessibilityValue_SetMax(ArkUI_AccessibilityValue* value, int32_t max)
```

**描述：**

设置无障碍最大值信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityValue* value | 无障碍信息对象指针。 |
| int32_t max | 基于范围组件的最大值, 默认为-1。 |




#### OH_ArkUI_AccessibilityValue_GetMax()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_AccessibilityValue_GetMax(ArkUI_AccessibilityValue* value)
```

**描述：**

获取无障碍最大值信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityValue* value | 无障碍信息对象指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| int32_t | 基于范围组件的最大值, 默认为-1; 若函数参数异常，返回-1。 |




#### OH_ArkUI_AccessibilityValue_SetCurrent()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_AccessibilityValue_SetCurrent(ArkUI_AccessibilityValue* value, int32_t current)
```

**描述：**

设置无障碍当前值信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityValue* value | 无障碍信息对象指针。 |
| int32_t current | 基于范围组件的当前值, 默认为-1。 |




#### OH_ArkUI_AccessibilityValue_GetCurrent()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_AccessibilityValue_GetCurrent(ArkUI_AccessibilityValue* value)
```

**描述：**

获取无障碍当前值信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityValue* value | 无障碍信息对象指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| int32_t | 基于范围组件的当前值, 默认为-1; 若函数参数异常，返回-1。 |




#### OH_ArkUI_AccessibilityValue_SetRangeMin()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_AccessibilityValue_SetRangeMin(ArkUI_AccessibilityValue* value, int32_t rangeMin)
```

**描述：**

设置范围组件的无障碍最小值信息。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityValue* value | 需要设置最小值的范围组件无障碍信息对象指针。 |
| int32_t rangeMin | 基于范围组件的最小值, 默认为-1。 |




#### OH_ArkUI_AccessibilityValue_GetRangeMin()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_AccessibilityValue_GetRangeMin(ArkUI_AccessibilityValue* value)
```

**描述：**

获取范围组件的无障碍最小值信息。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityValue* value | 需要获取最小值的范围组件无障碍信息对象指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| int32_t | 基于范围组件的最小值, 默认为-1; 若函数参数异常，返回-1。 |




#### OH_ArkUI_AccessibilityValue_SetRangeMax()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_AccessibilityValue_SetRangeMax(ArkUI_AccessibilityValue* value, int32_t rangeMax)
```

**描述：**

设置范围组件的无障碍最大值信息。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityValue* value | 需要设置最大值的范围组件无障碍信息对象指针。 |
| int32_t rangeMax | 基于范围组件的最大值, 默认为-1。 |




#### OH_ArkUI_AccessibilityValue_GetRangeMax()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_AccessibilityValue_GetRangeMax(ArkUI_AccessibilityValue* value)
```

**描述：**

获取范围组件的无障碍最大值信息。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityValue* value | 需要获取最小值的范围组件无障碍信息对象指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| int32_t | 基于范围组件的最大值, 默认为-1; 若函数参数异常，返回-1。 |




#### OH_ArkUI_AccessibilityValue_SetRangeCurrent()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_AccessibilityValue_SetRangeCurrent(ArkUI_AccessibilityValue* value, int32_t rangeCurrent)
```

**描述：**

用于设置范围组件的无障碍当前值信息。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityValue* value | 需要设置当前值的范围组件无障碍信息对象指针。 |
| int32_t rangeCurrent | 基于范围组件的当前值, 默认为-1。 |




#### OH_ArkUI_AccessibilityValue_GetRangeCurrent()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_AccessibilityValue_GetRangeCurrent(ArkUI_AccessibilityValue* value)
```

**描述：**

用于获取范围组件的无障碍当前值信息。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityValue* value | 需要获取当前值的范围组件无障碍信息对象指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| int32_t | 基于范围组件的当前值, 默认为-1; 若函数参数异常，返回-1。 |




#### OH_ArkUI_AccessibilityValue_SetText()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_AccessibilityValue_SetText(ArkUI_AccessibilityValue* value, const char* text)
```

**描述：**

设置无障碍文本描述信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityValue* value | 无障碍信息对象指针。 |
| const char* text | 组件的文本描述信息, 默认为空字符串。 |




#### OH_ArkUI_AccessibilityValue_GetText()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
const char* OH_ArkUI_AccessibilityValue_GetText(ArkUI_AccessibilityValue* value)
```

**描述：**

获取无障碍文本描述信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityValue* value | 无障碍信息对象指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| const char* | 组件的文本描述信息, 默认为空字符串; 若函数参数异常，返回空指针。 |




#### OH_ArkUI_CustomProperty_Destroy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_CustomProperty_Destroy(ArkUI_CustomProperty* handle)
```

**描述：**

销毁[ArkUI_CustomProperty](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-customproperty)实例。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_CustomProperty* handle | 要销毁的实例。 |




#### OH_ArkUI_CustomProperty_GetStringValue()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
const char* OH_ArkUI_CustomProperty_GetStringValue(ArkUI_CustomProperty* handle)
```

**描述：**

获取自定义属性对象的value信息。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_CustomProperty* handle | 自定义属性对象指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| const char* | 自定义属性对象的value信息。 |




#### OH_ArkUI_HostWindowInfo_GetName()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
const char* OH_ArkUI_HostWindowInfo_GetName(ArkUI_HostWindowInfo* info)
```

**描述：**

获取[ArkUI_HostWindowInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-hostwindowinfo)对象中的窗口名称。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_HostWindowInfo* info | HostWindowInfo对象。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| const char* | ArkUI_HostWindowInfo对象中的窗口名称。 |




#### OH_ArkUI_HostWindowInfo_Destroy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_HostWindowInfo_Destroy(ArkUI_HostWindowInfo* info)
```

**描述：**

销毁[ArkUI_HostWindowInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-hostwindowinfo)对象。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_HostWindowInfo* info | 要销毁的ArkUI_HostWindowInfo对象。 |




#### OH_ArkUI_ActiveChildrenInfo_Destroy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_ActiveChildrenInfo_Destroy(ArkUI_ActiveChildrenInfo* handle)
```

**描述：**

销毁[ArkUI_ActiveChildrenInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-activechildreninfo)实例，释放获取活跃子节点信息时分配的资源。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ActiveChildrenInfo* handle | 要销毁的ArkUI_ActiveChildrenInfo实例。 |




#### OH_ArkUI_ActiveChildrenInfo_GetNodeByIndex()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_NodeHandle OH_ArkUI_ActiveChildrenInfo_GetNodeByIndex(ArkUI_ActiveChildrenInfo* handle, int32_t index)
```

**描述：**

获取[ArkUI_ActiveChildrenInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-activechildreninfo)结构体中下标为index的子节点，适用于按下标遍历活跃子节点。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ActiveChildrenInfo* handle | 要获取信息的ArkUI_ActiveChildrenInfo实例。 |
| int32_t index | 子节点的下标。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_NodeHandle | 下标对应的子节点指针，异常时返回nullptr。 |




#### OH_ArkUI_ActiveChildrenInfo_GetCount()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_ActiveChildrenInfo_GetCount(ArkUI_ActiveChildrenInfo* handle)
```

**描述：**

获取[ArkUI_ActiveChildrenInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-activechildreninfo)结构体内的子节点数量，适用于遍历活跃子节点前确定数量。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_ActiveChildrenInfo* handle | 要获取信息的ArkUI_ActiveChildrenInfo实例。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| int32_t | 子节点数量，默认值0. |




#### OH_ArkUI_CrossLanguageOption_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_CrossLanguageOption* OH_ArkUI_CrossLanguageOption_Create(void)
```

**描述：**

创建跨语言配置项实例。

**起始版本：** 15

**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_CrossLanguageOption* | 返回跨语言实例。如果对象返回空指针，则表示创建失败，失败的原因可能是地址空间已满。 |




#### OH_ArkUI_CrossLanguageOption_Destroy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_CrossLanguageOption_Destroy(ArkUI_CrossLanguageOption* option)
```

**描述：**

销毁跨语言配置项实例。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_CrossLanguageOption* option | 要销毁的跨语言配置项实例。 |




#### OH_ArkUI_CrossLanguageOption_SetAttributeSettingStatus()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_CrossLanguageOption_SetAttributeSettingStatus(ArkUI_CrossLanguageOption* option, bool enabled)
```

**描述：**

设置配置项中是否允许跨语言修改属性。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_CrossLanguageOption* option | 跨语言配置项实例。 |
| bool enabled | 是否允许跨语言修改属性。true表示允许跨语言修改属性，false表示不允许跨语言修改属性，默认值：false。 |




#### OH_ArkUI_CrossLanguageOption_GetAttributeSettingStatus()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
bool OH_ArkUI_CrossLanguageOption_GetAttributeSettingStatus(ArkUI_CrossLanguageOption* option)
```

**描述：**

获取配置项中是否允许跨语言修改属性。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_CrossLanguageOption* option | 跨语言配置项实例。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 是否允许跨语言修改属性。true表示允许跨语言修改属性，false表示不允许跨语言修改属性。 |




#### OH_ArkUI_CrossLanguageOption_SetTreeOperatingStatus()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_CrossLanguageOption_SetTreeOperatingStatus(ArkUI_CrossLanguageOption* option, OH_ArkUI_CrossLanguageOperatingStatus status)
```

**描述：**

设置跨语言配置项的节点树操作状态。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_CrossLanguageOption* option | 跨语言配置项实例。 |
| OH_ArkUI_CrossLanguageOperatingStatus status | 需要设置的节点树操作状态。 默认值：OH_ARKUI_TREE_OPERATING_STATUS_UNDEFINED。 |




#### OH_ArkUI_CrossLanguageOption_GetTreeOperatingStatus()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_ArkUI_CrossLanguageOperatingStatus OH_ArkUI_CrossLanguageOption_GetTreeOperatingStatus(ArkUI_CrossLanguageOption* option)
```

**描述：**

获取跨语言配置项的节点树操作状态。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_CrossLanguageOption* option | 跨语言配置项实例。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| OH_ArkUI_CrossLanguageOperatingStatus | 跨语言配置项的节点树操作状态。 |




#### OH_ArkUI_ContentTransitionEffect_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ContentTransitionEffect* OH_ArkUI_ContentTransitionEffect_Create(int32_t type)
```

**描述：**

创建ContentTransitionEffect属性对象。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32_t type | 指定动效的转场方式。值为0表示无动效转场，值为1时表示淡入淡出动效转场。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ContentTransitionEffect* | 指向ContentTransitionEffect对象的指针。 |




#### OH_ArkUI_SelectionOptions_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_SelectionOptions* OH_ArkUI_SelectionOptions_Create()
```

**描述：**

创建选择选项。

**起始版本：** 23

**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_SelectionOptions* | 指向选择选项对象的指针。 |




#### OH_ArkUI_SelectionOptions_Dispose()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SelectionOptions_Dispose(ArkUI_SelectionOptions* options)
```

**描述：**

释放选择选项对象。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SelectionOptions* options | 指向待释放的选择选项对象的指针。 |




#### OH_ArkUI_SelectionOptions_SetMenuPolicy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SelectionOptions_SetMenuPolicy(ArkUI_SelectionOptions* options, ArkUI_MenuPolicy menuPolicy)
```

**描述：**

设置选择选项的菜单弹出策略。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SelectionOptions* options | 指向选择选项对象的指针。 |
| ArkUI_MenuPolicy menuPolicy | 菜单弹出策略。 |




#### OH_ArkUI_SelectionOptions_GetMenuPolicy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_MenuPolicy  OH_ArkUI_SelectionOptions_GetMenuPolicy(ArkUI_SelectionOptions* options)
```

**描述：**

获取选择选项的菜单弹出策略。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SelectionOptions* options | 指向选择选项对象的指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_MenuPolicy | 菜单弹出策略。 |




#### OH_ArkUI_TextMenuItem_SetContent()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextMenuItem_SetContent(ArkUI_TextMenuItem* item, const char* content)
```

**描述**

设置文本菜单项标题。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMenuItem* item | 指向ArkUI_TextMenuItem对象的指针。 |
| const char* content | 文本菜单项标题，默认为空字符串。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |




#### OH_ArkUI_TextMenuItem_GetContent()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextMenuItem_GetContent(const ArkUI_TextMenuItem* item, char* buffer, int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取文本菜单项标题。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_TextMenuItem* item | 指向ArkUI_TextMenuItem对象的指针。 |
| char* buffer | 缓冲区，由开发者创建分配内存，用于存储文本菜单项标题信息。 |
| int32_t bufferSize | 缓冲区大小。 |
| int32_t* writeLength | 返回值为ARKUI_ERROR_CODE_NO_ERROR时表示实际写入缓冲区的长度。 返回值为ARKUI_ERROR_CODE_BUFFER_SIZE_ERROR时表示字符串完整写入缓冲区所需要的最小长度。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_BUFFER_SIZE_ERROR 缓冲区大小不足。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |




#### OH_ArkUI_TextMenuItem_SetIcon()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextMenuItem_SetIcon(ArkUI_TextMenuItem* item, const char* icon)
```

**描述**

设置文本菜单项图标路径。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMenuItem* item | 指向ArkUI_TextMenuItem对象的指针。 |
| const char* icon | 文本菜单项图标路径，默认空字符串。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |




#### OH_ArkUI_TextMenuItem_GetIcon()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextMenuItem_GetIcon(const ArkUI_TextMenuItem* item, char* buffer, int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取文本菜单项图标路径。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_TextMenuItem* item | 指向ArkUI_TextMenuItem对象的指针。 |
| char* buffer | 缓冲区，由开发者创建分配内存，用于存储文本菜单项图标路径信息。 |
| int32_t bufferSize | 缓冲区大小。 |
| int32_t* writeLength | 返回值为ARKUI_ERROR_CODE_NO_ERROR时表示实际写入缓冲区的长度。 返回值为ARKUI_ERROR_CODE_BUFFER_SIZE_ERROR时表示字符串完整写入缓冲区所需要的最小长度。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_BUFFER_SIZE_ERROR 缓冲区大小不足。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |




#### OH_ArkUI_TextMenuItem_SetLabelInfo()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextMenuItem_SetLabelInfo(ArkUI_TextMenuItem* item, const char* labelInfo)
```

**描述**

设置文本菜单项快捷键提示，例如“复制”菜单项的快捷键提示可以设置为“Ctrl+C”。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMenuItem* item | 指向ArkUI_TextMenuItem对象的指针。 |
| const char* labelInfo | 文本菜单项快捷键提示，默认空字符串。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |




#### OH_ArkUI_TextMenuItem_GetLabelInfo()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextMenuItem_GetLabelInfo(const ArkUI_TextMenuItem* item, char* buffer, int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取文本菜单项快捷键提示，例如“复制”菜单项的快捷键提示一般为“Ctrl+C”。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_TextMenuItem* item | 指向ArkUI_TextMenuItem对象的指针。 |
| char* buffer | 缓冲区，由开发者创建分配内存，用于存储文本菜单项快捷键提示信息。 |
| int32_t bufferSize | 缓冲区大小。 |
| int32_t* writeLength | 返回值为ARKUI_ERROR_CODE_NO_ERROR时表示实际写入缓冲区的长度。 返回值为ARKUI_ERROR_CODE_BUFFER_SIZE_ERROR时表示字符串完整写入缓冲区所需要的最小长度。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_BUFFER_SIZE_ERROR 缓冲区大小不足。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |




#### OH_ArkUI_TextMenuItem_SetId()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextMenuItem_SetId(ArkUI_TextMenuItem* item, int32_t id)
```

**描述**

设置文本菜单项id。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMenuItem* item | 指向ArkUI_TextMenuItem对象的指针。 |
| int32_t id | 文本菜单项id。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |




#### OH_ArkUI_TextMenuItem_GetId()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextMenuItem_GetId(const ArkUI_TextMenuItem* item, int32_t* id)
```

**描述**

获取文本菜单项id。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const ArkUI_TextMenuItem* item | 指向ArkUI_TextMenuItem对象的指针。 |
| int32_t* id | 文本菜单项id。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |




#### OH_ArkUI_TextMenuItemArray_GetSize()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextMenuItemArray_GetSize(ArkUI_TextMenuItemArray* items, int32_t* size)
```

**描述**

获取文本菜单项数组大小。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMenuItemArray* items | 指向ArkUI_TextMenuItemArray对象的指针。 |
| int32_t* size | 文本菜单项数组大小。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |




#### OH_ArkUI_TextMenuItemArray_GetItem()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextMenuItemArray_GetItem(ArkUI_TextMenuItemArray* items, int32_t index, ArkUI_TextMenuItem** item)
```

**描述**

获取文本菜单项数组中指定索引位置的文本菜单项。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMenuItemArray* items | 指向ArkUI_TextMenuItemArray对象的指针。 |
| int32_t index | 指定索引位置。 |
| ArkUI_TextMenuItem** item | 指向ArkUI_TextMenuItem对象的二级指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |




#### OH_ArkUI_TextMenuItemArray_Insert()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextMenuItemArray_Insert(ArkUI_TextMenuItemArray* items, ArkUI_TextMenuItem* item, int32_t index)
```

**描述**

在文本菜单项数组中指定索引位置插入一个文本菜单项。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMenuItemArray* items | 指向ArkUI_TextMenuItemArray对象的指针。 |
| ArkUI_TextMenuItem* item | 指向ArkUI_TextMenuItem对象的指针。 |
| int32_t index | 要插入文本菜单项的索引位置。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |




#### OH_ArkUI_TextMenuItemArray_Erase()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextMenuItemArray_Erase(ArkUI_TextMenuItemArray* items, int32_t index)
```

**描述**

删除文本菜单项数组中指定索引位置的文本菜单项。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMenuItemArray* items | 指向ArkUI_TextMenuItemArray对象的指针。 |
| int32_t index | 要删除的文本菜单项索引位置。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |




#### OH_ArkUI_TextMenuItemArray_Clear()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextMenuItemArray_Clear(ArkUI_TextMenuItemArray* items)
```

**描述**

清除文本菜单项数组中所有的文本菜单项。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextMenuItemArray* items | 指向ArkUI_TextMenuItemArray对象的指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |




#### OH_ArkUI_TextEditMenuOptions_RegisterOnCreateMenuCallback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditMenuOptions_RegisterOnCreateMenuCallback(ArkUI_TextEditMenuOptions* editMenuOptions, void* userData, ArkUI_TextCreateMenuCallback cb)
```

**描述**

注册文本菜单创建事件回调函数。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextEditMenuOptions* editMenuOptions | 指向ArkUI_TextEditMenuOptions对象的指针。 |
| void* userData | 用户自定义数据。 |
| ArkUI_TextCreateMenuCallback cb | 文本菜单创建事件回调函数。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |




#### OH_ArkUI_TextEditMenuOptions_RegisterOnPrepareMenuCallback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditMenuOptions_RegisterOnPrepareMenuCallback(ArkUI_TextEditMenuOptions* editMenuOptions, void* userData, ArkUI_TextPrepareMenuCallback cb)
```

**描述**

注册文本菜单准备事件回调函数。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextEditMenuOptions* editMenuOptions | 指向ArkUI_TextEditMenuOptions对象的指针。 |
| void* userData | 用户自定义数据。 |
| ArkUI_TextPrepareMenuCallback cb | 文本菜单准备事件回调函数。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |




#### OH_ArkUI_TextEditMenuOptions_RegisterOnMenuItemClickCallback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditMenuOptions_RegisterOnMenuItemClickCallback(ArkUI_TextEditMenuOptions* editMenuOptions, void* userData, ArkUI_TextMenuItemClickCallback cb)
```

**描述**

注册文本菜单项点击事件回调函数。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextEditMenuOptions* editMenuOptions | 指向ArkUI_TextEditMenuOptions对象的指针。 |
| void* userData | 用户自定义数据。 |
| ArkUI_TextMenuItemClickCallback cb | 文本菜单项点击事件回调函数。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |




#### OH_ArkUI_TextSelectionMenuOptions_SetSpanType()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_SetSpanType(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, ArkUI_TextSpanType textSpanType)
```

**描述**

设置自定义文本选择菜单的文本识别类型。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextSelectionMenuOptions* selectionMenuOptions | 指向ArkUI_TextSelectionMenuOptions对象的指针。 |
| ArkUI_TextSpanType textSpanType | 自定义文本选择菜单的文本识别类型。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |




#### OH_ArkUI_TextSelectionMenuOptions_GetSpanType()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_GetSpanType(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, ArkUI_TextSpanType* spanType)
```

**描述**

获取自定义文本选择菜单的文本识别类型。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextSelectionMenuOptions* selectionMenuOptions | 指向ArkUI_TextSelectionMenuOptions对象的指针。 |
| ArkUI_TextSpanType* spanType | 自定义文本选择菜单的文本识别类型。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |




#### OH_ArkUI_TextSelectionMenuOptions_SetContentNode()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_SetContentNode(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, ArkUI_NodeHandle node)
```

**描述**

设置自定义文本选择菜单的内容节点。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextSelectionMenuOptions* selectionMenuOptions | 指向ArkUI_TextSelectionMenuOptions对象的指针。 |
| ArkUI_NodeHandle node | 自定义文本选择菜单的内容节点。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |




#### OH_ArkUI_TextSelectionMenuOptions_GetContentNode()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_GetContentNode(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, ArkUI_NodeHandle* node)
```

**描述**

获取自定义文本选择菜单的内容节点。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextSelectionMenuOptions* selectionMenuOptions | 指向ArkUI_TextSelectionMenuOptions对象的指针。 |
| ArkUI_NodeHandle* node | 自定义文本选择菜单的内容节点。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |




#### OH_ArkUI_TextSelectionMenuOptions_SetResponseType()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_SetResponseType(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, ArkUI_TextResponseType responseType)
```

**描述**

设置自定义文本选择菜单的响应类型。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextSelectionMenuOptions* selectionMenuOptions | 指向ArkUI_TextSelectionMenuOptions对象的指针。 |
| ArkUI_TextResponseType responseType | 自定义文本选择菜单的响应类型。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |




#### OH_ArkUI_TextSelectionMenuOptions_GetResponseType()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_GetResponseType(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, ArkUI_TextResponseType* responseType)
```

**描述**

获取自定义文本选择菜单的响应类型。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextSelectionMenuOptions* selectionMenuOptions | 指向ArkUI_TextSelectionMenuOptions对象的指针。 |
| ArkUI_TextResponseType* responseType | 自定义文本选择菜单的响应类型。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |




#### OH_ArkUI_TextSelectionMenuOptions_RegisterOnMenuShowCallback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_RegisterOnMenuShowCallback(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, void* userData, void (*callback)(int32_t start, int32_t end, void* userData))
```

**描述**

注册自定义文本选择菜单显示事件回调。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextSelectionMenuOptions* selectionMenuOptions | 指向ArkUI_TextSelectionMenuOptions对象的指针。 |
| void* userData | 用户自定义数据，取任意值。设置后，会通过callback回调回传回来。 |
| void (*callback)(int32_t start, int32_t end, void* userData) | 自定义文本选择菜单显示事件回调。 start：选中文本的起始位置。 end：选中文本的结束位置。 userData：用户自定义数据，对应OH_ArkUI_TextSelectionMenuOptions_RegisterOnMenuShowCallback接口的入参userData。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |




#### OH_ArkUI_TextSelectionMenuOptions_RegisterOnMenuHideCallback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextSelectionMenuOptions_RegisterOnMenuHideCallback(ArkUI_TextSelectionMenuOptions* selectionMenuOptions, void* userData, void (*callback)(int32_t start, int32_t end, void* userData))
```

**描述**

注册自定义文本选择菜单隐藏事件回调。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_TextSelectionMenuOptions* selectionMenuOptions | 指向ArkUI_TextSelectionMenuOptions对象的指针。 |
| void* userData | 用户自定义数据，取任意值。设置后，会通过callback回调回传回来。 |
| void (*callback)(int32_t start, int32_t end, void* userData) | 自定义文本选择菜单隐藏事件回调。 start：选中文本的起始位置。 end：选中文本的结束位置。 userData：用户自定义数据，对应OH_ArkUI_TextSelectionMenuOptions_RegisterOnMenuHideCallback接口的入参userData。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |




#### OH_ArkUI_SelectedDragPreviewStyle_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_SelectedDragPreviewStyle* OH_ArkUI_SelectedDragPreviewStyle_Create();
```

**描述**

创建选中状态下拖拽文本预览样式对象。

**起始版本：** 23

**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_SelectedDragPreviewStyle* | 指向ArkUI_SelectedDragPreviewStyle对象的指针。 |




#### OH_ArkUI_SelectedDragPreviewStyle_Dispose()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_SelectedDragPreviewStyle_Dispose(ArkUI_SelectedDragPreviewStyle* config)
```

**描述**

销毁选中状态下拖拽文本预览样式对象。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SelectedDragPreviewStyle* config | 指向ArkUI_SelectedDragPreviewStyle对象的指针。 |




#### OH_ArkUI_SelectedDragPreviewStyle_SetColor()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void  OH_ArkUI_SelectedDragPreviewStyle_SetColor(ArkUI_SelectedDragPreviewStyle* config, uint32_t color);
```

**描述**

设置选中态拖拽文本预览样式的背景色。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SelectedDragPreviewStyle* config | 指向ArkUI_SelectedDragPreviewStyle对象的指针。 |
| uint32_t color | 选中态拖拽文本预览样式的背景，格式为RGBA。 |




#### OH_ArkUI_SelectedDragPreviewStyle_GetColor()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
uint32_t OH_ArkUI_SelectedDragPreviewStyle_GetColor(ArkUI_SelectedDragPreviewStyle* config)
```

**描述**

获取选中态拖拽文本预览样式的背景色。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_SelectedDragPreviewStyle* config | 指向ArkUI_SelectedDragPreviewStyle对象的指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32_t color | 选中态拖拽文本预览样式的背景，格式为RGBA。 |




#### OH_ArkUI_DecorationStyleOptions_SetTextDecorationType()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_DecorationStyleOptions_SetTextDecorationType(OH_ArkUI_DecorationStyleOptions* options, ArkUI_TextDecorationType type)
```

**描述**

设置装饰线样式的装饰类型。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_DecorationStyleOptions* options | 指向OH_ArkUI_DecorationStyleOptions对象的指针。 |
| ArkUI_TextDecorationType type | 装饰类型ArkUI_TextDecorationType。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_DecorationStyleOptions_GetTextDecorationType()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_DecorationStyleOptions_GetTextDecorationType(OH_ArkUI_DecorationStyleOptions* options, ArkUI_TextDecorationType* type)
```

**描述**

获取装饰线样式的装饰类型。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_DecorationStyleOptions* options | 指向OH_ArkUI_DecorationStyleOptions对象的指针。 |
| ArkUI_TextDecorationType* type | 装饰类型ArkUI_TextDecorationType。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_DecorationStyleOptions_SetColor()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_DecorationStyleOptions_SetColor(OH_ArkUI_DecorationStyleOptions* options, uint32_t color)
```

**描述**

设置装饰线的颜色。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_DecorationStyleOptions* options | 指向OH_ArkUI_DecorationStyleOptions对象的指针。 |
| uint32_t color | 装饰线的颜色，0xARGB格式。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_DecorationStyleOptions_GetColor()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_DecorationStyleOptions_GetColor(OH_ArkUI_DecorationStyleOptions* options, uint32_t* color)
```

**描述**

获取装饰线的颜色。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_DecorationStyleOptions* options | 指向OH_ArkUI_DecorationStyleOptions对象的指针。 |
| uint32_t* color | 装饰线的颜色，0xARGB格式。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_DecorationStyleOptions_SetTextDecorationStyle()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_DecorationStyleOptions_SetTextDecorationStyle(OH_ArkUI_DecorationStyleOptions* options, ArkUI_TextDecorationStyle style)
```

**描述**

设置装饰线的样式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_DecorationStyleOptions* options | 指向OH_ArkUI_DecorationStyleOptions对象的指针。 |
| ArkUI_TextDecorationStyle style | 装饰线的样式ArkUI_TextDecorationStyle。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_DecorationStyleOptions_GetTextDecorationStyle()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_DecorationStyleOptions_GetTextDecorationStyle(OH_ArkUI_DecorationStyleOptions* options, ArkUI_TextDecorationStyle* style)
```

**描述**

获取装饰线的样式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_DecorationStyleOptions* options | 指向OH_ArkUI_DecorationStyleOptions对象的指针。 |
| ArkUI_TextDecorationStyle* style | 装饰线的样式ArkUI_TextDecorationStyle。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_DecorationStyleOptions_SetThicknessScale()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_DecorationStyleOptions_SetThicknessScale(OH_ArkUI_DecorationStyleOptions* options, float thicknessScale)
```

**描述**

设置装饰线的粗细缩放比例。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_DecorationStyleOptions* options | 指向OH_ArkUI_DecorationStyleOptions对象的指针。 |
| float thicknessScale | 装饰线的粗细缩放比例。取值范围为[0, +∞)。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_DecorationStyleOptions_GetThicknessScale()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_DecorationStyleOptions_GetThicknessScale(OH_ArkUI_DecorationStyleOptions* options, float* thicknessScale)
```

**描述**

获取装饰线的粗细缩放比例。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_DecorationStyleOptions* options | 指向OH_ArkUI_DecorationStyleOptions对象的指针。 |
| float* thicknessScale | 装饰线的粗细缩放比例。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextDataDetectorConfig_SetTypes()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextDataDetectorConfig_SetTypes(OH_ArkUI_TextDataDetectorConfig* config, const ArkUI_TextDataDetectorType* types, int32_t length)
```

**描述**

设置文本实体识别配置的类型。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextDataDetectorConfig* config | 指向OH_ArkUI_TextDataDetectorConfig对象的指针。 |
| const ArkUI_TextDataDetectorType* types | 文本实体识别配置的类型，取值为ArkUI_TextDataDetectorType枚举。 |
| int32_t length | 类型的数量。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextDataDetectorConfig_GetTypes()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextDataDetectorConfig_GetTypes(OH_ArkUI_TextDataDetectorConfig* config, ArkUI_TextDataDetectorType* buffer, int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取文本实体识别配置的类型。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextDataDetectorConfig* config | 指向OH_ArkUI_TextDataDetectorConfig对象的指针。 |
| ArkUI_TextDataDetectorType* buffer | 指向类型数组的缓冲区指针。 |
| int32_t bufferSize | 开发者为类型预留的缓冲区最多可以写入的类型的数量。 |
| int32_t* writeLength | 实际写入缓冲区的类型的数量。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 若bufferSize小于writeLength，返回ARKUI_ERROR_CODE_BUFFER_SIZE_ERROR。 |




#### OH_ArkUI_TextDataDetectorConfig_RegisterOnDetectResultUpdateCallback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextDataDetectorConfig_RegisterOnDetectResultUpdateCallback(OH_ArkUI_TextDataDetectorConfig* config, void* userData, void (*callback)(const char* result, int32_t length, void* userData))
```

**描述**

设置文本实体识别结果更新回调。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextDataDetectorConfig* config | 指向OH_ArkUI_TextDataDetectorConfig对象的指针。 |
| void* userData | 用户数据。 |
| void (*callback)(const char* result | 识别结果更新回调。result 识别到的文本实体内容。length 选中文本的结束位置。userData 用户自定义数据，对应OH_ArkUI_TextDataDetectorConfig_RegisterOnDetectResultUpdateCallback接口的入参userData。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextDataDetectorConfig_SetColor()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextDataDetectorConfig_SetColor(OH_ArkUI_TextDataDetectorConfig* config, uint32_t color)
```

**描述**

设置识别内容的颜色。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextDataDetectorConfig* config | 指向OH_ArkUI_TextDataDetectorConfig对象的指针。 |
| uint32_t color | 识别内容的颜色，0xARGB格式。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextDataDetectorConfig_GetColor()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextDataDetectorConfig_GetColor(OH_ArkUI_TextDataDetectorConfig* config, uint32_t* color)
```

**描述**

获取识别内容的颜色。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextDataDetectorConfig* config | 指向OH_ArkUI_TextDataDetectorConfig对象的指针。 |
| uint32_t* color | 识别内容的颜色，0xARGB格式。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextDataDetectorConfig_SetDecorationStyleOptions()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextDataDetectorConfig_SetDecorationStyleOptions(OH_ArkUI_TextDataDetectorConfig* config, OH_ArkUI_DecorationStyleOptions* decoration)
```

**描述**

设置识别内容的装饰样式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextDataDetectorConfig* config | 指向OH_ArkUI_TextDataDetectorConfig对象的指针。 |
| OH_ArkUI_DecorationStyleOptions* decoration | 识别内容的装饰样式。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextDataDetectorConfig_GetDecorationStyleOptions()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextDataDetectorConfig_GetDecorationStyleOptions(OH_ArkUI_TextDataDetectorConfig* config, OH_ArkUI_DecorationStyleOptions* decoration)
```

**描述**

获取识别内容的装饰样式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextDataDetectorConfig* config | 指向OH_ArkUI_TextDataDetectorConfig对象的指针。 |
| OH_ArkUI_DecorationStyleOptions* decoration | 识别内容的装饰样式。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextDataDetectorConfig_SetEnablePreviewMenu()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextDataDetectorConfig_SetEnablePreviewMenu(OH_ArkUI_TextDataDetectorConfig* config, bool enablePreviewMenu)
```

**描述**

设置长按识别内容时是否显示预览菜单。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextDataDetectorConfig* config | 指向OH_ArkUI_TextDataDetectorConfig对象的指针。 |
| bool enablePreviewMenu | 长按识别内容时是否显示预览菜单。true表示启用预览菜单，false表示不启用预览菜单。默认值为false。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextDataDetectorConfig_GetEnablePreviewMenu()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextDataDetectorConfig_GetEnablePreviewMenu(OH_ArkUI_TextDataDetectorConfig* config, bool* enablePreviewMenu)
```

**描述**

获取长按识别内容时是否显示预览菜单。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextDataDetectorConfig* config | 指向OH_ArkUI_TextDataDetectorConfig对象的指针。 |
| bool* enablePreviewMenu | 长按识别内容时是否显示预览菜单。true表示显示预览菜单，false表示不显示预览菜单。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorPlaceholderOptions_SetValue()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorPlaceholderOptions_SetValue(OH_ArkUI_TextEditorPlaceholderOptions* options, const char* value)
```

**描述**

设置无输入时的提示文本选项的提示文字。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorPlaceholderOptions* options | 指向OH_ArkUI_TextEditorPlaceholderOptions对象的指针。 |
| const char* value | 提示文字。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorPlaceholderOptions_GetValue()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorPlaceholderOptions_GetValue(OH_ArkUI_TextEditorPlaceholderOptions* options, char* buffer, int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取无输入时的提示文本选项的提示文字。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorPlaceholderOptions* options | 指向OH_ArkUI_TextEditorPlaceholderOptions对象的指针。 |
| char* buffer | 提示文字写入内存的缓冲区，内存空间需由开发者分配。 |
| int32_t bufferSize | 缓冲区最多可写入的字符的数量。 |
| int32_t* writeLength | 实际表示写入缓冲区的字符的数量。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 错误码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若节点、缓冲区或writeLength为空，返回ARKUI_ERROR_CODE_PARAM_INVALID。 若bufferSize小于writeLength，返回ARKUI_ERROR_CODE_BUFFER_SIZE_ERROR。 |




#### OH_ArkUI_TextEditorPlaceholderOptions_SetFontSize()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorPlaceholderOptions_SetFontSize(OH_ArkUI_TextEditorPlaceholderOptions* options, float fontSize)
```

**描述**

设置无输入时的提示文本选项的字体大小。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorPlaceholderOptions* options | 指向OH_ArkUI_TextEditorPlaceholderOptions对象的指针。 |
| float fontSize | 字体大小，单位为fp。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorPlaceholderOptions_GetFontSize()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorPlaceholderOptions_GetFontSize(OH_ArkUI_TextEditorPlaceholderOptions* options, float* fontSize)
```

**描述**

获取无输入时的提示文本选项的字体大小。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorPlaceholderOptions* options | 指向OH_ArkUI_TextEditorPlaceholderOptions对象的指针。 |
| float* fontSize | 字体大小，单位为fp。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorPlaceholderOptions_SetFontWeight()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorPlaceholderOptions_SetFontWeight(OH_ArkUI_TextEditorPlaceholderOptions* options, uint32_t fontWeight)
```

**描述**

设置无输入时的提示文本选项的字体粗细。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorPlaceholderOptions* options | 指向OH_ArkUI_TextEditorPlaceholderOptions对象的指针。 |
| uint32_t fontWeight | 字体粗细。取值为ArkUI_FontWeight中的枚举值，默认值为ARKUI_FONT_WEIGHT_W400。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorPlaceholderOptions_GetFontWeight()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorPlaceholderOptions_GetFontWeight(OH_ArkUI_TextEditorPlaceholderOptions* options, uint32_t* fontWeight)
```

**描述**

获取无输入时的提示文本选项的字体粗细。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorPlaceholderOptions* options | 指向OH_ArkUI_TextEditorPlaceholderOptions对象的指针。 |
| uint32_t* fontWeight | 字体粗细。取值为ArkUI_FontWeight中的枚举值，默认值为ARKUI_FONT_WEIGHT_W400。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorPlaceholderOptions_SetFontFamily()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorPlaceholderOptions_SetFontFamily(OH_ArkUI_TextEditorPlaceholderOptions* options, const char* fontFamily)
```

**描述**

设置无输入时的提示文本选项的字体家族。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorPlaceholderOptions* options | 指向OH_ArkUI_TextEditorPlaceholderOptions对象的指针。 |
| const char* fontFamily | 字体家族。存放待设置的字体名称，不同字体名称通过逗号拼接。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorPlaceholderOptions_GetFontFamily()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorPlaceholderOptions_GetFontFamily(OH_ArkUI_TextEditorPlaceholderOptions* options, char* buffer, int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取无输入时的提示文本选项的字体家族。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorPlaceholderOptions* options | 指向OH_ArkUI_TextEditorPlaceholderOptions对象的指针。 |
| char* buffer | 字体家族写入内存的缓冲区，内存空间需由开发者分配。 |
| int32_t bufferSize | 缓冲区最多可写入的字符的数量。 |
| int32_t* writeLength | 实际写入缓冲区的字符的数量。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 错误码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若节点、缓冲区或writeLength为空，返回ARKUI_ERROR_CODE_PARAM_INVALID。 若bufferSize小于writeLength，返回ARKUI_ERROR_CODE_BUFFER_SIZE_ERROR。 |




#### OH_ArkUI_TextEditorPlaceholderOptions_SetFontStyle()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorPlaceholderOptions_SetFontStyle(OH_ArkUI_TextEditorPlaceholderOptions* options, ArkUI_FontStyle fontStyle)
```

**描述**

设置无输入时的提示文本选项的字体样式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorPlaceholderOptions* options | 指向OH_ArkUI_TextEditorPlaceholderOptions对象的指针。 |
| ArkUI_FontStyle fontStyle | 字体样式。取值为ArkUI_FontStyle中的枚举。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorPlaceholderOptions_GetFontStyle()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorPlaceholderOptions_GetFontStyle(OH_ArkUI_TextEditorPlaceholderOptions* options, ArkUI_FontStyle* fontStyle)
```

**描述**

获取无输入时的提示文本选项的字体样式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorPlaceholderOptions* options | 指向OH_ArkUI_TextEditorPlaceholderOptions对象的指针。 |
| ArkUI_FontStyle* fontStyle | 字体样式。取值为ArkUI_FontStyle中的枚举。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorPlaceholderOptions_SetFontColor()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorPlaceholderOptions_SetFontColor(OH_ArkUI_TextEditorPlaceholderOptions* options, uint32_t fontColor)
```

**描述**

设置无输入时的提示文本选项的字体颜色。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorPlaceholderOptions* options | 指向OH_ArkUI_TextEditorPlaceholderOptions对象的指针。 |
| uint32_t fontColor | 字体颜色，0xARGB格式。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorPlaceholderOptions_GetFontColor()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorPlaceholderOptions_GetFontColor(OH_ArkUI_TextEditorPlaceholderOptions* options, uint32_t* fontColor)
```

**描述**

获取无输入时的提示文本选项的字体颜色。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorPlaceholderOptions* options | 指向OH_ArkUI_TextEditorPlaceholderOptions对象的指针。 |
| uint32_t* fontColor | 字体颜色，0xARGB格式。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorStyledStringController_SetCaretOffset()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorStyledStringController_SetCaretOffset(OH_ArkUI_TextEditorStyledStringController* controller, int32_t caretOffset)
```

**描述**

通过属性字符串控制器设置光标偏移量。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorStyledStringController* controller | 指向OH_ArkUI_TextEditorStyledStringController对象的指针。 |
| int32_t caretOffset | 索引位置。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorStyledStringController_GetCaretOffset()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorStyledStringController_GetCaretOffset(OH_ArkUI_TextEditorStyledStringController* controller, int32_t* caretOffset)
```

**描述**

通过属性字符串控制器获取光标索引位置。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorStyledStringController* controller | 指向OH_ArkUI_TextEditorStyledStringController对象的指针。 |
| int32_t* caretOffset | 索引位置。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorStyledStringController_SetSelection()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorStyledStringController_SetSelection(OH_ArkUI_TextEditorStyledStringController* controller, uint32_t start, uint32_t end, ArkUI_MenuPolicy menuPolicy)
```

**描述**

通过属性字符串控制器设置选中区域。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorStyledStringController* controller | 指向OH_ArkUI_TextEditorStyledStringController对象的指针。 |
| uint32_t start | 选中区域的起始位置。 |
| uint32_t end | 选中区域的结束位置。 |
| ArkUI_MenuPolicy menuPolicy | 选区内菜单弹出的策略。取值为ArkUI_MenuPolicy中的枚举。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorStyledStringController_IsEditing()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorStyledStringController_IsEditing(OH_ArkUI_TextEditorStyledStringController* controller, bool* isEditing)
```

**描述**

通过属性字符串控制器获取文本编辑器的编辑状态。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorStyledStringController* controller | 指向OH_ArkUI_TextEditorStyledStringController对象的指针。 |
| bool* isEditing | 编辑状态。true表示是编辑态，false表示不是编辑态。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorStyledStringController_StopEditing()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorStyledStringController_StopEditing(OH_ArkUI_TextEditorStyledStringController* controller)
```

**描述**

通过属性字符串控制器退出文本编辑器的编辑状态。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorStyledStringController* controller | 指向OH_ArkUI_TextEditorStyledStringController对象的指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorStyledStringController_GetPreviewText()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorStyledStringController_GetPreviewText(OH_ArkUI_TextEditorStyledStringController* controller, uint32_t* offset, char* buffer, int32_t bufferSize, int32_t* writeLength)
```

**描述**

通过属性字符串控制器获取预上屏文本内容。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorStyledStringController* controller | 指向OH_ArkUI_TextEditorStyledStringController对象的指针。 |
| uint32_t* offset | 预上屏文本位置。 |
| char* buffer | 预上屏文本内容写入内存的缓冲区，内存空间需由开发者分配。 |
| int32_t bufferSize | 缓冲区最多可写入的字符的数量。 |
| int32_t* writeLength | 实际写入缓冲区的字符的数量。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorStyledStringController_GetCaretRect()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorStyledStringController_GetCaretRect(OH_ArkUI_TextEditorStyledStringController* controller, ArkUI_Rect* rect)
```

**描述**

通过属性字符串控制器获取光标矩形区域。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorStyledStringController* controller | 指向OH_ArkUI_TextEditorStyledStringController对象的指针。 |
| ArkUI_Rect* rect | 光标区域信息。取值为ArkUI_Rect中的枚举。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorStyledStringController_DeleteBackward()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorStyledStringController_DeleteBackward(OH_ArkUI_TextEditorStyledStringController* controller)
```

**描述**

通过属性字符串控制器删除字符。没有内容被选中时，删除当前光标位置前的1个字符。有内容被选中时，删除选中内容。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorStyledStringController* controller | 指向OH_ArkUI_TextEditorStyledStringController对象的指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorParagraphStyle_SetTextAlign()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_SetTextAlign(OH_ArkUI_TextEditorParagraphStyle* style, ArkUI_TextAlignment align)
```

**描述**

设置段落样式中的文本对齐方式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorParagraphStyle* style | 指向OH_ArkUI_TextEditorParagraphStyle对象的指针。 |
| ArkUI_TextAlignment align | 文本对齐方式。取值为ArkUI_TextAlignment中的枚举。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorParagraphStyle_GetTextAlign()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_GetTextAlign(OH_ArkUI_TextEditorParagraphStyle* style, ArkUI_TextAlignment* align)
```

**描述**

获取段落样式中的文本对齐方式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorParagraphStyle* style | 指向OH_ArkUI_TextEditorParagraphStyle对象的指针。 |
| ArkUI_TextAlignment* align | 文本对齐方式。取值为ArkUI_TextAlignment中的枚举。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorParagraphStyle_SetLeadingMarginPixelMap()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_SetLeadingMarginPixelMap(OH_ArkUI_TextEditorParagraphStyle* style, struct OH_PixelmapNative* pixelmap)
```

**描述**

设置段落样式中段落缩进的像素图。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorParagraphStyle* style | 指向OH_ArkUI_TextEditorParagraphStyle对象的指针。 |
| struct OH_PixelmapNative* pixelmap | 段落缩进的像素图。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorParagraphStyle_GetLeadingMarginPixelMap()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_GetLeadingMarginPixelMap(OH_ArkUI_TextEditorParagraphStyle* style, struct OH_PixelmapNative** pixelmap)
```

**描述**

获取段落样式中段落缩进的像素图。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorParagraphStyle* style | 指向OH_ArkUI_TextEditorParagraphStyle对象的指针。 |
| struct OH_PixelmapNative** pixelmap | 段落缩进的像素图。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorParagraphStyle_SetLeadingMarginWidth()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_SetLeadingMarginWidth(OH_ArkUI_TextEditorParagraphStyle* style, uint32_t width)
```

**描述**

设置段落样式中段落缩进的宽度。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorParagraphStyle* style | 指向OH_ArkUI_TextEditorParagraphStyle对象的指针。 |
| uint32_t width | 段落缩进的宽度，单位为vp。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorParagraphStyle_GetLeadingMarginWidth()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_GetLeadingMarginWidth(OH_ArkUI_TextEditorParagraphStyle* style, uint32_t* width)
```

**描述**

获取段落样式中段落缩进的宽度。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorParagraphStyle* style | 指向OH_ArkUI_TextEditorParagraphStyle对象的指针。 |
| uint32_t* width | 段落缩进的宽度，单位为vp。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorParagraphStyle_SetLeadingMarginHeight()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_SetLeadingMarginHeight(OH_ArkUI_TextEditorParagraphStyle* style, uint32_t height)
```

**描述**

设置段落样式中段落缩进的高度。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorParagraphStyle* style | 指向OH_ArkUI_TextEditorParagraphStyle对象的指针。 |
| uint32_t height | 段落缩进的高度，单位为vp。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorParagraphStyle_GetLeadingMarginHeight()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_GetLeadingMarginHeight(OH_ArkUI_TextEditorParagraphStyle* style, uint32_t* height)
```

**描述**

获取段落样式中段落缩进的高度。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorParagraphStyle* style | 指向OH_ArkUI_TextEditorParagraphStyle对象的指针。 |
| uint32_t* height | 段落缩进的高度，单位为vp。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorParagraphStyle_SetWordBreak()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_SetWordBreak(OH_ArkUI_TextEditorParagraphStyle* style, ArkUI_WordBreak wordBreak)
```

**描述**

设置段落样式的断字方式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorParagraphStyle* style | 指向OH_ArkUI_TextEditorParagraphStyle对象的指针。 |
| ArkUI_WordBreak wordBreak | 断字方式。取值为ArkUI_WordBreak中的枚举。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorParagraphStyle_GetWordBreak()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_GetWordBreak(OH_ArkUI_TextEditorParagraphStyle* style, ArkUI_WordBreak* wordBreak)
```

**描述**

获取段落样式的断字方式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorParagraphStyle* style | 指向OH_ArkUI_TextEditorParagraphStyle对象的指针。 |
| ArkUI_WordBreak* wordBreak | 断字方式。取值为ArkUI_WordBreak中的枚举。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorParagraphStyle_SetLineBreakStrategy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_SetLineBreakStrategy(OH_ArkUI_TextEditorParagraphStyle* style, OH_ArkUI_LineBreakStrategy lineBreakStrategy)
```

**描述**

设置段落样式的换行策略。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorParagraphStyle* style | 指向OH_ArkUI_TextEditorParagraphStyle对象的指针。 |
| OH_ArkUI_LineBreakStrategy lineBreakStrategy | 换行策略。取值为OH_ArkUI_LineBreakStrategy中的枚举。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorParagraphStyle_GetLineBreakStrategy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_GetLineBreakStrategy(OH_ArkUI_TextEditorParagraphStyle* style, OH_ArkUI_LineBreakStrategy* lineBreakStrategy)
```

**描述**

获取段落样式的换行策略。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorParagraphStyle* style | 指向OH_ArkUI_TextEditorParagraphStyle对象的指针。 |
| OH_ArkUI_LineBreakStrategy* lineBreakStrategy | 换行策略。取值为OH_ArkUI_LineBreakStrategy中的枚举。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorParagraphStyle_SetParagraphSpacing()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_SetParagraphSpacing(OH_ArkUI_TextEditorParagraphStyle* style, uint32_t paragraphSpacing)
```

**描述**

设置段落样式的段落间距。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorParagraphStyle* style | 指向OH_ArkUI_TextEditorParagraphStyle对象的指针。 |
| uint32_t paragraphSpacing | 段落间距，单位为vp。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorParagraphStyle_GetParagraphSpacing()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_GetParagraphSpacing(OH_ArkUI_TextEditorParagraphStyle* style, uint32_t* paragraphSpacing)
```

**描述**

获取段落样式的段落间距。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorParagraphStyle* style | 指向OH_ArkUI_TextEditorParagraphStyle对象的指针。 |
| uint32_t* paragraphSpacing | 段落间距，单位为vp。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorParagraphStyle_SetTextVerticalAlign()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_SetTextVerticalAlign(OH_ArkUI_TextEditorParagraphStyle* style, ArkUI_TextVerticalAlignment verticalAlignment)
```

**描述**

设置段落样式的文本垂直对齐方式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorParagraphStyle* style | 指向OH_ArkUI_TextEditorParagraphStyle对象的指针。 |
| ArkUI_TextVerticalAlignment verticalAlignment | 文本垂直对齐方式。取值为ArkUI_TextVerticalAlignment中的枚举。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorParagraphStyle_GetTextVerticalAlign()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_GetTextVerticalAlign(OH_ArkUI_TextEditorParagraphStyle* style, ArkUI_TextVerticalAlignment* verticalAlignment)
```

**描述**

获取段落样式的文本垂直对齐方式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorParagraphStyle* style | 指向OH_ArkUI_TextEditorParagraphStyle对象的指针。 |
| ArkUI_TextVerticalAlignment* verticalAlignment | 文本垂直对齐方式。取值为ArkUI_TextVerticalAlignment中的枚举。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorParagraphStyle_SetTextDirection()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_SetTextDirection(OH_ArkUI_TextEditorParagraphStyle* style, ArkUI_TextDirection textDirection)
```

**描述**

设置段落样式的文本方向。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorParagraphStyle* style | 指向OH_ArkUI_TextEditorParagraphStyle对象的指针。 |
| ArkUI_TextDirection textDirection | 文本方向。取值为ArkUI_TextDirection中的枚举。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorParagraphStyle_GetTextDirection()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorParagraphStyle_GetTextDirection(OH_ArkUI_TextEditorParagraphStyle* style, ArkUI_TextDirection* textDirection)
```

**描述**

获取段落样式的文本方向。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorParagraphStyle* style | 指向OH_ArkUI_TextEditorParagraphStyle对象的指针。 |
| ArkUI_TextDirection* textDirection | 文本方向。取值为ArkUI_TextDirection中的枚举。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorStyledStringController_SetTypingParagraphStyle()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorStyledStringController_SetTypingParagraphStyle(OH_ArkUI_TextEditorStyledStringController* controller, OH_ArkUI_TextEditorParagraphStyle* style)
```

**描述**

通过属性字符串控制器设置预设段落样式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorStyledStringController* controller | 指向OH_ArkUI_TextEditorStyledStringController对象的指针。 |
| OH_ArkUI_TextEditorParagraphStyle* style | 预设段落样式。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorTextStyle_SetFontColor()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_SetFontColor(OH_ArkUI_TextEditorTextStyle* style, uint32_t color)
```

**描述**

设置文本样式的字体颜色。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorTextStyle* style | TextEditor组件文本样式。 |
| uint32_t color | 字体颜色，0xARGB格式。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorTextStyle_GetFontColor()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_GetFontColor(OH_ArkUI_TextEditorTextStyle* style, uint32_t* color)
```

**描述**

获取文本样式的字体颜色。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorTextStyle* style | TextEditor组件文本样式。 |
| uint32_t* color | 字体颜色，0xARGB格式。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorTextStyle_SetFontSize()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_SetFontSize(OH_ArkUI_TextEditorTextStyle* style, float size)
```

**描述**

设置文本样式的字体大小。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorTextStyle* style | TextEditor组件文本样式。 |
| float size | 字体大小，单位为fp。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorTextStyle_GetFontSize()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_GetFontSize(OH_ArkUI_TextEditorTextStyle* style, float* size)
```

**描述**

获取文本样式的字体大小。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorTextStyle* style | TextEditor组件文本样式。 |
| float* size | 字体大小，单位为fp。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorTextStyle_SetFontStyle()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_SetFontStyle(OH_ArkUI_TextEditorTextStyle* style, ArkUI_FontStyle fontStyle)
```

**描述**

设置文本样式的字体样式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorTextStyle* style | TextEditor组件文本样式。 |
| ArkUI_FontStyle fontStyle | 字体样式。取值为ArkUI_FontStyle中的枚举。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorTextStyle_GetFontStyle()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_GetFontStyle(OH_ArkUI_TextEditorTextStyle* style, ArkUI_FontStyle* fontStyle)
```

**描述**

获取文本样式的字体样式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorTextStyle* style | TextEditor组件文本样式。 |
| ArkUI_FontStyle* fontStyle | 字体样式。取值为ArkUI_FontStyle中的枚举。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorTextStyle_SetFontWeight()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_SetFontWeight(OH_ArkUI_TextEditorTextStyle* style, uint32_t fontWeight)
```

**描述**

设置文本样式的字体粗细。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorTextStyle* style | TextEditor组件文本样式。 |
| uint32_t fontWeight | 字体粗细。取值为ArkUI_FontWeight中的枚举值，默认值为ARKUI_FONT_WEIGHT_W400。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorTextStyle_GetFontWeight()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_GetFontWeight(OH_ArkUI_TextEditorTextStyle* style, uint32_t* fontWeight)
```

**描述**

获取文本样式的字体粗细。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorTextStyle* style | TextEditor组件文本样式。 |
| uint32_t* fontWeight | 字体粗细。取值为ArkUI_FontWeight中的枚举值，默认值为ARKUI_FONT_WEIGHT_W400。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorTextStyle_SetFontFamily()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_SetFontFamily(OH_ArkUI_TextEditorTextStyle* style, const char* fontFamily)
```

**描述**

设置文本样式的字体家族。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorTextStyle* style | TextEditor组件文本样式。 |
| const char* fontFamily | 字体家族。存放待设置的字体名称，不同字体名称通过逗号拼接。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorTextStyle_GetFontFamily()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_GetFontFamily(OH_ArkUI_TextEditorTextStyle* style, char* buffer, int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取文本样式的字体家族。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorTextStyle* style | TextEditor组件文本样式。 |
| char* buffer | 字体家族内容写入内存的缓冲区，内存空间需由开发者分配。 |
| int32_t bufferSize | 缓冲区最多可写入的字符的数量。 |
| int32_t* writeLength | 实际写入缓冲区的字符的数量。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorTextStyle_SetDecoration()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_SetDecoration(OH_ArkUI_TextEditorTextStyle* style, OH_ArkUI_DecorationStyleOptions* options)
```

**描述**

设置文本样式的文本装饰选项。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorTextStyle* style | TextEditor组件文本样式。 |
| OH_ArkUI_DecorationStyleOptions* options | 指向OH_ArkUI_DecorationStyleOptions对象的指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorTextStyle_GetDecoration()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_GetDecoration(OH_ArkUI_TextEditorTextStyle* style, OH_ArkUI_DecorationStyleOptions* options)
```

**描述**

获取文本样式的文本装饰选项。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorTextStyle* style | TextEditor组件文本样式。 |
| OH_ArkUI_DecorationStyleOptions* options | 指向OH_ArkUI_DecorationStyleOptions对象的指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorTextStyle_SetTextShadows()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_SetTextShadows(OH_ArkUI_TextEditorTextStyle* style, const OH_ArkUI_ShadowOptions** options, int32_t length)
```

**描述**

设置文本样式的文本阴影选项。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorTextStyle* style | TextEditor组件文本样式。 |
| const OH_ArkUI_ShadowOptions** options | 文本阴影选项。 |
| int32_t length | 文本阴影选项的长度。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorTextStyle_GetTextShadows()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_GetTextShadows(OH_ArkUI_TextEditorTextStyle* style, OH_ArkUI_ShadowOptions** shadowOptions, uint32_t shadowOptionsSize, uint32_t* writeLength)
```

**描述**

获取文本样式的文本阴影选项。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorTextStyle* style | TextEditor组件文本样式。 |
| OH_ArkUI_ShadowOptions** shadowOptions | 文本阴影选项。 |
| uint32_t shadowOptionsSize | 阴影选项的缓冲区大小。 |
| uint32_t* writeLength | 文本样式中实际的文本阴影选项数量。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorTextStyle_SetLineHeight()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_SetLineHeight(OH_ArkUI_TextEditorTextStyle* style, int32_t lineHeight)
```

**描述**

设置文本样式的文本行高。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorTextStyle* style | TextEditor组件文本样式。 |
| int32_t lineHeight | 文本行高。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorTextStyle_GetLineHeight()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_GetLineHeight(OH_ArkUI_TextEditorTextStyle* style, int32_t* lineHeight)
```

**描述**

获取文本样式的文本行高。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorTextStyle* style | TextEditor组件文本样式。 |
| int32_t* lineHeight | 文本行高。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorTextStyle_SetLetterSpacing()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_SetLetterSpacing(OH_ArkUI_TextEditorTextStyle* style, int32_t letterSpacing)
```

**描述**

设置文本样式的字符间距。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorTextStyle* style | TextEditor组件文本样式。 |
| int32_t letterSpacing | 字符间距。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorTextStyle_GetLetterSpacing()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_GetLetterSpacing(OH_ArkUI_TextEditorTextStyle* style, int32_t* letterSpacing)
```

**描述**

获取文本样式的字符间距。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorTextStyle* style | TextEditor组件文本样式。 |
| int32_t* letterSpacing | 字符间距。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorTextStyle_SetFontFeature()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_SetFontFeature(OH_ArkUI_TextEditorTextStyle* style, const char* fontFeature)
```

**描述**

设置文本样式的文字特性效果，比如数字等宽的特性。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorTextStyle* style | TextEditor组件文本样式。 |
| const char* fontFeature | 字体特性。存放待设置的字体特性，多个特性通过逗号拼接。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorTextStyle_GetFontFeature()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_GetFontFeature(OH_ArkUI_TextEditorTextStyle* style, char* buffer, int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取文本样式的文字特性效果，比如数字等宽的特性。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorTextStyle* style | TextEditor组件文本样式。 |
| char* buffer | 字体特性内容写入内存的缓冲区，内存空间需由开发者分配。 |
| int32_t bufferSize | 缓冲区最多可写入的字符的数量。 |
| int32_t* writeLength | 实际表示写入缓冲区的字符的数量。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorTextStyle_SetHalfLeading()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_SetHalfLeading(OH_ArkUI_TextEditorTextStyle* style, bool halfLeading)
```

**描述**

设置文本样式中文本是否将行间距平分至行的顶部与底部。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorTextStyle* style | TextEditor组件文本样式。 |
| bool halfLeading | 文本是否将行间距平分至行的顶部与底部。 true表示将行间距平分至行的顶部与底部，false表示不将行间距平分至行的顶部与底部。默认值为false。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorTextStyle_GetHalfLeading()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_GetHalfLeading(OH_ArkUI_TextEditorTextStyle* style, bool* halfLeading)
```

**描述**

获取文本样式中文本是否将行间距平分至行的顶部与底部。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorTextStyle* style | TextEditor组件文本样式。 |
| bool* halfLeading | 文本是否将行间距平分至行的顶部与底部。 true表示将行间距平分至行的顶部与底部，false表示不将行间距平分至行的顶部与底部。默认值为false。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorTextStyle_SetTextBackgroundColor()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_SetTextBackgroundColor(OH_ArkUI_TextEditorTextStyle* style, uint32_t color)
```

**描述**

设置文本样式中的文本背景颜色。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorTextStyle* style | TextEditor组件文本样式。 |
| uint32_t color | 文本背景颜色，0xARGB格式。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorTextStyle_GetTextBackgroundColor()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_GetTextBackgroundColor(OH_ArkUI_TextEditorTextStyle* style, uint32_t* color)
```

**描述**

获取文本样式中的文本背景颜色。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorTextStyle* style | TextEditor组件文本样式。 |
| uint32_t* color | 文本背景颜色，0xARGB格式。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorTextStyle_SetTextBackgroundRadius()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_SetTextBackgroundRadius(OH_ArkUI_TextEditorTextStyle* style, float topLeft, float topRight, float bottomLeft, float bottomRight)
```

**描述**

设置文本样式中文本背景的圆角半径。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorTextStyle* style | TextEditor组件文本样式。 |
| float topLeft | 文本背景左上角的圆角半径。单位为vp。 |
| float topRight | 文本背景右上角的圆角半径。单位为vp。 |
| float bottomLeft | 文本背景左下角的圆角半径。单位为vp。 |
| float bottomRight | 文本背景右下角的圆角半径。单位为vp。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorTextStyle_GetTextBackgroundRadius()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorTextStyle_GetTextBackgroundRadius(OH_ArkUI_TextEditorTextStyle* style, float* topLeft, float* topRight, float* bottomLeft, float* bottomRight)
```

**描述**

获取文本样式中文本背景的圆角半径。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorTextStyle* style | TextEditor组件文本样式。 |
| float* topLeft | 文本背景左上角的圆角半径。单位为vp。 |
| float* topRight | 文本背景右上角的圆角半径。单位为vp。 |
| float* bottomLeft | 文本背景左下角的圆角半径。单位为vp。 |
| float* bottomRight | 文本背景右下角的圆角半径。单位为vp。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorStyledStringController_SetTypingStyle()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorStyledStringController_SetTypingStyle(OH_ArkUI_TextEditorStyledStringController* controller, OH_ArkUI_TextEditorTextStyle* style)
```

**描述**

通过属性字符串控制器设置预设输入样式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorStyledStringController* controller | 指向OH_ArkUI_TextEditorStyledStringController对象的指针。 |
| OH_ArkUI_TextEditorTextStyle* style | 预设输入样式。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorStyledStringController_GetTypingStyle()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorStyledStringController_GetTypingStyle(OH_ArkUI_TextEditorStyledStringController* controller, OH_ArkUI_TextEditorTextStyle* style)
```

**描述**

通过属性字符串控制器获取预设输入样式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorStyledStringController* controller | 指向OH_ArkUI_TextEditorStyledStringController对象的指针。 |
| OH_ArkUI_TextEditorTextStyle* style | 预设输入样式。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorSelectionMenuOptions_SetSpanType()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorSelectionMenuOptions_SetSpanType(OH_ArkUI_TextEditorSelectionMenuOptions* options, OH_ArkUI_TextEditorSpanType textEditorSpanType)
```

**描述**

设置文本编辑器中文本选择菜单的span的类型。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorSelectionMenuOptions* options | 指向OH_ArkUI_TextEditorSelectionMenuOptions对象的指针。 |
| OH_ArkUI_TextEditorSpanType textEditorSpanType | span的类型。取值为OH_ArkUI_TextEditorSpanType中的枚举。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorSelectionMenuOptions_GetSpanType()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorSelectionMenuOptions_GetSpanType(OH_ArkUI_TextEditorSelectionMenuOptions* options, OH_ArkUI_TextEditorSpanType* textEditorSpanType)
```

**描述**

获取文本编辑器中文本选择菜单的span的类型。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorSelectionMenuOptions* options | 指向OH_ArkUI_TextEditorSelectionMenuOptions对象的指针。 |
| OH_ArkUI_TextEditorSpanType* textEditorSpanType | span的类型。取值为OH_ArkUI_TextEditorSpanType中的枚举。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorSelectionMenuOptions_SetContentNode()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorSelectionMenuOptions_SetContentNode(OH_ArkUI_TextEditorSelectionMenuOptions* options, ArkUI_NodeHandle node)
```

**描述**

设置文本编辑器中文本选择菜单的内容节点。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorSelectionMenuOptions* options | 指向OH_ArkUI_TextEditorSelectionMenuOptions对象的指针。 |
| ArkUI_NodeHandle node | 内容节点。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorSelectionMenuOptions_GetContentNode()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorSelectionMenuOptions_GetContentNode(OH_ArkUI_TextEditorSelectionMenuOptions* options, ArkUI_NodeHandle* node)
```

**描述**

获取文本编辑器中文本选择菜单的内容节点。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorSelectionMenuOptions* options | 指向OH_ArkUI_TextEditorSelectionMenuOptions对象的指针。 |
| ArkUI_NodeHandle* node | 内容节点。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorSelectionMenuOptions_SetResponseType()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorSelectionMenuOptions_SetResponseType(OH_ArkUI_TextEditorSelectionMenuOptions* options, OH_ArkUI_TextEditorResponseType responseType)
```

**描述**

设置文本编辑器中文本选择菜单的响应类型。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorSelectionMenuOptions* options | 指向OH_ArkUI_TextEditorSelectionMenuOptions对象的指针。 |
| OH_ArkUI_TextEditorResponseType responseType | 响应类型。取值为OH_ArkUI_TextEditorResponseType中的枚举。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorSelectionMenuOptions_GetResponseType()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorSelectionMenuOptions_GetResponseType(OH_ArkUI_TextEditorSelectionMenuOptions* options, OH_ArkUI_TextEditorResponseType* responseType)
```

**描述**

获取文本编辑器中文本选择菜单的响应类型。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorSelectionMenuOptions* options | 指向OH_ArkUI_TextEditorSelectionMenuOptions对象的指针。 |
| OH_ArkUI_TextEditorResponseType* responseType | 响应类型。取值为OH_ArkUI_TextEditorResponseType中的枚举。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorSelectionMenuOptions_SetMenuType()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorSelectionMenuOptions_SetMenuType(OH_ArkUI_TextEditorSelectionMenuOptions* options, OH_ArkUI_TextMenuType menuType)
```

**描述**

设置文本编辑器中文本选择菜单的类型。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorSelectionMenuOptions* options | 指向OH_ArkUI_TextEditorSelectionMenuOptions对象的指针。 |
| OH_ArkUI_TextMenuType menuType | 菜单类型。取值为OH_ArkUI_TextMenuType中的枚举。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorSelectionMenuOptions_GetMenuType()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorSelectionMenuOptions_GetMenuType(OH_ArkUI_TextEditorSelectionMenuOptions* options, OH_ArkUI_TextMenuType* menuType)
```

**描述**

获取文本编辑器中文本选择菜单的类型。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorSelectionMenuOptions* options | 指向OH_ArkUI_TextEditorSelectionMenuOptions对象的指针。 |
| OH_ArkUI_TextMenuType* menuType | 菜单类型。取值为OH_ArkUI_TextMenuType中的枚举。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorSelectionMenuOptions_RegisterOnMenuShowCallback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorSelectionMenuOptions_RegisterOnMenuShowCallback(OH_ArkUI_TextEditorSelectionMenuOptions* options, void* userData, void (*callback)(int32_t start, int32_t end, void* callbackUserData))
```

**描述**

设置文本选择菜单显示时触发的事件。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorSelectionMenuOptions* options | 指向OH_ArkUI_TextEditorSelectionMenuOptions对象的指针。 |
| void* userData | 用户数据。 |
| void (*callback)(int32_t start | 菜单显示的回调函数。start 选中内容的起始偏移量。end 选中内容的结束偏移量。callbackUserData 用户数据。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorSelectionMenuOptions_RegisterOnMenuHideCallback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorSelectionMenuOptions_RegisterOnMenuHideCallback(OH_ArkUI_TextEditorSelectionMenuOptions* options, void* userData, void (*callback)(int32_t start, int32_t end, void* callbackUserData))
```

**描述**

设置文本选择菜单隐藏时触发的事件。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorSelectionMenuOptions* options | 指向OH_ArkUI_TextEditorSelectionMenuOptions对象的指针。 |
| void* userData | 用户数据。 |
| void (*callback)(int32_t start | 菜单隐藏的回调函数。start 选中内容的起始偏移量。end 选中内容的结束偏移量。callbackUserData 用户数据。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorSelectionMenuOptions_RegisterOnMenuAppearCallback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorSelectionMenuOptions_RegisterOnMenuAppearCallback(OH_ArkUI_TextEditorSelectionMenuOptions* options, void* userData, void (*callback)(int32_t start, int32_t end, void* callbackUserData))
```

**描述**

设置文本选择菜单出现时触发的事件。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorSelectionMenuOptions* options | 指向OH_ArkUI_TextEditorSelectionMenuOptions对象的指针。 |
| void* userData | 用户数据。 |
| void (*callback)(int32_t start | 菜单出现的回调函数。start 选中内容的起始偏移量。end 选中内容的结束偏移量。callbackUserData 用户数据。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorSelectionMenuOptions_RegisterOnMenuDisappearCallback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorSelectionMenuOptions_RegisterOnMenuDisappearCallback(OH_ArkUI_TextEditorSelectionMenuOptions* options, void* userData, void (*callback)(void* callbackUserData))
```

**描述**

设置文本选择菜单消失时触发的事件。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorSelectionMenuOptions* options | 指向OH_ArkUI_TextEditorSelectionMenuOptions对象的指针。 |
| void* userData | 用户数据。 |
| void (*callback)(void* callbackUserData) | 菜单消失的回调函数。callbackUserData 用户数据。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorSelectionMenuOptions_SetHapticFeedbackMode()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorSelectionMenuOptions_SetHapticFeedbackMode(OH_ArkUI_TextEditorSelectionMenuOptions* options, OH_ArkUI_HapticFeedbackMode mode)
```

**描述**

设置文本编辑器中文本选择菜单的触觉反馈模式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorSelectionMenuOptions* options | 指向OH_ArkUI_TextEditorSelectionMenuOptions对象的指针。 |
| OH_ArkUI_HapticFeedbackMode mode | 触觉反馈模式。取值为OH_ArkUI_HapticFeedbackMode中的枚举。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorSelectionMenuOptions_GetHapticFeedbackMode()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorSelectionMenuOptions_GetHapticFeedbackMode(OH_ArkUI_TextEditorSelectionMenuOptions* options, OH_ArkUI_HapticFeedbackMode* mode)
```

**描述**

获取文本编辑器中文本选择菜单的触觉反馈模式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorSelectionMenuOptions* options | 指向OH_ArkUI_TextEditorSelectionMenuOptions对象的指针。 |
| OH_ArkUI_HapticFeedbackMode* mode | 触觉反馈模式。取值为OH_ArkUI_HapticFeedbackMode中的枚举。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorStyledStringController_CloseSelectionMenu()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorStyledStringController_CloseSelectionMenu(OH_ArkUI_TextEditorStyledStringController* controller)
```

**描述**

关闭文本编辑器属性字符串控制器的文本选择菜单。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorStyledStringController* controller | 指向OH_ArkUI_TextEditorStyledStringController对象的指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorStyledStringController_GetSelection()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorStyledStringController_GetSelection(const OH_ArkUI_TextEditorStyledStringController* controller, uint32_t* start, uint32_t* end)
```

**描述**

通过属性字符串控制器获取选中区域。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const OH_ArkUI_TextEditorStyledStringController* controller | 指向OH_ArkUI_TextEditorStyledStringController对象的指针。 |
| uint32_t* start | 选中区域的起始位置。 |
| uint32_t* end | 选中区域的结束位置。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorStyledStringController_SetStyledString()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorStyledStringController_SetStyledString(const OH_ArkUI_TextEditorStyledStringController* controller, const ArkUI_StyledString_Descriptor* descriptor)
```

**描述**

通过属性字符串控制器设置显示的属性字符串。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const OH_ArkUI_TextEditorStyledStringController* controller | 指向OH_ArkUI_TextEditorStyledStringController对象的指针。 |
| const ArkUI_StyledString_Descriptor* descriptor | 指向ArkUI_StyledString_Descriptor对象的指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorStyledStringController_GetStyledString()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorStyledStringController_GetStyledString(const OH_ArkUI_TextEditorStyledStringController* controller, ArkUI_StyledString_Descriptor* descriptor)
```

**描述**

通过属性字符串控制器获取显示的属性字符串。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const OH_ArkUI_TextEditorStyledStringController* controller | 指向OH_ArkUI_TextEditorStyledStringController对象的指针。 |
| ArkUI_StyledString_Descriptor* descriptor | 指向ArkUI_StyledString_Descriptor对象的指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorStyledStringController_SetStyledPlaceholder()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorStyledStringController_SetStyledPlaceholder(const OH_ArkUI_TextEditorStyledStringController* controller, const ArkUI_StyledString_Descriptor* descriptor)
```

**描述**

通过属性字符串控制器设置属性字符串样式的提示文本。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const OH_ArkUI_TextEditorStyledStringController* controller | 指向OH_ArkUI_TextEditorStyledStringController对象的指针。 |
| const ArkUI_StyledString_Descriptor* descriptor | 指向ArkUI_StyledString_Descriptor对象的指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_TextEditorStyledStringController_ScrollToVisible()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextEditorStyledStringController_ScrollToVisible(const OH_ArkUI_TextEditorStyledStringController* controller, int32_t start, int32_t end)
```

**描述**

通过属性字符串控制器使指定起始索引至结束索引范围内的内容滚动至可视区域。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const OH_ArkUI_TextEditorStyledStringController* controller | 指向OH_ArkUI_TextEditorStyledStringController对象的指针。 |
| int32_t start | 起始内容索引值。 起始索引应小于等于结束索引，否则接口调用无效。取值范围[0, TextEditor组件内容总长度]，起始索引小于0视为0，大于总长度视为总长度。 |
| int32_t end | 结束内容索引值。 结束索引应大于等于起始索引，否则接口调用无效。取值范围[0, TextEditor组件内容总长度]，结束索引小于0视为0，大于总长度视为总长度。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果码。 若操作成功，返回ARKUI_ERROR_CODE_NO_ERROR。 若参数异常，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_PickerIndicatorStyle_ConfigureBackground()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_PickerIndicatorStyle_ConfigureBackground(ArkUI_PickerIndicatorStyle* style, ArkUI_PickerIndicatorBackground* background)
```

**描述**

设置背景样式参数，此接口仅当选择器选中项样式枚举类型为[ARKUI_PICKER_INDICATOR_BACKGROUND](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-picker-h#arkui_pickerindicatortype)时生效。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_PickerIndicatorStyle* style | 选中项指示器样式ArkUI_PickerIndicatorStyle的实例。 |
| ArkUI_PickerIndicatorBackground* background | 背景样式参数。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |




#### OH_ArkUI_PickerIndicatorStyle_ConfigureDivider()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_PickerIndicatorStyle_ConfigureDivider(ArkUI_PickerIndicatorStyle* style, ArkUI_PickerIndicatorDivider* divider)
```

**描述**

设置分割线样式参数，此接口仅当选择器选中项样式枚举类型为[ARKUI_PICKER_INDICATOR_DIVIDER](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-picker-h#arkui_pickerindicatortype)时生效。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ArkUI_PickerIndicatorStyle* style | 选中项指示器样式ArkUI_PickerIndicatorStyle的实例。 |
| ArkUI_PickerIndicatorDivider* divider | 分割线样式参数。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |




#### OH_ArkUI_TextController_SetStyledString()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_TextController_SetStyledString(OH_ArkUI_TextController* controller, ArkUI_StyledString_Descriptor* descriptor)
```

**描述**

设置文本组件的属性字符串。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextController* controller | 指向OH_ArkUI_TextController对象的指针。 |
| ArkUI_StyledString_Descriptor* descriptor | 指向ArkUI_StyledString_Descriptor对象的指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 返回结果。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |




#### OH_ArkUI_LinearGradientOptions_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_ArkUI_LinearGradientOptions* OH_ArkUI_LinearGradientOptions_Create()
```

**描述**

创建线性渐变效果选项对象。

**起始版本：** 26.0.0

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH_ArkUI_LinearGradientOptions* | 指向OH_ArkUI_LinearGradientOptions*的指针。 |




#### OH_ArkUI_LinearGradientOptions_Destroy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_LinearGradientOptions_Destroy(OH_ArkUI_LinearGradientOptions* options)
```

**描述**

销毁线性渐变效果选项对象。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_LinearGradientOptions* options | 指向OH_ArkUI_LinearGradientOptions对象的指针。 |




#### OH_ArkUI_LinearGradientOptions_SetAngle()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_LinearGradientOptions_SetAngle(OH_ArkUI_LinearGradientOptions* options, float angle)
```

**描述**

设置线性渐变效果选项的角度。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_LinearGradientOptions* options | 指向OH_ArkUI_LinearGradientOptions对象的指针。 |
| float angle | 线性渐变效果选项的角度。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 操作结果码。 操作成功时，返回ARKUI_ERROR_CODE_NO_ERROR。 参数异常时，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_LinearGradientOptions_GetAngle()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_LinearGradientOptions_GetAngle(const OH_ArkUI_LinearGradientOptions* options, float* angle)
```

**描述**

获取线性渐变效果选项的角度。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const OH_ArkUI_LinearGradientOptions* options | 指向OH_ArkUI_LinearGradientOptions对象的指针。 |
| float* angle | 线性渐变效果选项的角度。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 操作结果码。 操作成功时，返回ARKUI_ERROR_CODE_NO_ERROR。 参数异常时，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_LinearGradientOptions_SetDirection()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_LinearGradientOptions_SetDirection(OH_ArkUI_LinearGradientOptions* options, ArkUI_LinearGradientDirection direction)
```

**描述**

设置线性渐变选项的方向。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_LinearGradientOptions* options | 指向OH_ArkUI_LinearGradientOptions对象的指针。 |
| ArkUI_LinearGradientDirection direction | 线性渐变选项的方向。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 操作结果码。 操作成功时，返回ARKUI_ERROR_CODE_NO_ERROR。 参数异常时，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_LinearGradientOptions_GetDirection()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_LinearGradientOptions_GetDirection(const OH_ArkUI_LinearGradientOptions* options, ArkUI_LinearGradientDirection* direction)
```

**描述**

获取线性渐变选项的方向。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const OH_ArkUI_LinearGradientOptions* options | 指向OH_ArkUI_LinearGradientOptions对象的指针。 |
| ArkUI_LinearGradientDirection* direction | 线性渐变选项的方向。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 操作结果码。 操作成功时，返回ARKUI_ERROR_CODE_NO_ERROR。 参数异常时，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_LinearGradientOptions_SetRepeating()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_LinearGradientOptions_SetRepeating(OH_ArkUI_LinearGradientOptions* options, bool repeating)
```

**描述**

设置颜色是否在线性渐变选项中重复。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_LinearGradientOptions* options | 指向OH_ArkUI_LinearGradientOptions对象的指针。 |
| bool repeating | 颜色是否在线性渐变选项中重复，false表示不重复着色，true表示重复着色。默认值：false。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 操作结果码。 操作成功时，返回ARKUI_ERROR_CODE_NO_ERROR。 参数异常时，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_LinearGradientOptions_GetRepeating()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_LinearGradientOptions_GetRepeating(const OH_ArkUI_LinearGradientOptions* options, bool* repeating)
```

**描述**

查询线性渐变选项中颜色是否重复。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const OH_ArkUI_LinearGradientOptions* options | 指向OH_ArkUI_LinearGradientOptions对象的指针。 |
| bool* repeating | 指向线性渐变选项中颜色是否重复的指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 操作结果码。 操作成功时，返回ARKUI_ERROR_CODE_NO_ERROR。 参数异常时，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_LinearGradientOptions_SetColorStop()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_LinearGradientOptions_SetColorStop(OH_ArkUI_LinearGradientOptions* options, const uint32_t* colors, const float* stops, int32_t colorsAndStopsSize)
```

**描述**

设置线性渐变选项的颜色停止点。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_LinearGradientOptions* options | 指向OH_ArkUI_LinearGradientOptions对象的指针。 |
| const uint32_t* colors | 指向颜色数组的指针。 |
| const float* stops | 指向颜色停止点数组的指针。 |
| int32_t colorsAndStopsSize | 颜色和颜色停止点中的元素数量。颜色和颜色停止点的元素数量必须相同。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 操作结果码。 操作成功时，返回ARKUI_ERROR_CODE_NO_ERROR。 参数异常时，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_LinearGradientOptions_GetColorStop()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_LinearGradientOptions_GetColorStop(const OH_ArkUI_LinearGradientOptions* options, uint32_t* colors, float* stops, int32_t colorsAndStopsSize, int32_t* writeLength)
```

**描述**

获取线性渐变选项的颜色停止点。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const OH_ArkUI_LinearGradientOptions* options | 指向OH_ArkUI_LinearGradientOptions对象的指针。 |
| uint32_t* colors | 指向颜色数组的指针。 |
| float* stops | 指向颜色停止点数组的指针。 |
| int32_t colorsAndStopsSize | 颜色和颜色停止点中的元素数量。颜色和颜色停止点的元素数量必须相同。 |
| int32_t* writeLength | 实际写入的颜色及颜色停止点数量。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 操作结果码。 操作成功时，返回ARKUI_ERROR_CODE_NO_ERROR。 参数异常时，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_RadialGradientOptions_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_ArkUI_RadialGradientOptions* OH_ArkUI_RadialGradientOptions_Create()
```

**描述**

创建一个径向渐变选项对象。

**起始版本：** 26.0.0

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH_ArkUI_RadialGradientOptions* | 指向OH_ArkUI_RadialGradientOptions对象的指针。 |




#### OH_ArkUI_RadialGradientOptions_Destroy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_RadialGradientOptions_Destroy(OH_ArkUI_RadialGradientOptions* options)
```

**描述**

销毁一个径向渐变选项对象。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_RadialGradientOptions* options | 指向OH_ArkUI_RadialGradientOptions对象的指针。 |




#### OH_ArkUI_RadialGradientOptions_SetCenterX()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_RadialGradientOptions_SetCenterX(OH_ArkUI_RadialGradientOptions* options, float centerX)
```

**描述**

设置径向渐变选项中心点的X坐标。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_RadialGradientOptions* options | 指向OH_ArkUI_RadialGradientOptions对象的指针。 |
| float centerX | 径向渐变选项中心点的X坐标。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 操作结果码。 操作成功时，返回ARKUI_ERROR_CODE_NO_ERROR。 参数异常时，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_RadialGradientOptions_GetCenterX()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_RadialGradientOptions_GetCenterX(const OH_ArkUI_RadialGradientOptions* options, float* centerX)
```

**描述**

获取径向渐变选项中心点的X坐标。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const OH_ArkUI_RadialGradientOptions* options | 指向OH_ArkUI_RadialGradientOptions对象的指针。 |
| float* centerX | 指向径向渐变选项中心点的X坐标。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 操作结果码。 操作成功时，返回ARKUI_ERROR_CODE_NO_ERROR。 参数异常时，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_RadialGradientOptions_SetCenterY()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_RadialGradientOptions_SetCenterY(OH_ArkUI_RadialGradientOptions* options, float centerY)
```

**描述**

设置径向渐变选项中心点的Y坐标。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_RadialGradientOptions* options | 指向OH_ArkUI_RadialGradientOptions对象的指针。 |
| float centerY | 径向渐变选项中心点的Y坐标。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 操作结果码。 操作成功时，返回ARKUI_ERROR_CODE_NO_ERROR。 参数异常时，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_RadialGradientOptions_GetCenterY()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_RadialGradientOptions_GetCenterY(const OH_ArkUI_RadialGradientOptions* options, float* centerY)
```

**描述**

获取径向渐变选项中心点的Y坐标。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const OH_ArkUI_RadialGradientOptions* options | 指向OH_ArkUI_RadialGradientOptions对象的指针。 |
| float* centerY | 指向径向渐变选项中心点的Y坐标。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 操作结果码。 操作成功时，返回ARKUI_ERROR_CODE_NO_ERROR。 参数异常时，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_RadialGradientOptions_SetRadius()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_RadialGradientOptions_SetRadius(OH_ArkUI_RadialGradientOptions* options, float radius)
```

**描述**

设置径向渐变选项的半径。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_RadialGradientOptions* options | 指向OH_ArkUI_RadialGradientOptions对象的指针。 |
| float radius | 径向渐变选项的半径。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 操作结果码。 操作成功时，返回ARKUI_ERROR_CODE_NO_ERROR。 参数异常时，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_RadialGradientOptions_GetRadius()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_RadialGradientOptions_GetRadius(const OH_ArkUI_RadialGradientOptions* options, float* radius)
```

**描述**

获取径向渐变选项的半径。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const OH_ArkUI_RadialGradientOptions* options | 指向OH_ArkUI_RadialGradientOptions对象的指针。 |
| float* radius | 指向径向渐变选项的半径的指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 操作结果码。 操作成功时，返回ARKUI_ERROR_CODE_NO_ERROR。 参数异常时，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_RadialGradientOptions_SetRepeating()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_RadialGradientOptions_SetRepeating(OH_ArkUI_RadialGradientOptions* options, bool repeating)
```

**描述**

设置径向渐变选项中颜色是否重复。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_RadialGradientOptions* options | 指向OH_ArkUI_RadialGradientOptions对象的指针。 |
| bool repeating | 径向渐变选项中颜色是否重复，false表示不重复着色，true表示重复着色。默认值：false。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 操作结果码。 操作成功时，返回ARKUI_ERROR_CODE_NO_ERROR。 参数异常时，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_RadialGradientOptions_GetRepeating()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_RadialGradientOptions_GetRepeating(const OH_ArkUI_RadialGradientOptions* options, bool* repeating)
```

**描述**

查询径向渐变选项中颜色是否重复。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const OH_ArkUI_RadialGradientOptions* options | 指向OH_ArkUI_RadialGradientOptions对象的指针。 |
| bool* repeating | 指向径向渐变选项中颜色是否重复的指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 操作结果码。 操作成功时，返回ARKUI_ERROR_CODE_NO_ERROR。 参数异常时，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_RadialGradientOptions_SetColorStop()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_RadialGradientOptions_SetColorStop(OH_ArkUI_RadialGradientOptions* options, const uint32_t* colors, const float* stops, int32_t colorsAndStopsSize)
```

**描述**

设置径向渐变选项的颜色停止点。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_RadialGradientOptions* options | 指向OH_ArkUI_RadialGradientOptions对象的指针。 |
| const uint32_t* colors | 指向颜色数组的指针。 |
| const float* stops | 指向颜色停止点数组的指针。 |
| int32_t colorsAndStopsSize | 颜色和颜色停止点中的元素数量。颜色和颜色停止点的元素数量必须相同。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 操作结果码。 操作成功时，返回ARKUI_ERROR_CODE_NO_ERROR。 参数异常时，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |




#### OH_ArkUI_RadialGradientOptions_GetColorStop()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ErrorCode OH_ArkUI_RadialGradientOptions_GetColorStop(const OH_ArkUI_RadialGradientOptions* options, uint32_t* colors, float* stops, int32_t colorsAndStopsSize, int32_t* writeLength)
```

**描述**

获取径向渐变选项的颜色停止点。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const OH_ArkUI_RadialGradientOptions* options | 指向OH_ArkUI_RadialGradientOptions对象的指针。 |
| uint32_t* colors | 指向颜色数组的缓冲区指针。 |
| float* stops | 指向颜色停止点数组的指针。 |
| int32_t colorsAndStopsSize | 颜色和颜色停止点中的元素数量。颜色和颜色停止点的元素数量必须相同。 |
| int32_t* writeLength | 实际写入的颜色停止点数量。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ArkUI_ErrorCode | 操作结果码。 操作成功时，返回ARKUI_ERROR_CODE_NO_ERROR。 参数异常时，返回ARKUI_ERROR_CODE_PARAM_INVALID。 |
