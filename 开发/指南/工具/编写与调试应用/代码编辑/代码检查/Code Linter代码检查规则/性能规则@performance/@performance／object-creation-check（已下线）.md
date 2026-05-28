# @performance/object-creation-check（已下线）

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-object-creation-check

建议使用字面量进行对象创建。仅支持检查ts文件，暂不支持ets文件检查。该规则已于5.0.3.500版本下线。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    <span style="color: rgb(135,16,148);">"@performance/object-creation-check"</span>: <span style="color: rgb(6,125,23);">"suggestion"</span>,
  }
}
```
 
 

#### 选项

该规则无需配置额外选项。
 
 

#### 正例

```text
// Test.ts
<span style="color: rgb(0,128,0);">// 创建一个array</span>
<span style="color: rgb(0,0,255);">let</span> arr: <span style="color: rgb(0,0,255);">number</span>[] = [];
<span style="color: rgb(0,128,0);">// 创建一个普通对象</span>
<span style="color: rgb(0,0,255);">let</span> obj = {};          
<span style="color: rgb(0,128,0);">// 创建一个正则对象</span>
<span style="color: rgb(0,0,255);">let</span> reg = <span style="color: rgb(128,0,0);">/../</span>;
```
 
 

#### 反例

```text
// Test.ts
<span style="color: rgb(0,128,0);">// 创建一个array</span>
<span style="color: rgb(0,0,255);">let</span> arr: <span style="color: rgb(0,0,255);">number</span>[] = <span style="color: rgb(0,0,255);">new</span> <span style="color: rgb(0,128,128);">Array</span>(); 
<span style="color: rgb(0,128,0);">// 创建一个普通对象</span>
<span style="color: rgb(0,0,255);">let</span> obj = <span style="color: rgb(0,0,255);">new</span> <span style="color: rgb(0,128,128);">Object</span>();          
<span style="color: rgb(0,128,0);">// 创建一个正则对象</span>
<span style="color: rgb(0,0,255);">let</span> reg = <span style="color: rgb(0,0,255);">new</span> <span style="color: rgb(0,128,128);">RegExp</span>(<span style="color: rgb(163,21,21);">'..'</span>);
```
 
 

#### 规则集

```text
<span style="color: rgb(106,135,89);">plugin:@performance/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
