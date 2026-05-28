# 打开和保存PDF文档

更新时间：2026-04-28 03:31:56

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-pdfview-open

##### 场景介绍

通过加载本地路径的PDF文档，实现打开PDF文档的预览功能。当PDF文档做了批注等相关的信息时，可以使用保存功能。

和pdfService的打开和保存能力相同，具体区别查看pdfService的[打开和保存PDF文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-open-document)的场景介绍。



##### 接口说明

| 接口名 | 描述 |
| --- | --- |
| loadDocument(path: string, password?: string, initPageIndex?: number, onProgress?: Callback&lt;number&gt;): Promise<pdfService.ParseResult> | 加载PDF文档。 |
| saveDocument(path: string, onProgress?: Callback&lt;number&gt;): Promise&lt;number&gt; | 保存PDF文档，使用Promise异步回调。 |




##### 示例代码
1. 在aboutToAppear函数里面加载PDF文档。
2. 调用PdfView预览组件，渲染显示。
3. 在【savePdfDocument】按钮中调用saveDocument方法另存PDF文档。

```text
import { pdfService, PdfView, pdfViewManager } from '@kit.PDFKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct PdfPage {
  private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();
  private context = this.getUIContext().getHostContext() as Context;
  private loadResult: pdfService.ParseResult = pdfService.ParseResult.PARSE_ERROR_FORMAT;

  aboutToAppear(): void {
    // 确保在工程目录src/main/resources/resfile里存在input.pdf文档
    let filePath = this.context.resourceDir + '/input.pdf';
    (async () => {
      this.loadResult = await this.controller.loadDocument(filePath);
    })()
  }

  build() {
    Column() {
      // 保存Pdf文档
      Button('savePdfDocument').onClick(async () => {
        if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
          let savePath = this.context.filesDir + '/savePdfDocument.pdf';
          let result = await this.controller.saveDocument(savePath);
          hilog.info(0x0000, 'PdfPage', 'savePdfDocument %{public}s!', result ? 'success' : 'fail');
        }
      })
      PdfView({
        controller: this.controller,
        pageFit: pdfService.PageFit.FIT_WIDTH,
        showScroll: true
      })
        .id('pdfview_app_view')
        .layoutWeight(1);
    }
    .width('100%')
    .height('100%')
  }
}
```
