# 如何定位单独设置APP偏好语言失败的问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-localization-16

#### 问题现象

单独设置APP偏好语言失败，APP语言必须和系统语言保持一致。
 
- 预期效果：应用可以根据用户的选择，自行变换应用内的语言。
- 实际效果：应用内语言只能与系统的偏好语言保持一致。

 
问题代码示例参考如下：
 
```text
import <span style="color: rgb(255,255,255);">I18n </span>from <span style="color: rgb(132,63,161);">'@ohos.i18n'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">BusinessError </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

try <span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">I18n</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">System</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setAppPreferredLanguage</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'en-Latn-US'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置应用当前的偏好语言为</span><span style="color: rgb(128,128,128);">'US'</span></em>
<span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
  let <span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">BusinessError </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">error </span>as <span style="color: rgb(181,106,1);">BusinessError</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`call System.setAppPreferredLanguage failed, error code: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">, message: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">.`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Component</span>
<span style="color: rgb(181,106,1);">@Entry</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'app.string.module_desc'</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
 

#### 背景知识

- [@ohos.i18n(国际化-I18n)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-i18n)：该模块提供系统相关的或者增强的国际化能力，包括区域管理、电话号码处理、日历等。
- [setAppPreferredLanguage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-i18n#setapppreferredlanguage11)：设置应用偏好语言。设置后，应用将优先加载应用偏好语言对应的资源。设置偏好语言为'default'后，应用语言将跟随系统语言，应用冷启动生效。

 
 

#### 问题定位
1. 排查资源文件中语言信息是否配置正确。
2. 排查切换语言过程中，语言状态status是否正确。
 
 

#### 分析结论

通过setAppPreferredLanguage接口实现单独设置应用偏好语言。主要实现思路有以下三步：
 1. setAppPreferredLanguage接口需要从资源文件中获取语言信息，资源文件中需要提前声明准备提供给用户的不同语言。
2. 在用户界面提供可选语言的下拉框或按钮等交互组件，让用户进行自主选择。
3. 记录用户的选择，并设置进偏好语言中。
 
 

#### 修改建议

根据上述思路，下文中将以“通过点击按钮，自主切换中英文”进行说明：
 1. 在资源文件中添加中/英文的value值。默认语言（base文件）以及中文语言（zh_CN文件）写的是中文，英文语言（en_US文件）写的是英文。因此在偏好语言为英文时，显示en_US文件的内容；偏好语言为中文时，显示zh_CN文件的内容；偏好语言为其他语言时，显示base文件的内容。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/1XDrbTGBSay6W35vK47mPw/zh-cn_image_0000002628663108.png?HW-CC-KV=V1&HW-CC-Date=20260730T072528Z&HW-CC-Expire=86400&HW-CC-Sign=7A593A610178805D7701051D3853BC3C213796183513A536B9989620D9A96B49)


  
base目录中的string.json如下：
```json
{
  <span style="color: rgb(132,63,161);">"string"</span><span style="color: rgb(181,106,1);">: </span>[
    {
      <span style="color: rgb(132,63,161);">"name"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"module_desc"</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(132,63,161);">"value"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"</span><span style="color: rgb(80,160,79);">模块描述</span><span style="color: rgb(80,160,79);">"</span>
    }<span style="color: rgb(181,106,1);">,</span>
    {
      <span style="color: rgb(132,63,161);">"name"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"language_button"</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(132,63,161);">"value"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"</span><span style="color: rgb(80,160,79);">改变语言</span><span style="color: rgb(80,160,79);">"</span>
    }<span style="color: rgb(181,106,1);">,</span>
    {
      <span style="color: rgb(132,63,161);">"name"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"EntryAbility_desc"</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(132,63,161);">"value"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"description"</span>
    }<span style="color: rgb(181,106,1);">,</span>
    {
      <span style="color: rgb(132,63,161);">"name"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"EntryAbility_label"</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(132,63,161);">"value"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"label"</span>
    }
  ]
}
```

2. en_US目录中的string.json如下：
```json
{
  <span style="color: rgb(132,63,161);">"string"</span><span style="color: rgb(181,106,1);">: </span>[
    {
      <span style="color: rgb(132,63,161);">"name"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"module_desc"</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(132,63,161);">"value"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"module description"</span>
    }<span style="color: rgb(181,106,1);">,</span>
    {
      <span style="color: rgb(132,63,161);">"name"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"language_button"</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(132,63,161);">"value"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"Change Language"</span>
    }
  ]
}
```

3. zh_CN目录中的string.json如下：
```json
{
  <span style="color: rgb(132,63,161);">"string"</span><span style="color: rgb(181,106,1);">: </span>[
    {
      <span style="color: rgb(132,63,161);">"name"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"module_desc"</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(132,63,161);">"value"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"</span><span style="color: rgb(80,160,79);">模块描述</span><span style="color: rgb(80,160,79);">"</span>
    }<span style="color: rgb(181,106,1);">,</span>
    {
      <span style="color: rgb(132,63,161);">"name"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"language_button"</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(132,63,161);">"value"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"</span><span style="color: rgb(80,160,79);">改变语言</span><span style="color: rgb(80,160,79);">"</span>
    }
  ]
}
```

4. 点击按钮切换语言。
进入页面后，显示的语言将跟随系统偏好语言进行设置。
5. 设置语言状态status，当系统偏好语言为中文时，status设置为-1，英文时，status设置为1。
6. 因为本例子中仅有中英两种语言，所以点击按钮后status将切换状态。
 
 

#### 总结

无论是在APP内单独切换语言设置，还是跟随系统语言切换，多语言都需要通过两个步骤：
 1. 定义资源文件。
2. 引用资源文件。
 
另附跟随系统切换语言相关指南：[多语言支持](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-multiple-languages)。
