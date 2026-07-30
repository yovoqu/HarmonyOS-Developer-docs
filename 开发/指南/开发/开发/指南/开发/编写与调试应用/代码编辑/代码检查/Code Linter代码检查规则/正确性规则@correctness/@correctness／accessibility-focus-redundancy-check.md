# @correctness/accessibility-focus-redundancy-check

更新时间：2026-07-28 12:07:32

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-accessibility-focus-redundancy-check

在无障碍场景开发中，避免控件焦点冗余。
 

#### 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@correctness/accessibility-focus-redundancy-check": "suggestion"
  }
}
```
 
 

#### 选项

该规则无需配置额外选项。
 
 

#### 正例

```text
@Entry
@Component
struct FocusRedundancyPositive {
    build() {
        Column() {
            Column() {
                Button('提交')
                    .onClick(() => {})
            }
            .accessibilityGroup(true)
            .onClick(() => {})
        }
    }
}
```
 
 

#### 反例

```text
@Entry
@Component
struct FocusRedundancyNegative {
    build() {
        Column() {
            Column() {
                Button('按钮1')
                    .accessibilityText('操作')
                    .onClick(() => {})

                Text('文本')
                    .accessibilityText('说明文字')

                Image($r('app.media.icon'))
                    .accessibilityText('图标')
                    .onClick(() => {}) 
            }
            .onClick(() => {})
        }
    }
}
```
 
 

#### 规则集

```text
plugin:@correctness/all
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
