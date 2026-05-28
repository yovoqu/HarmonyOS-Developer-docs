# Image Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-imagekit-b112

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：ImagePacker； API声明：packing(source: ImageSource, option: PackingOption, callback: AsyncCallback&lt;ArrayBuffer&gt;): void; 差异内容：NA | 类名：ImagePacker； API声明：packing(source: ImageSource, option: PackingOption, callback: AsyncCallback&lt;ArrayBuffer&gt;): void; 差异内容：13 | api/@ohos.multimedia.image.d.ts |
| API废弃版本变更 | 类名：ImagePacker； API声明：packing(source: ImageSource, option: PackingOption): Promise&lt;ArrayBuffer&gt;; 差异内容：NA | 类名：ImagePacker； API声明：packing(source: ImageSource, option: PackingOption): Promise&lt;ArrayBuffer&gt;; 差异内容：13 | api/@ohos.multimedia.image.d.ts |
| API废弃版本变更 | 类名：ImagePacker； API声明：packing(source: PixelMap, option: PackingOption, callback: AsyncCallback&lt;ArrayBuffer&gt;): void; 差异内容：NA | 类名：ImagePacker； API声明：packing(source: PixelMap, option: PackingOption, callback: AsyncCallback&lt;ArrayBuffer&gt;): void; 差异内容：13 | api/@ohos.multimedia.image.d.ts |
| API废弃版本变更 | 类名：ImagePacker； API声明：packing(source: PixelMap, option: PackingOption): Promise&lt;ArrayBuffer&gt;; 差异内容：NA | 类名：ImagePacker； API声明：packing(source: PixelMap, option: PackingOption): Promise&lt;ArrayBuffer&gt;; 差异内容：13 | api/@ohos.multimedia.image.d.ts |
| 错误码变更 | 类名：ImagePacker； API声明：packToFile(source: ImageSource, fd: number, options: PackingOption, callback: AsyncCallback&lt;void&gt;): void; 差异内容：NA | 类名：ImagePacker； API声明：packToFile(source: ImageSource, fd: number, options: PackingOption, callback: AsyncCallback&lt;void&gt;): void; 差异内容：62980096,62980101,62980106,62980113,62980115,62980119,62980120,62980172,62980252 | api/@ohos.multimedia.image.d.ts |
| 错误码变更 | 类名：ImagePacker； API声明：packToFile(source: ImageSource, fd: number, options: PackingOption): Promise&lt;void&gt;; 差异内容：NA | 类名：ImagePacker； API声明：packToFile(source: ImageSource, fd: number, options: PackingOption): Promise&lt;void&gt;; 差异内容：62980096,62980101,62980106,62980113,62980115,62980119,62980120,62980172,62980252 | api/@ohos.multimedia.image.d.ts |
| 错误码变更 | 类名：ImagePacker； API声明：packToFile(source: PixelMap, fd: number, options: PackingOption, callback: AsyncCallback&lt;void&gt;): void; 差异内容：NA | 类名：ImagePacker； API声明：packToFile(source: PixelMap, fd: number, options: PackingOption, callback: AsyncCallback&lt;void&gt;): void; 差异内容：62980096,62980101,62980106,62980113,62980115,62980119,62980120,62980172,62980252 | api/@ohos.multimedia.image.d.ts |
| 错误码变更 | 类名：ImagePacker； API声明：packToFile(source: PixelMap, fd: number, options: PackingOption): Promise&lt;void&gt;; 差异内容：NA | 类名：ImagePacker； API声明：packToFile(source: PixelMap, fd: number, options: PackingOption): Promise&lt;void&gt;; 差异内容：62980096,62980101,62980106,62980113,62980115,62980119,62980120,62980172,62980252 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImagePacker； API声明：packToData(source: ImageSource, options: PackingOption): Promise&lt;ArrayBuffer&gt;; 差异内容：packToData(source: ImageSource, options: PackingOption): Promise&lt;ArrayBuffer&gt;; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImagePacker； API声明：packToData(source: PixelMap, options: PackingOption): Promise&lt;ArrayBuffer&gt;; 差异内容：packToData(source: PixelMap, options: PackingOption): Promise&lt;ArrayBuffer&gt;; | api/@ohos.multimedia.image.d.ts |
| 删除API | 类名：image； API声明： interface PackingOptionsForSequence 差异内容： interface PackingOptionsForSequence | NA | api/@ohos.multimedia.image.d.ts |
| 删除API | 类名：PackingOptionsForSequence； API声明：frameCount: number; 差异内容：frameCount: number; | NA | api/@ohos.multimedia.image.d.ts |
| 删除API | 类名：PackingOptionsForSequence； API声明：delayTimeList: Array&lt;number&gt;; 差异内容：delayTimeList: Array&lt;number&gt;; | NA | api/@ohos.multimedia.image.d.ts |
| 删除API | 类名：PackingOptionsForSequence； API声明：disposalTypes?: Array&lt;number&gt;; 差异内容：disposalTypes?: Array&lt;number&gt;; | NA | api/@ohos.multimedia.image.d.ts |
| 删除API | 类名：PackingOptionsForSequence； API声明：loopCount?: number; 差异内容：loopCount?: number; | NA | api/@ohos.multimedia.image.d.ts |
| 删除API | 类名：ImagePacker； API声明：packing(pixelmapSequence: Array&lt;PixelMap&gt;, options: PackingOptionsForSequence): Promise&lt;ArrayBuffer&gt;; 差异内容：packing(pixelmapSequence: Array&lt;PixelMap&gt;, options: PackingOptionsForSequence): Promise&lt;ArrayBuffer&gt;; | NA | api/@ohos.multimedia.image.d.ts |
| 删除API | 类名：ImagePacker； API声明：packToFile(pixelmapSequence: Array&lt;PixelMap&gt;, fd: number, options: PackingOptionsForSequence): Promise&lt;void&gt;; 差异内容：packToFile(pixelmapSequence: Array&lt;PixelMap&gt;, fd: number, options: PackingOptionsForSequence): Promise&lt;void&gt;; | NA | api/@ohos.multimedia.image.d.ts |
