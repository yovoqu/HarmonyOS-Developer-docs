# @hw-stylistic/curly

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_curly

条件语句和循环语句的逻辑代码必须写在大括号中。该规则仅检查.ets文件类型。
 

##### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@hw-stylistic/curly": "error"
  }
}
```
 
 

##### 选项

该规则无需配置额外选项。
 
 

##### 正例

```text
export function test(a: number, b: number) {
  if (a > b) {
    console.info('doSomething');
  } else if (a === b) {
    console.info('doSomething');
  } else {
    console.info('doSomething');
  }

  while (a > b) {
    a--;
    console.info('doSomething');
  }

  console.info('doSomething');
}
```
 
 

##### 反例

```text
export function test(a: number, b: number) {
  if (a > b)
  // Expected { after 'if' condition.
    console.info('doSomething');
  else if (a === b)
  // Expected { after 'if' condition.
    console.info('doSomething');
  else
  // Expected { after 'else'.
    console.info('doSomething');
  console.info('doSomething');
}
```
 
 

##### 规则集

```text
<span style="color: rgb(6,125,23);">"plugin:@hw-stylistic/recommended"</span>
<span style="color: rgb(6,125,23);">"plugin:@hw-stylistic/all"</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
