# OS新增和增强特性

更新时间：2026-05-18 09:49:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/os-new-feature-602

#### 6.0.2(22) Release

6.0.2(22) Release在Beta1版本基础上未引入新增特性。
 
 

#### 6.0.2(22) Beta1关键特性

 

#### Ability Kit

- 新增C API支持获取本应用的应用级的日志文件目录。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-application-context-h#oh_abilityruntime_applicationcontextgetlogfiledir)）
- UIAbilityContext新增支持在当前进程中启动应用程序自己的UIAbility。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#startselfuiabilityincurrentprocess22)）
- UIAbilityContext新增支持重启应用的接口，处于获焦状态的UIAbility可以通过该接口重启当前UIAbility所在的进程，并拉起应用内的指定UIAbility。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#restartapp22)）
- 新增支持获取应用启动时预加载阶段的能力。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-application#applicationgetapppreloadtype22)）
- 新增支持根据传入的pid终止当前进程创建的Native子进程或ArkTS子进程。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/capi-nativechildprocess-development-guideline#终止子进程)）

 
 

#### AppGallery Kit

- 应用市场推荐服务新增支持TV设备。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appgallery-productview-loadproduct#约束与限制)）
- 应用归因服务，登记归因转化接口新增属性timestamp、serviceTag，支持设置转化事件时间及开发者关注的业务信息功能。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/store-attributionmanager#adtriggerinfo)）

 
 

#### ArkData

UDMF新增iWork文件格式的标准数据类型定义。详见[UTD预置列表的基础类型](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uniform-data-type-list#基础类型)。
 
 

#### AR Engine

新增获取拍照流图片接口，支持配置高清图像。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#arengine_arimagestreammode)）
 
 

#### ArkTS

- 新增支持在Sendable class上叠加使用除@Sendable装饰器之外的其他自定义装饰器。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sendable-constraints#支持在sendable-class上叠加自定义装饰器)）
- Util新增接口类AutoFinalizer，用于在ArkTS对象释放时提供回调。通过实现回调接口，开发者可自定义对象被回收时自动触发的资源清理逻辑。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-util#autofinalizert22)）
- 新增支持通过taskId或taskId与taskName获取对应的Task实例。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-taskpool#taskpoolgettask22)）

 
 

#### ArkUI

- 新增Picker容器组件，支持开发者自定义构造Picker选择器。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-ui-picker-component)）
- 滚动组件相关能力增强：
TextArea控件新增C API支持配置滚动条是否显示。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_barstate)）
- 滚动组件新增支持获取内容总大小的能力。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#contentsize22)）
- 滚动组件通用接口支持设置滚动内容区域偏移量，实现内容滚动到边缘时有留白、未滚动到边缘时有内容的效果。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scrollable-common#contentstartoffset22)）
- Grid组件支持通过C API设置布局选项（例如大小规则的GridItem在Grid中占的行数和列数）（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#oh_arkui_gridlayoutoptions_create)），滚动通用属性和事件（例如，设置滚动条宽度，在[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h#arkui_nodeattributetype)Attribute表中搜索“Grid从API version 22开始支持”）
- scrollBarColor的入参支持Resource类型，覆盖滚动组件通用接口（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scrollable-common#scrollbarcolor22)）、Scroll组件（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scrollbarcolor22)）、Grid组件（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid#scrollbarcolor22)）。
- 新增组件可见区域变化事件的回调。（[API参考-ArkTS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-component-visible-area-change-event#onvisibleareachange22)、[API参考-C API](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#oh_arkui_visibleareaeventoptions_setmeasurefromviewport)）

 - 新增C API支持停止指定的Swiper节点正在执行的翻页动画。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h#oh_arkui_swiper_finishanimation)）
- Tabs组件新增回调，支持监听Tabs组件初始化时显示首个页签的事件。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uiobserver#ontabchange22)）
- Navigation新增回调，支持监听Navigation页面在跳转前的拦截事件。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#interceptioncallback22)）
- Tabs组件新增支持自定义indicator，支持图片格式的下划线风格。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabcontent#indicator22)）
- UIContext新增支持获取后端实例的唯一标识ID。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getid22)）
- UIContext新增静态方法，提供静态获取UIContext的能力。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#通过静态方法获取uicontext对象)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-resolveduicontext)）
- 新增ReactiveBuilderNode，支持通过无状态的UI方法@Builder生成组件树，并持有该组件树的根节点。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-buildernode#reactivebuildernode22)）
- 新增一套自定义组件生命周期的机制，可使组件生命周期回调函数受状态机限制，保证生命周期回调函数调用时机符合预期。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-custom-components-new-lifecycle)）
- 窗口新增支持获取当前应用窗口的避让区域，即使避让区域当前处于不可见状态。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#getwindowavoidareaignoringvisibility22)）
- 窗口新增支持以vp单位获取当前应用窗口的尺寸限制。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#getwindowlimitsvp22)）
- 窗口扩展了maximize接口能力，新增参数acrossDisplay控制折叠屏悬停态下主窗口在最大化时的瀑布流模式行为。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#maximize22)）

 
 

