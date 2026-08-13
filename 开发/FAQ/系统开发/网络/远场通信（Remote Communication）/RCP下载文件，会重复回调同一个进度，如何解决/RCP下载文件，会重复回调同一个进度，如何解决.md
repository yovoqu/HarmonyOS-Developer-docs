# RCP下载文件，会重复回调同一个进度，如何解决

更新时间：2026-08-13 01:23:38

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-remote-communication-13

#### 问题现象

使用RCP接口下载文件，onDownloadProgress会重复回调同一个进度，导致业务逻辑重复执行。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/UGBRbAeHR9SMgcqhPcymbg/zh-cn_image_0000002628612488.png?HW-CC-KV=V1&HW-CC-Date=20260813T095610Z&HW-CC-Expire=86400&HW-CC-Sign=B1401FBCB7C110A188D149112BC798A809A055D4E9E5D923CEF3117A3F8F9D70)

 
 

#### 背景知识

- 通过[downloadToFile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-rcp#downloadtofile)接口下载文件，会在[onDownloadProgress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-rcp#ondownloadprogress)回调中返回当前下载进度，该接口需要配置ohos.permission.INTERNET权限，如果使用[PathPreference](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-rcp#pathpreference)的'cellular'模式，则额外需要ohos.permission.GET_NETWORK_INFO权限。
- [onHeaderReceive](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-rcp#onheaderreceive)回调中可以通过content-length获取下载文件的总长度。
- [onDataReceive](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-rcp#ondatareceive)回调可以获取到当前返回内容的长度。

 
 

#### 解决方案

- **方案一**：5.0系统版本，onDownloadProgress存在冗余回调bug，5.1及以上系统版本已经修复该问题，可升级系统至5.1以上版本。
- **方案二**：业务侧可通过文件总大小和当前已接收的文件大小计算下载进度：

  
```json
import rcp from '@hms.collaboration.rcp';

@Entry
@Component
struct Index {
  @State curValue: number = 0;
  @State totalData: number = 0;
  @State progress: number = 0;
  @State enableDownload: boolean = true;
 <em> // 需要替换成实际的url</em>
  downloadUrl: string = '';

  build() {
    Column({ space: 20 }) {
      Progress({ value: this.curValue, total: this.totalData, type: ProgressType.Capsule })
        .width(200)
        .height(40)
        .style({ enableSmoothEffect: true, content: this.progress.toFixed(2) + '%' });

      Button('点击开始下载')
        .onClick(() => {
          this.enableDownload = false;
          this.curValue = 0;
          this.progress = 0;
     <em>     // 下载文件数据</em>
          this.startDownload(this.downloadUrl);
        })
        .enabled(this.enableDownload);
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%');
  }

 <em> // 下载文件</em>
  startDownload(url: string) {
   <em> // 响应数据处理</em>
    const eventsHandler: rcp.HttpEventsHandler = {
      onHeaderReceive: (headers: rcp.ResponseHeaders) => {
        this.totalData = Number(headers['content-length']);
      },
      onDataReceive: (incomingData: ArrayBuffer) => {
        this.curValue += incomingData.byteLength;
        this.progress = (this.curValue / this.totalData) * 100;
        console.info('Download progress:', this.curValue, 'of', this.totalData);
      },
    <em>  // 数据完成接收监听</em>
      onDataEnd: () => {
        console.info('Data transfer complete');
        this.enableDownload = true;
      },
    <em>  // 取消数据接收监听</em>
      onCanceled: () => {
        console.info('Request/response canceled');
      },
    };
   <em> // 建立session对象</em>
    let session = rcp.createSession({
      requestConfiguration: {
        tracing: {
          verbose: true,
          collectTimeInfo: true,
          httpEventsHandler: eventsHandler,
        }
      }
    });
    session.downloadToFile(url, {
      kind: 'file',
      file: `${this.getUIContext().getHostContext()?.filesDir}/test`,
    }).then((response) => {
      console.info(`Download result ${response.toJSON()}`);
      session.close();
    }).catch((err: Error) => {
      console.error(`${JSON.stringify(err)}`);
      session.close();
    });
  }
}
```
