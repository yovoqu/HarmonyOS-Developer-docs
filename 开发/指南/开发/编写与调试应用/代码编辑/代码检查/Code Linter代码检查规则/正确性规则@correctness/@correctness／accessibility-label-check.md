# @correctness/accessibility-label-check

更新时间：2026-06-12 06:54:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-accessibility-label-check

## @correctness/accessibility-label-check
 

在无障碍场景中，建议通过[accessibilityText](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-accessibility#accessibilitytext)为控件添加无障碍文本信息。
 

##### 规则配置

```text
// code-linter.json5
{
  "rules": {
    "@correctness/accessibility-label-check": "suggestion"
  }
}
```
 
 

##### 选项

该规则无需配置额外选项。
 
 

##### 正例

```text
@Entry
@Component
struct AccessibilityLabelPositive {
    build() {
        Column() {
            Text('文本')
                .width(60)
                .height(60)
                .accessibilityText('返回')
                .onClick(() => {})
        }
    }
}
```
 
 

##### 反例

```text
@Entry
@Component
struct AccessibilityLabelNegative {
    build() {
        Column() {
            Text()
                .width(60)
                .height(60)
                .backgroundColor(0xeaeaea)
                .onClick(() => {})
        }
    }
}
```
 
 

##### 规则集

```text
plugin:@correctness/all
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
