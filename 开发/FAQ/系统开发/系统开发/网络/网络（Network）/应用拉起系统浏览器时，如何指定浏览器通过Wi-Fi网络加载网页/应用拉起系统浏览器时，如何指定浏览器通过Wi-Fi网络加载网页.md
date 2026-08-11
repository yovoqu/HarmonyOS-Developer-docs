# 应用拉起系统浏览器时，如何指定浏览器通过Wi-Fi网络加载网页

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-105

#### 问题现象

手机开启移动网络，并连接到Wi-Fi网络后，当三方应用拉起系统浏览器时，如何指定浏览器通过Wi-Fi网络加载网页。
 
 

#### 背景知识

- 通过[connection.getAllNets](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection#connectiongetallnets)方法可获取所有处于连接状态的网络列表。
- 通过[Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-want)跳转拉起应用时，可通过parameters参数传递数据。

 
 

#### 解决方案
1. 在module.json5文件中申请允许应用获取数据网络信息的权限：[ohos.permission.GET_NETWORK_INFO](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/permissions-for-all#ohospermissionget_network_info)。
2. 使用[connection.getAllNets](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection#connectiongetallnets)方法获取连接状态的网络列表，并使用[connection.getNetCapabilities](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection#connectiongetnetcapabilities)方法判断是否有Wi-Fi的netId，若存在Wi-Fi的netId，在应用拉起系统浏览器时，可通过parameters参数传递Wi-Fi网络的netId，并设置action，entities及abilityName参数，传递的uri为探测地址。
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">common</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">Want </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.AbilityKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">connection </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.NetworkKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">NetPage </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">RelativeContainer</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">拉起浏览器</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontWeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FontWeight</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bold</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignRules</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">middle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">center</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">VerticalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center </span><span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          let <span style="color: rgb(0,0,255);">netId </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
         <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取已连接的网络列表</span></em>
          let <span style="color: rgb(0,0,255);">netHandle </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">connection</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getAllNetsSync</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">netHandle</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">forEach</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
           <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">判断是否为</span><span style="color: rgb(128,128,128);">Wi-Fi</span><span style="color: rgb(128,128,128);">网络</span></em>
            if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">connection</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getNetCapabilitiesSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">bearerTypes</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">netId </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">netId</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">          }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

          try <span style="color: rgb(255,0,170);">{</span>
            let <span style="color: rgb(0,0,255);">want</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Want </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
             <em> <span style="color: rgb(128,128,128);">// action</span><span style="color: rgb(128,128,128);">设置为</span><span style="color: rgb(128,128,128);">ohos.want.action.awc</span><span style="color: rgb(128,128,128);">或</span><span style="color: rgb(128,128,128);">ohos.want.action.viewData</span></em>
              <span style="color: rgb(0,0,255);">action</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'ohos.want.action.awc'</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(0,0,255);">bundleName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'com.huawei.hmos.browser'</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(0,0,255);">entities</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">'entity.browser.hbct'</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(0,0,255);">abilityName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'CustomTabAbility'</span><span style="color: rgb(181,106,1);">,</span>
           <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">此处地址实际使用过程中替换为真实地址</span></em>
              <span style="color: rgb(0,0,255);">uri</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'xx.xx.xx'</span><span style="color: rgb(181,106,1);">,</span>
          <em>    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">传递</span><span style="color: rgb(128,128,128);">netId</span></em>
              <span style="color: rgb(0,0,255);">parameters</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
                <span style="color: rgb(255,0,170);">'netId'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">netId</span>
              <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">            }</span><span style="color: rgb(181,106,1);">;</span>
            let <span style="color: rgb(0,0,255);">context </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(0,0,255);">() </span>as <span style="color: rgb(0,0,255);">common</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">UIAbilityContext</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">startAbility</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">want</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`explicit start ability succeed`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`explicit start ability failed with </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
 

#### 常见FAQ

Q：如何指定拉起系统浏览器时打开的网页？
 
A：Want对象的uri属性即要打开的网页链接。
