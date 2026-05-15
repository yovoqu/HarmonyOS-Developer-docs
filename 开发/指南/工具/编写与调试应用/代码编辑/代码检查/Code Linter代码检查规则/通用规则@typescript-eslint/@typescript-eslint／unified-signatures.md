# @typescript-eslint/unified-signatures

更新时间：2026-03-09 07:00:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_unified-signatures

如果两个重载函数可以用联合类型参数（|）、可选参数（?）或者剩余参数（...）来重构为一个函数，不允许使用重载。


## 规则配置


```text
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/unified-signatures": "error"
  }
}
```


## 选项

详情请参考[@typescript-eslint/unified-signatures选项](https://typescript-eslint.nodejs.cn/rules/unified-signatures/#options)。

## 正例


```text
export declare function x(a: number | string): void;
export declare function y(...a: readonly number[]): void;
```


## 反例


```text
export declare function x(a: number): void;
export declare function x(a: string): void;

export declare function y(): void;
export declare function y(...a: readonly number[]): void;
```


## 规则集


```text
plugin:@typescript-eslint/all
```

 Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
