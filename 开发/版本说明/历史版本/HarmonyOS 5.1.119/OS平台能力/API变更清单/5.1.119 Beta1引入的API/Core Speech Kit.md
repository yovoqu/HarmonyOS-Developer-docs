# Core Speech Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-corespeechkit-5111

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：textToSpeech； API声明：function listVoices(queryParams: VoiceQuery): Promise<VoiceInfo[]>; 差异内容：function listVoices(queryParams: VoiceQuery): Promise<VoiceInfo[]>; | api/@hms.ai.textToSpeech.d.ts |
| 新增API | NA | 类名：textToSpeech； API声明：function downloadVoice(downloadParams: VoiceDownload, callback: AsyncCallback<DownloadResponse>): void; 差异内容：function downloadVoice(downloadParams: VoiceDownload, callback: AsyncCallback<DownloadResponse>): void; | api/@hms.ai.textToSpeech.d.ts |
| 新增API | NA | 类名：textToSpeech； API声明：type OnDataCallback = (requestId: string, audio: ArrayBuffer, response: SynthesisResponse) => void; 差异内容：type OnDataCallback = (requestId: string, audio: ArrayBuffer, response: SynthesisResponse) => void; | api/@hms.ai.textToSpeech.d.ts |
| 新增API | NA | 类名：textToSpeech； API声明：export interface VoiceDownload 差异内容：export interface VoiceDownload | api/@hms.ai.textToSpeech.d.ts |
| 新增API | NA | 类名：VoiceDownload； API声明：requestId: string; 差异内容：requestId: string; | api/@hms.ai.textToSpeech.d.ts |
| 新增API | NA | 类名：VoiceDownload； API声明：language: string; 差异内容：language: string; | api/@hms.ai.textToSpeech.d.ts |
| 新增API | NA | 类名：VoiceDownload； API声明：person: number; 差异内容：person: number; | api/@hms.ai.textToSpeech.d.ts |
| 新增API | NA | 类名：VoiceDownload； API声明：style: string; 差异内容：style: string; | api/@hms.ai.textToSpeech.d.ts |
| 新增API | NA | 类名：textToSpeech； API声明：export interface DownloadResponse 差异内容：export interface DownloadResponse | api/@hms.ai.textToSpeech.d.ts |
| 新增API | NA | 类名：DownloadResponse； API声明：requestId: string; 差异内容：requestId: string; | api/@hms.ai.textToSpeech.d.ts |
| 新增API | NA | 类名：DownloadResponse； API声明：on(type: 'start', callback: Callback<string>): void; 差异内容：on(type: 'start', callback: Callback<string>): void; | api/@hms.ai.textToSpeech.d.ts |
| 新增API | NA | 类名：DownloadResponse； API声明：off(type: 'start', callback?: Callback<string>): void; 差异内容：off(type: 'start', callback?: Callback<string>): void; | api/@hms.ai.textToSpeech.d.ts |
| 新增API | NA | 类名：DownloadResponse； API声明：on(type: 'progress', callback: Callback<string>): void; 差异内容：on(type: 'progress', callback: Callback<string>): void; | api/@hms.ai.textToSpeech.d.ts |
| 新增API | NA | 类名：DownloadResponse； API声明：off(type: 'progress', callback?: Callback<string>): void; 差异内容：off(type: 'progress', callback?: Callback<string>): void; | api/@hms.ai.textToSpeech.d.ts |
| 新增API | NA | 类名：DownloadResponse； API声明：on(type: 'complete', callback: Callback<VoiceInfo>): void; 差异内容：on(type: 'complete', callback: Callback<VoiceInfo>): void; | api/@hms.ai.textToSpeech.d.ts |
| 新增API | NA | 类名：DownloadResponse； API声明：off(type: 'complete', callback?: Callback<VoiceInfo>): void; 差异内容：off(type: 'complete', callback?: Callback<VoiceInfo>): void; | api/@hms.ai.textToSpeech.d.ts |
| 新增API | NA | 类名：DownloadResponse； API声明：on(type: 'cancel', callback: Callback<string>): void; 差异内容：on(type: 'cancel', callback: Callback<string>): void; | api/@hms.ai.textToSpeech.d.ts |
| 新增API | NA | 类名：DownloadResponse； API声明：off(type: 'cancel', callback?: Callback<string>): void; 差异内容：off(type: 'cancel', callback?: Callback<string>): void; | api/@hms.ai.textToSpeech.d.ts |
| 新增API | NA | 类名：DownloadResponse； API声明：on(type: 'error', callback: ErrorCallback<BusinessError>): void; 差异内容：on(type: 'error', callback: ErrorCallback<BusinessError>): void; | api/@hms.ai.textToSpeech.d.ts |
| 新增API | NA | 类名：DownloadResponse； API声明：off(type: 'error', callback?: ErrorCallback<BusinessError>): void; 差异内容：off(type: 'error', callback?: ErrorCallback<BusinessError>): void; | api/@hms.ai.textToSpeech.d.ts |
| 函数变更 | 类名：SpeakListener； API声明：onData?: (requestId: string, audio: ArrayBuffer, response: SynthesisResponse) => void; 差异内容：(requestId: string, audio: ArrayBuffer, response: SynthesisResponse) => void | 类名：SpeakListener； API声明：onData?: OnDataCallback; 差异内容：OnDataCallback | api/@hms.ai.textToSpeech.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：VoiceInfo； API声明：status?: string; 差异内容：status?: string; | api/@hms.ai.textToSpeech.d.ts |
