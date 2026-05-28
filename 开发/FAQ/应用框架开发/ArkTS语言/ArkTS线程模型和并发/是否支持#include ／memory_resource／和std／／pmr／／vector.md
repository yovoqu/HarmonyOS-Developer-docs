# 是否支持#include <memory_resource>和std::pmr::vector

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-149

# 是否支持#include &lt;memory_resource&gt;和std::pmr::vector
 

暂时不支持。
 
C++从C++17标准开始正式支持 &lt;memory_resource&gt; 和std::pmr::vector等“多态内存资源”容器，开发者可以直接在sdk下查询到当前llvm版本是15.0.4，暂时不支持部分C++17高级特性。
 
Windows：
 

![](assets/是否支持#include%20／memory_resource／和std／／pmr／／vector/file-20260515125704109-0.png)

 
Mac：
 

![](assets/是否支持#include%20／memory_resource／和std／／pmr／／vector/file-20260515125704109-1.png)
