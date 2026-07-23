# Natural Language Kit获取Entity中缺少rrule字段

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-natural-language-1

#### 问题现象

在5.0.1.130版本上使用[getEntity](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/natural-language-text-processing-api#section6469197174917)接口，返回回来的[jsonObject](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/natural-language-json-object-api)少了一个rrule字段。
 
问题代码示例参考如下：
 
```json
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">textProcessing</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">EntityType </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.NaturalLanguageKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">inputText</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">outputText</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">每周四晚上</span><span style="color: rgb(128,128,128);">10</span><span style="color: rgb(128,128,128);">点</span></em>
      <span style="color: rgb(0,0,255);">TextInput</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">placeholder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">请输入文本</span><span style="color: rgb(255,0,170);">' </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">40</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">16</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'90%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">10</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">inputText </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(0,0,255);">Scroll</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">outputText</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">16</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'90%'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">10</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'40%'</span><span style="color: rgb(0,0,255);">)</span>

     <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">调用实体抽取接口</span></em>
      <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">获取实体结果</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">type</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">ButtonType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Capsule</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">White</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'45%'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">10</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(</span>async <span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            try <span style="color: rgb(255,0,170);">{</span>
              let <span style="color: rgb(0,0,255);">result </span><span style="color: rgb(181,106,1);">= </span>await <span style="color: rgb(0,0,255);">textProcessing</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getEntity</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">inputText</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">entityTypes</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">EntityType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">DATETIME</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">outputText </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">formatEntityResult</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">result</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`getEntity errorCode: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, errorMessage: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">outputText </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'Error occurred while getting entities.'</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">          }</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>

 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">实体结果转义</span></em>
  private <span style="color: rgb(0,0,255);">formatEntityResult</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">entities</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">textProcessing</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Entity</span><span style="color: rgb(0,0,255);">[])</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(255,0,170);">{</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(0,0,255);">entities </span><span style="color: rgb(181,106,1);">|| !</span><span style="color: rgb(0,0,255);">entities</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      return <span style="color: rgb(255,0,170);">'No entities found.'</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    let <span style="color: rgb(0,0,255);">output </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'Entities:</span>\n<span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">;</span>
    for <span style="color: rgb(0,0,255);">(</span>let <span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(0,0,255);">entities</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      let <span style="color: rgb(0,0,255);">entity </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">entities</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">output </span><span style="color: rgb(181,106,1);">+= </span><span style="color: rgb(255,0,170);">`Entity[</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">]:\n`</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">output </span><span style="color: rgb(181,106,1);">+= </span><span style="color: rgb(255,0,170);">`oriText: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">entity</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">\n`</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">output </span><span style="color: rgb(181,106,1);">+= </span><span style="color: rgb(255,0,170);">`charOffset: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">entity</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">charOffset</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">\n`</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">output </span><span style="color: rgb(181,106,1);">+= </span><span style="color: rgb(255,0,170);">`entityType: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">entity</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">type</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">\n`</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">output </span><span style="color: rgb(181,106,1);">+= </span><span style="color: rgb(255,0,170);">`jsonObject: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">entity</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">jsonObject</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">\n\n`</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    return <span style="color: rgb(0,0,255);">output</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
输出结果如下：
 
```text
{
  "containFuzzySection": "E",
  "inferType": "ABSOLUTE",
  "isChangedIllegal": false,
  "isContainFuzzyTime": true,
  "isFestival": false,
  "isIllegal": false,
  "isLunarTime": false,
  "isPlusTwelveHour": false,
  "isSolarTerm": false,
  "minSection": "P",
  "oriFestival": "",
  "originTimestamp": <span style="color: rgb(0,0,255);">1750684503227</span>,
  "rangeDecoration": "POINT",
  "rangeText": "每周四晚上10点",
  "repeat": "W4",
  "sequence": <span style="color: rgb(0,0,255);">1</span>,
  "start": "T22:00:00",
  "startTimestamp": <span style="color: rgb(0,0,255);">1750946400000</span>,
  "timestampZone": "Asia/Shanghai"
}
```
 
 

#### 解决方案

从5.0.1.130版本开始，rrule字段以后不会输出了，请使用repeat字段替代，repeat字段的使用规范如下：
  
| repeat | 说明 |
| --- | --- |
| Y | 每年 |
| Y3 | 每年3月 |
| Y3.6 | 每年3月6日 |
| Y3.6-Y5.2 | 每年3月6日到5月2日 |
| M | 每月 |
| M2 | 每月2日 |
| M2-M5 | 每月2日到5日 |
| W | 每周 |
| W3 | 每周三 |
| W3-W5 | 每周三到每周五 |
| workingDay | 法定工作日 |
| holiday | 节假日 |
