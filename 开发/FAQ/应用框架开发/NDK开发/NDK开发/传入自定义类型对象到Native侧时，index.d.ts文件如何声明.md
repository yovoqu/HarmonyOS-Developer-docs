# 传入自定义类型对象到Native侧时，index.d.ts文件如何声明

更新时间：2026-03-17 00:56:02

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-61

此处以testCb为例
 
```ArkTS
class testCb {
  testNum: number = 0;
  testString: string = "";
}
```
 
方法一：
 
在index.d.ts文件中使用object类型进行声明。
 
```ts
export const modifyObject: (a: object) => object;
```
 
方法二：
 
创建xx.ts文件，并在该文件中导出类。然后在index.d.ts文件中导入并使用该类。
 
test.ts 导出类声明。
 
```ts
export class testCa {
  testNum: number = 0;
  testString: string = "";
}
```
 
在index.d.ts中导入并使用。
 
```ts
import { testCa } from "../../../ets/pages/interface/CustomObject"
export const test1: (a: testCa) => void;
```
