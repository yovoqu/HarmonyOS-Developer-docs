# @typescript-eslint/no-confusing-non-null-assertion

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-confusing-non-null-assertion

不允许在可能产生混淆的位置使用非空断言。
 
在赋值或者等于旁边使用非空断言（!）会产生混淆，看起来类似于不等于，不建议这种写法。
 

##### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@typescript-eslint/no-confusing-non-null-assertion": "error"
  }
}
```
 
 

##### 选项

该规则无需配置额外选项。
 
 

##### 正例

```text
interface Foo {
  bar?: string;
  num?: number;
}

function getFoo(): Foo {
  return {
    bar: 'bar',
    num: Number.MAX_VALUE
  };
}
const foo: Foo = getFoo();
export const isEqualsBar = foo.bar === 'hello';
const num = 2;
export const isEqualsNum = num + (foo.num!) === num;
```
 
 

##### 反例

```text
interface Foo {
  bar?: string;
  num?: number;
}

function getFoo(): Foo {
  return {
    bar: 'bar',
    num: Number.MAX_VALUE
  };
}
const foo: Foo = getFoo();
// 可能会产生混淆，误以为是不等于
export const isEqualsBar = foo.bar! === 'hello';
// 可能会产生混淆，误以为是不等于
const num = 2;
export const isEqualsNum = num + foo.num! === num;
```
 
 

##### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
