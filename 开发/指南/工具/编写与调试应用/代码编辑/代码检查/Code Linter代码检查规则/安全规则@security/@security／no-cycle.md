# @security/no-cycle

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-cycle

该规则禁止使用循环依赖。


## 规则配置


```text
// code-linter.json5
{
  "rules": {
    "@security/no-cycle": "error"
  }
}
```


## 选项

该规则无需配置额外选项。

## 正例


```text
// foo.ets
import {} from './bar';

// bar.ets
import {} from './index';
```


## 反例


```text
// foo.ets
import {} from './bar';

// bar.ets
import {} from './foo';
```


> [!NOTE]
> 反例中foo.ets文件依赖了bar.ets文件，bar.ets文件同时依赖了foo.ets文件，造成了循环依赖。


## 规则集


```text
plugin:@security/all
```

 Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
