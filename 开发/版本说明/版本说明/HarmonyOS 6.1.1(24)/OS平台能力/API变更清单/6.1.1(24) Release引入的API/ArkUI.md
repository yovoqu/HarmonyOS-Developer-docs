# ArkUI

更新时间：2026-06-27 01:41:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkui-6112

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：CrownAction； API声明：BEGIN = 0 差异内容：24 dynamic | 类名：CrownAction； API声明：BEGIN = 0 差异内容：24 | component/enums.d.ts |
| 新增API | NA | 类名：global； API声明：declare interface CachedCountOptions 差异内容：declare interface CachedCountOptions | component/swiper.d.ts |
| 新增API | NA | 类名：CachedCountOptions； API声明：isShown?: boolean; 差异内容：isShown?: boolean; | component/swiper.d.ts |
| 新增API | NA | 类名：CachedCountOptions； API声明：independent?: boolean; 差异内容：independent?: boolean; | component/swiper.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围不是包含关系 | 类名：SwiperAttribute； API声明：cachedCount(count: number, isShown: boolean): SwiperAttribute; 差异内容：cachedCount(count: number, isShown: boolean): SwiperAttribute; | 类名：SwiperAttribute； API声明：cachedCount(count: number, options: CachedCountOptions): SwiperAttribute; 差异内容：cachedCount(count: number, options: CachedCountOptions): SwiperAttribute; | component/swiper.d.ts |
