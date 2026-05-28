# OS新增和增强特性

更新时间：2026-05-26 06:42:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/os-new-feature-611

#### 6.1.1(24) Release新增和增强特性

 

#### Ability Kit

AbilityStage组件管理器新增AbilityStage即将创建第一个Ability的回调（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilitystage#onabouttocreateability24)），以及当进程从应用快照启动时的回调（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilitystage#onlaunchfromhypersnap24)）。
 
 

#### ArkTS

- 新增enableLocalHandleDetection接口，保证EventHandler和libuv机制的任务在scope范围内执行，从而避免内存泄漏。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-util#enablelocalhandledetection24)）
- XML解析新增支持XmlSAXHandler，定义了SAX解析xml文本时的回调方法。开发者需要实现这些回调方法来处理xml文本的不同部分。这些回调方法会在xml解析过程的对应时机触发。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-xml#xmlsaxhandler24)）

 
 

#### ArkWeb

在下载任务完成的回调中，新增支持获取下载项的原始URL地址（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webdownloaditem#getoriginalurl24)）；新增支持获取引用页的URL地址（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webdownloaditem#getreferrerurl24)）。
 
 

#### Call Service Kit

在企业员工来电或去电时，开发者可通过来电、去电手机号查询获取对应的企业服务信息，帮助员工快速了解通话号码相关的企业服务数据，目前支持快递类型的企业服务。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/callservice-enterprise-sersvice-display)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/callservicekit-callerinfoquery-extension-ability#onquerybusinessservicedata)）
 
 

#### Camera Kit

新增一批拍照/录像模式下的相机专业能力，包括：
 
- 新增支持订阅（[ArkTS API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-flash#onflashstatechange24)、[C API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_registerflashstatechangecallback)）/取消订阅（[ArkTS API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-flash#offflashstatechange24)、[C API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_unregisterflashstatechangecallback)）闪光灯状态变化事件回调。
- 新增光学防抖（OIS）相关参数的查询和设置能力。包括查询和设置OIS模式、获取和设置各轴向偏移量信息。
ArkTS API参考[Interface (OIS)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-ois)和[Interface (OISQuery)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-oisquery)。
- C API参考可在[capture_session.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_setoismodecustom)页面搜索关键字“OIS”。

 - 相机设备定义中新增多个细节信息，包括镜头焦距、等效焦距、最小对焦距离、镜头畸变参数、内参标定参数、传感器的物理尺寸、传感器的像素阵列大小、传感器的滤色阵列排列方式。同时支持管理逻辑摄像头：
ArkTS API参考可在[CameraDevice参数定义](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-i#cameradevice)中搜索对应关键字。
- C API参考可在[capture_session.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_setoismodecustom)页面搜索对应关键字。

 - 相机设备定义中新增支持管理逻辑摄像头的能力：
ArkTS API参考见[CameraDevice参数定义](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-i#cameradevice)，支持通过isLogicalCamera参数查询是否为逻辑摄像头，并通过constituentCameraDevices参数定义组成此逻辑相机的物理相机列表。
- C API支持[查询是否为逻辑摄像头](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-device-h#oh_cameradevice_islogicalcamera)、[查询逻辑摄像头包含的所有物理摄像头](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-device-h#oh_cameradevice_getlogicalcameraconstituentcameradevices)、[删除组成逻辑摄像头的所有物理摄像头](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-device-h#oh_cameradevice_deleteconstituentcameradevices)。

 - 相机曝光设置增强：
ArkTS API新增自动曝光类，支持自动曝光操作（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-autoexposure)）；新增手动曝光设置（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-manualexposure)）和手动曝光对象的查询（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-manualexposurequery)）。
- C API新增支持曝光操作的原子能力，包括查询指定曝光测光模式是否支持（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_isexposuremeteringmodesupported)）、获取当前曝光测光模式（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_getexposuremeteringmode)）、设置曝光测光模式（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_setexposuremeteringmode)）、获取支持的曝光时间范围（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_getsupportedexposuredurationrange)）、设置曝光时间（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_setexposureduration)）、获取当前曝光时间（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_getexposureduration)）、捕获会话曝光时间变更回调（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_onexposuredurationchange)）、注册曝光信息变更事件回调（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_registerexposureinfochangecallback)）、注销曝光信息变更回调（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_unregisterexposureinfochangecallback)）。

 - 新增手动对焦相关能力：
