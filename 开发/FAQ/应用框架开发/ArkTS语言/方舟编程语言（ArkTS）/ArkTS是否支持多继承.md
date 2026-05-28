# ArkTS是否支持多继承

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-95

接口支持多继承，类仅支持单继承。示例如下：
 
```ArkTS
class TestClassA {
  address: string = '';
}

class TestClassB {
  name: string = '';
}

// report errors：Classes can only extend a single class.
// class TestClassC extends TestClassA, TestClassB {
// }

interface AreaSize {
  calculateAreaSize(): number;
}

interface Cal {
  Sub(a: number, b: number): number;
}

interface Area extends AreaSize, Cal {
  areaName: string;
  length: number;
  width: number;
}
```
