# OS新增和增强特性

更新时间：2026-04-30 02:39:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/os-new-feature-510

#### 关键特性

HarmonyOS 5.1.0 Release版本重点提供如下的开放能力。全量新增接口可查看[API变更清单](https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/apidiff-510)。
 
 

#### Ability Kit

- 新增支持根据指定的数据加密级别创建应用上下文，以获取相应的路径。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context#createareamodecontext18)）
- 新增支持同步获取当前进程的进程名（processName）。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context#属性)）
- 新增支持获取应用被拉起原因（LAUNCH_REASON_MESSAGE）。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-wantconstant#params)）
- 启动框架新增支持HAR/HSP和so文件。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-startup#支持的范围)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-appstartup-startupmanager)）
- 新增支持获取应用上次异常退出的详细原因。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-exit-info-record)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilityconstant#lastexitdetailinfo18)）
- 新增支持设置UIAbility的颜色模式。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#setcolormode18)）

 
 

#### Account Kit

- 华为账号授权支持Wearable设备获取用户头像昵称、手机号和风险等级等信息。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-introduction#约束与限制)）
- 登录场景支持获取用户风险等级。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-get-risklevel)）

 
 

#### AppGallery Kit

应用市场更新功能、图标管理服务支持Wearable设备。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-introduction#支持的设备)）
 
 

#### AR Engine

- 新增ArkTS API，支持运动跟踪能力、环境跟踪能力和命中检测能力，包括[管理AR会话](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-arsession)、[获取设备位姿](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-get-pose)、检[测环境中的平面](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-get-plane)、[识别平面语义](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-get-semantics)、[获取深度估计信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-get-depth)、[获取网格扫描信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-get-mesh)、[图像跟踪](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-image-track)、[AR物体摆放](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-arworld)。
- 新增C API，支持如下特性：
图像跟踪，实现传入图像数据对现实环境中的物体进行识别跟踪。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-image-track)）
- 获取网格扫描信息，实现检测当前环境中的物体，并对物体表面进行网格化。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-get-mesh)）

 
 
 

#### ArkData

- RelationalStore新增rootDir配置，支持打开非database目录下的数据库（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-i#storeconfig)）
- ArkData RDB向量数据管理新增支持对向量数据的快速检索和相似性搜索。（[指南-ArkTS](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-persistence-by-vector-store)、[指南-C/C++](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-vector-store-guidelines)）
- 关系型数据库新增支持根据指定的列索引或列名称获取列数据类型。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-resultset#getcolumntype18)）

 
 

#### ArkTS

- TaskPool支持指定任务执行并发度和指定任务的排队策略。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-taskpool#asyncrunner18)）
- TaskPool支持通过任务ID取消任务池中的任务。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-taskpool#taskpoolcancel18)）
- collections（ArkTS容器集）在API 18新增支持以下方法（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkts-collections)）：Array：from、isArray、of、copyWithin、lastIndexOf、some、reduceRight、reverse、toString、every、toLocaleString

  TypedArray：toString、toLocaleString、lastIndexOf、reduceRight
- Sendable支持在缓存空间不够的时候，将近期最少使用的数据替换为新数据。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-utils-sendablelrucache)）
- Worker支持创建任务时指定任务的优先级。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-worker#threadworkerpriority18)）

 
 

#### ArkUI

