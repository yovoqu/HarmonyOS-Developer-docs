# 如何修改TextReader控件在屏幕纵向的起始位置

更新时间：2026-07-30 01:18:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-speech-3

#### 问题现象

[TextReader（朗读控件）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/speech-textreader-api)在屏幕垂直方向的位置固定，可以左右拖动，如何修改其在屏幕纵向的起始位置？
 
 

#### 背景知识

TextReader：朗读控件使用AI能力将文本实时转化成语音并进行朗读，适用于一些新闻类文本内容浏览类APP，帮助用户在一些无法直接浏览文本内容的场景下，通过文本朗读来高效获取信息。
 
[MinibarParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/speech-textreader-api#minibarparams)：用来设置Minibar初始化位置，以及与底部边框的距离。
 
 

#### 解决方案

可以通过设置参数MinibarParams中的bottom的值调整朗读控件离底部边缘的距离，从而达到修改控件在屏幕纵向的起始位置的效果，示例代码如下：
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">TextReader</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">TextReaderIcon</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">ReadStateCode </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.SpeechKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>

  <em>/**</em>
<em><span style="color: rgb(128,128,128);">   * </span><span style="color: rgb(128,128,128);">待加载的文章</span></em>
<em><span style="color: rgb(128,128,128);">   */</span></em>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">readInfoList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TextReader</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ReadInfo</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">selectedReadInfo</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TextReader</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ReadInfo </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">readInfoList</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>

<em>  <span style="color: rgb(128,128,128);">/**</span></em>
<em><span style="color: rgb(128,128,128);">   * </span><span style="color: rgb(128,128,128);">播放状态</span></em>
<em><span style="color: rgb(128,128,128);">   */</span></em>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">readState</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ReadStateCode </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">ReadStateCode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WAITING</span><span style="color: rgb(181,106,1);">;</span>

  <em>/**</em>
<em><span style="color: rgb(128,128,128);">   * </span><span style="color: rgb(128,128,128);">用于显示当前页的按钮状态</span></em>
<em><span style="color: rgb(128,128,128);">   */</span></em>
  private <span style="color: rgb(0,0,255);">isInit</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>

  async <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <em><span style="color: rgb(128,128,128);">/**</span></em>
<em><span style="color: rgb(128,128,128);">     * </span><span style="color: rgb(128,128,128);">加载数据</span></em>
<em><span style="color: rgb(128,128,128);">     */</span></em>
    let <span style="color: rgb(0,0,255);">readInfoList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TextReader</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ReadInfo</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">id</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'001'</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">title</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">水调歌头</span><span style="color: rgb(255,0,170);">.</span><span style="color: rgb(255,0,170);">明月几时有</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">isClickable</span><span style="color: rgb(181,106,1);">:</span>true
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">author</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">宋</span><span style="color: rgb(255,0,170);">.</span><span style="color: rgb(255,0,170);">苏轼</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">isClickable</span><span style="color: rgb(181,106,1);">:</span>true
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">date</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,170);">'2024/01/01'</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">isClickable</span><span style="color: rgb(181,106,1);">:</span>false
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">bodyInfo</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">明月几时有？把酒问青天。</span><span style="color: rgb(255,0,170);">'</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">readInfoList </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">readInfoList</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectedReadInfo </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">readInfoList</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">init</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <em><span style="color: rgb(128,128,128);">/**</span></em>
<em><span style="color: rgb(128,128,128);">   * </span><span style="color: rgb(128,128,128);">初始化</span></em>
<em><span style="color: rgb(128,128,128);">   */</span></em>


  async <span style="color: rgb(0,0,255);">init</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    const <span style="color: rgb(0,0,255);">readerParam</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TextReader</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ReaderParam </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">isVoiceBrandVisible</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">businessBrandInfo</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">panelName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">小艺朗读</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">panelIcon</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.media.startIcon'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">minibarParams</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">defaultAlignment</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">70</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(181,106,1);">;</span>
    try <span style="color: rgb(255,0,170);">{</span>
      let <span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Context </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">undefined </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        await <span style="color: rgb(0,0,255);">TextReader</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">init</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">readerParam</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isInit </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setActionListener</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    } </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`TextReader failed to init. Code: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, message: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>

<em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置操作监听</span></em>
  <span style="color: rgb(0,0,255);">setActionListener</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">TextReader</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'stateChange'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">state</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TextReader</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ReadState</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onStateChanged</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">state</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

    <span style="color: rgb(0,0,255);">TextReader</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'requestMore'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">TextReader</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadMore</span><span style="color: rgb(0,0,255);">([]</span><span style="color: rgb(181,106,1);">, </span>true<span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">onStateChanged </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">state</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TextReader</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ReadState</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectedReadInfo</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">id </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">state</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">readState </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">state</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">state</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">readState </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">ReadStateCode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WAITING</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">TextReaderIcon</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">readState</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">readState </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">right</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">32</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">32</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(</span>async <span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          try <span style="color: rgb(255,0,170);">{</span>
            await <span style="color: rgb(0,0,255);">TextReader</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">start</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">readInfoList</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectedReadInfo</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`TextReader failed to start. Code: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, message: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
