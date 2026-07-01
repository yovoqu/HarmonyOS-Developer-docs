# ArkTS是否支持反射调用类的静态成员函数和实例成员函数

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-83

ArkTS 可以通过动态 import 实现反射功能，支持根据类名和方法名调用类中的静态成员函数和实例成员函数。示例如下：
 
在harlibrary中定义类及其成员函数和全局函数，并进行导出。
 
```ArkTS
<em>// harlibrary's src/main/ets/utils/Calc.ets</em>
export class Calc {
  public static staticAdd(a:number, b:number):number {
    let c = a + b;
    console.log('DynamicImport I am harlibrary in staticAdd, %d + %d = %d', a, b, c);
    return c;
  }
  public instanceAdd(a:number, b:number):number {
    let c = a + b;
    console.log('DynamicImport I am harlibrary in instanceAdd, %d + %d = %d', a, b, c);
    return c;
  }
}
export function addHarlibrary(a:number, b:number):number {
  let c = a + b;
  console.log('DynamicImport I am harlibrary in addHarlibrary, %d + %d = %d', a, b, c);
  return c;
}
```
 
```ArkTS
<em>// harlibrary's Index.ets</em>
export { Calc, addHarlibrary } from './src/main/ets/utils/Calc'
```
 
在HAP中添加对HARLibrary模块的依赖，动态导入HARLibrary模块，并调用其静态成员函数staticAdd()、实例成员函数instanceAdd()以及全局方法addHarlibrary()。
 
```json
<em>// HAP's oh-package.json5</em>
"dependencies": {
  "harlibrary": "file:../harlibrary"
},
```
 
```ArkTS
<em>// HAP's Index.ets</em>
import('harlibrary').then((ns:ESObject) => {
  ns.Calc.staticAdd(8, 9); <em> // Call static member functions staticAdd()</em>
  let calc:ESObject = new ns.Calc();  <em>// Instantiate class Calc</em>
  calc.instanceAdd(10, 11);  <em>// Call member functions instanceAdd()</em>
  ns.addHarlibrary(6, 7); <em> // Call global methods addHarlibrary()</em>

 <em> // Use string names of classes, member functions, and methods for reflection calls</em>
  let className = 'Calc';
  let methodName = 'instanceAdd';
  let staticMethod = 'staticAdd';
  let functionName = 'addHarlibrary';
  ns[className][staticMethod](12, 13);  <em>// Call static member functions staticAdd()</em>
  let calc1:ESObject = new ns[className](); <em> // Instantiate class Calc</em>
  calc1[methodName](14, 15); <em> // Call member functions instanceAdd()</em>
  ns[functionName](16, 17); <em> // Call global methods addHarlibrary()</em>
});
```
 
具体可以参考：[业务扩展场景介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-dynamic-import#业务扩展场景介绍)。
