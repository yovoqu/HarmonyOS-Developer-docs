# 编译报错“Duplicated files found in module entry. This may cause unexpected errors at runtime”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-107

**问题现象**
 
编译构建时，报错“Duplicated files found in module entry. This may cause unexpected errors at runtime”。
 

![](assets/编译报错“Duplicated%20files%20found%20in%20module%20entry.%20This%20may%20cause%20unexpected%20errors%20at%20runtime”/file-20260515130135469-0.png)

 
**解决措施**
 
该报错是从不同的包中收集到了相同名称的so包，导致so包冲突，可在模块级build-profile.json5文件中添加enableOverride字段并设置true。更多内容可参考[模块级build-profile.json5文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-profile)。
 
```json
"buildOption": {
  "nativeLib": {
    "filter": {
      "enableOverride": true
    }
  }
},
```
