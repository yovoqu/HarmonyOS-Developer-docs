# OS新增和增强特性

更新时间：2026-07-29 02:36:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/os-new-feature-2600

#### 26.0.0 Beta2新增和增强特性



#### Ability Kit

 - 新增基于ModularObjectExtensionAbility的模块化对象，支持应用将自身功能以模块化对象的形式开放给其他应用调用。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/modular-object-extension-overview)）       
提供基于C API的使用ModularObjectExtensionAbility实现模块化对象的指导。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/modular-object-extension-development)）
 - 支持使用Taihe实现ModularObjectExtensionAbility的IPC通信。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/modular-object-extension-ability-taihe)）
 - 提供声明ModularObject分发器的C API，提供基于类型库元数据的跨进程延迟绑定调用能力。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-modular-object-dispatcher-h)）
 - 提供声明ModularObjectExtensionAbility实例的C API，包括注册生命周期回调函数和获取上下文等能力。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-modular-object-extension-ability-h)）
 - 提供声明ModularObjectExtensionAbility上下文的C API，包括启动UIAbility、销毁ModularObjectExtensionAbility自身、创建和销毁IPC对象等功能。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-modular-object-extension-context-h)）
 - 提供声明用于管理ModularObjectExtensionAbility的C API，包括查询ModularObjectExtensionAbility信息、连接与断开连接等能力。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-modular-object-extension-manager-h)）

      - 新增提供NativeAbility数据信息的相关C API，用于获取Ability实例ID、Ability名称和napi_env等信息。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-ability-wrapper-h)）
 - 新增声明ExtensionAbility的连接选项的C API，提供包括连接成功、断开连接和连接失败的回调接口。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-connect-options-h)）
 - 新增自动填充请求信息的定义能力，应用可定义自动填充的信息类型。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-autofillrequest)）
 - 包管理新增pluginBundleManager模块，提供应用对自分发插件的管理能力，包括安装、卸载本地插件。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-pluginbundlemanager)）




#### Account Kit

新增支持华为账号亲密圈服务，实现用户添加和选择亲友的能力。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-intimate#模块概述)）



#### Agent Framework Kit

新增支持通过AgentAbilityExtension实现智能体间A2A协议通信。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hmaf-a2a-dev-guide)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/hmaf-a2a-protocol)）



#### AOD Navigation Kit

【新增Kit】AOD Navigation Kit（熄屏导航服务）提供了应用接入熄屏导航的能力，在保障导航实时性的同时有效控制设备功耗，支持轨迹、里程等关键导航信息在设备熄屏界面无需解锁即可便捷查看。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/aodnavigation-introduction)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/aodnavigation-aodnavimanager)）



#### AppGallery Kit

 - 新增支持暂停下载任务。（[指南-ArkTS](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-moduleinstall_arkts#暂停下载任务)、[ArkTS API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/store-moduleinstallmanager#moduleinstallmanagerpausetask)、[指南-C](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-moduleinstall_c#暂停下载任务)、[C API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/store-c-moduleinstall#hms_moduleinstall_pausetask)）
 - 新增支持Car设备，涉及的能力包括：应用归因服务、隐私管理服务、图标管理服务、应用市场推荐、产品特性按需分发、生态查询、应用市场更新。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-introduction#支持的设备)）




#### ArkData

数据共享能力新增支持发布多个值类型的配置用于多应用共享。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-datashare#publish20)）



#### ArkGraphics 2D

绘制模块字体绘制能力新增支持获取文字的轮廓路径，同时支持字体回退能力。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-font#gettextpathwithfallback)）



#### ArkUI

 - 新增多个基于状态管理（V2）实现的组件，包括[ChipV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-chipv2)、[ChipGroupV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-chipgroupv2)、[CounterV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-counterv2)、[PopupV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-popupv2)、[SwipeRefresherV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-swiperefresherv2)、[TreeViewV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-treeviewv2)、[CounterV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-counterv2)。
 - 新增智慧手势的能力（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-events-smartgesture-event)）：       
