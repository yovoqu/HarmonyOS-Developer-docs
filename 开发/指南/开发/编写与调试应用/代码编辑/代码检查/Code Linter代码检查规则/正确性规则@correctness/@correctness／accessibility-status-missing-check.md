# @correctness/accessibility-status-missing-check

更新时间：2026-06-12 06:54:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-accessibility-status-missing-check

在无障碍场景开发中，须通过[accessibilityRole](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-accessibility#accessibilityrole18)声明组件的类型标识，如“按钮”、“编辑框”。
 

#### 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@correctness/accessibility-status-missing-check": "suggestion"
  }
}
```
 
 

#### 选项

该规则无需配置额外选项。
 
 

#### 正例

```text
@Entry
@Component
struct AccessibilityStatusMissingPositive {
    build() {
        Column() {
            Column()
                .width(100)
                .height(60)
                .backgroundColor(0xf0f0f0)
                .accessibilityRole(AccessibilityRoleType.BUTTON)
                .onClick(() => {})
		}
	}
}
```
 
 

#### 反例

```text
@Entry
@Component
struct AccessibilityStatusMissingNegative {
    build() {
        Column() {
            Column()
                .width(100)
                .height(60)
                .backgroundColor(0xf0f0f0)
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
