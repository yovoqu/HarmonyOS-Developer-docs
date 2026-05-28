# @performance/number-init-check

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-number-init-check

该规则将检查number是否正确使用。
 
根据[ArkTS高性能编程实践](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-high-performance-programming)，建议修改。
 

##### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    <span style="color: rgb(135,16,148);">"@performance/number-init-check"</span>: <span style="color: rgb(6,125,23);">"suggestion"</span>,
  }
}
```
 
 

##### 选项

该规则无需配置额外选项。
 
 

##### 正例

```text
<span style="color: rgb(0,0,255);">let</span> intNum = <span style="color: rgb(9,134,88);">1</span>;
intNum = <span style="color: rgb(9,134,88);">2</span>;
<span style="color: rgb(0,0,255);">let</span> floatNum = <span style="color: rgb(9,134,88);">1.3</span>;
floatNum = <span style="color: rgb(9,134,88);">2.4</span>;
```
 
 

##### 反例

```text
<span style="color: rgb(0,0,255);">let</span> intNum = <span style="color: rgb(9,134,88);">1</span>;
<span style="color: rgb(0,128,0);">// intNum is declared as int. Avoid changing it to float.</span>
intNum = <span style="color: rgb(9,134,88);">1.1</span>; 
<span style="color: rgb(0,0,255);">let</span> floatNum = <span style="color: rgb(9,134,88);">1.3</span>;
<span style="color: rgb(0,128,0);">// floatNum is declared as float. Avoid changing it to int.</span>
floatNum = <span style="color: rgb(9,134,88);">2</span>;
```
 
 

##### 规则集

```text
<span style="color: rgb(106,135,89);">plugin:@performance/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
