# @performance/hp-arkui-remove-redundant-nest-container

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-no-redundant-nest

避免冗余的嵌套。
 
通用丢帧场景下，建议优先修改。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    <span style="color: rgb(135,16,148);">"@performance/hp-arkui-remove-redundant-nest-container"</span>: <span style="color: rgb(6,125,23);">"suggestion"</span>,
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
  <span style="color: rgb(205,49,49);">@</span><span style="color: rgb(0,128,128);">State</span> children: <span style="color: rgb(0,128,128);">number</span>[] = <span style="color: rgb(0,128,128);">Array</span>.<span style="color: rgb(0,0,255);">from</span>(<span style="color: rgb(0,128,128);">Array</span><<span style="color: rgb(0,0,255);">number</span>>(<span style="color: rgb(9,134,88);">900</span>), (v, k) => k);  
  
  build() {  
    <span style="color: rgb(0,128,128);">Scroll</span>() {  
      <span style="color: rgb(0,128,128);">Grid</span>() {  
        <span style="color: rgb(0,128,128);">ForEach</span>(<span style="color: rgb(0,0,255);">this</span>.children, (item: <span style="color: rgb(0,128,128);">Number</span>[]) => {  
          <span style="color: rgb(0,128,128);">GridItem</span>() {  
            <span style="color: rgb(0,128,128);">Text</span>(item.toString())  
          }.backgroundColor(<span style="color: rgb(0,128,128);">Color</span>.<span style="color: rgb(0,128,128);">Yellow</span>)  
        }, (item: <span style="color: rgb(0,0,255);">string</span>) => item)  
      }  
      .columnsTemplate(<span style="color: rgb(163,21,21);">'1fr 1fr 1fr 1fr'</span>)  
      .columnsGap(<span style="color: rgb(9,134,88);">0</span>)  
      .rowsGap(<span style="color: rgb(9,134,88);">0</span>)  
      .size({ width: <span style="color: rgb(163,21,21);">"100%"</span>, height: <span style="color: rgb(163,21,21);">"100%"</span> })  
    }  
  }  
}
```
 
 

#### 反例

```text
<span style="color: rgb(205,49,49);">@</span><span style="color: rgb(0,128,128);">Entry</span>
<span style="color: rgb(205,49,49);">@</span><span style="color: rgb(0,128,128);">Component</span>
struct MyComponent {
    <span style="color: rgb(205,49,49);">@</span><span style="color: rgb(0,128,128);">State</span> children: <span style="color: rgb(0,128,128);">number</span>[] = <span style="color: rgb(0,128,128);">Array</span>.<span style="color: rgb(0,0,255);">from</span>(<span style="color: rgb(0,128,128);">Array</span><<span style="color: rgb(0,0,255);">number</span>>(<span style="color: rgb(9,134,88);">900</span>), (v, k) => k);
    
    build() {
      <span style="color: rgb(0,128,128);">Scroll</span>() {
      <span style="color: rgb(0,128,128);">Grid</span>() {
        <span style="color: rgb(0,128,128);">ForEach</span>(<span style="color: rgb(0,0,255);">this</span>.children, (item: <span style="color: rgb(0,128,128);">Number</span>[]) => {
          <span style="color: rgb(0,128,128);">GridItem</span>() {
            <span style="color: rgb(0,128,0);">// 冗余Stack</span>
            <span style="color: rgb(0,128,128);">Stack</span>() {  
              <span style="color: rgb(0,128,128);">Stack</span>() {  
                <span style="color: rgb(0,128,128);">Stack</span>() {  
                  <span style="color: rgb(0,128,128);">Text</span>(item.toString())  
                }.size({ width: <span style="color: rgb(163,21,21);">"100%"</span>})  
              }.backgroundColor(<span style="color: rgb(0,128,128);">Color</span>.<span style="color: rgb(0,128,128);">Yellow</span>)  
            }.backgroundColor(<span style="color: rgb(0,128,128);">Color</span>.<span style="color: rgb(0,128,128);">Pink</span>)  
          }  
        }, (item: <span style="color: rgb(0,0,255);">string</span>) => item)  
      }  
      .columnsTemplate(<span style="color: rgb(163,21,21);">'1fr 1fr 1fr 1fr'</span>)  
      .columnsGap(<span style="color: rgb(9,134,88);">0</span>)  
      .rowsGap(<span style="color: rgb(9,134,88);">0</span>)  
      .size({ width: <span style="color: rgb(163,21,21);">"100%"</span>, height: <span style="color: rgb(163,21,21);">"100%"</span> })  
    }  
  }  
}
```
 
 

#### 规则集

```text
<span style="color: rgb(106,135,89);">plugin:@performance/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
