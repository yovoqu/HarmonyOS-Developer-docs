# @typescript-eslint/restrict-plus-operands

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_restrict-plus-operands

要求加法的两个操作数都是相同的类型，并且是“bigint”、“number”或“string”。


## 规则配置


```text
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/restrict-plus-operands": "error"
  }
}
```


## 选项

详情请参考[@typescript-eslint/restrict-plus-operands选项](https://typescript-eslint.nodejs.cn/rules/restrict-plus-operands/#options)。

## 正例


```text
const num = 10;
const bigIntNum = 1n;
export const foo1 = parseInt('5.5', num) + num;
export const foo2 = bigIntNum + bigIntNum;
```


## 反例


```text
const num = 10;
const bigIntNum = 1n;
export const foo2 = bigIntNum + num;
```


## 规则集


```text
plugin:@typescript-eslint/all
```

 Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