新增智慧手势的API，提供智慧手势使能、监听、选中态控制，以及动态决策智慧手势行为的能力。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-smartgesturecontroller)）
 - 交互属性新增对智慧手势的响应。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-smart-gesture-shortcut)）

      - 滚动与滑动组件新增懒加载瀑布流布局组件[LazyVWaterFlowLayout](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-lazyvwaterflowlayout)、懒加载垂直线性布局组件[LazyColumnLayout](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-lazycolumnlayout)、懒加载动态布局容器组件[LazyDynamicLayout](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-lazydynamiclayout)。
 - 响应式环境变量组件新增环境变量容器[WithEnv](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-with-env)、自定义环境变量[@CustomEnv](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-env-property)。
 - 新增DatePickerComponent组件，用于选择日期（年月日）和时间（时分秒）。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-datepickercomponent)）
 - 新增SelectionContainer组件，用于为多个文本节点提供跨节点文本选中、复制及菜单扩展能力。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-selectioncontainer)）
 - 新增支持设置调测标签，帮助开发者分辨同类节点，提高开发和分析调试的效率。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-inspector-label)）
 - ChipGroup组件新增支持通过backgroundSystemMaterial和activatedBackgroundSystemMaterial配置正常状态和激活状态下的系统材质背景。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-chipgroup#示例6设置系统材质样式)）
 - SelectionMenu组件新增支持通过backgroundSystemMaterial配置菜单的背景板的系统材质。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-selectionmenu#示例3设置背景板材质)）
 - Navigation组件新增配置项systemMaterial属性，支持系统材质效果。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#示例20设置systemmaterial开启标题栏材质效果)）
 - 弹窗类组件DatePickerDialog新增配置项systemMaterial，支持系统材质效果。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-datepicker-dialog#datepickerdialogoptions对象说明)）
 - C API新增沉浸式材质类型和API声明。（[C API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-material-h)）
 - 组件动态属性新增悬浮状态样式。（[ArkTS API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#applyhoveredattribute)、[C API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-common-attributes-h#arkui_uistate)）
 - UIContext的OverlayManager新增按层级配置浮层的能力。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-overlaymanager#openorderoverlay)）
 - 文本类组件新增支持尾部缩进属性（tailIndents），包括：Text组件（[ArkTS API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#tailindents)、[C API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h-nodeattributetype-text#node_text_tail_indents)）、属性字符串（[ArkTS API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string#属性-9)、[C API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-styled-string-h#oh_arkui_paragraphstyle_settailindents)）
 - 自定义组件的生命周期新增支持组件由非激活状态转变为激活状态的装饰器[@ComponentActive](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-new-lifecycle#componentactive)，以及组件由激活状态转变为非激活状态的装饰器[@ComponentInactive](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-new-lifecycle#componentinactive)。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-custom-components-new-lifecycle#自定义组件的激活与非激活生命周期)）
 - 窗口管理新增支持设置主窗或子窗支持的窗口模式。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#setsupportedwindowmodes)）
 - 窗口管理的闪控球新增销毁事件的监听。当闪控球销毁时，回调函数会接收到销毁原因的字符串。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-floatingball#ondestroy)）




#### ArkTS

setMultithreadingDetectionEnabled接口新增多线程检测可配置参数，支持开发者配置故障类型、采样频率、故障上报时间间隔（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-util#multithreadingdetectionoptions)）



#### Audio Kit

 - 新增音频设备增强管理器功能。（[ArkTS API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiodeviceenhancemanager)、[C API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-device-enhance-manager-h)）
 - 新增基于C/C++的音频格式转换能力。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-suite-format-converter)）




#### AVSession Kit

 - 新增支持自定义播控中心的控制按钮显示布局的能力。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/avsession-mediacentercontroltype-scene)）
 - 媒体会话管理AVSession新增支持设置应用支持的播放倍速列表（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-avsession#setsupportedplayspeeds)）、设置应用支持的循环模式列表（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-avsession#setsupportedloopmodes)）、设置应用支持的控制类型列表（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-avsession#setmediacentercontroltype)）。同时通过AVSessionController支持获取应用支持的播放倍速列表（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-avsessioncontroller#getsupportedplayspeeds)）、获取应用支持的循环模式列表（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-avsessioncontroller#getsupportedloopmodes)）、获取应用支持的控制类型列表（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-avsessioncontroller#getmediacentercontroltype)），以及支持注册播放倍速列表变化的监听事件（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-avsessioncontroller#onsupportedplayspeedschange)）、注册循环模式列表变化的监听事件（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-avsessioncontroller#onsupportedloopmodeschange)）、注册控制类型列表变化的监听事件（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-avsessioncontroller#onmediacentercontroltypechanged)）。




#### Basic Services Kit

串口通信能力新增支持对串口通信的管理，包括获取串口设备列表、打开和关闭串口、读写数据、硬件流控信号管理等。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/serial-guidelines)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-busmanager-serial)）



#### Camera Kit

C API新增元数据对象扩展概念的声明。（[C API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-metadata-object-ext-h)）



