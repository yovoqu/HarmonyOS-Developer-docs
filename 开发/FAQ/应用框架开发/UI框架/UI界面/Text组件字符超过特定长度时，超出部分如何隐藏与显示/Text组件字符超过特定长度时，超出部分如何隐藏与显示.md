# Text组件字符超过特定长度时，超出部分如何隐藏与显示

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1409

#### 问题现象

在Text中显示文本时，如果文本超过一定长度，通常会有超出部分隐藏与显示的需求，例如：当最多显示的行数为2，组件宽度比例为0.4时，该如何实现？
 
 

#### 背景知识

- [measureText](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-measureutils#measuretext12)方法能够根据文本信息计算文本宽度。
- [getAllDisplays](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#displaygetalldisplays9)方法能够获取display对象，display对象的width属性为屏幕的宽度。

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/r1xThnd5Q-SCmDhTNqZpnw/zh-cn_image_0000002658842531.png?HW-CC-KV=V1&HW-CC-Date=20260811T005651Z&HW-CC-Expire=86400&HW-CC-Sign=42A45AA6975363CD91FA1996541F48795D1C700A821265FCB6A23C56234A216E)

 
 

#### 解决方案
1. 首先设定的文本长度计算方式：设定文本长度 = 屏幕宽度 * 最大行数 * 组件宽度比例。屏幕宽度可以使用[getAllDisplays](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#displaygetalldisplays9)获取。
2. 然后使用[measureText](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-measureutils#measuretext12)方法测量实际文本宽度，比较“设定文本长度”与“实际文本宽度”进行大小比较，判断是否需要隐藏。
3. 当需要隐藏时，只展示“设定长度”的文本内容，超出部分显示为“...”。当点击“…”时将该文本变为“…收起”，显示隐藏部分内容。
 
完整示例参考如下：
 
```json
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">MeasureUtils </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(0,0,255);">curves </span>from <span style="color: rgb(255,0,170);">'@ohos.curves'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@ohos.base'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(0,0,255);">display </span>from <span style="color: rgb(255,0,170);">'@ohos.display'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">长文本</span></em>
  <span style="color: rgb(0,0,255);">longMessage</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">走在繁华的城市街头，明空感到无比紧张。他的心跳如雷鼓般擂动着胸膛，使得身上的伪装仿佛随时都要被揭开。然而，他仍然保持着冷静，凭借着过人的胆识与智慧，成功地躲过了敌人的层层封锁。</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
    <span style="color: rgb(255,0,170);">'</span>\n<span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+</span>
    <span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">　　最终，明空来到了敌对帮派的老巢。此时此刻，那里的守卫正沉浸在欢庆的氛围中，丝毫没有察觉到即将来临的危机。明空深吸一口气，压抑住内心的激动，悄然潜入了这座古老的建筑。</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">;</span>
 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">最大显示行数</span></em>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">lines</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(181,106,1);">;</span>
  <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">长文本状态（展开</span><span style="color: rgb(128,128,128);"> or </span><span style="color: rgb(128,128,128);">收起）</span></em>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">collapseText</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'...'</span><span style="color: rgb(181,106,1);">;</span>
 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">屏幕宽度（单位</span><span style="color: rgb(128,128,128);">px</span><span style="color: rgb(128,128,128);">）</span></em>
  <span style="color: rgb(0,0,255);">screenWidth</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
  <em>// </em><em><span style="color: rgb(128,128,128);">是否需要显示</span><span style="color: rgb(128,128,128);">"</span><span style="color: rgb(128,128,128);">展开</span><span style="color: rgb(128,128,128);">"</span><span style="color: rgb(128,128,128);">字样（注：当文本长度较短时就不需要</span><span style="color: rgb(128,128,128);">“</span><span style="color: rgb(128,128,128);">展开</span><span style="color: rgb(128,128,128);">”</span><span style="color: rgb(128,128,128);">）</span></em>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">isExpanded</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">uiContext</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">UIContext </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">uiContextMeasure</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">MeasureUtils </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">uiContext</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getMeasureUtils</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">测量文本宽度（单位</span><span style="color: rgb(128,128,128);">px</span><span style="color: rgb(128,128,128);">）</span></em>
  <span style="color: rgb(0,0,255);">textWidth</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">uiContextMeasure</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">measureText</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">textContent</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">longMessage</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取当前所有的</span><span style="color: rgb(128,128,128);">display</span><span style="color: rgb(128,128,128);">对象</span></em>
  <span style="color: rgb(0,0,255);">promise</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Promise</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">display</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Display</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(0,0,255);">display</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getAllDisplays</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">文本宽度为：</span><span style="color: rgb(255,0,170);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textWidth</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">promise</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">display</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Display</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">所有的屏幕信息：</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">单位为像素</span></em>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">screenWidth </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">][</span><span style="color: rgb(255,0,170);">"width"</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
    <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">屏幕宽度</span><span style="color: rgb(128,128,128);"> * </span><span style="color: rgb(128,128,128);">最大行数</span><span style="color: rgb(128,128,128);"> * </span><span style="color: rgb(128,128,128);">组件宽度比例 和 文字测量宽度</span></em>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isExpanded </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">screenWidth </span><span style="color: rgb(181,106,1);">* </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lines </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(255,0,0);">0.4 </span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textWidth</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Failed to obtain all the display objects. Code: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isExpanded</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">alignContent</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Alignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BottomEnd </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">longMessage</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Black</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">maxLines</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lines</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">"40%"</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">collapseText</span><span style="color: rgb(0,0,255);">)</span>
                <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(0,0,255);">)</span>
                <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">White</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(255,0,170);">}</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">End</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
              if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">collapseText </span><span style="color: rgb(181,106,1);">== </span><span style="color: rgb(255,0,170);">'...'</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
                this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">collapseText </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'...</span><span style="color: rgb(255,0,170);">收起</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">;</span>
              <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">展开动画</span></em>
                this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">uiContext</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">animateTo</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
                  <span style="color: rgb(0,0,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">150</span><span style="color: rgb(181,106,1);">,</span>
                  <span style="color: rgb(0,0,255);">curve</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">curves</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">springMotion</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">0.5</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">0.8</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">,</span>
                <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
                  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lines </span><span style="color: rgb(181,106,1);">= -</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">使得设置的最大行属性无效</span></em>
                <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
                this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">collapseText </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'...'</span><span style="color: rgb(181,106,1);">;</span>
               <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">收起动画</span></em>
                this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">uiContext</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">animateTo</span><span style="color: rgb(0,0,255);">(</span>
                  <span style="color: rgb(255,0,170);">{</span>
                    <span style="color: rgb(0,0,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">100</span><span style="color: rgb(181,106,1);">,</span>
                    <span style="color: rgb(0,0,255);">curve</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Curve</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Friction</span><span style="color: rgb(181,106,1);">,</span>
                  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
                  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lines </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">只显示</span><span style="color: rgb(128,128,128);">2</span><span style="color: rgb(128,128,128);">行</span></em>
                <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">            }</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span>
        else <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">longMessage</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Black</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">      }</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
 

#### 常见FAQ

Q：如何设置文字超出宽度后继续显示，不要滚动？
 
A：只使用textOverflow属性不能实现这种效果，可以使用Row嵌套Text，再动态设置文字宽度来实现类似效果。
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">MeasureUtils </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">TextDemo </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">textString</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">我是超长文本，超出的部分显示。</span><span style="color: rgb(255,0,170);">I am an extra long text'</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">textWidth</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">uiContext</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">UIContext </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">uiContextMeasure</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">MeasureUtils </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">uiContext</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getMeasureUtils</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">textSize</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">14</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">计算文字宽度</span></em>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textWidth </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">uiContextMeasure</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">measureText</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">textContent</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textString</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textSize</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textString</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textSize</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">maxLines</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textWidth</span><span style="color: rgb(181,106,1);">+</span><span style="color: rgb(255,0,170);">'px'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Pink</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">250</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">border</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignItems</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Start</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
