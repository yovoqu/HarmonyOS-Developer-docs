# @hw-stylistic/brace-style

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-brace-style-stylistic

强制大括号和语句位于同一行。该规则仅检查.ets文件类型。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@hw-stylistic/brace-style": "error"
  }
}
```
 
 

#### 选项

该规则无需配置额外选项。
 
 

#### 正例

```text
try {
  // doSomething
} catch (e) {
  // doSomething
} finally {
  // doSomething
}
```
 
 

#### 反例

```text
try
// Opening curly brace does not appear on the same line as statement before.
{

// Closing curly brace does not appear on the same line as statement after.
}
catch (e)
// Opening curly brace does not appear on the same line as statement before.
{

// Closing curly brace does not appear on the same line as statement after.
}
finally
// Opening curly brace does not appear on the same line as statement before.
{

}
```
 
 

#### 规则集

```text
<span style="color: rgb(6,125,23);">"plugin:@hw-stylistic/recommended"</span>
<span style="color: rgb(6,125,23);">"plugin:@hw-stylistic/all"</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
