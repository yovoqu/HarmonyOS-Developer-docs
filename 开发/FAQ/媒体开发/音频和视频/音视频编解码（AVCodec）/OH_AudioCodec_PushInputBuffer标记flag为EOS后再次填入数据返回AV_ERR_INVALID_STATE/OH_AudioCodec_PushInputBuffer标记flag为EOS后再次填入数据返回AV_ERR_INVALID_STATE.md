# OH_AudioCodec_PushInputBuffer标记flag为EOS后再次填入数据返回AV_ERR_INVALID_STATE

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avcodec-16

#### 问题现象

开发者使用OH_AVDemuxer配合OH_AVCodec实现对音频解码成pcm数据的功能。
 
当音频文件读取结束时，调用者第一次调用OH_AudioCodec_PushInputBuffer对缓冲区完成数据填充时返回正常(OH_AVCodecBufferAttr的flags参数为AVCODEC_BUFFER_FLAGS_EOS)，设置完成最后一个数据后依然可以继续收到OnInputBufferAvailable回调。再次输入数据给编码器时返回错误码8，并停止解码。
 
 

#### 背景知识

- 解码时，调用者调用[OH_AudioCodec_PushInputBuffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avcodec-audiocodec-h#oh_audiocodec_pushinputbuffer)，写入待解码的数据，解码器需开发者填充完整的输入数据后方可调用。
> [!NOTE]
> 音频文件结束后，需要将 OH_AVCodecBufferAttr 的flags标识成AVCODEC_BUFFER_FLAGS_EOS。

- [音视频编解码errorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avcodec-13)为AV_ERR_INVALID_STATE则表示当前状态不支持此操作，取值为8。

 
 

#### 问题定位

首次解码成功的流程：
 
循环（收到输入缓存区回调->使用解码器读取buffer（buffer属性中flags不为AVCODEC_BUFFER_FLAGS_EOS）->设置buffer到缓存区）。
 
解码异常流程：
 
当读到音频文件末尾时：
 1. 收到输入缓存区回调->使用解码器读取buffer（实际上读取到的数据是0，读取的buffer属性中flags为AVCODEC_BUFFER_FLAGS_EOS）->设置buffer到缓存区（此时正常）。
2. 再次收到输入缓存区回调->使用解码器读取buffer（实际上读取到的数据是0，读取的buffer属性中flags为AVCODEC_BUFFER_FLAGS_EOS）->设置buffer到缓存区（此时OH_AudioCodec_PushInputBuffer返回值为8，并且不再收到OnOutputBufferAvailable回调）。
 
 

#### 分析结论

OnInputBufferAvailable的作用是通过异步方式提供了可用的buffer给调用者输入，输入AVCODEC_BUFFER_FLAGS_EOS之后，即是结束标识，解码器不再接收新的数据，再次进行设置buffer到缓存区处理就会出现当前状态不支持此操作，取值为8的报错。
 
 

#### 修改建议

当读取的buffer属性中flag为AVCODEC_BUFFER_FLAGS_EOS后，解码器将不再接收新的数据，未使用的buffer，可以不做处理。假如是保存在调用者的队列中，可以在EOS后，清空调用者记录的队列，相关内存会在[OH_AudioCodec_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avcodec-audiocodec-h#oh_audiocodec_destroy)时清理。
