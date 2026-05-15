# @typescript-eslint/semi

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_semi

要求或不允许使用分号。


## 规则配置


```text
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/semi": "error"
  }
}
```


## 选项

详情请参考[@typescript-eslint/semi选项](https://eslint.nodejs.cn/docs/rules/semi#选项)。

## 正例


```text
export const name = 'ESLint';

export class Foo {
  public bar = '1';
}
```


## 反例


```text
// 默认在语句末尾需要加分号
export const name = 'ESLint'

export class Foo {
  // 默认在语句末尾需要加分号
  public bar = '1'
}
```


## 规则集


```text
plugin:@typescript-eslint/all
```

 Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
