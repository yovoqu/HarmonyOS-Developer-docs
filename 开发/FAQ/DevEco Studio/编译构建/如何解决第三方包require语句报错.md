# 如何解决第三方包require语句报错

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-125

**问题现象**
 
引入第三方包时，编译出现错误。
 
**报错原因**
 
部分第三方包由npm迁移而来，其开发环境为Node。其中的require语法ArkCompiler不完全支持，导致运行时出现错误。
 
**场景1**：
 
```json
<em>// Module/src/test.json</em>
{a: 1, b: 2}
<em>// use.js</em>
let test = require("Module/src/test.json")
```
 
**需修改为：**
 
```json
<em>// Module/src/test.json</em>
module.exports = {a: 1, b: 2}
```
 
```text
<em>// use.js</em>
let test = require("Module/src/test")
```
 
**场景2：**
 
```json
<em>// Module/package.json</em>
...
main: "./src"
...
<em>// use.js</em>
let module = require("Module")
```
 
**需修改为：**
 
```json
<em>// Module/package.json</em>
"main": "./src/index.js",
```
 
```text
<em>// use.js</em>
let module = require("Module")
```
 
**场景3：**
 
编译时出现警告信息：
 
```text
Plugin node-resolve: preferring built-in module 'util' over local alternative at '/Users/~/Documents/fe-module/demo/node_modules/util/util.js', pass 'preferBuiltins: false' to disable this behavior or 'preferBuiltins: true' to disable this warning
```
 
**解决方案**
 
修改rollup.config.js中的preferBuiltins字段。
 
```text
plugins: [
    resolve({
        preferBuiltins: false,   <em> // true or false</em>
        mainFields: ['module', 'main'],
        extensions
    })
];
```
 
**场景4：**
 
```text
import {Buffer} from 'buffer'
```
 
**需修改为：**
 
```text
import {Buffer} from 'buffer/'
```
