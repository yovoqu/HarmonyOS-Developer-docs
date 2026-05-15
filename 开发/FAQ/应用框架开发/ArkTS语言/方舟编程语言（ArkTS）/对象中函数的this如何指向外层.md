# 对象中函数的this如何指向外层

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-139

通过箭头函数实现。参考代码如下：

```ts
interface T {
start: () => number
}
@Component
struct PointingOuterLayer {
@State num: number = 1
obj: T = {
start: () => {
return this.num
}
}
```
