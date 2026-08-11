# native如何通过父类创建子类并返回到ArkTS侧

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-development-15

#### 问题现象

C/C++侧同时创建了父类和子类，可以通过父类方法创建子类，ArkTS侧如何调用此类native实现获取到子类实例。
 
 

#### 背景知识

- [napi_new_instance](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-class#napi_new_instance)：通过给定的构造函数实例化一个对象，将这个对象返回ArkTS侧使用。
- [napi_define_class](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-class#napi_define_class)：用于定义一个ArkTS类。该函数允许在Node-API模块中创建一个ArkTS类，并将类的方法和属性与相应的Node-API模块关联起来。
- [napi_wrap](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-class#napi_wrap)：在ArkTS object上绑定一个native对象实例。

 
 

#### 解决方案

代码示例：
 1. native侧Parent类为父类，Child类为子类。
```text
<span style="color: rgb(0,0,255);">extern </span>class <span style="color: rgb(0,0,255);">Child</span><span style="color: rgb(181,106,1);">;</span>

class <span style="color: rgb(0,0,255);">Parent </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">public</span><span style="color: rgb(181,106,1);">:</span>
    <span style="color: rgb(0,0,255);">void </span><span style="color: rgb(0,0,255);">DoSomething</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">Child </span><span style="color: rgb(181,106,1);">*</span><span style="color: rgb(0,0,255);">CreateChild</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>

class <span style="color: rgb(0,0,255);">Child </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Parent </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">public</span><span style="color: rgb(181,106,1);">:</span>
    void <span style="color: rgb(0,0,255);">DoSomething</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
```
 通过napi方法[napi_define_class](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-class#napi_define_class)定义ArkTS侧的Parent类和Child类并导出。

  
```text
<span style="color: rgb(0,0,255);">EXTERN_C_START</span>
<span style="color: rgb(0,0,255);">static napi_value </span><span style="color: rgb(0,0,255);">Init</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">napi_env env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">napi_value exports</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">napi_property_descriptor parentDesc</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">        {</span><span style="color: rgb(255,0,170);">"doSomething"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">ParentDoSomething</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">napi_default</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,0,170);">{</span><span style="color: rgb(255,0,170);">"createChild"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">ParentCreateChild</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">napi_default</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(181,106,1);">;</span>

    <span style="color: rgb(0,0,255);">napi_property_descriptor childDesc</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">        {</span><span style="color: rgb(255,0,170);">"doSomething"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">ChildDoSomething</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">napi_default</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(181,106,1);">;</span>

    <span style="color: rgb(0,0,255);">napi_value parentConstructor </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">napi_define_class</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">"Parent"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">NAPI_AUTO_LENGTH</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">ParentConstructor</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">sizeof</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">parentDesc</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">/ </span><span style="color: rgb(0,0,255);">sizeof</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">parentDesc</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">,</span>
                      <span style="color: rgb(0,0,255);">parentDesc</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(0,0,255);">parentConstructor</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">napi_set_named_property</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">exports</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">"Parent"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">parentConstructor</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

    <span style="color: rgb(0,0,255);">napi_value childConstructor </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">napi_define_class</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">"Child"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">NAPI_AUTO_LENGTH</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">ChildConstructor</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">sizeof</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">childDesc</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">/ </span><span style="color: rgb(0,0,255);">sizeof</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">childDesc</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">,</span>
                      <span style="color: rgb(0,0,255);">childDesc</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(0,0,255);">childConstructor</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">napi_set_named_property</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">exports</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">"Child"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">childConstructor</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    return <span style="color: rgb(0,0,255);">exports</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(0,0,255);">EXTERN_C_END</span>
```
 Index.d.ts中导出的定义：

  
```text
export class <span style="color: rgb(0,0,255);">Parent </span><span style="color: rgb(255,0,170);">{</span>
  constructor<span style="color: rgb(0,0,255);">()</span>

  <span style="color: rgb(0,0,255);">doSomething</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void</span>

  <span style="color: rgb(0,0,255);">createChild</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">obj</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ESObject</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Child</span>
<span style="color: rgb(255,0,170);">}</span>

export class <span style="color: rgb(0,0,255);">Child </span><span style="color: rgb(255,0,170);">{</span>
  constructor<span style="color: rgb(0,0,255);">()</span>

  <span style="color: rgb(0,0,255);">doSomething</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void</span>
<span style="color: rgb(255,0,170);">}</span>
```

2. 执行native侧的ParentCreateChild函数。
- 通过[napi_new_instance](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-class#napi_new_instance)在native端创建一个Child类的实例（也就是Child的native对象）。

3. 该Child实例会被包装成一个可被ArkTS使用的对象（通过[napi_wrap](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-class#napi_wrap)绑定）。

4. 最后，该Child实例被返回给ArkTS侧的createChild()方法。
> [!NOTE]
> 在native层创建Child实例，通过 napi_wrap 包装并绑定，最终返回给ArkTS侧使用。


  
```text
<span style="color: rgb(0,0,255);">static napi_value </span><span style="color: rgb(0,0,255);">ParentCreateChild</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">napi_env env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">napi_callback_info info</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">size_t argc </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">napi_value args</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">napi_value jsthis</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">Parent </span><span style="color: rgb(181,106,1);">*</span><span style="color: rgb(0,0,255);">instanceParent </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">bool bRet </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">napi_value result </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">napi_status status</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">status </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">napi_get_cb_info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(0,0,255);">argc</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">args</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(0,0,255);">jsthis</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">status </span><span style="color: rgb(181,106,1);">!= </span><span style="color: rgb(0,0,255);">napi_ok</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">OH_LOG_ERROR</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">LOG_APP</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">"ParentcreateChild napi_get_cb_info fail.Status:%{public}d"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">status</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    return <span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">status </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">napi_unwrap</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">jsthis</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">reinterpret_cast</span><span style="color: rgb(181,106,1);"><</span>void <span style="color: rgb(181,106,1);">**</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(0,0,255);">instanceParent</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
  if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">status </span><span style="color: rgb(181,106,1);">!= </span><span style="color: rgb(0,0,255);">napi_ok</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">OH_LOG_ERROR</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">LOG_APP</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">"ParentcreateChild napi_unwrap fail.Status:%{public}d"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">status</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    return <span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">status </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">napi_new_instance</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">args</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(0,0,255);">result</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">status </span><span style="color: rgb(181,106,1);">!= </span><span style="color: rgb(0,0,255);">napi_ok</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">OH_LOG_ERROR</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">LOG_APP</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">"ParentcreateChild napi_new_instance fail.Status:%{public}d"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">status</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    return <span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">Child </span><span style="color: rgb(181,106,1);">*</span><span style="color: rgb(0,0,255);">instanceChild </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">instanceParent</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">CreateChild</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>


  <span style="color: rgb(0,0,255);">status </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">napi_wrap</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">result</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">reinterpret_cast</span><span style="color: rgb(181,106,1);"><</span>void <span style="color: rgb(181,106,1);">*</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">instanceChild</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">DerefChild</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">NULL</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">NULL</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">status </span><span style="color: rgb(181,106,1);">!= </span><span style="color: rgb(0,0,255);">napi_ok</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">主动释放内存</span></em>
    <span style="color: rgb(0,0,255);">OH_LOG_INFO</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">LOG_APP</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">"ParentcreateChild ChildConstructor napi_wrap fail status:%{public}d"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">status</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    delete <span style="color: rgb(0,0,255);">instanceChild</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  return <span style="color: rgb(0,0,255);">result</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```

- ArkTS侧的调用逻辑：
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'Hello World'</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.float.page_text_font_size'</span><span style="color: rgb(0,0,255);">))</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontWeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FontWeight</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bold</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'Welcome'</span><span style="color: rgb(181,106,1);">;</span>
            let <span style="color: rgb(0,0,255);">parent </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">testNapi</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Parent</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
            let <span style="color: rgb(0,0,255);">child </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">testNapi</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Child</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(0,0,255);">parent</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">doSomething</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(0,0,255);">child</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">doSomething</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
            let <span style="color: rgb(0,0,255);">newChild</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">testNapi</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Child </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">parent</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createChild</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">testNapi</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Child</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(0,0,255);">newChild</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">doSomething</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```


 
**完整实现如下：**
 
ArkTS侧实现：
 
```text
import <span style="color: rgb(0,0,255);">testNapi </span>from <span style="color: rgb(255,0,170);">'libentry.so'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'Hello World'</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.float.page_text_font_size'</span><span style="color: rgb(0,0,255);">))</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontWeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FontWeight</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bold</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'Welcome'</span><span style="color: rgb(181,106,1);">;</span>
            let <span style="color: rgb(0,0,255);">parent </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">testNapi</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Parent</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
            let <span style="color: rgb(0,0,255);">child </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">testNapi</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Child</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(0,0,255);">parent</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">doSomething</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(0,0,255);">child</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">doSomething</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
            let <span style="color: rgb(0,0,255);">newChild</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">testNapi</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Child </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">parent</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createChild</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">testNapi</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Child</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(0,0,255);">newChild</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">doSomething</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
native侧实现：
 
```text
<span style="color: rgb(181,106,1);">#</span><span style="color: rgb(0,0,255);">include </span><span style="color: rgb(255,0,170);">"hilog/log.h"</span>
<span style="color: rgb(181,106,1);">#</span><span style="color: rgb(0,0,255);">include </span><span style="color: rgb(255,0,170);">"napi/native_api.h"</span>

<span style="color: rgb(181,106,1);">#</span><span style="color: rgb(0,0,255);">define LOG_TAG </span><span style="color: rgb(255,0,170);">"test"</span>
<span style="color: rgb(0,0,255);">extern </span>class <span style="color: rgb(0,0,255);">Child</span><span style="color: rgb(181,106,1);">;</span>

class <span style="color: rgb(0,0,255);">Parent </span><span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(0,0,255);">public</span><span style="color: rgb(181,106,1);">:</span>
    <span style="color: rgb(0,0,255);">void </span><span style="color: rgb(0,0,255);">DoSomething</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">Child </span><span style="color: rgb(181,106,1);">*</span><span style="color: rgb(0,0,255);">CreateChild</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>

class <span style="color: rgb(0,0,255);">Child </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Parent </span><span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(181,106,1);">public</span><span style="color: rgb(181,106,1);">:</span>
    void <span style="color: rgb(0,0,255);">DoSomething</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
void <span style="color: rgb(0,0,255);">Parent</span><span style="color: rgb(181,106,1);">::</span><span style="color: rgb(0,0,255);">DoSomething</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">OH_LOG_ERROR</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">LOG_APP</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">"Parent DoSomething"</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(0,0,255);">Child </span><span style="color: rgb(181,106,1);">*</span><span style="color: rgb(0,0,255);">Parent</span><span style="color: rgb(181,106,1);">::</span><span style="color: rgb(0,0,255);">CreateChild</span><span style="color: rgb(0,0,255);">()</span>
<span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Child </span><span style="color: rgb(181,106,1);">*</span><span style="color: rgb(0,0,255);">instance </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Child</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    return <span style="color: rgb(0,0,255);">instance</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

void <span style="color: rgb(0,0,255);">Child</span><span style="color: rgb(181,106,1);">::</span><span style="color: rgb(0,0,255);">DoSomething</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">OH_LOG_ERROR</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">LOG_APP</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">"Child DoSomething"</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(255,0,170);">}</span>


<span style="color: rgb(0,0,255);">static napi_value </span><span style="color: rgb(0,0,255);">Add</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">napi_env env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">napi_callback_info info</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">size_t argc </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">napi_value args</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>

    <span style="color: rgb(0,0,255);">napi_get_cb_info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(0,0,255);">argc</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">args</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

    <span style="color: rgb(0,0,255);">napi_valuetype valuetype0</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">napi_typeof</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">args</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(0,0,255);">valuetype0</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

    <span style="color: rgb(0,0,255);">napi_valuetype valuetype1</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">napi_typeof</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">args</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(0,0,255);">valuetype1</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

    <span style="color: rgb(0,0,255);">double value0</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">napi_get_value_double</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">args</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(0,0,255);">value0</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

    <span style="color: rgb(0,0,255);">double value1</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">napi_get_value_double</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">args</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(0,0,255);">value1</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

    <span style="color: rgb(0,0,255);">napi_value sum</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">napi_create_double</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">value0 </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">value1</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(0,0,255);">sum</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

    return <span style="color: rgb(0,0,255);">sum</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>


<span style="color: rgb(0,0,255);">static </span>void <span style="color: rgb(0,0,255);">DerefParent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">napi_env env</span><span style="color: rgb(181,106,1);">, </span>void <span style="color: rgb(181,106,1);">*</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">, </span>void <span style="color: rgb(181,106,1);">*</span><span style="color: rgb(0,0,255);">hint</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(255,0,170);">{</span>
    <em>// </em><em><span style="color: rgb(128,128,128);">可选的原生回调，用于在</span><span style="color: rgb(128,128,128);">ArkTS</span><span style="color: rgb(128,128,128);">对象被垃圾回收时释放原生实例</span></em>
    <span style="color: rgb(0,0,255);">OH_LOG_INFO</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">LOG_APP</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">"Node-API DerefItem"</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">Parent </span><span style="color: rgb(181,106,1);">*</span><span style="color: rgb(0,0,255);">obj </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">reinterpret_cast</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">Parent </span><span style="color: rgb(181,106,1);">*</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">obj </span><span style="color: rgb(181,106,1);">!= </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        delete <span style="color: rgb(0,0,255);">obj</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(0,0,255);">static </span>void <span style="color: rgb(0,0,255);">DerefChild</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">napi_env env</span><span style="color: rgb(181,106,1);">, </span>void <span style="color: rgb(181,106,1);">*</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">, </span>void <span style="color: rgb(181,106,1);">*</span><span style="color: rgb(0,0,255);">hint</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(255,0,170);">{</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">可选的原生回调，用于在</span><span style="color: rgb(128,128,128);">ArkTS</span><span style="color: rgb(128,128,128);">对象被垃圾回收时释放原生实例</span></em>
    <span style="color: rgb(0,0,255);">OH_LOG_INFO</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">LOG_APP</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">"Node-API DerefItem"</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">Child </span><span style="color: rgb(181,106,1);">*</span><span style="color: rgb(0,0,255);">obj </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">reinterpret_cast</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">Child </span><span style="color: rgb(181,106,1);">*</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">obj </span><span style="color: rgb(181,106,1);">!= </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        delete <span style="color: rgb(0,0,255);">obj</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>


<span style="color: rgb(0,0,255);">static napi_value </span><span style="color: rgb(0,0,255);">ParentConstructor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">napi_env env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">napi_callback_info info</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">napi_value undefineVar </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">napi_get_undefined</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(0,0,255);">undefineVar</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">napi_value jsInstance </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">napi_get_cb_info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(0,0,255);">jsInstance</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">!= </span><span style="color: rgb(0,0,255);">napi_ok</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        return <span style="color: rgb(0,0,255);">undefineVar</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>

    <span style="color: rgb(0,0,255);">Parent </span><span style="color: rgb(181,106,1);">*</span><span style="color: rgb(0,0,255);">instance </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Parent</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

    <span style="color: rgb(0,0,255);">napi_status status </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">napi_wrap</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">jsInstance</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">reinterpret_cast</span><span style="color: rgb(181,106,1);"><</span>void <span style="color: rgb(181,106,1);">*</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">instance</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">DerefParent</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">NULL</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">NULL</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">status </span><span style="color: rgb(181,106,1);">!= </span><span style="color: rgb(0,0,255);">napi_ok</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">主动释放内存</span></em>
        <span style="color: rgb(0,0,255);">OH_LOG_INFO</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">LOG_APP</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">"ParentConstructor napi_wrap fail"</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        delete <span style="color: rgb(0,0,255);">instance</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(0,0,255);">OH_LOG_INFO</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">LOG_APP</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">"ParentConstructor success"</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    return <span style="color: rgb(0,0,255);">jsInstance</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

<em>// </em><em><span style="color: rgb(128,128,128);">定义类</span><span style="color: rgb(128,128,128);">Parent</span><span style="color: rgb(128,128,128);">的方法</span></em>
<span style="color: rgb(0,0,255);">static napi_value </span><span style="color: rgb(0,0,255);">ParentDoSomething</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">napi_env env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">napi_callback_info info</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">napi_value jsthis</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">Parent </span><span style="color: rgb(181,106,1);">*</span><span style="color: rgb(0,0,255);">instance </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">bool bRet </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">napi_value result </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">napi_get_cb_info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(0,0,255);">jsthis</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

    <span style="color: rgb(0,0,255);">napi_unwrap</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">jsthis</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">reinterpret_cast</span><span style="color: rgb(181,106,1);"><</span>void <span style="color: rgb(181,106,1);">**</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(0,0,255);">instance</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>


    <span style="color: rgb(0,0,255);">instance</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">DoSomething</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    return <span style="color: rgb(0,0,255);">result</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(0,0,255);">static napi_value </span><span style="color: rgb(0,0,255);">ParentCreateChild</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">napi_env env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">napi_callback_info info</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">size_t argc </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">napi_value args</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">napi_value jsthis</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">Parent </span><span style="color: rgb(181,106,1);">*</span><span style="color: rgb(0,0,255);">instanceParent </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">bool bRet </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">napi_value result </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">napi_status status</span><span style="color: rgb(181,106,1);">;</span>

    <span style="color: rgb(0,0,255);">status </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">napi_get_cb_info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(0,0,255);">argc</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">args</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(0,0,255);">jsthis</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">status </span><span style="color: rgb(181,106,1);">!= </span><span style="color: rgb(0,0,255);">napi_ok</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">OH_LOG_ERROR</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">LOG_APP</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">"ParentcreateChild napi_get_cb_info fail.Status:%{public}d"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">status</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        return <span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>

    <span style="color: rgb(0,0,255);">status </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">napi_unwrap</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">jsthis</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">reinterpret_cast</span><span style="color: rgb(181,106,1);"><</span>void <span style="color: rgb(181,106,1);">**</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(0,0,255);">instanceParent</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">status </span><span style="color: rgb(181,106,1);">!= </span><span style="color: rgb(0,0,255);">napi_ok</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">OH_LOG_ERROR</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">LOG_APP</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">"ParentcreateChild napi_unwrap fail.Status:%{public}d"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">status</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        return <span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>

    <span style="color: rgb(0,0,255);">status </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">napi_new_instance</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">args</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(0,0,255);">result</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">status </span><span style="color: rgb(181,106,1);">!= </span><span style="color: rgb(0,0,255);">napi_ok</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">OH_LOG_ERROR</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">LOG_APP</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">"ParentcreateChild napi_new_instance fail.Status:%{public}d"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">status</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        return <span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>

    <span style="color: rgb(0,0,255);">Child </span><span style="color: rgb(181,106,1);">*</span><span style="color: rgb(0,0,255);">instanceChild </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">instanceParent</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">CreateChild</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>


    <span style="color: rgb(0,0,255);">status </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">napi_wrap</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">result</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">reinterpret_cast</span><span style="color: rgb(181,106,1);"><</span>void <span style="color: rgb(181,106,1);">*</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">instanceChild</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">DerefChild</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">NULL</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">NULL</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">status </span><span style="color: rgb(181,106,1);">!= </span><span style="color: rgb(0,0,255);">napi_ok</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
       <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">主动释放内存</span></em>
        <span style="color: rgb(0,0,255);">OH_LOG_INFO</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">LOG_APP</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">"ParentcreateChild ChildConstructor napi_wrap fail status:%{public}d"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">status</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        delete <span style="color: rgb(0,0,255);">instanceChild</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>

    return <span style="color: rgb(0,0,255);">result</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>


<em>// </em><em><span style="color: rgb(128,128,128);">定义类</span><span style="color: rgb(128,128,128);">Child</span><span style="color: rgb(128,128,128);">的构造函数</span></em>
<span style="color: rgb(0,0,255);">static napi_value </span><span style="color: rgb(0,0,255);">ChildConstructor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">napi_env env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">napi_callback_info info</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">napi_value undefineVar </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">napi_get_undefined</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(0,0,255);">undefineVar</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">napi_value jsInstance </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">napi_get_cb_info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(0,0,255);">jsInstance</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">!= </span><span style="color: rgb(0,0,255);">napi_ok</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    return <span style="color: rgb(0,0,255);">undefineVar</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

    <span style="color: rgb(0,0,255);">Child </span><span style="color: rgb(181,106,1);">*</span><span style="color: rgb(0,0,255);">instance </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Child</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">napi_status status </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">napi_wrap</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">jsInstance</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">reinterpret_cast</span><span style="color: rgb(181,106,1);"><</span>void <span style="color: rgb(181,106,1);">*</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">instance</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">DerefChild</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">NULL</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">NULL</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">status </span><span style="color: rgb(181,106,1);">!= </span><span style="color: rgb(0,0,255);">napi_ok</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">主动释放内存</span></em>
        <span style="color: rgb(0,0,255);">OH_LOG_INFO</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">LOG_APP</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">"ChildConstructor napi_wrap fail"</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        delete <span style="color: rgb(0,0,255);">instance</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(0,0,255);">OH_LOG_INFO</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">LOG_APP</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">"ChildConstructor success"</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    return <span style="color: rgb(0,0,255);">jsInstance</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

<em>// </em><em><span style="color: rgb(128,128,128);">定义类</span><span style="color: rgb(128,128,128);">Child</span><span style="color: rgb(128,128,128);">的方法</span></em>
<span style="color: rgb(0,0,255);">static napi_value </span><span style="color: rgb(0,0,255);">ChildDoSomething</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">napi_env env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">napi_callback_info info</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">napi_value jsthis</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">Child </span><span style="color: rgb(181,106,1);">*</span><span style="color: rgb(0,0,255);">instance </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">bool bRet </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">napi_value result </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">napi_get_cb_info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(0,0,255);">jsthis</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

    <span style="color: rgb(0,0,255);">napi_unwrap</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">jsthis</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">reinterpret_cast</span><span style="color: rgb(181,106,1);"><</span>void <span style="color: rgb(181,106,1);">**</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(0,0,255);">instance</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>

    <span style="color: rgb(0,0,255);">instance</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(0,0,255);">DoSomething</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    return <span style="color: rgb(0,0,255);">result</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(0,0,255);">EXTERN_C_START</span>
<span style="color: rgb(0,0,255);">static napi_value </span><span style="color: rgb(0,0,255);">Init</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">napi_env env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">napi_value exports</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">napi_property_descriptor parentDesc</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">        {</span><span style="color: rgb(255,0,170);">"doSomething"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">ParentDoSomething</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">napi_default</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,0,170);">{</span><span style="color: rgb(255,0,170);">"createChild"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">ParentCreateChild</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">napi_default</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(181,106,1);">;</span>

    <span style="color: rgb(0,0,255);">napi_property_descriptor childDesc</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">        {</span><span style="color: rgb(255,0,170);">"doSomething"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">ChildDoSomething</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">napi_default</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(181,106,1);">;</span>

    <span style="color: rgb(0,0,255);">napi_value parentConstructor </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">napi_define_class</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">"Parent"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">NAPI_AUTO_LENGTH</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">ParentConstructor</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">sizeof</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">parentDesc</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">/ </span><span style="color: rgb(0,0,255);">sizeof</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">parentDesc</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">,</span>
                      <span style="color: rgb(0,0,255);">parentDesc</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(0,0,255);">parentConstructor</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">napi_set_named_property</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">exports</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">"Parent"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">parentConstructor</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

    <span style="color: rgb(0,0,255);">napi_value childConstructor </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">napi_define_class</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">"Child"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">NAPI_AUTO_LENGTH</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">ChildConstructor</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">sizeof</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">childDesc</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">/ </span><span style="color: rgb(0,0,255);">sizeof</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">childDesc</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">,</span>
                      <span style="color: rgb(0,0,255);">childDesc</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(0,0,255);">childConstructor</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">napi_set_named_property</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">env</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">exports</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">"Child"</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">childConstructor</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    return <span style="color: rgb(0,0,255);">exports</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(0,0,255);">EXTERN_C_END</span>

<span style="color: rgb(0,0,255);">static napi_module demoModule </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">nm_version </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">,</span>
<span style="color: rgb(181,106,1);">    .</span><span style="color: rgb(0,0,255);">nm_flags </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">,</span>
<span style="color: rgb(181,106,1);">    .</span><span style="color: rgb(0,0,255);">nm_filename </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">nullptr</span><span style="color: rgb(181,106,1);">,</span>
<span style="color: rgb(181,106,1);">    .</span><span style="color: rgb(0,0,255);">nm_register_func </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">Init</span><span style="color: rgb(181,106,1);">,</span>
<span style="color: rgb(181,106,1);">    .</span><span style="color: rgb(0,0,255);">nm_modname </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">"entry"</span><span style="color: rgb(181,106,1);">,</span>
<span style="color: rgb(181,106,1);">    .</span><span style="color: rgb(0,0,255);">nm_priv </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">((</span>void <span style="color: rgb(181,106,1);">*</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">,</span>
<span style="color: rgb(181,106,1);">    .</span><span style="color: rgb(0,0,255);">reserved </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(0,0,255);">extern </span><span style="color: rgb(255,0,170);">"C" </span><span style="color: rgb(0,0,255);">__attribute__</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">constructor</span><span style="color: rgb(0,0,255);">)) </span>void <span style="color: rgb(0,0,255);">RegisterEntryModule</span><span style="color: rgb(0,0,255);">(</span>void<span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">napi_module_register</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(0,0,255);">demoModule</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(255,0,170);">}</span>
```
 
CMakeLists.txt编译脚本：
 
```text
<span style="color: rgb(181,106,1);"># </span><span style="color: rgb(0,0,255);">the minimum version of CMake</span><span style="color: rgb(181,106,1);">.</span>
<span style="color: rgb(0,0,255);">cmake_minimum_required</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">VERSION </span><span style="color: rgb(255,0,0);">3.5.0</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(0,0,255);">project</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">MultipleClass</span><span style="color: rgb(0,0,255);">)</span>

<span style="color: rgb(0,0,255);">set</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">NATIVERENDER_ROOT_PATH $</span><span style="color: rgb(255,0,170);">{</span><span style="color: rgb(0,0,255);">CMAKE_CURRENT_SOURCE_DIR</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>

if<span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">DEFINED PACKAGE_FIND_FILE</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(0,0,255);">include</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">$</span><span style="color: rgb(255,0,170);">{</span><span style="color: rgb(0,0,255);">PACKAGE_FIND_FILE</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(0,0,255);">endif</span><span style="color: rgb(0,0,255);">()</span>

<span style="color: rgb(0,0,255);">include_directories</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">$</span><span style="color: rgb(255,0,170);">{</span><span style="color: rgb(0,0,255);">NATIVERENDER_ROOT_PATH</span><span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(0,0,255);">$</span><span style="color: rgb(255,0,170);">{</span><span style="color: rgb(0,0,255);">NATIVERENDER_ROOT_PATH</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">/include)</span>

<span style="color: rgb(0,0,255);">add_library</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">entry SHARED napi_init</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">cpp</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(0,0,255);">target_link_libraries</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">entry PUBLIC libace_napi</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">z</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">so libhilog_ndk</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">z</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">so</span><span style="color: rgb(0,0,255);">)</span>
```
 
 

#### 常见FAQ

Q：如何构建一个ArkTS指定对象并调用其构造方法？
 
A：可以通过[napi_new_instance](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-class#napi_new_instance)接口调用给定的构造函数实现对象的实例化。
 
 

#### 总结

通过[napi_new_instance](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-class#napi_new_instance)可以在native侧创建一个ArkTS的类实例，调用[napi_wrap](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-class#napi_wrap)方法与native实例进行绑定，再将ArkTS的类实例返回，即可实现通过父类创建子类并返回的效果。
