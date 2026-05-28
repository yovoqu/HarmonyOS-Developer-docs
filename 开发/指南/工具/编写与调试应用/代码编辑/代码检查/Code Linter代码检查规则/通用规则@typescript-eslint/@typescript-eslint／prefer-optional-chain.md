# @typescript-eslint/prefer-optional-chain

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-optional-chain

强制使用链式可选表达式，而不是链式逻辑与、否定逻辑或、或空对象。
 

 

##### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@typescript-eslint/prefer-optional-chain": "error"
  }
}
```
 
 

##### 选项

详情请参考[@typescript-eslint/prefer-optional-chain选项](https://typescript-eslint.nodejs.cn/rules/prefer-optional-chain/#options)。
 
 

##### 正例

```text
class Foo {
  public a?: Foo = new Foo();

  public b?: Foo = new Foo();

  public c?: Foo = new Foo();

  public method?(): void {
    console.info('method');
  }
}

const foo = new Foo();
export const c = foo.a?.b?.c;
foo.a?.b?.method?.();
```
 
 

##### 反例

```text
class Foo {
  public a?: Foo = new Foo();

  public b?: Foo = new Foo();

  public c?: Foo = new Foo();

  public method?(): void {
    console.info('method');
  }
}

const foo = new Foo();
let c = foo.a;
c = c && c.b;
c = c && c.c;
export { c };
if (foo.a && foo.a.b && foo.a.b.method) {
  foo.a.b.method();
}
```
 
 

##### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
