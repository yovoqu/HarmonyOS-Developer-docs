# 应用ArkTS侧如何通过代码手动控制H5中视频

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-184

#### 问题现象

H5网页集成到应用中，需要通过ArkTS控制H5中video视频播放暂停及倍速播放等，请问如何实现？
 
 

#### 背景知识

- H5中video组件，可以通过video.play()、video.pause()控制视频播放与暂停，通过video.playbackRate设置播放速率。
- [runJavaScript](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#runjavascript)：异步执行JavaScript脚本，并通过回调方式返回脚本执行的结果。应用侧可通过调用runJavaScript，在H5中执行video.play()、video.pause()等脚本控制视频播放/暂停。
- [mediaPlayGestureAccess](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-attributes#mediaplaygestureaccess9)：设置有声视频的自动播放是否需要用户手动点击，静音视频播放不受该接口管控。若是视频是有声视频，Webview需要配置此属性。

 
 

#### 解决方案
1. 对于有声视频，需为Web组件设置[mediaPlayGestureAccess](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-attributes#mediaplaygestureaccess9)属性。
2. 页面加载完成，通过元素选择器document.querySelector('video')获取页面video元素。
3. 应用侧设置暂停/播放/倍速播放按钮，通过[runJavaScript](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#runjavascript)函数，触发H5页面执行JavaScript脚本，控制video组件暂停与播放及倍速播放等。

  示例代码如下：
```text
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct VideoControlExample {
  private controller: webview.WebviewController = new webview.WebviewController();
  @State isPlaying: boolean = false;

  build() {
    Column() {
      <em>// Web组件加载视频页面</em>
      Web({
        src: '******', <em>// H5页面地址</em>
        controller: this.controller
      })
        <em>// 页面加载完成后初始化视频控制</em>
        .onPageEnd(() => {
          this.controller.runJavaScript(
            <em>// 获取页面video元素，并设置video.controls为false，设置video播放控件不显示</em>
            "window.videoElement = document.querySelector('video');"
              + "window.videoElement.controls = false;"
          );
        })
        .mediaPlayGestureAccess(false)  <em>// 允许有声视频用户手动点击播放</em>
        .fileAccess(true)
        .geolocationAccess(false)
        .width('100%')
        .height('85%')

      <em>// 播放/暂停控制按钮</em>
      Button(this.isPlaying ? '暂停' : '播放')
        .onClick(() => {
          this.isPlaying = !this.isPlaying;
          if (this.isPlaying) {
            this.controller.runJavaScript('window.videoElement.play();');
          } else {
            this.controller.runJavaScript('window.videoElement.pause();');
          }
        })
        .margin({top: 10})
        .width('90%')
        .height('5%')

      <em>// 倍速控制按钮组</em>
      Row() {
        Button('0.75x').onClick(() => this.setPlaybackSpeed(0.75))
        Button('1.0x').onClick(() => this.setPlaybackSpeed(1.0))
        Button('1.5x').onClick(() => this.setPlaybackSpeed(1.5))
      }
      .margin({top: 10})
    }
    .width('100%')
    .height('100%')
  }

  <em>// 倍速控制按钮触发</em>
  setPlaybackSpeed(speed: number) {
    const script = `document.querySelector('video').playbackRate = ${speed};`;
    this.controller.runJavaScript(
      script,
      (error, result) => {
        if (error) {
          console.info(`Speed set failed, error code: ${error.code}, error message: ${error.message}`);
        }
        if (result) {
          console.info(`Speed set success: ${speed}x`);
        }
      });
  }
}
```

 
 

#### 常见FAQ

Q：ArkTS侧如何设置H5中视频的播放控件不显示？
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/2-jcIQFtQk6gR18BHCjdjA/zh-cn_image_0000002628899170.png?HW-CC-KV=V1&HW-CC-Date=20260723T013353Z&HW-CC-Expire=86400&HW-CC-Sign=900058B63241CBA70B0F0EBC5F15C1A4F4ADFC4FB2DB1F16BDA28EE7AADA279A)

 
A：video的播放控件由controls属性进行控制，网页加载完成后，设置controls属性为false，播放控件就不会显示。示例代码：
 
```text
<em>// Web组件加载视频页面</em>
Web({
  src: '******', <em>// H5页面地址</em>
  controller: this.controller
})
  <em>// 页面加载完成后初始化视频控制</em>
  .onPageEnd(() => {
    this.controller.runJavaScript(
      <em>// 获取页面video元素，并设置video.controls为false，设置video播放控件不显示</em>
      "window.videoElement = document.querySelector('video');"
        + "window.videoElement.controls = false;"
    );
  })
```
