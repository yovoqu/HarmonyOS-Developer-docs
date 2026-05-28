# OH_NN_Tensor

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime-oh-nn-tensor
**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
typedef struct OH_NN_Tensor {...} OH_NN_Tensor
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | TV

张量结构体。
 
通常用于构造模型图中的数据节点和算子参数，在构造张量时需要明确数据类型、维数、维度信息和量化信息。
 
**起始版本：** 9
 
**废弃版本：** 11
 
**替代接口：** [NN_TensorDesc](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime-nn-tensordesc)
 
**相关模块：** [NeuralNetworkRuntime](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime)
 
**所在头文件：** [neural_network_runtime_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| OH_NN_DataType dataType | 指定张量的数据类型，要求从OH_NN_DataType枚举类型中取值。 |
| uint32_t dimensionCount | 指定张量的维数。 |
| const int32_t *dimensions | 指定张量的维度信息（形状）。 |
| const OH_NN_QuantParam *quantParam | 指定张量的量化信息，数据类型要求为OH_NN_QuantParam。 |
| OH_NN_TensorType type | 指定张量的类型。type的取值和张量的用途相关，当张量用作模型的输入或输出，则要求将type设置为OH_NN_TENSOR；当张量用作算子参数，则要求从OH_NN_TensorType中选择除OH_NN_TENSOR以外的枚举值。 |
