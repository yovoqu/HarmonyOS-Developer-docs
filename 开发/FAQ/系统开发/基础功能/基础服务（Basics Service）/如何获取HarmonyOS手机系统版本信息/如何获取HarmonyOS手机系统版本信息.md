# 如何获取HarmonyOS手机系统版本信息

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-62

#### 问题现象

目前通过deviceInfo.displayVersion获取的手机系统版本是：ALN-AL00 6.0.0.110(SP97C00E110R4P8log)，如何获取软件版本号6.0.0.110，如何获取软件版本号中的"110"。
 
 

#### 解决方案

- **方案一**：直接通过正则表达式直接匹配点分十进制格式的版本号（如6.0.0.110），并捕获第四位数值"110"。
- **方案二**：先通过正则表达式直接匹配点分十进制格式的版本号（如6.0.0.110），再通过字符串分割取其中第四位数值"110"。

 
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">deviceInfo </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getSysVersion</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">getSysVersion</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">displayVersionStr</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">deviceInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">displayVersion</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`displayVersionStr :</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">displayVersionStr</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <em>// </em><em><span style="color: rgb(128,128,128);">方案一：</span></em>
<em>    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">核心正则表达式为</span><span style="color: rgb(128,128,128);">(\d+\.){3}(\d+)</span><span style="color: rgb(128,128,128);">，其中</span><span style="color: rgb(128,128,128);">(\d+)</span><span style="color: rgb(128,128,128);">用于捕获第四位数值。</span></em>
<em>    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">匹配返回包含搜索结果的数组，其中索引为</span><span style="color: rgb(128,128,128);">2</span><span style="color: rgb(128,128,128);">的元素为您需要的字符串值。</span></em>
    const <span style="color: rgb(255,255,255);">versionMatch </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">displayVersionStr</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">match</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">/(\d+\.){3}(\d+)/</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`versionMatch :</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">versionMatch</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">versionMatch </span><span style="color: rgb(181,106,1);">!= </span>null<span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`extractFourthValue1 is :</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">versionMatch</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">输出结果：</span><span style="color: rgb(128,128,128);">extractFourthValue1 is:6.0.0.110</span></em>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`extractFourthValue2 is :</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">versionMatch</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(80,160,79);">2</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
   <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">输出结果：</span><span style="color: rgb(128,128,128);">extractFourthValue2 is:110</span></em>
    <span style="color: rgb(181,106,1);">}</span>

   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">方案二：</span></em>
<em>    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">先通过正则表达式直接匹配点分十进制格式的版本号（如</span><span style="color: rgb(128,128,128);"> 6.0.0.110</span><span style="color: rgb(128,128,128);">），再通过字符串分割取其中第四位数值</span><span style="color: rgb(128,128,128);">"110"</span><span style="color: rgb(128,128,128);">。</span></em>
    const <span style="color: rgb(255,255,255);">version </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">displayVersionStr</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">match</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">/\b\d+\.\d+\.\d+\.\d+\b/</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`versionMatch :</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">version</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">version </span><span style="color: rgb(181,106,1);">!= </span>null<span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      let <span style="color: rgb(255,255,255);">result</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(255,255,255);">version</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">split</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'.'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`extractFourthValue1 is :</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">version</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
     <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">输出结果：</span><span style="color: rgb(128,128,128);">extractFourthValue1 is:6.0.0.110</span></em>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`extractFourthValue2 is :</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">result</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(80,160,79);">3</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">输出结果：</span><span style="color: rgb(128,128,128);">extractFourthValue2 is:110</span></em>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
<span style="color: rgb(181,106,1);">  }</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
可从日志中获取系统版本号信息：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/GJNNT1W4TTimWewtlFYnsQ/zh-cn_image_0000002628773844.png?HW-CC-KV=V1&HW-CC-Date=20260730T072604Z&HW-CC-Expire=86400&HW-CC-Sign=FD0B3B2AD088CF0C23795D9CDC0BA6167634C5398568EFBE474284373A572E57)
