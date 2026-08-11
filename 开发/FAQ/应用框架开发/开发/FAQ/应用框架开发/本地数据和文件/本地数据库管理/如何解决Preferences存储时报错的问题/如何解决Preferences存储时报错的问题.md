# 如何解决Preferences存储时报错的问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-55

#### 问题现象

Preferences存储json格式字符串时报错：
 
```text
Parameter error.The type of value must be less then 16 * 1024 * 1024 bytes.
```
 
 

#### 背景知识

Preferences的[运作机制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-persistence-by-preferences#运作机制)如下图所示，用户程序通过ArkTS接口读写对应的数据文件。开发者可以将持久化文件的内容加载到Preferences实例，每个文件唯一对应到一个Preferences实例，系统会通过静态容器将该实例存储在内存中，直到主动从内存中移除该实例或者删除该文件。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/zqD7lV3_TYuAPzgkhR0wnQ/zh-cn_image_0000002659258293.png?HW-CC-KV=V1&HW-CC-Date=20260811T005848Z&HW-CC-Expire=86400&HW-CC-Sign=B7163A37558A199D6CFDF1E5E59CD570E29D9444F48F1772A6BE08D8BA6AF1E9)

 
Preferences在使用过程中会存在以下[约束限制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-persistence-by-preferences#约束限制)：包括[通用限制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-persistence-by-preferences#首选项通用限制)、[XML模式约束限制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-persistence-by-preferences#xml模式约束限制)以及[GSKV模式约束限制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-persistence-by-preferences#gskv模式约束限制)。
 
 

#### 问题定位

根据[官网文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)提示，表明传入的参数错误。可能的原因：
 1. 强制参数未指定。
2. 参数类型不正确。
3. 参数校验失败。
 
 

#### 分析结论

通过报错信息可知传入的value超过了最大上限。如果Preferences的Value值为string类型，请使用UTF-8编码格式，可以为空，不为空时长度不超过16*1024*1024个字节。
 
 

#### 修改建议

根据分析结论中的限制，修改保存进Preferences的value值，防止超过最大长度。
