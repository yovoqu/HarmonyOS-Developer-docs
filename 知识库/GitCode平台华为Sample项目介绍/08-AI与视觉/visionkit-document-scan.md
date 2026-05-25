# visionkit-document-scan — 文档扫描

> 来源：https://gitcode.com/HarmonyOS_Samples/visionkit-sample-code-document-scan-demo-ark-ts  
> 语言：ArkTS | 版本要求：HarmonyOS 5.0.0+, DevEco 6.0.0+

## 项目简介

基于 Vision Kit 的文档扫描 Demo。扫描文档/表格，应用滤镜，裁剪，导出为 JPEG/PDF/Excel。

## 核心 API

| API | 用途 |
|-----|------|
| `DocumentScannerConfig` | 扫描配置（张数/类型/滤镜/保存格式） |
| `DocumentScanner({ scannerConfig, onResult })` | 文档扫描器组件 |
| `onResult` 回调 | 结果码 200=成功, -1=取消 |

## 配置项

- 最大拍摄张数：1~50
- 文档类型：DOC（文档）/ SHEET（表格）
- 滤镜：原图/黑白/增强
- 拍摄模式：自动/手动
- 导出格式：JPG / PDF / Excel

## 约束

不能被子组件或窗口遮挡；仅支持华为手机和平板。
