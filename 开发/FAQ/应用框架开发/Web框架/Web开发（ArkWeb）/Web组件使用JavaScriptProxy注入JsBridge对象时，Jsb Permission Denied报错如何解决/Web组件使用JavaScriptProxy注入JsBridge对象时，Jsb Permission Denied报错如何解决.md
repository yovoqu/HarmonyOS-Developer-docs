# Web组件使用JavaScriptProxy注入JsBridge对象时，Jsb Permission Denied报错如何解决

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-160

#### 问题现象

Web组件用file协议加载位于Download目录下的html文件，用JavaScriptProxy注入JsBridge对象，但前端页面无法调用注入的JsBridge对象的方法，前端页面报错为Uncaught Error：Jsb Permission Denied。部分问题代码如下：
```text
<span style="color: rgb(181,106,1);">jsBridgePermission</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">JsBridgePermission </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">javascriptProxyPermission</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">urlPermissionList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">[      </span><em> </em><em><span style="color: rgb(128,128,128);">// Object</span><span style="color: rgb(128,128,128);">级权限，如果匹配，所有</span><span style="color: rgb(128,128,128);">Method</span><span style="color: rgb(128,128,128);">都授权</span></em>
      <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">scheme</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'resource'</span><span style="color: rgb(181,106,1);">,    </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">精确匹配，不能为空</span></em>
        <span style="color: rgb(0,0,255);">host</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'rawfile'</span><span style="color: rgb(181,106,1);">,      </span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">精确匹配，不能为空</span></em>
        <span style="color: rgb(0,0,255);">port</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">,            </span><em>  </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">精确匹配，为空不检查</span></em>
        <span style="color: rgb(0,0,255);">path</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">''             </span><em>  </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">前缀匹配，为空不检查</span></em>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">scheme</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'file'</span><span style="color: rgb(181,106,1);">,  </span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">精确匹配，不能为空</span></em>
        <span style="color: rgb(0,0,255);">host</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">,  </span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">精确匹配，不能为空</span></em>
        <span style="color: rgb(0,0,255);">port</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">,       </span><em>   </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">精确匹配，为空不检查</span></em>
        <span style="color: rgb(0,0,255);">path</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">''        </span><em>   </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">前缀匹配，为空不检查</span></em>
      <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(0,0,255);">methodList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">[</span>
      <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">methodName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'test'</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">urlPermissionList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">[  </span><em> </em><em><span style="color: rgb(128,128,128);">// Method</span><span style="color: rgb(128,128,128);">级权限</span></em>
          <span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">scheme</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'resource'</span><span style="color: rgb(181,106,1);">, </span><em>// </em><em><span style="color: rgb(128,128,128);">精确匹配，不能为空</span></em>
            <span style="color: rgb(0,0,255);">host</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'rawfile'</span><span style="color: rgb(181,106,1);">,  </span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">精确匹配，不能为空</span></em>
            <span style="color: rgb(0,0,255);">port</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">,       </span><em>   </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">精确匹配，为空不检查</span></em>
            <span style="color: rgb(0,0,255);">path</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">''        </span><em>   </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">前缀匹配，为空不检查</span></em>
          <span style="color: rgb(255,0,170);">}</span>
        <span style="color: rgb(0,0,255);">]</span>
      <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(0,0,255);">]</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
 
 

#### 背景知识

- [前端页面调用应用侧函数](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-in-page-app-function-invoking)：开发者使用Web组件将应用侧代码注册到前端页面中，注册完成之后，前端页面中使用注册的对象名称就可以调用应用侧的函数，实现在前端页面中调用应用侧方法。
- [JavaScriptProxy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-attributes#javascriptproxy)：定义要注入的JavaScript对象。该方法有一个可选参数permission——JSON字符串，默认为空，通过该字符串配置JsBridge的权限管控，可以定义object、method一级的url白名单。

 
 

#### 问题定位

根据问题现象及报错信息，可知是JsBridge权限相关问题。发现代码中配置了JavaScriptProxy的permission参数，考虑JsBridge使用受限是由于该参数对JsBridge权限进行了管控，排查该参数配置：
 1. scheme（协议）和host（域名）参数是否为空，若为空则会报错。
2. 是否配置了调用失败的JsBridge方法的method级白名单。以file协议为例，使用file协议加载html，若只在object级配置了file协议的白名单、方法A的method级未配置file协议的白名单，将无法调用方法A；反过来也一样，若只在方法A的method级配置了file协议、object级中未配置file协议的白名单，也无法调用方法A。
 
 

#### 分析结论

要使用JavaScriptProxy的permission对JsBridge方法的调用进行权限管控，JavaScriptProxy的permission参数配置需要遵循以下原则：
 
- scheme（协议）和host（域名）参数不可为空。
- 可以只配置object级的白名单，该白名单对所有JsBridge方法生效。
- 若JsBridge方法A设置了method级白名单，那么**方法A最终的白名单是object级白名单与其method级白名单的交集**。比如方法A的method级配置了scheme为file、host为docs的白名单，那么object级也必须设置scheme为file、host为docs的白名单；反过来也是如此，若object级配置了scheme为file、host为docs的白名单，而方法A需要在对应场景允许调用的话，方法A的method级也需要配置同样scheme和host的白名单。
- file协议的host为第一级目录名称，path（路径）可为空，不为空时需要注意object级和method级白名单的交集原则，object级和method级的path不能冲突（完全相同或method级path为object级path的子目录）。

 
 

#### 修改建议

以file协议加载Download目录下的html文件场景为例，要允许注入的JsBridge的方法A被调用，可参考如下修改建议：
 
- 不需要对JsBridge进行权限管控时，不配置JavaScriptProxy的permission参数即可。
- 只需要对JsBridge的所有方法统一权限管控时，只配置JavaScriptProxy的permission参数的object级白名单即可，配置项如下（使用对象形式方便修改和展示，实际使用时需将对象转换为JSON字符串格式）：
```text
<span style="color: rgb(181,106,1);">jsBridgePermission</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">JsBridgePermission </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">javascriptProxyPermission</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">urlPermissionList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">[</span> <em>// Object</em><em><span style="color: rgb(128,128,128);">级权限，如果匹配，所有</span><span style="color: rgb(128,128,128);">Method</span><span style="color: rgb(128,128,128);">都授权</span></em>
      <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">scheme</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'resource'</span><span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">精确匹配，不能为空</span></em>
        <span style="color: rgb(0,0,255);">host</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'rawfile'</span><span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">精确匹配，不能为空</span></em>
        <span style="color: rgb(0,0,255);">port</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">, </span><em>// </em><em><span style="color: rgb(128,128,128);">精确匹配，为空不检查</span></em>
        <span style="color: rgb(0,0,255);">path</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">''            </span><em>   </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">前缀匹配，为空不检查</span></em>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">scheme</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'file'</span><span style="color: rgb(181,106,1);">,</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">精确匹配，不能为空</span></em>
        <span style="color: rgb(0,0,255);">host</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'docs'</span><span style="color: rgb(181,106,1);">, </span><em>// </em><em><span style="color: rgb(128,128,128);">精确匹配，不能为空</span></em>
        <span style="color: rgb(0,0,255);">port</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">, </span><em>// </em><em><span style="color: rgb(128,128,128);">精确匹配，为空不检查</span></em>
        <span style="color: rgb(0,0,255);">path</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'/storage/Users/currentUser/Download/'          </span><em> </em><em><span style="color: rgb(128,128,128);">// file</span><span style="color: rgb(128,128,128);">协议加载</span><span style="color: rgb(128,128,128);">HTML</span><span style="color: rgb(128,128,128);">时，所有</span><span style="color: rgb(128,128,128);">JsBridge</span><span style="color: rgb(128,128,128);">方法只允许</span><span style="color: rgb(128,128,128);">Download</span><span style="color: rgb(128,128,128);">目录下的</span><span style="color: rgb(128,128,128);">HTML</span><span style="color: rgb(128,128,128);">调用</span></em>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(0,0,255);">]</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
```


 
- 需要针对JsBridge的某些方法进行权限管控时，应同时在object级和该方法的method级配置相同scheme、host、port的白名单，且path不能冲突（完全相同或method级path为object级path的子目录）。配置项如下（使用对象形式方便修改和展示，实际使用时需将对象转换为JSON字符串格式）：
```json
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">webview </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkWeb'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">fileIo</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">picker </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.CoreFileKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">common </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.AbilityKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">JSON </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkTS'</span><span style="color: rgb(181,106,1);">;</span>

class <span style="color: rgb(0,0,255);">TestClass </span><span style="color: rgb(255,0,170);">{</span>
  constructor<span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">  }</span>

  <span style="color: rgb(0,0,255);">test</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">param</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(255,0,170);">{</span>
    return <span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">param</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">-</span><span style="color: rgb(255,0,170);">></span><span style="color: rgb(255,0,170);">Hello, I am ets!`</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

interface <span style="color: rgb(0,0,255);">JsBridgePermission </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">javascriptProxyPermission</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">JavascriptProxyPermission</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

interface <span style="color: rgb(0,0,255);">JavascriptProxyPermission </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">urlPermissionList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">UrlPermission</span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">methodList</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">MethodPermission</span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

interface <span style="color: rgb(0,0,255);">MethodPermission </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">urlPermissionList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">UrlPermission</span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">methodName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

interface <span style="color: rgb(0,0,255);">UrlPermission </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">scheme</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">host</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">port</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">path</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">webviewController</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">声明需要注册的对象</span></em>
  <span style="color: rgb(0,0,255);">testObj</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TestClass </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">TestClass</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">jsBridgePermission</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">JsBridgePermission </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">javascriptProxyPermission</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">urlPermissionList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">[</span> <em>// Object</em><em><span style="color: rgb(128,128,128);">级权限，如果匹配，所有</span><span style="color: rgb(128,128,128);">Method</span><span style="color: rgb(128,128,128);">都授权</span></em>
        <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">scheme</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'resource'</span><span style="color: rgb(181,106,1);">,</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">精确匹配，不能为空</span></em>
          <span style="color: rgb(0,0,255);">host</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'rawfile'</span><span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">精确匹配，不能为空</span></em>
          <span style="color: rgb(0,0,255);">port</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">,</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">精确匹配，为空不检查</span></em>
          <span style="color: rgb(0,0,255);">path</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">''             </span><em>  </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">前缀匹配，为空不检查</span></em>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">scheme</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'file'</span><span style="color: rgb(181,106,1);">,</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">精确匹配，不能为空</span></em>
          <span style="color: rgb(0,0,255);">host</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'docs'</span><span style="color: rgb(181,106,1);">, </span><em>// </em><em><span style="color: rgb(128,128,128);">精确匹配，不能为空</span></em>
          <span style="color: rgb(0,0,255);">port</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">, </span><em>// </em><em><span style="color: rgb(128,128,128);">精确匹配，为空不检查</span></em>
          <span style="color: rgb(0,0,255);">path</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'/storage/Users/currentUser/'         </span><em>  </em><em><span style="color: rgb(128,128,128);">// file</span><span style="color: rgb(128,128,128);">协议加载</span><span style="color: rgb(128,128,128);">HTML</span><span style="color: rgb(128,128,128);">时，所有</span><span style="color: rgb(128,128,128);">JsBridge</span><span style="color: rgb(128,128,128);">方法只允许</span><span style="color: rgb(128,128,128);">docs/storage/Users/currentUser/</span><span style="color: rgb(128,128,128);">目录下的</span><span style="color: rgb(128,128,128);">HTML</span><span style="color: rgb(128,128,128);">调用</span></em>
        <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">methodList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">[</span>
        <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">methodName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'test'</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">urlPermissionList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">[</span><em> // Method</em><em><span style="color: rgb(128,128,128);">级权限</span></em>
            <span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">scheme</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'resource'</span><span style="color: rgb(181,106,1);">, </span><em>// </em><em><span style="color: rgb(128,128,128);">精确匹配，不能为空</span></em>
              <span style="color: rgb(0,0,255);">host</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'rawfile'</span><span style="color: rgb(181,106,1);">,</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">精确匹配，不能为空</span></em>
              <span style="color: rgb(0,0,255);">port</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">,</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">精确匹配，为空不检查</span></em>
              <span style="color: rgb(0,0,255);">path</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">''         </span><em>  </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">前缀匹配，为空不检查</span></em>
            <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">scheme</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'file'</span><span style="color: rgb(181,106,1);">, </span><em>// </em><em><span style="color: rgb(128,128,128);">精确匹配，不能为空</span></em>
              <span style="color: rgb(0,0,255);">host</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'docs'</span><span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">精确匹配，不能为空</span></em>
              <span style="color: rgb(0,0,255);">port</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">,</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">精确匹配，为空不检查</span></em>
              <span style="color: rgb(0,0,255);">path</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'/storage/Users/currentUser/Download/'         </span><em>  </em><em><span style="color: rgb(128,128,128);">// file</span><span style="color: rgb(128,128,128);">协议加载</span><span style="color: rgb(128,128,128);">HTML</span><span style="color: rgb(128,128,128);">时，</span><span style="color: rgb(128,128,128);">test</span><span style="color: rgb(128,128,128);">方法只允许</span><span style="color: rgb(128,128,128);">Download</span><span style="color: rgb(128,128,128);">目录下的</span><span style="color: rgb(128,128,128);">HTML</span><span style="color: rgb(128,128,128);">调用</span></em>
            <span style="color: rgb(255,0,170);">}</span>
          <span style="color: rgb(0,0,255);">]</span>
        <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(0,0,255);">]</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">将</span><span style="color: rgb(255,0,170);">index.html</span><span style="color: rgb(255,0,170);">下载到</span><span style="color: rgb(255,0,170);">Download</span><span style="color: rgb(255,0,170);">目录</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">type</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">ButtonType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ROUNDED_RECTANGLE</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(</span>async <span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          try <span style="color: rgb(255,0,170);">{</span>
            let <span style="color: rgb(0,0,255);">context </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(0,0,255);">() </span>as <span style="color: rgb(0,0,255);">common</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">UIAbilityContext</span><span style="color: rgb(181,106,1);">;</span>
            let <span style="color: rgb(0,0,255);">documentSaveOptions </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">picker</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">DocumentSaveOptions</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(0,0,255);">documentSaveOptions</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">newFileNames </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">'index.html'</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
            let <span style="color: rgb(0,0,255);">documentPicker </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">picker</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">DocumentViewPicker</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(0,0,255);">documentPicker</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">save</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">documentSaveOptions</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">documentSelectResult</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'DocumentViewPicker.select successfully, documentSelectResult uri: ' </span><span style="color: rgb(181,106,1);">+</span>
              <span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">documentSelectResult</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
              let <span style="color: rgb(0,0,255);">path </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">documentSelectResult</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
              let <span style="color: rgb(0,0,255);">file </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">fileIo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">openSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">path</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">fileIo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">OpenMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">READ_WRITE</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
              let <span style="color: rgb(0,0,255);">data </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">resourceManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getRawFileContentSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'index.html'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(0,0,255);">fileIo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">writeSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">file</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fd</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">buffer</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(0,0,255);">fileIo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">closeSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">file</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">文件写入成功</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`DocumentViewPicker.select failed with err, code is: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, message is: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Failed to getRdbStore. code: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, message: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">选择</span><span style="color: rgb(255,0,170);">Download</span><span style="color: rgb(255,0,170);">下</span><span style="color: rgb(255,0,170);">index.html'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">choseHtml</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Web</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">webviewController </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">javaScriptProxy</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">object</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">testObj</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'testObjName'</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">methodList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">'test'</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">webviewController</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">asyncMethodList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">permission</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">jsBridgePermission</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fileAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">javaScriptAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">geolocationAccess</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">domStorageAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">choseHtml</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    const <span style="color: rgb(0,0,255);">documentSelectOptions </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">picker</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">DocumentSelectOptions</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">documentSelectOptions</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">maxSelectNumber </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">documentSelectOptions</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fileSuffixFilters </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">文档</span><span style="color: rgb(255,0,170);">|.html'</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(0,0,255);">uris</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(0,0,255);">context </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(0,0,255);">() </span>as <span style="color: rgb(0,0,255);">common</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">UIAbilityContext</span><span style="color: rgb(181,106,1);">;</span>
    const <span style="color: rgb(0,0,255);">documentViewPicker </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">picker</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">DocumentViewPicker</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">documentViewPicker</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">select</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">documentSelectOptions</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">documentSelectResult</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">uris </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">documentSelectResult</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">uris</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// file://docs/storage/Users/currentUser/Download/index.html</span></em>
      try <span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">webviewController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadUrl</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">uris</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`ErrorCode: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error </span>as <span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">,  Message: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error </span>as <span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Invoke documentViewPicker.select failed, code is </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, message is </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```


 
完整示例参考如下：
 
ArkTS示例代码：
 
```json
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">webview </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkWeb'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">fileIo</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">picker </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.CoreFileKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">common </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.AbilityKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">JSON </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkTS'</span><span style="color: rgb(181,106,1);">;</span>

class <span style="color: rgb(0,0,255);">TestClass </span><span style="color: rgb(255,0,170);">{</span>
  constructor<span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">  }</span>

  <span style="color: rgb(0,0,255);">test</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">param</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(255,0,170);">{</span>
    return <span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">param</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">-</span><span style="color: rgb(255,0,170);">></span><span style="color: rgb(255,0,170);">Hello, I am ets!`</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

interface <span style="color: rgb(0,0,255);">JsBridgePermission </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">javascriptProxyPermission</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">JavascriptProxyPermission</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

interface <span style="color: rgb(0,0,255);">JavascriptProxyPermission </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">urlPermissionList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">UrlPermission</span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">methodList</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">MethodPermission</span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

interface <span style="color: rgb(0,0,255);">MethodPermission </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">urlPermissionList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">UrlPermission</span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">methodName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

interface <span style="color: rgb(0,0,255);">UrlPermission </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">scheme</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">host</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">port</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">path</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">webviewController</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">声明需要注册的对象</span></em>
  <span style="color: rgb(0,0,255);">testObj</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TestClass </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">TestClass</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">jsBridgePermission</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">JsBridgePermission </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">javascriptProxyPermission</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">urlPermissionList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">[</span> <em>// Object</em><em><span style="color: rgb(128,128,128);">级权限，如果匹配，所有</span><span style="color: rgb(128,128,128);">Method</span><span style="color: rgb(128,128,128);">都授权</span></em>
        <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">scheme</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'resource'</span><span style="color: rgb(181,106,1);">, </span><em>// </em><em><span style="color: rgb(128,128,128);">精确匹配，不能为空</span></em>
          <span style="color: rgb(0,0,255);">host</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'rawfile'</span><span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">精确匹配，不能为空</span></em>
          <span style="color: rgb(0,0,255);">port</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">精确匹配，为空不检查</span></em>
          <span style="color: rgb(0,0,255);">path</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">''             </span><em>  </em><em><span style="color: rgb(128,128,128);">// </span></em><em>前缀匹配，为空不检查</em>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">scheme</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'file'</span><span style="color: rgb(181,106,1);">, </span><em>// </em><em><span style="color: rgb(128,128,128);">精确匹配，不能为空</span></em>
          <span style="color: rgb(0,0,255);">host</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'docs'</span><span style="color: rgb(181,106,1);">,</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">精确匹配，不能为空</span></em>
          <span style="color: rgb(0,0,255);">port</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">精确匹配，为空不检查</span></em>
          <span style="color: rgb(0,0,255);">path</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'/storage/Users/currentUser/'         </span><em>  </em><em><span style="color: rgb(128,128,128);">// file</span><span style="color: rgb(128,128,128);">协议加载</span><span style="color: rgb(128,128,128);">HTML</span><span style="color: rgb(128,128,128);">时，所有</span><span style="color: rgb(128,128,128);">JsBridge</span><span style="color: rgb(128,128,128);">方法只允许</span><span style="color: rgb(128,128,128);">docs/storage/Users/currentUser/</span><span style="color: rgb(128,128,128);">目录下的</span><span style="color: rgb(128,128,128);">HTML</span><span style="color: rgb(128,128,128);">调用</span></em>
        <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">methodList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">[</span>
        <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">methodName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'test'</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">urlPermissionList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">[</span><em> // Method</em><em><span style="color: rgb(128,128,128);">级权限</span></em>
            <span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">scheme</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'resource'</span><span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">精确匹配，不能为空</span></em>
              <span style="color: rgb(0,0,255);">host</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'rawfile'</span><span style="color: rgb(181,106,1);">,</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">精确匹配，不能为空</span></em>
              <span style="color: rgb(0,0,255);">port</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">精确匹配，为空不检查</span></em>
              <span style="color: rgb(0,0,255);">path</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">''       </span><em>    </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">前缀匹配，为空不检查</span></em>
            <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">scheme</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'file'</span><span style="color: rgb(181,106,1);">,</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">精确匹配，不能为空</span></em>
              <span style="color: rgb(0,0,255);">host</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'docs'</span><span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">精确匹配，不能为空</span></em>
              <span style="color: rgb(0,0,255);">port</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">, </span><em>// </em><em><span style="color: rgb(128,128,128);">精确匹配，为空不检查</span></em>
              <span style="color: rgb(0,0,255);">path</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'/storage/Users/currentUser/Download/'       </span><em>    </em><em><span style="color: rgb(128,128,128);">// file</span><span style="color: rgb(128,128,128);">协议加载</span><span style="color: rgb(128,128,128);">HTML</span><span style="color: rgb(128,128,128);">时，</span><span style="color: rgb(128,128,128);">test</span><span style="color: rgb(128,128,128);">方法只允许</span><span style="color: rgb(128,128,128);">Download</span><span style="color: rgb(128,128,128);">目录下的</span><span style="color: rgb(128,128,128);">HTML</span><span style="color: rgb(128,128,128);">调用</span></em>
            <span style="color: rgb(255,0,170);">}</span>
          <span style="color: rgb(0,0,255);">]</span>
        <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(0,0,255);">]</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">将</span><span style="color: rgb(255,0,170);">index.html</span><span style="color: rgb(255,0,170);">下载到</span><span style="color: rgb(255,0,170);">Download</span><span style="color: rgb(255,0,170);">目录</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">type</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">ButtonType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ROUNDED_RECTANGLE</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(</span>async <span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          try <span style="color: rgb(255,0,170);">{</span>
            let <span style="color: rgb(0,0,255);">context </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(0,0,255);">() </span>as <span style="color: rgb(0,0,255);">common</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">UIAbilityContext</span><span style="color: rgb(181,106,1);">;</span>
            let <span style="color: rgb(0,0,255);">documentSaveOptions </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">picker</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">DocumentSaveOptions</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(0,0,255);">documentSaveOptions</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">newFileNames </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">'index.html'</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
            let <span style="color: rgb(0,0,255);">documentPicker </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">picker</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">DocumentViewPicker</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(0,0,255);">documentPicker</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">save</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">documentSaveOptions</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">documentSelectResult</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'DocumentViewPicker.select successfully, documentSelectResult uri: ' </span><span style="color: rgb(181,106,1);">+</span>
              <span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">documentSelectResult</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
              let <span style="color: rgb(0,0,255);">path </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">documentSelectResult</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
              let <span style="color: rgb(0,0,255);">file </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">fileIo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">openSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">path</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">fileIo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">OpenMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">READ_WRITE</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
              let <span style="color: rgb(0,0,255);">data </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">resourceManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getRawFileContentSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'index.html'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(0,0,255);">fileIo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">writeSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">file</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fd</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">buffer</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(0,0,255);">fileIo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">closeSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">file</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">文件写入成功</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`DocumentViewPicker.select failed with err, code is: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, message is: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Failed to getRdbStore. code: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, message: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">选择</span><span style="color: rgb(255,0,170);">Download</span><span style="color: rgb(255,0,170);">下</span><span style="color: rgb(255,0,170);">index.html'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">choseHtml</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Web</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">webviewController </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">javaScriptProxy</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">object</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">testObj</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'testObjName'</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">methodList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">'test'</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">webviewController</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">asyncMethodList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">permission</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">jsBridgePermission</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fileAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">javaScriptAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">geolocationAccess</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">domStorageAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">choseHtml</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    const <span style="color: rgb(0,0,255);">documentSelectOptions </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">picker</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">DocumentSelectOptions</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">documentSelectOptions</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">maxSelectNumber </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">documentSelectOptions</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fileSuffixFilters </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">文档</span><span style="color: rgb(255,0,170);">|.html'</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(0,0,255);">uris</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(0,0,255);">context </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(0,0,255);">() </span>as <span style="color: rgb(0,0,255);">common</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">UIAbilityContext</span><span style="color: rgb(181,106,1);">;</span>
    const <span style="color: rgb(0,0,255);">documentViewPicker </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">picker</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">DocumentViewPicker</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">documentViewPicker</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">select</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">documentSelectOptions</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">documentSelectResult</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">uris </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">documentSelectResult</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">uris</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// file://docs/storage/Users/currentUser/Download/index.html</span></em>
      try <span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">webviewController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadUrl</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">uris</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`ErrorCode: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error </span>as <span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">,  Message: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error </span>as <span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Invoke documentViewPicker.select failed, code is </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, message is </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
html示例代码：
 
```text
<em><!-- index.html --></em>
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no"/>
    <style>
        button {
          width: 200px;
          height: 60px;
          font-size: 20px;
        }
        #demo {
          font-size: 24px;
          font-weight: 700;
        }
    </style>
</head>
<body>
<button class="inline-style-button" type="button" onclick="callArkTSMethod()">
    CallArkTS Method
</button>
<p id="demo"></p>
<script>
    function callArkTSMethod() {
      let str = testObjName.test("Hi, I am H5.");
      document.getElementById("demo").innerHTML = str;
    }
</script>
</body>
</html>
```
 
 

#### 总结

要允许注入的JsBridge的方法A被调用，可参考如下修改建议：
 
- 不需要对JsBridge进行权限管控时，不配置JavaScriptProxy的permission参数即可。
- 只需要对JsBridge的所有方法统一权限管控时，只配置JavaScriptProxy的permission参数的object级白名单即可。
- 需要针对JsBridge的某些方法进行权限管控时，应同时在object级和该方法的method级配置相同scheme、host、port的白名单，且path不能冲突（完全相同或method级path为object级path的子目录）。
