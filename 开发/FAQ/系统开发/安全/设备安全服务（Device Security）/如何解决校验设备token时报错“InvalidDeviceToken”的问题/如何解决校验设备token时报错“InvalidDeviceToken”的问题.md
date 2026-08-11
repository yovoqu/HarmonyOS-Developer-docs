# 如何解决校验设备token时报错“InvalidDeviceToken”的问题

更新时间：2026-07-30 01:55:38

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-device-security-3

#### 问题现象

应用设备检测场景中，使用checkDeviceToken API校验设备Token时，如何解决报错InvalidDeviceToken的问题。
 
 

#### 背景知识

[checkDeviceToken](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-deviceverify-checkdevicetoken)返回的错误码有以下几种：
  
| 错误码 | 描述 |
| --- | --- |
| OK | 请求处理成功。 |
| InvalidDeviceToken | deviceToken缺失或不合法。 |
| DeviceTokenExpired | deviceToken过期。 |
| InvalidTimeStamp | timeStamp缺失或不合法。 |
| InternalServerError | 服务器内部错误。 |
| InvalidBundleName | bundleName缺失或不合法。 |
 
 
 

#### 解决方案

针对deviceToken缺失或者不合法问题，要从deviceToken生成和请求发送过程进行分析。
 
- deviceToken生成过程：1. 检查是否已“[开通Device Security服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-deviceverify-activateservice)”中的应用设备状态检测能力并[申请调试Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-debug-cert-0000002283256797)。

2. 检查生成deviceToken代码是否合理，参考以下示例代码：
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">deviceCertificate </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.DeviceSecurityKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">hilog </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.PerformanceAnalysisKit'</span><span style="color: rgb(181,106,1);">;</span>

const <span style="color: rgb(0,0,255);">TAG </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">"DeviceCertificateJsTest"</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">获取设备</span><span style="color: rgb(255,0,170);">Token'</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">RelativeContainer</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'getDeviceToken'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.float.page_text_font_size'</span><span style="color: rgb(0,0,255);">))</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontWeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FontWeight</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bold</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignRules</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">center</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">VerticalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">middle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center </span><span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getDeviceToken</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>

<em>  <span style="color: rgb(128,128,128);">/**</span></em>
<em><span style="color: rgb(128,128,128);">   * </span><span style="color: rgb(128,128,128);">获取设备的</span><span style="color: rgb(128,128,128);">token</span></em>
<em><span style="color: rgb(128,128,128);">   * @returns</span></em>
<em><span style="color: rgb(128,128,128);">   */</span></em>
  <span style="color: rgb(0,0,255);">getDeviceToken</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(255,0,170);">{</span>
    let <span style="color: rgb(0,0,255);">res </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">""</span><span style="color: rgb(181,106,1);">;</span>
    try <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">deviceCertificate</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getDeviceToken</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">token</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">TAG</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'Succeeded in executing getDeviceToken'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'token</span><span style="color: rgb(255,0,170);">：</span><span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">token</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">TAG</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'getDeviceToken failed!  %{public}d %{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      let <span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">err </span>as <span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">TAG</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'getDeviceToken failed!  %{public}d %{public}s'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    return <span style="color: rgb(0,0,255);">res</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```


3. 检查deviceToken参数类型，deviceToken类型参数需要定义为String类型。

4. 检查deviceToken生成时间，防止失效。deviceToken由Device Security Kit加密生成，每次调用生成Token均不一样，有效期1小时。

 
- 请求发送过程：1. 检查是否正确获取服务账号令牌，服务账号令牌获取指导详情请参见[基于服务账号生成鉴权令牌](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-deviceverify-token)。

2. 检查消息体构造是否正确。请求构造过程需要构造请求消息体时，消息体需要在外层包一层data结构。详情参考如[请求示例](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-deviceverify-checkdevicetoken#请求示例)。
