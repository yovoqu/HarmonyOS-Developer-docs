# @typescript-eslint/no-unnecessary-type-constraint

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unnecessary-type-constraint

不允许在泛型中使用不必要的约束条件。

 泛型参数（）如果不包含“extends”关键字，默认约束条件是“unknown”（即），所以““、““的写法是多余的。

 该规则仅支持对.js/.ts文件进行检查。


## 规则配置


```text
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-unnecessary-type-constraint": "error"
  }
}
```


## 选项

该规则无需配置额外选项。

## 正例


```text
export interface Foo {
  foo: T;
}

export const bar = (param: T): void => {
  console.info(`${param as string}`);
};

export function foo(param: T): void {
  console.info(`${param as string}`);
}
```


## 反例


```text
// extends any或者extends unknown的写法是多余的
export interface Foo {
  foo: T;
}

export const bar = (param: T): void => {
  console.info(`${param as string}`);
};

export function foo(param: T): void {
  console.info(`${param as string}`);
}
```


## 规则集


```text
plugin:@typescript-eslint/recommended
plugin:@typescript-eslint/all
```

 Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