#### Confidential Space Kit

【新增Kit】Confidential Space Kit（机密空间服务）提供了在机密空间内部运行数据应用、处理隐私数据的能力，支持应用与系统、应用与应用在空间内安全地共享数据，防止隐私信息外泄。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/confidentialspace-introduction)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/confidentialspace-confidentialspace)）



#### Core File Kit

新增支持压缩解压缩模块，为应用提供数据压缩和解压缩的能力，可用于文件打包分发、减少存储占用、加速网络传输等场景。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/archive-overview)）



#### Desktop Extension Kit

 - 新增查询接入快捷栏能力，支持开发者查询当前设备是否可以接入快捷栏。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/desktop-quickbar-extension-guide#检查是否支持快捷栏功能)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/desktop-quickbar-extension-manager#quickbarmanagerisquickbarcapabilitysupported)）
 - 新增设置快捷栏应用图标和进度条能力，支持开发者自定义图标和进度条。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/desktop-quickbar-extension-guide#快捷栏自定义图标和进度条)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/desktop-quickbar-extension-manager#quickbarmanagersetquickbarcombineicon)）
 - 新增检查设备状态是否支持状态栏图标接入能力，以及图标悬浮（hover）状态回调能力。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/statusbar-extension-guide#开发步骤)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/statusbar-extension-manager#statusbarmanagerisstatusbarcapabilitysupported)）




#### Device Security Kit

 - 新增设备开关机、音频接口插拔、视频接口插拔、账户管理等通知类审计事件。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-securityaudit-api#notifyevent)）
 - 新增应用进程执行、文件读结束的阻断类审计事件。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-audit-subscribe-c-auth#场景介绍)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-securityaudit-api#authevent)）
 - 新增ArkTS API、C API，支持审计阻断类事件设置默认超时阻断策略。（[ArkTS API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-securityaudit-api#authclientconfiguration)、[C API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-securityaudit#hms_securityaudit_createauthclientconfiguration)）
 - 新增ArkTS API、C API，支持全量查询阻断类客户端信息。（[ArkTS API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-securityaudit-api#acquireallauthclientsinfo)、[C API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-securityaudit#hms_securityaudit_acquireallauthclientsinfo)）
 - 新增ArkTS API、C API，支持全量查询通知类客户端信息。（[ArkTS API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-securityaudit-api#acquireallclientsinfo)、[C API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-securityaudit#hms_securityaudit_acquireallclientsinfo)）




#### Enterprise Data Guard Kit

新增进程管控时长管理，支持开发者查询、设置进程管控策略和查询、添加与删除进程管控信息。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-managed-process-management)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataguard-fileguard#getmanagedprocesspolicy)）



#### Enterprise Space Kit

 - 新增切换工作空间的能力。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-lifecycle-management)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/enterprisespace-spacemanager#switchworkspace)）
 - 新增支持跨空间消息提醒配置的能力。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-cross-space-notification)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/enterprisespace-spacemanager#setnotificationconfig)）




#### Enterprise Threat Protection Kit

病毒检测与处置服务新增威胁进程终止接口，为企业安全类应用提供对运行中恶意进程及可疑进程的安全处置能力。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisethreatprotection-virusremediation-terminate)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/enterprisethreatprotection-virusremediation-interface#terminateprocess)）



#### FAST Kit

 - 新增高性能排序能力，支持通用数据类型的排序操作。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-utils-algorithm-8h)）
 - 新增多项式零点求解器能力，支持一元多项式的实数根计算。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fast-polynomial-root)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-solver-polynomial-8h)）
 - 新增复数向量基础运算、信号处理与线性代数、向量归约与统计能力。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fast-concurrent-hashmap)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-dsp-transform-8h#函数)）
 - 新增高性能哈希表数据结构能力，支持哈希表的创建与销毁等功能。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fast-hashmap)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-collections-hashmap-8h)）
 - 新增系统优化能力，支持应用程序向系统提供性能场景信息，系统在生效范围内优化应用性能，提升用户体验。（[指南-ArkTS](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fast-scheduling-optimization_arkts)、[ArkTS API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-scheduling-optimization)、[指南-C](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fast-scheduling-optimization_c)、[C API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-scheduling-optimization-8h)）




#### Graphics Accelerate Kit

新增游戏伴随服务，为游戏陪玩类的应用提供伴随悬浮控件、游戏状态感知、音频采集与传输、游戏画面采集等基础能力。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-gamebuddy-service)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/graphics-accelerate-gamebuddyservice)）



#### Linx Kit

