# 使用ArkWeb下载文件提示完成但文件为何为空

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-137

#### 问题现象

使用ArkWeb下载文件时，下载代理提示已下载完成，并且有实际下载内容，但是保存文件时为空。
 
```text
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri, picker } from '@kit.CoreFileKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  delegate: webview.WebDownloadDelegate = new webview.WebDownloadDelegate();

  build() {
    Column() {
      Button('setDownloadDelegate')
        .onClick(() => {
         <em> // 下载开始前通知给用户，用户需要在此接口中调用WebDownloadItem.start("xxx")并提供下载路径，否则下载会一直处于PENDING状态。</em>
          this.delegate.onBeforeDownload((webDownloadItem: webview.WebDownloadItem) => {
            console.info('EntryAbility: will start a download.');
            const documentSaveOptions = new picker.DocumentSaveOptions();
            documentSaveOptions.newFileNames =
              ['fileName_' + (new Date()).getTime() + '.txt'];
            documentSaveOptions.fileSuffixChoices = ['.txt'];
            let uris: Array<string> = [];
            let documentViewPicker = new picker.DocumentViewPicker();
            documentViewPicker.save(documentSaveOptions).then((documentSaveResult: Array<string>) => {
              uris = documentSaveResult;
              if (0 == uris.length) {
                return;
              }
              console.info(`EntryAbility: documentViewPicker.save to file succeed and uris are:${uris}`);
              webDownloadItem.start(uris[0].toString());
              console.info(`EntryAbility: download to ${uris[0].toString()}`);
            }).catch((err: BusinessError) => {
              console.error(`EntryAbility: Invoke documentViewPicker.save failed, code is ${err.code}, message is ${err.message}`);
            });
          });

          this.controller.setDownloadDelegate(this.delegate);
        });
      Button('startDownload')
        .onClick(() => {
          try {
            this.controller.startDownload('www.example.com');
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        });
      Web({ src: 'www.example.com', controller: this.controller });
    };
  }
}
```
 
日志打印下载完成：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/kJbZyg25QASBHQFyRLwZ_A/zh-cn_image_0000002659138403.png?HW-CC-KV=V1&HW-CC-Date=20260811T005839Z&HW-CC-Expire=86400&HW-CC-Sign=FA82D8D77415D0A74BC9CB6418674256E80A1AD01E8D696755B957220938DC1E)

 
实际下载文件为空：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/w9S2x46ITpOqFYW700zT7Q/zh-cn_image_0000002629059052.png?HW-CC-KV=V1&HW-CC-Date=20260811T005839Z&HW-CC-Expire=86400&HW-CC-Sign=7E6892C496B1193B1DAAAE55A7C3C2940DAB4DED114A6EDEB428641F410E7236)

 
 

#### 背景知识

- [监听页面触发的下载](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-download#监听页面触发的下载)：通过[setDownloadDelegate()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#setdownloaddelegate11)向Web组件注册一个DownloadDelegate来监听页面触发的下载任务。资源由Web组件进行下载，Web组件会通过DownloadDelegate将下载的进度通知给应用。
- [@ohos.file.picker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-picker)：选择器(Picker)是一个封装DocumentViewPicker、AudioViewPicker、PhotoViewPicker的API模块，具有选择与保存的能力。
- [DocumentSaveOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-picker#documentsaveoptions)：文档保存选项。DocumentSaveOptions是选择器(@ohos.file.picker)模块的核心配置类，用于定制文件保存操作的行为。

 
 

#### 问题定位

- 确认文件是否由webDownloadItem.start下载生成：1. 在picker选择器后打断点执行，发现在webDownloadItem.start执行之前，手机中已经生成文件。由此判断，此时文件并非由webDownloadItem.start下载，而是picker选择器创建的空文件。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/hwD9uWrdQdSHKpmp9IR63A/zh-cn_image_0000002659258355.png?HW-CC-KV=V1&HW-CC-Date=20260811T005839Z&HW-CC-Expire=86400&HW-CC-Sign=E47BFF231ADA27CB06A3F51BDB710A6163D2AA45A45C282751992194C25CEB53)


2. 添加URI转换const uri = new fileUri.FileUri\(uris\[0\]\);，文件下载成功。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/DMFHFeJuSzmvKGr_tHT4Dw/zh-cn_image_0000002628899136.png?HW-CC-KV=V1&HW-CC-Date=20260811T005839Z&HW-CC-Expire=86400&HW-CC-Sign=9034A867433389B5EC2301615141297D09C1592EBCBF43C40F46060FD96CEAFF)

