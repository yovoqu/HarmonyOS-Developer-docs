# setCurrentTime方法指定Video组件开始播放位置偶现其它帧闪烁的问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1221

#### 问题现象

进入一个页面时想让Video组件从一个指定的时间开始播放，比如第10秒，设置了参数this.controller.setCurrentTime(AppStorage.get('currentTime'),SeekMode.ClosestKeyframe)偶尔会出现定位不准，展示了视频第一帧的情况。已知在onStart中调用setCurrentTime一定会出现第一帧，在onPrepare中开始调用setCurrentTime偶尔会出现第一帧。是什么原因造成的该情况，如何避免？
 
问题代码示例参考如下：
 
```text
@Entry
@Component
struct VideoExamplePage {
  previewUri: Resource = $r('app.media.startIcon');
  curRate: PlaybackSpeed = PlaybackSpeed.Speed_Forward_1_00_X;
  isAutoPlay: boolean = true;
  showControls: boolean = true;
  controller: VideoController = new VideoController();
  @State totalTime: number = 0;

  build() {
    Column() {
      Video({
        src: $rawfile('videoTest.mp4'), <em>// 替换已有视频资源</em>
        currentProgressRate: this.curRate,
        controller: this.controller
      })
        .width('100%')
        .height(600)
        .autoPlay(this.isAutoPlay)
        .controls(this.showControls)
        .onPrepared((error?: DurationObject) => {
          if (error != undefined) {
            console.error(`onPrepared is ${error.duration}`);
            this.totalTime = error.duration;
            this.controller.setCurrentTime(10, SeekMode.Accurate); <em>// </em><em>从第十秒开始播放</em>
          }
        });
      Row() {
        Button('setTime')
          .onClick(() => {
            this.controller.setCurrentTime(10, SeekMode.Accurate); <em>// 精准跳转到视频的10s位置</em>
          })
          .margin(2);
      };
    };
  }
}

interface DurationObject {
  duration: number;
}
```
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/yjlbN-ovRH-ttrtEV6i_Jg/zh-cn_image_0000002658953229.gif?HW-CC-KV=V1&HW-CC-Date=20260701T041255Z&HW-CC-Expire=86400&HW-CC-Sign=874B8822678B2C766600ABD3F10AE81F5C9E0EC6D83F253EF61256FFED398B4A)

 
 

#### 背景知识

- [Video组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-media-components-video#video-1)中[onPrepared事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-media-components-video#onprepared)是视频准备完成时触发的事件，[onStart事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-media-components-video#onstart)是视频开始播放时触发的事件。
- [VideoController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-media-components-video#videocontroller)是Video组件的控制器，其中[setCurrentTime方法](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-media-components-video#setcurrenttime8)可以指定视频播放的进度位置，并指定跳转模式。

 
 

#### 问题定位

由于Video组件的跳转和播放都是在后台线程里进行，所以当视频自动播放时与跳转事件存在执行先后顺序的冲突。
 
 

#### 分析结论

视频的play播放和seek跳转都是在后台线程里进行，由于冲突导致定位跳转过程中会偶现原位置的下一帧图片。
 
 

#### 修改建议

取消自动播放，在onPrepare事件里先设置跳转，再进行播放，来代替[autoPlay(true)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-media-components-video#autoplay)自动播放。
 1. 设置autoPlay(true)修改为autoPlay(false)。
2. onPrepared事件修改参考如下：
```text
.onPrepared((error?: DurationObject) => {
  if (error != undefined) {
    console.info(`onPrepared is ${error.duration}`);
    this.totalTime = error.duration;
    this.controller.setCurrentTime(10, SeekMode.Accurate);<em> </em><em>// 从第十秒开始播放</em>
    this.controller.start();
  }
})
```

 
完整示例参考如下：
 
```text
@Entry
@Component
struct VideoExamplePage {
  previewUri: Resource = $r('app.media.startIcon');
  curRate: PlaybackSpeed = PlaybackSpeed.Speed_Forward_1_00_X;
  isAutoPlay: boolean = false;
  showControls: boolean = true;
  controller: VideoController = new VideoController();
  @State totalTime: number = 0;

  build() {
    Column() {
      Video({
        src: $rawfile('example.mp4'), <em>// 替换已有视频资源</em>
        currentProgressRate: this.curRate,
        controller: this.controller
      })
        .width('100%')
        .height(600)
        .controls(this.showControls)
        .onPrepared((error?: DurationObject) => {
          if (error != undefined) {
            console.info(`onPrepared is ${error.duration}`);
            this.totalTime = error.duration;
            this.controller.setCurrentTime(10, SeekMode.Accurate); <em>// 从第十秒开始播放</em>
            this.controller.start();
          }
        })
        .autoPlay(this.isAutoPlay);
      Row() {
        Button('setTime')
          .onClick(() => {
            this.controller.setCurrentTime(10, SeekMode.Accurate);<em> </em><em>// 精准跳转到视频的10s位置</em>
          })
          .margin(2);
      };
    };
  }
}

interface DurationObject {
  duration: number;
}
```
