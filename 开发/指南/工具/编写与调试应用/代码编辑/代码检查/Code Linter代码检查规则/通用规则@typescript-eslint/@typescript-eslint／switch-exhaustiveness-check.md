# @typescript-eslint/switch-exhaustiveness-check

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_switch-exhaustiveness-check

要求switch语句对于联合类型中值的判断是详尽无遗的。
 
当switch语句中的判断条件是字面量值的集合或者是一个枚举类型，如果case语句中缺少任何一个值的判断，并且没有default语句时，此规则会告警。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@typescript-eslint/switch-exhaustiveness-check": "error"
  }
}
```
 
 

#### 选项

详情请参考[@typescript-eslint/switch-exhaustiveness-check选项](https://typescript-eslint.nodejs.cn/rules/switch-exhaustiveness-check/#options)。
 
 

#### 正例

```text
type Day =
  | 'Monday'
  | 'Tuesday'
  | 'Wednesday'
  | 'Thursday'
  | 'Friday'
  | 'Saturday'
  | 'Sunday';

declare const day1: Day;

let result = '0';

switch (day1) {
  case 'Monday':
    result = '1';
    break;
  case 'Tuesday':
    result = '2';
    break;
  case 'Wednesday':
    result = '3';
    break;
  case 'Thursday':
    result = '4';
    break;
  case 'Friday':
    result = '5';
    break;
  case 'Saturday':
    result = '6';
    break;
  case 'Sunday':
    result = '7';
    break;
}

declare const day2: Day;

result = '0';

switch (day2) {
  case 'Monday':
    result = '1';
    break;
  default:
    result = '42';
}
console.info(result);

enum Fruit {
  apple = 'apple',
  banana = 'banana',
  cherry = 'cherry'
}

declare const fruit: Fruit;

switch (fruit) {
  case Fruit.apple:
    console.log('an apple');
    break;

  case Fruit.banana:
    console.log('a banana');
    break;

  case Fruit.cherry:
    console.log('a cherry');
    break;
}
```
 
 

#### 反例

```text
type Day =
  | 'Monday'
  | 'Tuesday'
  | 'Wednesday'
  | 'Thursday'
  | 'Friday'
  | 'Saturday'
  | 'Sunday';

declare const day: Day;
let result = '0';

switch (day) {
  // 只处理了'Monday'，缺少其他值的判断，并且也没有default分支
  case 'Monday':
    result = '1';
    break;
}
console.info(result);
```
 
 

#### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
