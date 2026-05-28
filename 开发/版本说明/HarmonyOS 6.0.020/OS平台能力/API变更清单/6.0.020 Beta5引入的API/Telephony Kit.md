# Telephony Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-telephonykit-6004

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：eSIM； API声明：export interface AccessRule 差异内容：export interface AccessRule | api/@ohos.telephony.esim.d.ts |
| 新增API | NA | 类名：AccessRule； API声明：certificateHashHexStr: string; 差异内容：certificateHashHexStr: string; | api/@ohos.telephony.esim.d.ts |
| 新增API | NA | 类名：AccessRule； API声明：packageName: string; 差异内容：packageName: string; | api/@ohos.telephony.esim.d.ts |
| 新增API | NA | 类名：AccessRule； API声明：accessType: number; 差异内容：accessType: number; | api/@ohos.telephony.esim.d.ts |
| 新增API | NA | 类名：sim； API声明：function getSimLabel(slotId: number, callback: AsyncCallback&lt;SimLabel&gt;): void; 差异内容：function getSimLabel(slotId: number, callback: AsyncCallback&lt;SimLabel&gt;): void; | api/@ohos.telephony.sim.d.ts |
| 新增API | NA | 类名：sim； API声明：function getSimLabel(slotId: number): Promise&lt;SimLabel&gt;; 差异内容：function getSimLabel(slotId: number): Promise&lt;SimLabel&gt;; | api/@ohos.telephony.sim.d.ts |
| 新增API | NA | 类名：sim； API声明：function getSimLabelSync(slotId: number): SimLabel; 差异内容：function getSimLabelSync(slotId: number): SimLabel; | api/@ohos.telephony.sim.d.ts |
| 新增API | NA | 类名：sim； API声明：export enum SimType 差异内容：export enum SimType | api/@ohos.telephony.sim.d.ts |
| 新增API | NA | 类名：SimType； API声明：PSIM = 0 差异内容：PSIM = 0 | api/@ohos.telephony.sim.d.ts |
| 新增API | NA | 类名：SimType； API声明：ESIM = 1 差异内容：ESIM = 1 | api/@ohos.telephony.sim.d.ts |
| 新增API | NA | 类名：sim； API声明：export interface SimLabel 差异内容：export interface SimLabel | api/@ohos.telephony.sim.d.ts |
| 新增API | NA | 类名：SimLabel； API声明：simType: SimType; 差异内容：simType: SimType; | api/@ohos.telephony.sim.d.ts |
| 新增API | NA | 类名：SimLabel； API声明：index: number; 差异内容：index: number; | api/@ohos.telephony.sim.d.ts |
