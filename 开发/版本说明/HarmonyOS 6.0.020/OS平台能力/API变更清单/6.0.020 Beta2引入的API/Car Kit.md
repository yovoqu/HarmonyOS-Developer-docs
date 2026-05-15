# Car Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-carkit-6002

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：navigationInfoMgr； API声明：function getNavigationController(): NavigationController; 差异内容：NA | 类名：navigationInfoMgr； API声明：function getNavigationController(): NavigationController; 差异内容：801 | api/@hms.carService.navigationInfoMgr.d.ts |
| 新增错误码 | 类名：NavigationController； API声明：updateNavigationStatus(navigationStatus: NavigationStatus): void; 差异内容：NA | 类名：NavigationController； API声明：updateNavigationStatus(navigationStatus: NavigationStatus): void; 差异内容：1003810001,1003810002,801 | api/@hms.carService.navigationInfoMgr.d.ts |
| 新增错误码 | 类名：NavigationController； API声明：updateNavigationMetadata(navigationMetadata: NavigationMetadata): void; 差异内容：NA | 类名：NavigationController； API声明：updateNavigationMetadata(navigationMetadata: NavigationMetadata): void; 差异内容：1003810001,1003810002,801 | api/@hms.carService.navigationInfoMgr.d.ts |
| 新增错误码 | 类名：NavigationController； API声明：registerSystemNavigationListener(listener: SystemNavigationListener): void; 差异内容：NA | 类名：NavigationController； API声明：registerSystemNavigationListener(listener: SystemNavigationListener): void; 差异内容：1003810001,801 | api/@hms.carService.navigationInfoMgr.d.ts |
| 新增错误码 | 类名：NavigationController； API声明：unregisterSystemNavigationListener(): void; 差异内容：NA | 类名：NavigationController； API声明：unregisterSystemNavigationListener(): void; 差异内容：801 | api/@hms.carService.navigationInfoMgr.d.ts |
| 新增错误码 | 类名：smartMobilityCommon； API声明：function getSmartMobilityAwareness(): SmartMobilityAwareness; 差异内容：NA | 类名：smartMobilityCommon； API声明：function getSmartMobilityAwareness(): SmartMobilityAwareness; 差异内容：801 | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增错误码 | 类名：SmartMobilityAwareness； API声明：on(type: 'smartMobilityStatus', smartMobilityTypes: SmartMobilityType[], callback: Callback<SmartMobilityInfo>): void; 差异内容：NA | 类名：SmartMobilityAwareness； API声明：on(type: 'smartMobilityStatus', smartMobilityTypes: SmartMobilityType[], callback: Callback<SmartMobilityInfo>): void; 差异内容：801 | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增错误码 | 类名：SmartMobilityAwareness； API声明：off(type: 'smartMobilityStatus', smartMobilityTypes: SmartMobilityType[], callback?: Callback<SmartMobilityInfo>): void; 差异内容：NA | 类名：SmartMobilityAwareness； API声明：off(type: 'smartMobilityStatus', smartMobilityTypes: SmartMobilityType[], callback?: Callback<SmartMobilityInfo>): void; 差异内容：801 | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增错误码 | 类名：SmartMobilityAwareness； API声明：on(type: 'smartMobilityEvent', smartMobilityTypes: SmartMobilityType[], callback: Callback<SmartMobilityEvent>): void; 差异内容：NA | 类名：SmartMobilityAwareness； API声明：on(type: 'smartMobilityEvent', smartMobilityTypes: SmartMobilityType[], callback: Callback<SmartMobilityEvent>): void; 差异内容：801 | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增错误码 | 类名：SmartMobilityAwareness； API声明：off(type: 'smartMobilityEvent', smartMobilityTypes: SmartMobilityType[], callback?: Callback<SmartMobilityEvent>): void; 差异内容：NA | 类名：SmartMobilityAwareness； API声明：off(type: 'smartMobilityEvent', smartMobilityTypes: SmartMobilityType[], callback?: Callback<SmartMobilityEvent>): void; 差异内容：801 | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增错误码 | 类名：SmartMobilityAwareness； API声明：getSmartMobilityStatus(type: SmartMobilityType): SmartMobilityInfo; 差异内容：NA | 类名：SmartMobilityAwareness； API声明：getSmartMobilityStatus(type: SmartMobilityType): SmartMobilityInfo; 差异内容：801 | api/@hms.carService.smartMobilityCommon.d.ts |
| 新增错误码 | 类名：SmartMobilityAwareness； API声明：getSmartMobilityEvent(type: SmartMobilityType, eventName: string): SmartMobilityEvent; 差异内容：NA | 类名：SmartMobilityAwareness； API声明：getSmartMobilityEvent(type: SmartMobilityType, eventName: string): SmartMobilityEvent; 差异内容：801 | api/@hms.carService.smartMobilityCommon.d.ts |
