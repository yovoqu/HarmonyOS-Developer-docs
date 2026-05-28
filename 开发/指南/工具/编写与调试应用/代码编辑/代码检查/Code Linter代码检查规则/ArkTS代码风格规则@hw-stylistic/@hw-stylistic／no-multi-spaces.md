# @hw-stylistic/no-multi-spaces

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-multi-spaces

不允许出现连续多个空格，除非是换行。该规则仅检查.ets文件类型。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@hw-stylistic/no-multi-spaces": "error"
  }
}
```
 
 

#### 选项

该规则无需配置额外选项。
 
 

#### 正例

```text
export const message: string = 'Hello World';
```
 
 

#### 反例

```text
// Multiple spaces found before 'message'.
// Multiple spaces found before 'string'.
// Multiple spaces found before '='.
// Multiple spaces found before 'Hello World'.
export const   message:  string  =  'Hello World';
```
 
 

#### 规则集

```text
<span style="color: rgb(6,125,23);">"plugin:@hw-stylistic/recommended"</span>
<span style="color: rgb(6,125,23);">"plugin:@hw-stylistic/all"</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