【新增Kit】Linx Kit（灵犀加速库）基于芯片底层架构实现软硬协同优化，提供CPU的性能加速能力。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/linx-kit-introduction)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hotspot-accelerate)）



#### Map Kit

 - 新增支持折线添加文字。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-polyline#折线添加文字)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mappolyline#addlinetext)）
 - 新增支持3D地球背景替换。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-presenting#section3d地球背景替换)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mapcomponentcontroller#setspheremapenabled)）
 - 新增支持信号路线功能，可预测路线中的弱信号或无信号路段，提前提醒用户下载离线地图、提升户外安全性。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-map-signal-line)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mapcomponentcontroller#addsignalline)）
 - 在屏幕坐标和经纬度转换场景下，新增设置相对于地面的高度。（[API参考-将像素点坐标转换成经纬度坐标](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-projection#fromscreenlocation-1)、[API参考-将经纬度坐标转换成像素点坐标](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-projection#toscreenlocation-1)）
 - 新增支持根据经纬度查询离线地图中未下载的区域。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-offline-map-data)）




#### MDM Kit

 - 企业设备的账号管理新增创建普通系统账号（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-accountmanager#accountmanagercreatenormalosaccount)）、移除系统账号（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-accountmanager#accountmanagerremoveosaccount)）以及切换系统账号（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-accountmanager#accountmanageractivateosaccount)）的接口。
 - 企业设备的应用管理新增支持查询指定应用的窗口状态信息列表。可以查询到应用是否在底部Dock栏，以及当前应用窗口是否在前台显示等信息。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-applicationmanager#applicationmanagergetapplicationwindowstates)）




