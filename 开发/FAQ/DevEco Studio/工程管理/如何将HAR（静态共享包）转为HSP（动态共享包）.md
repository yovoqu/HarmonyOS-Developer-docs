# 如何将HAR（静态共享包）转为HSP（动态共享包）

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-7

HAR转换成HSP可参考如下步骤：

1. 新建一个HSP，将HAR包拷贝到lib目录，并在HSP的oh-package.json5文件的dependencies下配置HAR包。
```json
"dependencies": {
"myhar": "file:./lib/myHar.har" // MyHar.Har path: oh-package.json5 file in the same directory as the lib folder
},
```
2. 在HSP的Index.ets中直接导出HAR内容。
```ts
export * as myhar from 'myhar';
```
3. 最后编译该HSP。
