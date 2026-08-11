# 如何设置Text组件的缩进避让

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-625

#### 问题现象

当Text组件与其他组件堆叠出现时，Text的文字内容需获取其他组件的宽高数据，进行缩进避让。
 
 

#### 背景知识

- [Stack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-stack)堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。
- [RelativeContainer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-relativecontainer)，相对布局，子组件间通过相对位置的布局，实现多个组件层叠显示的效果。
- [onAreaChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-component-area-change-event#onareachange)，获取组件的组件大小、位置信息。
- [textIndent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#textindent10)，设置Text组件首行文本缩进。
- [ContainerSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-containerspan)组件为Text组件的子组件，用于统一管理多个Span、ImageSpan的背景色及圆角弧度。可以包含Span、ImageSpan子组件。

 
 

#### 解决方案

- **方案一**：问题描述提到组件堆叠，则可用Stack布局，通过设置缩进，为文本标签留下空间。
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">ExampleOne </span><span style="color: rgb(181,106,1);">{</span>
  private <span style="color: rgb(255,255,255);">dynamicText</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">标签</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">alignContent</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">Alignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">TopStart </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">这是详细内容这是详细内容这是详细内容这是详细内容这是详细内容这是详细内容</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">30</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textIndent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">60</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>

      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">dynamicText</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">20</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">50</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">border</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">width</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">color</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Black</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">radius</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">10 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textAlign</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">TextAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">20</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/XXMdXGLxSpyXpdpGr_RXxw/zh-cn_image_0000002658913485.png?HW-CC-KV=V1&HW-CC-Date=20260811T005716Z&HW-CC-Expire=86400&HW-CC-Sign=D6957E891C2F0257E1C402F3BDDE4AD5D10B70161EB2CE91910630DB97148032)

- **方案二**：获取其他组件宽度并设置Text组件的缩进避让。1. 在通过RelativeContainer相对布局，实现标题Row组件和内容Text组件的相同位置显示，但此时两个组件内容会有重叠遮挡。

2. 通过onAreaChange获取标题Row组件的宽度信息（this.titleWidth），转换为number类型。
```json
<span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">短剧</span><span style="color: rgb(132,63,161);">·</span><span style="color: rgb(132,63,161);">中国版教父</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span>
<span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#a3cf62'</span><span style="color: rgb(255,0,170);">)</span>
<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">4</span><span style="color: rgb(255,0,170);">)</span>
<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderRadius</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">4</span><span style="color: rgb(255,0,170);">)</span>
<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'row1'</span><span style="color: rgb(255,0,170);">)</span>
<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignRules</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'text'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">VerticalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Top </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,255,255);">left</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'text'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Start </span><span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onAreaChange</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">oldValue</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Area</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">newValue</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Area</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">sizeValue </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">newValue</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">titleWidth </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">parseInt</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">sizeValue</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">split</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'width":'</span><span style="color: rgb(255,0,170);">)[</span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">split</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">','</span><span style="color: rgb(255,0,170);">)[</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">])</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">获取标题组件的宽度</span></em>
<span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
```


3. 配置Text组件的首行缩进长度为第二步获取的Row组件的宽度（this.titleWidth），实现文字避让。
```text
<span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">key</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'text'</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">maxLines</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">lines</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lineHeight</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">26</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textIndent</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">titleWidth </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(80,160,79);">2</span><span style="color: rgb(255,0,170);">)</span>
```


  完整示例参考如下：

  
```json
const <span style="color: rgb(255,255,255);">COLLAPSE_LINES</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">2</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">ExampleTwo </span><span style="color: rgb(181,106,1);">{</span>
  private <span style="color: rgb(255,255,255);">lines</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">COLLAPSE_LINES</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">sizeValue</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">titleWidth</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">这里是详情内容，这里是详情内容，这里是详情内容，这里是详情内容</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">RelativeContainer</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">key</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'text'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">maxLines</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">lines</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lineHeight</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">26</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textIndent</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">titleWidth </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(80,160,79);">2</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">短剧</span><span style="color: rgb(132,63,161);">·</span><span style="color: rgb(132,63,161);">中国版教父</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#a3cf62'</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">4</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderRadius</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">4</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'row1'</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignRules</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'text'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">VerticalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Top </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,255,255);">left</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'text'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Start </span><span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">      }</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onAreaChange</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">oldValue</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Area</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">newValue</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Area</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">sizeValue </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">newValue</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">titleWidth </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">parseInt</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">sizeValue</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">split</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'width":'</span><span style="color: rgb(255,0,170);">)[</span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">split</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">','</span><span style="color: rgb(255,0,170);">)[</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">])</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">获取标题组件的宽度</span></em>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'auto'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderWidth</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">left</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">8</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">right</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">8 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/dLtkq2N1TuCblRA-N2Qsew/zh-cn_image_0000002658793535.png?HW-CC-KV=V1&HW-CC-Date=20260811T005716Z&HW-CC-Expire=86400&HW-CC-Sign=A2DF89FEE144A3BCEDB32AC45E958BE36797B40239590372CF0A515247F4F46D)


 
- **方案三**：可以使用ContainerSpan组件，作为设置Text组件的缩进避让的替代方案，可参考官方文档[通过attributemodifier设置背景样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-containerspan#示例2通过attributemodifier设置背景样式)。可在组件内使用Span、ImageSpan组件。但此方法不支持通用属性和通用事件，有一定局限性。