- 文本与输入组件能力增强。包括：
文本组件支持通过NODE_IMMUTABLE_FONT_WEIGHT属性，设置文字粗细不会跟随系统字体粗细而变化。（[API参考-C API](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h#arkui_nodeattributetype)）
- 文本组件支持对选中的文本提供分享服务 （[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common#属性)）、支持按音节连字符换行（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#wordbreak11)）。
- 富文本（RichEditor）组件支持设置最大行数。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#maxlength18)）
- TextInput组件支持设置文本省略位置。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#ellipsismode18)）
- TextInput/TextArea/Search/RichEditor组件支持将文本行间距平分至行的顶部与底部。（[API参考-TextInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#halfleading18)、[API参考-TextArea](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#halfleading18)、[API参考-Search](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-search#halfleading18)、[API参考-RichEditor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#richeditortextstyleresult)）
- TextInput/TextArea组件扩展自动填充类型，包含：车牌号、护照号等。（[API参考-ArkTS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#contenttype12枚举说明)、[API参考-C API](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_textinputcontenttype)）
- 富文本（RichEditor）组件在长按预览菜单时支持振动效果。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#previewmenuoptions18)）

 - 新增适配圆形屏幕的能力。包括：
新增旋转表冠事件，组件获焦后扭动表冠可获取时间戳、旋转角速度、旋转角度和表冠动作信息。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-crown)、[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-events-crown-event)）
- 新增弧形列表组件ArcList和ArcListItem，可呈现连续、多行的同类数据。（[API参考-ArcList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist)、[API参考-ArcListItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclistitem)、[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-arclist)）
- 新增弧形索引条组件ArcAlphabetIndexer，可按字母顺排序进行快速定位。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arc-alphabet-indexer)、[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-arclist#与弧形索引条arcalphabetindexer联动)）
- 新增弧形滚动条组件ArcScrollBar，可为弧形列表添加外置滚动条。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-arcscrollbar)、[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-arclist#添加外置滚动条arcscrollbar)）
- 新增弧形按钮组件ArcButton，可提供强调、普通、警告等样式按钮。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton)、[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-advanced-components-arcbutton)）

 - 通用拖拽能力增强。包括：
支持设置自定义落位动效。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-drag-drop#executedropanimation18)）

 
- 支持自定义控制在拖拽至可滚动组件边缘时，是否触发自动滚屏（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-drag-drop#draginteractionoptions12)）

 - 弹窗能力增强。包括：
支持通过设置levelOrder来管理弹出框的显示顺序，确保层级较高的弹出框覆盖在层级较低的弹出框之上。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-promptaction#showdialogoptions)、[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-dialog-levelorder)）
- 支持在自定义内容中，创建和关闭对应的自定义弹窗。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-promptaction#opencustomdialogwithcontroller18)）
- Popup组件支持通过maxWidth设置最大宽度。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-popup#popupoptions)）
- 半模态Popup样式弹窗，支持通过placement设置相对于目标的显示位置，通过placementOnTarget设置弹窗能否覆盖在目标节点上。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sheet-transition#sheetoptions)）
- Menu和Dialog支持通过backgroundBlurStyleOptions和backgroundEffect设置自定义背景模糊。（[API参考-Menu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-menu#contextmenuoptions10)、[API参考-Dialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-promptaction#showdialogoptions)）
- 模态转场和MenuItem支持!!双向绑定变量。（[API参考-半模态转场](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sheet-transition#bindsheet)、[API参考-全屏模态转场](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-modal-transition#bindcontentcover)、[API参考-MenuItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-menuitem#selected)）
- 自定义弹窗支持避让键盘后，通过keyboardAvoidDistance设置弹窗和键盘之间的最小距离。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-custom-dialog-box#customdialogcontrolleroptions对象说明)、[API参考-C API](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-2)）
- 支持通过effectEdge设置半模态面板边缘滚动的效果。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sheet-transition#sheetoptions)）

 - 表单选择类组件能力增强。包括：
新增SegmentButtonV2组件，可创建页签型、单选或多选的胶囊型分段按钮。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-segmentbuttonv2)）
- TextPicker/TimePicker支持选项进入选中区域时触发事件回调。（[API参考-TextPicker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textpicker#onenterselectedarea18)、[API参考-TimePicker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-timepicker#onenterselectedarea18)）
- TimePicker/CalendarPicker支持通过start和end配置开始时间和结束时间（[API参考-TimePicker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-timepicker#timepickeroptions对象说明)、[API参考-CalendarPicker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-calendarpicker#calendaroptions对象说明)）。
- TimePicker支持通过enableCascade设置12小时制时上午下午跟随时间联动。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-timepicker#enablecascade18)）

 - 滚动与滑动组件能力增强。包括：
Swiper/Tabs组件增加页面选中元素改变时触发的回调，返回当前选中或将要隐藏的元素的索引值。（[API参考-Swiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#onselected18)、[API参考-Tabs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#onselected18)）
- Swiper组件增加控制手指或者鼠标等按下屏幕时，子组件是否停止自动播放的能力。（[API参考-Swiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#autoplay18)）
- Swiper组件CAPI能力增强，可设置缓存节点是否显示、数字导航点和导航箭头的样式。（[API参考-C API](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-swiperdigitindicator)）
- List组件支持设置布局样式和滚动效果（NODE_LIST_SCROLL_TO_INDEX_IN_GROUP、 NODE_LIST_LANES、NODE_LIST_SCROLL_SNAP_ALIGN、NODE_LIST_MAINTAIN_VISIBLE_CONTENT_POSITION）（[API参考-C API](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h#arkui_nodeattributetype)）。

 - 新增C API，支持可配置用户自定义数据的手势中断事件回调函数。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativegestureapi-2)）
- 支持设置组件的自定义焦点走焦逻辑。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-focus#nextfocus18)、[API参考-C API](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_focusmove)）
- 支持动态获取手势配置参数，可返回连续点击次数阈值。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-common#taprecognizer18)）
- 支持手势取消时，触发的onActionCancel回调中返回手势事件信息。（[API参考-LongPressGesture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-longpressgesture#事件)、[API参考-PanGesture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-pangesture#事件)、[API参考-PinchGesture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-pinchgesture#事件)、[API参考-RotationGesture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-rotationgesture#事件)）
- 无障碍支持自定义焦点顺序（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-accessibility#accessibilitynextfocusid18)）、支持控制组件的屏幕朗读方式（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-accessibility#accessibilityrole18)）、支持设置屏幕朗读滚动操作（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-accessibility#accessibilityscrolltriggerable18)）。
- 支持设置EmbeddedComponent或UIExtensionComponent组件的占用事件，指定手势事件的响应方式。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-uiextension#occupyevents18)）
- 支持将当前FrameNode移动到目标FrameNode的指定位置，实现跨实例节点迁移。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-framenode#moveto18)、[API参考-C API](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h#oh_arkui_nodeutils_moveto)）
- NodeController新增节点上下树和绑定解绑前后的生命周期回调接口（onAttach、onDetach、onWillBind、onWillUnbind、onBind、onUnbind）。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-nodecontroller#onattach18)）
- 支持对ComponentContent构建的UI组件进行截图。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-componentsnapshot#createfromcomponent18)）
- 菜单（Menu）在弹出时支持振动效果。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-menu#hapticfeedbackmode18)）
- 窗口管理新增软键盘弹出动画完成的监听回调。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#onkeyboarddidshow18)）
- 窗口管理新增支持设置当前子窗口（未设置模态属性）的层级级别。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#setsubwindowzlevel18)）

 
 

#### ArkWeb

- 支持获取上一次被点击区域的元素信息。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#getlasthittest18)）
- 支持设置Web组件是否开启字重跟随系统设置变化。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-attributes#enablefollowsystemfontweight18)）
- 支持Web内音视频可对接到播控中心。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-attributes#enablewebavsession18)）
- 对接W3C规范，支持通过accept指定上传的文件类型。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onshowfileselector9)）
- 提供静态方法，清除应用中的资源缓存文件。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#removeallcache18)）

 
 

#### Asset Store Kit

新增基于群组的关键资产访问控制。通过设置群组属性，同一开发者开发的多个应用可以共享数据。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-js-group-access-control)）
 
 

#### Audio Kit

- 音频新增支持Float32格式音频输出。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiostream-base-h#oh_audiostream_sampleformat)）
- 新增支持空间音频管理的能力。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/public-audio-spatialization-management)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiomanager#getspatializationmanager18)）

 
 

#### AVCodec Kit

视频解码新增支持MPEG2、MPEG4。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/avcodec-support-formats)）
 
 

#### AVSession Kit

新增支持通过AV会话命令传递设置目标循环模式（setTargetLoopMode）的能力（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-t#avcontrolcommandtype10)），并提供对设置动作的事件监听回调（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-avsession#onsettargetloopmode18)）。
 
 

#### Basic Service Kit

- 上传下载支持应用缓存下载能力，支持应用提前缓存文件到沙箱目录或内存中。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-request-cachedownload)）
- 上传下载agent接口支持设置任务最高限速（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-request#setmaxspeed18)），支持设置待上传文件在表单中的content-type字段（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-request#requestagentfilespec10)）。
- 剪贴板支持获取剪贴板的内容变化的次数。（[API参考-ArkTS API](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-pasteboard#getchangecount18)、[API参考-C API](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-pasteboard-h#oh_pasteboard_getchangecount)）

 
 

#### CANN Kit（原HiAI Foundation Kit）

- Kit名称从HiAI Foundation Kit修改为CANN Kit，相关Kit API引用方式同步变更。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-introduction)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit)）
- 新增支持设置模型加载时的维测选项，用于采集Profiling性能数据。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit#hms_hiaioptions_setomoptions)）

 
 

#### Car Kit

导航信息服务支持向地图类应用发起兴趣点（POI）搜索。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/car-navigationinfomgr#commandtype)）
 
 

#### Cloud Foundation Kit

云函数、云数据库、云存储服务支持Wearable设备。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-introduction#支持的设备)）
 
 

#### Device Security Kit

新增ArkTS API，支持安全图像压缩、裁剪特性能力。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-taas-secimage-process)）
 
 

#### Distributed Service Kit

新增应用跨设备协同进行数据传输的能力。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/abilityconnectmanager-guidelines)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributed-abilityconnectionmanager)）
 
 

