# @hw-stylistic/semi-spacing

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_semi-spacing

强制分号之前不加空格。该规则仅检查.ets文件类型。


## 规则配置


```text
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/semi-spacing": "error"
  }
}
```


## 选项

该规则无需配置额外选项。

## 正例


```text
export {x, test, C};

const x = 10;

function test(size: number): number {
  let sum = 0;
  for (let a = 0; a

## 反例


```text
// Unexpected whitespace before semicolon.
export {x, test, C} ;

// Unexpected whitespace before semicolon.
const x = 10 ;

function test(size: number): number {
let sum = 0;
// Unexpected whitespace before semicolon.
// Unexpected whitespace before semicolon.
for (let a = 0 ; a

## 规则集


```text
"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"
```

 Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
