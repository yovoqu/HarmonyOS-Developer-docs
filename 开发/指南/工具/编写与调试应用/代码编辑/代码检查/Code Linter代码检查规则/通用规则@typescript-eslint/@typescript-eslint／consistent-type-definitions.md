# @typescript-eslint/consistent-type-definitions

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_consistent-type-definitions

强制使用一致的类型声明样式，仅使用“interface”或者仅使用“type”。
 
该规则仅支持对.js/.ts文件进行检查。
 

##### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@typescript-eslint/consistent-type-definitions": "error"
  }
}
```
 
 

##### 选项

详情请参考[@typescript-eslint/consistent-type-definitions选项](https://typescript-eslint.nodejs.cn/rules/consistent-type-definitions/#options)。
 
 

##### 正例

```text
// 基本类型的定义可以使用type
export type T1 = string;

// 默认推荐使用interface 进行对象类型定义
export interface T2 {
  x: number;
}

export type Foo = string | T2;
```
 
 

##### 反例

```text
// 默认推荐使用interface 进行对象类型定义
type T = { x: number };
```
 
 

##### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
