# OpenSL ES音频录制示例调用崩溃

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-3

问题现象

OpenSL ES音频录制接口调用失败，程序崩溃。报错日志信息如下：

08-06 00:39:20.042 5198-5219/? E C02b00/AudioFramework: [audio_service_client.cpp] Client doesn't have MICROPHONE permission

解决措施

需要申请ohos.permission.MICROPHONE权限。详情请参见开放权限（用户授权）。
