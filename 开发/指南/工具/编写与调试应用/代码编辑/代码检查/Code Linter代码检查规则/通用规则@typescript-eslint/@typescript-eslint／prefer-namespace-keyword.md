# @typescript-eslint/prefer-namespace-keyword

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-namespace-keyword

推荐使用“namespace”关键字而不是“module”关键字来声明一个自定义的 TypeScript 模块。
 
该规则仅支持对.js/.ts文件进行检查。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@typescript-eslint/prefer-namespace-keyword": "error"
  }
}
```
 
 

#### 选项

该规则无需配置额外选项。
 
 

#### 正例

```text
export namespace Example {}
```
 
 

#### 反例

```text
export module Example {}
```
 
 

#### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
