# @hw-stylistic/no-tabs

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-tabs

禁止使用tab作为缩进，推荐使用空格。该规则仅检查.ets文件类型。


## 规则配置


```text
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/no-tabs": "error"
  }
}
```


## 选项

该规则无需配置额外选项。

## 正例


```text
export const message: string = 'Hello World';
```


## 反例


```text
export	const	message:	string = 'Hello World';
```


## 规则集


```text
"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"
```

 Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
