# Class (PdfData)

更新时间：2026-04-28 03:31:56

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-pdfdata
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

PdfData类用于封装createPdf函数输出的数据流。
 
> [!NOTE]
> 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。 本Class首批接口从API version 14开始支持。 示例效果请以真机运行为准。 在网页生成PDF过程中，返回的是数据流，由PdfData类封装。

  

##### pdfArrayBuffer14+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

pdfArrayBuffer(): Uint8Array
 
获取网页生成的PDF数据流。完整示例代码参考[createPdf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#createpdf14)。
 
**系统能力：** SystemCapability.Web.Webview.Core
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Uint8Array | 数据流。 |
