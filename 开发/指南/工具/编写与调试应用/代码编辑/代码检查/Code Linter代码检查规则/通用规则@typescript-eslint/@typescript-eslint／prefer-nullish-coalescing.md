# @typescript-eslint/prefer-nullish-coalescing

更新时间：2026-04-20 06:32:02

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-nullish-coalescing

强制使用空值合并运算符（??）而不是逻辑运算符。
 

##### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@typescript-eslint/prefer-nullish-coalescing": "error"
  }
}
```
 
 

##### 选项

详情请参考[@typescript-eslint/prefer-nullish-coalescing选项](https://typescript-eslint.nodejs.cn/rules/prefer-nullish-coalescing/#options)。
 
 

##### 正例

```text
function getText1(): string | undefined {
  return 'bar';
}

function getText2(): string | null {
  return 'bar';
}

const foo1: string | undefined = getText1();
export const v1 = foo1 ?? 'a string';

const foo2: string | null = getText2();
export const v2 = foo2 ?? 'a string';
```
 
 

##### 反例

```text
declare const a: string | null;
declare const b: string | null;

export const c = a || b;
```
 
 

##### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