ArkTS API新增手动对焦对象定义（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-manualfocus)）和手动对焦对象的查询能力（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-manualfocusquery)）。
- C API新增支持查询是否支持对焦距离设置（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_isfocusdistancesupported)）、获取当前对焦距离（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_getfocusdistance)）以及设置对焦距离（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_setfocusdistance)）。

 - 新增手动设置ISO感光度的相关能力：
ArkTS API新增手动ISO对象定义（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-manualiso)）和手动ISO对象的查询能力（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-manualisoquery)）。
- C API新增支持查询ISO感光度范围（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_getsupportedisorange)）、获取当前ISO感光度值（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_getiso)）以及设置ISO感光度值（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_setiso)）。

 - 新增手动设置物理光圈的相关能力：
ArkTS API新增物理光圈对象定义（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-aperture)）和物理光圈对象的查询能力（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-aperturequery)）。
- C API新增支持获取当前物理光圈值（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_getphysicalaperture)）、设置物理光圈值（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_setphysicalaperture)）、获取支持的物理光圈列表（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_getsupportedphysicalapertures)）以及删除支持的物理光圈列表（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_deletephysicalapertures)）。

 
 
 

#### CANN Kit

针对PC设备开放大语言模型推理API，新增支持接入大语言模型，实现计算链路的加速封装和计算加速。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-llm-summary)）
 
 

#### MDM Kit

设备设置管理支持对当前用户下被隐藏的设置项列表进行添加、删除、查询操作。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-devicesettings#devicesettingsaddhiddensettingsmenu24)）
 
 

#### 6.1.1(24) Beta1新增和增强特性

 

#### Ability Kit

- Ability上次退出的信息字段新增支持获取退出原因。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilityconstant#lastexitdetailinfo18)）
- AbilityStage上下文新增launchElement字段，用于在AbilityStage调用onCreate时告知应用正在加载的Ability，从而动态加载资源。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitystagecontext#属性)）

 
 

#### AppGallery Kit

新增支持查询、删除应用内快捷方式的能力，支持用户查看、管理应用的桌面快捷方式。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appgallery-productview-getshortcut)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/store-productviewmanager#productviewmanagergetpinshortcutinfos)）
 
 

#### ArkData

- 新增创建或打开已有的关系型数据库的同步方法。同步方法可阻塞线程直到获取到RdbStore。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-f#relationalstoregetrdbstoresync24)）

 
 

#### ArkGraphics 2D

- 新增支持为组件内容添加HDR（高动态范围成像）提亮效果。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-uieffect#hdrbrightnessratio24)）
- 新增支持视频的AIHDR格式。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hdrcapability#hdrformat)）

 
 

#### ArkTS

- 虚拟机维测能力增强：
新增支持获取所有虚拟机线程的堆内存信息，包括线程ID、线程名称、堆类型和堆对象大小。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-util#getallvmheapmemoryinfo24)）
- 新增堆内存超过预警阈值的回调函数，在虚拟机主线程完成垃圾回收后如果堆内存仍超过预警阈值则触发回调执行。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-util#onvmheapmemorypressure24)）

 - taskpool的execute方法增强，执行任务或任务组可以指定任务超时时长。如果任务或任务组的执行时间超过设置的超时时长，则抛出对应错误信息。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-taskpool#taskpoolexecute24)）

 
 

#### ArkUI

