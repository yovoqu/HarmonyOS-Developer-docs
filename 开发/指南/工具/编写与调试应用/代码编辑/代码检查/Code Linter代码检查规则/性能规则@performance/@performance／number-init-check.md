# @performance/number-init-check

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-number-init-check

该规则将检查number是否正确使用。

 根据[ArkTS高性能编程实践](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-high-performance-programming)，建议修改。


## 规则配置


```text
// code-linter.json5
{
  "rules": {
    "@performance/number-init-check": "suggestion",
  }
}
```


## 选项

该规则无需配置额外选项。

## 正例


```text
let intNum = 1;
intNum = 2;
let floatNum = 1.3;
floatNum = 2.4;
```


## 反例


```text
let intNum = 1;
// intNum is declared as int. Avoid changing it to float.
intNum = 1.1;
let floatNum = 1.3;
// floatNum is declared as float. Avoid changing it to int.
floatNum = 2;
```


## 规则集


```text
plugin:@performance/all
```

 Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
