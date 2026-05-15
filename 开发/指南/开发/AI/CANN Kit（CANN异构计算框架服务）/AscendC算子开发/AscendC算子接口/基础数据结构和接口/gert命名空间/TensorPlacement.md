# TensorPlacement

更新时间：2026-05-12 09:31:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensorplacement

```text
enum TensorPlacement {
    kOnDeviceHbm, // < Tensor位于Device上的HBM内存
    kOnHost, // < Tensor位于Host
    kFollowing, // < Tensor位于Host，且数据紧跟在结构体后面
    kOnDeviceP2p, // < Tensor位于Device上的P2p内存，指的是HBM透到PCIE BAR空间上，可以让NPU跨PCIE能访问的地址空间
    kTensorPlacementEnd
};
```
