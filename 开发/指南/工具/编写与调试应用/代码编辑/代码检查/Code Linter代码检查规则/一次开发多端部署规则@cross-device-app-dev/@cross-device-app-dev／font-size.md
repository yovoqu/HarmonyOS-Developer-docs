# @cross-device-app-dev/font-size

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_font-size

字体大小要求至少为8fp以便于阅读。
 

##### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    <span style="color: rgb(135,16,148);">"@cross-device-app-dev/font-size"</span>: <span style="color: rgb(6,125,23);">"warn"</span>
  }
}
```
 
 

##### 选项

该规则无需配置额外选项。
 
 

##### 正例

```text
const FONT_SIZE = 12;

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text('message').fontSize(12)
      Text('message').fontSize('12fp')
    }
  }
}
```
 
 

##### 反例

```text
const FONT_SIZE = 7;

@Entry
@Component
struct Index1 {
  build() {
    RelativeContainer() {
      Text('message').fontSize(FONT_SIZE)
      Text('message').fontSize('7fp')
    }
  }
}
```
 
 

##### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@cross-device-app-dev/recommended</span>
<span style="color: rgb(6,125,23);">plugin:@cross-device-app-dev/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
