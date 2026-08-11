# 创建AVSession出错，错误码6600101

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avsession-20

#### 问题现象

在销毁上一次成功创建的AVSession后创建新的AVSession时，偶尔会出现新AVSession创建失败。报错信息为：CreateSession failed，错误码为6600101。
 
 

#### 背景知识

[AVSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-avsession)是系统提供的音视频管控服务，用于统一管理系统中所有音视频行为，构建音视频统一展示和控制能力。
 
 

#### 问题定位
1. 根据问题现象中的场景和错误码，确定是创建AVSession时出错，原因是[会话服务端异常](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession#section6600101-会话服务端异常)。
2. 参考[createAVSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-f#avsessioncreateavsession10)（创建AVSession），一个Ability只能存在一个AVSession，重复创建会失败，错误码为6600101。推测是重复创建导致错误。
3. 在确保当前AVSession销毁完毕后再创建新的AVSession，创建AVSession成功。
4. 确定是重复创建AVSession导致错误。
 
 

#### 分析结论

一个Ability中只能存在一个AVSession，重复创建会失败。在创建AVSession时，必须确保此时Ability内没有已创建的AVSession存在。
 
 

#### 修改建议

销毁媒体会话的[destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-avsession#destroy10)是异步接口，需要确保销毁流程完毕后，才能创建新的AVSession。
 
```json
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">avSession </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.AVSessionKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">common </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.AbilityKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">session</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">avSession</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">AVSession </span><span style="color: rgb(181,106,1);">= </span>undefined<span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Create Session'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(</span>async <span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          let <span style="color: rgb(0,0,255);">context </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(0,0,255);">() </span>as <span style="color: rgb(0,0,255);">common</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">UIAbilityContext</span><span style="color: rgb(181,106,1);">;</span>
          if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">session </span><span style="color: rgb(181,106,1);">!== </span>undefined<span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">session</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">destroy</span><span style="color: rgb(0,0,255);">()</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">(</span>async <span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
                try <span style="color: rgb(255,0,170);">{</span>
                  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">session </span><span style="color: rgb(181,106,1);">= </span>await <span style="color: rgb(0,0,255);">avSession</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createAVSession</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'SESSION_NAME'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'audio'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
                  <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`create session successfully`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
                <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
                  <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`failed to create session, error=</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
                <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">              }</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
                <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`failed to destroy session, error=</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
            try <span style="color: rgb(255,0,170);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">session </span><span style="color: rgb(181,106,1);">= </span>await <span style="color: rgb(0,0,255);">avSession</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createAVSession</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'SESSION_NAME'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'audio'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`failed to create session, error=</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">          }</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignItems</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
