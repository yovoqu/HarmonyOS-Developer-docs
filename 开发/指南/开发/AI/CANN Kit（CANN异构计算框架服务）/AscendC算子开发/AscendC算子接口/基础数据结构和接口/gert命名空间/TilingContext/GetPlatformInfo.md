# GetPlatformInfo

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getplatforminfo

#### 函数功能

获取fe::PlatFormInfos指针。
 
  

#### 函数原型

```text
fe::PlatFormInfos *GetPlatformInfo() const
```
 
  

#### 参数说明

无
 
  

#### 返回值

fe::PlatFormInfos指针。
 
  

#### 约束说明

无
 
  

#### 调用示例

```text
ge::graphStatus Tiling4XXX(TilingContext* context) {
  auto platform_info = context->GetPlatformInfo();
  // ...
}
```
