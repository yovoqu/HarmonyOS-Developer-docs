# @typescript-eslint/no-type-alias

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-type-alias

禁止使用类型别名。
 
该规则仅支持对.js/.ts文件进行检查。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@typescript-eslint/no-type-alias": "error"
  }
}
```
 
 

#### 选项

详情请参考[@typescript-eslint/no-type-alias选项](https://typescript-eslint.nodejs.cn/rules/no-type-alias/#options)。
 
 

#### 正例

```text
interface Person {
  readonly firstName: string;
  readonly lastName: string;
  readonly age: number;
}

export function addPerson(person: Person): Person {
  return person;
}
```
 
 

#### 反例

```text
// 不允许使用类型别名，建议使用接口替代
type Person = {
  readonly firstName: string;
  readonly lastName: string;
  readonly age: number;
};

export function addPerson(person: Person): Person {
  return person;
}
```
 
 

#### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
