# @returns

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arktsdoc-returns

@returns标签用于记录函数返回值。
 

##### 语法

@returns [description]
 
 

##### 示例

```text
/**
 * Returns the sum of a and b
 * @param a
 * @param b
 * @returns Sum of a and b
 */
export function sum(a: number, b: number): number{
  return a + b;
}
```
