# @hw-stylistic/array-bracket-spacing

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_array-bracket-spacing

强制数组“[”之后和“]”之前不加空格。该规则仅检查.ets文件类型。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@hw-stylistic/array-bracket-spacing": "error"
  }
}
```
 
 

#### 选项

该规则无需配置额外选项。
 
 

#### 正例

```text
export const arr = ['a', 'b'];
```
 
 

#### 反例

```text
// There should be no space after '['.
// There should be no space before ']'.
export const arr = [ 'a', 'b' ];
```
 
 

#### 规则集

```text
<span style="color: rgb(6,125,23);">"plugin:@hw-stylistic/recommended"</span>
<span style="color: rgb(6,125,23);">"plugin:@hw-stylistic/all"</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