#### Form Kit

新增渲染模式的配置项renderingMode。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-configuration)）
 
 

#### Game Service Kit

- 新增游戏近场快传能力，支持设备在彼此靠近的情况下进行游戏数据交换。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-nearbytransfer-dev)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/gameservice-nearbytransfer)）
- 新增addGameCustomData接口，支持上报自定义数据。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/gameservice-gameperformance#gameperformanceaddgamecustomdata)）

 
 

#### Graphics Accelerate Kit

- 新增ArkTS API，支持资源包预下载能力。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-assetdownload-introduction)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/graphics-accelerate-arkts)）
- 新增支持系统送显模式，当游戏应用触发插帧任务后，系统会完成送显。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-fg-systempresent)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#fg_presentmode-1)）

 
 

#### Health Service Kit

- 新增情绪、心率变异性采样数据类型。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-emotion)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-samplepointhelper#fields-4)）
- 新增手动数据同步能力。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-cloudsync)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore#healthstoresyncall)）

 
 

#### IAP Kit

消耗型、非消耗型商品购买支持Wearable设备。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-introduction#支持的设备)）
 
 

#### Image Kit

新增C API支持获取图片的可编辑标志。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pixelmap-native-h#oh_pixelmapinitializationoptions_geteditable)）
 
 

