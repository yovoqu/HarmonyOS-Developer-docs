# ReadPageComponent（阅读页组件）

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/reader-api-readpagecomponent
**支持设备：** Phone / PC/2in1 / Tablet

本模块提供ReadPageComponent组件，HarmonyOS应用通过集成该组件可快速构建书籍阅读功能。

**起始版本：** 5.0.4(16)


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet


```ts
import { ReadPageComponent } from '@kit.ReaderKit';
```


## ReadPageComponent
**支持设备：** Phone / PC/2in1 / Tablet

阅读页组件，支持对书籍排版内容的显示、多种翻页交互和翻页动效，以及翻页阅读过程中阅读器所需要的进度、行为感知能力。


**装饰器类型：** @Component

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.ReaderCore

**起始版本：** 5.0.4(16)

**参数：**


| 参数名 | 类型 | 装饰器类型 | 说明 |
| --- | --- | --- | --- |
| controller | [ReaderComponentController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/reader-read-core#readercomponentcontroller) | _ | ReadPageComponent控制器。 |
| readerCallback | AsyncCallback&lt;readerCore.[ReaderComponentController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/reader-read-core#readercomponentcontroller)&gt; | _ | 回调函数。 |


### build
**支持设备：** Phone / PC/2in1 / Tablet

build(): void

用于创建ReadPageComponent对象的构造函数。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.ReaderCore

**起始版本：** 5.0.4(16)

**示例：**


```ts
import { bookParser, readerCore, ReadPageComponent } from '@kit.ReaderKit';
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Reader {
  private readerComponentController: readerCore.ReaderComponentController = new readerCore.ReaderComponentController();

  aboutToAppear(): void {
    this.init();
  }

  private async init() {
    // 通过提前导入到应用沙箱目录中的书籍文件，初始化书籍解析器
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let filePath: string = `${context.filesDir}/abc.epub`;
    let bookParserHandler: bookParser.BookParserHandler = await bookParser.getDefaultHandler(filePath);
    let spineList: bookParser.SpineItem[] = bookParserHandler.getSpineList();
    let spineIndex: number = spineList[0].index;
    let domPos: string = '';

    await this.readerComponentController.init(context);
    this.readerComponentController.registerBookParser(bookParserHandler);
    this.readerComponentController.startPlay(spineIndex || 0, domPos);
    hilog.info(0x0000, 'testTag', `startPlay succeeded`);
  }

  aboutToDisappear(): void {
    this.readerComponentController.releaseBook();
  }

  build() {
    Stack() {
      ReadPageComponent({
        controller: this.readerComponentController,
        readerCallback: (err: BusinessError, data: readerCore.ReaderComponentController) => {
          this.readerComponentController = data;
        }
      })
    }.width('100%').height('100%').onClick(() => {
      // 支持在此实现点击拉起菜单栏功能
    })
  }
}
```
