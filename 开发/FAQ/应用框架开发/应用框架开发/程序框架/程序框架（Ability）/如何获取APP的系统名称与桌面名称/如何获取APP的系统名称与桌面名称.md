# 如何获取APP的系统名称与桌面名称

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-149

#### 问题现象

开发者在开发过程中，需要获取APP的名称用于一些功能展示，如何获取APP的名称呢？
 
 

#### 背景知识

APP名称可以分为系统APP名称与桌面APP名称。
 
- 系统APP名称，指应用在系统内部管理的标识名称，通常对应开发者在AppScope中app.json5中配置的label属性，该名称用于应用列表、权限管理等系统级交互场景。通常使用[getBundleInfoForSelf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager#bundlemanagergetbundleinfoforself)获取系统APP名称。
- 桌面APP名称，指用户直接看到的应用图标下方显示的名称，对应开发者在module.json5中配置的label属性，该名称可以灵活调整，无需与系统名称完全一致。通常使用[AbilityInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-abilityinfo#abilityinfo-1)获取桌面APP名称。需要注意的是，如果在module.json5配置文件的abilities标签中未设置label，系统将返回app.json5中的label，作为桌面APP名称。

 
 

#### 解决方案

获取APP的系统名称与桌面名称有两种方案：
 
- **方案一**：通过[getBundleInfoForSelf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager#bundlemanagergetbundleinfoforself)获取系统APP名称，通过[AbilityInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-abilityinfo#abilityinfo-1)获取桌面APP名称。
- **方案二**：系统APP名称和桌面APP名称都可以通过资源管理的接口[getStringSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resource-manager#getstringsync9)获取。

 
```text
import <span style="color: rgb(0,0,255);">common </span>from <span style="color: rgb(255,0,170);">'@ohos.app.ability.common'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">bundleManager </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.AbilityKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index1 </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">systemAPPNameOne</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">systemAPPNameTwo</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">desktopAppNameOne</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">desktopAppNameTwo</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    const <span style="color: rgb(0,0,255);">context </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(0,0,255);">() </span>as <span style="color: rgb(0,0,255);">common</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">UIAbilityContext</span><span style="color: rgb(181,106,1);">;</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取系统</span><span style="color: rgb(128,128,128);">APP</span><span style="color: rgb(128,128,128);">的名称</span></em>
    let <span style="color: rgb(0,0,255);">bundleFlags </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">bundleManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BundleFlag</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">GET_BUNDLE_INFO_WITH_APPLICATION</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(0,0,255);">bundleInfo </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">bundleManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getBundleInfoForSelfSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">bundleFlags</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(0,0,255);">appLabel</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">bundleInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">appInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">label</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(0,0,255);">appRes </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">appLabel</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">split</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">':'</span><span style="color: rgb(0,0,255);">)[</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">systemAPPNameOne </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">resourceManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getStringByNameSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">appRes</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">方案一：获取系统</span><span style="color: rgb(255,0,170);">APP</span><span style="color: rgb(255,0,170);">的名称：</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">systemAPPNameOne</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">systemAPPNameTwo </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">resourceManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getStringSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.string.app_name'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">方案二：获取系统</span><span style="color: rgb(255,0,170);">APP</span><span style="color: rgb(255,0,170);">的名称：</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">systemAPPNameTwo</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取桌面</span><span style="color: rgb(128,128,128);">APP</span><span style="color: rgb(128,128,128);">的名称</span></em>
    let <span style="color: rgb(0,0,255);">windowAppLabel </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">abilityInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">label</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(0,0,255);">windowAppRes </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">windowAppLabel</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">split</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">':'</span><span style="color: rgb(0,0,255);">)[</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">desktopAppNameOne </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">resourceManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getStringByNameSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">windowAppRes</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">方案一：获取桌面</span><span style="color: rgb(255,0,170);">APP</span><span style="color: rgb(255,0,170);">的名称：</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">desktopAppNameOne</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">desktopAppNameTwo </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">resourceManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getStringSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.string.EntryAbility_label'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">方案二：获取桌面</span><span style="color: rgb(255,0,170);">APP</span><span style="color: rgb(255,0,170);">的名称：</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">desktopAppNameTwo</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">方案一：系统</span><span style="color: rgb(255,0,170);">APP</span><span style="color: rgb(255,0,170);">的名称</span><span style="color: rgb(255,0,170);">: ' </span><span style="color: rgb(181,106,1);">+ </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">systemAPPNameOne</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">方案二：系统</span><span style="color: rgb(255,0,170);">APP</span><span style="color: rgb(255,0,170);">的名称</span><span style="color: rgb(255,0,170);">: ' </span><span style="color: rgb(181,106,1);">+ </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">systemAPPNameTwo</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">方案一：桌面</span><span style="color: rgb(255,0,170);">APP</span><span style="color: rgb(255,0,170);">的名称</span><span style="color: rgb(255,0,170);">: ' </span><span style="color: rgb(181,106,1);">+ </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">desktopAppNameOne</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">方案二：桌面</span><span style="color: rgb(255,0,170);">APP</span><span style="color: rgb(255,0,170);">的名称</span><span style="color: rgb(255,0,170);">: ' </span><span style="color: rgb(181,106,1);">+ </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">desktopAppNameTwo</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
验证图示和桌面APP图示如下:
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/HewurUxBQ5-HWV_cILQ9oQ/zh-cn_image_0000002658988569.png?HW-CC-KV=V1&HW-CC-Date=20260811T005857Z&HW-CC-Expire=86400&HW-CC-Sign=C727D5907469D7518C31C47F00CD0E29D0EBC1B344CB222CF0DB53670E25DF9F)
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/mPqqBrp-SiqxvYr_bvdmjA/zh-cn_image_0000002658868625.png?HW-CC-KV=V1&HW-CC-Date=20260811T005857Z&HW-CC-Expire=86400&HW-CC-Sign=1E59028C186613F61C3F19F2A1F6AA5A53C3BE99DD7F9A19AB705E37AB2A61DB)

 
 

#### 常见FAQ

Q：在module.json5中修改了label属性，但是APP名称显示未生效？
 
A：建议卸载APP重新安装。
