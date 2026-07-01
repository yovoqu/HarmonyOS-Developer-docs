# 加载so库后App出现闪退如何解决

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-jsvm-9

## 加载so库后App出现闪退如何解决
 


##### 问题现象

在NAPI项目中链接so后出现APP启动闪退，CMakeLists.txt去除对应so链接后，APP无闪退现象。
 
 

##### 背景知识

[在NDK工程中使用预构建库](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/build-with-ndk-prebuilts)时，可以选择使用.so动态库或者.a静态库。so文件是共享库（shared library）的一种格式，程序在运行时动态链接so库中的代码，而不是像.a静态库编译时静态链接。
 
 

##### 问题定位

- 查看crash日志。如下图，本次闪退为cppcrash，说明so加载链接完成，但是在代码运行时出现错误，根据下图Reason反馈得知由于空指针访问导致的报错。
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/8uLypro5RXyF-nJYyd36gw/zh-cn_image_0000002658907821.png?HW-CC-KV=V1&HW-CC-Date=20260701T025533Z&HW-CC-Expire=86400&HW-CC-Sign=BEB23EE7CDEB64D72164691245A636BD7C8EDC5B12F341BDDDC7AF3D36683CB0)

 若闪退并非cppcrash而是jscrash，如下图，则说明js在访问so或者so加载链接出现问题，需要进一步定位。
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/_q4c8sfmTFWD8lvKRpzQ8w/zh-cn_image_0000002658787883.png?HW-CC-KV=V1&HW-CC-Date=20260701T025533Z&HW-CC-Expire=86400&HW-CC-Sign=CE20F773DCF50F38C0827D6B980AA9C172DB300E4938471F9849AB0C6C0C7F0E)

 ArkTS出错位置和so对外导出的头文件如下二图：
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/r0MKY5jaQP-a8fqy5cwVOw/zh-cn_image_0000002628388610.png?HW-CC-KV=V1&HW-CC-Date=20260701T025533Z&HW-CC-Expire=86400&HW-CC-Sign=83A439F73697BA98B1E323824CDE9F9435FF75AAF2009B7B25F3D41F3ABC0C24)

 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/UWf1ynCfSH2JGwdba-7Fug/zh-cn_image_0000002628548510.png?HW-CC-KV=V1&HW-CC-Date=20260701T025533Z&HW-CC-Expire=86400&HW-CC-Sign=2F0620F86373495226824C6DED1CE7F2270D8D19726B2961D3FEBA792A59AD94)

- 解压HAP包，查看lib目录下是否存在对应的so文件。
在HAP文件后添加.rar扩展名，点击压缩文件打开。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/u9cDoYf4Qj2kllu4X1mqww/zh-cn_image_0000002658907823.png?HW-CC-KV=V1&HW-CC-Date=20260701T025533Z&HW-CC-Expire=86400&HW-CC-Sign=284CF84AFFFDFFFD984E7C22BC6D16F576BA0FF413945255CF872ADF3C4861C8)

- 查看libs\arm64-v8a目录下是否存在对应的so文件，如果缺失so文件说明在编译链接过程中没有将so文件打包进HAP，需要定位具体原因。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/qKtEBRQXQt27LXR5z9ICLw/zh-cn_image_0000002658787885.png?HW-CC-KV=V1&HW-CC-Date=20260701T025533Z&HW-CC-Expire=86400&HW-CC-Sign=BA460F6556C6FCBCCCBD5428E33EF4AE94172BCC7A0889D309991B4762C33C98)


 - 确认HAP中的so文件是真实的库文件。由于在不同平台中软链接格式不同，此处以Linux为例。在Linux平台进行交叉编译时，一些源码通过编译链接后会生成多个链接文件，如下图。libjpeg.so/libjpeg.so.62均为链接文件，占用空间很小，而实际的so文件则为libjpeg.so.62.4.0,如果只拷贝链接文件会导致无法链接到真正的so文件。
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/jCn9uSyWQy-CH8E16Gc1YA/zh-cn_image_0000002628388612.png?HW-CC-KV=V1&HW-CC-Date=20260701T025533Z&HW-CC-Expire=86400&HW-CC-Sign=2EC38ADDA141102149900141B2750C50E4962B242FDBD726C60662CDDBC21385)

- 确认so文件依赖so文件均已导入进HAP包中。通过readelf -d xxx.so命令可以读取so文件中依赖的so文件，以下图libavcodec.so为例。该so同时依赖了libswreasample.so\libavutil.so\libz.so\libc.so，需要确保如上so均打包进入HAP中或者存在于HarmonyOS的系统库中。
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/XvxjwQ3XQDiigieiantz-Q/zh-cn_image_0000002628548512.png?HW-CC-KV=V1&HW-CC-Date=20260701T025533Z&HW-CC-Expire=86400&HW-CC-Sign=67633790CF7DA51F8C8E202C01CAA6A4E082DAEBFB6E3ABFAAFB99E97002150A)


 
 

##### 分析结论

应用打包缺少so动态库文件及其依赖的其他动态库或者错误的so文件均会导致应用在启动过程中闪退。
 
 

##### 修改建议

- 修改C/C++源码。根据cppcrash反馈的报错原因和堆栈调用定位代码出错原因，修改C/C++源码。
- 将需要的so放置于libs\${OHOS_ARCH}目录下。将so放置于libs\${OHOS_ARCH}目录下后，编译HAP时会自动将so打包进去。
- 重新编译去除so库版本号，避免软链接文件造成干扰。修改源码的编译文件，去除版本号的相关定义，重新编译生成库文件。
- 保障so链接完整性。通过readelf等工具排查清楚so依赖的其他库文件，将该so所有的依赖库文件均放置于libs\${OHOS_ARCH}目录下。
