# 如何判断某个IP是否在某IP段范围内

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-101

#### 问题现象

当前IP：192.168.9.230，如何判断该目标IP是否在10.101.10.210~255.201.255.1范围内？
 
 

#### 背景知识

IPv4地址采用点分十进制表示法，每个点分部分称为一个"八位组"，范围是0-255。判断某个IP是否在某IP段范围内可以先将IP转换为32位无符号整数，转换原理是基于256进制（2^8）的位权计算。例如：192.168.1.1=192×256³ + 168×256² + 1×256 + 1。
 
 

#### 解决方案

判断当前IP是否在某IP段范围内，可以参照以下步骤：
 1. 将点分十进制格式的IP地址转换为长整型数字，便于比较大小。
2. 检查目标IP是否在指定的起始IP和结束IP范围内。
 
```text
function <span style="color: rgb(0,0,255);">ipToLong</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">ip</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(255,0,170);">{</span>
  const <span style="color: rgb(0,0,255);">parts </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">ip</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">split</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'.'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">map</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">part </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">parseInt</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">part</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
  return <span style="color: rgb(0,0,255);">parts</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(0,0,255);">Math</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pow</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">256</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">3</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">parts</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(0,0,255);">Math</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pow</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">256</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">parts</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(255,0,0);">256 </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">parts</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">3</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

function <span style="color: rgb(0,0,255);">isIPInRange</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">ip</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">startIP</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">endIP</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(255,0,170);">{</span>
  const <span style="color: rgb(0,0,255);">ipNum </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">ipToLong</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">ip</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  const <span style="color: rgb(0,0,255);">startIPNum </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">ipToLong</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">startIP</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  const <span style="color: rgb(0,0,255);">endIPNum </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">ipToLong</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">endIP</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

  return <span style="color: rgb(0,0,255);">ipNum </span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">startIPNum </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span> <span style="color: rgb(0,0,255);">ipNum </span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">endIPNum</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">JudgeIp </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">judge</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    const <span style="color: rgb(0,0,255);">targetIP </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'192.168.9.230'</span><span style="color: rgb(181,106,1);">;</span>
    const <span style="color: rgb(0,0,255);">startIP </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'10.101.10.210'</span><span style="color: rgb(181,106,1);">;</span>
    const <span style="color: rgb(0,0,255);">endIP </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'255.201.255.1'</span><span style="color: rgb(181,106,1);">;</span>

    let <span style="color: rgb(0,0,255);">res </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">isIPInRange</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">targetIP</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">startIP</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">endIP</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    try <span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPromptAction</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showToast</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">目标</span><span style="color: rgb(255,0,170);">ip</span><span style="color: rgb(255,0,170);">地址是否在范围内</span><span style="color: rgb(255,0,170);">: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">res</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">` </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Error code: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, Message: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">查询</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">judge</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
