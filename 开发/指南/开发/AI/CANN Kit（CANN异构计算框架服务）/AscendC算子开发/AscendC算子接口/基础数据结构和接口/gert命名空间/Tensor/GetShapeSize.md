# GetShapeSize

更新时间：2026-05-12 09:31:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getshapesize

## 函数功能

获取当前Tensor运行时的shape大小，即此Tensor中包含的元素的数量。

## 函数原型


```text
int64_t GetShapeSize() const
```


## 参数说明

不涉及。

## 返回值

返回执行时shape的大小。

## 约束说明

无

## 调用示例


```text
Tensor tensor{{{8, 3, 224, 224}, {16, 3, 224, 224}}, // shape
              {ge::FORMAT_ND, ge::FORMAT_FRACTAL_NZ, {}}, // format
              kOnDeviceHbm, // placement
              ge::DT_FLOAT16, // dt
              nullptr};
auto shape_size = tensor.GetShapeSize(); // 16*3*224*224
```