#### ArkWeb

- 将分词高亮与文本选择后弹出AI菜单的功能进行解耦，允许开发者单独进行功能配置。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-data-detector#文本选择菜单扩展)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-attributes#enableselecteddatadetector22)）
- 新增支持监听Web页面白屏事件，并提供事件的回调。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#ondetectedblankscreen22)）
- 新增属性emulateTouchFromMouseEvent，支持Web组件设置mouse事件转touch事件。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-i#weboptions)）
- 新增支持设置软键盘自动控制模式，用于控制Web组件在失去焦点或获得焦点、状态切换为inactive或active时是否尝试触发软键盘自动隐藏或拉起。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#setsoftkeyboardbehaviormode22)）
- 新增支持通过ContextMenuDataMediaType获取触发onContextMenuShow的Web元素类型，类型包含NONE、IMAGE 、VIDEO 、AUDIO 、CANVAS。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webcontextmenuparam#getcontextmenumediatype22)）
- 新增支持快速返回Web页面顶部的能力。当网页处于非顶部状态或向下抛滑时，此时若需返回网页顶部，可以使用backToTop方法，开启后通过点击状态栏，打断抛滑并将网页滚动到网页顶部。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-attributes#backtotop22)）
- 新增设置属性，支持设置是否通过组合按键（Ctrl+'-/+'或Ctrl+鼠标滚轮/触摸板）进行缩放。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-attributes#zoomcontrolaccess22)）
- OnRefreshAccessedHistoryEvent新增可选参数isMainFrame，用于标记是否为主文档触发。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-i#onrefreshaccessedhistoryevent12)）
- 新增支持在使用CookieManager的场景下，延后初始化ArkWeb内核的能力。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-cookie-and-data-storage-mgmt#cookie管理)、[ArkTS API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webcookiemanager#setlazyinitializewebengine22)、[C API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-arkweb-h#oh_nativearkweb_lazyinitializewebengineincookiemanager)）

 
 

#### AVSession Kit

新增支持返回当前进程已创建过的会话对象。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-f#avsessiongetavsession22)）
 
 

#### Basic Services Kit

新增API注解能力，可用于标记API支持的最低可用版本。在源码定义处添加注解后，编译工具会在使用处检查潜在的兼容性问题。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-annotation#available)）
 
 

#### Call Service Kit

- 新增允许运营商通话中发起VoIP主叫。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/call-voipcall#voipcallattribute)）
- 新增用户按键静音VoIP来电铃声。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/call-voipcall#voipcallattribute)）

 
 

#### Connectivity Kit

- 蓝牙新增支持查询指定套接字链路下的最大接收数据大小（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-socket#socketgetmaxreceivedatasize22)）和最大发送数据大小（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-socket#socketgetmaxtransmitdatasize22)）。
- 蓝牙新增支持查询指定套接字链路下的连接状态。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-socket#socketisconnected22)）
- 蓝牙新增支持获取指定server端服务的能力。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#getservice22)）
- 蓝牙新增支持将16位、32位UUID转128位UUID的能力。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-access#accessconvertuuid22)）
- NFC新增支持应用声明off_host_apdu能力，将应用添加到默认付款应用列表中。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nfc-hce-guide#offhost应用刷卡)）

 
 

