# @typescript-eslint/require-array-sort-compare

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_require-array-sort-compare

要求调用“Array#sort”时，始终提供“compareFunction”。
 

##### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@typescript-eslint/require-array-sort-compare": "error"
  }
}
```
 
 

##### 选项

详情请参考[@typescript-eslint/require-array-sort-compare选项](https://typescript-eslint.nodejs.cn/rules/require-array-sort-compare/#options)。
 
 

##### 正例

```text
declare const array: string[];

array.sort((a, b) => a.length - b.length);
array.sort((a, b) => a.localeCompare(b));
```
 
 

##### 反例

```text
declare const array: number[];
declare const stringArray: object[];

array.sort();

// String arrays should be sorted using `String#localeCompare`.
stringArray.sort();
```
 
 

##### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
