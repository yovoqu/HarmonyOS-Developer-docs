# GetWorkspaceSizes

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getworkspacesizes

## 函数功能

获取workspace sizes指针。

## 函数原型


```text
size_t *GetWorkspaceSizes(const size_t workspace_count);
```


## 参数说明


| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| workspace_count | 输入 | workspace的个数，传入的workspace个数不可以超过编译时指定的最大workspace个数。 |


## 返回值

workspace sizes指针。

## 约束说明

传入的workspace个数不可以超过编译时指定的最大workspace个数。 当前Kirin9020支持的最大的workspace是8个。 当前KirinX90支持的最大的workspace是8个。

## 调用示例


```text
ge::graphStatus Tiling4XXX(TilingContext* context) {
  auto ws = context->GetWorkspaceSizes(5);
  // ...
}
```
