# hdc命令无法获取蓝牙HCI日志该怎么处理

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-48

#### 问题现象
1. 开发者模式已打开“开启蓝牙hci信息收集日志”开关。
2. 通过如下hdc命令，未获取到蓝牙hci日志，获取日志数量为0：
```text
<span style="color: rgb(0,0,255);">hdc file recv </span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">log</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">bt </span><span style="color: rgb(181,106,1);">./</span>
<span style="color: rgb(0,0,255);">FileTransfer finish</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">Size </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">File count </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">time</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">ms </span><span style="color: rgb(181,106,1);">rate</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,0);">0.00</span><span style="color: rgb(0,0,255);">kB</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">s</span>
```

 
 

#### 背景知识

- [hdc命令工具](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hdc)。
- [开发者选项](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-developer-mode)。

 
 

#### 问题定位
1. hdc命令工具是否安装，使用hdc -v命令查看hdc命令工具版本信息，判断hdc命令工具是否安装成功。
2. 开发者选项是否开启USB调试。USB调试：如果开发者希望通过计算机侧命令对移动设备进行调测，需要启用USB调试，同时通过设备授权确认。

  开启并授权后，HarmonyOS设备才能连接到计算机进行调试，可用于在计算机和设备之间复制数据、在设备上安装或卸载调试应用、以及读取日志数据等。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/-VwM2XKXR-SXgyPkzyaOww/zh-cn_image_0000002628394988.png?HW-CC-KV=V1&HW-CC-Date=20260730T072250Z&HW-CC-Expire=86400&HW-CC-Sign=D2F912A660A8839CEBF7D33420AAAAB73C58F6878C3370ED9A1722775BC9B945)

3. 根据背景知识中的hdc命令工具链接，检查hdc命令是否正确。
4. 查看是否存在报错返回，根据报错信息分析，可借助背景知识中的hdc命令工具中hdc错误码进行初步解决。
 
 

#### 分析结论
1. hdc命令用于直接调用手机的开发者模式的调试，类似于Linux的Shell命令，出现问题则需要检查与机器的连接状态是否正常、开发者选项是否开启USB调试、hdc命令是否正确。
2. 如出现hdc命令工具本身的问题，则需根据hdc命令工具报错进行分析，借助hdc命令工具中hdc错误码进行分析。
 
 

#### 修改建议

使用正确的hdc命令：
 
蓝牙hci日志：
 
```text
<span style="color: rgb(0,0,255);">hdc file recv </span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">log</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">bt</span>
```
 
hilog日志：
 
```text
<span style="color: rgb(0,0,255);">hdc file recv </span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">log</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">hilog</span>
```
 
日志默认下载位置为执行该hdc命令的当前目录下。
