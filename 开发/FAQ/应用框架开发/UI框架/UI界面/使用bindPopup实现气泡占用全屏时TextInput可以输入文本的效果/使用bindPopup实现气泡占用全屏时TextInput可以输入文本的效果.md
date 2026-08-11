# 使用bindPopup实现气泡占用全屏时TextInput可以输入文本的效果

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1331

#### 问题现象

使用TextInput和bindPopup如何实现带动态提示的输入框。需要实现以下效果：
 
- Popup的背景为透明，Popup显示时占用整个窗口。
- 当点击TextInput输入框时可以获取焦点输入文本，并且输入框失去焦点时隐藏Popup。

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/EORzekH6QxWKvTVkpjTVHA/zh-cn_image_0000002658839163.gif?HW-CC-KV=V1&HW-CC-Date=20260811T005655Z&HW-CC-Expire=86400&HW-CC-Sign=603BCE30462F35E8878236173C3448082611770CE4685ADE38EC54BC2EA19D2D)

 
 

#### 背景知识

- [bindPopup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-popup#bindpopup)为[TextInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput)等组件绑定Popup气泡，可以设置[PopupOptions类型说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-popup#popupoptions类型说明)下的backgroundBlurStyle属性为BlurStyle.NONE用来关闭气泡的模糊背景，可以使气泡变为透明。
- TextInput主要用于获取用户输入的信息，并将信息处理成数据进行上传，[添加事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-text-input#添加事件)可以获取输入框内改变的文本内容。

 
 

#### 解决方案

实现气泡占用全屏时TextInput可以输入文本的效果，参考以下步骤：
 1. 定义message存储TextInput组件当前的文本内容，并且使用@State装饰。
```text
<span style="color: rgb(181,106,1);">@</span><span style="color: rgb(0,0,255);">State </span><span style="color: rgb(181,106,1);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
```

2. 定义customPopup控制弹出框(Popup)的显示和隐藏状态。当customPopup为true时，弹出框显示，为false时，弹出框隐藏。
```text
<span style="color: rgb(181,106,1);">@</span><span style="color: rgb(0,0,255);">State </span><span style="color: rgb(181,106,1);">customPopup</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
```

3. 将弹出框(Popup)的尺寸设置为其可用空间的100%宽度和100%高度。
```text
<span style="color: rgb(181,106,1);">@</span><span style="color: rgb(0,0,255);">Builder</span>
<span style="color: rgb(0,0,255);">popupBuilder</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">2 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tips</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">15</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignItems</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">VerticalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">) </span><em><span style="color: rgb(128,128,128);">// popup</span><span style="color: rgb(128,128,128);">显示时占用整个窗口</span></em>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">5</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```

4. 创建TextInput输入框，使用onEditChange事件控制弹出框(Popup)的显示和隐藏，设置backgroundBlurStyle: BlurStyle.NONE禁用弹出框(Popup)弹出背景的模糊效果。
```text
<span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">TextInput</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">placeholder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">请输入姓名</span><span style="color: rgb(255,0,170);">' </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">50</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">left</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">15</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">right</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">15</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">enableAutoFill</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">bindPopup</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">customPopup</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">builder</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">popupBuilder</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">placement</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Placement</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bottom</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">mask</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">color</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'#33000000' </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">backgroundBlurStyle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BlurStyle</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">NONE</span><span style="color: rgb(181,106,1);">,</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">去除模糊背景填充效果</span></em>
        <span style="color: rgb(0,0,255);">enableArrow</span><span style="color: rgb(181,106,1);">: </span>false<span style="color: rgb(181,106,1);">, </span><em>// </em><em><span style="color: rgb(128,128,128);">隐藏箭头</span></em>
        <span style="color: rgb(0,0,255);">autoCancel</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">showInSubWindow</span><span style="color: rgb(181,106,1);">: </span>false<span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">onStateChange</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isVisible</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">customPopup </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">点击了弹出框外部的区域，及时地将</span><span style="color: rgb(128,128,128);">@State</span><span style="color: rgb(128,128,128);">变量同步更新为</span><span style="color: rgb(128,128,128);">false</span></em>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span>
<span style="color: rgb(255,0,170);">      }</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">;</span>
        if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length </span><span style="color: rgb(181,106,1);">== </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tips </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
          return<span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>

        if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(0,0,255);">isChineseCharByRegex</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(0,0,255);">)) </span><span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tips </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">您的输入有误，姓名只能为汉字</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tips </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">      }</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onEditChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">isEditing</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <em>  <span style="color: rgb(128,128,128);">// isEditing</span><span style="color: rgb(128,128,128);">为</span><span style="color: rgb(128,128,128);">true</span><span style="color: rgb(128,128,128);">表示输入框获得了焦点</span></em>
        if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">isEditing</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{ </span><em>// </em><em><span style="color: rgb(128,128,128);">只有获得焦点才显示</span></em>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">customPopup </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">customPopup </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">输入框失去焦点时隐藏</span></em>
        <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">      }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```

 
完整示例参考如下：
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">BindPopUpDemo </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">customPopup</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">tips</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(181,106,1);">@Builder</span>
  <span style="color: rgb(0,0,255);">popupBuilder</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">2 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tips</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">15</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignItems</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">VerticalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><em> </em><em><span style="color: rgb(128,128,128);">// popup</span><span style="color: rgb(128,128,128);">显示时占用整个窗口</span></em>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">5</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">TextInput</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">placeholder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">请输入姓名</span><span style="color: rgb(255,0,170);">' </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">50</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">left</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">15</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">right</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">15</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">enableAutoFill</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">bindPopup</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">customPopup</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">builder</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">popupBuilder</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">placement</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Placement</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bottom</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">mask</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">color</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'#33000000' </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">backgroundBlurStyle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BlurStyle</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">NONE</span><span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">去除模糊背景填充效果</span></em>
          <span style="color: rgb(0,0,255);">enableArrow</span><span style="color: rgb(181,106,1);">: </span>false<span style="color: rgb(181,106,1);">,</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">隐藏箭头</span></em>
          <span style="color: rgb(0,0,255);">autoCancel</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">showInSubWindow</span><span style="color: rgb(181,106,1);">: </span>false<span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">onStateChange</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isVisible</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">customPopup </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">点击了弹出框外部的区域，及时地将</span><span style="color: rgb(128,128,128);">@State</span><span style="color: rgb(128,128,128);">变量同步更新为</span><span style="color: rgb(128,128,128);">false</span></em>
            <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">          }</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">;</span>
          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length </span><span style="color: rgb(181,106,1);">== </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tips </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
            return<span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>

          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(0,0,255);">isChineseCharByRegex</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(0,0,255);">)) </span><span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tips </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">您的输入有误，姓名只能为汉字</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tips </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onEditChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">isEditing</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        <em>  <span style="color: rgb(128,128,128);">// isEditing</span><span style="color: rgb(128,128,128);">为</span><span style="color: rgb(128,128,128);">true</span><span style="color: rgb(128,128,128);">表示输入框获得了焦点</span></em>
          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">isEditing</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">只有获得焦点才显示</span></em>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">customPopup </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">customPopup </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">输入框失去焦点时隐藏</span></em>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

function <span style="color: rgb(0,0,255);">isChineseCharByRegex</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">char</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(255,0,170);">{</span>
  return <span style="color: rgb(255,0,170);">/^[\u4e00-\u9fa5\u3400-\u4dbf\ud840-\ud87f\udc00-\udfff\uF900-\uFAFF]+$/</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">test</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">char</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```
