# @performance/hp-arkui-use-scale-to-replace-attr-animateto

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-use-scale-to-replace-attr-animateto

建议组件布局改动时使用图形变换属性动画。
 
动效丢帧场景下，建议优先修改。
 

##### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    <span style="color: rgb(135,16,148);">"@performance/hp-arkui-use-scale-to-replace-attr-animateto"</span>: <span style="color: rgb(6,125,23);">"warn"</span>,
  }
}
```
 
 

##### 选项

该规则无需配置额外选项。
 
 

##### 正例

```text
<span style="color: rgb(205,49,49);">@</span><span style="color: rgb(0,128,128);">Entry</span>
<span style="color: rgb(205,49,49);">@</span><span style="color: rgb(0,128,128);">Component</span>
struct <span style="color: rgb(0,128,128);">MyComponent</span> {
  <span style="color: rgb(205,49,49);">@</span><span style="color: rgb(0,128,128);">State</span> textScaleX: number = <span style="color: rgb(9,134,88);">1</span>;
  <span style="color: rgb(205,49,49);">@</span><span style="color: rgb(0,128,128);">State</span> textScaleY: number = <span style="color: rgb(9,134,88);">1</span>;
  build() {
    <span style="color: rgb(0,128,128);">Column</span>() {
      <span style="color: rgb(0,128,128);">Text</span>()
        .backgroundColor(<span style="color: rgb(0,128,128);">Color</span>.<span style="color: rgb(0,128,128);">Blue</span>)
        .fontColor(<span style="color: rgb(0,128,128);">Color</span>.<span style="color: rgb(0,128,128);">White</span>)
        .fontSize(<span style="color: rgb(9,134,88);">20</span>)
        .width(<span style="color: rgb(9,134,88);">10</span>)
        .height(<span style="color: rgb(9,134,88);">10</span>)
        .scale({ x: <span style="color: rgb(0,0,255);">this</span>.textScaleX, y: <span style="color: rgb(0,0,255);">this</span>.textScaleY })
        .margin({ top: <span style="color: rgb(9,134,88);">100</span> })
      <span style="color: rgb(0,128,128);">Button</span>(<span style="color: rgb(163,21,21);">'图形变换属性'</span>)
        .backgroundColor(<span style="color: rgb(0,128,128);">Color</span>.<span style="color: rgb(0,128,128);">Blue</span>)
        .fontColor(<span style="color: rgb(0,128,128);">Color</span>.<span style="color: rgb(0,128,128);">White</span>)
        .fontSize(<span style="color: rgb(9,134,88);">20</span>)
        .margin({ top: <span style="color: rgb(9,134,88);">60</span> })
        .borderRadius(<span style="color: rgb(9,134,88);">30</span>)
        .padding(<span style="color: rgb(9,134,88);">10</span>)
        .onClick(() => {
          animateTo({ duration: <span style="color: rgb(9,134,88);">1000</span> }, () => {
            <span style="color: rgb(0,0,255);">this</span>.textScaleX = <span style="color: rgb(9,134,88);">10</span>;
            <span style="color: rgb(0,0,255);">this</span>.textScaleY = <span style="color: rgb(9,134,88);">10</span>;
          })
        })
    }
 }
}
```
 
 

##### 反例

```text
<span style="color: rgb(205,49,49);">@</span><span style="color: rgb(0,128,128);">Entry</span>
<span style="color: rgb(205,49,49);">@</span><span style="color: rgb(0,128,128);">Component</span>
struct <span style="color: rgb(0,128,128);">MyComponent</span> {
  <span style="color: rgb(205,49,49);">@</span><span style="color: rgb(0,128,128);">State</span> textWidth: number = <span style="color: rgb(9,134,88);">10</span>;
  <span style="color: rgb(205,49,49);">@</span><span style="color: rgb(0,128,128);">State</span> textHeight: number = <span style="color: rgb(9,134,88);">10</span>;
  build() {
    <span style="color: rgb(0,128,128);">Column</span>() {
      <span style="color: rgb(0,128,128);">Text</span>()
        .backgroundColor(<span style="color: rgb(0,128,128);">Color</span>.<span style="color: rgb(0,128,128);">Blue</span>)
        .fontColor(<span style="color: rgb(0,128,128);">Color</span>.<span style="color: rgb(0,128,128);">White</span>)
        .fontSize(<span style="color: rgb(9,134,88);">20</span>)
        .width(<span style="color: rgb(0,0,255);">this</span>.textWidth)
        .height(<span style="color: rgb(0,0,255);">this</span>.textHeight)
      <span style="color: rgb(0,128,128);">Button</span>(<span style="color: rgb(163,21,21);">'布局属性'</span>)
        .backgroundColor(<span style="color: rgb(0,128,128);">Color</span>.<span style="color: rgb(0,128,128);">Blue</span>)
        .fontColor(<span style="color: rgb(0,128,128);">Color</span>.<span style="color: rgb(0,128,128);">White</span>)
        .fontSize(<span style="color: rgb(9,134,88);">20</span>)
        .margin({ top: <span style="color: rgb(9,134,88);">30</span> })
        .borderRadius(<span style="color: rgb(9,134,88);">30</span>)
        .padding(<span style="color: rgb(9,134,88);">10</span>)
        .onClick(() => {
          animateTo({ duration: <span style="color: rgb(9,134,88);">1000</span> }, () => {
            <span style="color: rgb(0,0,255);">this</span>.textWidth = <span style="color: rgb(9,134,88);">100</span>;
            <span style="color: rgb(0,0,255);">this</span>.textHeight = <span style="color: rgb(9,134,88);">100</span>;
          })
        })
    }
 }
}
```
 
 

##### 规则集

```text
<span style="color: rgb(106,135,89);">plugin:@performance/recommended</span>
plugin:@performance/all
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
