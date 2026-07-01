# ArkUI页面的视频加载缓慢

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-12

#### 问题现象

打开应用中视频观看时，需要等待一段时间后视频才开始播放。
 
 

#### 背景知识

- [Video](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-media-components-video)：可用于播放视频文件的组件。
- 视频码率：在单位时间内，视频文件传输的数据量，也叫视频的数据速率，通常用bps（位每秒）、Kbps（千位每秒）或Mbps（兆位每秒）来表示。
- 视频起播水线：为了保证视频流畅播放设置的缓冲区阈值。当视频缓冲区的已下载数据量达到起播水线值时，才会开始播放视频，有助于减少视频播放初期可能出现的卡顿现象。起播水线取值与下载速率与视频码率有关，如果下载速率大于或等于视频码率，起播水线取值为0.3*码率，如果下载速率小于视频码率，起播水线取值为5*码率，具体可看[缓冲区工作过程](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-online-video-playback-lags-practice#section1411814743015)。
- ArkUI Inspector：DevEco Studio提供的[布局分析](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkui-inspector)工具，可用于查看应用在真机上的UI显示效果，能够快速分析定位状态变量、组件嵌套层次、UI界面布局存在的问题等。
- DevEco Profiler：集成在DevEco Studio中的性能调优工具，提供场景化的性能调优功能体验，可以检测应用的性能指标、录制Trace信息，通过分析Trace数据能够发现代码中的性能瓶颈，进而优化性能，相关内容可看[DevEco Profiler调优工具简介](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler)。视频加载关键Trace点如下：

| Trace关键字 | 描述 | 泳道/线程 |

| --- | --- | --- |

| H:DispatchTouchEvent xxx type=1 | 应用收到手指离开屏幕的事件 | 应用主进程 |

| H:Create[组件名][self:组件id] | 组件创建 | 应用主进程 |

| H:PlayerServer::PrepareAsync | 系统播放器服务准备播放 | media_service进程的H:PlayerServer::PrepareAsync泳道 |

| H:PlayerServer::Play | 系统播放器服务启动播放 | media_service进程的H:PlayerServer::Play泳道 |

| H:HiPlayerImpl::PrepareAsync | 播放器引擎实例初始化，准备播放。与H:PlayerServer::PrepareAsync对应，分析H:PlayerServer::PrepareAsync具体耗时情况需要分析该Trace关键字，如下图所示 | media_service进程的PlayerEngine线程 |

| H:HiPlayerImpl::Play | 播放器引擎实例启动播放。与H:PlayerServer::Play对应，分析H:PlayerServer::Play具体耗时情况需要分析该Trace关键字，如下图所示 | media_service进程的PlayerEngine线程 |

| H:HttpRequest | http请求 | 应用进程的H:HttpRequest泳道 |

 
 

#### 问题定位

以某应用视频加载时间长问题为例，定位过程如下：
 1. 使用ArkUI Inspector抓取应用页面布局，得知应用使用Video组件进行视频播放。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/ztN_JBUZSvG31KsMQgL6UQ/zh-cn_image_0000002628395104.png?HW-CC-KV=V1&HW-CC-Date=20260701T041401Z&HW-CC-Expire=86400&HW-CC-Sign=61858A6B4A7800BD450A1780E365D7D26C298CE4A16E79E227B228A488D97539)

2. 使用Profiler Frame抓取视频加载播放过程的应用Trace信息，然后搜索应用收到手指离开屏幕的事件、Video组件创建、播放器准备、播放器播放相关Trace点。
- 应用收到手指离开屏幕：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/hegzFrVeRuSb0a01eIGMpw/zh-cn_image_0000002658914323.png?HW-CC-KV=V1&HW-CC-Date=20260701T041401Z&HW-CC-Expire=86400&HW-CC-Sign=22D90E972AFB51638846C5FDED100226487C8EF8CC4BA612475483593095A574)


3. Video组件创建：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/nvC5S7nUSLKHWp7XUNFIeg/zh-cn_image_0000002658794371.png?HW-CC-KV=V1&HW-CC-Date=20260701T041401Z&HW-CC-Expire=86400&HW-CC-Sign=717A7D0B77C809A7D83798CC56CD4D5A1C8DC85D3E0A2884E0698F8338373A46)


4. 播放器准备：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/NvHJMN8pQYaLxq0fkyULrA/zh-cn_image_0000002628555006.png?HW-CC-KV=V1&HW-CC-Date=20260701T041401Z&HW-CC-Expire=86400&HW-CC-Sign=6073FEE79D677A0873AFC825865C9D0431C028D021BA45C8BB9DAC6F36090EF4)


5. 播放器播放：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/bfygrqw-QZarcd57_gdHdg/zh-cn_image_0000002628395106.png?HW-CC-KV=V1&HW-CC-Date=20260701T041401Z&HW-CC-Expire=86400&HW-CC-Sign=C961CE8B3C2236DBAA0BF525FBD65167E01D716DC752148A3E40032A084DFFE7)


1. 计算上述Trace关键字之间的时间，分析其中耗时最多的部分，具体情况如下：
耗时主要集中在从应用收到手指离开屏幕事件到Video组件创建阶段，如下表所示。

| 应用收到手指离开屏幕事件到Video组件创建 | Video组件创建到播放器准备 | 播放器准备耗时 | 播放器播放耗时 |

