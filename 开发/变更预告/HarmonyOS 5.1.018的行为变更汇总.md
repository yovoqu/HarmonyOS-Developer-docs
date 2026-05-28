# HarmonyOS 5.1.0(18)的行为变更汇总

更新时间：2026-01-23 09:24:00

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-roadmap/all-changelogs-510

##### OS平台API行为的变更
 
| Kit | 变更描述 | 变更引入版本 | 变更影响 | 影响设备类型 | 变更生效规则 |
| --- | --- | --- | --- | --- | --- |
| ArkTS | 默认不合并依赖混淆规则变更说明 | 5.1.0(18) Release | 小 | phone, tablet, 2in1 | DevEco Studio 5.1.0(18) Release版本生效 |
| ArkUI | getKeyboardAvoidMode接口返回值变更 | 5.1.0(18) Release | 小 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.1.0(18)变更生效 |
| ArkUI | XComponent组件上使用renderFit接口显示效果变更 | 5.1.0(18) Release | 中 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.1.0(18)变更生效 |
| ArkUI | 当使用自定义组件名和内置属性重名时编译报错变更 | 5.1.0(18) Release | 小 | phone, tablet, 2in1 | 使用DevEco Studio 5.1.0 Release及以上版本时生效 |
| ArkUI | CanvasRenderingContext2D方法传NaN和Infinity值后执行的其他绘制方法由不绘制变更为正常绘制 | 5.1.0(18) Release | 小 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.1.0(18)变更生效 |
| ArkUI | CanvasRenderingContext2D的drawImage接口默认单位变更 | 5.1.0(18) Release | 中 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.1.0(18)变更生效 |
| ArkUI | 修复blendMode接口离屏模式会影响组件设置的不透明度的问题 | 5.1.0(18) Release | 小 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.1.0(18)变更生效 |
| ArkUI | XComponent设置为Texture模式使用blendMode接口的行为由不生效变更为正常生效 | 5.1.0(18) Release | 小 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.1.0(18)变更生效 |
| ArkUI | setSpecificSystemBarEnabled接口在横屏的行为变更 | 5.1.0(18) Release | 小 | phone | targetSdkVersion ≥ 5.1.0(18)变更生效 |
| ArkUI | 滚动组件通用接口backToTop属性默认值变更 | 5.1.0(18) Release | 小 | phone, tablet | targetSdkVersion ≥ 5.1.0(18)变更生效 |
| ArkUI | 页面退出场景自定义组件删除前移 | 5.1.0(18) Release | 小 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.1.0(18)变更生效 |
| ArkUI | V1和V2组件冻结能力增强 | 5.1.0(18) Release | 小 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.1.0(18)变更生效 |
| Audio Kit | 音频框架识别USB音频设备类型行为变更 | 5.1.0(18) Release | 小 | 2in1 | targetSdkVersion ≥ 5.1.0(18)变更生效 |
| Basic Services Kit | osAccount.distributedAccount.DistributedAccountAbility.getOsAccountDistributedInfo接口返回值生成规则变更 | 5.1.0(18) Release | 中 | phone, tablet, 2in1 | 全部生效 |
| CANN Kit（原HiAI Foundation Kit） | 原hiai_foundation目录下的头文件废弃，替换为CANNKit下的头文件 | 5.1.0(18) Release | 小 | phone, tablet, 2in1 | 使用DevEco Studio 5.1.0 Release及以上版本时生效 |
| Device Security Kit | Device Security Kit优化错误码上报 | 5.1.0(18) Release | 中 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.1.0(18)变更生效 |
| Form Kit | 卡片支持能力增加安全校验 | 5.1.0(18) Release | 中 | phone, tablet, 2in1 | 全部生效 |
| Media Kit | 应用创建SoundPool时调用media.createSoundPool接口变更 | 5.1.0(18) Release | 小 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.1.0(18)变更生效 |
| Performance Analysis Kit | 用户态trace打点格式变更 | 5.1.0(18) Release | 小 | phone, tablet, 2in1 | 全部生效 |
| Remote Communication Kit | fetch接口新增错误码返回 | 5.1.0(18) Release | 小 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.1.0(18)变更生效 |
| NDK开发 | JIT功能默认关闭，需申请权限证书并通过审核后启用 | 5.1.0(18) Release | 大 | phone, tablet, 2in1 | 全部生效 |
 
 
 

##### UX样式或效果的变更
 
| 变更描述 | 变更引入版本 | 变更影响 | 影响设备类型 | 变更生效规则 |
| --- | --- | --- | --- | --- |
| 按钮默认值变更为新增圆角矩形类型 | 5.1.0(18) Release | 小 | phone, tablet, 2in1 | targetSdkVersion ≥ 5.1.0(18)变更生效 |
| 修复Popup高级组件宽度限制计算错误的问题 | 5.1.0(18) Release | 小 | phone, tablet, 2in1 | 全部生效 |
| 半模态底部样式最大高度默认避让状态栏安全区 | 5.1.0(18) Release | 小 | phone | targetSdkVersion ≥ 5.1.0(18)变更生效 |
 
 
 

##### 开发工具的变更
 
| 工具分类 | 变更描述 | 变更引入版本 | 变更影响 | 影响设备类型 | 变更生效规则 |
| --- | --- | --- | --- | --- | --- |
| 命令行工具 | hiperf命令行调试工具使用权限缩小 | 5.1.0(18) Release | 小 | phone, tablet, 2in1 | 使用DevEco Studio 5.1.0 Release及以上版本时生效 |
| DevEco Studio | DevEco Studio中fastjson版本升级 | 5.1.0(18) Release | 小 | phone, tablet, 2in1 | 使用DevEco Studio 5.1.0 Release及以上版本时生效 |
| DevEco Studio | 堆栈格式变化 | 5.1.0(18) Release | 小 | phone, tablet, 2in1 | 使用DevEco Studio 5.1.0 Release及以上版本时生效 |
