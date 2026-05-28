# @typescript-eslint/no-misused-promises

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-misused-promises

禁止在不正确的位置使用Promise。
 

##### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@typescript-eslint/no-misused-promises": "error"
  }
}
```
 
 

##### 选项

详情请参考[@typescript-eslint/no-misused-promises选项](https://typescript-eslint.nodejs.cn/rules/no-misused-promises/#options)。
 
 

##### 正例

```text
export async function func(): Promise<void>{
  const promise = Promise.resolve('value');

  // Always `await` the Promise in a conditional
  if (await promise) {
    // Do something
  }

  const val = await promise ? '123' : '456';
  console.log(`${val}`);

  while (await promise) {
    // Do something
  }
}
```
 
 

##### 反例

```text
export async function func(): Promise<void>{
  const promise = Promise.resolve('value');
  // 默认条件语句中需要使用await Promise
  if (promise) {
    // Do something
  }

  // 默认条件语句中需要使用await Promise
  const val = promise ? '123' : '456';
  console.log(`${val}`);

  // 默认条件语句中需要使用await Promise
  while (promise) {
    // Do something
  }
}
```
 
 

##### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@typescript-eslint/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
