# @typescript-eslint/no-unnecessary-type-arguments

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unnecessary-type-arguments

当类型参数和默认值相同时，不允许显式使用。


## 规则配置


```text
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-unnecessary-type-arguments": "error"
  }
}
```


## 选项

该规则无需配置额外选项。

## 正例


```text
function f(para: T): void {
  console.info(`${para as number}`);
}
f(Number.MAX_VALUE);
f('hello');

function g(para1: T, para2?: U) {
  if (para2 !== undefined) {
    console.info(`${para2 as string}`);
  }
  console.info(`${para1 as number}`);
}
g('para1', 'para2');
g(Number.MAX_VALUE);

class C {
  public name: T;

  public constructor(name: T) {
    this.name = name;
  }
}
new C(Number.MAX_VALUE);
new C('hello');
```


## 反例


```text
function f(para: T): void {
  console.info(`${para as number}`);
}
// 参数类型默认是number，直接使用f()即可
f(Number.MAX_VALUE);

function g(para1: T, para2?: U) {
  if (para2 !== undefined) {
    console.info(`${para2 as string}`);
  }
  console.info(`${para1 as number}`);
}
// 第二个参数类型默认是string，直接使用g()即可
g('hello');

class C {
  public meth(para: T): void {
    console.info(`${para as number}`);
  }
}
// 参数类型默认是number，直接使用new C()即可
new C();
```


## 规则集


```text
plugin:@typescript-eslint/all
```

 Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
