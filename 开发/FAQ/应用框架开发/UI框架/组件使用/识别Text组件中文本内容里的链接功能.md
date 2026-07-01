# 识别Text组件中文本内容里的链接功能

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1233

#### 问题现象

某一长段文本中存在多个超链接，如何实现超链接的识别与点击功能？
 
 

#### 背景知识

- [Text组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)是常用的文本显示组件，自带链接等信息识别功能，包括但不限于对链接进行识别跳转。

 
- [ForEach](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-rendering-control-foreach)：ForEach接口基于数组类型数据来进行循环渲染。
- [Span](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span)：作为Text、ContainerSpan组件的子组件，用于显示行内文本的组件。

 
- 匹配字符串中的URL可以采用正则表达式的方式进行匹配。正则表达式（Regular Expression）是一种用于匹配字符串中字符组合的模式。它广泛应用于编程和文本处理中，特别是在搜索、替换和提取特定文本模式时。

 
 

#### 解决方案

- **方案一**：采用Text组件的[enableDataDetector](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#enabledatadetector11)属性，具体实现方式参考官方文档：[特殊文本识别跳转](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-special-text-recognition)。
> [!NOTE]
> 该属性识别的URL不支持跳转自定义WebView，但是可以跳转系统浏览器。

- **方案二**：实现思路如下：1. 创建URL字符串的正则表达式。

2. 通过match方法匹配原文本中的URL。

3. 通过split方法以URL分割字符串，生成数组。

4. 最后Text组件内通过ForEach循环渲染Span组件，匹配文本内的超链接。

  
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">ExampleText </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">strArr</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(255,0,170);">[]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">urlArr</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(255,0,170);">[]</span><span style="color: rgb(181,106,1);">;</span>
<em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">示例字符串</span></em>
  <span style="color: rgb(255,255,255);">text</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">这是一个网址：</span><span style="color: rgb(132,63,161);">https://developer.huawei.com</span><span style="color: rgb(132,63,161);">，还有一个网址：</span><span style="color: rgb(132,63,161);">https://developer.huawei.org'</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">splitUrls</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">text</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">splitUrls</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">str</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">urlPattern </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">/(https?:\/\/|www.)[a-zA-Z_0-9\-@]+(\.\w[a-zA-Z_0-9\-:]</span><span style="color: rgb(132,63,161);">+)+(\/[\(\)~#</span><span style="color: rgb(132,63,161);">&</span><span style="color: rgb(132,63,161);">\-=?\+\%/\.\w]+)?/g</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(255,255,255);">urlsArr </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">str</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">match</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">urlPattern</span><span style="color: rgb(255,0,170);">) </span>as <span style="color: rgb(181,106,1);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">urlsArr </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span> <span style="color: rgb(255,255,255);">urlsArr</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">strArr </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">splitString</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">str</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">urlsArr</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">urlArr </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">urlsArr</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

  <span style="color: rgb(0,0,255);">splitString</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">str</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">separators</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    return <span style="color: rgb(255,255,255);">str</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">split</span><span style="color: rgb(255,0,170);">(</span>new <span style="color: rgb(0,0,255);">RegExp</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">separators</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">join</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'|'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'g'</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">ForEach</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">strArr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">str</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(0,0,255);">Span</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">str</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          if <span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">urlArr</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,255,255);">index</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(0,0,255);">Span</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">urlArr</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(255,0,170);">])</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#0a59f7'</span><span style="color: rgb(255,0,170);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
                this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPromptAction</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showToast</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">点击网址</span><span style="color: rgb(132,63,161);">' </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">        }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'90%'</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">14</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/vfCNiHbeSfeSWbdizyGkxQ/zh-cn_image_0000002658833297.png?HW-CC-KV=V1&HW-CC-Date=20260701T041330Z&HW-CC-Expire=86400&HW-CC-Sign=C882AC106236651BCD87BD017C5BE730F05F83972702F15F56F97A445FDDBF88)


 
 

#### 总结

方案一为系统自带的Text组件的识别能力，能自动识别文本的信息并跳转，简单高效。方案二和方案三在识别到网络链接后，可以通过[App Linking](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-linking-startup)、[Deep Linking](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deep-linking-startup)等方式拉起其它应用跳转指定页面，或者通过[Web组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkweb)显示网址的内容。
