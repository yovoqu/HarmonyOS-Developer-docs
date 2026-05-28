# @typescript-eslint/restrict-template-expressions

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_restrict-template-expressions

要求模板表达式中的变量为“string”类型。
 

##### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@typescript-eslint/restrict-template-expressions": "error"
  }
}
```
 
 

##### 选项

详情请参考[@typescript-eslint/restrict-template-expressions选项](https://typescript-eslint.nodejs.cn/rules/restrict-template-expressions/#options)。
 
 

##### 正例

```text
const arg: string | undefined = 'foo';
export const msg1 = `arg = ${arg}`;
export const msg2 = `arg = ${arg || 'default'}`;
```
 
 

##### 反例

```text
const arg1 = ['1', '2'];
export const msg1 = `arg1 = ${arg1}`;

interface GeneratedObjectLiteralInterface {
  name: string;
}

const arg2: GeneratedObjectLiteralInterface = { name: 'Foo' };
export const msg2 = `arg2 = ${arg2 || null}`;
```
 
 

##### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