#### Localization Kit

- 新增支持获取用户偏好温度单位和周起始日的能力，新增支持获取语言的最简表示的能力。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-i18n#gettemperaturetype18)）
- 新增支持时间日期/数字精细化格式化的能力，便于更灵活的使用格式化能力。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-i18n#i18ngetsimpledatetimeformatbypatterndeprecated)）
- 新增支持返回富文本的数字格式化能力。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-i18n#stylednumberformat18)）
- 新增支持路径本地化显示的能力，可以根据输入语言判断路径是否需要镜像显示。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-i18n#getunicodewrappedfilepathdeprecated)）

 
 

#### MDM Kit

- 可禁用/启用的特性限制新增MTP（mtpClient/mtpServer）和恢复出厂设置（resetFactory）。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-restrictions#restrictionssetdisallowedpolicy)）
- 新增支持按系统账户安装用户证书。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-securitymanager#securitymanagerinstallusercertificate18)）
- 新增支持订阅账号的新增、删除、切换系统事件。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-adminmanager#managedevent)）

 
 

#### Media Kit

- 播放器支持向应用透传SEI字段数据，适用于HTTP-FLV直播。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#onseimessagereceived18)）
- 调用媒体播放器AVPlayer设置播放策略时，新增支持起播缓冲水线（preferredBufferDurationForPlaying）的播放策略。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#setplaybackstrategy12)）
- 能力增强：支持应用创建多个SoundPool实例。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-f#mediacreatesoundpool10)）
- 新增屏幕录制时视频填充模式的枚举。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-e#avscreencapturefillmode18)）
- 音视频录制配置文件新增支持配置稳定录制模式enableStableQualityMode。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-i#avrecorderconfig9)）
- 播放器新增支持向媒体源申请媒体数据。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-mediasource#setmediaresourceloaderdelegate18)）
- 播放器新增支持动态开启视频超分算法。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#setsuperresolution18)）
- 调用媒体播放器AVPlayer设置播放策略时，新增支持智能追帧水线（thresholdForAutoQuickPlay）。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-i#playbackstrategy12)）

 
 

