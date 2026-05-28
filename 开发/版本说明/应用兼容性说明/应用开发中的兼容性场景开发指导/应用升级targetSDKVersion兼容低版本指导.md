# 应用升级targetSDKVersion兼容低版本指导

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/app-compatibility-upgrade

应用的源码工程配置项（build-profile.json5文件）中通过targetSdkVersion和compatibleSdkVersion定义了应用运行的目标SDK版本和最低SDK版本。
 
推荐开发者适配最新发布的API版本，即推荐开发者配置targetSDKVersion和CompileSdkVersion一样，享受到最新版本特性。开发者可根据自身实际情况升级targetSDKVersion。
 
部分应用升级targetSDKVersion时，可能不升级compatibleSdkVersion，下面介绍这种场景如何进行兼容性适配。
 
例如：接口A在SDK版本5.0.2(14)产生行为变更并进行了版本隔离，应用升级targetSDKVersion≥5.0.2(14)并适配了新版本行为， compatibleSdkVersion还保持设置为5.0.1(13)， 则若应用分发到低版本设备5.0.1(13)上，需保证该应用在低版本设备能够兼容运行正常（如下图所示）。
 

![](assets/应用升级targetSDKVersion兼容低版本指导/file-20260515135042074-0.png)

 
这种场景开发者可以使用如下方式进行兼容处理：
 

#### 基于C/ArkTS语言API接口兼容低版本行为

- 针对HarmonyOS设备独有特性接口，即接口标记为since M.F.S(N)（文档中标记“起始版本：M.F.S(N)”, SDK物理包中hms路径下所包含的接口），使用distributionOSApiVersion接口进行兼容性判断保护。

  ArkTS API:
```text
<span style="color: rgb(0,0,255);">import</span> { deviceInfo } <span style="color: rgb(0,0,255);">from</span> <span style="color: rgb(255,0,0);">'@kit.BasicServicesKit'</span>;
<span style="color: rgb(80,160,79);">//针对HarmonyOS专有接口，即接口标记为since M.F.S(N)的接口</span>
getTestData(): <span style="color: rgb(0,0,255);">void</span> {
    <span style="color: rgb(80,160,79);">// 兼容性判断，50002是由新接口的since字段M*10000+F*100+S转换而来</span>
    <span style="color: rgb(0,0,255);">if</span> (deviceInfo.distributionOSApiVersion >=  50002) {
        <span style="color: rgb(80,160,79);">// </span><span style="color: rgb(80,160,79);">适配5.0.2(14)版本某API行为变更后的处理</span>
    } <span style="color: rgb(0,0,255);">else</span> {
        <span style="color: rgb(80,160,79);">// 兼容原有逻辑</span>
    }
}
```


  C API：

  
```text
<span style="color: rgb(255,0,170);">#include</span> <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">deviceinfo.h</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(255,0,170);">#include</span> <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">stdio.h</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(80,160,79);">//针对HarmonyOS专有接口，即接口标记为since M.F.S(N)的接口</span>
<span style="color: rgb(0,0,255);">void</span> <span style="color: rgb(181,106,1);">GetTestData</span>() {
<span style="color: rgb(80,160,79);">    // 兼容性判断，50002是由新接口的since字段M*10000+F*100+S转换而来</span>
    <span style="color: rgb(255,0,170);">if</span> (<span style="color: rgb(181,106,1);">OH_GetDistributionOSApiVersion</span>() >=  50002) {
<span style="color: rgb(80,160,79);">        // 适配5.0.2(14)版本某API行为变更后的处理</span>
    } <span style="color: rgb(255,0,170);">else</span> {
<span style="color: rgb(80,160,79);">        // 兼容原有逻辑</span>
    }
}
```

- 针对OpenHarmony底座接口，即接口标记为since N（文档中标记“起始版本：N”，SDK物理包中openharmony路径下所包含的接口），使用sdkApiVersion接口进行兼容性判断保护。

  ArkTS API:
```text
<span style="color: rgb(0,0,255);">import</span> { deviceInfo } <span style="color: rgb(0,0,255);">from</span> <span style="color: rgb(255,0,0);">'@kit.BasicServicesKit'</span>;
<span style="color: rgb(80,160,79);">//针对OpenHarmony底座公共接口，即接口标记为since N</span>
getTestData(): <span style="color: rgb(0,0,255);">void</span> {
    <span style="color: rgb(80,160,79);">// 增加兼容性判断</span>
    <span style="color: rgb(0,0,255);">if</span> (deviceInfo.sdkApiVersion >= 14) {
        <span style="color: rgb(80,160,79);">// 适配5.0.2(14)版本某API行为变更后的处理</span>
    } <span style="color: rgb(0,0,255);">else</span> {
        <span style="color: rgb(80,160,79);">// 兼容原有逻辑</span>
    }
}
```


  C API：

  
```text
<span style="color: rgb(255,0,170);">#include</span> <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">deviceinfo.h</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(255,0,170);">#include</span> <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">stdio.h</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(80,160,79);">//针对OpenHarmony底座公共接口，即接口标记为since N</span>
<span style="color: rgb(0,0,255);">void</span> <span style="color: rgb(181,106,1);">GetTestData</span>() {
<span style="color: rgb(80,160,79);">    // 增加兼容性判断</span>
    <span style="color: rgb(255,0,170);">if</span> (<span style="color: rgb(181,106,1);">OH_GetSdkApiVersion</span>() >=  <span style="color: rgb(80,160,79);">14</span>) {
<span style="color: rgb(80,160,79);">        // 适配5.0.2(14)版本某API行为变更后的处理</span>
    } <span style="color: rgb(255,0,170);">else</span> {
<span style="color: rgb(80,160,79);">        // 兼容原有逻辑</span>
    }
}
```
