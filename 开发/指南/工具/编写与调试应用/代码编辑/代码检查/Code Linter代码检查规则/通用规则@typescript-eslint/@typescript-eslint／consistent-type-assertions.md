# @typescript-eslint/consistent-type-assertions

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_consistent-type-assertions

强制使用一致的类型断言。


## 规则配置


```text
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/consistent-type-assertions": "error"
  }
}
```


## 选项

详情请参考[@typescript-eslint/consistent-type-assertions选项](https://typescript-eslint.nodejs.cn/rules/consistent-type-assertions/#options)。

## 正例


```text
interface MyType {
  name: string;
}
export const x: MyType = {
  name: 'hello'
};
// 默认推荐使用 value as Type：始终优先选择const x = value as Type; 而不是const x = value;
export const y = x as object;
```


## 反例


```text
interface MyType {
  name: string;
}
export const x: MyType = {
  name: 'hello'
};
// 默认推荐使用 value as Type：始终优先选择const x = value as Type; 而不是const x = value;
export const y = x;
```


## 规则集


```text
plugin:@typescript-eslint/all
```

 Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
