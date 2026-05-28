# @cross-device-app-dev/touch-target-size

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_touch-target-size

组件通用属性responseRegion点击热区需满足最小尺寸要求。
 
主要交互元素或控件的可点击热区至少为48vp×48vp（推荐），不得小于40vp×40vp。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    <span style="color: rgb(135,16,148);">"@cross-device-app-dev/touch-target-size"</span>: <span style="color: rgb(6,125,23);">"warn"</span>
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
      Text('message').responseRegion({width: 60, height: 60})
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
      Text('message').responseRegion({width: 27, height: 40})
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
