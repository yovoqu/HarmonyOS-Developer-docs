# @typescript-eslint/class-literal-property-style

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_class-literal-property-style

建议类中的字面量属性对外暴露时，保持一致的风格。


## 规则配置


```text
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/class-literal-property-style": "error"
  }
}
```


## 选项

详情请参考[@typescript-eslint/class-literal-property-style选项](https://typescript-eslint.nodejs.cn/rules/class-literal-property-style/#options)。

## 正例


```text
class Mx {
  public readonly myField1 = 'hello';

  public readonly myField2 = ['a', 'b'];

  public readonly ['myField3'] = 'hello world';

  public get myField4() {
    return `hello ${this.myField1}`;
  }
}

export { Mx };
```


## 反例


```text
class Mx {
  public static get myField1() {
    return '1';
  }

  public get ['myField2']() {
    return 'hello world';
  }
}

export { Mx };
```


## 规则集


```text
plugin:@typescript-eslint/all
```

 Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
