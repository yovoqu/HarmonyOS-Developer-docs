# Vision Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-visionkit-b065

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 属性变更 | 类名：DocumentScanner； API声明：onResult: (code: number, saveType: SaveOption, uris: string[]) => void; 差异内容：(code: number, saveType: SaveOption, uris: string[]) => void | 类名：DocumentScanner； API声明：onResult: DocumentScannerResultCallback; 差异内容：DocumentScannerResultCallback | api/@hms.ai.DocumentScanner.d.ets |
| 新增API | NA | 类名：global； API声明：declare type DocumentScannerResultCallback = (code: number, saveType: SaveOption, uris: string[]) => void; 差异内容：declare type DocumentScannerResultCallback = (code: number, saveType: SaveOption, uris: string[]) => void; | api/@hms.ai.DocumentScanner.d.ets |