- 应用主动接入平行视界功能时，通过新API接口能够运行时获取当前平行视界的分栏状态，方便对业务逻辑&UX动效等进行调整。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)）
- 自定义组件支持跨Ability迁移。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-custom-components#自定义组件支持跨ability迁移)）
- 新增多个组件的C API：[OH_ArkUI_DecorationStyleOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkui-nativemodule-oh-arkui-decorationstyleoptions)、[OH_ArkUI_TextDataDetectorConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkui-nativemodule-oh-arkui-textdatadetectorconfig)、[OH_ArkUI_TextEditorSelectionMenuOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/tivemodule-oh-arkui-texteditorselectionmenuoptions)、[OH_ArkUI_TextEditorPlaceholderOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nativemodule-oh-arkui-texteditorplaceholderoptions)、[OH_ArkUI_TextEditorStyledStringController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vemodule-oh-arkui-texteditorstyledstringcontroller)、[OH_ArkUI_TextEditorParagraphStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/kui-nativemodule-oh-arkui-texteditorparagraphstyle)、[OH_ArkUI_ShadowOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-shadowoptions)、[OH_ArkUI_TextEditorTextStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pi-arkui-nativemodule-oh-arkui-texteditortextstyle)。
- 新增一批属性字符串的C API。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-styled-string-h#oh_arkui_styledstringkey)）
- 支持将含有竞争策略的事件分发到目标UI组件节点。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-buildernode#postinputeventwithstrategy24)）
- 新增支持获取UIContext对应页面的根节点。（[ArkTS API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getpagerootnode24)、[C API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h#oh_arkui_nativemodule_getpagerootnodehandlebycontext)）
- Text组件新增支持根据坐标获取最近的字符的位置信息。（[ArkTS API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common#getcharacterpositionatcoordinate24)、[C API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-styled-string-h#oh_arkui_textlayoutmanager_getcharacterpositionatcoordinate)）
- 新增拖拽异步通知接口，可以在拖拽的落入行为中指定采取剪切或者复制的处理方式（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drag-and-drop-h#oh_arkui_notifysuggesteddropoperation)），以及指定是否执行拖拽落入行为的动效（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drag-and-drop-h#oh_arkui_notifydisabledefaultdropanimation)）。
- 新增onNeedSoftkeyboard回调，支持开发者配置焦点转移后不关闭拉起的软键盘。（[ArkTS API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-onneedsoftkeyboard)、[C API参考-NODE_ON_NEED_SOFTKEYBOARD](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h#arkui_nodeeventtype)）
- CanvasRenderingContext2D（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-canvasrenderingcontext2d#antialias24)）和OffscreenCanvasRenderingContext2D（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-offscreencanvasrenderingcontext2d#antialias24)）新增antialias属性，支持关闭文本抗锯齿功能。
- 分段按钮新增enableStateAnimation配置项，用于指定selectedIndexes在绑定的状态变量发生变化时是否执行系统动画。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-segmentbutton#segmentbutton-1)）
- Tabs组件新增支持嵌套滚动能力。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#nestedscroll24)）
- JS组件新增支持旋转表冠事件监听接口。（[API参考-ArkUI.Full](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-monitorcrownevents)、[API参考-ArkUI.Lite](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-common-monitorcrownevents)）
- 多行文本的缩略模式新增支持设置为省略行首内容（MULTILINE_START）或省略行中内容（MULTILINE_CENTER）。（[ArkTS API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#ellipsismode11)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_ellipsismode)）
- 新增动态布局容器组件，支持在运行时动态切换不同的布局算法，不改变子组件的状态。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-dynamiclayout)）
- 窗口管理新增支持按需销毁窗口（WindowStage）的页面内容（UIContent）。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-windowstage#releaseuicontent24)）

 
 

#### ArkWeb

- ArkWeb网页请求支持User-Agent Client Hints功能。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#setuseragentclienthintsenabled24)）
- ArkWeb新增默认右键菜单启用开关，可通过该接口控制默认的右键菜单是否开启。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-attributes#enabledefaultcontextmenu24)）
- 设置Web页的URL白名单，只有白名单内的URL才能允许加载/跳转，否则将拦截并弹出告警页。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#seturltrustlist24)）

 
 

#### Audio Kit

- 音频采集和音频渲染新增支持设置独立的音频会话策略和行为参数。（[API参考-音频采集](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiocapturer#setindependentaudiosessionstrategy24)、[API参考-音频渲染](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiorenderer#setindependentaudiosessionstrategy24)）
- 新增OH_MIDI的C API，支持应用通过USB或蓝牙BLE连接外接MIDI设备（如MIDI键盘、电子琴、MIDI控制器等），实现MIDI消息的收发、设备枚举与热插拔监听，可用于音乐创作、乐器录制与教学、MIDI设备控制等场景。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/midi-overview)）

 
 

#### AVCodec Kit

- 新增支持Cinepak媒体格式的编解码能力。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/avcodec-support-formats#媒体编解码)）
- 新增支持筛选特定MIME类型的安全解码器，在处理受数字版权管理保护的DRM媒体资源时，可以使用支持安全链路的"安全解码器"。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/obtain-supported-codecs#筛选特定mime类型的安全解码器drm播放场景)）

 
 

#### AVSession Kit

新增支持后台播放模式的设置，可由应用告知系统是否支持后台播放，系统根据能力决策实况胶囊的显示。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-avsession#setbackgroundplaymode24)）
 
 

#### Camera Kit

新增支持创建延迟预览输出对象，在配流时替代普通的预览输出对象加入数据流（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-cameramanager#createdeferredpreviewoutput24)）。同时支持配置延迟预览的Surface（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-previewoutput#adddeferredsurface24)）。
 
 

#### Connectivity Kit

- 新增支持通过C API获取Wi-Fi连接信息。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-wifi-h#oh_wifi_getlinkedinfo)）
- 新增A2DP的播放状态广播以及SCO广播事件。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/commoneventmanager-definitions#common_event_bluetooth_a2dpsource_play_state_change24)）

 
 

#### Content Embed Kit

【新增Kit】Content Embed Kit（内容嵌入服务）提供应用间文档互相嵌入与协同编辑的框架能力，并为开发者封装了客户端与服务端的开发接口，便于快速实现文档跨应用嵌入与协作。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/content-embed-kit-overview)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed)）
 
 

#### Desktop Extension Kit

- 新增支持更新单个一级菜单项内容。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/statusbar-extension-manager#statusbarmanagerupdatestatusbarmenuitem)）
- 新增支持更新单个二级菜单项内容。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/statusbar-extension-manager#statusbarmanagerupdatestatusbarsubmenuitem)）
- 新增支持配置菜单项的默认显示图标、及选中时显示的图标。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/statusbar-extension-manager#statusbarmenuitemoptions)）

 
 

#### Device Security Kit

- 新增代码签名信息查询功能，开发者可获取设备上已签名的文件签名信息。（[指南-ArkTS](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-audit-acquirecodesign-arkts)、[API参考-ArkTS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-securityaudit-api#acquirecodesign)、[指南-C/C++](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-audit-acquirecodesign-c)、[API参考-C/C++](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-securityaudit#hms_securityaudit_acquirecodesign)）
- 数字盾服务新增支持Tablet、PC/2in1设备。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-introduction#支持的设备)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-trusted-auth-api)）
- 新增系统安全专项相关事件：进程提权事件、进程异常调试事件、系统目录异常挂载事件、进程异常崩溃事件、应用代码未签名事件、应用代码验签异常事件、驱动代码验签异常事件、驱动非法映射内核内存事件、内核内存异常使用事件。（[指南-ArkTS](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-audit-subscribe-arkts-filterevent)、[API参考-ArkTS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-securityaudit-api#notifyevent)、[指南-C/C++](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-audit-subscribe-c-filterevent)、[API参考-C/C++](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-securityaudit#securityaudit_notify_event)）

 
 

#### Enterprise Data Guard

- 新增放通应用列表管理功能，开发者可设定特定应用不受KIA策略管控。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-unrestricted-app-list)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataguard-fileguard#addunrestrictedapplicationlist)）
- 新增设置上位机和下位机之间的HDC鉴权密钥。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-set-hdc-authentication-key)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataguard-fileguard#sethdcauthenticationkey)）
- 新增订阅或取消订阅打印服务启动事件。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-print-startup-event)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataguard-fileguard#onprintstartup)）
- 新增弹框验证锁屏密码用于获取重置锁屏密码的恢复密钥。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/recoverykey-getkeyforresetpin)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataguard-recoverykey#verifyuserbydialog)）

 
 

