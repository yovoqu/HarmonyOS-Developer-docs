# @hw-stylistic/indent

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_indent

强制switch语句中的case和default缩进一层。该规则仅检查.ets文件类型。
 

##### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@hw-stylistic/indent": "error"
  }
}
```
 
 

##### 选项

该规则无需配置额外选项。
 
 

##### 正例

```text
enum E {
  a = 'a',
  b = 'b',
  c = 'c'
}

export function test(e: E) {
  switch (e) {
    case E.a:
      console.info('doSomething');
      break;
    case E.b:
    case E.c:
      console.info('doSomething');
      break;
    default:
      console.info('doSomething');
  }
}
```
 
 

##### 反例

```text
enum E {
  a = 'a',
  b = 'b',
  c = 'c'
}

export function test(e: E) {
  switch (e) {
      // Expected indentation of 2 relative to switch.
      case E.a:
      // Expected indentation of 2 relative to case.
      console.info('hello');
      // Expected indentation of 2 relative to case.
      break;
    case E.b:
      console.info('hello');
      break;
    case E.c:
    // Expected indentation of 2 relative to case.
    console.info('hello');
      break;
    default:
    // Expected indentation of 2 relative to default.
    console.info('hello');
  }
}
```
 
 

##### 规则集

```text
<span style="color: rgb(6,125,23);">"plugin:@hw-stylistic/recommended"</span>
<span style="color: rgb(6,125,23);">"plugin:@hw-stylistic/all"</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
