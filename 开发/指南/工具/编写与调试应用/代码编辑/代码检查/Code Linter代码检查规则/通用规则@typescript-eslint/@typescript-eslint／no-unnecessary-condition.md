# @typescript-eslint/no-unnecessary-condition

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unnecessary-condition

不允许使用类型始终为真或始终为假的表达式作为判断条件。
 

 

##### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@typescript-eslint/no-unnecessary-condition": "error"
  }
}
```
 
 

##### 选项

详情请参考[@typescript-eslint/no-unnecessary-condition选项](https://typescript-eslint.nodejs.cn/rules/no-unnecessary-condition/#options)。
 
 

##### 正例

```text
const index = 0;
export function head(items: readonly string[]): string {
  // Necessary, since items.length might be 0
  if (items.length) {
    return items[index].toUpperCase();
  } else {
    return '';
  }
}

export function foo(arg: string): void {
  // Necessary, since foo might be ''.
  if (arg) {
  }
}

export function bar(arg?: string | null) {
  // Necessary, since arg might be nullish
  return arg?.length;
}
```
 
 

##### 反例

```text
const index = 0;
export function head(items: readonly string[]) {
  // items can never be nullable, so this is unnecessary
  if (items) {
    return items[index].toUpperCase();
  } else {
    return '';
  }
}

export function foo(arg: 'bar' | 'baz') {
  // arg is never nullable or empty string, so this is unnecessary
  if (arg) {
  }
}

export function bar(arg: string) {
  // arg can never be nullish, so ?. is unnecessary
  return arg?.length;
}
```
 
 

##### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
