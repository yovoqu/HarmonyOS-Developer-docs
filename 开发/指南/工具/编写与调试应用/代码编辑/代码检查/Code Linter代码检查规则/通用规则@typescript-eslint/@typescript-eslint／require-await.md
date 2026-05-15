# @typescript-eslint/require-await

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_require-await

异步函数必须包含“await”。


## 规则配置


```text
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/require-await": "error"
  }
}
```


## 选项

该规则无需配置额外选项。

## 正例


```text
async function doSomething(): Promise {
  return Promise.resolve();
}

export async function foo() {
  await doSomething();
}

export function baz() {
  doSomething().catch(() => {
    console.info('error');
  });
}
```


## 反例


```text
async function doSomething(): Promise {
  return Promise.resolve();
}

export async function foo() {
  doSomething();
}
```


## 规则集


```text
plugin:@typescript-eslint/all
```

 Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