#### Media Kit

 - 新增C API，支持对音频PCM数据处理后再播出的能力（[C API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avplayer-h#oh_avplayer_setpcmprocessorcallback)），同时支持设置音频处理后再播出的回调函数单次可返回的最大数据量（[C API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avplayer-h#oh_avplayer_setpcmprocessormaxlen)）。
 - 新增ArkTS API，支持广告插播能力，实现广告资源的播放以及广告事件的监听。（[ArkTS API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avadscontroller)）
 - 新增ArkTS API，实现应用可以离线缓存下载在线资源。（[ArkTS API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avdownloadermanager)）
 - 新增ArkTS API和C PAI，支持录屏过程中暂停录制屏幕与恢复录制屏幕的能力。 （[ArkTS API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-i#avscreencapturestrategy20)、[C API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-h#oh_avscreencapture_strategyforpause)）
 - 新增C PAI，支持对指定应用的所有窗口进行屏幕录制。（[C API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-base-h#oh_capturepickermode)）




#### NearLink Kit

 - 新增订阅的配对状态变化原因详情。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-manager#pairingstateparam)）
 - 新增订阅的连接状态变化事件的原因详情。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-manager#connectionstateparam)）
 - 新增扫描扫描过滤条件，过滤信号强度大于或等于信号强度门限值的广播报文。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-scan#scanfilters)）




#### Network Kit

建立WebSocket连接的可选参数新增支持supportOriginPort，可用于控制Origin字段是否携带自定义端口号。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-websocket#websocketrequestoptions)）



#### Online Authentication Kit

 - 新增用户认证失败切换其他认证方式的认证方式指示。（[ArkTS API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/onlineauthentication-passkey-api#authenticate)、[C API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/onlineauthentication_capi_header_fido2#枚举)）
 - 新增可选择的认证类型列表。（[ArkTS API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/onlineauthentication-passkey-api#clientcapability)、[C API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/onlineauthentication_capi_header_fido2#枚举)）
 - 新增credentialDisclosurePropertyList参数，支持查看凭证披露属性列表。([API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/onlineauthentication-did-api#credentialfilter))




#### PDF Kit

 - 新增支持自定义渲染风格功能。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pdf-arkts-pdfviewmanage#setrendermode)）
 - 新增支持二进制数据读取PDF能力。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pdf-arkts-pdfviewmanage#loaddocumentfrommemory)）
 - 新增支持根据视图坐标点获取PDF页面索引。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pdf-arkts-pdfviewmanage#getpageindexfromviewpoint)）
 - 新增支持视图坐标与PDF页面坐标的双向点转换。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pdf-arkts-pdfviewmanage#pdfpointtoviewpoint)）
 - 新增支持视图坐标与PDF页面坐标的双向矩形转换。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pdf-arkts-pdfviewmanage#viewrecttopdfrect)）




#### Pen Kit

新增手写笔跟手性加速接口，支持笔记类应用提升手写笔书写时延。（[指南-ArkTS](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pen-stylus-frame-boost)、[指南-C](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pen-stylus-frame-boost-c)、[ArkTS API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-stylusframeboost)、[C API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-handwrite-c#hms_handwrite_setrefreshdelayoff)）



#### Performance Analysis Kit

HiDebug新增支持注册内存导出监听器，用于在内存占用较高或通过hidumper命令手动触发时导出应用内存快照。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hidebug-guidelines#导出内存快照)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-h#oh_hidebug_registermemdumplistener)）



#### Ringtone Kit

查询不同铃声类型和文件类型对应的文件大小上限。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ringtone-preparations)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ringtone-ringtone#ringtonegetsupportedmaxsize)）



#### Remote Communication Kit

 - 新增支持设置抛出异常时是否在异常信息中显示明文内容。（[API参考](https://developer.huawei.com/consumer/cn/doc/doccenter-capabilities/api/remote-communication-rcp#tracingconfiguration)）
 - 新增支持证书压缩和解压缩。（[API参考](https://developer.huawei.com/consumer/cn/doc/doccenter-capabilities/api/remote-communication-rcp#certificatedecompress)）
 - 新增支持国密[TLCP](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=778097598DA2761E94A5FF3F77BD66DA)协议。（[API参考](https://developer.huawei.com/consumer/cn/doc/doccenter-capabilities/api/remote-communication-rcp#securitylayertype)）
 - 新增支持多路传输控制协议（MPTCP）。（[API参考](https://developer.huawei.com/consumer/cn/doc/doccenter-capabilities/api/remote-communication-rcp#sessionpathpreference)）




#### Service Collaboration Kit

新增碰一碰场景API，设备间可以通过顶端碰的方式触发连接、传递信息、断开连接等。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/serviceinteraction-dev-guides)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-collaboration-serviceinteraction)）



#### Service Support Kit

【新增Kit】Service Support Kit（服务与支持）为企业开发者应用提供设备硬件检测能力，通过对设备的硬件状态信息进行检测，以达到硬件信息快速评估、提升检测效率的效果。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/service-support-introduction)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-devicedetection)）



#### Spatial Recon Kit

 - 新增分块3DGS（Tiled 3D Gaussian Splatting）渲染对象，支持设置驱动分块选择的相机、设置瓦片请求回调函数、通知渲染器指定的瓦片现在可以加载等。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/spatial-recon-spatialrender#tiledgsnode)）
 - 新增高级回调函数（HMS_SpatialReconNGCallbackFunc）类型，支持在通知开发者重建或保存的结果时传入额外的数据，方便开发者区分不同的重建任务。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-spatial-recon-interface-h#hms_spatialrecon_registerngcallbackfunc)）




#### UI Design Kit

 - 新增颜色选择与收藏管理功能，支持网格、光谱和滑块三种颜色选择模式，支持用户将常用颜色添加到收藏列表。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-color-picker-favorites)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdscolorpicker)）


 - HdsSnackBar组件新增新增支持左侧图标（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdssnackbar#snackbariconoptions)）、中间文本的标题和内容（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdssnackbar#snackbarmessageoptions)）、右侧操作区关闭按钮的图标（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdssnackbar#snackbaroperationoptions)）的样式修改。
 - HdsListItem组件新增多态样式的设置功能。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdslistitem#hdslistitemstatestylesoptions)）
 - HdsListItemCard组件单选框支持样式选择。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdslistitemcard#hdsradiostyle)）




#### XEngine Kit

空域AI超分特性OpenGL ES移除对OH_NativeBuffer的依赖，提升集成灵活性。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xengine-kit-ai-spatial-upscaling#集成xengine空域ai超分opengl-es)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_neural_upscale2_extension_name)）



#### 26.0.0 Beta1新增和增强特性



#### Ability Kit

 - 新增支持AgentCard，提供AgentCard的配置、解析与持久化。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agent-extension-configuration)）
 - 新增支持基于ArkTS脚本的应用Skill开发能力。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-skill-development-guide)）
 - 新增支持获取指定包名和分身索引的应用名称。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager#bundlemanagergetapplicationlabel)）
 - 新增用于脚本管理的ArkTS API模块，提供管理和组织脚本信息的能力。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-scriptmanager)）




#### Accessibility Kit

新增支持应用接入系统的关怀模式，使应用提升长辈关怀功能及体验。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/eldercare-appconfig)）



#### Accessory Kit

【新增Kit】Accessory Kit（配件接入服务）为合作配件设备及生态企业应用提供关联唤醒、系统服务联动、按需调度与安全授信管理等能力，有效提升配件设备接入效率。

详细信息请参见[Accessory Kit开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/accessorykit-introduction)。



#### Account Kit

LoginWithHuaweiIDButton组件新增支持自定义设置文本多语言显示、自定义动效加载。（[API参考-文本多语言显示](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-component-manager#setlocale)、[API参考-自定义动效加载](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-component-manager#extrastyle)）



#### AR Engine

 - 新增C API，支持控制相机闪光灯。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#hms_arengine_arsession_openflash)）
 - 新增ArkTS API，支持获取预览流图片数据。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-api-arengine#arframeacquirecameraimage)）
 - 新增ArkTS API，支持加载3D高斯模型。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-api-arviewcontroller#arviewcontextloadgsmodel)）
 - 新增ArkTS API、C API，支持获取外部相机和传感器数据进行计算。（[ArkTS API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-api-arengine#arremotesensormode)、[C API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#arengine_remotesensormode)）




#### ArkGraphics 2D

绘制模块新增用于处理坐标点的类，支持对坐标点取反和设置偏移量。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-pointutils)）



#### ArkUI

 - 新增通用属性systemMaterial，所有支持通用属性的组件，均支持通过systemMaterial设置系统材质。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-image-effect#systemmaterial)）
 - Chip组件新增支持通过backgroundSystemMaterial和activatedBackgroundSystemMaterial配置正常状态和激活状态下的系统材质背景。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-chip#示例10设置系统材质样式)）
 - 弹窗类组件或元素新增配置项systemMaterial，支持系统材质效果：[Tips组件悬浮气泡](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-tips#示例3设置悬浮气泡的系统材质视效)、[Toast](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-promptaction#showtoastoptions)、[对话框](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-promptaction#showdialogoptions)、[操作菜单](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-promptaction#actionmenuoptions)、[自定义弹窗](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-custom-dialog-box#customdialogcontrolleroptions对象说明)、[半模态](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sheet-transition#示例10半模态设置系统材质)、[Popup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-popup#popupoptions类型说明)等。
 - 新增ArkUI组件级沉浸光感，提供的一套高品质视觉与动效体系，通过沉浸式系统材质效果与空间动效的结合，为应用组件带来通透、精致的视觉表现。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-immersive-light-sense)）
 - 新增容器断点组件ContainerReader，允许开发者基于容器尺寸而非窗口尺寸实现自适应布局。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-container-reader)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-containerreader)）
 - 新增懒加载垂直瀑布流布局容器LazyVWaterFlowLayout，嵌套在可滚动父组件（Scroll、List、WaterFlow）内部，负责按需加载子组件。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-lazy-layout)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-lazyvwaterflowlayout)）
 - 新增自定义组件全局复用能力，可针对指定@Reusable/@ReusableV2复用组件配置复用池，用于提供全局复用的能力。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-reuse-pool)）
 - 窗口管理新增闪控窗。闪控窗是悬浮在桌面/应用界面上的小型窗口，提供灵活的窗口管理能力，包括判断设备是否支持闪控窗功能、创建闪控窗控制器以启动、更新或停止闪控窗等。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-floatview)）




