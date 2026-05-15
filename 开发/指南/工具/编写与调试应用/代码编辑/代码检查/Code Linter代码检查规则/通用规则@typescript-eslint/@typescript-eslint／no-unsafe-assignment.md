# @typescript-eslint/no-unsafe-assignment

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-assignment

禁止将“any”类型的值赋值给变量和属性。

 该规则仅支持对.ts文件进行检查。


## 规则配置


```text
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-unsafe-assignment": "error"
  }
}
```


## 选项

该规则无需配置额外选项。

## 正例


```text
let [x] = ['1'];
[x] = ['1'] as [string];
console.info([x].toString());

// generic position examples
export const a1: Set = new Set();
export const a2: Map = new Map();
export const a3: Set = new Set();
export const a4: Set>> = new Set>>();
```


## 反例


```text
let [x] = ['1'];
[x] = ['1'] as [any];
[x] = '1' as any;
console.info([x].toString());

// generic position examples
export const a1: Set = new Set();
export const a2: Map = new Map();
export const a3: Set = new Set();
export const a4: Set>> = new Set>>();
```


## 规则集


```text
plugin:@typescript-eslint/recommended
plugin:@typescript-eslint/all
```

 Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
