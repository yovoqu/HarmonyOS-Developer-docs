# GetCapacity

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getcapacity

#### 函数功能

获取本实例可容纳的最大tiling data长度。
 
  

#### 函数原型

```text
size_t GetCapacity() const;
```
 
  

#### 参数说明

无
 
  

#### 返回值

最大tiling data长度。
 
  

#### 约束说明

无
 
  

#### 调用示例

```text
auto td_buf = TilingData::CreateCap(100U);
auto td = reinterpret_cast<TilingData *>(td_buf.get());
size_t cap = td->GetCapacity(); // 100U
```
