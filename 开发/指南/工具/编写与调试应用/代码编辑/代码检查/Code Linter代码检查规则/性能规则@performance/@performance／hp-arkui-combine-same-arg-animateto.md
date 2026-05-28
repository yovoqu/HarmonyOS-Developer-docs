# @performance/hp-arkui-combine-same-arg-animateto

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-combine-same-arg-animateto

建议动画参数相同时使用同一个animateTo。
 
动效丢帧场景下，建议优先修改。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    <span style="color: rgb(135,16,148);">"@performance/hp-arkui-combine-same-arg-animateto"</span>: <span style="color: rgb(6,125,23);">"warn"</span>,
  }
}
```
 
 

#### 选项

该规则无需配置额外选项。
 
 

#### 正例

```text
<span style="color: rgb(205,49,49);">@</span><span style="color: rgb(0,128,128);">Entry</span>
<span style="color: rgb(205,49,49);">@</span><span style="color: rgb(0,128,128);">Component</span>
struct <span style="color: rgb(0,128,128);">MyComponent</span> {
  <span style="color: rgb(205,49,49);">@</span><span style="color: rgb(0,128,128);">State</span> textWidth: <span style="color: rgb(0,0,255);">number</span> = <span style="color: rgb(9,134,88);">200</span>;
  <span style="color: rgb(205,49,49);">@</span><span style="color: rgb(0,128,128);">State</span> color: <span style="color: rgb(0,128,128);">Color</span> = <span style="color: rgb(0,128,128);">Color</span>.<span style="color: rgb(0,128,128);">Red</span>;
  
  func() {
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">animateTo</span>({ curve: <span style="color: rgb(0,128,128);">Curve</span>.<span style="color: rgb(0,128,128);">Sharp</span>, duration: <span style="color: rgb(9,134,88);">1000</span> }, () => {
      <span style="color: rgb(0,0,255);">this</span>.textWidth = (<span style="color: rgb(0,0,255);">this</span>.textWidth === <span style="color: rgb(9,134,88);">100</span> ? <span style="color: rgb(9,134,88);">200</span> : <span style="color: rgb(9,134,88);">100</span>);
      <span style="color: rgb(0,0,255);">this</span>.color = (<span style="color: rgb(0,0,255);">this</span>.color === <span style="color: rgb(0,128,128);">Color</span>.<span style="color: rgb(0,128,128);">Yellow</span> ? <span style="color: rgb(0,128,128);">Color</span>.<span style="color: rgb(0,128,128);">Red</span> : <span style="color: rgb(0,128,128);">Color</span>.<span style="color: rgb(0,128,128);">Yellow</span>);
    });
  }
  
  build() {
    <span style="color: rgb(0,128,128);">Column</span>() {
      <span style="color: rgb(0,128,128);">Row</span>()
        .width(<span style="color: rgb(0,0,255);">this</span>.textWidth)
        .height(<span style="color: rgb(9,134,88);">10</span>)
        .backgroundColor(<span style="color: rgb(0,0,255);">this</span>.color)
      <span style="color: rgb(0,128,128);">Text</span>(<span style="color: rgb(163,21,21);">'click'</span>)
        .onClick(() => {
          <span style="color: rgb(0,0,255);">this</span>.func();
        })
    }
    .width(<span style="color: rgb(163,21,21);">'100%'</span>)
    .height(<span style="color: rgb(163,21,21);">'100%'</span>)
  }
}
```
 
 

#### 反例

```text
<span style="color: rgb(205,49,49);">@</span><span style="color: rgb(0,128,128);">Entry</span>
<span style="color: rgb(205,49,49);">@</span><span style="color: rgb(0,128,128);">Component</span>
struct <span style="color: rgb(0,128,128);">MyComponent</span> {
  <span style="color: rgb(205,49,49);">@</span><span style="color: rgb(0,128,128);">State</span> textWidth: <span style="color: rgb(0,0,255);">number</span> = <span style="color: rgb(9,134,88);">200</span>;
  <span style="color: rgb(205,49,49);">@</span><span style="color: rgb(0,128,128);">State</span> color: <span style="color: rgb(0,128,128);">Color</span> = <span style="color: rgb(0,128,128);">Color</span>.<span style="color: rgb(0,128,128);">Red</span>;
  
  func1() {
    animateTo({ curve: <span style="color: rgb(0,128,128);">Curve</span>.<span style="color: rgb(0,128,128);">Sharp</span>, duration: <span style="color: rgb(9,134,88);">1000</span> }, () => {
      <span style="color: rgb(0,0,255);">this</span>.textWidth = (<span style="color: rgb(0,0,255);">this</span>.textWidth === <span style="color: rgb(9,134,88);">100</span> ? <span style="color: rgb(9,134,88);">200</span> : <span style="color: rgb(9,134,88);">100</span>);
    });
  }
  
  func2() {
    animateTo({ curve: <span style="color: rgb(0,128,128);">Curve</span>.<span style="color: rgb(0,128,128);">Sharp</span>, duration: <span style="color: rgb(9,134,88);">1000</span> }, () => {
      <span style="color: rgb(0,0,255);">this</span>.color = (<span style="color: rgb(0,0,255);">this</span>.color === <span style="color: rgb(0,128,128);">Color</span>.<span style="color: rgb(0,128,128);">Yellow</span> ? <span style="color: rgb(0,128,128);">Color</span>.<span style="color: rgb(0,128,128);">Red</span> : <span style="color: rgb(0,128,128);">Color</span>.<span style="color: rgb(0,128,128);">Yellow</span>);
    });
  }
  
  build() {
    <span style="color: rgb(0,128,128);">Column</span>() {
      <span style="color: rgb(0,128,128);">Row</span>()
        .width(<span style="color: rgb(0,0,255);">this</span>.textWidth)
        .height(<span style="color: rgb(9,134,88);">10</span>)
        .backgroundColor(<span style="color: rgb(0,0,255);">this</span>.color)
      <span style="color: rgb(0,128,128);">Text</span>(<span style="color: rgb(163,21,21);">'click'</span>)
        .onClick(() => {
          <span style="color: rgb(0,0,255);">this</span>.func1();
          <span style="color: rgb(0,0,255);">this</span>.func2();
        })
    }
    .width(<span style="color: rgb(163,21,21);">'100%'</span>)
    .height(<span style="color: rgb(163,21,21);">'100%'</span>)
  }
}
```
 
 

#### 规则集

```text
<span style="color: rgb(106,135,89);">plugin:@performance/recommended</span>
plugin:@performance/all
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
