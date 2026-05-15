# 如何在Web请求时添加header头

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-37

可以通过loadUrl方法设置headers。该方法接收两个参数：url表示需要加载的URL，headers为数组类型表示附加的HTTP请求头。

```ts
// With parameter headers
this.controller.loadUrl('www.example.com', [
  { headerKey: 'headerKey', headerValue: 'headerValue' },
]);
```

参考链接

loadUrl

WebHeader
