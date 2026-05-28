# @typescript-eslint/no-array-constructor

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-array-constructor

不允许使用“Array”构造函数。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@typescript-eslint/no-array-constructor": "error"
  }
}
```
 
 

#### 选项

该规则无需配置额外选项。
 
 

#### 正例

```text
const length = 500;
Array(length);

export const newArr: number[] = new Array(['1'].length);

export const arr = ['0', '1', '2'];

export const createArray = (array: string) => new Array(array.length);
```
 
 

#### 反例

```text
Array();

Array('0', '1', '2');

new Array('0', '1', '2');
```
 
 

#### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
