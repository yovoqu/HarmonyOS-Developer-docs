# @typescript-eslint/comma-spacing

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_comma-spacing

强制逗号前后的空格风格保持一致。
 

##### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@typescript-eslint/comma-spacing": "error"
  }
}
```
 
 

##### 选项

详情请参考[@typescript-eslint/comma-spacing选项](https://eslint.nodejs.cn/docs/rules/comma-spacing#选项)。
 
 

##### 正例

```text
// 默认不允许逗号前有空格，逗号后需要一个或多个空格
export const arr1 = ['1', '2'];
export const arr2 = ['1',, '3'];

function qur(a: string, b: string) {
  return `${a}${b}`;
}
qur('1', '2');
```
 
 

##### 反例

```text
// 默认不允许逗号前有空格，逗号后需要一个或多个空格
export const arr = ['1' , '2'];

function qur(a: string ,b: string) {
  return `${a}${b}`;
}
qur('1' ,'2');
```
 
 

##### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
