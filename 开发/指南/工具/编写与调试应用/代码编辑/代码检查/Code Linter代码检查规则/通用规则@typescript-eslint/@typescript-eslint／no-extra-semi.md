# @typescript-eslint/no-extra-semi

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-extra-semi

禁止使用不必要的分号。


## 规则配置


```text
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-extra-semi": "error"
  }
}
```


## 选项

该规则无需配置额外选项。

## 正例


```text
export const x = 5;

export function foo() {
  // code
}

export const bar = () => {
  // code
};

export class C {
  public field: string = 'field';

  static {
    // code
  }

  public method() {
    // code
  }
}
```


## 反例


```text
export const x = 5;;

export function foo() {
  // code
};

export const bar = () => {
  // code
};;

export class C {
  public field: string = 'field';;

  static {
    // code
  };

  public method() {
    // code
  };
};
```


## 规则集


```text
plugin:@typescript-eslint/all
```

 Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