#### ArkWeb

 - ArkWeb基于上游社区的Chromium内核从132升级为144版本。（[变更说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-for-all-apps-7001#ch2026032368425)）
 - 新增安全特性选项配置的类，用于设置网页的安全配置属性。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-securityparams)）




#### AVCodec Kit

 - H265硬件编码器新增支持CBRHQ（高质量恒定码率模式）。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/video-encoding-configuration-typical-scenarios#低时延场景)）
 - Audio Vivid能力新增支持Audio Vivid编码。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audiovivid-audioencoder)）
 - C API新增提供Audio Vivid相关的函数和枚举。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-vivid-h)）




#### AVSession Kit

AVSession的枚举新增定义了在不同场景中使用的额外键的枚举。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-e#extrakey)）



#### Background Tasks Kit

提醒的倒计时实例对象新增参数重复周期（repeatInterval）和重复次数（repeatCount）。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-reminderagentmanager#reminderrequesttimer)）



#### Core Vision Kit

 - 新增支持图像超分能力，可实现对低分辨率图像进行超分辨率重建，使图像更加清晰。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/core-vision-image-super-resolution)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/core-vision-image-super-resolution-api)）
 - 新增支持通过文本语意搜索图片的能力，即用户可以通过输入文本语意，从图片库中搜索匹配的图像结果。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/core-vision-text-search-image)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/core-vision-text-search-image-api)）




