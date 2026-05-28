# @previewer/no-unallowed-decorator-on-root-component

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unallowed-decorator-on-root-component

不允许直接预览包含@Consume、@Link、@ObjectLink、@Prop等装饰器的子组件；
 
建议使用一个定义了完整的、合法的、不依赖运行时的默认值的父组件，并预览此父组件来查看子组件的预览效果。
 

##### 规则配置

```json
// code-linter.json5
<span style="color: rgb(65,97,0);">{</span>
<span style="color: rgb(65,97,0);">  "rules": {</span>
<span style="color: rgb(65,97,0);">    "</span><span style="color: rgb(65,97,0);">@previewer/no-unallowed-decorator-on-root-component": "warn"</span>
<span style="color: rgb(65,97,0);">  }</span>
<span style="color: rgb(65,97,0);">}</span>
```
 
 

##### 选项

该规则无需配置额外选项。
 
 

##### 正例

```text
<span style="color: rgb(65,97,0);">@</span><span style="color: rgb(65,97,0);">Entry</span>
<span style="color: rgb(65,97,0);">@Component</span>
<span style="color: rgb(65,97,0);">struct LinkSampleContainer {</span>
<span style="color: rgb(65,97,0);">  @State message: string = 'Hello World';</span>
<span style="color: rgb(65,97,0);">  build() {</span>
<span style="color: rgb(65,97,0);">    Row() {</span>
<span style="color: rgb(65,97,0);">      LinkSample({message: this.message})</span>
<span style="color: rgb(65,97,0);">    }</span>
<span style="color: rgb(65,97,0);">  }</span>
<span style="color: rgb(65,97,0);">}</span>
<span style="color: rgb(65,97,0);">@Component</span>
<span style="color: rgb(65,97,0);">struct LinkSample {</span>
<span style="color: rgb(65,97,0);">  @Link message: string;</span>
<span style="color: rgb(65,97,0);">  build() {</span>
<span style="color: rgb(65,97,0);">    Row() {</span>
<span style="color: rgb(65,97,0);">      Text(this.message)</span>
<span style="color: rgb(65,97,0);">    }</span>
<span style="color: rgb(65,97,0);">  }</span>
<span style="color: rgb(65,97,0);">}</span>
```
 
 

##### 反例

```text
<span style="color: rgb(65,97,0);">@</span><span style="color: rgb(65,97,0);">Preview</span>
<span style="color: rgb(65,97,0);">@Component</span>
<span style="color: rgb(65,97,0);">struct LinkSample {</span>
<span style="color: rgb(65,97,0);">  @Link message: string;</span>
<span style="color: rgb(65,97,0);">  build() {</span>
<span style="color: rgb(65,97,0);">    Row() {</span>
<span style="color: rgb(65,97,0);">      Text(this.message)</span>
<span style="color: rgb(65,97,0);">    }</span>
<span style="color: rgb(65,97,0);">  }</span>
<span style="color: rgb(65,97,0);">}</span>
```
 
 

##### 规则集

```text
<span style="color: rgb(106,135,89);">plugin:@previewer/recommended</span>
<span style="color: rgb(106,135,89);">plugin:@previewer/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
