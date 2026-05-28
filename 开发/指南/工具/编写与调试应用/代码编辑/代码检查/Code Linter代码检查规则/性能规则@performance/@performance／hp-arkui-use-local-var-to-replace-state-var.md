# @performance/hp-arkui-use-local-var-to-replace-state-var

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-use-local-var-to-replace-state-var

建议使用临时变量替换状态变量。
 
通用丢帧场景下，建议优先修改。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    <span style="color: rgb(135,16,148);">"@performance/hp-arkui-use-local-var-to-replace-state-var"</span>: <span style="color: rgb(6,125,23);">"warn"</span>,
  }
}
```
 
 

#### 选项

该规则无需配置额外选项。
 
 

#### 正例

```text
<span style="color: rgb(205,49,49);">@</span><span style="color: rgb(0,128,128);">Entry</span>
<span style="color: rgb(205,49,49);">@</span><span style="color: rgb(0,128,128);">Component</span>
struct MyComponent {
  <span style="color: rgb(205,49,49);">@</span><span style="color: rgb(0,128,128);">State</span> message: string = <span style="color: rgb(163,21,21);">''</span>;
  appendMsg(newMsg: string) {
      <span style="color: rgb(0,0,255);">let</span> message = <span style="color: rgb(0,0,255);">this</span>.message;
      message += newMsg;
      message += <span style="color: rgb(163,21,21);">";"</span>;
      message += <span style="color: rgb(163,21,21);">"</span><span style="color: rgb(163,21,21);"><</span><span style="color: rgb(163,21,21);">br/</span><span style="color: rgb(163,21,21);">></span><span style="color: rgb(163,21,21);">"</span>;
      <span style="color: rgb(0,0,255);">this</span>.message = message;
  }
  build() {
    <span style="color: rgb(0,128,0);">// 业务代码...</span>
  }
}
```
 
 

#### 反例

```text
<span style="color: rgb(205,49,49);">@</span><span style="color: rgb(0,128,128);">Entry</span>
<span style="color: rgb(205,49,49);">@</span><span style="color: rgb(0,128,128);">Component</span>
struct MyComponent {
  <span style="color: rgb(205,49,49);">@</span><span style="color: rgb(0,128,128);">State</span> message: string = <span style="color: rgb(163,21,21);">''</span>;
  appendMsg(newMsg: string) {
      <span style="color: rgb(0,0,255);">this</span>.message += newMsg;
      <span style="color: rgb(0,0,255);">this</span>.message += <span style="color: rgb(163,21,21);">";"</span>;
      <span style="color: rgb(0,0,255);">this</span>.message += <span style="color: rgb(163,21,21);">"</span><span style="color: rgb(163,21,21);"><</span><span style="color: rgb(163,21,21);">br/</span><span style="color: rgb(163,21,21);">></span><span style="color: rgb(163,21,21);">"</span>;
  }
  build() {
    <span style="color: rgb(0,128,0);">// 业务代码...</span>
  }
}
```
 
 

#### 规则集

```text
<span style="color: rgb(106,135,89);">plugin:@performance/recommended</span>
plugin:@performance/all
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
