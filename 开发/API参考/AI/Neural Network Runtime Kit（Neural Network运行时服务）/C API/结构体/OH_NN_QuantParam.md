# OH_NN_QuantParam

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime-oh-nn-quantparam
**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
typedef struct OH_NN_QuantParam {...} OH_NN_QuantParam
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | TV

量化信息。
 
在量化的场景中，32位浮点型数据根据以下公式量化为定点数据：
 

![](assets/OH_NN_QuantParam/file-20260514165249318-0.png)

 
其中s和z是量化参数，在OH_NN_QuantParam中通过scale和zeroPoint保存，r是浮点数，q是量化后的结果，q_min是量化后下界，q_max是量化后的上界，计算方式如下：
 

![](assets/OH_NN_QuantParam/file-20260514165249318-1.png)

 

![](assets/OH_NN_QuantParam/file-20260514165249318-2.png)

 
clamp函数定义如下：
 

![](assets/OH_NN_QuantParam/file-20260514165249318-3.png)

 
**起始版本：** 9
 
**废弃版本：** 11
 
**替代接口：** [NN_QuantParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime-nn-quantparam)
 
**相关模块：** [NeuralNetworkRuntime](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime)
 
**所在头文件：** [neural_network_runtime_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| uint32_t quantCount | 指定numBits、scale和zeroPoint数组的长度。在per-layer量化的场景下，quantCount通常指定为1，即一个张量所有通道共享一套量化参数；在per-channel量化场景下，quantCount通常和张量通道数一致，每个通道使用自己的量化参数。 |
| const uint32_t *numBits | 量化位数。 |
| const double *scale | 指向量化公式中scale数据的指针。 |
| const int32_t *zeroPoint | 指向量化公式中zero point数据的指针。 |
