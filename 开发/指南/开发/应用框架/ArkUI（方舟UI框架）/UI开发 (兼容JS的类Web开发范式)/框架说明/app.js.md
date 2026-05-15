# app.js

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/js-framework-js-file

## 应用生命周期

每个应用可以在app.js自定义应用级[生命周期](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/js-framework-lifecycle)的实现逻辑，以下示例仅在生命周期函数中打印对应日志：
```text
// app.js
export default {
    onCreate() {
        console.info('Application onCreate');
    },

    onDestroy() {
        console.info('Application onDestroy');
    },
}
```


## 应用对象6+


| 属性 | 类型 | 描述 |
| --- | --- | --- |
| getApp | Function | 提供getApp()全局方法，可以在自定义js文件中获取app.js中暴露的对象。 |

示例如下：
```text
// app.js
export default {
    data: {
        test: "by getApp"
    },
    onCreate() {
        console.info('AceApplication onCreate');
    },
    onDestroy() {
        console.info('AceApplication onDestroy');
    },
}
```


```text
// test.js 自定义逻辑代码
export var appData = getApp().data;
```
