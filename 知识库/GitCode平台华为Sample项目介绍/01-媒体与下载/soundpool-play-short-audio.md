# 基于SoundPool播放短音频

## 项目简介
本场景解决方案主要面向前台音频开发人员，指导开发者基于SoundPool开发短音频播放功能。

## 效果预览
| 主页面                              | 
|----------------------------------|
| ![](./assets/soundpool-play-short-audio/device/index.png)|

## 使用说明
1. 运行工程，进入首页后，点击底部播放按钮，可听见应用播放短音。
2. 点击底部循环播放按钮，可以听见循环播放短音三次。
3. 点击底部0.5倍速度播放，可以听见短音以0.5倍速度播放。
4. 点击底部2倍速度播放，可以听见短音以2倍速度播放。
5. 点击底部0.5倍音量播放，可以听见短音以0.5倍音量播放。


## 工程目录
```
├──entry/src/main/ets/
│  ├──entryability
│  │  └──EntryAbility.ets                                 // Ability的生命周期回调内容
│  ├──entrybackupability
│  │  └──EntryBackupAbility.ets                           // EntryBackupAbility的生命周期回调内容
│  └──pages
│     └──Index.ets                                        // 首页
└──entry/src/main/resources                               // 应用静态资源目录
```

## 具体实现
使用系统接口SoundPool实现播放短音功能，短音文件来源于项目rawfile目录下的ogg文件。

## 相关权限
不涉及

## 约束与限制
1. 本示例仅支持标准系统上运行，支持设备：直板机。
2. HarmonyOS系统：HarmonyOS 6.0.0 Release Release及以上。
3. DevEco Studio版本：DevEco Studio 6.0.0 Release及以上。
4. HarmonyOS SDK版本：HarmonyOS 6.0.0 Release SDK及以上。