#### Enterprise Threat Protection Kit

【新增Kit】Enterprise Threat Protection Kit（企业威胁防护服务）提供了构建安全防护应用的核心能力，专注于文件访问与处置。应用可对文件进行扫描以识别潜在威胁，并对威胁文件执行隔离、恢复或删除操作，从而有效保护企业设备的数据安全。详细信息请参见[Enterprise Threat Protection Kit开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprise-threat-protection-kit-guide)。
 
 

#### FAST Kit

- 新增并发哈希表。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fast-concurrent-hashmap)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-ads-concurrent-hashmap-8h)）
- 新增部分向量运算和复数处理功能。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fast-dsp-vector-calculation)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-dsp-common-8h)）
- 新增二阶IIR滤波器功能。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fast-dsp-iir-filter)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-dsp-common-8h)）

 
 

#### Form Kit

在onUpdateForm回调中新增支持卡片更新原因字段。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-form-forminfo#formupdatereason24)）
 
 

#### Image Kit

新增WebP图像元数据类，用于存储图像的元数据。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-webpmetadata)）
 
 

#### Input Kit

C API输入事件增强，提供输入事件的压力、相对窗口左上角的XY相对坐标等事件。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-input-manager-h#oh_input_settoucheventpressure)）
 
 

#### Live View Kit

