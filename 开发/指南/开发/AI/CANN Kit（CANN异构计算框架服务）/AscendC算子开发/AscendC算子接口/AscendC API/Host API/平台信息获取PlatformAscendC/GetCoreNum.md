# GetCoreNum

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getcorenum

## 函数功能

获取当前硬件平台的核数。若AI Core的架构为Cube、Vector分离架构，返回AI Core上的Vector核数；非分离架构返回AI Core的核数。

## 函数原型


```text
uint32_t GetCoreNum(void) const;
```


## 参数说明

无

## 返回值

针对Kirin9020系列处理器，Cube、Vector分离架构，返回AI Core上的Vector核数。

## 约束说明

无

## 调用示例


```text
ge::graphStatus TilingXXX(gert::TilingContext* context) {
    auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());
    auto coreNum = ascendcPlatform.GetCoreNum();
    // ... 根据核数自行设计Tiling策略
    context->SetBlockDim(coreNum);
    return ret;
}
```
