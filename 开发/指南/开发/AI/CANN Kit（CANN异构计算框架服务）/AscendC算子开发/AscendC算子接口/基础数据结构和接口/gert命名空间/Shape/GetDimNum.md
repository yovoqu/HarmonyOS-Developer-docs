# GetDimNum

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getdimnum

##### 函数功能

获取dim_num。
 
  

##### 函数原型

```text
size_t GetDimNum() const
```
 
  

##### 参数说明

无
 
  

##### 返回值

获取dim_num，即Shape的长度。
 
  

##### 约束说明

无
 
  

##### 调用示例

```text
Shape shape0({3, 256, 256});
auto dim_num = shape0.GetDimNum(); // 3
```
