# Web组件加载视频时无法隐藏下载按钮怎么处理

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-138

#### 问题现象

正常情况下Web组件通过url加载视频时，默认会提供一个下载按钮：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/ZqD8cGz2RsywPYUmWABMAg/zh-cn_image_0000002629059054.png?HW-CC-KV=V1&HW-CC-Date=20260701T041336Z&HW-CC-Expire=86400&HW-CC-Sign=94A0AC362F767ACFCA52B4A60761B28FC5C553847D7580DCE89B23629B3794CC)

 
如上图所示。但是有些场景下并不希望视频被下载，如何实现隐藏下载按钮？
 
 

#### 背景知识

- [runJavaScript](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#runjavascript-1)：在当前显示页面的上下文中异步执行JavaScript脚本，脚本执行的结果将通过Promise方式返回。此方法必须在用户界面（UI）线程上使用，并且回调也将在用户界面（UI）线程上调用。
- [onPageEnd](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onpageend)：网页加载完成时触发该回调，且只在主frame触发，iframe或者frameset的内容加载时不会触发此回调。
- H5中video标签的controlsList属性提供了对video额外的控制，使开发者能够控制显示哪些video元素控件。controlsList属性接受一个空格分隔的字符串，每个字符串代表一个控件的名称。主要可以控制的选项包括：
nodownload：隐藏下载按钮。
- nofullscreen：隐藏全屏按钮。
- noremoteplayback：隐藏远程播放按钮。

 
 
 

#### 解决方案

Web组件没有直接的属性来控制下载按钮的隐藏，但是可以通过runJavaScript执行JS脚本来间接实现。具体方法如下：
 1. 在Web组件onPageEnd网页加载完成的回调中通过runJavaScript执行JS脚本，隐藏下载按钮。
2. JS脚本的实现原理如下：
通过document.querySelector()获取video对象。
3. 设置controlsList属性值为nodownload。
 
```text
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private webviewController: webview.WebviewController = new webview.WebviewController();
 <em> // 此处地址实际使用过程中替换为真实视频地址</em>
  private videoUrl: string = 'xx.xx.xx';
  private removeDownloadButtonScript: string = 'window.onload = function() {\n' +
    '    let video = document.querySelector(\'video[name="media"]\');\n' +
    '    if (video) {\n' +
    '        video.setAttribute(\'controlsList\', \'nodownload\');\n' +
    '    }\n' +
    '}';

  aboutToAppear(): void {
    window.getLastWindow(this.getUIContext().getHostContext()!, (err: BusinessError, windowClass) => {
      if (err.code) {
        console.error(`Failed to obtain the top window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      let systemBarProperties: window.SystemBarProperties = {
        statusBarContentColor: '#FFFFFF' <em>// 状态栏文字颜色</em>
      };
      windowClass.setWindowSystemBarProperties(systemBarProperties).then(() => {
        console.info('Succeeded in setting the system bar properties.');
      }).catch((err: BusinessError) => {
        console.error(`Failed to set systemBar properties. Cause code: ${err.code}, message: ${err.message}`);
      });
    });
  }

  build() {
    Column() {
      Web({
        src: this.videoUrl,
        controller: this.webviewController
      })
        .geolocationAccess(false)
        .fileAccess(false)
        .size({
          width: '100%'
        })
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
        .onPageEnd(() => {
          this.webviewController.runJavaScript(this.removeDownloadButtonScript).then((result: string) => {
            console.info(`result: ${result}`);
          }).catch((error: BusinessError) => {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          });
        });
    }
    .height('100%')
    .width('100%')
  }
}
```
