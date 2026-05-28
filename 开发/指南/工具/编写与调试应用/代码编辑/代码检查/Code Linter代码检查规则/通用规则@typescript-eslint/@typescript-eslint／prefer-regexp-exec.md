# @typescript-eslint/prefer-regexp-exec

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-regexp-exec

如果未提供全局标志（/g），推荐使用“RegExp#exec”，而不是“String#match”。
 

##### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@typescript-eslint/prefer-regexp-exec": "error"
  }
}
```
 
 

##### 选项

该规则无需配置额外选项。
 
 

##### 正例

```text
<span style="color: rgb(101,49,112);">/thing/</span><span style="color: rgb(133,152,1);">.</span><span style="color: rgb(0,169,158);">exec</span><span style="color: rgb(108,113,196);">(</span><span style="color: rgb(101,49,112);">'something'</span><span style="color: rgb(108,113,196);">)</span><span style="color: rgb(133,152,1);">;</span>

<span style="color: rgb(101,49,112);">'some things are just things'</span><span style="color: rgb(133,152,1);">.</span><span style="color: rgb(0,169,158);">match</span><span style="color: rgb(108,113,196);">(</span><span style="color: rgb(101,49,112);">/thing/g</span><span style="color: rgb(108,113,196);">)</span><span style="color: rgb(133,152,1);">;</span>

const <span style="color: rgb(17,64,142);">text </span><span style="color: rgb(133,152,1);">= </span><span style="color: rgb(101,49,112);">'something'</span><span style="color: rgb(133,152,1);">;</span>
const <span style="color: rgb(17,64,142);">search </span><span style="color: rgb(133,152,1);">= </span><span style="color: rgb(101,49,112);">/thing/</span><span style="color: rgb(133,152,1);">;</span>
<span style="color: rgb(17,64,142);">search</span><span style="color: rgb(133,152,1);">.</span><span style="color: rgb(0,169,158);">exec</span><span style="color: rgb(108,113,196);">(</span><span style="color: rgb(17,64,142);">text</span><span style="color: rgb(108,113,196);">)</span><span style="color: rgb(133,152,1);">;</span>
```
 
 

##### 反例

```text
<span style="color: rgb(101,49,112);">'something'</span><span style="color: rgb(133,152,1);">.</span><span style="color: rgb(0,169,158);">match</span><span style="color: rgb(108,113,196);">(</span><span style="color: rgb(101,49,112);">/thing/</span><span style="color: rgb(108,113,196);">)</span><span style="color: rgb(133,152,1);">;</span>

<span style="color: rgb(101,49,112);">'some things are just things'</span><span style="color: rgb(133,152,1);">.</span><span style="color: rgb(0,169,158);">match</span><span style="color: rgb(108,113,196);">(</span><span style="color: rgb(101,49,112);">/thing/</span><span style="color: rgb(108,113,196);">)</span><span style="color: rgb(133,152,1);">;</span>

const <span style="color: rgb(17,64,142);">text </span><span style="color: rgb(133,152,1);">= </span><span style="color: rgb(101,49,112);">'something'</span><span style="color: rgb(133,152,1);">;</span>
const <span style="color: rgb(17,64,142);">search </span><span style="color: rgb(133,152,1);">= </span><span style="color: rgb(101,49,112);">/thing/</span><span style="color: rgb(133,152,1);">;</span>
<span style="color: rgb(17,64,142);">text</span><span style="color: rgb(133,152,1);">.</span><span style="color: rgb(0,169,158);">match</span><span style="color: rgb(108,113,196);">(</span><span style="color: rgb(17,64,142);">search</span><span style="color: rgb(108,113,196);">)</span><span style="color: rgb(133,152,1);">;</span>
```
 
 

##### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
