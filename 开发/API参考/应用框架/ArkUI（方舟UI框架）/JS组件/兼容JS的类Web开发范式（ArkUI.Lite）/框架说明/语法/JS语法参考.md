# JS语法参考

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-framework-syntax-js
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / lite_wearable / TV

JS文件用来定义HML页面的业务逻辑，支持ECMA规范的JavaScript语言。基于JavaScript语言的动态化能力，可以使应用更加富有表现力，具备更加灵活的设计。下面讲述JS文件的编译和运行的支持情况。


## 语法
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / lite_wearable / TV

支持ES6语法。轻量级智能穿戴支持的ES6语法有限，仅支持以下ES6 语法：


1. let/const
2. arrow functions
3. class
4. default value
5. destructuring assignment
6. destructuring binding pattern
7. enhanced object initializer
8. for-of
9. rest parameter
10. template strings


- 模块声明  使用import方法引入功能模块：  __PREBLOCK_0__
- 代码引用  使用import方法导入js代码：  __PREBLOCK_1__


## 对象
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / lite_wearable / TV


- 页面对象 属性 类型 描述   data Object/Function 页面的数据模型，类型是对象或者函数，如果类型是函数，返回值必须是对象。属性名不能以\$或_开头，不要使用保留字for, if, show, tid。   \$refs Object 持有注册过ref 属性的DOM元素或子组件实例的对象。示例见[获取DOM元素](#获取dom元素)。


## 获取DOM元素
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / lite_wearable / TV


1. 通过\$refs获取DOM元素  __PREBLOCK_2__  __PREBLOCK_3__
