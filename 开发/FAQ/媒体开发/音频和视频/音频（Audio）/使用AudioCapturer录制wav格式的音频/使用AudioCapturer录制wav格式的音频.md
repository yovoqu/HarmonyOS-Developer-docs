# 使用AudioCapturer录制wav格式的音频

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-54

#### 问题现象

使用AudioCapturer录制的是pcm格式的音频，无法直接播放，能否录制可以直接播放的音频？
 
 

#### 背景知识

[AudioCapturer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiocapturer)：用于音频输入的API，仅支持pcm格式，需要应用持续读取音频数据进行工作。应用可以在音频输出后添加数据处理，要求开发者具备音频处理的基础知识，适用于更专业、更多样化的媒体录制应用开发。
 
 

#### 解决方案

可以使用添加文件头的方法将pcm格式的音频数据封装成wav格式。wav格式的音频可以直接播放。
 1. 使用AudioCapturer录制音频：开发步骤及完整示例可以参考[使用AudioCapturer开发音频录制功能](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-audiocapturer-for-recording)。
2. 将录制的pcm文件转换成wav格式。通过对pcm文件添加文件头，封装成wav格式的音频文件，具体步骤可查看pcmToWav类。
 
完整示例参考如下：
 
```json
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { abilityAccessCtrl, common, Permissions } from '@kit.AbilityKit';
import { fileIo } from '@kit.CoreFileKit';

const TAG = 'AudioCapturerDemo';
const permissions: Permissions[] = ['ohos.permission.MICROPHONE'];

class Options {
  offset?: number;
  length?: number;
}

let audioCapturer: audio.AudioCapturer | undefined = undefined;
let audioStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000,<em> </em><em>// 采样率。</em>
  channels: audio.AudioChannel.CHANNEL_2, <em>// 通道。</em>
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, <em>// 采样格式。</em>
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW <em>// 编码格式。</em>
};
let audioCapturerInfo: audio.AudioCapturerInfo = {
  source: audio.SourceType.SOURCE_TYPE_MIC, <em>// </em><em>音源类型：Mic音频源。根据业务场景配置，参考SourceType。</em>
  capturerFlags: 0 <em>// </em><em>音频采集器标志。</em>
};
let audioCapturerOptions: audio.AudioCapturerOptions = {
  streamInfo: audioStreamInfo,
  capturerInfo: audioCapturerInfo
};
let file: fs.File;
let readDataCallback: Callback<ArrayBuffer>;

async function initArguments(context: common.UIAbilityContext) {
  let bufferSize: number = 0;
  let path = context.cacheDir;
  let filePath = path + '/StarWars10s-2C-48000-4SW.pcm';
  file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
  readDataCallback = (buffer: ArrayBuffer) => {
    let options: Options = {
      offset: bufferSize,
      length: buffer.byteLength
    };
    fs.writeSync(file.fd, buffer, options);
    bufferSize += buffer.byteLength;
  };
}

<em>// </em><em>初始化，创建实例，设置监听事件。</em>
async function init() {
  audio.createAudioCapturer(audioCapturerOptions, (err, capturer) => { <em>// 创建AudioCapturer实例。</em>
    if (err) {
      console.error(`Invoke createAudioCapturer failed, code is ${err.code}, message is ${err.message}`);
      return;
    }
    console.info(`${TAG}: create AudioCapturer success`);
    audioCapturer = capturer;
    if (audioCapturer !== undefined) {
      audioCapturer.on('readData', readDataCallback);
    }
  });
}

<em>// </em><em>开始一次音频采集。</em>
async function start() {
  if (audioCapturer !== undefined) {
    let stateGroup = [audio.AudioState.STATE_PREPARED, audio.AudioState.STATE_PAUSED, audio.AudioState.STATE_STOPPED];
    if (stateGroup.indexOf(audioCapturer.state.valueOf()) ===
      -1) {<em> </em><em>// 当且仅当状态为STATE_PREPARED、STATE_PAUSED和STATE_STOPPED之一时才能启动采集。</em>
      console.error(`${TAG}: start failed`);
      return;
    }

  <em>  // 启动采集。</em>
    audioCapturer.start((err: BusinessError) => {
      if (err) {
        console.error('Capturer start failed.');
      } else {
        console.info('Capturer start success.');
      }
    });
  }
}

<em>// </em><em>停止采集。</em>
async function stop() {
  if (audioCapturer !== undefined) {
  <em>  // 只有采集器状态为STATE_RUNNING或STATE_PAUSED的时候才可以停止。</em>
    if (audioCapturer.state.valueOf() !== audio.AudioState.STATE_RUNNING &&
      audioCapturer.state.valueOf() !== audio.AudioState.STATE_PAUSED) {
      console.info('Capturer is not running or paused');
      return;
    }

   <em> // 停止采集。</em>
    audioCapturer.stop((err: BusinessError) => {
      if (err) {
        console.error('Capturer stop failed.');
      } else {
        console.info('Capturer stop success.');
      }
    });
  }
}

<em>// </em><em>销毁实例，释放资源。</em>
async function release() {
  if (audioCapturer !== undefined) {
   <em> // 采集器状态不是STATE_RELEASED或STATE_NEW状态，才能release。</em>
    if (audioCapturer.state.valueOf() === audio.AudioState.STATE_RELEASED ||
      audioCapturer.state.valueOf() === audio.AudioState.STATE_NEW) {
      console.info('Capturer already released');
      return;
    }

  <em>  // 释放资源。</em>
    audioCapturer.release((err: BusinessError) => {
      if (err) {
        console.error('Capturer release failed.');
      } else {
        fs.closeSync(file);
        console.info('Capturer release success.');
      }
    });
  }
}

async function requestPermissions(permissions: Permissions[], context: common.UIAbilityContext): Promise<boolean> {
  let permissionGrant = true;
  let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
  await atManager.requestPermissionsFromUser(context, permissions)
    .then((data) => {
      let grantStatus: number[] = data.authResults;
      let length: number = grantStatus.length;
      for (let i = 0; i < length; i++) {
        if (grantStatus[i] === 0) {
          console.info(`Request ${permissions[i]} succeed`);
        } else {
          permissionGrant = false;
          console.info(`Request ${permissions[i]} rejected`);
        }
      }
    })
    .catch((err: BusinessError) => {
      permissionGrant = false;
      console.error(`Request permission failed, err: ${JSON.stringify(err)}`);
    });
  return permissionGrant;
}

@Entry
@Component
struct Index {
  private microphoneGranted: boolean = false;
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  private pcmTranslater = new pcmToWav(this.context);

  aboutToAppear(): void {
    requestPermissions(permissions, this.context).then((granted: boolean) => {
      this.microphoneGranted = granted;
      console.info(`Microphone Permission Granted ${this.microphoneGranted}`);
    });
  }

  build() {
    Scroll() {
      Column() {
        Row() {
          Column() {
            Text('初始化').fontColor(Color.Black).fontSize(16).margin({ top: 12 });
          }
          .backgroundColor(Color.White)
          .borderRadius(30)
          .width('45%')
          .height('25%')
          .margin({ right: 12, bottom: 12 })
          .onClick(async () => {
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
            initArguments(context);
            init();
          });

          Column() {
            Text('开始录制').fontColor(Color.Black).fontSize(16).margin({ top: 12 });
          }
          .backgroundColor(Color.White)
          .borderRadius(30)
          .width('45%')
          .height('25%')
          .margin({ bottom: 12 })
          .onClick(async () => {
            start();
          });
        };

        Row() {
          Column() {
            Text('停止录制').fontSize(16).margin({ top: 12 });
          }
          .id('audio_effect_manager_card')
          .backgroundColor(Color.White)
          .borderRadius(30)
          .width('45%')
          .height('25%')
          .margin({ right: 12, bottom: 12 })
          .onClick(async () => {
            stop();
          });

          Column() {
            Text('释放资源').fontColor(Color.Black).fontSize(16).margin({ top: 12 });
          }
          .backgroundColor(Color.White)
          .borderRadius(30)
          .width('45%')
          .height('25%')
          .margin({ bottom: 12 })
          .onClick(async () => {
            release();
          });
        }
        .padding(12);

        Button('PCM转码WAV')
          .width('100%')
          .onClick(async () => {
            let filepath = this.context.cacheDir + '/StarWars10s-2C-48000-4SW.pcm';
            await this.pcmTranslater.pcmTranslate(filepath);
          });
      }
      .height('100%')
      .width('100%')
      .backgroundColor('#F1F3F5');

    };
  }
}

interface WavHeader {
  riff: string,
  fileSize: number,
  wave: string,
  fmtChunkMarker: string,
  fmtSize: number,
  formatType: number,
  channels: number,
  sampleRate: number,
  byteRate: number,
  blockAlign: number,
  bitsPerSample: number,
  dataChunkMarker: string,
  dataSize: number
};

<em>// pcm</em><em>转wav工具类</em>
class pcmToWav {
  private context: Context;

  constructor(context: Context) {
    this.context = context;
  }

<em>  // wav文件需要的文件头</em>
  waveHeader: WavHeader = {
    riff: 'RIFF', <em>// "RIFF"</em>
    fileSize: 0, <em>// 文件大小减去8</em>
    wave: 'WAVE', <em>// ”WAVE“</em>
    fmtChunkMarker: 'fmt ', <em>// "fmt "</em>
    fmtSize: 16, <em>// 16</em>
    formatType: 1,<em> </em><em>// 1（表示PCM）</em>
    channels: 2,<em> </em><em>// 声道数</em>
    sampleRate: 48000,<em> </em><em>// 采样率</em>
    byteRate: 48000 * 2 * 2, <em>// 每秒字节数(SampleRate * Channels * BitsPerSample / 8)</em>
    blockAlign: 2 * 2,<em> </em><em>// 帧大小(channels * BitsPerSample / 8)</em>
    bitsPerSample: 16, <em>// 采样位数</em>
    dataChunkMarker: 'data', <em>// ”data“</em>
    dataSize: 0,<em> </em><em>// 数据大小</em>
  };

  setString(idx: number, str: string, view: DataView) {
    for (let i = 0; i < str.length; i++) {
      view.setInt8(idx++, str.charCodeAt(i));
    }
  }

 <em> /**</em>
<em>   * 为pcm文件封装wav头</em>
<em>   * @param pcmFilePath 保存录制的pcm数据的沙箱文件路径</em>
<em>   */</em>
  async pcmTranslate(pcmFilePath: string) {
  <em>  // 创建一个大小为44字节的缓冲区，用于存储wav文件的头部信息，再将其写入输出文件</em>
    let fileSize = 0;
    try {
      fileSize = fileIo.statSync(pcmFilePath).size;
    } catch (err) {
      console.error(`failed to get file size, ${JSON.stringify(err)}`);
    }
    this.waveHeader.fileSize = fileSize + 44 - 8;
    this.waveHeader.dataSize = fileSize;

    let idx: number = 0;
    let buffer: ArrayBuffer = new ArrayBuffer(44);
    let bufferView: DataView = new DataView(buffer);
   <em> // riff</em>
    this.setString(idx, this.waveHeader.riff, bufferView);
    idx += 4;
  <em>  // file size</em>
    bufferView.setInt32(idx, this.waveHeader.fileSize, true);
    idx += 4;
  <em>  // wave</em>
    this.setString(idx, this.waveHeader.wave, bufferView);
    idx += 4;
  <em>  // fmt</em>
    this.setString(idx, this.waveHeader.fmtChunkMarker, bufferView);
    idx += 4;
  <em>  // fmt size</em>
    bufferView.setInt32(idx, this.waveHeader.fmtSize, true);
    idx += 4;
 <em>   // format type</em>
    bufferView.setInt16(idx, this.waveHeader.formatType, true);
    idx += 2;
 <em>   // channels</em>
    bufferView.setInt16(idx, this.waveHeader.channels, true);
    idx += 2;
  <em>  // sample rate</em>
    bufferView.setInt32(idx, this.waveHeader.sampleRate, true);
    idx += 4;
   <em> // byte rate</em>
    bufferView.setInt32(idx, this.waveHeader.byteRate, true);
    idx += 4;
  <em>  // block align</em>
    bufferView.setInt16(idx, this.waveHeader.blockAlign, true);
    idx += 2;
  <em>  // bits per sample</em>
    bufferView.setInt16(idx, this.waveHeader.bitsPerSample, true);
    idx += 2;
  <em>  // data</em>
    this.setString(idx, this.waveHeader.dataChunkMarker, bufferView);
    idx += 4;
  <em>  // data size</em>
    bufferView.setInt32(idx, this.waveHeader.dataSize, true);

  <em>  // 将PCM数据从输入文件写入输出文件，使用fs.readSync读取输入文件的数据，并写入输出文件，直到读取完毕</em>
    let path = this.context.filesDir + '/output.wav'; <em>// output wav file path</em>
    let inputFile: fileIo.File | undefined;
    let outputFile: fileIo.File | undefined;
    try {
      inputFile = fileIo.openSync(pcmFilePath, fileIo.OpenMode.READ_ONLY);
      outputFile = fileIo.openSync(path, fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC | fileIo.OpenMode.WRITE_ONLY);
    <em>  // write wav header</em>
      fileIo.writeSync(outputFile.fd, buffer);
    <em>  // write pcm data</em>
      let readSize = 0;
      let readBuf = new ArrayBuffer(1024 * 1024);
      do {
        readSize = fileIo.readSync(inputFile.fd, readBuf);
        fileIo.writeSync(outputFile.fd, readBuf, { length: readSize });
      } while (readSize > 0);
    } catch (err) {
      console.error(`Failed to write file, ${JSON.stringify(err)}`);
    } finally {
      if (inputFile) {
        fileIo.closeSync(inputFile);
      }
      if (outputFile) {
        fileIo.closeSync(outputFile);
      }
    }
  }

}
```
