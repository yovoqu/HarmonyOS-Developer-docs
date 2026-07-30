# AVRecorder如何获取录制音频的Uint8Array数据

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-35

#### 问题现象

应用在聊天功能中，需要发送Uint8Array类型语音数据给对方，该如何实现？
 
 

#### 背景知识

- [AVRecorder](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-avrecorder-for-recording)：主要工作是捕获音频信号，接收视频信号，完成音视频编码并保存到文件中，帮助开发者轻松实现音视频录制功能。
- [fs.readSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fsreadsync)：以同步方法从文件读取数据到缓冲区。

 
 

#### 解决方案
1. 应用通过AVRecorder完成语音录制，将语音文件保存到应用沙箱中。
2. 语音录制结束后，通过[文件管理](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs)接口readSync，获取语音文件的arrayBuffer数据后，转换为Uint8Array数据。
 
完整示例参考如下：
 
```json
import { fileIo } from '@kit.CoreFileKit';
import { media } from '@kit.MediaKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

@Entry
@Component
struct Index {
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  private filesDir: string = this.context.filesDir;
  private avRecorder: media.AVRecorder | undefined = undefined;
  private curFile: fileIo.File | undefined = undefined;
  private avProfile: media.AVRecorderProfile = {
    audioBitrate: 100000, <em>// 音频比特率</em>
    audioChannels: 2, <em>// </em><em>音频声道数</em>
    audioCodec: media.CodecMimeType.AUDIO_AAC,<em> </em><em>// 音频编码格式，当前只支持aac</em>
    audioSampleRate: 48000, <em>// 音频采样率</em>
    fileFormat: media.ContainerFormatType.CFT_MPEG_4A, <em>// 封装格式，当前只支持m4a</em>
  };
  private avConfig: media.AVRecorderConfig = {
    audioSourceType: media.AudioSourceType.AUDIO_SOURCE_TYPE_MIC, <em>// </em><em>音频输入源，这里设置为麦克风</em>
    profile: this.avProfile,
    url: '',<em> </em><em>// 参考应用文件访问与管理开发示例新建并读写一个文件</em>
  };
  textTimerController: TextTimerController = new TextTimerController();

  build() {
    Row() {
      Column() {
        Text('按住说话')
          .fontSize(20)
          .fontWeight(FontWeight.Normal)
          .width(300)
          .height(40)
          .textAlign(TextAlign.Center)
          .backgroundColor(Color.Orange)
          .border({ radius: 20 }) <em>// </em><em>单指长按文本触发该手势事件</em>
          .gesture(
            LongPressGesture({ repeat: false })
              .onAction(async (event?: GestureEvent) => {
                console.info(`LongPressGesture onAction.${JSON.stringify(event)}`);
               <em> // 长按录音</em>
                await this.startRecordingProcess();
              }) <em>// </em><em>长按动作一结束触发</em>
              .onActionEnd(async () => {
                console.info(`LongPressGesture onActionEnd.`);
                await this.stopRecordingProcess();
              })
          );
      }
      .width('100%');
    }
    .height('100%');
  }

 <em> // 开始录制对应的流程</em>
  async startRecordingProcess() {
    try {
      if (this.avRecorder == undefined) {
        <em>// 1.创建录制实例</em>
        this.avRecorder = await media.createAVRecorder();
      }
      this.setAudioRecorderCallback();
     <em> // 2.获取录制文件fd赋予avConfig里的url；参考FilePicker文档</em>
      this.curFile = fileIo.openSync(this.filesDir + '/Audio_' + new Date().getTime() + '.mp4',
        fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
      this.avConfig.url = 'fd://' + this.curFile.fd;
    <em>  // 3.配置录制参数完成准备工作</em>
      await this.avRecorder.prepare(this.avConfig);
      <em>// 4.开始录制</em>
      this.textTimerController.start();
      await this.avRecorder.start();

    } catch (err) {
      console.info('startRecordingProcess' + JSON.stringify(err));
    }
  }

  <em>// </em><em>停止录制对应的流程</em>
  async stopRecordingProcess() {
    if (this.avRecorder != undefined) {
     <em> // 1. 停止录制</em>
      if (this.avRecorder.state === 'started'
        || this.avRecorder.state === 'paused') {<em> </em><em>// 仅在started或者paused状态下调用stop为合理状态切换</em>
        await this.avRecorder.stop();
      }
      await this.avRecorder.reset();
      this.textTimerController.reset();
    <em>  // 3.释放录制实例</em>
      await this.avRecorder.release();
     <em> // 转Uint8Array</em>
      let bytes: Uint8Array = this.stringToUint8Array(this.avConfig.url);
      console.info(`${bytes}`);
     <em> // 4.关闭录制文件fd</em>
      fileIo.closeSync(this.curFile);
      this.avRecorder = undefined;
    }
  }

  <em>// </em><em>注册audioRecorder回调函数</em>
  setAudioRecorderCallback() {
    if (this.avRecorder != undefined) {
     <em> // 状态机变化回调函数</em>
      this.avRecorder.on('stateChange', (state: media.AVRecorderState, reason: media.StateChangeReason) => {
        console.info(`AudioRecorder current state is ${state}`);
        console.info(`${reason}`);
      });
     <em> // 错误上报回调函数</em>
      this.avRecorder.on('error', (err: BusinessError) => {
        console.error(`AudioRecorder failed, code is ${err.code}, message is ${err.message}`);
      });
    }
  }

  stringToUint8Array(str: string): Uint8Array {
    let textEncoder = new util.TextEncoder();
    return textEncoder.encodeInto(str);
  }
}
```
