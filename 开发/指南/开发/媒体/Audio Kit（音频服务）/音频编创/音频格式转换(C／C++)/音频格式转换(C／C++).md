# 音频格式转换(C/C++)

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-suite-format-converter

从API版本26.0.0开始，[AudioConverter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-audioconverter)给开发者提供PCM音频格式转换能力，在纯音频转码等场景下支持开发者使用格式转换接口将PCM（Pulse Code Modulation）音频数据从一种格式转换为另一种格式，包括采样率、声道布局、采样格式（位深）的转换。


#### 开发步骤

开发者使用[AudioConverter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-audioconverter)提供的PCM音频格式转换能力，添加对应的头文件。



#### 在CMake脚本中链接动态库

```text
target_link_libraries(sample PUBLIC libohaudiosuite.so)
```



#### 添加头文件

开发者通过引入头文件<[native_audio_converter.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-converter-h)>，使用音频格式转换相关API。

```text
#include <ohaudiosuite/native_audio_converter.h>
```

音频格式转换相关接口返回值请参考：[OH_AudioConverter_Result](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-converter-h#oh_audioconverter_result)。

详细的API说明请参考：[AudioConverter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-audioconverter)。

**功能特性**

格式转换器提供的核心功能如下所示：

 - 采样率转换：支持14种标准采样率之间的相互转换，包括8000Hz至192000Hz的常用采样率。
 - 声道布局转换：支持32种声道布局之间的转换，覆盖1-8声道的各种音频配置。如立体声转单声道、5.1环绕声转7.1环绕声等。
 - 采样格式转换：支持5种PCM采样格式之间的相互转换，包括8-bit无符号、16/24/32-bit有符号和32-bit浮点格式。


**使用限制**

 - 仅支持PCM格式的音频数据进行转换。
 - 回调数据大小限制：单次回调最多返回400KB数据，超出部分需要分多次返回。
 - 输出缓冲区容量：输出缓冲区容量必须至少能容纳一个完整音频帧（采样率 × 声道数 × 采样格式字节数）。
 - 数据流结束处理：当输入回调函数返回AUDIOCONVERTER_INPUT_DATA_FINISHED表示输入数据已经输入完成时，仍需要继续调用[OH_AudioConverter_Process()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-converter-h#oh_audioconverter_process)直到outputSize为0，以确保所有缓存的转换数据都被输出。
 - 数据指针有效性：回调函数返回的数据指针在[OH_AudioConverter_Process()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-converter-h#oh_audioconverter_process)返回前必须保持有效，不能在回调返回后立即释放。


**数据流处理流程**

格式转换器采用流式数据处理模式，完整的数据处理流程如下所示：
1. 初始化阶段。

  
 - 调用[OH_AudioConverter_Create()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-converter-h#oh_audioconverter_create)创建转换器实例。

2. 调用[OH_AudioConverter_SetInputCallback()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-converter-h#oh_audioconverter_setinputcallback)设置输入数据回调函数。

3. 数据输入阶段。

  
转换器内部维护输入数据缓存。

4. 当缓存数据不足时，转换器会自动调用回调函数请求更多数据。

5. 回调函数根据当前状态返回数据：         
AUDIOCONVERTER_INPUT_HAVE_DATA：有数据可用，返回本次提供的数据大小（必须大于0）。

6. AUDIOCONVERTER_INPUT_NO_AVAILABLE_DATA：暂无数据可用，返回0，转换器停止本次处理。

7. AUDIOCONVERTER_INPUT_DATA_FINISHED：数据流结束，返回0，转换器继续处理缓存数据。

8. 数据转换阶段。

  
转换器根据输入和输出格式计算需要的输入数据量。

9. 对输入数据进行重采样、声道转换、格式转换等操作。

10. 将转换后的数据存入输出缓存。

11. 数据输出阶段。

  
调用[OH_AudioConverter_Process()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-converter-h#oh_audioconverter_process)获取转换后的数据。

12. 每次调用返回的outputSize表示实际输出的数据大小。

13. 需要循环调用[OH_AudioConverter_Process()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-converter-h#oh_audioconverter_process)接口执行格式转换，直到outputSize为0，且输入回调函数返回AUDIOCONVERTER_INPUT_DATA_FINISHED状态，确保所有缓存的转换数据都被输出。

14. 清理阶段。

  
调用[OH_AudioConverter_Destroy()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-converter-h#oh_audioconverter_destroy)销毁转换器实例。

15. 释放所有相关资源。

  **支持的音频格式**

  格式转换接口支持以下PCM音频格式：

  
采样率：[SAMPLE_RATE_8000](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-suite-base-h#oh_audio_samplerate)、[SAMPLE_RATE_11025](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-suite-base-h#oh_audio_samplerate)、[SAMPLE_RATE_12000](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-suite-base-h#oh_audio_samplerate)、[SAMPLE_RATE_16000](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-suite-base-h#oh_audio_samplerate)、[SAMPLE_RATE_22050](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-suite-base-h#oh_audio_samplerate)、[SAMPLE_RATE_24000](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-suite-base-h#oh_audio_samplerate)、[SAMPLE_RATE_32000](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-suite-base-h#oh_audio_samplerate)、[SAMPLE_RATE_44100](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-suite-base-h#oh_audio_samplerate)、[SAMPLE_RATE_48000](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-suite-base-h#oh_audio_samplerate)、[SAMPLE_RATE_64000](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-suite-base-h#oh_audio_samplerate)、[SAMPLE_RATE_88200](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-suite-base-h#oh_audio_samplerate)、[SAMPLE_RATE_96000](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-suite-base-h#oh_audio_samplerate)、[SAMPLE_RATE_176400](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-suite-base-h#oh_audio_samplerate)、[SAMPLE_RATE_192000](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-suite-base-h#oh_audio_samplerate)。
 - 声道布局：[CH_LAYOUT_MONO](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout)、[CH_LAYOUT_STEREO](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout)、[CH_LAYOUT_STEREO_DOWNMIX](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout)、[CH_LAYOUT_2POINT1](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout)、[CH_LAYOUT_3POINT0](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout)、[CH_LAYOUT_SURROUND](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout)、[CH_LAYOUT_3POINT1](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout)、[CH_LAYOUT_4POINT0](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout)、[CH_LAYOUT_QUAD_SIDE](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout)、[CH_LAYOUT_QUAD](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout)、[CH_LAYOUT_2POINT0POINT2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout)、[CH_LAYOUT_4POINT1](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout)、[CH_LAYOUT_5POINT0](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout)、[CH_LAYOUT_5POINT0_BACK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout)、[CH_LAYOUT_2POINT1POINT2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout)、[CH_LAYOUT_3POINT0POINT2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout)、[CH_LAYOUT_5POINT1](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout)、[CH_LAYOUT_5POINT1_BACK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout)、[CH_LAYOUT_6POINT0](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout)、[CH_LAYOUT_3POINT1POINT2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout)、[CH_LAYOUT_6POINT0_FRONT](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout)、[CH_LAYOUT_HEXAGONAL](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout)、[CH_LAYOUT_6POINT1](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout)、[CH_LAYOUT_6POINT1_BACK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout)、[CH_LAYOUT_6POINT1_FRONT](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout)、[CH_LAYOUT_7POINT0](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout)、[CH_LAYOUT_7POINT0_FRONT](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout)、[CH_LAYOUT_7POINT1](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout)、[CH_LAYOUT_OCTAGONAL](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout)、[CH_LAYOUT_5POINT1POINT2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout)、[CH_LAYOUT_7POINT1_WIDE](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout)、[CH_LAYOUT_7POINT1_WIDE_BACK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout)。
 - 采样格式：[AUDIO_SAMPLE_U8](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-suite-base-h#oh_audio_sampleformat)、[AUDIO_SAMPLE_S16LE](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-suite-base-h#oh_audio_sampleformat)、[AUDIO_SAMPLE_S24LE](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-suite-base-h#oh_audio_sampleformat)、[AUDIO_SAMPLE_S32LE](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-suite-base-h#oh_audio_sampleformat)、[AUDIO_SAMPLE_F32LE](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-suite-base-h#oh_audio_sampleformat)。




#### 创建格式转换器

```cpp
// 用户需按照实际情况设置输入格式。
OH_AudioConverter_Format inputFormat = {
    .encodingType = OH_Audio_EncodingType::AUDIO_ENCODING_TYPE_RAW,
    .samplingRate = OH_Audio_SampleRate::SAMPLE_RATE_48000,
    .channelLayout = OH_AudioChannelLayout::CH_LAYOUT_STEREO,
    .sampleFormat = OH_Audio_SampleFormat::AUDIO_SAMPLE_S16LE
};

// 用户需按照实际情况设置输出格式。
OH_AudioConverter_Format outputFormat = {
    .encodingType = OH_Audio_EncodingType::AUDIO_ENCODING_TYPE_RAW,
    .samplingRate = OH_Audio_SampleRate::SAMPLE_RATE_192000,
    .channelLayout = OH_AudioChannelLayout::CH_LAYOUT_6POINT0_FRONT,
    .sampleFormat = OH_Audio_SampleFormat::AUDIO_SAMPLE_S24LE
};

// 创建转换器。
OH_AudioConverter_Result result = OH_AudioConverter_Create(&inputFormat, &outputFormat, &converter);
if (result != AUDIOCONVERTER_SUCCESS) {
    OH_LOG_Print(LOG_APP, LOG_ERROR, GLOBAL_RESMGR, TAG, "Failed to create converter: %{public}d", result);
    return false;
}
```



#### 设置输入数据回调函数

创建输入数据回调函数RequestDataCallback，函数类型为[OH_AudioConverter_RequestDataCallback()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-converter-h#oh_audioconverter_requestdatacallback)，调用[OH_AudioConverter_SetInputCallback()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-converter-h#oh_audioconverter_setinputcallback)接口设置回调函数。

输入数据回调函数。

```cpp
// 设置输出数据指针。
// 注意：数据指针的值并不一定要从userData中获取，也可以是存储数据的缓存地址。
// 例如：从文件中读取数据放入缓存，然后将该缓存地址赋值给输出数据指针。
// 只要确保数据指针在OH_AudioConverter_Process()返回前保持有效即可。
*outInputData = dataInfo->buffer + dataInfo->readDataOffset;

// 计算本次可提供的数据大小（单次回调最多返回400KB）。
// bufferSize：文件的总字节数。
// readDataOffset：已读取的字节数偏移量。
int32_t remainingSize = dataInfo->bufferSize - dataInfo->readDataOffset;
if (remainingSize < 0) {
    return -1;
}
int32_t actualDataSize = (remainingSize < MAX_DATA_SIZE) ? remainingSize : MAX_DATA_SIZE;

// 更新已读取位置。
dataInfo->readDataOffset += actualDataSize;

// 设置输入数据状态。
if (dataInfo->readDataOffset >= dataInfo->bufferSize) {
    *outStatus = OH_AudioConverter_InputStatus::AUDIOCONVERTER_INPUT_DATA_FINISHED;
    dataInfo->readDataFinish = true;
} else {
    *outStatus = OH_AudioConverter_InputStatus::AUDIOCONVERTER_INPUT_HAVE_DATA;
}
```

设置输入数据回调。

```cpp
// 设置输入回调。
result = OH_AudioConverter_SetInputCallback(converter, AudioConverterRequestDataCallback, dataInfo);
if (result != AUDIOCONVERTER_SUCCESS) {
    OH_LOG_Print(LOG_APP, LOG_ERROR, GLOBAL_RESMGR, TAG, "Failed to set input callback: %{public}d", result);
    OH_AudioConverter_Destroy(converter);
    return false;
}
```



#### 执行格式转换

调用[OH_AudioConverter_Process()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-converter-h#oh_audioconverter_process)接口执行格式转换。


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/_FVfGXmqQamET8gh5qxgmQ/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260730T072204Z&HW-CC-Expire=86400&HW-CC-Sign=18447B9FC56B11322A78F4E5D4DED1B53A891EF18B62592C42BEABAE06D742BE)


 - 判断数据处理是否完成需要同时满足以下三个条件：         
OH_AudioConverter_Process()返回AUDIOCONVERTER_SUCCESS。
 - outputSize为0。
 - 所有输入数据已经结束（回调函数已经返回了AUDIOCONVERTER_INPUT_DATA_FINISHED）。

        - AUDIOCONVERTER_INPUT_NO_AVAILABLE_DATA和AUDIOCONVERTER_INPUT_DATA_FINISHED状态下，OH_AudioConverter_Process()会返回[AUDIOCONVERTER_SUCCESS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-converter-h#oh_audioconverter_result)和outputSize = 0。因此，不能仅凭outputSize = 0或result = AUDIOCONVERTER_SUCCESS判断数据处理已经完成，还需要调用方确保所有数据已经输入结束。




```cpp
// 分配处理缓冲区。
const int32_t processBufferSize = 4096 * 4; // 16KB。
uint8_t *processBuffer = new uint8_t[processBufferSize];
int32_t outputSize = 0;
int32_t totalOutputSize = 0;
OH_AudioConverter_Result result;

do {
    result = OH_AudioConverter_Process(converter, processBuffer, processBufferSize, &outputSize);
    if (result != AUDIOCONVERTER_SUCCESS) {
        OH_LOG_Print(LOG_APP, LOG_ERROR, GLOBAL_RESMGR, TAG, "Audio data processing failed: %{public}d", result);
        delete[] processBuffer;
        SafeCloseConverterFile(outputFile, outputFilePath);
        return false;
    }
        
    if (outputSize > 0) {
        // 用户可以根据自己的业务要求做相应的处理。
        size_t written = fwrite(processBuffer, 1, outputSize, outputFile);
        if (written != static_cast<size_t>(outputSize)) {
            OH_LOG_Print(LOG_APP, LOG_ERROR, GLOBAL_RESMGR, TAG, "Failed to write output data");
            delete[] processBuffer;
            SafeCloseConverterFile(outputFile, outputFilePath);
            return false;
        }
        totalOutputSize += outputSize;
    }
    // outputSize返回0，且用户写入数据完成。
} while (outputSize > 0 || !dataInfo->readDataFinish);

delete[] processBuffer;
processBuffer = nullptr;
SafeCloseConverterFile(outputFile, outputFilePath);
```



#### 销毁格式转换器

```cpp
OH_AudioConverter_Destroy(converter);
```



#### 完整示例代码

 - [音频编创示例代码](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/Media/Audio/AudioSuiteSample)
