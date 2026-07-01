# fast_collections_hashmap.h

更新时间：2026-06-27 10:02:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-collections-hashmap-8h

**支持设备：** Phone | PC/2in1 | Tablet

## fast_collections_hashmap.h
 
 

##### 概述

哈希表相关数据结构及函数定义。
 
**引用文件：** <FASTKit/fast_collections_hashmap.h>
 
**库：** libfast_collections.so
 
**系统能力：** SystemCapability.FAST.Core
 
**起始版本：** 26.0.0
 
**相关模块：** [FAST](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast)
 
  

##### 汇总

  

##### [h2]类型定义
 
| 名称 | 描述 |
| --- | --- |
| typedef void* FAST_HashmapHandle | 哈希表的句柄。 |
| typedef void* FAST_HashmapKeyPtr | 哈希表键指针。 |
| typedef void* FAST_HashmapValuePtr | 哈希表的值指针。 |
| typedef uint64_t(* HMS_FAST_Hashmap_HashFunc) (const FAST_HashmapKeyPtr key) | 自定义的哈希值计算函数。 |
| typedef int32_t(* HMS_FAST_Hashmap_KeyEqualFunc) (const FAST_HashmapKeyPtr leftKey, const FAST_HashmapKeyPtr rightKey) | 自定义的键比较函数。 |
| typedef int32_t(* HMS_FAST_Hashmap_HookFunc) (const FAST_HashmapKeyPtr key, FAST_HashmapValuePtr value, void* context) | 自定义的通用回调函数形式。 |
 
 
  

##### [h2]函数
 
| 名称 | 描述 |
| --- | --- |
| FAST_ErrorCode HMS_FAST_Hashmap_Create (FAST_HashmapHandle* handle, HMS_FAST_Hashmap_HashFunc hasher, HMS_FAST_Hashmap_KeyEqualFunc equaler) | 创建哈希表实例。 |
| void HMS_FAST_Hashmap_Destroy (FAST_HashmapHandle handle) | 销毁哈希表实例。 |
| FAST_ErrorCode HMS_FAST_Hashmap_Insert (FAST_HashmapHandle handle, const FAST_HashmapKeyPtr key, const FAST_HashmapValuePtr value, FAST_HashmapValuePtr* originValue) | 将给定的键值对插入哈希表中，如果键已经存在，则使用value覆写原有的值，并将原有值的地址保存在originValue中。 |
| FAST_ErrorCode HMS_FAST_Hashmap_Find (FAST_HashmapHandle handle, const FAST_HashmapKeyPtr key, FAST_HashmapValuePtr* value) | 检索与给定键关联的值，并将对应的值保存在value中。 |
| FAST_ErrorCode HMS_FAST_Hashmap_Erase (FAST_HashmapHandle handle, const FAST_HashmapKeyPtr key, FAST_HashmapKeyPtr* originKey, FAST_HashmapValuePtr* originValue) | 在给定哈希表中删除输入的键，并将键/值对应的地址保存在originKey和originValue中。 |
| FAST_ErrorCode HMS_FAST_Hashmap_TryInsert (FAST_HashmapHandle handle, const FAST_HashmapKeyPtr key, const FAST_HashmapValuePtr value) | 将给定的键值对插入哈希表中，如果键已经存在、则不做操作。 |
| size_t HMS_FAST_Hashmap_Size (FAST_HashmapHandle handle) | 返回哈希表中的元素个数。 |
| void HMS_FAST_Hashmap_Clear (FAST_HashmapHandle handle) | 从哈希表中删除所有元素。 |
| size_t HMS_FAST_Hashmap_EraseIf (FAST_HashmapHandle handle, HMS_FAST_Hashmap_HookFunc condFunc, void* condCtx, HMS_FAST_Hashmap_HookFunc freeFunc, void* freeCtx) | 删除哈希表中符合输入条件的所有元素，并使用自定义的方式释放其内存。 |
| void HMS_FAST_Hashmap_Traverse (FAST_HashmapHandle handle, HMS_FAST_Hashmap_HookFunc condFunc, void* condCtx, HMS_FAST_Hashmap_HookFunc workFunc, void* workCtx) | 遍历哈希表，将所有符合输入条件的键值对按开发者给定的方式修改。 |
