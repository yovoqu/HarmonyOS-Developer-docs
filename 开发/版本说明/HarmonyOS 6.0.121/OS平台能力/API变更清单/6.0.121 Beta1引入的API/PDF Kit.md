# PDF Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-pdfkit-6011

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：pdfService； API声明：export interface SearchResultData 差异内容：export interface SearchResultData | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：SearchResultData； API声明：pageIndex: number; 差异内容：pageIndex: number; | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：SearchResultData； API声明：rects: PdfRect[]; 差异内容：rects: PdfRect[]; | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：SearchResultData； API声明：contextString: string; 差异内容：contextString: string; | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：pdfService； API声明：export interface SearchOptions 差异内容：export interface SearchOptions | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：SearchOptions； API声明：startIndex?: number; 差异内容：startIndex?: number; | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：SearchOptions； API声明：endIndex?: number; 差异内容：endIndex?: number; | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：SearchOptions； API声明：isMatchWholeWord?: boolean; 差异内容：isMatchWholeWord?: boolean; | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：SearchOptions； API声明：isMatchCase?: boolean; 差异内容：isMatchCase?: boolean; | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：SearchOptions； API声明：contextStringLength?: number; 差异内容：contextStringLength?: number; | api/@hms.officeservice.pdfservice.d.ts |
| 新增API | NA | 类名：pdfService； API声明：export type SearchKeyCallback = (results: SearchResultData[]) => boolean; 差异内容：export type SearchKeyCallback = (results: SearchResultData[]) => boolean; | api/@hms.officeservice.pdfservice.d.ts |
| 类新增必选属性或非同名方法 | 类名：global； API声明： 差异内容：NA | 类名：PdfDocument； API声明：searchKey(text: string, listener: SearchKeyCallback, options?: SearchOptions): Promise&lt;void&gt;; 差异内容：searchKey(text: string, listener: SearchKeyCallback, options?: SearchOptions): Promise&lt;void&gt;; | api/@hms.officeservice.pdfservice.d.ts |
