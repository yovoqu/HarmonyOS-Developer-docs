# 如何解决mock中继承Base64Helper不生效的问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-20

#### 问题现象

mock中继承Base64Helper不生效。
 
问题代码示例参考如下：
 
```ArkTS
<em>// Base64HelperMock.mock.ets</em>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">util </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ArkTS'</span>

export class <span style="color: rgb(0,0,255);">Base64HelperMock </span>extends <span style="color: rgb(255,255,255);">util</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Base64Helper </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(0,0,255);">decodeSync</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(181,106,1);">Uint8Array</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">options</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(181,106,1);">util</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Type </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(181,106,1);">undefined</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Uint8Array </span><span style="color: rgb(181,106,1);">{</span>
    return new <span style="color: rgb(0,0,255);">Uint8Array</span><span style="color: rgb(255,0,170);">([</span><span style="color: rgb(80,160,79);">99</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(80,160,79);">97</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(255,0,170);">])</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
  <span style="color: rgb(0,0,255);">encodeSync</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Uint8Array</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">options</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(181,106,1);">util</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Type </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(181,106,1);">undefined</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    return new <span style="color: rgb(0,0,255);">Uint8Array</span><span style="color: rgb(255,0,170);">([</span><span style="color: rgb(80,160,79);">99</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(80,160,79);">97</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(255,0,170);">])</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
  <span style="color: rgb(0,0,255);">encodeToStringSync</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Uint8Array</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">options</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(181,106,1);">util</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Type </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(181,106,1);">undefined</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">{</span>
    return <span style="color: rgb(132,63,161);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
```ArkTS
<em>// mock-config.json5</em>
{
  <span style="color: rgb(132,63,161);">"@ohos.util"</span><span style="color: rgb(181,106,1);">: </span>{
    <span style="color: rgb(132,63,161);">"source"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"src/mock/Base64HelperMock.mock.ets"</span>
  }
}
```
 
```text
<em>// </em><em><span style="color: rgb(128,128,128);">测试文件</span></em>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">util </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ArkTS'</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">describe</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">it </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@ohos/hypium'</span><span style="color: rgb(181,106,1);">;</span>

export default function <span style="color: rgb(0,0,255);">localUnitTest</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(0,0,255);">describe</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'localUnitTest'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">it</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'assertContain'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      const <span style="color: rgb(255,255,255);">array </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(255,255,255);">util</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Base64Helper</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">decodeSync</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">''</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
运行报错如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/wtkWrTbfTKyLeVlLxbjdAg/zh-cn_image_0000002658808815.png?HW-CC-KV=V1&HW-CC-Date=20260730T072721Z&HW-CC-Expire=86400&HW-CC-Sign=090E6AE8C3E720D871A81F9CCA045B59F87F4476CF7283647B4007536CC761F3)

 
 

#### 背景知识

[Mock能力](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-test-mock)：在实际开发中，一些接口或者对象依赖于外部资源或复杂的逻辑，这些依赖在测试环境中难以复现，导致这些接口或者对象难以测试，此时，可以使用mock能力，对这些接口或对象进行模拟。
 
 

#### 问题定位

请按以下方案进行排查：
 1. 确认mock文件的导出方式和被mock接口的导出方式一致。查看被mock接口的导出方式，可以用Ctrl+鼠标左键点击被mock的接口。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/i5etq4F7S8uAXh7qXE9NHA/zh-cn_image_0000002628409548.png?HW-CC-KV=V1&HW-CC-Date=20260730T072721Z&HW-CC-Expire=86400&HW-CC-Sign=D92BA6CB0497A006300102C49A3261122F3974B9813FFA13E55D2967DC944F3F)


  查看mock文件的导出方式。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/VExXDQuJSCSYZVctRgxvmw/zh-cn_image_0000002628569446.png?HW-CC-KV=V1&HW-CC-Date=20260730T072721Z&HW-CC-Expire=86400&HW-CC-Sign=8DDFB71A03FBB2BC8D39D143905ED79EDDAAD226464D18AA0589253E992CDBB2)

 
 

#### 分析结论

mock文件的导出方式和被mock接口的导出方式不一致。
 
 

#### 修改建议

mock文件的导出方式要与mock的接口（util接口）的导出方式一致，[util](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-util)接口的导出方式为export default util，所以这边mock文件的导出方式要为export default mockUtil。
 1. 在“src/mock”目录下新建一个ArkTS文件，例如Base64HelperMock.mock.ets，在这个文件内定义目标模块的mock实现。
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">util </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ArkTS'</span>
type MockUtil <span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">Record</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">Object</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">;</span>

export class <span style="color: rgb(0,0,255);">Base64HelperMock </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(0,0,255);">decodeSync</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(181,106,1);">Uint8Array</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">options</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(181,106,1);">util</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Type </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(181,106,1);">undefined</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Uint8Array </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'run mock'</span><span style="color: rgb(255,0,170);">)</span>
    return new <span style="color: rgb(0,0,255);">Uint8Array</span><span style="color: rgb(255,0,170);">([</span><span style="color: rgb(80,160,79);">99</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(80,160,79);">97</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(255,0,170);">])</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
  <span style="color: rgb(0,0,255);">encodeSync</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Uint8Array</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">options</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(181,106,1);">util</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Type </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(181,106,1);">undefined</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    return new <span style="color: rgb(0,0,255);">Uint8Array</span><span style="color: rgb(255,0,170);">([</span><span style="color: rgb(80,160,79);">99</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(80,160,79);">97</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(255,0,170);">])</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
  <span style="color: rgb(0,0,255);">encodeToStringSync</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Uint8Array</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">options</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(181,106,1);">util</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Type </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(181,106,1);">undefined</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">{</span>
    return <span style="color: rgb(132,63,161);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>

const <span style="color: rgb(255,255,255);">mockUtil</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">MockUtil </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(132,63,161);">'Base64Helper'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">Base64HelperMock</span><span style="color: rgb(181,106,1);">,</span>
<span style="color: rgb(181,106,1);">}</span>

export default <span style="color: rgb(255,255,255);">mockUtil</span>
```

2. 在mock配置文件“src/mock/mock-config.json5”中定义目标模块与mock实现的映射关系。
```ArkTS
{
  <span style="color: rgb(132,63,161);">"@ohos.util"</span><span style="color: rgb(181,106,1);">: </span>{
    <span style="color: rgb(132,63,161);">"source"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"src/mock/Base64HelperMock.mock.ets"</span>
  }
}
```

3. 在测试文件中编写如下代码。
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">util </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ArkTS'</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">describe</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">it </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@ohos/hypium'</span><span style="color: rgb(181,106,1);">;</span>

export default function <span style="color: rgb(0,0,255);">localUnitTest</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(0,0,255);">describe</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'localUnitTest'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">it</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'assertContain'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      const <span style="color: rgb(255,255,255);">array </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(255,255,255);">util</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Base64Helper</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">decodeSync</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">''</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>
```
