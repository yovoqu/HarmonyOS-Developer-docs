# @hw-stylistic/one-var-declaration-per-line

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_one-var-declaration-per-line

变量声明时，要求一次仅声明一个变量。该规则仅检查.ets文件类型。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@hw-stylistic/one-var-declaration-per-line": "error"
  }
}
```
 
 

#### 选项

该规则无需配置额外选项。
 
 

#### 正例

```text
let a: string = 'hello';
let b: string = 'world';
a += 'my';
b += 'my';

const c: string = 'hello';
const d: string = 'world';

console.info(`a: ${a}, b: ${b}, c: ${c}, d: ${d}`);
```
 
 

#### 反例

```text
// Split 'const' declarations into multiple statements.
const a: string = 'hello', b: string = 'world';
```
 
 

#### 规则集

```text
<span style="color: rgb(6,125,23);">"plugin:@hw-stylistic/recommended"</span>
<span style="color: rgb(6,125,23);">"plugin:@hw-stylistic/all"</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
