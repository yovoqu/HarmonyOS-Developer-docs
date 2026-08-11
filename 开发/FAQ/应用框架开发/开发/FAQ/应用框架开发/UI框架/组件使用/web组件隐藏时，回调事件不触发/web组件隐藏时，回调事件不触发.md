# web组件隐藏时，回调事件不触发

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1543

#### 问题现象

当web组件需要隐藏时，回调事件不触发，比如onPageBegin未触发。
 
问题代码示例参考如下：
 
```text
<span style="color: rgb(0,0,255);">Web</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{}</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onPageBegin</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`into onPageBegin`</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">visibility</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Visibility</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">None</span><span style="color: rgb(255,0,170);">)</span>
```
 
 

#### 背景知识

[visibility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-visibility)是控制组件显隐控制的一个基础属性。其值类型说明参考文档：[Visibility枚举说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#visibility)。
 
 

#### 问题定位

通过ArkUI Inspector工具，可以看到出问题的组件并没有被渲染出来。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/_gzHfCtTRE2BiJzcRj985w/zh-cn_image_0000002658968439.png?HW-CC-KV=V1&HW-CC-Date=20260811T005758Z&HW-CC-Expire=86400&HW-CC-Sign=668F19E98023883B098BBBBA1962D3F3703BF5B2CF0F5558DEF4422B2CD32509)

 
 

#### 分析结论

visibility属性设置Visibility.None后，是不会渲染组件的，所以组件相关的生命周期也不会触发。
 
 

#### 修改建议

把visibility属性的值改成Visibility.Hidden即可。
 
```text
import <span style="color: rgb(255,255,255);">webview </span>from <span style="color: rgb(132,63,161);">'@ohos.web.webview'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(181,106,1);">{</span>
<em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">开发者需根据自身需求填写网址</span></em>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">webSrc</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'xxx'</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">webController</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">WebviewController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(255,255,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Web</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">src</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">webSrc</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">webController </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">size</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">width</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">height</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'100%' </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onPageBegin</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`into onPageBegin (web Hidden)`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
    <em>    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">按照示例代码，开发者需要隐藏，因此设置为</span><span style="color: rgb(128,128,128);">Visibility.Hidden</span></em>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">visibility</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Visibility</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Hidden</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">geolocationAccess</span><span style="color: rgb(255,0,170);">(</span>false<span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fileAccess</span><span style="color: rgb(255,0,170);">(</span>false<span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
日志中onPageBegin()触发，打印了into onPageBegin (web Hidden)。
