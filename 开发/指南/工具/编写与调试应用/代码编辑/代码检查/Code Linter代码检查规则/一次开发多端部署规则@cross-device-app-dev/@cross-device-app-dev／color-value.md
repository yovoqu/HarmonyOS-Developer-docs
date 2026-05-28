# @cross-device-app-dev/color-value

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_color-value

颜色值应当使用“\$r”从color.json中引用，以适配不同的系统颜色模式，禁止使用固定的值。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    <span style="color: rgb(135,16,148);">"@cross-device-app-dev/color-value"</span>: <span style="color: rgb(6,125,23);">"warn"</span>
  }
}
```
 
 

#### 选项

该规则无需配置额外选项。
 
 

#### 正例

```json
@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      // 通过'sys.color.xxx'引用的颜色值，默认支持dark和light颜色模式
      Text()
        .fontColor($r('sys.color.ohos_id_color_activated'));
      // 通过'app.color.xxx'引用的颜色值，需要分别在dark和light颜色模式的color.json中配置
      Text()
        .fontColor($r('app.color.text_color'));
    }
  }
}
```
 
 

#### 反例

```text
@Entry
@Component
struct Index1 {
  build() {
    RelativeContainer() {
      Text('message').fontColor('#000000')
      Text('message').fontColor('rgb(0, 0, 0)')
      Text('message').fontColor(Color.Black)
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
