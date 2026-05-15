# @typescript-eslint/promise-function-async

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_promise-function-async

要求任何返回Promise的函数或方法标记为async。


## 规则配置


```text
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/promise-function-async": "error"
  }
}
```


## 选项

详情请参考[@typescript-eslint/promise-function-async选项](https://typescript-eslint.nodejs.cn/rules/promise-function-async/#options)。

## 正例


```text
export const arrowFunctionReturnsPromise = async () => Promise.resolve('value');

export async function functionReturnsPromise() {
  return Promise.resolve('value');
}

// An explicit return type that is not Promise means this function cannot be made async, so it is ignored by the rule
export function functionReturnsUnionWithPromiseExplicitly(
  p: boolean
): string | Promise {
  return p ? 'value' : Promise.resolve('value');
}

export async function functionReturnsUnionWithPromiseImplicitly(p: boolean) {
  return p ? 'value' : Promise.resolve('value');
}
```


## 反例


```text
export const arrowFunctionReturnsPromise = () => Promise.resolve('value');

export function functionReturnsPromise() {
  return Promise.resolve('value');
}

export function functionReturnsUnionWithPromiseImplicitly(p: boolean) {
  return p ? 'value' : Promise.resolve('value');
}
```


## 规则集


```text
plugin:@typescript-eslint/all
```

 Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
