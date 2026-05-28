# @typescript-eslint/method-signature-style

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_method-signature-style

定义函数类型的属性时，强制使用特定的风格。
 
有两种方式定义对象/接口中函数类型的属性，一种是定义为属性，属性签名是函数，另一种是直接定义为方法。
 
该规则仅支持对.js/.ts文件进行检查。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@typescript-eslint/method-signature-style": "error"
  }
}
```
 
 

#### 选项

详情请参考[@typescript-eslint/method-signature-style选项](https://typescript-eslint.nodejs.cn/rules/method-signature-style/#options)。
 
 

#### 正例

```text
// 默认要求定义为属性
export interface T1 {
  func: (arg: string) => number;
}
```
 
 

#### 反例

```text
// 默认要求定义为属性
export interface T1 {
  func(arg: string): number;
}
```
 
 

#### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
