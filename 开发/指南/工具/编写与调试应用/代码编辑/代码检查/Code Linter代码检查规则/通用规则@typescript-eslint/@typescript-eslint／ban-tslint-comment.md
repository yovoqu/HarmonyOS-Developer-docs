# @typescript-eslint/ban-tslint-comment

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_ban-tslint-comment

不允许使用`//tslint:<rule-flag>`格式的注释。
 

##### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@typescript-eslint/ban-tslint-comment": "error"
  }
}
```
 
 

##### 选项

该规则无需配置额外选项。
 
 

##### 正例

```text
// This is a comment that just happens to mention tslint
/* This is a multiline comment that just happens to mention tslint */
console.log('hello'); // This is a comment that just happens to mention tslint
```
 
 

##### 反例

```text
/* tslint:disable */
/* tslint:enable */
/* tslint:disable:rule1 rule2 rule3... */
/* tslint:enable:rule1 rule2 rule3... */
// tslint:disable-next-line
console.log('hello'); // tslint:disable-line
// tslint:disable-next-line:rule1 rule2 rule3...
```
 
 

##### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
