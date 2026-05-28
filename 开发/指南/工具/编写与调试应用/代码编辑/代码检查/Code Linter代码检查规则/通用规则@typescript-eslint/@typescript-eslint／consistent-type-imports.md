# @typescript-eslint/consistent-type-imports

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_consistent-type-imports

强制使用一致的类型导入风格。
 
该规则仅支持对.js/.ts文件进行检查。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@typescript-eslint/consistent-type-imports": "error"
  }
}
```
 
 

#### 选项

详情请参考[@typescript-eslint/consistent-type-imports选项](https://typescript-eslint.nodejs.cn/rules/consistent-type-imports/#options)。
 
 

#### 正例

```text
// 默认推荐使用import type Foo from '...'
import type { Foo } from 'Foo';
import type Bar from 'Bar';
export type T = Foo;
export const x: Bar = 1;
```
 
 

#### 反例

```text
// 默认推荐使用import type Foo from '...'
import { Foo } from 'Foo';
import Bar from 'Bar';
export type T = Foo;
export const x: Bar = 1;
```
 
 

#### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/recommended</span>
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
