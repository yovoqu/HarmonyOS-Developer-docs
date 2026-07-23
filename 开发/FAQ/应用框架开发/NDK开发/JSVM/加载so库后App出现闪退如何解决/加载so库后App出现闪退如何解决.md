# 加载so库后App出现闪退如何解决

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-jsvm-9

#### 问题现象

在NAPI项目中链接so后出现APP启动闪退，CMakeLists.txt去除对应so链接后，APP无闪退现象。
 
 

#### 背景知识

[在NDK工程中使用预构建库](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/build-with-ndk-prebuilts)时，可以选择使用.so动态库或者.a静态库。so文件是共享库（shared library）的一种格式，程序在运行时动态链接so库中的代码，而不是像.a静态库编译时静态链接。
 
 

#### 问题定位
1. 查看crash日志。如下图，本次闪退为cppcrash，说明so加载链接完成，但是在代码运行时出现错误，根据下图Reason反馈得知由于空指针访问导致的报错。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/8uLypro5RXyF-nJYyd36gw/zh-cn_image_0000002658907821.png?HW-CC-KV=V1&HW-CC-Date=20260723T012522Z&HW-CC-Expire=86400&HW-CC-Sign=1776631923AFDFD2F12CF0B5A6E21BF0B529C0CC41A7E70D8683CB4236DB3179)


  若闪退并非cppcrash而是jscrash，如下图，则说明js在访问so或者so加载链接出现问题，需要进一步定位。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/_q4c8sfmTFWD8lvKRpzQ8w/zh-cn_image_0000002658787883.png?HW-CC-KV=V1&HW-CC-Date=20260723T012522Z&HW-CC-Expire=86400&HW-CC-Sign=7EEE91F50EC8027B0C96AB332D9350727C8A44BD0A04D339566729D2E23684BF)


  ArkTS出错位置和so对外导出的头文件如下二图：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/r0MKY5jaQP-a8fqy5cwVOw/zh-cn_image_0000002628388610.png?HW-CC-KV=V1&HW-CC-Date=20260723T012522Z&HW-CC-Expire=86400&HW-CC-Sign=D1CAC7475D567B284FE65BB59E0DB326C72207FD01EEC5C6BCA7159F002AF313)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/UWf1ynCfSH2JGwdba-7Fug/zh-cn_image_0000002628548510.png?HW-CC-KV=V1&HW-CC-Date=20260723T012522Z&HW-CC-Expire=86400&HW-CC-Sign=D634BB7C5BB225740DB91542C495962D797E8453F7614C8040E2B085F6C38171)

2. 解压HAP包，查看lib目录下是否存在对应的so文件。
- 在HAP文件后添加.rar扩展名，点击压缩文件打开。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/u9cDoYf4Qj2kllu4X1mqww/zh-cn_image_0000002658907823.png?HW-CC-KV=V1&HW-CC-Date=20260723T012522Z&HW-CC-Expire=86400&HW-CC-Sign=9E7E1018F69640124EE117367A8A7AF5B76EFC04554AFDC6078E3C59921E03A6)


3. 查看libs\arm64-v8a目录下是否存在对应的so文件，如果缺失so文件说明在编译链接过程中没有将so文件打包进HAP，需要定位具体原因。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/qKtEBRQXQt27LXR5z9ICLw/zh-cn_image_0000002658787885.png?HW-CC-KV=V1&HW-CC-Date=20260723T012522Z&HW-CC-Expire=86400&HW-CC-Sign=D3390A29751EC1251137650D3716D8568ACC14CBB3BFBEDA8584F38B160C1A84)

- 确认HAP中的so文件是真实的库文件。由于在不同平台中软链接格式不同，此处以Linux为例。在Linux平台进行交叉编译时，一些源码通过编译链接后会生成多个链接文件，如下图。libjpeg.so/libjpeg.so.62均为链接文件，占用空间很小，而实际的so文件则为libjpeg.so.62.4.0,如果只拷贝链接文件会导致无法链接到真正的so文件。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/jCn9uSyWQy-CH8E16Gc1YA/zh-cn_image_0000002628388612.png?HW-CC-KV=V1&HW-CC-Date=20260723T012522Z&HW-CC-Expire=86400&HW-CC-Sign=F899BE30C7A44B68D8C1DE5E869ABE5C8915C1C5FE9A8CEB43F991EDA8CD1F37)

- 确认so文件依赖so文件均已导入进HAP包中。通过readelf -d xxx.so命令可以读取so文件中依赖的so文件，以下图libavcodec.so为例。该so同时依赖了libswreasample.so\libavutil.so\libz.so\libc.so，需要确保如上so均打包进入HAP中或者存在于HarmonyOS的系统库中。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/XvxjwQ3XQDiigieiantz-Q/zh-cn_image_0000002628548512.png?HW-CC-KV=V1&HW-CC-Date=20260723T012522Z&HW-CC-Expire=86400&HW-CC-Sign=6CF1C05DC1003DF90FFACF62929BB969F68F1783C9C5E5DB90EB0CA3A23B95E4)


 
 

#### 分析结论

应用打包缺少so动态库文件及其依赖的其他动态库或者错误的so文件均会导致应用在启动过程中闪退。
 
 

#### 修改建议
1. 修改C/C++源码。根据cppcrash反馈的报错原因和堆栈调用定位代码出错原因，修改C/C++源码。
2. 将需要的so放置于libs\${OHOS_ARCH}目录下。将so放置于libs\${OHOS_ARCH}目录下后，编译HAP时会自动将so打包进去。
3. 重新编译去除so库版本号，避免软链接文件造成干扰。修改源码的编译文件，去除版本号的相关定义，重新编译生成库文件。
4. 保障so链接完整性。通过readelf等工具排查清楚so依赖的其他库文件，将该so所有的依赖库文件均放置于libs\${OHOS_ARCH}目录下。
