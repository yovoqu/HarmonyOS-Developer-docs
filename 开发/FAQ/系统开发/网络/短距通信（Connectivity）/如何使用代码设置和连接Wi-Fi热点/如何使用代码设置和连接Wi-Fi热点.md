# 如何使用代码设置和连接Wi-Fi热点

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-27

#### 问题现象

- 问题一：如何在代码中设置并开启自定义名称和密码的Wi-Fi热点？
- 问题二：如何通过代码搜索到Wi-Fi列表，连接上指定的Wi-Fi？

 
 

#### 解决方案

- **问题一**：除系统应用外，其他应用不支持通过代码开启自定义名称和密码的Wi-Fi热点，可在应用中跳转至系统设置页来开启热点。
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">common</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">Want </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.AbilityKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Go to Settings'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">300 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          let <span style="color: rgb(0,0,255);">context </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(0,0,255);">() </span>as <span style="color: rgb(0,0,255);">common</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">UIAbilityContext</span><span style="color: rgb(181,106,1);">;</span>
          let <span style="color: rgb(0,0,255);">want</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Want </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">bundleName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'com.huawei.hmos.settings'</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">abilityName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'com.huawei.hmos.settings.MainAbility'</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">uri</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'hotspot_data_settings'</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">parameters</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
             <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">传对应应用的包名</span></em>
              <span style="color: rgb(0,0,255);">pushParams</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'com.example.myapplication'</span>
            <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">          }</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">startAbility</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">want</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

- **问题二**：可以使用接口[wifiManager.getCandidateConfigs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanagergetcandidateconfigs)获取候选网络配置，再使用接口[wifiManager.connectToCandidateConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanagerconnecttocandidateconfig)连接到自己添加的候选网络即可。
