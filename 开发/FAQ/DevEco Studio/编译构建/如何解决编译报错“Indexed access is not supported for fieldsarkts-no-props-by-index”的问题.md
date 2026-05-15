# 如何解决编译报错“Indexed access is not supported for fields(arkts-no-props-by-index)”的问题

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-126

问题现象

动态调用类或接口的字段会导致编译报错：Indexed access is not supported for fields (arkts-no-props-by-index)。


![](assets/如何解决编译报错“Indexed%20access%20is%20not%20supported%20for%20fieldsarkts-no-props-by-index”的问题/file-20260515130146738-0.png)


解决方案

修改代码：

```ts
getValue(breakpoint: string): T {
return Reflect.get(this.options, breakpoint) as T;
}
```
