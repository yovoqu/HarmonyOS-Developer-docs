# @typescript-eslint/no-invalid-void-type

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-invalid-void-type

禁止在返回类型或者泛型类型之外使用void。


## 规则配置


```text
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-invalid-void-type": "error"
  }
}
```


## 选项

详情请参考[@typescript-eslint/no-invalid-void-type选项](https://typescript-eslint.nodejs.cn/rules/no-invalid-void-type/#options)。

## 正例


```text
export type NoOp = () => void;
export function noop(): void {
  console.info('noop');
}
export const trulyUndefined = void Number.MAX_VALUE;
export async function promiseMeSomething(): Promise {
  return Promise.reject('value').catch(() => {
    console.error('error');
  });
}
export type StillVoid = void | never;
```


## 反例


```text
// 不允许使用void作为类型
export type PossibleValues = string | number | void;
// 不允许使用void作为类型
export type MorePossibleValues = string | (string | void);

// 不允许使用void作为类型
export function logSomething(thing: void) {
  return thing;
}
export function printArg(arg: T) {
  return arg;
}

export interface Interface {
  lambda: () => void;
  // 不允许使用void作为类型
  prop: void;
}
```


## 规则集


```text
plugin:@typescript-eslint/all
```

 Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
