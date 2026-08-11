# 使用PolyRoot求解多项式根

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fast-polynomial-root

多项式零点求解器（Polynomial Root Solver）用于计算一元多项式的实数根。其接收稀疏格式的多项式描述作为输入进行零点求解，适用于计算机辅助设计、信号处理、控制理论等需要高精度多项式根计算的场景。

其相关定义如下：多项式
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/PU95F4QyQGuBZaFJriLW7Q/zh-cn_image_0000002668461332.png?HW-CC-KV=V1&HW-CC-Date=20260811T005948Z&HW-CC-Expire=86400&HW-CC-Sign=C263130C408EFFA42ED721DB54160166871F0BA09B91A8BAC465BE36F8B15ABF)
由稀疏格式的FAST_Poly结构体描述，其中coeff数组存储各项系数，pow数组存储对应指数，且需按指数升序排列。例如多项式
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/F8L51Vg0RH2e6anwjHTFlw/zh-cn_image_0000002698221211.png?HW-CC-KV=V1&HW-CC-Date=20260811T005948Z&HW-CC-Expire=86400&HW-CC-Sign=3E2C3DA6F792B061BA66C28E01635A04BB0E2201FA73539DADEAAB8E047799C9)
可表示为coeff={1, -2, 3}，pow={0, 1, 2}。


#### 接口说明

具体API说明详见[接口文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast)。

| 名称 | 描述 |
| --- | --- |
| FAST_ErrorCode HMS_FAST_PolyRoot_ComputeRoots (const FAST_Poly *poly, const size_t maxRootCount, double *root, size_t *rootCount) | 计算多项式的给定数量的实根。 |
| FAST_ErrorCode HMS_FAST_PolyRoot_ComputeSingle (const FAST_Poly *poly, double *root) | 计算多项式的单个主导(绝对值最大)实根。 |
| FAST_ErrorCode HMS_FAST_PolyRoot_ComputeRootIntervals (const FAST_Poly *poly, const size_t maxRootCount, double *leftBoundary, double *rightBoundary, size_t *rootCount) | 计算多项式给定数量实根的隔离区间，输出每个实根的左右边界。 |




#### 开发步骤
1. 在CMake脚本中链接相关动态库。

  
```text
find_library(
    lib_fast_solver
    NAMES fast_solver
)
target_link_libraries(entry PRIVATE ${lib_fast_solver})
```

2. 构造FAST_Poly结构体，填充系数数组coeff和指数数组pow（需按指数升序排列）。
3. 调用API(HMS_FAST_PolyRoot_ComputeRoots)计算多项式的根。

```text
#include <cstdio>
#include <cstdlib>
#include "FASTKit/fast_solver_polynomial.h"

int main() {
    // 构造多项式 f(x) = x^2 - 3x + 2 = (x-1)(x-2)，根为 1.0 和 2.0
    // 系数数组：[常数项, 一次项系数, 二次项系数]
    double coeff[] = {2.0, -3.0, 1.0};
    // 指数数组：[对应项的指数]
    uint32_t pow[] = {0, 1, 2};
    size_t length = 3;

    // 初始化FAST_Poly结构体
    FAST_Poly poly;
    poly.coeff = coeff;
    poly.pow = pow;
    poly.length = length;

    // 定义存储根的数组和根的数量
    double roots[2];
    size_t rootCount = 0;
    FAST_ErrorCode ret;

    // 调用API计算多项式的根
    ret = HMS_FAST_PolyRoot_ComputeRoots(&poly, 2, roots, &rootCount);
    if (ret != FAST_ERROR_CODE_SUCCESS) {
        printf("Failed to compute roots: %d\n", ret);
        return ret;
    }

    printf("Found %zu roots:\n", rootCount);
    for (size_t i = 0; i < rootCount; ++i) {
        printf("  root[%zu] = %f\n", i, roots[i]);
    }

    /*
     * Found 2 roots:
     *   root[0] = 1.000000
     *   root[1] = 2.000000
     */

    printf("ret = %d\n", ret);
    return 0;
}
```



#### 注意事项
1. 构造FAST_Poly结构体，填充系数数组coeff和指数数组pow（需按指数升序排列）。
2. 若pow数组未按指数升序排列，则函数将返回错误码FAST_ERROR_CODE_ILLEGAL_INPUT，表示输入参数非法。
