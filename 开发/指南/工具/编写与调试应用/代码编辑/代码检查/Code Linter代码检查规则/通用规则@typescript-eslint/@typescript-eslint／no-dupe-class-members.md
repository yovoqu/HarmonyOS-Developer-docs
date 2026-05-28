# @typescript-eslint/no-dupe-class-members

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-dupe-class-members

不允许重复的类成员。如果类成员中有同名的声明，最后一个声明会覆盖其他声明，可能会导致意外行为。
 
编译器会自动校验该规则检查的代码问题，新建项目时可以不开启此规则。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@typescript-eslint/no-dupe-class-members": "error"
  }
}
```
 
 

#### 选项

该规则无需配置额外选项。
 
 

#### 正例

```text
/*eslint no-dupe-class-members: "error"*/
export class A {
  public bar() {
    console.info('bar');
  }

  public qux() {
    console.info('qux');
  }
}

export class B {
  private name: string = 'bar';

  public get bar() {
    return this.name;
  }

  public set bar(value) {
    this.name = value;
  }
}

export class E {
  public static bar() {
    console.info('static bar');
  }

  public bar() {
    console.info('method bar');
  }
}
```
 
 

#### 反例

```text
/*eslint no-dupe-class-members: "error"*/
export class A {
  public bar() {
    console.info('bar');
  }

  public bar() {
    console.info('bar');
  }
}

export class B {
  private readonly name: string = 'bar';

  public get bar() {
    return this.name;
  }

  public bar() {
    return this.name;
  }
}

export class E {
  public static bar() {
    console.info('static bar');
  }

  public static bar() {
    console.info('static bar');
  }
}
```
 
 

#### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
