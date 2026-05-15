# @hw-stylistic/space-before-function-paren

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-space-before-function-paren-stylistic

在函数名和“(”之间强制不加空格。该规则仅检查.ets文件类型。


## 规则配置


```text
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/space-before-function-paren": "error"
  }
}
```


## 选项

该规则无需配置额外选项。

## 正例


```text
function bar() {
  // doSomething
}
bar();
```


## 反例


```text
// Unexpected space before function parentheses.
function bar () {
  // doSomething
}
// Unexpected space before function parentheses.
bar  ();
```


## 规则集


```text
"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"
```

 Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