- 验证非当前HAP包名的文件夹是否可以作为文件下载路径：选择非当前HAP包名的文件夹进行下载，此时文件无法下载。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/BKVgcbAHSP-sqm_PDLxH3g/zh-cn_image_0000002659138405.png?HW-CC-KV=V1&HW-CC-Date=20260811T005839Z&HW-CC-Expire=86400&HW-CC-Sign=42D6C3914C196E2B24A3E378DFCF7817FCCE3EF3AC257C43F028E2E2B15BFF56)


 
 

#### 分析结论

未设置picker选择器配置DocumentSaveOptions的pickerMode时，pickerMode = picker.DocumentPickerMode.DEFAULT，此时选择指定目录，会在目录下生成空文件，适合需要生成文件再进行数据写入的场景。
 
 

#### 修改建议

修改picker选择器配置DocumentSaveOptions的pickerMode文档保存选项为picker.DocumentPickerMode.DOWNLOAD，选择器自动返回当前HAP包名的文件夹。修改后代码如下：
 
```text
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri, picker } from '@kit.CoreFileKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  delegate: webview.WebDownloadDelegate = new webview.WebDownloadDelegate();

  build() {
    Column() {
      Button('setDownloadDelegate')
        .onClick(() => {
        <em>  // 下载开始前通知给用户，用户需要在此接口中调用WebDownloadItem.start("xxx")并提供下载路径，否则下载会一直处于PENDING状态。</em>
          this.delegate.onBeforeDownload((webDownloadItem: webview.WebDownloadItem) => {
            console.info('EntryAbility: will start a download.');
            const documentSaveOptions = new picker.DocumentSaveOptions();
           <em> // 修改pickerMode为DOWNLOAD，删除newFileNames和fileSuffixChoices，设置为DOWNLOAD时，配置的参数newFileNames和fileSuffixChoices将不会生效</em>
            documentSaveOptions.pickerMode = picker.DocumentPickerMode.DOWNLOAD;
            let uris: Array<string> = [];
            let documentViewPicker = new picker.DocumentViewPicker();
            documentViewPicker.save(documentSaveOptions).then((documentSaveResult: Array<string>) => {
            <em>  // 固定返回当前HAP包名的文件夹</em>
              uris = documentSaveResult;
              if (0 == uris.length) {
                return;
              }
              console.info(`EntryAbility: documentViewPicker.save to file succeed and uris are:${uris}`);

              const uriString = documentSaveResult[0];
              if (!uriString) {
                return;
              }
            <em>  // 添加文件路径转换</em>
              const uri = new fileUri.FileUri(uriString);
              webDownloadItem.start(uri.path + '/fileName_' + (new Date()).getTime() + '.txt');
              console.info(`EntryAbility: download to ${uri.path}`);
            }).catch((err: BusinessError) => {
              console.error(`EntryAbility: Invoke documentViewPicker.save failed, code is ${err.code}, message is ${err.message}`);
            });
          });

          this.controller.setDownloadDelegate(this.delegate);
        });
      Button('startDownload')
        .onClick(() => {
          try {
           <em> // 运行时需替换为实际的链接</em>
            this.controller.startDownload('XXX');
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        });
     <em> // 运行时需替换为实际的链接</em>
      Web({ src: 'XXX', controller: this.controller }).fileAccess(false).geolocationAccess(false);
    };
  }
}
```
 
 

#### 总结

使用选择器选择下载路径时，需要注意DocumentSaveOptions的pickerMode选项：
 
- pickerMode = picker.DocumentPickerMode.DEFAULT适用场景：选择指定目录，在目录下生成空文件，适合需要生成文件再进行数据写入的场景。
- pickerMode = picker.DocumentPickerMode.DOWNLOAD适用场景：固定返回当前HAP包名的文件夹路径，没有文件夹时自动创建，适合需要下载文件存放路径的场景。
