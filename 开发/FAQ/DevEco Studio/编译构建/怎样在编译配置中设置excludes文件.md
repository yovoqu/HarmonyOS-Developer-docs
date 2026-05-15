# 怎样在编译配置中设置excludes文件

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-57

在模块级build-profile.json5中如下进行配置：

```json
"nativeLib": {
"debugSymbol": {
"strip": true,
"exclude": [
"**/3.so"
]
}
},
```
