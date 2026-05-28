# @typescript-eslint/no-dynamic-delete

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-dynamic-delete

不允许在computed key表达式上使用“delete”运算符。
 
该规则仅支持对.js/.ts文件进行检查。
 

##### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@typescript-eslint/no-dynamic-delete": "error"
  }
}
```
 
 

##### 选项

该规则无需配置额外选项。
 
 

##### 正例

```text
const container: Record<string, number> = {
  /* ... */
};

// Constant runtime lookups by string index
delete container.aaa;

// Constants that must be accessed by []
delete container['7'];
// '-Infinity' is number.  
delete container['-Infinity'];
```
 
 

##### 反例

```text
const container: Record<string, number> = {
  /* ... */
};

// Can be replaced with the constant equivalents, such as container.aaa
delete container['aaa'];
// 'Infinity' may be a string constant
delete container['Infinity'];

// Dynamic, difficult-to-reason-about lookups
const name = 'name';
delete container[name];
delete container[name.toUpperCase()];
```
 
 

##### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/recommended</span>
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
