# @typescript-eslint/space-before-function-paren

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_space-before-function-paren

强制在函数名和括号之间保持一致的空格风格。
 
> [!NOTE]
> 该规则默认要求函数名和括号间有空格。如需修改请参考 选项 。 该规则建议在对.ts文件进行检查时使用。如需检查.ets文件，建议使用 @hw-stylistic/space-before-function-paren 。

 

##### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@typescript-eslint/space-before-function-paren": "error"
  }
}
```
 
 

##### 选项

详情请参考[@typescript-eslint/space-before-function-paren选项](https://eslint.nodejs.cn/docs/rules/space-before-function-paren#选项)。
 
 

##### 正例

```text
// 默认foo和(之间需要一个空格
export function foo () {
  // ...
}
```
 
 

##### 反例

```text
// 默认foo和(之间需要一个空格
export function foo() {
  // ...
}
```
 
 

##### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
