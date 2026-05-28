# MutableData

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-continuousvector-mutabledata

#### 函数功能

获取首个元素的指针地址，[GetData(), reinterpret_cast<T *>(GetData()) + GetSize()]中的数据即为当前容器中保存的数据。
 
  

#### 函数原型

```text
void *MutableData()
```
 
  

#### 参数说明

无
 
  

#### 返回值

首个元素的指针地址。
 
  

#### 约束说明

无
 
  

#### 调用示例

```text
size_t capacity = 100U;
auto cv_holder = ContinuousVector::Create<int64_t>(capacity);
auto cv = reinterpret_cast<ContinuousVector *>(cv_holder.get());
auto cap = cv->MutableData();
```
