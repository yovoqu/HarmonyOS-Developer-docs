# @typescript-eslint/brace-style

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_brace-style

对代码块强制执行一致的括号样式。


## 规则配置


```text
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/brace-style": "error"
  }
}
```


## 选项

详情请参考[@typescript-eslint/brace-style选项](https://eslint.nodejs.cn/docs/rules/brace-style#选项)。

## 正例


```text
function foo(): boolean {
  return true;
}

class C {
  static {
    foo();
  }

  public meth() {
    foo();
  }
}

export { C };
```


## 反例


```text
function foo(): boolean
{
  return true;
}

class C {
  static
  {
    foo();
  }

  public meth()
  {
    foo();
  }
}

export { C };
```


## 规则集


```text
plugin:@typescript-eslint/all
```

 Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
