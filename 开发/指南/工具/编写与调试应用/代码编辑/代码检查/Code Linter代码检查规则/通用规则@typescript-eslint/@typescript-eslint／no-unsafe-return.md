# @typescript-eslint/no-unsafe-return

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-return

函数禁止返回类型为“any”的值。

 该规则仅支持对.js/.ts文件进行检查。


## 规则配置


```text
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-unsafe-return": "error"
  }
}
```


## 选项

该规则无需配置额外选项。

## 正例


```text
export function foo1(): string {
  return '1';
}

export function foo2(): object {
  return Object.create(null) as Record;
}

export const foo3 = (): object[] => [];
export const foo4 = (): string[] => ['a'];

export function assignability1(): Set {
  return new Set(['foo']);
}
```


## 反例


```text
export function foo1(): string {
  return '1' as any;
}

export function foo2(): string {
  return Object.create(null) as any;
}

export const foo3 = (): object[] => [] as any;
export const foo4 = (): string[] => ['a'] as any;

export function assignability1(): Set {
  return new Set(['foo']) as any;
}
```


## 规则集


```text
plugin:@typescript-eslint/recommended
plugin:@typescript-eslint/all
```

 Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
