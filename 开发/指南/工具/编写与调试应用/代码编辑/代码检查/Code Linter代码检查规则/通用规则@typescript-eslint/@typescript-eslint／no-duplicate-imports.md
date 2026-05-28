# @typescript-eslint/no-duplicate-imports

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-duplicate-imports

禁止重复的模块导入。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@typescript-eslint/no-duplicate-imports": "error"
  }
}
```
 
 

#### 选项

详情请参考[eslint/no-duplicate-imports选项](https://eslint.nodejs.cn/docs/latest/rules/no-duplicate-imports#选项)。
 
 

#### 正例

```text
// foo和bar代表两个文件
import { foo } from './foo';
import bar from './bar';
```
 
 

#### 反例

```text
// foo代表文件
import { foo } from './foo';
import { bar } from './foo';
```
 
 

#### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
