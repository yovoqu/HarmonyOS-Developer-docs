# @performance/init-list-component

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-init-list-component

List组件在使用时，建议同时定义width和height属性。


## 规则配置


```text
// code-linter.json5
{
  "rules": {
    "@performance/init-list-component": "warn",
  }
}
```


## 选项

该规则无需配置额外选项。

## 正例


```text
@Component
struct Greeting {
  @Builder myBuilder() {
    List().width(10).height(10)
  }
  build() {
    List() {
    }.width(10).height(10);
  }
}

@Builder function globalBuilder() {
  List().width(10).height(10)
}
```


## 反例


```text
@Component
struct Greeting {
  @Builder myBuilder() {
    // missing initialization of attribute 'height'
    List().width(10)
  }
  build() {
    // missing initialization of attribute 'width'
    List().height(10);
  }
}

@Builder function myBuilder() {
  // missing initialization of attribute 'height'
  List().width(10)
}
```


## 规则集


```text
plugin:@performance/all
```

 Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