- 新增支持点击实况窗卡片辅助区结束实况窗。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/liveview-liveviewmanager#actiontype)）
- 新增实况窗最长存活时间参数配置，系统将在达到预设时间后自动结束实况窗。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/liveview-liveviewmanager#primarydata)）

 
 

#### Map Kit

- 关键字搜索场景下，查询结果新增支持展示相关性分数。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-site#site)）
- 在区划查询场景下，新增支持选择区划层级范围。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-location-division#开发步骤)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-scenemap#districtselectoptions)）
- 新增支持设置Marker注释背景颜色。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#markeroptions)）
- 瓦片图层场景下，新增支持高层级复用低层级瓦片。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-tile#支持高层级复用低层级瓦片)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#tileoverlayoptions)）
- 新增支持拉起地图App离线地图管理页面和地点详情。（[指南-离线地图管理页面](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-petalmaps#打开地图应用离线地图管理页面)、[API参考-离线地图管理页面](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-petal-maps#openmapofflinedatamanagement)、[指南-地点详情](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-petalmaps#打开地图应用查看地点详情)、[API参考-地点详情](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-petal-maps#poidetailparams)）
- 新增Marker长按事件监听能力。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-marker#设置监听标记长按事件)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mapeventmanager#onmarkerlongclick)）
- 新增POI长按事件监听能力。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mapeventmanager#onpoilongclick)）

 
 

#### NearLink Kit

新增获取星闪合作设备集合管理信息的能力。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-cdsm-information)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-cdsm)）
 
 

#### MDM Kit

- kiosk模式下，新增支持通过上划停留手势进入最近任务栏（ALLOW_GESTURE_CONTROL）以及通过边缘内划停留手势进入侧边DOCK栏（ALLOW_SIDE_DOCK）。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-applicationmanager#kioskfeature20)）
- 新增支持安装和卸载企业重签名证书的能力。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-securitymanager#securitymanagerinstallenterpriseresignaturecertificate24)）
- 新增支持根据位置索引添加应用到PC/2in1设备的底部快捷栏的能力。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-applicationmanager#applicationmanageradddockapp24)）

 
 

#### Media Kit

- C API新增隐私保护设置的回调函数，用于响应截屏录屏时捕获的隐私保护事件。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-h#oh_avscreencapture_setprivacyprotectcallback)）
- C API新增支持获取多屏幕录制能力信息（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-h#oh_avscreencapture_getmultidisplaycapturecapability)），以及通过DisplayID选择多屏幕进行录制（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-h#oh_avscreencapture_getmultidisplayidsselected)）。

 
 

#### Network Boost Kit

新增支持设置数据传输低功耗模式。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/networkboost-netboost#netboostsetlowpowermode)）
 
 

#### Network Kit

