# DevEco Testing实用工具设备投屏一直提示加载中的排查方法

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-utilities-cast-4

#### 问题现象

DevEco Testing设备投屏一直提示加载中，无法投屏。
 
 

#### 背景知识

[DevEco Testing](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deveco-testing)中实用工具设备投屏支持将设备界面实时投放到PC上，并支持在PC上对设备进行操作，如按键操作、查看设备/应用信息，文件管理、自定义指令等常用操作。
 
 

#### 问题定位

通过以下命令检查设备目标文件夹下是否存在图片文件（文件名：latestScreen.jpeg）：
 
```bash
hdc shell ls /data/local/tmp
```
 
执行结果如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/Fe9EMLwhQEK__rrQGV48sw/zh-cn_image_0000002658923403.png?HW-CC-KV=V1&HW-CC-Date=20260811T005530Z&HW-CC-Expire=86400&HW-CC-Sign=EB9C984F15296FE9C6A06EA5C4ED6A077AA36E8ECEF7F018C24B294FA984181C)

 
 

#### 分析结论

目标文件存在，需要清理该文件来刷新投屏使用。
 
 

#### 修改建议

通过清除手机缓存文件解决该问题，具体步骤如下：
 1. 电脑连接需要投屏的手机。
2. 执行以下命令：
```bash
hdc shell rm -r /data/local/tmp/latestScreen.jpeg
```

3. 重试设备投屏，如果获取页面仍失败可重启设备后再试。
4. 如果问题仍未解决，将右上角的流畅模式切换成标准模式。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/SWuouiKjQYS0cMNsFxFORg/zh-cn_image_0000002658803455.png?HW-CC-KV=V1&HW-CC-Date=20260811T005530Z&HW-CC-Expire=86400&HW-CC-Sign=7511AE8FF64B501C0A14F07FF0FF7E4D3D28E5E57F641A87BE8301AF55F4A317)

 
 

#### 常见FAQ

Q：DevEco Testing更换版本后无法连接设备，如何解决？
 
A：
 1. 本地hdc list targets可识别，但DevEco Testing中无法识别，可以先尝试关闭DevEco Testing，然后本地执行hdc kill，再重新启动查看是否已识别。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/43vfrSklSliuRWYab8_npg/zh-cn_image_0000002628404192.png?HW-CC-KV=V1&HW-CC-Date=20260811T005530Z&HW-CC-Expire=86400&HW-CC-Sign=620ED78590004E4227CA141D841343160A9DABA60CC3AB8DAE96D38A0BFA0ED2)

2. 若仍未解决请参考[环境准备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hdc#环境准备)获取最新版本的hdc至安装路径D:\DevEco Testing\app\resources\bin下（安装路径D盘时），替换hdc.exe、libusb_shared.dll文件，并将DevEco Testing安装路径下hdc地址配置到系统环境变量中，重启即可恢复。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/hWOC1vOtThOu4MgC19Ageg/zh-cn_image_0000002628564096.png?HW-CC-KV=V1&HW-CC-Date=20260811T005530Z&HW-CC-Expire=86400&HW-CC-Sign=E99A71D1EC8F7C6AB5D7E29D9F6492DC9CB3A3A9BDF664E9DFBE87FCA7D75960)

 
Q：DevEco Testing更换版本后流畅模式提示“设备无法使用视频流进行投屏，请切换至普通模式进行投屏”，切换后显示一直加载中，无法投屏。
 
A：检查本地电脑的USB存储策略是否允许调试且在有效期内。
 
 

#### 总结

出现该问题的原因是该设备的/data/local/tmp/latestScreen.jpeg文件出现了损坏，导致这个文件无法被覆盖写入。可以打开cmd窗口，执行hdc指令删除该文件，再重新投屏即可。
