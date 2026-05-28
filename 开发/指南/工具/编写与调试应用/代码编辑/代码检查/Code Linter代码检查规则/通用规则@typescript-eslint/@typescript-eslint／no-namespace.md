# @typescript-eslint/no-namespace

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-namespace

禁止使用 TypeScript语法中的命名空间。
 
命名空间是一种过时的语法，推荐使用import/export。
 
该规则仅支持对.js/.ts文件进行检查。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@typescript-eslint/no-namespace": "error"
  }
}
```
 
 

#### 选项

详情请参考[@typescript-eslint/no-namespace选项](https://typescript-eslint.nodejs.cn/rules/no-namespace/#options)。
 
 

#### 正例

```text
// foo为模块名
declare module 'foo' {}
// anything inside a d.ts file
```
 
 

#### 反例

```text
module foo {}
namespace foo {}

declare module foo {}
declare namespace foo {}
```
 
 

#### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
