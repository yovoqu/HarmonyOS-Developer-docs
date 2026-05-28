# @typescript-eslint/no-unnecessary-type-assertion

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unnecessary-type-assertion

禁止不必要的类型断言。
 
如果类型断言没有更改表达式的类型，也就没有必要使用。
 

##### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@typescript-eslint/no-unnecessary-type-assertion": "error"
  }
}
```
 
 

##### 选项

详情请参考[@typescript-eslint/no-unnecessary-type-assertion选项](https://typescript-eslint.nodejs.cn/rules/no-unnecessary-type-assertion/#options)。
 
 

##### 正例

```text
const num = 3;
export const foo2 = num as number;
export const foo3 = 'foo' as string;
```
 
 

##### 反例

```text
const num = 3;
export const foo = num;
export const bar = foo!;
```
 
 

##### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
