# Core Vision Kit

更新时间：2026-06-27 01:41:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-corevisionkit-7001

## Core Vision Kit
 
 
| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明：declare namespace imageSuperResolution 差异内容：declare namespace imageSuperResolution | api/@hms.ai.vision.imageSuperResolution.d.ts |
| 新增API | NA | 类名：imageSuperResolution； API声明：export class ISPResponse 差异内容：export class ISPResponse | api/@hms.ai.vision.imageSuperResolution.d.ts |
| 新增API | NA | 类名：ISPResponse； API声明：pixelMap: image.PixelMap; 差异内容：pixelMap: image.PixelMap; | api/@hms.ai.vision.imageSuperResolution.d.ts |
| 新增API | NA | 类名：imageSuperResolution； API声明：class ImageSRAnalyzer 差异内容：class ImageSRAnalyzer | api/@hms.ai.vision.imageSuperResolution.d.ts |
| 新增API | NA | 类名：ImageSRAnalyzer； API声明：public static create(): Promise&lt;ImageSRAnalyzer&gt;; 差异内容：public static create(): Promise&lt;ImageSRAnalyzer&gt;; | api/@hms.ai.vision.imageSuperResolution.d.ts |
| 新增API | NA | 类名：ImageSRAnalyzer； API声明：process(request: visionBase.Request): Promise&lt;ISPResponse&gt;; 差异内容：process(request: visionBase.Request): Promise&lt;ISPResponse&gt;; | api/@hms.ai.vision.imageSuperResolution.d.ts |
| 新增API | NA | 类名：ImageSRAnalyzer； API声明：destroy(): Promise&lt;void&gt;; 差异内容：destroy(): Promise&lt;void&gt;; | api/@hms.ai.vision.imageSuperResolution.d.ts |
| 新增API | NA | 类名：global； API声明：declare namespace textSearchImage 差异内容：declare namespace textSearchImage | api/@hms.ai.vision.textSearchImage.d.ts |
| 新增API | NA | 类名：textSearchImage； API声明：class ImageObject 差异内容：class ImageObject | api/@hms.ai.vision.textSearchImage.d.ts |
| 新增API | NA | 类名：ImageObject； API声明：imagePath: string; 差异内容：imagePath: string; | api/@hms.ai.vision.textSearchImage.d.ts |
| 新增API | NA | 类名：ImageObject； API声明：scope: string; 差异内容：scope: string; | api/@hms.ai.vision.textSearchImage.d.ts |
| 新增API | NA | 类名：ImageObject； API声明：similarity: number; 差异内容：similarity: number; | api/@hms.ai.vision.textSearchImage.d.ts |
| 新增API | NA | 类名：textSearchImage； API声明：function init(): Promise&lt;boolean&gt;; 差异内容：function init(): Promise&lt;boolean&gt;; | api/@hms.ai.vision.textSearchImage.d.ts |
| 新增API | NA | 类名：textSearchImage； API声明：function insertImage(imagePath: string, scope: string): Promise&lt;boolean&gt;; 差异内容：function insertImage(imagePath: string, scope: string): Promise&lt;boolean&gt;; | api/@hms.ai.vision.textSearchImage.d.ts |
| 新增API | NA | 类名：textSearchImage； API声明：function search(query: string, scope: string, topKey?: number): Promise<ImageObject[]>; 差异内容：function search(query: string, scope: string, topKey?: number): Promise<ImageObject[]>; | api/@hms.ai.vision.textSearchImage.d.ts |
| 新增API | NA | 类名：textSearchImage； API声明：function deleteImage(imagePath: string, scope: string): Promise&lt;boolean&gt;; 差异内容：function deleteImage(imagePath: string, scope: string): Promise&lt;boolean&gt;; | api/@hms.ai.vision.textSearchImage.d.ts |
| 新增API | NA | 类名：textSearchImage； API声明：function clearData(): Promise&lt;boolean&gt;; 差异内容：function clearData(): Promise&lt;boolean&gt;; | api/@hms.ai.vision.textSearchImage.d.ts |
| 新增API | NA | 类名：textSearchImage； API声明：function release(): Promise&lt;boolean&gt;; 差异内容：function release(): Promise&lt;boolean&gt;; | api/@hms.ai.vision.textSearchImage.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@hms.ai.vision.imageSuperResolution.d.ts 差异内容：CoreVisionKit | api/@hms.ai.vision.imageSuperResolution.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@hms.ai.vision.textSearchImage.d.ts 差异内容：CoreVisionKit | api/@hms.ai.vision.textSearchImage.d.ts |
