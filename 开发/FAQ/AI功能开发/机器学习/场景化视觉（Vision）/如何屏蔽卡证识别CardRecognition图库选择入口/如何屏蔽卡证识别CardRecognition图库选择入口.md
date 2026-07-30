# 如何屏蔽卡证识别CardRecognition图库选择入口

更新时间：2026-07-30 01:18:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-vision-12

#### 问题现象

高端理财身份证OCR识别，不能使用照片，只能拍照或者扫描有没有办法把图库选择的入口屏蔽？
 
 

#### 背景知识

[卡证识别](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/vision-cardrecognition)控件提供身份证（目前仅支持中国大陆二代身份证，且不包含民汉双文身份证）、行驶证、驾驶证、护照、银行卡的结构化识别服务，满足卡证的自动分类功能，系统可自动判断所属卡证类型并返回结构化信息和卡证图片信息。
 
对于需要填充卡证信息的场景，如身份证、银行卡信息等，可使用卡证识别控件读取OCR（Optical Character Recognition）信息，将结果信息返回后进行填充。支持单独识别正面、反面，或同时进行双面识别。
 
 

#### 解决方案

在卡证识别控件的参数配置对象[CardRecognitionConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vision-card-recognition#cardrecognitionconfig)中有一个isPhotoSelectionSupported参数，可以控制在卡证识别时是否支持从图库中选取图片进行识别。参数说明如下：
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isPhotoSelectionSupported | boolean | 否 | 是 | 是否支持从图库选图。 true为显示图库按钮并支持从图库选图。false为不显示图库按钮且不支持从图库选图。默认值：true。 元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
 
 
只需要在CardRecognitionConfig对象配置时将isPhotoSelectionSupported设置为false即可。
 
完整示例参考如下：
 
CardDemoPage.ets：
 
```json
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">CardRecognition</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">CardRecognitionResult</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">CardType</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">CardSide</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">ShootingMode </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.VisionKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">hilog </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.PerformanceAnalysisKit'</span><span style="color: rgb(181,106,1);">;</span>

const <span style="color: rgb(255,255,255);">TAG</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'CardRecognitionPage'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Component</span>
export struct <span style="color: rgb(0,0,255);">CardDemoPage </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">cardDataSource</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Record</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(255,0,170);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">[]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@Consume</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'pathStack'</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">NavPathStack</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">NavDestination</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">alignContent</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">Alignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Top </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">cardDataShowBuilder</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'80%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'80%'</span><span style="color: rgb(255,0,170);">)</span>

        <span style="color: rgb(0,0,255);">CardRecognition</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">supportType</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">CardType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">CARD_ID</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(255,255,255);">cardSide</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">CardSide</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">DEFAULT</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(255,255,255);">cardRecognitionConfig</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">defaultShootingMode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">ShootingMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">MANUAL</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,255,255);">isPhotoSelectionSupported</span><span style="color: rgb(181,106,1);">: </span>false<span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,255,255);">setCardMargins</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(80,160,79);">100</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(255,255,255);">onResult</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">params</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">CardRecognitionResult</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(0x0001</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">TAG</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">`params code: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">params</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">params</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code </span><span style="color: rgb(181,106,1);">!== </span><span style="color: rgb(80,160,79);">200</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pop</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span>
            <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(0x0001</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">TAG</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">`params cardType: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">params</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">cardType</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">params</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">cardInfo</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(255,255,255);">front </span><span style="color: rgb(181,106,1);">!== </span>undefined<span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">cardDataSource</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">params</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">cardInfo</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(255,255,255);">front</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span>

            if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">params</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">cardInfo</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(255,255,255);">back </span><span style="color: rgb(181,106,1);">!== </span>undefined<span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">cardDataSource</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">params</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">cardInfo</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(255,255,255);">back</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span>

            if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">params</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">cardInfo</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(255,255,255);">main </span><span style="color: rgb(181,106,1);">!== </span>undefined<span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">cardDataSource</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">params</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">cardInfo</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(255,255,255);">main</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span>
            <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(0x0001</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">TAG</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">`params cardInfo front: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">params</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">cardInfo</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(255,255,255);">front</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,255,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(0x0001</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">TAG</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">`params cardInfo back: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">params</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">cardInfo</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(255,255,255);">back</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hideTitleBar</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(181,106,1);">@Builder</span>
  <span style="color: rgb(0,0,255);">cardDataShowBuilder</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">List</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">ForEach</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">cardDataSource</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">cardData</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Record</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">ListItem</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(0,0,255);">Image</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">cardData</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">cardImageUri</span><span style="color: rgb(255,0,170);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">objectFit</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">ImageFit</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Contain</span><span style="color: rgb(255,0,170);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(255,0,170);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(255,0,170);">)</span>

            <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">cardData</span><span style="color: rgb(255,0,170);">))</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">12</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">        }</span>
<span style="color: rgb(181,106,1);">      }</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listDirection</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Axis</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Vertical</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignListItem</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">ListItemAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">50</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
Index.ets：
 
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">CardDemoPage </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'./CardDemoPage'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">MainPage </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@Provide</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'pathStack'</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">NavPathStack </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">NavPathStack</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(181,106,1);">@Builder</span>
  <span style="color: rgb(0,0,255);">PageMap</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">name </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(132,63,161);">'cardRecognition'</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">CardDemoPage</span><span style="color: rgb(255,0,170);">()</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">卡证识别入口按钮</span></em>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Navigation</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'CardRecognition'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">stateEffect</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">ButtonType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Capsule </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'50%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">40</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">pathStack</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pushPath</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'cardRecognition' </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">title</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">卡证识别控件</span><span style="color: rgb(132,63,161);">demo'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">navDestination</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">PageMap</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mode</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">NavigationMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Stack</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
