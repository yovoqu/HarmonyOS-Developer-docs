# 单元测试中如何获取上下文Context

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-27

#### 问题现象

部分逻辑需要获取到应用的上下文才能进行单元测试，如何在Instrument Test测试用例中获取Context？
 
 

#### 背景知识

- [Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)：Stage模型的上下文基类，主要用于访问特定应用程序的资源，以及执行应用级操作的回调。
- [getCurrentTopAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitydelegator#getcurrenttopability9-1)：用于获取当前应用顶部Ability。

 
 

#### 解决方案

可以通过getCurrentTopAbility获取当前应用顶部Ability，再获取其Context。示例代码如下：
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">describe</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">it </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@ohos/hypium'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">relationalStore </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkData'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">abilityDelegatorRegistry </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.TestKit'</span><span style="color: rgb(181,106,1);">;</span>

const <span style="color: rgb(0,0,255);">delegator </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">abilityDelegatorRegistry</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getAbilityDelegator</span><span style="color: rgb(0,0,255);">()</span>

export default function <span style="color: rgb(0,0,255);">OhosGetContext</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">describe</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'OhosGetContextTest'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    <em>// Defines a test suite. Two parameters are supported: test suite name and test suite function.</em>
    <span style="color: rgb(0,0,255);">it</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'GetContextTest'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span>async <span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      const <span style="color: rgb(0,0,255);">STORE_CONFIG</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">relationalStore</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">StoreConfig </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
        <em>// </em><em>数据库文件名</em>
        <span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'RdbTest.db'</span><span style="color: rgb(181,106,1);">,</span>
        <em>// </em><em><span style="color: rgb(128,128,128);">数据库安全级别</span></em>
        <span style="color: rgb(0,0,255);">securityLevel</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">relationalStore</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SecurityLevel</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">S3</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
      const <span style="color: rgb(0,0,255);">SQL_CREATE_TABLE </span><span style="color: rgb(181,106,1);">=</span>
        <span style="color: rgb(255,0,170);">'CREATE TABLE IF NOT EXISTS EMPLOYEE (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, AGE INTEGER, SALARY REAL, CODES BLOB, IDENTITY UNLIMITED INT)'</span><span style="color: rgb(181,106,1);">;</span>

      let <span style="color: rgb(0,0,255);">cont </span><span style="color: rgb(181,106,1);">= </span>await <span style="color: rgb(0,0,255);">delegator</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getCurrentTopAbility</span><span style="color: rgb(0,0,255);">()</span>

      await new <span style="color: rgb(0,0,255);">Promise</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">void</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">resolve</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">reject</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">relationalStore</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getRdbStore</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">cont</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">STORE_CONFIG</span><span style="color: rgb(181,106,1);">, </span>async <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">store</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Failed to get RdbStore. Code:</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, message:</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(0,0,255);">reject</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            return<span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Succeeded in getting RdbStore.'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          try <span style="color: rgb(255,0,170);">{</span>
            await <span style="color: rgb(0,0,255);">store</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">execute</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">SQL_CREATE_TABLE</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(0,0,255);">resolve</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Failed to execute sql.`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(0,0,255);">reject</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
> [!NOTE]
> Context本身是一个对象，无法直接打印，但可以按需打印字段，如console.info('deviceTypes：', cont.context.abilityInfo.deviceTypes)可打印测试设备的设备类型。

 
 

#### 常见FAQ

Q：对每个测试文件（如Ability.test.ets）执行Instrument Test可以成功，但是运行整个工程目录（test）只会成功第一个测试文件，这种情况如何解决？
 
A：每个测试文件需要加后置处理步骤，查阅[基础流程能力](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/unittest-guidelines#基础流程能力)，可以在每个测试文件里加入afterAll()，清除当前的Ability： await ability.context.terminateSelf();
 
Q：Instrument Test测试文件的超时时间如何设置？
 
A：在工具栏主菜单单击Run > Edit Configurations进入Run/Debug Configurations界面，选择左边下拉菜单Instrument Test里的测试文件（如Ability.test.ets），在Parameters中设置Time Out参数，并点击OK即可。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/DwK2eHdBQ1KAVe68_X00mg/zh-cn_image_0000002628569458.png?HW-CC-KV=V1&HW-CC-Date=20260701T041011Z&HW-CC-Expire=86400&HW-CC-Sign=36DCA273C97CBBDC34B0E162608592C9AE1211B93B8604A100AC30EAC0E52738)
