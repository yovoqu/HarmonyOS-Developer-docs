# @typescript-eslint/no-unused-expressions

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unused-expressions

代码中禁止包含未使用的表达式。
 

 

##### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@typescript-eslint/no-unused-expressions": "error"
  }
}
```
 
 

##### 选项

详情请参考[@typescript-eslint/no-unused-expressions选项](https://eslint.nodejs.cn/docs/rules/no-unused-expressions#选项)。
 
 

##### 正例

```text
export const v1 = Number.MAX_VALUE;

if ('hello'.length === v1) {
  console.info('hello');
}

{
  const v2 = '0';
  console.info(v2);
}
```
 
 

##### 反例

```text
Number.MAX_VALUE;

if ('0') '0';

{'0';}
```
 
 

##### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