TLS支持证书链的验证，可通过传入数组的方式最多支持到1000个证书。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-socket#tlssecureoptions9)）
 
 

#### Notification Kit

- 新增支持查询本APP通知中wantAgent字段的部分信息。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationmanager#notificationmanagergetnotificationparameters24)）
- 新增支持使用应用沙箱内的文件作为通知的自定义铃声。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/notification-customized-ringtone)）

 
 

#### Payment Kit

人脸核身能力新增支持PC设备。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-introduction)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-realnameservice)）
 
 

#### Performance Analysis Kit

- 当应用发生SIGPIPE异常退出时，在Debug版本应用可开启SIGPIPE信号打印调用栈功能辅助定位问题。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cppcrash-guidelines#应用发生sigpipe异常退出)）
- hiprofiler新增文件缓存模式（use_file_cache_mode），通过将缓存数据落盘，提升内存分配信息的采集性能。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiprofiler#native-hook插件)）
- HiDebug新增资源采集功能，支持按需采集应用进程资源分配栈至沙箱，覆盖文件描述符、线程、Native/GPU内存及全局句柄等类别，辅助定位资源泄漏。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hidebug-guidelines)）
- HiDebug新增支持获取应用程序进程的物理内存使用信息。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hidebug#hidebuggetrssinfo24)）
- HiDebug新增支持将转储的堆快照由线程级改为进程级。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hidebug#hidebugsetprocdumpinsharedoom24)）
- HiDebug新增提供包括内核信息在内的Trace采集请求接口。（[ArkTS API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hidebug#hidebugrequesttrace24)、[C API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-h#oh_hidebug_requesttrace)）
- HiAppEvent新增多个参数，用于自定义APP_CRASH事件中的CPP_CRASH类型的日志规格，包括打印PC、LR寄存器扩展字节范围的内存内容（[OH_APP_CRASH_PARAM_EXTEND_PC_LR_PRINTING](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-param-h#oh_app_crash_param_extend_pc_lr_printing)）、按设置的参数值大小截断（[OH_APP_CRASH_PARAM_LOG_FILE_CUTOFF_SZ_BYTES](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-param-h#oh_app_crash_param_log_file_cutoff_sz_bytes)）、只打印崩溃日志中出现的地址所属的VMA映射信息（[OH_APP_CRASH_PARAM_SIMPLIFY_VMA_PRINTING](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-param-h#oh_app_crash_param_simplify_vma_printing)）、在CPP_CRASH场景拼接应用沙箱中指定文件的日志（[OH_APP_CRASH_PARAM_MERGE_CPPCRASH_APP_LOG](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-param-h#oh_app_crash_param_merge_cppcrash_app_log)）。

 
 

#### Remote Communication Kit

- 新增支持发起仅建立连接的请求。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/remote-communication-pre-connect)、[API参考-ArkTS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-rcp#request)、[API参考-C/C++](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#hms_rcp_setrequestconnectonly)）
- 新增支持C API获取默认session。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#hms_rcp_getdefaultsession)）
- 新增支持配置蜂窝网络失败时是否抛出错误。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-rcp#transferconfiguration)）

 
 

#### Screen Time Guard Kit

新增支持请求用户授权的同时配置管控应用在管控生效过程中是否可卸载。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-request-user-auth)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/screentimeguard-guardservice#requestuserauth-1)）
 
 

#### Speech Kit

- AI字幕初始化场景下，新增支持设置源语言、目标语言以及对应语言下字体颜色和字体大小。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/speech-aicaptioncomponent#aicaptionoptions)）
- 朗读控件新增TextReaderIconV2图标接口，支持对ArkTS的状态管理V2装饰器的适配。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/speech-textreadericonv2)）

 
 

#### UI Design Kit

底部页签新增支持页签栏和迷你栏垂直布局样式。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdstabs#hdsbarlayoutmode)）
 
 

#### Vision Kit

卡证识别场景下，新增支持识别港澳居民来往内地通行证、台湾居民来往大陆通行证。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vision-card-recognition#cardtype)）
 
 

#### 标准库

新增Seccomp开放系统调用列表。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/seccomp-symbol)）
