# 使用AVPlayer播放视频时，如何实现应用从后台切回前台时继续播放原视频

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-4

在切换到前台的生命周期方法onPageShow()里调用AVPlayer的播放方法avPlayer.play()，并在切换到后台的生命周期方法onPageHide()里调用AVPlayer的暂停方法avPlayer.pause()即可。