#### Crypto Architecture Kit

- 新增支持ChaCha20算法的加解密。（[指南-ArkTS](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-chacha20-encrypt-decrypt)，[指南-C/C++](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-chacha20-encrypt-decrypt-ndk)）
- 新增支持ChaCha20-Poly1305算法的加解密。（[指南-ArkTS](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-chacha20-encrypt-decrypt-poly1305)，[指南-C/C++](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-chacha20-encrypt-decrypt-poly1305-ndk)）

 
 

#### DeskTop Extension Kit

- 新增支持更新状态栏图标hover的信息。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/statusbar-extension-manager#statusbarmanagerupdatestatusbarhovertips)）
- 新增应用接入快捷栏服务，可自定义快捷栏图标的右键菜单。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/desktop-quickbar-extension-guide)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/desktop-quickbar-extension-manager)）

 
 

#### Device Security Kit

- 新增支持模拟点击增强检测。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-detectsimulatedclickriskenhanced)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-brid-api#detectsimulatedclickriskenhanced)）
- 新增支持查询和监听设备的超级隐私模式状态。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-superprivacymode)）

 
 

#### Enterprise Space Kit

空间管理场景下，新增支持设置工作空间策略、查询工作空间策略、设置深度冻结豁免名单、查询深度冻结豁免名单功能。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-spacemanager-guide)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/enterprisespace-spacemanager)）
 
 

#### FAST Kit

【新增Kit】FAST Kit（算法加速服务）提供高性能算法和数据结构等加速服务，用于提升开发者的开发效率和用户的应用使用体验。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fast-introduction)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast)）
 
 

#### Game Service Kit

- 新增支持在游戏账号登录面板上置顶游戏官方账号。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-gameplayer-network)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/gameservice-gameplayer)）
- 游戏场景感知，新增C API，支持返回CPU性能信息及建议工作电流等信息。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-gameperformance-access-procedure-c)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/gameservice-game-performance)）

 
 

#### IME Kit

新增输入法扩展信息模块，提供对输入法扩展信息的管理，支持ArkUI编辑框在拉起输入法时传递扩展信息给输入法应用。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod-extraconfig)）
 
 

#### Input Kit

新增支持注入修饰键后查询到修饰键状态。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-input-manager-h#oh_input_injectkeyevent)）
 
 

#### Live View Kit

实况窗支持显示本地天气效果，典型场景包括即时配送、出行打车等。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/liveview-liveviewmanager#weatherlocationtype)）
 
 

#### Localization Kit

新增国际化能力的C API能力。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n)）
 
 

#### Map Kit

- Marker的icon新增支持设置x、y偏移量。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-marker#setoffset)）
- 自定义矢量瓦片图层新增支持模糊效果。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mvtoverlay#setblur)）
- 地图Picker新增支持配置转场动效时间。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-scenemap#locationqueryoptions)）

 
 

#### MDM Kit

- 新增支持设置应用不可关停策略。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-applicationmanager#applicationmanageraddusernonstopapps22)）
- 新增支持应用后台防冻结策略。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-applicationmanager#applicationmanageraddfreezeexemptedapps22)）
- 网络防火墙接口新增支持IPv6。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-networkmanager#networkmanageraddfirewallrule)）

 
 

#### NDK开发

- 新增支持使用扩展的Node-API接口创建对ArkTS对象的强引用。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-strong-reference)）
- 新增支持使用扩展的Node-API接口创建和销毁临界区作用域及访问字符串内容。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-critical)）

 
 

#### Network Kit

