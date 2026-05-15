# @cross-device-app-dev/font-size-unit

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_font-size-unit

字体大小单位建议使用fp，以适配系统字体设置。


## 规则配置


```text
// code-linter.json5
{
  "rules": {
    "@cross-device-app-dev/font-size-unit": "warn"
  }
}
```


## 选项

该规则无需配置额外选项。

## 正例


```text
const FONT_SIZE = 12;

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text('message').fontSize(FONT_SIZE)
      Text('message').fontSize('12fp')
    }
  }
}
```


## 反例


```text
@Entry
@Component
struct Index1 {
  build() {
    RelativeContainer() {
      Text('message').fontSize('12vp')
      Text('message').fontSize('12px')
      Text('message').fontSize('12lpx')
    }
  }
}
```


## 规则集


```text
plugin:@cross-device-app-dev/recommended
plugin:@cross-device-app-dev/all
```

 Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