#### Core File Kit

 - 打开文件或目录时新增参数UNCACHE，支持读写文件不进行页缓存。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileioopen)）
 - 新增listFileExt方法支持递归列出和自定义文件名过滤。可通过配置options中recursion参数实现递归列出所有文件的相对路径。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiolistfileext)）
 - 新增支持开发者通过文件mmap能力集（基于文件描述符或文件对象创建文件映射对象），实现文件的高效读写访问。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiommap)）
 - 新增支持应用捐献自身沙箱目录给系统设置为共享，其他应用可以通过文管直接获取到目录里的文件。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-app-file-configuration)）




#### Data Augmentation Kit

知识加工新增邮件智能分析模块（Handler），支持邮件分类、摘要、待办抽取。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-augmentation-knowledge-processing#开发步骤)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-knowledgeprocessor-api#knowledgeprocessorconfig)）



#### Device Security Kit

 - 新增星盾机密风控引擎能力，支持风险因子引入、联防联控。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-starshieldconfidentialriskcontrolengine)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-riskcontrolengine-api)）
 - 新增统一风控凭证能力。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-safetydetect-queryriskfactors)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-safetydetectenhanced-api#queryriskfactors)）


 - 新增超级隐私策略化管控能力，支持对相机、麦克风、位置分别进行管控。（[指南-查询管控策略场景](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-getsuperprivacypolicies)、[指南-订阅管控策略改变事件场景](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-subscribe-superprivacypolicy)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-superprivacymode-api)）
 - 新增按文件操作类型订阅文件事件，支持订阅文件打开、关闭、删除、重命名、拷贝等事件。（[API参考-ArkTS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-securityaudit-api#notifyevent)、[API参考-C/C++](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-security-audit-8h#枚举)）
 - 新增按文件路径正则表达式过滤文件事件，支持按正则表达式过滤文件事件。（[API参考-ArkTS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-securityaudit-api#filtertype)、[API参考-C/C++](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-security-audit-8h#枚举)）




#### Driver Development Kit

新增支持查询外接USB Hub并开发用户态驱动。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usb-ddk-api-h#oh_usb_getnonroothubs)）



#### Enterprise Data Guard Kit

 - 文件分级管控服务新增getPolicy接口，支持用户获取当前设备生效的管控策略内容。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataguard-fileguard#getpolicy)）
 - 文件分级管控服务新增isKia接口，支持用户判断文件或文件夹是否是KIA。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataguard-fileguard#iskia)）




#### Enterprise Space Kit

新增支持查询设备双空间状态、判断工作空间是否为企业空间的能力。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-lifecycle-management)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/enterprisespace-spacemanager)）



#### FAST Kit

 - 新增实数快速傅里叶变换（FFT）及其逆变换功能，支持实数时域信号及其相应频域信号间的快速转换。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fast-dsp-transform)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-dsp-transform-8h)）
 - 新增智能序列预测功能，支持接收历史采样数据预测下一时刻的序列值。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fast-math-prediction)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-math-prediction)）




#### Game Service Kit

游戏近场快传新增支持免集成Game Service Kit实现安装包传输。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-nearbytransfer-installation-package#免集成game-service-kit实现安装包传输)）



#### Graphics Accelerate Kit

 - 游戏资源加速服务新增isSupportAssetDownload接口，支持查询用户的当前设备类型是否支持资源包下载能力。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/graphics-accelerate-assetdownloadmanager#assetdownloadmanagerissupportassetdownload)）
 - 游戏资源加速服务的AppDownloadProgress新增resourceVersion参数，支持开发者通过正在下载资源的版本标识符上报下载进度信息。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/graphics-accelerate-assetdownloadmanager#appdownloadprogress)）
 - 游戏启动加速服务新增预启动特性，支持根据用户的使用习惯，在系统资源充足时提前加载游戏，进行部分初始化和资源加载的能力。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-prelaunch)）
 - 游戏渲染加速新增枚举FG_FeatureType，定义超帧的特性类型。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#fg_featuretype)）
 - 新增接口HMS_FG_IsFrameGenerationSupported，支持查询用户的当前设备类型是否支持此类型的超帧功能。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#hms_fg_isframegenerationsupported)）




#### Image Kit

 - 新增[GIF图像元数据类](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-gifmetadata)、[JFIF图像元数据类](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-jfifmetadata)、[TIFF图像元数据类](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-tiffmetadata)、[PNG图像元数据类](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pngmetadata)以及[AVIS图像元数据类](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-avismetadata)，用于存储对应格式图像的元数据。
 - 新增[XMP（Extensible Metadata Platform）元数据](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-xmpmetadata)。




