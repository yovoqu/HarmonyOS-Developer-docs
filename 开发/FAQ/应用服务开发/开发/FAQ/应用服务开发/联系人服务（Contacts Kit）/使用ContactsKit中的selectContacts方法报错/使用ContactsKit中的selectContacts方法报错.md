# 使用ContactsKit中的selectContacts方法报错

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-contacts-3

#### 问题现象

使用ContactsKit中的selectContacts方法打开选择联系人UI界面，传入筛选条件（filterClause），执行过程中抛出401错误。导致联系人选择器无法正常显示，无法进行联系人选择操作。
 
 

#### 背景知识

- [contact.selectContacts](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-contact#contactselectcontacts10-2)：用于在应用中弹出联系人选择器的方法，允许用户从系统联系人中选择若干个联系人。
- [ContactSelectionOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-contact#contactselectionoptions10)：用于配置选择联系人条件。
- [ContactSelectionFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-contact#contactselectionfilter15)：用于配置联系人查询过滤条件。

 
 

#### 问题定位

通过分析代码发现，在调用selectContacts方法时，filterClause的参数使用for循环传入了多个filterCondition一样的id，不符合接口预期，从而返回401错误。
 
```json
let <span style="color: rgb(255,255,255);">arr</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">contact</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">FilterOptions</span><span style="color: rgb(255,0,170);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">[]</span>
for <span style="color: rgb(255,0,170);">(</span>const <span style="color: rgb(255,255,255);">id </span>of <span style="color: rgb(255,0,170);">[</span><span style="color: rgb(132,63,161);">'1'</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(132,63,161);">'2'</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(132,63,161);">'3'</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(132,63,161);">'4'</span><span style="color: rgb(255,0,170);">]) </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">arr</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span><span style="color: rgb(255,255,255);">filterCondition</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,255,255);">contact</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">FilterCondition</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">IN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,255,255);">id</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(255,255,255);">contact</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectContacts</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">isMultiSelect</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,255,255);">maxSelectable</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">4</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,255,255);">filter</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">filterType</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,255,255);">contact</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">FilterType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">DEFAULT_SELECT</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">filterClause</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(181,106,1);">{</span><span style="color: rgb(255,255,255);">id</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,255,255);">arr</span><span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span><span style="color: rgb(181,106,1);">,</span>
<span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">BusinessError</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
  if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`selectContact callback, errCode:</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">, errMessage:</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    return<span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
  <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`selectContact callback: success data-</span><span style="color: rgb(132,63,161);">></span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
```
 
 

#### 分析结论

问题根因是filterClause传入参数错误。
 
 

#### 修改建议

若filterCondition一致，无需传入多个id值。
 
```json
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">contact </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ContactsKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">BusinessError </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">SelectContacts </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">选择联系人</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">50</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span><span style="color: rgb(255,255,255);">top</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(80,160,79);">200</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(()</span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">contact</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectContacts</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">isMultiSelect</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,255,255);">maxSelectable</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">4</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,255,255);">filter</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(255,255,255);">filterType</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,255,255);">contact</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">FilterType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">DEFAULT_SELECT</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(255,255,255);">filterClause</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(181,106,1);">{</span><span style="color: rgb(255,255,255);">id</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(181,106,1);">{</span><span style="color: rgb(255,255,255);">filterCondition</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,255,255);">contact</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">FilterCondition</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">IN</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(132,63,161);">'1'</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(132,63,161);">'2'</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(132,63,161);">'3'</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(132,63,161);">'4'</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">            }</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">BusinessError</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`selectContact callback, errCode:</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">, errMessage:</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
              return<span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span>
            <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`selectContact callback: success data-</span><span style="color: rgb(132,63,161);">></span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
