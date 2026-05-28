# @typescript-eslint/space-infix-ops

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_space-infix-ops

运算符前后要求有空格。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@typescript-eslint/space-infix-ops": "error"
  }
}
```
 
 

#### 选项

详情请参考[@typescript-eslint/space-infix-ops选项](https://eslint.nodejs.cn/docs/rules/space-infix-ops#选项)。
 
 

#### 正例

```text
declare const a: number;
declare const b: number;
export const c = a + b;
```
 
 

#### 反例

```text
declare const a: number;
declare const b: number;
export const c = a+b;
```
 
 

#### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
