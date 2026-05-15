# ArkUI

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkui-6012

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| syscap变更 | 类名：RenderNode； API声明：get shapeClip(): ShapeClip; 差异内容：SystemCapability.ArkUI.ArkUI.clip | 类名：RenderNode； API声明：get shapeClip(): ShapeClip; 差异内容：SystemCapability.ArkUI.ArkUI.Full | api/arkui/RenderNode.d.ts |
| 函数变更 | 类名：CommonMethod； API声明：onVisibleAreaApproximateChange(options: VisibleAreaEventOptions, event: VisibleAreaChangeCallback \| undefined): void; 差异内容：NA | 类名：CommonMethod； API声明：onVisibleAreaApproximateChange(options: VisibleAreaEventOptions, event: VisibleAreaChangeCallback \| undefined): T; 差异内容：T | component/common.d.ts |
| 新增API | NA | 类名：global； API声明：declare class ContentTransitionEffect 差异内容：declare class ContentTransitionEffect | component/common.d.ts |
| 新增API | NA | 类名：ContentTransitionEffect； API声明：static get IDENTITY(): ContentTransitionEffect; 差异内容：static get IDENTITY(): ContentTransitionEffect; | component/common.d.ts |
| 新增API | NA | 类名：ContentTransitionEffect； API声明：static get OPACITY(): ContentTransitionEffect; 差异内容：static get OPACITY(): ContentTransitionEffect; | component/common.d.ts |
| 新增API | NA | 类名：ImageAttribute； API声明：contentTransition(transition: ContentTransitionEffect): ImageAttribute; 差异内容：contentTransition(transition: ContentTransitionEffect): ImageAttribute; | component/image.d.ts |
| 新增API | NA | 类名：PosterOptions； API声明：contentTransitionEffect?: ContentTransitionEffect; 差异内容：contentTransitionEffect?: ContentTransitionEffect; | component/video.d.ts |
