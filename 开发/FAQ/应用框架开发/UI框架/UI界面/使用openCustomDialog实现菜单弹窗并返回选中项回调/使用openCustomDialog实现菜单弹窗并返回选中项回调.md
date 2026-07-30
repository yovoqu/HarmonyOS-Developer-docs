# 使用openCustomDialog实现菜单弹窗并返回选中项回调

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-715

#### 问题现象

如何使用openCustomDialog实现一个从外部传参的菜单弹窗，并且可以在外部监听菜单项的选中状态。
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/QfF2XLtPRL-rZEzmh8cV6Q/zh-cn_image_0000002628395012.gif?HW-CC-KV=V1&HW-CC-Date=20260730T072440Z&HW-CC-Expire=86400&HW-CC-Sign=96AE08444F192CCB73375A73864C2B163C34799DF8EB2EB734852E84AF84C705)

 
 

#### 背景知识

[不依赖UI组件的全局自定义弹出框 (openCustomDialog)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-uicontext-custom-dialog)存在两种入参方式创建自定义弹出框，[ComponentContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-componentcontent#componentcontent-1)和[Builder](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builder)：
 
- ComponentContent封装内容可以与UI界面解耦，调用更加灵活。
- 使用Builder的方式，必须要与上下文做绑定，与UI存在一定耦合，具体请参考：[不依赖UI组件的全局自定义弹出框 (openCustomDialog)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-uicontext-custom-dialog)的说明部分和[@Builder装饰器使用说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builder#装饰器使用说明)。

 
 

#### 解决方案
1. 参考[完整示例](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-uicontext-custom-dialog#完整示例)实现弹窗工具类，其核心是以下属性的具体实现：
ctx：获取UI上下文用于实现弹窗服务。
2. contentNode：构建弹窗的内容节点，其中弹窗中菜单项的个数，内容和传给外部监听的回调通过Params类型的数组传递。
3. options：弹窗的配置选项，如位置、样式、动画等。
```text
export class <span style="color: rgb(0,0,255);">CustomerPromptAction </span><span style="color: rgb(255,0,170);">{</span>
  static <span style="color: rgb(0,0,255);">ctx</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">UIContext</span><span style="color: rgb(181,106,1);">;</span>
  static <span style="color: rgb(0,0,255);">contentNode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ComponentContent</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">Object</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">;</span>
  static <span style="color: rgb(0,0,255);">options</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">promptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BaseDialogOptions</span><span style="color: rgb(181,106,1);">;</span>

 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">定义方法，从外部传入上下文。</span></em>
  static <span style="color: rgb(0,0,255);">setContext</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">UIContext</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">CustomerPromptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ctx </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

<em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">配置内容节点。</span></em>
  static <span style="color: rgb(0,0,255);">setContentNode</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">UIContext</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">para</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Params</span><span style="color: rgb(0,0,255);">[]) </span><span style="color: rgb(255,0,170);">{</span>
    let <span style="color: rgb(0,0,255);">contentNode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ComponentContent</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">Object</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span>new <span style="color: rgb(0,0,255);">ComponentContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">wrapBuilder</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">buildText</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">para</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">CustomerPromptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">contentNode </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">contentNode</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">弹窗配置项。</span></em>
  static <span style="color: rgb(0,0,255);">setOptions</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">options</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">promptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BaseDialogOptions</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">CustomerPromptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">options </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">options</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">定义弹窗打开的方法。</span></em>
  static <span style="color: rgb(0,0,255);">openDialog</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">options</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">promptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BaseDialogOptions</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">UIContext</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">para</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Params</span><span style="color: rgb(0,0,255);">[]) </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">CustomerPromptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setContext</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">CustomerPromptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setContentNode</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">para</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">CustomerPromptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setOptions</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">alignment</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">DialogAlignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bottom</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">offset</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">dx</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">dy</span><span style="color: rgb(181,106,1);">: -</span><span style="color: rgb(255,0,0);">20 </span><span style="color: rgb(255,0,170);">} }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">CustomerPromptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">contentNode </span><span style="color: rgb(181,106,1);">!== </span>null<span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">CustomerPromptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ctx</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPromptAction</span><span style="color: rgb(0,0,255);">()</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">openCustomDialog</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">CustomerPromptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">contentNode</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">options</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>

 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">关闭弹窗。</span></em>
  static <span style="color: rgb(0,0,255);">closeDialog</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">CustomerPromptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">contentNode </span><span style="color: rgb(181,106,1);">!== </span>null<span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">CustomerPromptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ctx</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPromptAction</span><span style="color: rgb(0,0,255);">()</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">closeCustomDialog</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">CustomerPromptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">contentNode</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>
<span style="color: rgb(255,0,170);">}</span>
```

4. 在页面中调用弹窗。
自定义菜单项实体类，声明属性方法，并通过构造器实例化。
```text
export class <span style="color: rgb(0,0,255);">Params </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">title</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">""</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">iconName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Resource</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">click</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">void</span><span style="color: rgb(181,106,1);">;</span>

  constructor<span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">title</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">iconName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Resource</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">click</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">void</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">title </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">title</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">iconName </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">iconName</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">click </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">click</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

5. 定义接收菜单项选中回调的函数，根据返回的index处理逻辑。
```text
<em>// </em><em><span style="color: rgb(128,128,128);">点击弹窗中按钮的回调，并根据返回的</span><span style="color: rgb(128,128,128);">index</span><span style="color: rgb(128,128,128);">判断逻辑。</span></em>
<span style="color: rgb(0,0,255);">callBack </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
  switch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    case <span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">:</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPromptAction</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showToast</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">点击了关闭</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">2000</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      break<span style="color: rgb(181,106,1);">;</span>
    case <span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">:</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPromptAction</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showToast</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">点击了刷新</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">2000</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      break<span style="color: rgb(181,106,1);">;</span>
    case <span style="color: rgb(255,0,0);">2</span><span style="color: rgb(181,106,1);">:</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPromptAction</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showToast</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">点击了帮助</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">2000</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      break<span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
```

6. 初始化菜单数据源。
```text
<span style="color: rgb(181,106,1);">@</span><span style="color: rgb(0,0,255);">State </span><span style="color: rgb(181,106,1);">arr</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Params</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[</span>
  new <span style="color: rgb(0,0,255);">Params</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">关闭</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.media.startIcon'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">callBack</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">,</span>
  new <span style="color: rgb(0,0,255);">Params</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">刷新</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.media.startIcon'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">callBack</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">,</span>
  new <span style="color: rgb(0,0,255);">Params</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">帮助</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.media.startIcon'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">callBack</span><span style="color: rgb(0,0,255);">)]</span><span style="color: rgb(181,106,1);">;</span>
```

 
完整示例参考如下：
 1. CustomerPromptAction.ets。
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">ComponentContent</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">promptAction </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">UIContext </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@ohos.arkui.UIContext'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">Params </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'./Params'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Builder</span>
function <span style="color: rgb(0,0,255);">buildText</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">params</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Params</span><span style="color: rgb(0,0,255);">[]) </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Flex</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">direction</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">FlexDirection</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SpaceAround </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">ForEach</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">params</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Params</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">Image</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">iconName</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">30</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">30</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">click</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">title</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">15</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

    <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">取消</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">50</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textAlign</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">TextAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Blue</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">CustomerPromptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">closeDialog</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'#FFF0F0F0'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderRadius</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">10</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
export class <span style="color: rgb(0,0,255);">CustomerPromptAction </span><span style="color: rgb(255,0,170);">{</span>
  static <span style="color: rgb(0,0,255);">ctx</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">UIContext</span><span style="color: rgb(181,106,1);">;</span>
  static <span style="color: rgb(0,0,255);">contentNode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ComponentContent</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">Object</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">;</span>
  static <span style="color: rgb(0,0,255);">options</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">promptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BaseDialogOptions</span><span style="color: rgb(181,106,1);">;</span>

  <em>// </em><em><span style="color: rgb(128,128,128);">定义方法，从外部传入上下文。</span></em>
  static <span style="color: rgb(0,0,255);">setContext</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">UIContext</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">CustomerPromptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ctx </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">配置内容节点。</span></em>
  static <span style="color: rgb(0,0,255);">setContentNode</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">UIContext</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">para</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Params</span><span style="color: rgb(0,0,255);">[]) </span><span style="color: rgb(255,0,170);">{</span>
    let <span style="color: rgb(0,0,255);">contentNode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ComponentContent</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">Object</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span>new <span style="color: rgb(0,0,255);">ComponentContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">wrapBuilder</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">buildText</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">para</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">CustomerPromptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">contentNode </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">contentNode</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

<em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">弹窗配置项。</span></em>
  static <span style="color: rgb(0,0,255);">setOptions</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">options</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">promptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BaseDialogOptions</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">CustomerPromptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">options </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">options</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

<em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">定义弹窗打开的方法。</span></em>
  static <span style="color: rgb(0,0,255);">openDialog</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">options</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">promptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BaseDialogOptions</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">UIContext</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">para</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Params</span><span style="color: rgb(0,0,255);">[]) </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">CustomerPromptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setContext</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">CustomerPromptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setContentNode</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">para</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">CustomerPromptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setOptions</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">alignment</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">DialogAlignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bottom</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">offset</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">dx</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">dy</span><span style="color: rgb(181,106,1);">: -</span><span style="color: rgb(255,0,0);">20 </span><span style="color: rgb(255,0,170);">} }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">CustomerPromptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">contentNode </span><span style="color: rgb(181,106,1);">!== </span>null<span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">CustomerPromptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ctx</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPromptAction</span><span style="color: rgb(0,0,255);">()</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">openCustomDialog</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">CustomerPromptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">contentNode</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">options</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>

  <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">关闭弹窗。</span></em>
  static <span style="color: rgb(0,0,255);">closeDialog</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">CustomerPromptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">contentNode </span><span style="color: rgb(181,106,1);">!== </span>null<span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">CustomerPromptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ctx</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPromptAction</span><span style="color: rgb(0,0,255);">()</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">closeCustomDialog</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">CustomerPromptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">contentNode</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>
<span style="color: rgb(255,0,170);">}</span>
```

2. Index.ets。
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">Params </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'./Params'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">CustomerPromptAction </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'./CustomerPromptAction'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
<em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">点击弹窗中按钮的回调，并根据返回的</span><span style="color: rgb(128,128,128);">index</span><span style="color: rgb(128,128,128);">判断逻辑。</span></em>
  <span style="color: rgb(0,0,255);">callBack </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    switch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      case <span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">:</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPromptAction</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showToast</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">点击了关闭</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">2000</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        break<span style="color: rgb(181,106,1);">;</span>
      case <span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">:</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPromptAction</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showToast</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">点击了刷新</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">2000</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        break<span style="color: rgb(181,106,1);">;</span>
      case <span style="color: rgb(255,0,0);">2</span><span style="color: rgb(181,106,1);">:</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPromptAction</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showToast</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">点击了帮助</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">2000</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        break<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span><span style="color: rgb(181,106,1);">;</span>
  <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">初始化弹窗菜单的数据源。</span></em>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">arr</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Params</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[</span>
    new <span style="color: rgb(0,0,255);">Params</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">关闭</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.media.startIcon'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">callBack</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">,</span>
    new <span style="color: rgb(0,0,255);">Params</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">刷新</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.media.startIcon'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">callBack</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">,</span>
    new <span style="color: rgb(0,0,255);">Params</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">帮助</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.media.startIcon'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">callBack</span><span style="color: rgb(0,0,255);">)]</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">横向菜单</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">50 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">CustomerPromptAction</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">openDialog</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">alignment</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">DialogAlignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bottom</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(0,0,255);">offset</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">dx</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">dy</span><span style="color: rgb(181,106,1);">: -</span><span style="color: rgb(255,0,0);">20 </span><span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">            }</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">arr</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

3. Params.ets。
```text
export class <span style="color: rgb(0,0,255);">Params </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">title</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">""</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">iconName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Resource</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">click</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">void</span><span style="color: rgb(181,106,1);">;</span>

  constructor<span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">title</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">iconName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Resource</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">click</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">void</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">title </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">title</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">iconName </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">iconName</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">click </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">click</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
