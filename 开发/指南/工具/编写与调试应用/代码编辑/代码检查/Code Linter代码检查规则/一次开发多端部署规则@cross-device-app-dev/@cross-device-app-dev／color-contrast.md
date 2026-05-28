# @cross-device-app-dev/color-contrast

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_color-contrast

文本和背景之间的颜色对比度至少为4.5:1以确保可读性。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    <span style="color: rgb(135,16,148);">"@cross-device-app-dev/color-contrast"</span>: <span style="color: rgb(6,125,23);">"warn"</span>
  }
}
```
 
 

#### 选项

该规则无需配置额外选项。
 
 

#### 正例

```text
@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text('message')
        // app.color.color1=#ffffff
        .fontColor($r('app.color.color1'))
          // app.color.color2=#000000
        .backgroundColor($r('app.color.color2'))
    }
  }
}
```
 
 

#### 反例

```text
@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text('message')
        // app.color.color1=#000000
        .fontColor($r('app.color.color1'))
        // app.color.color2=#333333
        .backgroundColor($r('app.color.color2'))
    }
  }
}
```
 
 

#### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@cross-device-app-dev/recommended</span>
<span style="color: rgb(6,125,23);">plugin:@cross-device-app-dev/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
