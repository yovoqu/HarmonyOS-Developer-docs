# Vision Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-visionkit-5111

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：CardRecognition； API声明：callback: Callback&lt;CallbackParam&gt;; 差异内容：NA | 类名：CardRecognition； API声明：callback: Callback&lt;CallbackParam&gt;; 差异内容：19 | api/@hms.ai.CardRecognition.d.ets |
| API废弃版本变更 | 类名：global； API声明：declare interface CallbackParam 差异内容：NA | 类名：global； API声明：declare interface CallbackParam 差异内容：19 | api/@hms.ai.CardRecognition.d.ets |
| API废弃版本变更 | 类名：CallbackParam； API声明：code: number; 差异内容：NA | 类名：CallbackParam； API声明：code: number; 差异内容：19 | api/@hms.ai.CardRecognition.d.ets |
| API废弃版本变更 | 类名：CallbackParam； API声明：cardType?: CardType; 差异内容：NA | 类名：CallbackParam； API声明：cardType?: CardType; 差异内容：19 | api/@hms.ai.CardRecognition.d.ets |
| API废弃版本变更 | 类名：CallbackParam； API声明：cardInfo?: Record<string, Record<string, string>>; 差异内容：NA | 类名：CallbackParam； API声明：cardInfo?: Record<string, Record<string, string>>; 差异内容：19 | api/@hms.ai.CardRecognition.d.ets |
| 删除错误码 | 类名：VisionImageAnalyzerController； API声明：on(type: 'cursorMoveInText', callback: Callback&lt;void&gt;): void; 差异内容：1013700002,401 | 类名：VisionImageAnalyzerController； API声明：on(type: 'cursorMoveInText', callback: Callback&lt;void&gt;): void; 差异内容：NA | api/@hms.ai.visionImageAnalyzer.d.ets |
| 删除错误码 | 类名：VisionImageAnalyzerController； API声明：off(type: 'cursorMoveInText', callback?: ErrorCallback): void; 差异内容：1013700002,401 | 类名：VisionImageAnalyzerController； API声明：off(type: 'cursorMoveInText', callback?: Callback&lt;void&gt;): void; 差异内容：NA | api/@hms.ai.visionImageAnalyzer.d.ets |
| 删除错误码 | 类名：VisionImageAnalyzerController； API声明：on(type: 'cursorMoveOutText', callback: Callback&lt;void&gt;): void; 差异内容：1013700002,401 | 类名：VisionImageAnalyzerController； API声明：on(type: 'cursorMoveOutText', callback: Callback&lt;void&gt;): void; 差异内容：NA | api/@hms.ai.visionImageAnalyzer.d.ets |
| 删除错误码 | 类名：VisionImageAnalyzerController； API声明：off(type: 'cursorMoveOutText', callback?: ErrorCallback): void; 差异内容：1013700002,401 | 类名：VisionImageAnalyzerController； API声明：off(type: 'cursorMoveOutText', callback?: Callback&lt;void&gt;): void; 差异内容：NA | api/@hms.ai.visionImageAnalyzer.d.ets |
| 新增API | NA | 类名：CardRecognition； API声明：onResult: Callback&lt;CardRecognitionResult&gt;; 差异内容：onResult: Callback&lt;CardRecognitionResult&gt;; | api/@hms.ai.CardRecognition.d.ets |
| 新增API | NA | 类名：global； API声明：declare interface CardRecognitionResult 差异内容：declare interface CardRecognitionResult | api/@hms.ai.CardRecognition.d.ets |
| 新增API | NA | 类名：CardRecognitionResult； API声明：code: number; 差异内容：code: number; | api/@hms.ai.CardRecognition.d.ets |
| 新增API | NA | 类名：CardRecognitionResult； API声明：cardType?: CardType; 差异内容：cardType?: CardType; | api/@hms.ai.CardRecognition.d.ets |
| 新增API | NA | 类名：CardRecognitionResult； API声明：cardInfo?: Record<string, Record<string, string>>; 差异内容：cardInfo?: Record<string, Record<string, string>>; | api/@hms.ai.CardRecognition.d.ets |
| 函数变更 | 类名：VisionImageAnalyzerController； API声明：off(type: 'cursorMoveInText', callback?: ErrorCallback): void; 差异内容：callback?: ErrorCallback | 类名：VisionImageAnalyzerController； API声明：off(type: 'cursorMoveInText', callback?: Callback&lt;void&gt;): void; 差异内容：callback?: Callback&lt;void&gt; | api/@hms.ai.visionImageAnalyzer.d.ets |
| 函数变更 | 类名：VisionImageAnalyzerController； API声明：off(type: 'cursorMoveOutText', callback?: ErrorCallback): void; 差异内容：callback?: ErrorCallback | 类名：VisionImageAnalyzerController； API声明：off(type: 'cursorMoveOutText', callback?: Callback&lt;void&gt;): void; 差异内容：callback?: Callback&lt;void&gt; | api/@hms.ai.visionImageAnalyzer.d.ets |
