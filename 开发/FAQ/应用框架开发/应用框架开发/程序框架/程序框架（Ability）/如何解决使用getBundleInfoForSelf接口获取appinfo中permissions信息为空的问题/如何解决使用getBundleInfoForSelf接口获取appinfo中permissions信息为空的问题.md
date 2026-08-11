# 如何解决使用getBundleInfoForSelf接口获取appinfo中permissions信息为空的问题

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-154

#### 问题现象

在开发应用时，需要获取应用包申请权限信息，系统提供了bundleManager.getBundleInfoForSelf接口去获取应用包权限信息，但接口返回后获取的appinfo信息中permissions为空值，是什么原因？
 
```json
let <span style="color: rgb(0,0,255);">bundleFlags </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">bundleManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BundleFlag</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">GET_BUNDLE_INFO_WITH_APPLICATION</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(0,0,255);">bundleManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getBundleInfoForSelf</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">bundleFlags</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
  let <span style="color: rgb(0,0,255);">permissions </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">reqPermissionDetails</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'test'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">`permissions: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">permissions</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
```
 
 

#### 背景知识

应用包信息，可以通过[bundleManager.getBundleInfoForSelf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager#bundlemanagergetbundleinfoforself)获取自身的应用包信息，其中参数[BundleFlag](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager#bundleflag)指定所返回的[BundleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-bundleinfo)中所包含的信息。
 
 

#### 问题定位
1. 调用bundleManager.getBundleInfoForSelf接口获取应用包信息需要传入bundleFlags参数，根据传入的bundleFlags参数不同，获取的appinfo信息不同，检查bundleFlags参数是否设置正确。
2. bundleFlags参数设置可以参考[BundleFlag](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager#bundleflag)。
3. 获取应用包申请权限信息需要添加包信息标志GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION，未添加此标志值则无法获取应用包申请权限信息。
 
 

#### 分析结论

由于未添加包信息标志GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION，导致无法获取包申请权限信息。
 
 

#### 修改建议

添加包信息标志GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION，以获取包申请权限信息。
 
```json
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">bundleManager </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.AbilityKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">hilog </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.PerformanceAnalysisKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">GetBundleInfo </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">getInfo</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    let <span style="color: rgb(0,0,255);">bundleFlags </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">bundleManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BundleFlag</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">GET_BUNDLE_INFO_WITH_APPLICATION </span><span style="color: rgb(181,106,1);">|</span>
    <span style="color: rgb(0,0,255);">bundleManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BundleFlag</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">bundleManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getBundleInfoForSelf</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">bundleFlags</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      let <span style="color: rgb(0,0,255);">permissions </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">reqPermissionDetails</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'TAG'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'permissions:' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">permissions</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(0x0000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'TAG'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">点击获取包申请权限信息</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">30</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getInfo</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
 

#### 总结

部分API接口会根据传入的参数不同而返回不同的结果，在使用此类API接口时需要注意传入参数的准确性，从而正确的获取所需要的数据。