#### Input Kit

新增输入事件注入模块，提供键盘和鼠标输入事件模拟能力。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputeventclient)）



#### Live View Kit

新增实况窗卡片辅助区模板，支持展示百分比进度环。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/liveview-liveviewmanager#extensiondata)）



#### NDK

JSVM新增支持从外部内存创建ArrayBuffer对象。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-h#oh_jsvm_createarraybufferfromexternalmemory)）



#### Nearlink Kit

新增startScan接口，支持扫描所有可发现的周边星闪设备。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-scan#startscan-1)）



#### Network Boost Kit

新增netBoost.setDataFlowDesc接口，支持应用根据五元组信息设置流描述。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/networkboost-netboost#netboostsetdataflowdesc)）



#### Notification Kit

 - 新增是否开启锁屏通知等字段。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationmanager#notificationsetting20)）
 - 新增支持以半模态方式拉起应用的通知设置界面。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationmanager#notificationmanageropennotificationsettingswithresult)）




#### Online Authentication Kit

新增DID（Decentralized Identifier，去中心化身份）能力，支持DID密钥生成、数字凭证导入/查询/删除、数据签名等功能。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/onlineauthentication-did)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/onlineauthentication-did-api)）



#### PDF Kit

新增支持将多张页面的指定区域转化为一张图片。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pdf-arkts-pdfservice#getpixelmapwithpages)）



#### Push Kit

推送实况窗消息能力新增支持Wearable设备。([指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-update-liveview)）



#### Performance Analysis Kit

 - 新增应用灰度采集的管理，可通过端云配合，采集应用故障日志，提升应用运维能力。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiretrieval-intro)）
 - HiAppEvent新增应用冻屏告警事件，提供事件的订阅能力。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-appfreezewarning-events)）




#### Preview Kit

 - 新增C API，支持在文件打开加速前，扫描文件是否具备加速条件，并且在文件加速场景下，可定制加速的预加载策略，包括动态配置文件后缀和文件大小范围。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/preview-openfileboost)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost_preview)）
 - 新增C API，支持文件打开加速服务可用性查询和文件操作事件上报功能。（[API参考-可用性查询](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost_preview#hms_preview_openfileboost_isenabled)、[API参考-文件操作事件上报](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost_preview#hms_preview_openfileboost_notifyfileoperation)）




#### Remote Communication Kit

 - 新增HttpVersionSelectCallback接口，支持选择HTTP版本。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-rcp#httpversionselectcallback)）
 - 新增HMS_Rcp_SetRequestGetDataCallback()接口，支持流式上传。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#hms_rcp_setrequestgetdatacallback)）
 - 新增HMS_Rcp_SetFormOrder()接口，支持发送有序表单。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#hms_rcp_setformorder)）
 - 新增C API，支持使用QUIC客户端进行数据传输。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/remote-communication-quic-persistent-connection)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_quic_h)）




#### Scan Kit

 - 新增支持查询当前设备是否支持默认界面扫码。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scan-scancore#isdefaultscansupported)）
 - 新增支持查询当前设备是否支持自定义界面扫码。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scan-scancore#iscustomscansupported)）




#### Scenario Fusion Kit

场景化分享Button新增参数，支持分享图片、视频、文本等格式。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scenario-fusion-functionalbuttoncomponentmanager#shareparam)）



#### Share Kit

手机与PC/2in1、手机与Tablet设备触发碰一碰分享时，新增支持在PC/2in1或Tablet设备侧获取轻碰的位置信息。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/knock-share-pc-phones-mutually#获取轻碰坐标)）



#### Spatial Recon Kit

新增支持编辑3DGS模型中的高斯球，包括选择、变换、上色和删除等操作。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/spatial-recon-spatialedit)）



#### UI Design Kit

 - 新增标题顶部自定义区域更新节点的配置能力。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsnavigation#titlebarcontentoptions)）
 - 新增标题底部自定义区域是否更新节点的配置能力。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsnavigation#bottombuilderparams)）




#### XEngine Kit

 - 新增控显分离特性，支持折叠机在展开态下，在上屏显示游戏画面，在下屏显示游戏按键及部分信息，提升游戏沉浸感。（[指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xengine-kit-control-display-separation)、[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-neuralupscalecreateinfo)）
 - 空域AI超分特性新增支持Vulkan协议。（[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-neural-upscale-8h)）
