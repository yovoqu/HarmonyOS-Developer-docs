# @typescript-eslint/no-loop-func

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-loop-func

禁止在循环语句内包含不安全引用的函数声明。

 该规则仅支持对.js/.ts文件进行检查。


## 规则配置


```text
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-loop-func": "error"
  }
}
```


## 选项

该规则无需配置额外选项。

## 正例


```text
const a = function(): void {
  console.info('hello');
};

for (let i = 10; i; i--) {
  a();
}

for (let i = 10; i; i--) {
  const b = function(): void {
    a();
  }; // OK, no references to variables in the outer scopes.
  b();
}
```


## 反例


```text
const num = 10;
for (let i = num; i; i--) {
  // 变量i是不安全的引用
  (function(): number {
    return i;
  })();
}

let i1 = 0;
while (i1

## 规则集


```text
plugin:@typescript-eslint/all
```

 Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
