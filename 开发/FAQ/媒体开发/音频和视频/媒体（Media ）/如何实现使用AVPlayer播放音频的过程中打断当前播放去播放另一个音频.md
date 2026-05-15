# 如何实现使用AVPlayer播放音频的过程中打断当前播放去播放另一个音频

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-3

需要先调用reset()打断前一个音频，然后切换音频源。因为reset()是异步的，所以调用reset()的语句需加上await关键字。
