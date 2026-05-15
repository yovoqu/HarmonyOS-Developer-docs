# @typescript-eslint/prefer-readonly

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-readonly

如果私有成员从未在构造函数之外进行修改，则要求将其标记为“只读”。


## 规则配置


```text
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/prefer-readonly": "error"
  }
}
```


## 选项

详情请参考[@typescript-eslint/prefer-readonly选项](https://typescript-eslint.nodejs.cn/rules/prefer-readonly/#options)。

## 正例


```text
export class Container {
  // Public members might be modified externally
  public publicMember: boolean = true;

  // Protected members might be modified by child classes
  protected protectedMember: number = Number.MAX_VALUE;

  // This is modified later on by the class
  private modifiedLater = 'unchanged';

  public mutate() {
    this.modifiedLater = 'mutated';
  }
}
```


## 反例


```text
export class Container {
  // These member variables could be marked as readonly
  private neverModifiedMember = true;

  private onlyModifiedInConstructor: number;

  // Private parameter properties can also be marked as readonly
  private neverModifiedParameter: string;

  public constructor(
    onlyModifiedInConstructor: number,
    // Private parameter properties can also be marked as readonly
    neverModifiedParameter: string,
  ) {
    this.neverModifiedParameter = neverModifiedParameter;
    this.onlyModifiedInConstructor = onlyModifiedInConstructor;
  }
}
```


## 规则集


```text
plugin:@typescript-eslint/all
```

 Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
