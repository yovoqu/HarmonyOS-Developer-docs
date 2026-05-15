# @typescript-eslint/member-ordering

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_member-ordering

要求类、接口和类型字面量中成员的排序方式保持一致的风格。


## 规则配置


```text
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/member-ordering": "error"
  }
}
```


## 选项

详情请参考[@typescript-eslint/member-ordering选项](https://typescript-eslint.nodejs.cn/rules/member-ordering/#options)。

## 正例


```text
// 默认排序规则：field-constructor-method
export class Foo2 {
  // -> field
  protected static e: string = '';

  public d: string = '';

  private readonly c: string = '';

  // -> constructor
  public constructor() {
    console.info('constructor');
  }

  // -> method
  public static a(): void {
    console.info('static method');
  }

  public b(): void {
    console.info(this.c);
  }
}
```


## 反例


```text
// 默认排序规则：field-constructor-method
export class Foo2 {
  // -> method
  public static a(): void {
    console.info('static method');
  }

  public b(): void {
    console.info(this.c);
  }

  // -> field
  protected static e: string = '';

  private readonly c: string = '';

  public d: string = '';

  // -> constructor
  public constructor() {
    console.info('constructor');
  }
}
```


## 规则集


```text
plugin:@typescript-eslint/all
```

 Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
