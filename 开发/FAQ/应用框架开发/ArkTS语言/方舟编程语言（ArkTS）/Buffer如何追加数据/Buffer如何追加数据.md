# Buffer如何追加数据

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-178

#### 问题现象

[Buffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/buffer)没有看到writeBuffer(buffer: Buffer)方法，如何实现追加流？
 
 

#### 背景知识

- [Buffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/buffer)将内存区域抽象为可读写、修改的逻辑对象，提供高效的二进制数据处理接口。每个Buffer实例是连续的字节序列，支持创建自定义大小的内存块，用于存储和操作序列化后的数据。
- [Buffer.concat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-buffer#bufferconcat)将数组中的内容复制指定字节长度到新的Buffer对象中并返回。
- [Buffer.fill](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-buffer#fill)使用value填充当前对象指定位置的数据，默认为循环填充，并返回填充后的Buffer对象。

 
 

#### 解决方案

Buffer对象需要指定大小初始化且内存容量固定。
 1. Buffer已填充满数据，通过[concat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-buffer#bufferconcat)合并Buffer对象并返回新的Buffer对象。
```text
let <span style="color: rgb(0,0,255);">buf1 </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">buffer</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">from</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'1234'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
let <span style="color: rgb(0,0,255);">buf2 </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">buffer</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">from</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'abcd'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
let <span style="color: rgb(0,0,255);">buf </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">buffer</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">concat</span><span style="color: rgb(0,0,255);">([</span><span style="color: rgb(0,0,255);">buf1</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">buf2</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">已填充数据</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(0,0,255);">buf</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">())</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(128,128,128);">// 1234abcd</span>
```

2. Buffer未填充满数据，通过[Buffer.fill](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-buffer#fill)填充数据。
```text
let <span style="color: rgb(0,0,255);">buf </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">buffer</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">allocUninitializedFromPool</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">8</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(0,0,255);">buf</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fill</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">buffer</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">from</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'1234'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">4</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(0,0,255);">buf</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fill</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">buffer</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">from</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'abcd'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">4</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">8</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">buf</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">())</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(128,128,128);">// 1234abcd</span>
```

 
完整示例代码如下：
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">buffer </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkTS'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">已填充数据</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.float.page_text_font_size'</span><span style="color: rgb(0,0,255);">))</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontWeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FontWeight</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bold</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          let <span style="color: rgb(0,0,255);">buf1 </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">buffer</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">from</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'1234'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          let <span style="color: rgb(0,0,255);">buf2 </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">buffer</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">from</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'abcd'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          let <span style="color: rgb(0,0,255);">buf </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">buffer</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">concat</span><span style="color: rgb(0,0,255);">([</span><span style="color: rgb(0,0,255);">buf1</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">buf2</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">已填充数据</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(0,0,255);">buf</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">())</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(128,128,128);">// 1234abcd</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>

      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">未填充满数据</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.float.page_text_font_size'</span><span style="color: rgb(0,0,255);">))</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontWeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FontWeight</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bold</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          let <span style="color: rgb(0,0,255);">buf </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">buffer</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">allocUninitializedFromPool</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">8</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">buf</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fill</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">buffer</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">from</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'1234'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">4</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">buf</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fill</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">buffer</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">from</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'abcd'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">4</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">8</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">buf</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">())</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(128,128,128);">// 1234abcd</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignItems</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
 

#### 总结

ArkTS的Buffer对象的内容可以在创建后修改，但其长度是固定的，不能动态改变。
