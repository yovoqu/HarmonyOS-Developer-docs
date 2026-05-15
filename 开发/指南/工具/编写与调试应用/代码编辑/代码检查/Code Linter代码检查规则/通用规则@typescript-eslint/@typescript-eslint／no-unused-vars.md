# @typescript-eslint/no-unused-vars

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unused-vars

禁止定义未使用的变量。


## 规则配置


```text
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-unused-vars": "error"
  }
}
```


## 选项

详情请参考[@typescript-eslint/no-unused-vars选项](https://eslint.nodejs.cn/docs/rules/no-unused-vars#选项)。

## 正例


```text
const x = 10;
console.info(`${x}`);

((foo) => {
  return foo;
})();

const num = 50;
let myFunc1: () => number = () => num;
myFunc1 = () => setTimeout(() => {
  // myFunc is considered used
  myFunc1();
}, num);
```


## 反例


```text
const x = 10;

((foo) => {
  return 'hello';
})();

const num = 50;
const myFunc1: () => number = () => num;
```


## 规则集


```text
plugin:@typescript-eslint/all
```

 Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
