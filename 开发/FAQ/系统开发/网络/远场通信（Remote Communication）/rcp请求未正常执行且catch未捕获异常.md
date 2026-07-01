# rcp请求未正常执行且catch未捕获异常

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-remote-communication-4

#### 问题现象

通过rcp访问指定链接，未发现自定义日志打印，catch未捕获异常，程序也未能正常访问链接。
 
问题代码示例参考如下：
 
```json
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">rcp </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.RemoteCommunicationKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

<em>// 1.</em><em><span style="color: rgb(128,128,128);">定义请求地址</span></em>
const <span style="color: rgb(0,0,255);">getAccessTokenUrl </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'https</span><span style="color: rgb(255,0,170);">：</span><span style="color: rgb(255,0,170);">123123123123'</span><span style="color: rgb(181,106,1);">;</span>

<em>// 2.</em><em><span style="color: rgb(128,128,128);">创建会话</span></em>
const <span style="color: rgb(0,0,255);">session </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">rcp</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createSession</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

<em>// 3.</em><em><span style="color: rgb(128,128,128);">构建请求参数对象</span></em>
interface <span style="color: rgb(0,0,255);">GeneratedObjectLiteralInterface_1 </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">clientID</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">clientSecret</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

const <span style="color: rgb(0,0,255);">request</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">GeneratedObjectLiteralInterface_1 </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">clientID</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'123456789'</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(0,0,255);">clientSecret</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'123456789'</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>

<em>// 4.</em><em><span style="color: rgb(128,128,128);">发起</span><span style="color: rgb(128,128,128);">POST</span><span style="color: rgb(128,128,128);">请求获取</span><span style="color: rgb(128,128,128);">Access Token</span></em>
<span style="color: rgb(0,0,255);">session</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">post</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">getAccessTokenUrl</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">request</span><span style="color: rgb(0,0,255);">))</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">response</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">请求成功，响应内容</span><span style="color: rgb(255,0,170);">: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">response</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">可选：解析</span><span style="color: rgb(128,128,128);">JSON</span><span style="color: rgb(128,128,128);">响应</span></em>
    try <span style="color: rgb(255,0,170);">{</span>
      const <span style="color: rgb(0,0,255);">data </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">response</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">解析后的</span><span style="color: rgb(255,0,170);"> Token </span><span style="color: rgb(255,0,170);">数据</span><span style="color: rgb(255,0,170);">:`</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">warn</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">响应内容无法解析为</span><span style="color: rgb(255,0,170);"> JSON`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">请求失败，错误码</span><span style="color: rgb(255,0,170);">: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, </span><span style="color: rgb(255,0,170);">消息</span><span style="color: rgb(255,0,170);">: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
```
 
 

#### 背景知识

[rcp](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-rcp)访问网络，通过回调获取结果，并使用[Console ](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-logs)输出相关内容到控制台。
 
其中[Promise](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/async-concurrency-overview#promise)提供了then、catch、finally方法来注册回调函数，以处理异步操作的成功或失败结果，但是，若调用本身存在问题，不能执行接口，则无法执行回调。
 
 

#### 问题定位

上述场景中对post回调结果以及异常进行捕获，但并未捕获post本身的使用异常。
 
 

#### 分析结论

需要对post语句本身使用try-catch进行异常捕获，并根据相应信息处理问题。
 
 

#### 修改建议

使用try-catch捕获post异常，并根据错误码处理。
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">rcp </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.RemoteCommunicationKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>


<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Transform </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Flex</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">direction</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">FlexDirection</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">alignItems</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ItemAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'POST</span><span style="color: rgb(255,0,170);">请求</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          try <span style="color: rgb(255,0,170);">{</span>
           <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">定义请求地址，使用时请变更为所需地址</span></em>
            const <span style="color: rgb(0,0,255);">getAccessTokenUrl </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'https</span><span style="color: rgb(255,0,170);">：</span><span style="color: rgb(255,0,170);">123123123123'</span><span style="color: rgb(181,106,1);">;</span>
        <em>    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">创建会话</span></em>
            const <span style="color: rgb(0,0,255);">session </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">rcp</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createSession</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
           <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">发起</span><span style="color: rgb(128,128,128);">POST</span><span style="color: rgb(128,128,128);">请求获取</span><span style="color: rgb(128,128,128);">Access Token</span></em>
            <span style="color: rgb(0,0,255);">session</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">post</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">getAccessTokenUrl</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">response</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
                <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Succeeded in getting the response </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">response</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
                <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Failed in getting the response, error code: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, error message: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Failed in coding, error code: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, error data:</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, error message: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
常见错误码及处理方式如下：
 
- 场景一：
错误信息：code：[201](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)，data：Permission Denied。
- 信息分析：信息为权限申请失败，通过post接口可知，post需要权限：ohos.permission.INTERNET(如果使用PathPreference的'cellular'模式，则额外需要ohos.permission.GET_NETWORK_INFO)
- 处理方案：在module.json5中配置ohos.permission.INTERNET权限信息。

 - 场景二：
错误信息：code：[10200002](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-utils#section10200002-参数解析错误)，message：Syntax Error. Invalid Url string。
- 信息分析：信息为入参错误，无效的Url链接，可以检查传入的Url参数或者直接使用HarmonyOS浏览器访问，确认Url是否可用。
- 处理方案：传入正确格式的链接。

 
 
 

#### 常见FAQ

Q：使用rcp请求服务端接口时返回400 Bad Request响应状态码？
 
A：该响应码通常是提交数据的字段名称或者是字段类型和后台的实体类不一致，或者提交的数据格式与服务端接口的数据格式不一致。请对照字段名称，类型保证一致性，保证请求的数据格式的正确性。
 
Q：使用rcp下载文件报错，报错信息{"code":1007900028,"data":"Timeout was reached"}？
 
A：可以尝试增大[timeout](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-rcp#section253517541009)的时间。
 
Q：可以使用哪些API实现post类型的长连接？例如聊天场景。
 
A：可以使用[rcp](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-rcp)和[@ohos.net.http](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-http)，在请求头中添加：Connection: keep-alive。
 
Q：rcp网络请求想要实现防止重复请求，除了防抖和节流，有没有更好的实现方式？
 
A：为避免网络重复请求可以考虑如下方案措施：
 1. 客户端及服务端设置请求超时时间，如果在规定时间内没有收到响应，则认为请求失败避免重复发送请求。
2. 发送请求头中使用唯一标识避免重复请求。
3. 请求中设置缓存技术，避免重复请求相同的数据。
 
 

#### 总结

若某段代码执行不符合预期，可以用try-catch捕获其中的异常信息，或者使用断点调试的方案，查看预期执行逻辑停止位置，然后具体分析。
