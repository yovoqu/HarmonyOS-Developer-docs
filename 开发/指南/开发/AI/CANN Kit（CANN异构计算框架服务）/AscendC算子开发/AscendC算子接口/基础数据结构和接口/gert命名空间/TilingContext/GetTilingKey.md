# GetTilingKey

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-gettilingkey

## 函数功能

获取tiling key。

## 函数原型


```text
uint64_t GetTilingKey() const;
```


## 参数说明

无

## 返回值

返回tiling key。

## 约束说明

无

## 调用示例


```text
ge::graphStatus Tiling4XXX(TilingContext* context) {
  auto tiling_key = context->GetTilingKey();
  // ...
}
```
