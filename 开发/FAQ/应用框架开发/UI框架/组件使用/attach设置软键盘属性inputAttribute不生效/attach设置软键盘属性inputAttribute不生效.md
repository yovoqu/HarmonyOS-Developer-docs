# attach设置软键盘属性inputAttribute不生效

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-784

#### 问题现象

inputAttribute属性用于设置enter键的功能类型，enterKeyType:5表示"下一步"。TextInput使用attach方法唤起的软键盘，设置的inputAttribute属性初次生效，enter键的功能为"下一步"，关闭键盘后再拉起键盘，inputAttribute属性失效，enter键的功能为"完成"。
 
问题代码示例参考如下：
 
```text
<span style="color: rgb(0,0,255);">onFocus</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
  let <span style="color: rgb(0,0,255);">textConfig</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">inputMethod</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">TextConfig </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">inputAttribute</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">textInputType</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">enterKeyType</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">5</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span><span style="color: rgb(181,106,1);">;</span>
  let <span style="color: rgb(0,0,255);">inputMethodController </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">inputMethod</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getController</span><span style="color: rgb(0,0,255);">()</span>
  <span style="color: rgb(0,0,255);">inputMethodController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">attach</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">textConfig</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">  }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
```
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/fT21AMxITBWIHP2sOIpAaw/zh-cn_image_0000002658916947.gif?HW-CC-KV=V1&HW-CC-Date=20260723T012613Z&HW-CC-Expire=86400&HW-CC-Sign=F9C16FFCA6746A1277408C22D4FEC2C16D890996776B5776DE9C7AF6BFE1798E)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/_TRTnWHNTN-bvrgtezPGmg/zh-cn_image_0000002628397738.gif?HW-CC-KV=V1&HW-CC-Date=20260723T012613Z&HW-CC-Expire=86400&HW-CC-Sign=A7DC29F97F6FD61BD38704CC3C1675D2CA49AD3383E5B9893DCF32FAD30E6929)

 
 

#### 背景知识

- [attach](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod#attach10)：自绘控件绑定输入法。使用callback异步回调。
- [updateAttribute](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod#updateattribute10)：更新编辑框属性信息。使用callback异步回调。当编辑框属性信息更新成功时，err为undefined；否则为错误对象。

 
 

#### 解决方案

使用updateAttribute方法设置inputAttribute属性。
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">inputMethod </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.IMEKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">CustomPopup </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">TextInput</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">placeholder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">请输入正确内容</span><span style="color: rgb(255,0,170);">' </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">focusable</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">100</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">left</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">10</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">right</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">10 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onFocus</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          let <span style="color: rgb(0,0,255);">inputAttribute</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">inputMethod</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">InputAttribute </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">textInputType</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">enterKeyType</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">5 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
          let <span style="color: rgb(0,0,255);">inputMethodController </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">inputMethod</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">inputMethodController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">updateAttribute</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">inputAttribute</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">          }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
