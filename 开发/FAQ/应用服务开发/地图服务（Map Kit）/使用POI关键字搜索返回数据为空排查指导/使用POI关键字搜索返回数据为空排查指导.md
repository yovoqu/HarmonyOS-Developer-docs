# 使用POI关键字搜索返回数据为空排查指导

更新时间：2026-08-12 10:47:00

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-14

#### 问题现象

使用关键字搜索获取不到结果，POI关键字搜索返回数据为空。
 
 

#### 背景知识

[POI搜索](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-site-search)提供多种查询POI信息的能力：
 
- [关键字搜索](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-site-search#关键字搜索)：通过指定的关键字和可选的地理范围，查询诸如旅游景点、企业和学校之类的地点。
- [周边搜索](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-site-search#周边搜索)：基于用户设备位置进行地点查找。
- [自动补全](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-site-search#自动补全)：根据输入的关键字返回预测的输入关键字和地点查询建议。
- [地点详情](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-site-search#地点详情)：查询某个地点更详细的信息。

 
 

#### 问题定位
1. 首先需要排查下是否[开通地图服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-config-agc#开通地图服务)。
2. 开启“地图服务”开放能力后，是否完成[手动签名](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing#section297715173233)。
3. 若使用原有的Profile文件，还要确保在申请Profile文件之前已开启“地图服务”，否则开启后需要重新申请Profile文件，并重新配置签名信息。
 
 

#### 分析结论

开通地图服务后未更新调试证书添加公钥指纹和调试Profile，DevEco Studio未更新手动签名的文件，导致地图服务开通却未生效。
 
 

#### 修改建议

步骤如下：
 1. 在[AGC](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)创建对应的项目并添加相应的应用，同时“开通地图服务”；
2. [申请调试证书](https://developer.huawei.com/consumer/cn/doc/app/agc-help-debug-cert-0000002283256797)、[配置公钥指纹](https://developer.huawei.com/consumer/cn/doc/app/agc-help-cert-fingerprint-0000002278002933)，使用添加指纹后的调试证书去[申请调试Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-debug-profile-0000002248181278)；
3. 上架前，需要把发布证书公钥指纹也添加上；
4. 使用调试证书和调试Profile来[配置手动签名](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing#section297715173233)，使用[自动签名](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing#section18815157237)无法使用地图服务；
5. 运行项目查看搜索结果。
 
配置完成后运行示例代码：
 
```json
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">site </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.MapKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(181,106,1);">{</span>
  async <span style="color: rgb(0,0,255);">poiSearch</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">params</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">site</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">SearchByTextParams </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
    <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">指定关键字，</span><span style="color: rgb(128,128,128);">xxx</span><span style="color: rgb(128,128,128);">需替换具体地址</span></em>
      <span style="color: rgb(255,255,255);">query</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">"xxxxxxxx"</span><span style="color: rgb(181,106,1);">,</span>
    <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">经纬度坐标</span></em>
      <span style="color: rgb(255,255,255);">location</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">latitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">34.19390192547735</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,255,255);">longitude</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">108.87269875520396</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">,</span>
   <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">指定地理位置的范围半径</span></em>
      <span style="color: rgb(255,255,255);">radius</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">10000</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,255,255);">language</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">"zh"</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
 <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">返回关键字搜索结果</span></em>
    const <span style="color: rgb(255,255,255);">result </span><span style="color: rgb(181,106,1);">= </span>await <span style="color: rgb(255,255,255);">site</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">searchByText</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">params</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">log</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">"</span><span style="color: rgb(132,63,161);">搜索结果：</span><span style="color: rgb(132,63,161);">"</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(255,255,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">result</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'click'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(</span>async <span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">{</span>
        await  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">poiSearch</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">"100%"</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">"100%"</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
 

#### 常见FAQ

Q：使用POI关键字搜索省份/城市信息为什么只返回一条数据？
 
A：搜索区划信息时返回最准确的一个，如搜索出关键字相关的地点可以使用自动补全接口：queryAutoComplete。
 
Q：花瓣地图如何监听点击POI对象？
 
A：建议使用[on('poiClick')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mapcomponentcontroller#onpoiclick)监听POI点击事件。支持传递多个callback异步回调。
