# @typescript-eslint/prefer-regexp-exec

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-regexp-exec

如果未提供全局标志（/g），推荐使用“RegExp#exec”，而不是“String#match”。


## 规则配置


```text
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/prefer-regexp-exec": "error"
  }
}
```


## 选项

该规则无需配置额外选项。

## 正例


```text
/thing/.exec('something');

'some things are just things'.match(/thing/g);

const text = 'something';
const search = /thing/;
search.exec(text);
```


## 反例


```text
'something'.match(/thing/);

'some things are just things'.match(/thing/);

const text = 'something';
const search = /thing/;
text.match(search);
```


## 规则集


```text
plugin:@typescript-eslint/all
```

 Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
