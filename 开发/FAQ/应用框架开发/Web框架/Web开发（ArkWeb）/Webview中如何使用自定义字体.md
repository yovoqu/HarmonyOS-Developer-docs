# Webview中如何使用自定义字体

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-149

#### 问题现象

Webview中h5侧如何使用自定义字体？
 
 

#### 背景知识

自定义字体是指开发者根据应用需求创建或选择的字体，通常用于实现特定的文字风格或满足独特的设计要求。当应用需要使用特定的文本样式和字符集时，可以注册并使用自定义字体进行文本渲染。
 
 

#### 解决方案

使用本地自定义字体，实现思路参考如下：
 1. 将字体文件放在resources/rawfile/font文件夹里。
2. h5侧直接通过font-face引用字体。
```text
<span style="color: rgb(181,106,1);">@</span><span style="color: rgb(0,0,255);">font</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(0,0,255);">face </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">font</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(0,0,255);">family</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'HarmonyOS Sans'</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">url</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'./font/HarmonyOS_Sans_SC_Regular.ttf'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">harmonyos</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(0,0,255);">sans </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">font</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(0,0,255);">family</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'HarmonyOS Sans'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">sans</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(0,0,255);">serif</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```

 
完整示例参考如下：
 
- src/main/ets/pages/webPage页面。
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">webview </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkWeb'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">WebComponent </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Web</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">$rawfile</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Index.html'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fileAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">javaScriptAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">domStorageAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onlineImageAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">geolocationAccess</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>
<span style="color: rgb(255,0,170);">}</span>
```

- resources/rawfile/Index.html页面。
```text
<!DOCTYPE html>
<html lang="en-gb">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>自定义字体</title>
    <style>
        body {
          font-size: 20px;
        }
        @font-face {
          font-family: 'HarmonyOS Sans';
          src: url('./font/HarmonyOS_Sans_SC_Regular.ttf');
        }
        .harmonyos-sans {
          font-family: 'HarmonyOS Sans', sans-serif;
        }
    </style>
</head>
<body>
<div class="harmonyos-sans">Sans字体：Innation in china</div>
</body>
</html>
```
