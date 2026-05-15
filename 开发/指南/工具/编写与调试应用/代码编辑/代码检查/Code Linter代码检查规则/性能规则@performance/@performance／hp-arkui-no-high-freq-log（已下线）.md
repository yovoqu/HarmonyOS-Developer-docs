# @performance/hp-arkui-no-high-freq-log（已下线）

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hp-arkui-no-high-freq-log

建议在正式发布的版本中，注释掉或删除日志打印代码。该规则已于5.0.3.403版本下线。


## 正例


```text
import hilog from '@ohos.hilog';
@Entry
@Component
struct MyComponent{
  build() {
    Column() {
      Scroll()
        .onScroll(() => {
          //正例
          //hilog.info(1001, 'Index', 'onScroll')
          // do something
        })
    }
  }
}
```


## 反例


```text
import hilog from '@ohos.hilog';
@Entry
@Component
struct MyComponent{
  build() {
    Column() {
      Scroll()
        .onScroll(() => {
          // 高频操作中不建议写日志
          hilog.info(1001, 'Index', 'onScroll')
          // do something
        })
    }
  }
}
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
