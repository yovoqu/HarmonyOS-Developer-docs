# ArkData

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkdata-b031

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 属性变更 | 类名：Asset； API声明：name: string \| undefined; 差异内容：string,undefined | 类名：Asset； API声明：name: string; 差异内容：string | api/@ohos.data.commonType.d.ts |
| 属性变更 | 类名：Asset； API声明：uri: string \| undefined; 差异内容：string,undefined | 类名：Asset； API声明：uri: string; 差异内容：string | api/@ohos.data.commonType.d.ts |
| 属性变更 | 类名：Asset； API声明：path: string \| undefined; 差异内容：string,undefined | 类名：Asset； API声明：path: string; 差异内容：string | api/@ohos.data.commonType.d.ts |
| 属性变更 | 类名：Asset； API声明：createTime: string \| undefined; 差异内容：string,undefined | 类名：Asset； API声明：createTime: string; 差异内容：string | api/@ohos.data.commonType.d.ts |
| 属性变更 | 类名：Asset； API声明：modifyTime: string \| undefined; 差异内容：string,undefined | 类名：Asset； API声明：modifyTime: string; 差异内容：string | api/@ohos.data.commonType.d.ts |
| 属性变更 | 类名：Asset； API声明：size: string \| undefined; 差异内容：string,undefined | 类名：Asset； API声明：size: string; 差异内容：string | api/@ohos.data.commonType.d.ts |
| 属性变更 | 类名：Asset； API声明：status?: AssetStatus \| undefined; 差异内容：AssetStatus,undefined | 类名：Asset； API声明：status?: AssetStatus; 差异内容：AssetStatus | api/@ohos.data.commonType.d.ts |
| 自定义类型变更 | 类名：unifiedDataChannel； API声明：type ValueType = number \| string \| image.PixelMap \| Want \| ArrayBuffer; 差异内容：number \| string \| image.PixelMap \| Want \| ArrayBuffer | 类名：unifiedDataChannel； API声明：type ValueType = number \| string \| boolean \| image.PixelMap \| Want \| ArrayBuffer \| object \| null \| undefined; 差异内容：number \| string \| boolean \| image.PixelMap \| Want \| ArrayBuffer \| object \| null \| undefined | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：StoreConfig； API声明：isReadOnly?: boolean; 差异内容：isReadOnly?: boolean; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore； API声明： interface SqlExecutionInfo 差异内容： interface SqlExecutionInfo | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SqlExecutionInfo； API声明：sql: Array&lt;string&gt;; 差异内容：sql: Array&lt;string&gt;; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SqlExecutionInfo； API声明：totalTime: number; 差异内容：totalTime: number; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SqlExecutionInfo； API声明：waitTime: number; 差异内容：waitTime: number; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SqlExecutionInfo； API声明：prepareTime: number; 差异内容：prepareTime: number; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SqlExecutionInfo； API声明：executeTime: number; 差异内容：executeTime: number; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RebuildType； API声明：REPAIRED 差异内容：REPAIRED | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore； API声明：on(event: 'statistics', observer: Callback&lt;SqlExecutionInfo&gt;): void; 差异内容：on(event: 'statistics', observer: Callback&lt;SqlExecutionInfo&gt;): void; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore； API声明：off(event: 'statistics', observer?: Callback&lt;SqlExecutionInfo&gt;): void; 差异内容：off(event: 'statistics', observer?: Callback&lt;SqlExecutionInfo&gt;): void; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：XHTML = 'general.xhtml' 差异内容：XHTML = 'general.xhtml' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：RSS = 'general.rss' 差异内容：RSS = 'general.rss' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：CSS = 'general.css' 差异内容：CSS = 'general.css' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：TEX = 'general.tex' 差异内容：TEX = 'general.tex' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：ASC_TEXT = 'general.asc-text' 差异内容：ASC_TEXT = 'general.asc-text' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：RICH_TEXT = 'general.rich-text' 差异内容：RICH_TEXT = 'general.rich-text' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：DELIMITED_VALUES_TEXT = 'general.delimited-values-text' 差异内容：DELIMITED_VALUES_TEXT = 'general.delimited-values-text' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：COMMA_SEPARATED_VALUES_TEXT = 'general.comma-separated-values-text' 差异内容：COMMA_SEPARATED_VALUES_TEXT = 'general.comma-separated-values-text' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：TAB_SEPARATED_VALUES_TEXT = 'general.tab-separated-values-text' 差异内容：TAB_SEPARATED_VALUES_TEXT = 'general.tab-separated-values-text' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：GIF = 'general.gif' 差异内容：GIF = 'general.gif' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：WORD_DOT = 'com.microsoft.word.dot' 差异内容：WORD_DOT = 'com.microsoft.word.dot' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：POWERPOINT_PPS = 'com.microsoft.powerpoint.pps' 差异内容：POWERPOINT_PPS = 'com.microsoft.powerpoint.pps' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：POWERPOINT_POT = 'com.microsoft.powerpoint.pot' 差异内容：POWERPOINT_POT = 'com.microsoft.powerpoint.pot' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：EXCEL_XLT = 'com.microsoft.excel.xlt' 差异内容：EXCEL_XLT = 'com.microsoft.excel.xlt' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：VISIO_VSD = 'com.microsoft.visio.vsd' 差异内容：VISIO_VSD = 'com.microsoft.visio.vsd' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：TS = 'general.ts' 差异内容：TS = 'general.ts' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：MPEGURL_VIDEO = 'general.mpegurl-video' 差异内容：MPEGURL_VIDEO = 'general.mpegurl-video' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：MATROSKA_VIDEO = 'org.matroska.mkv' 差异内容：MATROSKA_VIDEO = 'org.matroska.mkv' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：FLASH = 'com.adobe.flash' 差异内容：FLASH = 'com.adobe.flash' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：MPEGURL_AUDIO = 'general.mpegurl-audio' 差异内容：MPEGURL_AUDIO = 'general.mpegurl-audio' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：MPEG_4_AUDIO = 'general.mpeg-4-audio' 差异内容：MPEG_4_AUDIO = 'general.mpeg-4-audio' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：MP2 = 'general.mp2' 差异内容：MP2 = 'general.mp2' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：MPEG_AUDIO = 'general.mpeg-audio' 差异内容：MPEG_AUDIO = 'general.mpeg-audio' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：ULAW_AUDIO = 'general.ulaw-audio' 差异内容：ULAW_AUDIO = 'general.ulaw-audio' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：MATROSKA_AUDIO = 'org.matroska.mka' 差异内容：MATROSKA_AUDIO = 'org.matroska.mka' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：OPG = 'general.opg' 差异内容：OPG = 'general.opg' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：TAZ_ARCHIVE = 'general.taz-archive' 差异内容：TAZ_ARCHIVE = 'general.taz-archive' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：WEB_ARCHIVE = 'general.web-archive' 差异内容：WEB_ARCHIVE = 'general.web-archive' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：ISO = 'general.iso' 差异内容：ISO = 'general.iso' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：DRAWINGML_VISIO = 'org.openxmlformats.drawingml.visio' 差异内容：DRAWINGML_VISIO = 'org.openxmlformats.drawingml.visio' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：DRAWINGML_TEMPLATE = 'org.openxmlformats.drawingml.template' 差异内容：DRAWINGML_TEMPLATE = 'org.openxmlformats.drawingml.template' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：WORDPROCESSINGML_TEMPLATE = 'org.openxmlformats.wordprocessingml.template' 差异内容：WORDPROCESSINGML_TEMPLATE = 'org.openxmlformats.wordprocessingml.template' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：PRESENTATIONML_TEMPLATE = 'org.openxmlformats.presentationml.template' 差异内容：PRESENTATIONML_TEMPLATE = 'org.openxmlformats.presentationml.template' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：PRESENTATIONML_SLIDESHOW = 'org.openxmlformats.presentationml.slideshow' 差异内容：PRESENTATIONML_SLIDESHOW = 'org.openxmlformats.presentationml.slideshow' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：SPREADSHEETML_TEMPLATE = 'org.openxmlformats.spreadsheetml.template' 差异内容：SPREADSHEETML_TEMPLATE = 'org.openxmlformats.spreadsheetml.template' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：RAR_ARCHIVE = 'com.rarlab.rar-archive' 差异内容：RAR_ARCHIVE = 'com.rarlab.rar-archive' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：SEVEN_ZIP_ARCHIVE = 'org.7-zip.7-zip-archive' 差异内容：SEVEN_ZIP_ARCHIVE = 'org.7-zip.7-zip-archive' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：OFD = 'general.ofd' 差异内容：OFD = 'general.ofd' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：CAD = 'general.cad' 差异内容：CAD = 'general.cad' | api/@ohos.data.uniformTypeDescriptor.d.ts |
| 新增API | NA | 类名：UniformDataType； API声明：OCTET_STREAM = 'general.octet-stream' 差异内容：OCTET_STREAM = 'general.octet-stream' | api/@ohos.data.uniformTypeDescriptor.d.ts |
