# RichEditor组件实现自定义换行键

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-679

#### 问题现象

在2in1设备上，将Enter键功能设置为非换行类型后，对于RichEditor类的输入组件，如何将Shift+Enter组合键设为换行功能？
 
 

#### 背景知识

ArkUI提供的[文本输入组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/text-and-input)有TextArea、TextInput、RichEditor、Search等。这些组件均具有[enterKeyType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#enterkeytype11)属性，用于设置输入法回车键类型。[按键事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-key)是组件通用事件，可以监听键盘的输入按键进行处理。
 
 

#### 解决方案

使用[onKeyPreIme](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-key#onkeypreime12)监听按键事件，该方法返回值为true时，视作该按键事件已被消费，后续的事件回调不会触发。在按键事件中监听Shift和Enter，实现Shift+Enter按下为换行的逻辑。上述文本输入组件的实现方式相同，示例代码以TextArea为例：Shift+Enter为换行，Enter将清空TextArea并在Text中显示内容。
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">KeyCode </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.InputKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">ShiftEnterNewline </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">texts</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">isShiftPressed</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">12 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">ForEach</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">texts</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">left</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'12vp'</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'4vp'</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">right</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'12vp'</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'4vp'</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'90%'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderRadius</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'12vp'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'#F1F3F5'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">item</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">TextArea</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">$$this</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">placeholder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">请输入内容</span><span style="color: rgb(255,0,170);">' </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">text </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">同步输入框中的文本</span></em>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onKeyPreIme</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">KeyEvent</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          const <span style="color: rgb(0,0,255);">keyCode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">KeyCode </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">keyCode</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">获取按键码</span></em>
       <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">监听</span><span style="color: rgb(128,128,128);">Shift</span><span style="color: rgb(128,128,128);">键</span></em>
          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">keyCode </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">KeyCode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">KEYCODE_SHIFT_LEFT </span><span style="color: rgb(181,106,1);">|| </span><span style="color: rgb(0,0,255);">keyCode </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">KeyCode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">KEYCODE_SHIFT_RIGHT</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isShiftPressed </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">type </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">KeyType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Down</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">记录</span><span style="color: rgb(128,128,128);">Shift</span><span style="color: rgb(128,128,128);">按下的状态</span></em>
            return true<span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
        <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">监听</span><span style="color: rgb(128,128,128);">Enter</span><span style="color: rgb(128,128,128);">键</span></em>
          if <span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">keyCode </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">KeyCode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">KEYCODE_ENTER </span><span style="color: rgb(181,106,1);">|| </span><span style="color: rgb(0,0,255);">keyCode </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">KeyCode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">KEYCODE_NUMPAD_ENTER</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span>
            <span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">type </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">KeyType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Down</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isShiftPressed</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
   <em>           <span style="color: rgb(128,128,128);">// shift+enter</span><span style="color: rgb(128,128,128);">的处理逻辑</span></em>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">text </span><span style="color: rgb(181,106,1);">+= </span><span style="color: rgb(255,0,170);">'</span>\n<span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">添加换行符</span></em>
            <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
        <em>      <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">只按下</span><span style="color: rgb(128,128,128);">enter</span><span style="color: rgb(128,128,128);">的处理逻辑</span></em>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">texts</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">text</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">text </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
              return true<span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">          }</span>
          return false<span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'90%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">100</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">12 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
 
> [!NOTE]
> 此方法适用于物理键盘输入，不适用于虚拟键盘。
