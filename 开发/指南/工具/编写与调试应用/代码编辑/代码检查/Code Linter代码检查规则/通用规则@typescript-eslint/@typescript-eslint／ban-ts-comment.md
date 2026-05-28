# @typescript-eslint/ban-ts-comment

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_ban-ts-comment

不允许使用`@ts-&lt;directional&gt;`格式的注释，或要求在注释后进行补充说明。
 

##### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@typescript-eslint/ban-ts-comment": "error"
  }
}
```
 
 

##### 选项

详情请参考[@typescript-eslint/ban-ts-comment选项](https://typescript-eslint.nodejs.cn/rules/ban-ts-comment/#options)。
 
 

##### 正例

```text
console.log('hello');
```
 
 

##### 反例

```text
// @ts-expect-error
console.log('hello');

/* @ts-expect-error */
console.log('hello');
```
 
 

##### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
