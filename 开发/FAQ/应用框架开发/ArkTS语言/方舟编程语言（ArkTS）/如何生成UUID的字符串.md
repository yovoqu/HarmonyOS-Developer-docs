# 如何生成UUID的字符串

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-20

使用util工具的generateRandomUUID函数可以生成字符串类型的UUID，示例如下：

```ts
let uuid = util.generateRandomUUID(true);
console.info('RFC 4122 Version 4 UUID:' + uuid); // Output randomly generated UUID
```

参考链接

util.generateRandomUUID
