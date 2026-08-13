# 如何通过User-Agent识别系统类型和设备类型

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-182

#### 问题现象

在开发中，需要根据系统类型和设备类型进行适配，通常分为以下场景：
 
场景一：如何判断当前的操作系统是HarmonyOS系统？
 
场景二：如何判断当前的设备类型是手机、平板、PC？
 
 

#### 背景知识

[User-Agent开发指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-default-useragent)：User-Agent（简称UA）是一个特殊的字符串，包含设备类型、操作系统及版本等关键信息。在Web开发中，这个字符串使服务器能够识别请求的来源设备及其特性，从而根据这些信息提供定制化的内容和服务。如果页面无法正确识别UA，可能会导致多种异常情况。
 
- UserAgent结构：
```text
<span style="color: rgb(0,0,255);">Mozilla</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(255,0,0);">5.0 </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span><span style="color: rgb(0,0,255);">DeviceType</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(255,0,170);">{</span><span style="color: rgb(0,0,255);">OSName</span><span style="color: rgb(255,0,170);">} {</span><span style="color: rgb(0,0,255);">OSVersion</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(0,0,255);">AppleWebKit</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(255,0,0);">537.36 </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">KHTML</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">like Gecko</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(0,0,255);">Chrome</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(255,0,170);">{</span><span style="color: rgb(0,0,255);">ChromeCompatibleVersion</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,0);">.0.0.0 </span><span style="color: rgb(0,0,255);">Safari</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(255,0,0);">537.36  </span><span style="color: rgb(0,0,255);">ArkWeb</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(255,0,170);">{</span><span style="color: rgb(0,0,255);">ArkWeb VersionCode</span><span style="color: rgb(255,0,170);">} {</span><span style="color: rgb(0,0,255);">DeviceCompat</span><span style="color: rgb(255,0,170);">} {</span><span style="color: rgb(0,0,255);">扩展区</span><span style="color: rgb(255,0,170);">}</span>
```
 举例说明：

  
```text
<span style="color: rgb(0,0,255);">Mozilla</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(255,0,0);">5.0 </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Phone</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">OpenHarmony </span><span style="color: rgb(255,0,0);">5.0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(0,0,255);">AppleWebKit</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(255,0,0);">537.36 </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">KHTML</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">like Gecko</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(0,0,255);">Chrome</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(255,0,0);">114.0.0.0 </span><span style="color: rgb(0,0,255);">Safari</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(255,0,0);">537.36  </span><span style="color: rgb(0,0,255);">ArkWeb</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(255,0,0);">4.1.6.1 </span><span style="color: rgb(0,0,255);">Mobile</span>
```

- 字段说明：

| 字段 | 含义 |
| --- | --- |
| DeviceType | 当前的设备类型。 取值范围： Phone：手机设备。 Tablet：平板设备。 PC：2in1设备。 |
| OSName | 基础操作系统名称。默认取值：OpenHarmony。 |
| OSVersion | 基础操作系统版本，两位数字，M.S。 通过系统参数const.ohos.fullname解析版本号得到，取版本号部分M.S前两位。 默认取值：例如5.0 |
| ChromeCompatibleVersion | 兼容Chrome主版本的版本号，从114版本开始演进。 默认取值：114 |
| ArkWeb | HarmonyOS版本Web内核名称。 默认取值：ArkWeb |
| ArkWeb VersionCode | ArkWeb版本号，格式a.b.c.d。 默认取值：例如4.1.6.1 |
| DeviceCompat | 前向兼容字段。 默认取值：Mobile |
| 扩展区 | 三方应用可以扩展的字段。 三方应用使用ArkWeb组件时，可以做UA扩展，例如加入APP相关信息标识。 |

 
 

#### 解决方案

场景一：
 
- 通过User-Agent中的{OSName}字段识别HarmonyOS系统。当{OSName}字段值为OpenHarmony表明当前操作系统为HarmonyOS。
```text
const <span style="color: rgb(0,0,255);">isHarmonyOS </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">/OpenHarmony/i</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">test</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">navigator</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">userAgent</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
```

- 通过User-Agent中的{OSName}和{OSVersion}字段识别HarmonyOS系统及系统版本。格式为：OpenHarmony+版本号。
```text
const <span style="color: rgb(0,0,255);">matches </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">navigator</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">userAgent</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">match</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">/OpenHarmony (\d+\.?\d*)/</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
const <span style="color: rgb(0,0,255);">isHarmonyOS5Plus </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">matches</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">length </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span> <span style="color: rgb(0,0,255);">Number</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">matches</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">]) </span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">5</span><span style="color: rgb(181,106,1);">;</span>
```


 
场景二：
 
通过User-Agent中的{DeviceType}字段识别设备类型，Phone代表手机、Tablet代表平板、PC代表2in1设备。
 
- 检测是否为手机设备：
```text
const <span style="color: rgb(0,0,255);">isPhone </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">/Phone/i</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">test</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">navigator</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">userAgent</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
```

- 检测是否为平板设备：
```text
const <span style="color: rgb(0,0,255);">isTablet </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">/Tablet/i</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">test</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">navigator</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">userAgent</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
```

- 检测是否为PC设备：
```text
const <span style="color: rgb(0,0,255);">is2in1 </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">/PC/i</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">test</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">navigator</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">userAgent</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
```


 
完整实现代码如下：在[onControllerAttached](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#oncontrollerattached10)通过[setCustomUserAgent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#setcustomuseragent10)设置User-Agent。
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">webview </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkWeb'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">userAgent</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Web</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">$rawfile</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'judgeUA.html'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onControllerAttached</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">userAgent </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUserAgent</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,0,170);">' test'</span><span style="color: rgb(181,106,1);">;</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setCustomUserAgent</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">userAgent</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">geolocationAccess</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fileAccess</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">domStorageAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
HTML示例代码如下：
 
```text
<em><!DOCTYPE html></em>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>设备检测</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
        #result {
            margin-top: 20px;
            font-size: 24px;
            color: #333;
        }
    </style>
</head>
<body>
<h1>判断设备类型与系统类型</h1>
<div id="result"></div>
<script>
    const isPhone = () => /Phone/i.test(navigator.userAgent);
    const isHarmonyOS = () => /OpenHarmony/i.test(navigator.userAgent);
    const matches = navigator.userAgent.match(/OpenHarmony (\d+\.?\d*)/);
    const isHarmonyOS5Plus = matches?.length && Number(matches[1]) >= 5;
    const isTablet = () => /Tablet/i.test(navigator.userAgent);
    const is2in1 = () => /PC/i.test(navigator.userAgent);
    const resultElement = document.getElementById('result');
    const additionalInfo = [];
    if (isHarmonyOS()) {
        additionalInfo.push("运行在HarmonyOS系统上");
        if (isHarmonyOS5Plus) {
            additionalInfo.push("HarmonyOS版本 >= 5");
        }
    } else {
        additionalInfo.push("没有运行在HarmonyOS系统上");
    }
    if (isTablet()) {
        resultElement.innerHTML = "当前设备：平板";
    }
    if (isPhone()) {
        resultElement.innerHTML = "当前设备：手机";
    }
    if (is2in1()) {
        resultElement.innerHTML = "当前设备：PC";
    }
    if (additionalInfo.length > 0) {
        resultElement.innerHTML += "<br><br>判断是否在HarmonyOS系统：<br>" + additionalInfo.join("<br>");
    }
</script>
</body>
</html>
```
