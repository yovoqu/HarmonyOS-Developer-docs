# GetWorkspaceNum

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getworkspacenum

#### 函数功能

获取workspace个数。
 
  

#### 函数原型

```text
size_t GetWorkspaceNum() const;
```
 
  

#### 参数说明

无
 
  

#### 返回值

workspace的个数。
 
  

#### 约束说明

无
 
  

#### 调用示例

```text
ge::graphStatus Tiling4XXX(TilingContext* context) {
  auto ws_num = context->GetWorkspaceNum();
  // ...
}
```