#### Media Library Kit

- 相册管理单选模式增强，新增支持多种相册内图片在单选时的呈现模式类型。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-e#singleselectionmode18)）

 
 

#### NearLink Kit

- 支持使用星闪传输数据。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-start-data-transfer)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-data-transfer-api)）
- 新增逻辑链路连接状态获取能力。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-remote-device#getacbstate)）
- 新增数传链路连接状态获取能力。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-data-transfer-api#getconnectionstate)）

 
 

#### Network Boost Kit

新增C API，提供网络加速能力以及网络感知、网络质量预测等能力。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/network-boost-kit-guide)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/networkboost-c)）
 
 

#### PDF Kit

- 新增支持获取透明背景的PDF页面pixelMap类型的图片。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pdf-arkts-pdfservice#getareapixelmapwithoptions)）
- 新增PdfAction及相关类，支持获取页面内链接和网址链接跳转信息。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pdf-arkts-pdfservice#pdfannotationinfo)）

 
 

#### Pen Kit

- 支持设置工具栏默认笔刷、笔刷类型及笔宽、各笔刷默认宽度。（API参考：[默认笔刷](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-handwritecomponent#handwritecomponent)、[笔刷类型及笔宽](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-handwritecomponent#penhspinfo)、[各笔刷默认宽度](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-handwritecomponent#handwritecomponent)）
- 新增支持全局取色实时显示RGB色值。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-imagefeaturepicker#pickforresult-1)）

 
 

#### Performance Analysis Kit

新增支持为当前线程转储虚拟机的原始堆快照。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hidebug#hidebugdumpjsrawheapdata18)）
 
 

#### Remote Communication Kit

MultipartForm新增boundary分隔符字段，支持开发者在上传多表单时通过自定义方式实现对表单数据的准确分隔与传输。([API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-rcp#multipartform))
 
 

#### Scan Kit

新增setAutoZoomEnabled接口，支持设置自动变焦。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scan-customscan-api#customscansetautozoomenabled)）
 
 

#### Scenario Fusion Kit

- 新增场景化Input组件，开发者可调用对应FunctionalInput组件快速拉起选择地区界面，供用户选择地区信息。([指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-input-zone-selectors)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scenario-fusion-functionalinput))
- 支持智能填充的推荐车牌号场景。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-licenseplateno)）
- 场景化API新增支持Wearable设备。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-api-information-attribute)）
- 支持智能填充的发票抬头推荐场景。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-introduction-to-smart-fill#发票抬头推荐场景)）

 
 

#### Share Kit

新增支持获取用户分享结果，可实现对用户内容分享渠道的统计。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-share-completed)）
 
 

#### Test Kit

- 新增支持按照模糊匹配/正则匹配方式查找符合条件的控件id、type的能力。（API参考：[id](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-uitest#id18)、[type](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-uitest#type18)）
- 新增支持获取控件提示文本（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-uitest#gethint18)），并根据控件提示文本查找控件（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-uitest#hint18)）。
- 新增支持横向滑动查找控件，仅适用于支持滑动的控件。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-uitest#scrollsearch18)）
- 新增支持模拟触摸板多指滑动手势操作，仅支持2in1设备。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-uitest#touchpadmultifingerswipe18)）
- 新增支持模拟手写笔的点击、长按、双击、滑动操作。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-uitest#penclick18)）

 
 

#### UI Design Kit

新增Hds导航组件HdsNavigation以及HdsNavDestination，继承ArkUI [Navigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-navigation)的页面跳转能力及基础样式，同时扩展支持：
 
- 标题栏随内容区滚动的动态模糊样式。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-navigation-dynamic-blur)）
- 菜单栏新增信息提醒能力。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-navigation-message-reminder)）

 
 

#### Vision Kit

新增支持在PC设备上对光标移入移出文本事件的监听。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vision-image-analyzer#ontype-cursormoveintext)）
 
 

#### Wear Engine Kit

新增支持Wearable设备。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/we-business_introduction#支持的设备)）
