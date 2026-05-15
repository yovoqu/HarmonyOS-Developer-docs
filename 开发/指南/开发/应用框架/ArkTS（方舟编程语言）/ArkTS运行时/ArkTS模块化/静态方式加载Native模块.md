# 静态方式加载Native模块

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-import-native-module

在ES6(ECMAScript 6.0)模块设计中，使用import语法加载其他文件导出的内容是ECMA规范所定义的语法规则。为支持开发者使用该功能导入Native模块（so）导出的内容，ArkTS进行了相关适配，并提供了以下几种支持写法。


## 直接导入

在Native模块的index.d.ts文件中导出，并在文件内直接导入。

## 具名导入


```text
// libentry.so对应的index.d.ts
export const add: (a: number, b: number) => number;
```


```text
// NameImport.ets
import { add } from 'libentry.so'
add(2, 3);
```


## 默认导入


```text
// libentry.so对应的index.d.ts
export const add: (a: number, b: number) => number;
```


```text
// DefaultImport.ets
import entry from 'libentry.so'
entry.add(2, 3);
```


## 命名空间导入


```text
// libentry.so对应的index.d.ts
export const add: (a: number, b: number) => number;
```


```text
// NamespaceImport.ets
import * as entry from 'libentry.so'
entry.add(2, 3);
```


## 间接导入


## 转为具名变量导出再导入


```text
// libentry.so对应的index.d.ts
export const add: (a: number, b: number) => number;
```


```text
// NameExport.ets
// 将libentry.so的API封装后导出
import { add } from 'libentry.so';
export { add };
```


```text
// NameImportFromExport.ets
// 从中间模块导入API
import { add } from './NameExport';
const result = add(2, 3);
```


## 转为命名空间导出再导入


```text
// libentry.so对应的index.d.ts
export const add: (a: number, b: number) => number;
```


```text
// NamespaceExport.ets
export * from 'libentry.so'
```


```text
// NamespaceImportFromExport.ets
import { add } from './NamespaceExport'
add(2, 3);
```

![](assets/静态方式加载Native模块/file-20260514130449758-0.png)
不支持Native模块导出和导入同时使用命名空间。   **反例：**
```text
// test1.ets
export * from 'libentry.so'
```


```text
// test2.ets
import * as add from './test1'
// 无法获取add对象
```


## 动态导入


## 直接导入


```text
// libentry.so对应的index.d.ts
export const add: (a: number, b: number) => number;
```


```text
// DynamicImport.ets
import('libentry.so').then((entry:ESObject) => {
  entry.default.add(2, 3);
})
```


## 间接导入


```text
// DynamicExport.ets
import entry from 'libentry.so'
export { entry }
```


```text
// DynamicImportFromExport.ets
import('./DynamicExport').then((ns:ESObject) => {
  ns.entry.add(2, 3);
})
```

![](assets/静态方式加载Native模块/file-20260514130449758-1.png)
不支持动态加载时，导出文件使用命名空间。   **反例：**
```text
// test1.ets
export * from 'libentry.so'
```


```text
// test2.ets
import('./test1').then((ns:ESObject) => {
    // 无法获取ns对象
})
```
