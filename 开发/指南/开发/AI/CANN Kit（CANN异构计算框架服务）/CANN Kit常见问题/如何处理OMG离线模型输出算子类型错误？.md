# 如何处理OMG离线模型输出算子类型错误？

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-faqs-4

Caffe网络中具有相同类型名但计算功能不同的层。比如DetectionOutput层，需要使用算子映射指明为FSRDetectionOutput、SSDDetectionOutput等检测算子类型，否则OMG生成离线模型会执行失败。为了避免出现错误，以下两种方案二选一即可。
 
- 方案1：可以在OMG命令中加入--op_name_map参数，参考[OMG参数](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-overall-parameter)中op_name_map参数设置。
- 方案2：可以在原始网络proto模型文件中将输出算子类型指定为SSDDetectionOutput等算子类型，如下图所示。

  **图1** 输出算子类型修改前（左）和修改后（右）

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/sOBB9uA6ThygLifMQ8-iZA/zh-cn_image_0000002611835221.png?HW-CC-KV=V1&HW-CC-Date=20260528T030039Z&HW-CC-Expire=86400&HW-CC-Sign=F3103C39373368F16498A99C0DA2158AB94262BDCC34E3362FFEA07EB97BD648)
