# RCP下载进度监听

更新时间：2026-07-30 01:55:38

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-remote-communication-14

#### 问题现象

RCP进行文件下载时，如何对下载进度实时监听？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/JTiYw05CRq-LOP658KiVsA/zh-cn_image_0000002658851747.png?HW-CC-KV=V1&HW-CC-Date=20260811T005941Z&HW-CC-Expire=86400&HW-CC-Sign=8971879A078ABC55FBACDD6741575BBC4D1C83F6CA76A989B90B2BFD5F78CBF3)

 
 

#### 解决方案

使用[OnDownloadProgress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-rcp#ondownloadprogress)接口实时监听下载进度，回调函数会返回三个参数：
 
- totalSize：要下载文件的总大小（number类型）。
- transferredSize：已下载文件大小（number类型）。
- request：触发回调的HTTP请求。

 
以下为文件下载进度监听案例：
 
```text
import rcp from '@hms.collaboration.rcp';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct ProgressListen {
  @State progress: number = 0;
  downloadUrl: string = 'xxxxxxx'; <em>// 需更换为真实地址</em>
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  filePath = `${this.context.filesDir}/test.png`;

  build() {
    Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
      Column({ space: 16 }) {
        Button('下载文件').onClick(() => {
          this.getDownloadProgress(this.downloadUrl);
        });
        Column({ space: 16 }) {
          Flex({ justifyContent: FlexAlign.SpaceBetween }) {
            Text('downloadProgress');
            Text(this.progress.toFixed(2) + '%');
          };

          Progress({ value: 0, total: 100, type: ProgressType.Linear }).value(this.progress).color('#0A59F7');
        }.width('90%').height(50);
      };
    }
    .height('100%')
    .width('100%');
  }

  <em>// 下载文件监听进度</em>
  getDownloadProgress(url: string) {
    const customHttpEventsHandler: rcp.HttpEventsHandler = {
      onDownloadProgress: (totalSize: number, transferredSize: number) => {
        this.progress = transferredSize / totalSize * 100;
      },

     <em> // 数据完成接收监听</em>
      onDataEnd: () => {
        console.info('Data transfer complete');
      },

      <em>// 取消数据接收监听</em>
      onCanceled: () => {
        console.info('Request/response canceled');
      },
    };

   <em> // TracingConfiguration用于获取请求期间详细信息</em>
    const tracingConfig: rcp.TracingConfiguration = {
      verbose: true,
      collectTimeInfo: true,
      httpEventsHandler: customHttpEventsHandler,
    };

    let session = rcp.createSession({
      requestConfiguration: {
        tracing: tracingConfig
      }
    });

  <em>  // 下载文件</em>
    session.downloadToFile(url, { kind: 'file', file: this.filePath }).then(() => {
      session.close();
    }).catch(() => {
      session.close();
    });
  }
}
```
