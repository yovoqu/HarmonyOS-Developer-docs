# @performance/hp-arkui-limit-refresh-scope（已下线）

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-limit-refresh-scope

建议减少组件刷新范围。该规则已于5.0.3.500版本下线。
 

##### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    <span style="color: rgb(135,16,148);">"@performance/hp-arkui-limit-refresh-scope"</span>: <span style="color: rgb(6,125,23);">"suggestion"</span>,
  }
}
```
 
 

##### 选项

该规则无需配置额外选项。
 
 

##### 正例

```text
<span style="color: rgb(78,201,176);">@Entry</span>
<span style="color: rgb(78,201,176);">@Component</span>
struct <span style="color: rgb(78,201,176);">StackExample6</span> {
  <span style="color: rgb(78,201,176);">@State</span> isVisible : <span style="color: rgb(78,201,176);">boolean</span> <span style="color: rgb(212,212,212);">=</span> <span style="color: rgb(86,156,214);">false</span>;
  build() {
    <span style="color: rgb(78,201,176);">Column</span>() {
      <span style="color: rgb(78,201,176);">Stack</span>({alignContent: <span style="color: rgb(78,201,176);">Alignment.Top</span>}) {
        <span style="color: rgb(78,201,176);">Text</span>()<span style="color: rgb(212,212,212);">.</span>width(<span style="color: rgb(206,145,120);">'100%'</span>)<span style="color: rgb(212,212,212);">.</span>height(<span style="color: rgb(206,145,120);">'70%'</span>)<span style="color: rgb(212,212,212);">.</span>backgroundColor(<span style="color: rgb(181,206,168);">0xd2cab3</span>)
          .align(<span style="color: rgb(78,201,176);">Alignment.Center</span>)<span style="color: rgb(212,212,212);">.</span>textAlign(<span style="color: rgb(78,201,176);">TextAlign.Center</span>);
        <span style="color: rgb(106,153,85);">// 此处省略100个相同的背景Text组件</span>
        <span style="color: rgb(78,201,176);">Stack</span>() {
          <span style="color: rgb(197,134,192);">if</span> (<span style="color: rgb(86,156,214);">this</span><span style="color: rgb(212,212,212);">.</span>isVisible) {
            <span style="color: rgb(78,201,176);">Text</span>(<span style="color: rgb(206,145,120);">'New Page'</span>)<span style="color: rgb(212,212,212);">.</span>height(<span style="color: rgb(206,145,120);">"70%"</span>)<span style="color: rgb(212,212,212);">.</span>backgroundColor(<span style="color: rgb(181,206,168);">0xd2cab3</span>)
              .align(<span style="color: rgb(78,201,176);">Alignment.Center</span>)<span style="color: rgb(212,212,212);">.</span>textAlign(<span style="color: rgb(78,201,176);">TextAlign.Center</span>);
          }
        }<span style="color: rgb(212,212,212);">.</span>width(<span style="color: rgb(206,145,120);">'100%'</span>)<span style="color: rgb(212,212,212);">.</span>height(<span style="color: rgb(206,145,120);">'70%'</span>)
      }
      <span style="color: rgb(78,201,176);">Button</span>(<span style="color: rgb(206,145,120);">"press"</span>)<span style="color: rgb(212,212,212);">.</span>onClick(() <span style="color: rgb(212,212,212);">=</span><span style="color: rgb(212,212,212);">></span> {
        <span style="color: rgb(86,156,214);">this</span><span style="color: rgb(212,212,212);">.</span>isVisible <span style="color: rgb(212,212,212);">=</span> <span style="color: rgb(212,212,212);">!</span>(<span style="color: rgb(86,156,214);">this</span><span style="color: rgb(212,212,212);">.</span>isVisible);
      })
    }
  }
}
```
 
 

##### 反例

```text
@Entry
@Component
struct StackExample5 {
  @State isVisible : boolean = false;
  build() {
    Column() {
      Stack({alignContent: Alignment.Top}) {
        Text().width('100%').height('70%').backgroundColor(0xd2cab3)
          .align(Alignment.Center).textAlign(TextAlign.Center);
        // 此处省略100个相同的背景Text组件
        if (this.isVisible) {
          Text('New Page').height("70%").backgroundColor(0xd2cab3)
            .align(Alignment.Center).textAlign(TextAlign.Center);
        }
      }
      Button("press").onClick(() => {
        this.isVisible = !(this.isVisible);
      })
    }
  }
}
```
 
 

##### 规则集

```text
<span style="color: rgb(106,135,89);">plugin:@performance/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
