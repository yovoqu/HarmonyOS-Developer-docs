# @performance/hp-performance-no-closures

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-performance-no-closures

建议函数内部变量尽量使用参数传递。
 
根据[ArkTS编程规范](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-high-performance-programming)，建议修改。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    <span style="color: rgb(135,16,148);">"@performance/hp-performance-no-closures"</span>: <span style="color: rgb(6,125,23);">"suggestion"</span>,
  }
}
```
 
 

#### 选项

该规则无需配置额外选项。
 
 

#### 正例

```text
let arr = [0, 1, 2];
function foo(array: Array<number>): number {
  // arr 尽量通过参数传递
  return array[0] + array[1];
}
foo(arr);
```
 
 

#### 反例

```text
let arr = [0, 1, 2];
<span style="color: rgb(86,156,214);">function</span> foo() {
  // arr 尽量通过参数传递
<span style="color: rgb(86,156,214);">  return</span> arr[0] + arr[1];
}
foo();
```
 
 

#### 规则集

```text
<span style="color: rgb(106,135,89);">plugin:@performance/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
