# AudioSession音频会话未停用影响其他应用音频

更新时间：2026-07-30 01:58:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-64

#### 问题现象

AudioSession音频会话激活时，会影响其他应用音频播放，如何解决？
 
 

#### 解决方案

AudioSession音频会话[isAudioSessionActivated](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiosessionmanager#isaudiosessionactivated12)可查询音频会话是否已激活，音频会话激活状态与是否有音频正在播放没有关系。
 
当音频结束音频播放时，如果需要释放音频焦点，需要手动调用[deactivateAudioSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiosessionmanager#deactivateaudiosession12)停用音频会话释放焦点，否则音频会话仍然会保持焦点1分钟，影响其他应用音频播放效果。
