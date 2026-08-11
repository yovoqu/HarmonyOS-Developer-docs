# fast_solver_polynomial.h

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-solver-polynomial-8h
**支持设备：** Phone | PC/2in1 | Tablet

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet

多项式零点求解器相关数据结构及函数定义。
 
**引用文件：** <FASTKit/fast_solver_polynomial.h>
 
**库：** libfast_solver.so
 
**系统能力：** SystemCapability.FAST.Core
 
**起始版本：** 26.0.0
 
**相关模块：** [FAST](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet

  

#### 结构体

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| struct FAST_Poly | 定义稀疏格式多项式的数据结构。 |
 
 
  

#### 类型定义

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| typedef struct FAST_Poly FAST_Poly | 定义稀疏格式多项式的数据结构。 |
 
 
  

#### 函数

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| FAST_ErrorCode HMS_FAST_PolyRoot_ComputeRoots (const FAST_Poly *poly, const size_t maxRootCount, double *root, size_t *rootCount) | 计算多项式的给定数量的实根。 |
| FAST_ErrorCode HMS_FAST_PolyRoot_ComputeSingle (const FAST_Poly *poly, double *root) | 计算多项式的单个主导(绝对值最大)实根。 |
| FAST_ErrorCode HMS_FAST_PolyRoot_ComputeRootIntervals (const FAST_Poly *poly, const size_t maxRootCount, double *leftBoundary, double *rightBoundary, size_t *rootCount) | 计算多项式给定数量实根的隔离区间。 |
