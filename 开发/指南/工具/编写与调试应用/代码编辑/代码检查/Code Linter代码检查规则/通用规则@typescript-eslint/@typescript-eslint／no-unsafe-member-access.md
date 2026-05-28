# @typescript-eslint/no-unsafe-member-access

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-member-access

禁止成员访问“any”类型的值。
 
该规则仅支持对.js/.ts文件进行检查。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@typescript-eslint/no-unsafe-member-access": "error"
  }
}
```
 
 

#### 选项

该规则无需配置额外选项。
 
 

#### 正例

```text
declare const properlyTyped: { prop: { a: string } };

export const v1 = properlyTyped.prop.a;

const key = 'a';
export const v2 = properlyTyped.prop[key];

const arr = ['1', '2', '3'];
let idx = 1;
export const v3 = arr[idx];
export const v4 = arr[idx++];
```
 
 

#### 反例

```text
declare const properlyTyped: { prop: { a: any } };

export const v1 = properlyTyped.prop.a;

const key = 'a' as any;
export const v2 = properlyTyped.prop[key];

const arr = ['1', '2', '3'];
let idx: any = 1;
export const v3 = arr[idx];
export const v4 = arr[idx++];
```
 
 

#### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/recommended</span>
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
