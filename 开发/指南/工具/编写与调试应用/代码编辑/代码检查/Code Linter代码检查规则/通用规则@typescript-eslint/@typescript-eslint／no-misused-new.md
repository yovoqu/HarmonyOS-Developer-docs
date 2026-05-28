# @typescript-eslint/no-misused-new

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-misused-new

要求正确地定义“new”和“constructor”。
 

##### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@typescript-eslint/no-misused-new": "error"
  }
}
```
 
 

##### 选项

该规则无需配置额外选项。
 
 

##### 正例

```text
export declare class C {
  public name: string;

  public constructor();
}
```
 
 

##### 反例

```text
export declare class C {
  // 应该定义为constructor(): C
  public new(): C;
}

export interface I {
  // 不应该定义constructor
  constructor(): void;
}
```
 
 

##### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
