# 如何判断JS对象中是否存在某个值

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-192

Object.values(对象名).indexOf(待检测值)，若返回-1表示不包含对应值；返回值不等于-1则表示包含。

```text
var res = array.indexOf(val)
```
