# @hw-stylistic/keyword-spacing

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-keyword-spacing-stylistic

在关键字前后强制加空格。该规则仅检查.ets文件类型。


## 规则配置


```text
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/keyword-spacing": "error"
  }
}
```


## 选项

该规则无需配置额外选项。

## 正例


```text
export function test(a: number, b: number) {
  if (a > b) {
    console.info('doSomething');
  } else if (a === b) {
    console.info('doSomething');
  } else {
    console.info('doSomething');
  }

  for (const item of [a, b]) {
    console.info(`${item}`);
  }
}
```


## 反例


```text
export function test(a: number, b: number) {
  // Expected space after 'if'.
  if(a > b) {
    console.info('doSomething');
  // Expected space before 'else'.
  // Expected space after 'if'.
  }else if(a === b) {
    console.info('doSomething');
  // Expected space before 'else'.
  // Expected space after 'else'.
  }else{
    console.info('doSomething');
  }

  // Expected space after 'for'.
  for(const item of [a, b]) {
    console.info(`${item}`);
  }
}
```


## 规则集


```text
"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"
```

 Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
