# SetMin

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setmin

#### 函数功能

设置最小的T对象指针。
 
  

#### 函数原型

```text
void SetMin(T *min)
```
 
  

#### 参数说明
 
| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| min | 输入 | 最小的T对象指针。 |
 
 
  

#### 返回值

无
 
  

#### 约束说明

无
 
  

#### 调用示例

```text
Range<int> range;
int min = -1;
range.SetMin(&min);
```
