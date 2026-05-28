# GetTilingCond

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-gettilingcond

#### 函数功能

获取tiling cond。
 
  

#### 函数原型

```text
int32_t GetTilingCond() const;
```
 
  

#### 参数说明

无
 
  

#### 返回值

tiling cond:
 
若返回值大于等于0，代表此tiling cond为有效的tiling cond。
 
若返回值为-1，代表此tiling cond为无效的tiling cond。
 
  

#### 约束说明

无
 
  

#### 调用示例

```text
ge::graphStatus Tiling4XXX(TilingContext* context) {
  auto tiling_cond = context->GetTilingCond();
  // ...
}
```
