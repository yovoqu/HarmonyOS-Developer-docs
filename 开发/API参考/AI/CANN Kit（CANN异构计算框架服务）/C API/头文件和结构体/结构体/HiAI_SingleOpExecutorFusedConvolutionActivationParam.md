# HiAI_SingleOpExecutorFusedConvolutionActivationParam

更新时间：2026-05-14 10:06:22

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit-sopexec-fusedconv-actparam
**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
typedef struct HiAI_SingleOpExecutorFusedConvolutionActivationParam {...} HiAI_SingleOpExecutorFusedConvolutionActivationParam
```
  

##### 概述

[HMS_HiAISingleOpExecutor_CreateFusedConvolutionActivation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit#hms_hiaisingleopexecutor_createfusedconvolutionactivation)输入参数。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [CANN](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit)
 
**所在头文件：** [hiai_single_op.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit-hiai-single-op-8h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| HiAI_SingleOpOptions * options | 指向HiAI_SingleOpOptions对象的指针。该值不能为空指针，否则接口调用失败。 |
| HiAI_SingleOpDescriptor * convOpDesc | 指向卷积算子对应的HiAI_SingleOpDescriptor对象的指针。该值不能为空指针，否则接口调用失败。 |
| HiAI_SingleOpDescriptor * actOpDesc | 指向激活算子对应的HiAI_SingleOpDescriptor对象的指针。该值不能为空指针，否则接口调用失败。 |
| HiAI_SingleOpTensorDesc * input | 指向输入Tensor描述的指针。该值不能为空指针，否则接口调用失败。 |
| HiAI_SingleOpTensorDesc * output | 指向输出Tensor描述的指针。该值不能为空指针，否则接口调用失败。 |
| HiAI_SingleOpTensor * filter | 指向卷积核Tensor的指针。该值不能为空指针，否则接口调用失败。 |
| HiAI_SingleOpTensor * bias | 指向偏置Tensor的指针。如果卷积没有偏置，则该值可以是空指针。 |
 
 
  

##### 结构体成员变量说明

  

##### actOpDesc

```text
HiAI_SingleOpDescriptor* HiAI_SingleOpExecutorFusedConvolutionActivationParam::actOpDesc
```
 
**描述**
 
指向激活算子对应的[HiAI_SingleOpDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit#hiai_singleopdescriptor)对象的指针。该值不能为空指针，否则接口调用失败。
 
  

##### bias

```text
HiAI_SingleOpTensor* HiAI_SingleOpExecutorFusedConvolutionActivationParam::bias
```
 
**描述**
 
指向偏置Tensor的指针。如果卷积没有偏置，则该值可以是空指针。
 
  

##### convOpDesc

```text
HiAI_SingleOpDescriptor* HiAI_SingleOpExecutorFusedConvolutionActivationParam::convOpDesc
```
 
**描述**
 
指向卷积算子对应的[HiAI_SingleOpDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit#hiai_singleopdescriptor)对象的指针。该值不能为空指针，否则接口调用失败。
 
  

##### filter

```text
HiAI_SingleOpTensor* HiAI_SingleOpExecutorFusedConvolutionActivationParam::filter
```
 
**描述**
 
指向卷积核Tensor的指针。该值不能为空指针，否则接口调用失败。
 
  

##### input

```text
HiAI_SingleOpTensorDesc* HiAI_SingleOpExecutorFusedConvolutionActivationParam::input
```
 
**描述**
 
指向输入Tensor描述的指针。该值不能为空指针，否则接口调用失败。
 
  

##### options

```text
HiAI_SingleOpOptions* HiAI_SingleOpExecutorFusedConvolutionActivationParam::options
```
 
**描述**
 
指向[HiAI_SingleOpOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit#hiai_singleopoptions)对象的指针。该值不能为空指针，否则接口调用失败。
 
  

##### output

```text
HiAI_SingleOpTensorDesc* HiAI_SingleOpExecutorFusedConvolutionActivationParam::output
```
 
**描述**
 
指向输出Tensor描述的指针。该值不能为空指针，否则接口调用失败。
