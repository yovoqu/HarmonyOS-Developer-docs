# @typescript-eslint/init-declarations

更新时间：2026-04-20 06:32:02

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_init-declarations

禁止或者要求在变量声明中进行初始化。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@typescript-eslint/init-declarations": "error"
  }
}
```
 
 

#### 选项

详情请参考[@typescript-eslint/init-declarations选项](https://eslint.nodejs.cn/docs/rules/init-declarations#选项)。
 
 

#### 正例

```text
// 默认变量必须在声明时初始化
export function foo() {
  console.info('hello');
}

export const bar = 1;
export const qux = 3;
```
 
 

#### 反例

```text
// 默认变量必须在声明时初始化
export function foo() {
  console.info('hello');
}

export let bar: string;
export let qux: number;
```
 
 

#### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
