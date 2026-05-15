# @performance/object-creation-check（已下线）

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-object-creation-check

建议使用字面量进行对象创建。仅支持检查ts文件，暂不支持ets文件检查。该规则已于5.0.3.500版本下线。


## 规则配置


```text
// code-linter.json5
{
  "rules": {
    "@performance/object-creation-check": "suggestion",
  }
}
```


## 选项

该规则无需配置额外选项。

## 正例


```text
// Test.ts
// 创建一个array
let arr: number[] = [];
// 创建一个普通对象
let obj = {};
// 创建一个正则对象
let reg = /../;
```


## 反例


```text
// Test.ts
// 创建一个array
let arr: number[] = new Array();
// 创建一个普通对象
let obj = new Object();
// 创建一个正则对象
let reg = new RegExp('..');
```


## 规则集


```text
plugin:@performance/all
```

 Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
