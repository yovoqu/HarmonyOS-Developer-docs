# 调用联系人服务（ContactKit）的queryContacts接口导致应用闪退

更新时间：2026-07-30 01:03:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-contacts-4

#### 问题现象

手机通讯录联系人数量接近十万条，调用联系人服务（ContactKit）的[queryContacts](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-contact#contactquerycontacts10)接口获取通讯录联系人时，方法执行一段时间后，应用出现闪退现象。
 
 

#### 背景知识

- [queryContacts](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-contact#contactquerycontacts10)：查询所有联系人。
- [分析AppFreeze（应用无响应）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appfreeze-guidelines)：用户在使用应用时会出现点击没反应、应用无响应等情况，其超过一定时间限制后即被定义为应用无响应(AppFreeze)。系统提供了检测应用无响应的机制，并生成AppFreeze日志供应用开发分析。

 
 

#### 问题定位

应用运行报出AppFreeze应用无响应，通过日志找到卡死原因是[THREAD_BLOCK_6S](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appfreeze-guidelines#thread_block_6s应用主线程卡死超时)，分析可知是联系人数据量过大导致主线程卡死超时。
 
 

#### 分析结论

应用主线程为单线程，设备在高压情况下，CPU不仅调度queryContacts动作，数据量大的情况下线程执行函数超过6秒，触发AppFreeze，导致应用闪退。
 
 

#### 修改建议

可以将查询放在子线程里执行。
 
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">abilityAccessCtrl</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">common</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">Permissions</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">sendableContextManager </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.AbilityKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">taskpool </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ArkTS'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">contact </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ContactsKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">BusinessError </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

const <span style="color: rgb(255,255,255);">permissions</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">Permissions</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(132,63,161);">'ohos.permission.READ_CONTACTS'</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">;</span>

function <span style="color: rgb(0,0,255);">reqPermissionsFromUser</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">permissions</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">Permissions</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">common</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">UIAbilityContext</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
  let <span style="color: rgb(255,255,255);">atManager</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">abilityAccessCtrl</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">AtManager </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">abilityAccessCtrl</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createAtManager</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">atManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">requestPermissionsFromUser</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">permissions</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">grantStatus</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">authResults</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(255,255,255);">length</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">grantStatus</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length</span><span style="color: rgb(181,106,1);">;</span>
    for <span style="color: rgb(255,0,170);">(</span>let <span style="color: rgb(255,255,255);">i </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(255,255,255);">i </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(255,255,255);">length</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(255,255,255);">i</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">grantStatus</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(255,255,255);">i</span><span style="color: rgb(255,0,170);">] </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
<span style="color: rgb(181,106,1);">      } </span>else <span style="color: rgb(181,106,1);">{</span>
        return<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">    }</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">授权成功。</span></em>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">BusinessError</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`Failed to request permissions from user. Code is </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">, message is </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Sendable</span>
export class <span style="color: rgb(0,0,255);">SendableObject </span><span style="color: rgb(181,106,1);">{</span>
  constructor<span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">sendableContext</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">sendableContextManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">SendableContext</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">contextName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">sendableContext </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">sendableContext</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">contextName </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">contextName</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(255,255,255);">sendableContext</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">sendableContextManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">SendableContext</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">contextName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Concurrent</span>
async function <span style="color: rgb(0,0,255);">queryContactsAsync</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">SendableObject</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">SendableObject</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Promise</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
  let <span style="color: rgb(255,255,255);">num</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
  try <span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Context </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">sendableContextManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">convertToContext</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">SendableObject</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">sendableContext</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(255,255,255);">contactsData</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">contact</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Contact</span><span style="color: rgb(255,0,170);">[] </span><span style="color: rgb(181,106,1);">= </span>await <span style="color: rgb(255,255,255);">contact</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">queryContacts</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">num </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">contactsData</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">log</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`PermissionDetail-queryContacts fail: err-</span><span style="color: rgb(132,63,161);">></span> <span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">} ${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
  return <span style="color: rgb(255,255,255);">num</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">QueryContacts </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">contactNumber</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">子线程查询全量联系人的方法</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">reqPermissionsFromUser</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">permissions</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(255,0,170);">() </span>as <span style="color: rgb(181,106,1);">common</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">UIAbilityContext</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        let <span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">sendableContextManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">SendableContext </span><span style="color: rgb(181,106,1);">=</span>
          <span style="color: rgb(255,255,255);">sendableContextManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">convertFromContext</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(255,0,170);">() </span>as <span style="color: rgb(181,106,1);">Context</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        let <span style="color: rgb(255,255,255);">object</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">SendableObject </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">SendableObject</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'AbilityStageContext'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,255,255);">taskpool</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">execute</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">queryContactsAsync</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">object</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">res</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">object</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          try <span style="color: rgb(181,106,1);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">contactNumber </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">Number</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">res</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">ClassCastException</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'ClassCastException'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">        }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
使用API前需要申请读取通讯录权限：[ohos.permission.READ_CONTACTS](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/restricted-permissions#ohospermissionread_contacts)。
