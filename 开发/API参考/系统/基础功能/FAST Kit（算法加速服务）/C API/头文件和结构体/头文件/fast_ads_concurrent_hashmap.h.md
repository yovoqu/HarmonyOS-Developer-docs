# fast_ads_concurrent_hashmap.h

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-ads-concurrent-hashmap-8h
**支持设备：** Phone | PC/2in1 | Tablet

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet

并发哈希表相关数据结构及函数定义。
 
**引用文件：** <FASTKit/fast_ads_concurrent_hashmap.h>
 
**库：** libfast_ads.so
 
**系统能力：** SystemCapability.FAST.Core
 
**起始版本：** 6.1.1(24)
 
**相关模块：** [FAST](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet

  

##### 类型定义

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| typedef void * FAST_ConcurrentHashmapHandle | 并发哈希表句柄。 |
| typedef void * FAST_ConcurrentHashmapKeyPtr | 并发哈希表键指针 |
| typedef void * FAST_ConcurrentHashmapValuePtr | 并发哈希表的值指针 |
| typedef uint64_t (*HMS_FAST_ConcurrentHashmap_HashFunc) (const FAST_ConcurrentHashmapKeyPtr key) | 开发者自定义的哈希值计算函数 |
| typedef int32_t (*HMS_FAST_ConcurrentHashmap_KeyEqualFunc) (const FAST_ConcurrentHashmapKeyPtr leftKey, const FAST_ConcurrentHashmapKeyPtr rightKey) | 开发者自定义的键比较函数 |
| typedef int32_t (*HMS_FAST_ConcurrentHashmap_HookFunc) (const FAST_ConcurrentHashmapKeyPtr key, FAST_ConcurrentHashmapValuePtr value, void* context) | 开发者自定义的通用回调函数形式 |
 
 
  

##### 函数

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| FAST_ErrorCode HMS_FAST_ConcurrentHashmap_Create (FAST_ConcurrentHashmapHandle* handle, HMS_FAST_ConcurrentHashmap_HashFunc hasher, HMS_FAST_ConcurrentHashmap_KeyEqualFunc equaler, float maxLoadFac, size_t numShards) | 使用给定配置创建并发哈希表 |
| void HMS_FAST_ConcurrentHashmap_Destroy (FAST_ConcurrentHashmapHandle handle) | 销毁指定并发哈希表 |
| FAST_ErrorCode HMS_FAST_ConcurrentHashmap_Insert (FAST_ConcurrentHashmapHandle handle, const FAST_ConcurrentHashmapKeyPtr key, const FAST_ConcurrentHashmapValuePtr value, FAST_ConcurrentHashmapValuePtr* originValue) | 将给定的键值对插入并发哈希表中，如果键已经存在、则使用value覆写原有的值，并将对应值的地址保存在originValue中 |
| FAST_ErrorCode HMS_FAST_ConcurrentHashmap_Find (FAST_ConcurrentHashmapHandle handle, const FAST_ConcurrentHashmapKeyPtr key, FAST_ConcurrentHashmapValuePtr* value) | 在给定并发哈希表中查找输入的键，并将对应的值保存在value中 |
| FAST_ErrorCode HMS_FAST_ConcurrentHashmap_Erase (FAST_ConcurrentHashmapHandle handle, const FAST_ConcurrentHashmapKeyPtr key, FAST_ConcurrentHashmapKeyPtr* originKey, FAST_ConcurrentHashmapValuePtr* originValue) | 在给定哈希表中删除输入的键，并将键和值对应的地址分别保存在originKey和originValue中 |
| FAST_ErrorCode HMS_FAST_ConcurrentHashmap_TryInsert (FAST_ConcurrentHashmapHandle handle, const FAST_ConcurrentHashmapKeyPtr key, const FAST_ConcurrentHashmapValuePtr value) | 将给定的键值对插入并发哈希表中，如果键已经存在、则不做操作 |
| size_t HMS_FAST_ConcurrentHashmap_Size (FAST_ConcurrentHashmapHandle handle) | 返回给定哈希表当前的元素个数 |
| void HMS_FAST_ConcurrentHashmap_Clear (FAST_ConcurrentHashmapHandle handle) | 清空给定哈希表中维护的所有元素 |
| size_t HMS_FAST_ConcurrentHashmap_EraseIf (FAST_ConcurrentHashmapHandle handle, HMS_FAST_ConcurrentHashmap_HookFunc condFunc, void* condCtx, HMS_FAST_ConcurrentHashmap_HookFunc freeFunc, void* freeCtx) | 删除哈希表中符合开发者定义条件的所有元素，并使用开发者定义的方式释放其内存 |
| void HMS_FAST_ConcurrentHashmap_Traverse (FAST_ConcurrentHashmapHandle handle, HMS_FAST_ConcurrentHashmap_HookFunc condFunc, void* condCtx, HMS_FAST_ConcurrentHashmap_HookFunc workFunc, void* workCtx) | 遍历哈希表，将所有符合开发者输入条件的键值对按开发者给定的方式修改 |
