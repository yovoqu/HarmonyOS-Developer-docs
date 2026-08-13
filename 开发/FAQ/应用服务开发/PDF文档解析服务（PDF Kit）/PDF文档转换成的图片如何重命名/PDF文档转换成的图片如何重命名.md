# PDF文档转换成的图片如何重命名

更新时间：2026-08-12 10:47:00

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-pdf-8

#### 问题现象

调用convertToImage将PDF文档转换成的图片如何重命名？
 
 

#### 背景知识

- [convertToImage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pdf-arkts-pdfservice#converttoimage)：转换PDF文档为图片。
- [fs.renameSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileiorenamesync)：以同步方法重命名文件或目录。

 
 

#### 解决方案

convertToImage将PDF文档转换成图片，每一页对应一张图片，图片名称按数字顺序命名。此API不支持自定义生成的图片名，需要使用[@ohos.file.fs (文件管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs)的能力重命名图片。
 
以将生成的图片重命名为{{PDF文件名(不带后缀)}}_{{数字顺序}}.png为例，示例代码如下：
```json
import { common } from '@kit.AbilityKit';
import { fileIo as fs, ListFileOptions } from '@kit.CoreFileKit';
import { pdfService, pdfViewManager } from '@kit.PDFKit';

@Entry
@Component
struct PdfPreview {
  private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  @State filePath: string = '';

  aboutToAppear(): void {
    let dir: string = this.context.filesDir;
   <em> // 确保在工程目录src/main/resources/rawfile里存在test.pdf文档</em>
    this.filePath = dir + '/test.pdf';
    let res = fs.accessSync(this.filePath);
    if (!res) {
      let content: Uint8Array = this.context.resourceManager.getRawFileContentSync('rawfile/test.pdf');
      let fdSand: fs.File | null = null;
      try {
        fdSand =
          fs.openSync(this.filePath, fs.OpenMode.WRITE_ONLY | fs.OpenMode.CREATE | fs.OpenMode.TRUNC);
        fs.writeSync(fdSand.fd, content.buffer);
      } catch (e) {
        console.error('fs.openSync fdSand failed error is : ', JSON.stringify(e));
      } finally {
        if (fdSand !== null) {
          fs.closeSync(fdSand.fd);
        }
      }
    }
    (async () => {
      let loadResult: pdfService.ParseResult = await this.controller.loadDocument(this.filePath);
      console.log('loadResult is ', loadResult);
      if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
        this.controller.setPageZoom(1);
      }
    })();

  }

  build() {
    Column({ space: 5 }) {
      Row() {
        Button('生成图片并重命名').onClick(async () => {
        <em>  // 获取PDF文件名(不带后缀)，作为存放生成的图片的文件夹</em>
          let file: fs.File | null = null;
          try {
            file = fs.openSync(this.filePath, fs.OpenMode.READ_ONLY);
            let pdfFileNameWithoutSuf = file.name.slice(0, file.name.length - 4);
            let document = new pdfService.PdfDocument();
            let loadResult = document.loadDocument(this.filePath, '');
            if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
              let pdfImgDir: string = this.context.filesDir + '/' + pdfFileNameWithoutSuf;
              if (!fs.accessSync(pdfImgDir)) {
                fs.mkdirSync(pdfImgDir);
              }
              document.convertToImage(pdfImgDir, pdfService.ImageFormat.PNG);
             <em> // 生成图片后遍历出路径下所有图片</em>
              let listFileOption: ListFileOptions = {
                recursion: false,
                listNum: 0,
                filter: {
                  suffix: ['.png']
                }
              };
              let filenames = fs.listFileSync(pdfImgDir, listFileOption);
            <em>  // 获取图片原名，拼接好新名后调用fs.renameSync重命名图片</em>
              for (let i = 0; i < filenames.length; i++) {
                let oldDir = pdfImgDir + '/' + filenames[i];
                let curFile: fs.File | null = null;
                try {
                  curFile = fs.openSync(oldDir, fs.OpenMode.READ_ONLY);
                  let curFileName = curFile.name;
                  if (curFileName.indexOf(pdfFileNameWithoutSuf) < 0) {
                    let newDir = pdfImgDir + '/' + pdfFileNameWithoutSuf + '_' + curFileName;
                    fs.renameSync(oldDir, newDir);
                  }
                } catch (e) {
                  console.error('fs.openSync curFile failed error is : ', JSON.stringify(e));
                } finally {
                  if (curFile !== null) {
                    fs.closeSync(curFile.fd);
                  }
                }
              }
            }
          } catch (e) {
            console.error('fs.openSync file failed error is : ', JSON.stringify(e));
          } finally {
            if (file !== null) {
              fs.closeSync(file.fd);
            }
          }
        })
      }
      .height('10%')
    }
    .width('100%')
    .height('100%')
  }
}
```
 
 
可使用[Device File Browser](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-device-file-explorer#section165192211111)查看重命名效果：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/SGd1bOOQQoC0-gz4mOLGgA/zh-cn_image_0000002658793613.png?HW-CC-KV=V1&HW-CC-Date=20260813T095552Z&HW-CC-Expire=86400&HW-CC-Sign=E02E0840E349B17A1C223EBB108F12D6E7C1CBBE5988D58D4C0802670F3A2EA6)

> [!NOTE]
> convertToImage将PDF文档转换成图片是耗时任务，若PDF文件过大，需要放到子线程里执行。 若有多个PDF文件需要转图片，由于convertToImage生成的图片以数字顺序命名，若放在同一个目录下会存在图片文件覆盖问题，可以按PDF文件名新建目录存放生成的图片，重命名后再移动到同一个目录下。