- 新增支持保护应用进程不受VPN连接影响的能力。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-vpnextension#protectprocessnet22)）
- 新增支持获取本地设备IP邻居表条目信息，包括IPv4和IPv6，每个条目信息包括IP地址、MAC地址、网卡名。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection#connectiongetipneightable22)）
- TLS新增支持设置timeout字段，TLSSocket会在timeout后断开连接。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-socket#tlsconnectoptions9)）
- 新增支持在VPN首次启动时传递want中的parameters字段。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-vpnextension#vpnextensionstartvpnextensionability)）
- 新增网络策略的接口，在需要设置当前应用能否使用Wi-Fi/蜂窝联网时，可调用该接口打开当前应用的联网设置界面，以设置应用的联网权限。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-policy#policyshowappnetpolicysettings22)）

 
 

#### Network Boost Kit

新增C API，支持连接迁移（多网并发），包括业务场景设置、多网状态监听、多网建议监听、多网配额查询、多网发起和释放。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-netmultipath-setscenedesc-c)）
 
 

#### Notification Kit

- 新增支持三方应用获取本机通知，用于协同至三方穿戴设备等场景。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/notification-subscriber-extension-ability)，[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationsubscriberextensionability)）
- 新增支持查询应用自身的通知角标数量。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationmanager#notificationmanagergetbadgenumber22)）

 
 

#### PDF Kit

新增PDFView组件嵌套滚动能力。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pdf-arkts-pdfviewmanage#pdfnestedscrollmode)）
 
 

#### Performance Analysis Kit

- AppFreeze采样栈新增支持对libuv异步栈的跟踪。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appfreeze-guidelines#增强日志规格)）
- HiAppEvent新增支持主线程超时事件配置策略，支持主线程超时结束自动停止采样栈的功能。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-mainthreadjank-events#自定义参数)，[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-hiappevent#eventpolicy22)）
- HiDebug新增接口支持对指定的数个线程进行Perf采样，并在调用结束后返回采样栈内容。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-h#oh_hidebug_requestthreadlitesampling)）
- JS Crash增加混合栈字段（HybridStack），支持打印CPP和JS之间跨语言的代码调用栈。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/jscrash-guidelines#hybridstack格式)）

 
 

#### Scan Kit

- 默认界面扫码能力、自定义界面扫码能力和图像识码能力支持获取码图是否携带GS1（Global Standards 1）数据。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scan-scanbarcode-api#scanresult)）
- 默认界面扫码能力支持获取扫码结果来源。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scan-scanbarcode-api#scanresult)）

 
 

#### Scenario Fusion Kit

获取手机号和风险等级Button。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-button-get-risklevel)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scenario-fusion-functionalbuttoncomponentmanager#ongetphonenumberandrisklevel)）
 
 

#### Screen Time Guard Kit

- 新增支持拉起许可应用跳转页的能力，以便快速跳转到指定应用。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-start-app-form)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/screentimeguard-app-picker#startappform)）
- 新增共享时长的时间管控策略类型，即策略关联的所有应用共享同一可用时长配额。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/screentimeguard-guardservice#timestrategytype)）

 
 

#### Share Kit

碰一碰分享新增支持当前界面无可分享内容时，引导用户前往可分享场景的能力。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/knock-share-between-phones-content#当前界面无可分享内容)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/share-harmony-share#clarifynonshare)）
 
 

#### Test Kit

- 单元测试框架新增接口beforeEachIt和afterEachIt，用于支持嵌套场景下生命周期函数的执行。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/unittest-guidelines#基础流程能力)）
- UITest新增支持窗口变化和组件操作事件监听能力。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-uitest#oncewindowchange22)）
- UITest新增支持指关节操作模拟能力。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-uitest#knuckleknock22)）
- UITest新增支持在模拟操作的同时查找目标控件是否存在。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-uitest#iscomponentpresentwhenlongclick22)）
- UITest新增支持触摸板双指滚动操作模拟能力 。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-uitest#touchpadtwofingersscroll22)）

 
 

#### UI Design Kit

HdsVisualComponent组件新增支持卡片能力。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hds-visual-component)）
 
 

#### 标准库

ICU4C新增支持ICU版本、名称本地化、码点处理及CLDR版本。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/icu4c)）
 
 

#### 调试命令

- uinput命令支持控制注入的修饰键状态。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uinput#控制注入的修饰键状态)）
- bm工具安装命令的-p参数支持指定待安装的APP路径。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/bm-tool#安装命令install)）
