# @security/no-commented-code

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-commented-code

不使用的代码段建议直接删除，不允许通过注释的方式保留。


## 规则配置


```text
// code-linter.json5
{
  "rules": {
    "@security/no-commented-code": "warn"
  }
}
```


## 选项

该规则无需配置额外选项。

## 正例


```text
// this is a comment
```


## 反例


```text
// console.log('info')
```


## 规则集


```text
plugin:@security/recommended
plugin:@security/all
```

 Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
