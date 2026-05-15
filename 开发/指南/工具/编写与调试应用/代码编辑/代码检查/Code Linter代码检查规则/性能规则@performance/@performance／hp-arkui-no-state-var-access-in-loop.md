# @performance/hp-arkui-no-state-var-access-in-loop

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-no-state-var-access-in-loop

避免在for、while等循环逻辑中频繁读取状态变量。

 通用丢帧场景下，建议优先修改。


## 规则配置


```text
// code-linter.json5
{
  "rules": {
    "@performance/hp-arkui-no-state-var-access-in-loop": "warn",
  }
}
```


## 选项

该规则无需配置额外选项。

## 正例


```text
import hilog from '@ohos.hilog'

@Entry
@Component
struct MyComponent{
  @State message: string = '';
  build() {
    Column() {
      Button('点击打印日志')
        .onClick(() => {
          this.message = 'click';
          let logMessage: string = this.message;
          for (let i = 0; i

## 反例


```text
import hilog from '@ohos.hilog'
@Entry
@Component
struct MyComponent{
@State message: string = '';
build() {
Column() {
Button('点击打印日志')
.onClick(() => {
this.message = 'click';
for (let i = 0; i

## 规则集


```text
plugin:@performance/recommended
plugin:@performance/all
```

 Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
