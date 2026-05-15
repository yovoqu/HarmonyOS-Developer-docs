# Vision Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-visionkit-b105

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：interactiveLiveness； API声明：function startLivenessDetection(config: InteractiveLivenessConfig): Promise<boolean>; 差异内容：1008301002 | 类名：interactiveLiveness； API声明：function startLivenessDetection(config: InteractiveLivenessConfig): Promise<boolean>; 差异内容：1008301002,201 | api/@hms.ai.interactiveLiveness.d.ts |
| 新增API | NA | 类名：VisionImageAnalyzerController； API声明：setSubjectMenuVisibility(visible: boolean): void; 差异内容：setSubjectMenuVisibility(visible: boolean): void; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：VisionImageAnalyzerController； API声明：on(type: 'objectSearchPanelVisibilityChange', callback: Callback<ObjectSearchPanelVisibility>): void; 差异内容：on(type: 'objectSearchPanelVisibilityChange', callback: Callback<ObjectSearchPanelVisibility>): void; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：VisionImageAnalyzerController； API声明：off(type: 'objectSearchPanelVisibilityChange', callback?: Callback<ObjectSearchPanelVisibility>): void; 差异内容：off(type: 'objectSearchPanelVisibilityChange', callback?: Callback<ObjectSearchPanelVisibility>): void; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：visionImageAnalyzer； API声明： enum ObjectSearchPanelVisibility 差异内容： enum ObjectSearchPanelVisibility | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：ObjectSearchPanelVisibility； API声明：SHOW = 0 差异内容：SHOW = 0 | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：ObjectSearchPanelVisibility； API声明：HIDE = 1 差异内容：HIDE = 1 | api/@hms.ai.visionImageAnalyzer.d.ets |
