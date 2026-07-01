# ArkTS是否支持多继承

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-95

接口支持多继承，类仅支持单继承。示例如下：
 
```text
class TestClassA {
  address: string = '';
}

class TestClassB {
  name: string = '';
}

<em>// report errors：Classes can only extend a single class.</em>
<em>// class TestClassC extends TestClassA, TestClassB {</em>
<em>// }</em>

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
