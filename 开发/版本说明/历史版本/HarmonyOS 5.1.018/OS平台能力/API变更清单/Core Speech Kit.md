# Core Speech Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-corespeechkit-510

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：speechRecognizer； API声明：function createEngine(createEngineParams: CreateEngineParams, callback: AsyncCallback&lt;SpeechRecognitionEngine&gt;): void; 差异内容：NA | 类名：speechRecognizer； API声明：function createEngine(createEngineParams: CreateEngineParams, callback: AsyncCallback&lt;SpeechRecognitionEngine&gt;): void; 差异内容：1002200009 | api/@hms.ai.speechRecognizer.d.ts |
| 新增错误码 | 类名：speechRecognizer； API声明：function createEngine(createEngineParams: CreateEngineParams): Promise&lt;SpeechRecognitionEngine&gt;; 差异内容：NA | 类名：speechRecognizer； API声明：function createEngine(createEngineParams: CreateEngineParams): Promise&lt;SpeechRecognitionEngine&gt;; 差异内容：1002200009 | api/@hms.ai.speechRecognizer.d.ts |
| 新增错误码 | 类名：SpeechRecognitionEngine； API声明：listLanguages(params: LanguageQuery, callback: AsyncCallback<Array&lt;string&gt;>): void; 差异内容：NA | 类名：SpeechRecognitionEngine； API声明：listLanguages(params: LanguageQuery, callback: AsyncCallback<Array&lt;string&gt;>): void; 差异内容：1002200009 | api/@hms.ai.speechRecognizer.d.ts |
| 新增错误码 | 类名：SpeechRecognitionEngine； API声明：listLanguages(params: LanguageQuery): Promise<Array&lt;string&gt;>; 差异内容：NA | 类名：SpeechRecognitionEngine； API声明：listLanguages(params: LanguageQuery): Promise<Array&lt;string&gt;>; 差异内容：1002200009 | api/@hms.ai.speechRecognizer.d.ts |
