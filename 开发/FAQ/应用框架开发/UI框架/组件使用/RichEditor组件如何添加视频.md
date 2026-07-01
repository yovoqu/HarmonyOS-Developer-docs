# RichEditor组件如何添加视频

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1175

## RichEditor组件如何添加视频
 


##### 问题现象

RichEditor组件是否可以添加视频，如何添加？
 
 

##### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/hLwGCN0MQ6SVbWKrQ8yc1w/zh-cn_image_0000002628569784.png?HW-CC-KV=V1&HW-CC-Date=20260701T025603Z&HW-CC-Expire=86400&HW-CC-Sign=D313305A56F62C1E061EEE767F5A5EF464B685D2C6596296266453AFED561993)

 
 

##### 背景知识

- [RichEditor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor)组件提供了[addBuilderSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#addbuilderspan11)接口用于添加用户自定义布局Span。
- [Video](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-media-components-video#video-1)：用于播放视频文件并控制其播放状态的组件。

 
 

##### 解决方案

- 配置Video组件相关参数。
- 使用addBuilderSpan接口将Video组件添加至文本框中。
```text
@Entry
@Component
struct VideoDemo {
  controller: RichEditorController = new RichEditorController();
  option: RichEditorOptions = { controller: this.controller };
  private my_offset: number | undefined = undefined;
  private my_builder: CustomBuilder = undefined;

  @Builder
  placeholderBuilder() {
    Row({ space: 2 }) {
      // 配置Video组件各项参数
      Video({
        src: $rawfile('video-v8.mp4'), // 根据场景需要添加视频
        previewUri: $r('app.media.background'), // 视频未播放时的预览图片路径
        currentProgressRate: PlaybackSpeed.Speed_Forward_1_00_X, // 视频播放倍速
        controller: new VideoController() // 设置视频控制器，可以控制视频的播放状态
      }).width('100%');
    }

    .width('100%')
    .height(250)
    .borderRadius(10)
  }

  build() {
    Column() {
      Column() {
        RichEditor(this.option)
          .width('100%')
          .padding(-16);

        Row() {
          Button('builder1')
            .margin({ bottom: 15, top: 15 })
            .onClick(() => {
              this.my_builder = () => {
                this.placeholderBuilder();
              };
            });
        };

        Button('add span')
          .onClick(() => {
            // 使用addBuilderSpan接口将Video组件添加到文本框中
            let num = this.controller.addBuilderSpan(this.my_builder, { offset: this.my_offset });
            console.info('addBuilderSpan return ' + num);
          });
      }
      .width('100%')
      .height('70%');
    }
    .width('100%');
  }
}
```