| --- | --- | --- | --- |

| 10s | 41ms | 314ms | 25ms |

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/u5zFWqJsR_u-LPZT9NKLIg/zh-cn_image_0000002658914325.png?HW-CC-KV=V1&HW-CC-Date=20260701T041401Z&HW-CC-Expire=86400&HW-CC-Sign=87E54501E25B89F80C46DED0A0FCEAFAFB5A6B4052166637C11F1C63BC529A7A)


  查看上图中应用收到手指离开屏幕事件到Video组件创建阶段，应用主线程并无长时间Running的情况，在Video组件创建前可以看到状态变量有刷新，怀疑应用刷新该状态变量后会触发Video组件创建，而状态变量刷新可能与http请求有关。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/hj1BH1O6RWuZNrbY0vhspg/zh-cn_image_0000002658794373.png?HW-CC-KV=V1&HW-CC-Date=20260701T041401Z&HW-CC-Expire=86400&HW-CC-Sign=85261EE3A4453C6BEF79714C4AE6E91DF1BECA98AC80516ADF14A43568DFEF54)


  排查应用H:HttpRequest泳道信息发现应用有进行http请求，耗时接近10s，由此可知应用在加载视频前会进行http请求，从服务器获取数据后刷新组件的状态变量，创建Video组件开始播放视频。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/u_8q3u2JQsSm3ttNlrlITg/zh-cn_image_0000002628555008.png?HW-CC-KV=V1&HW-CC-Date=20260701T041401Z&HW-CC-Expire=86400&HW-CC-Sign=DBB97DB69808E6FFCA0B7AB65937CE05946F0A9419019F1FF693F2765299A21E)


  搜索应用包名/NETSTACK日志关键字，查看http请求时的相关耗时参数，发现此处http请求耗时集中在firstRecv部分，应用服务器响应应用请求时，处理耗时较多。

  
```cpp
04-22 21:36:54.839 22080 22716 I C015B0/com.example.myapplication/NETSTACK: [http_exec.cpp:418] taskid=-2147483621, size:40791, dns:0.100, connect:0.000, tls:0.000, firstSend:0.230, firstRecv:9672.959, total:9965.226, redirect:0.000, errCode:0, RespCode:200, httpVer:3, method:GET, osErr:0
```


2. 耗时主要集中在播放器准备，如下表所示，需要通过日志分析视频数据下载情况。

| 应用收到手指离开屏幕事件到Video组件创建 | Video组件创建到播放器准备 | 播放器准备耗时 | 播放器播放耗时 |

| --- | --- | --- | --- |

| 394ms | 18.1ms | 12.4s | 44.4ms |

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/qPi4-AvtTU6UTqqi5xXztQ/zh-cn_image_0000002628395108.png?HW-CC-KV=V1&HW-CC-Date=20260701T041401Z&HW-CC-Expire=86400&HW-CC-Sign=1ADD6BF32AD89F4C29AED456F99108DCE779146D0207E9EE347D0E1B48984561)


  在日志中搜索BUFFERING_START PAUSE|BUFFERING_END PLAYING|HTTP Buffer is enough|bitrate =找到视频缓冲的起始点、结束点、起播水线、数据下载速度和视频码率，如下图中看到视频缓冲的时间为11.415s（BUFFERING_START PAUSE和BUFFERING_END PLAYING时间间隔），起播水线为5773077字节，下载速度为4209738bit/s，视频码率为9236923bps。

  
```text
07-14 14:15:02.080  1707  3269 I C02B32/av_codec_service/HCODEC: [44][dec.avc][Initialized][Configure 104] bitrate = 9236923 | codec_config, bufferSize = 52 | codec_mime = video/avc | frame_rate = 30.000000 | height = 1080 | language = und | rotation_angle = 0 | track_index = 0 | track_start_time = 0 | track_type = 1 | video_delay = 1 | video_encoder_enable_surface_input_call ...
07-14 14:15:02.097  1436 24011 I C02B22/media_service/HiPlayer: #2180 BUFFERING_START PAUSE
07-14 14:15:13.512  1436 24017 I C02B23/media_service/HiStreamer: (HandleBuffering(), 289): HTTP Buffer is enough, bufferSize:5773623 waterLineAbove: 5773077 avgDownloadSpeed: 4209738.819320
07-14 14:15:13.512  1436 24011 I C02B22/media_service/HiPlayer: #2171 BUFFERING_END PLAYING
```
 由于视频码率大于下载速率，起播水线取值为5*9236923/8=5773076.875字节，与日志中看见的一致，由于视频码率较大，超过当前网络下载速率，视频缓冲到起播水线需要时间，导致视频加载慢。

  

  #### 分析结论

  视频加载慢的原因有：

  
应用在视频播放前发送http请求访问服务器获取数据，服务器端业务逻辑处理耗时较长，导致应用侧收到数据较慢，视频延迟一段时间后才能播放。
- 视频码率较大，超过当前网络下载速率，视频缓冲到起播水线需要时间，导致视频加载慢。

 
 

#### 修改建议

- 优化服务器侧处理逻辑。
- 使用码率较小的视频资源，增加视频加载中提示，或使用[AVPlayer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer)实现视频播放，通过[setMediaSource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#setmediasource12)方法调整PlaybackStrategy中的preferredBufferDurationForPlaying参数去设置起播缓冲水线值。
