# Socket通信时，如何根据使用场景正确转换数据类型

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-86

#### 问题现象

使用WebSocket、TCPSocket、TLSSocket、UDPSocket发送数据时，如何根据使用场景正确转换数据类型。
 
 

#### 知识背景

- Socket进行数据传输，支持TCPSocket、UDPSocket、WebSocket和TLSSocket，仅可发送string或ArrayBuffer类型的数据，详情请参考[Socket连接](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-socket)。
- ArrayBuffer是ArkTS TypedArray的底层数据结构，TypedArray支持Int8Array、Uint8Array、Int16Array、Uint16Array等，详情请参考[ArrayBuffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-arraybuffer)。

 
 

#### 解决方案

Socket数据传输仅支持string或ArrayBuffer数据类型，与服务器进行交互时，有以下五种场景：
 
- **场景一**：客户端发送普通字符串数据，且服务端接收普通字符串，可直接调用[send](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-socket#send)接口发送。
- **场景二**：

  客户端发送普通字符串数据，但服务端需要接收二进制数据。可在Socket发送前将字符串转为Unicode，最后转换为ArrayBuffer类型数据。
```text
function <span style="color: rgb(0,0,255);">strToArrayBuffer</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">str</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
  let <span style="color: rgb(255,255,255);">buf </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">str</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(80,160,79);">2</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  let <span style="color: rgb(255,255,255);">bufView </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Uint16Array</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">buf</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  for <span style="color: rgb(255,0,170);">(</span>let <span style="color: rgb(255,255,255);">i </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">strLen </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">str</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(255,255,255);">i </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(255,255,255);">strLen</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(255,255,255);">i</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">bufView</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(255,255,255);">i</span><span style="color: rgb(255,0,170);">] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">str</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">charCodeAt</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">i</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
  <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`bufView </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">bufView</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  return <span style="color: rgb(255,255,255);">bufView</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">buffer</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>

let <span style="color: rgb(255,255,255);">inputValue </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'This is a plain string'</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(0,0,255);">strToArrayBuffer</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">inputValue</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
```

- **场景三**：

  客户端发送十六进制字符串数据如[FA AF 11 C5 FE FF...]，服务端需要接收8位有符号整数数值如[-6, -81, 17, -59, 3, -1...]，可在Socket发送前将十六进制字符转成8位有符号整数（元素取值范围-128至127）。
```text
function <span style="color: rgb(0,0,255);">strToInt8ArrayBuffer</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">str</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
  const <span style="color: rgb(255,255,255);">arr </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">str</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">split</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">' '</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">map</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">hex </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">num </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">parseInt</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">hex</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">16</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    return <span style="color: rgb(255,255,255);">num </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(80,160,79);">127 </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(255,255,255);">num </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(80,160,79);">256 </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">num</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  const <span style="color: rgb(255,255,255);">typedArray </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Int8Array</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">arr</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`typedArray </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">typedArray</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  return <span style="color: rgb(255,255,255);">typedArray</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">buffer</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>

let <span style="color: rgb(255,255,255);">hexString </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'FA AF 11 C5 FE FF FF FF FF FF FF F0 53 C8 B9 25 E1 A7 67 46 68 94 1D 72 BC'</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(0,0,255);">strToInt8ArrayBuffer</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">hexString</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
```
 
> [!NOTE]
> 若其他平台十六进制字符转8位二进制流数据给服务端正常，HarmonyOS端十六进制字符转8位二进制流数据给服务端解析异常时，请排查服务端需要的8位整数数据类型，需要8位有符号整数且取值范围为-128至127时，请参考该场景的转换方法。

- **场景四**：

  客户端发送十六进制字符串数据如[FA AF 11 C5 FE FF...]，服务端需要接收8位无符号整数数值如[250, 175, 17, 197, 254, 255...]，可在Socket发送前将十六进制字符转成8位无符号整数（元素取值范围0至255）。
```text
function <span style="color: rgb(0,0,255);">strToUint8ArrayBuffer</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">str</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
  const <span style="color: rgb(255,255,255);">arr </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">str</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">split</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">' '</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">map</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">hex </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">num </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">parseInt</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">hex</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">16</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    return <span style="color: rgb(255,255,255);">num</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  const <span style="color: rgb(255,255,255);">typedArray </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Uint8Array</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">arr</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`typedArray </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">typedArray</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  return <span style="color: rgb(255,255,255);">typedArray</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">buffer</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>

let <span style="color: rgb(255,255,255);">hexValue </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'FA AF 11 C5 FE FF FF FF FF FF FF F0 53 C8 B9 25 E1 A7 67 46 68 94 1D 72 BC'</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(0,0,255);">strToUint8ArrayBuffer</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">hexValue</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
```
 
> [!NOTE]
> 若其他平台十六进制字符转8位二进制流数据给服务端正常，HarmonyOS端十六进制字符转8位二进制流服务端解析异常时，请排查服务端需要的8位整数数据类型，需要8位无符号整数且取值范围为0至255时，请参考该场景的转换方法。

- **场景五**：客户端需要发送复合类型的数据，如对象、数组等，可在Socket发送前使用JSON.stringify()转为string类型，若服务端接收普通字符串请参考场景一，若服务端接收二进制流数据请参考场景二。

 
完整示例参考如下：
 
```text
function <span style="color: rgb(0,0,255);">strToArrayBuffer</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">str</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
  let <span style="color: rgb(255,255,255);">buf </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">ArrayBuffer</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">str</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(80,160,79);">2</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  let <span style="color: rgb(255,255,255);">bufView </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Uint16Array</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">buf</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  for <span style="color: rgb(255,0,170);">(</span>let <span style="color: rgb(255,255,255);">i </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">strLen </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">str</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(255,255,255);">i </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(255,255,255);">strLen</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(255,255,255);">i</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">bufView</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(255,255,255);">i</span><span style="color: rgb(255,0,170);">] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">str</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">charCodeAt</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">i</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
  <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`bufView </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">bufView</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  return <span style="color: rgb(255,255,255);">bufView</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">buffer</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>

let <span style="color: rgb(255,255,255);">inputValue </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'This is a plain string'</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(0,0,255);">strToArrayBuffer</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">inputValue</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

function <span style="color: rgb(0,0,255);">strToInt8ArrayBuffer</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">str</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
  const <span style="color: rgb(255,255,255);">arr </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">str</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">split</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">' '</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">map</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">hex </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">num </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">parseInt</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">hex</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">16</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    return <span style="color: rgb(255,255,255);">num </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(80,160,79);">127 </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(255,255,255);">num </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(80,160,79);">256 </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">num</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  const <span style="color: rgb(255,255,255);">typedArray </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Int8Array</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">arr</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`typedArray </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">typedArray</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  return <span style="color: rgb(255,255,255);">typedArray</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">buffer</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>

let <span style="color: rgb(255,255,255);">hexString </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'FA AF 11 C5 FE FF FF FF FF FF FF F0 53 C8 B9 25 E1 A7 67 46 68 94 1D 72 BC'</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(0,0,255);">strToInt8ArrayBuffer</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">hexString</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

function <span style="color: rgb(0,0,255);">strToUint8ArrayBuffer</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">str</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
  const <span style="color: rgb(255,255,255);">arr </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">str</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">split</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">' '</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">map</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">hex </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">num </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">parseInt</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">hex</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">16</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    return <span style="color: rgb(255,255,255);">num</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  const <span style="color: rgb(255,255,255);">typedArray </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Uint8Array</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">arr</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`typedArray </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">typedArray</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  return <span style="color: rgb(255,255,255);">typedArray</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">buffer</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>

let <span style="color: rgb(255,255,255);">hexValue </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'FA AF 11 C5 FE FF FF FF FF FF FF F0 53 C8 B9 25 E1 A7 67 46 68 94 1D 72 BC'</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(0,0,255);">strToUint8ArrayBuffer</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">hexValue</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@ComponentV2</span>
struct <span style="color: rgb(0,0,255);">SocketTest </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">普通字符串转</span><span style="color: rgb(132,63,161);">buffer'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">strToArrayBuffer</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">inputValue</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'16</span><span style="color: rgb(132,63,161);">进制字符转</span><span style="color: rgb(132,63,161);">Int8ArrayBuffer'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">strToInt8ArrayBuffer</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">hexString</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'16</span><span style="color: rgb(132,63,161);">进制字符转</span><span style="color: rgb(132,63,161);">Uint8ArrayBuffer'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">strToUint8ArrayBuffer</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">hexValue</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
 

#### 常见FAQ

Q：同时启动多个tcp server去监听同样的端口，都可以成功，这种情况不应该抛出端口占用的异常吗？
 
A：目前如果遇到指定端口被占用的情况，tcpsocketserver的listen会自动绑定一个新的随机端口。
 
应用可以通过[getLocalAddress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-socket#getlocaladdress12-1)获取监听的端口，判断是否与指定的一致。
