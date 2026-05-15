# 如何解决调用两次fileIo接口写文件，但第二次写入的内容未完全覆盖第一次写入的内容的问题

更新时间：2026-04-21 08:35:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-25

清空文件时必须要设置OpenMode.TRUNC，默认覆盖模式(WRITE_ONLY)只是覆盖不会清除，TRUNC模式会先清空文件内容。参考代码如下：

```ts
fileIo.openSync(
  dst,
  fileIo.OpenMode.WRITE_ONLY | fileIo.OpenMode.TRUNC | fileIo.OpenMode.CREATE,
);
```
