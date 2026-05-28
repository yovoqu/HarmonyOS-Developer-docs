# @typescript-eslint/no-magic-numbers

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-magic-numbers

禁止使用魔法数字。
 
“魔法数字”是在代码中多次出现但没有明确含义的数字，最好将它们替换为常量。
 

##### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@typescript-eslint/no-magic-numbers": "warn"
  }
}
```
 
 

##### 选项

详情请参考[@typescript-eslint/no-magic-numbers选项](https://typescript-eslint.nodejs.cn/rules/no-magic-numbers#选项)。
 
 

##### 正例

```text
const TAX = 0.25;
const dutyFreePrice = 100;
export const finalPrice = dutyFreePrice + dutyFreePrice * TAX;
```
 
 

##### 反例

```text
export const finalPrice = 100 + 100 * 0.25;

const data = ['foo', 'bar', 'baz'];
export const dataLast = data[2];
```
 
 

##### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
