# @typescript-eslint/prefer-reduce-type-parameter

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-reduce-type-parameter

调用“Array#reduce”时推荐使用类型参数而不是类型断言。
 

 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@typescript-eslint/prefer-reduce-type-parameter": "error"
  }
}
```
 
 

#### 选项

该规则无需配置额外选项。
 
 

#### 正例

```text
['1', '2', '3'].reduce<readonly string[]>((arr, text) => {
  const newArr = [...arr];
  newArr.push(text);
  return newArr;
}, []);
```
 
 

#### 反例

```text
['1', '2', '3'].reduce((arr, text) => {
  const newArr = [...arr];
  newArr.push(text);
  return newArr;
}, [] as readonly string[]);
```
 
 

#### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
