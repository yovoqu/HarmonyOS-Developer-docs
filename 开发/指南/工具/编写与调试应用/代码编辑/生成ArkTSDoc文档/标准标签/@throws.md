# @throws

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arktsdoc-throws

@throws标签用于函数，记录函数可能引发的错误。可以在一个ArkTSDoc注释中多次使用@throws标记。
 

#### 语法

@throws description
 
 

#### 示例

使用带有描述的 @throws 标记：
 
```text
/**
 * @throws Will throw an error if the argument is null.
 */
export function bar(x: number) {
  throw new Error();
}
```
