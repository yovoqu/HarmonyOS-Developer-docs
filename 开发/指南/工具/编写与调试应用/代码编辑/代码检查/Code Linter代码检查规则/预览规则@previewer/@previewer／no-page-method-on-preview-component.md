# @previewer/no-page-method-on-preview-component

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-page-method-on-preview-component

禁止在非路由组件上实例化onPageShow、onPageHide、onBackPress等页面级方法。
 

#### 规则配置

```json
// code-linter.json5
<span style="color: rgb(65,97,0);">{</span>
<span style="color: rgb(65,97,0);">  "rules": {</span>
<span style="color: rgb(65,97,0);">    "</span><span style="color: rgb(65,97,0);">@previewer/no-page-method-on-preview-component": "warn"</span>
<span style="color: rgb(65,97,0);">  }</span>
<span style="color: rgb(65,97,0);">}</span>
```
 
 

#### 选项

该规则无需配置额外选项。
 
 

#### 正例

```text
<span style="color: rgb(65,97,0);">@</span><span style="color: rgb(65,97,0);">Entry</span>
<span style="color: rgb(65,97,0);">@Component</span>
<span style="color: rgb(65,97,0);">struct Index {</span>
<span style="color: rgb(65,97,0);">  @State message: string = 'Hello World';</span>
<span style="color: rgb(65,97,0);">  onPageShow(): void {}</span>
<span style="color: rgb(65,97,0);">  onPageHide(): void {}</span>
<span style="color: rgb(65,97,0);">  onBackPress(): void {}</span>
<span style="color: rgb(65,97,0);">  build() {</span>
<span style="color: rgb(65,97,0);">    Row() {</span>
<span style="color: rgb(65,97,0);">      Column() {</span>
<span style="color: rgb(65,97,0);">        Text(this.message)</span>
<span style="color: rgb(65,97,0);">      }</span>
<span style="color: rgb(65,97,0);">    }</span>
<span style="color: rgb(65,97,0);">  }</span>
<span style="color: rgb(65,97,0);">}</span>
```
 
 

#### 反例

```text
<span style="color: rgb(212,212,212);">@</span><span style="color: rgb(65,97,0);">Preview</span>
<span style="color: rgb(65,97,0);">@Component</span>
<span style="color: rgb(65,97,0);">struct Index {</span>
<span style="color: rgb(65,97,0);">  @State message: string = 'Hello World';</span>
<span style="color: rgb(65,97,0);">  onPageShow(): void {}</span>
<span style="color: rgb(65,97,0);">  onPageHide(): void {}</span>
<span style="color: rgb(65,97,0);">  onBackPress(): void {}</span>
<span style="color: rgb(65,97,0);">  build() {</span>
<span style="color: rgb(65,97,0);">    Column() {</span>
<span style="color: rgb(65,97,0);">      Text(this.message)</span>
<span style="color: rgb(65,97,0);">    }</span>
<span style="color: rgb(65,97,0);">  }</span>
<span style="color: rgb(65,97,0);">}</span>
```
 
 

#### 规则集

```text
<span style="color: rgb(106,135,89);">plugin:@previewer/recommended</span>
<span style="color: rgb(106,135,89);">plugin:@previewer/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
