# @typescript-eslint/array-type

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_array-type

定义数组类型时，建议使用相同的样式。比如都使用T[]或者都使用Array&lt;T&gt;。
 

##### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    <span style="color: rgb(135,16,148);">"@typescript-eslint/array-type"</span>: <span style="color: rgb(6,125,23);">"error"</span>
  }
}
```
 
 

##### 选项

详情请参考[typescript/array-type 选项](https://typescript-eslint.nodejs.cn/rules/array-type#options)。
 
 

##### 正例

```text
const x: string[] = ['a', 'b'];
const y: readonly string[] = ['a', 'b'];

export { x, y };
```
 
 

##### 反例

```text
const x: Array<string> = ['a', 'b'];
const y: ReadonlyArray<string> = ['a', 'b'];

export { x, y };
```
 
 

##### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
