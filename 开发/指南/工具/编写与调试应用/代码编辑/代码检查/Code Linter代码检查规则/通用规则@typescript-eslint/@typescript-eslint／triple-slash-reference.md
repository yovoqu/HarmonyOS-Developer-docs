# @typescript-eslint/triple-slash-reference

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_triple-slash-reference

不允许某些三斜杠引用，推荐使用ES6风格的导入声明。
 
支持以下三种三斜杠引用方式的检查
 
```text
<span style="color: rgb(128,128,128);">/// </span><span style="color: rgb(128,128,128);"><</span><span style="color: rgb(128,128,128);">reference lib="..." /</span><span style="color: rgb(128,128,128);">></span>
<span style="color: rgb(128,128,128);">/// </span><span style="color: rgb(128,128,128);"><</span><span style="color: rgb(128,128,128);">reference path="..." /</span><span style="color: rgb(128,128,128);">></span> 
<span style="color: rgb(128,128,128);">/// </span><span style="color: rgb(128,128,128);"><</span><span style="color: rgb(128,128,128);">reference types="..." /</span><span style="color: rgb(128,128,128);">></span>
```
 

##### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@typescript-eslint/triple-slash-reference": "error"
  }
}
```
 
 

##### 选项

详情请参考[@typescript-eslint/triple-slash-reference选项](https://typescript-eslint.nodejs.cn/rules/triple-slash-reference/#options)。
 
 

##### 正例

```text
import { value } from 'code';
export { value };
```
 
 

##### 反例

```text
/// <reference path="code" />

globalThis.value;
```
 
 

##### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
