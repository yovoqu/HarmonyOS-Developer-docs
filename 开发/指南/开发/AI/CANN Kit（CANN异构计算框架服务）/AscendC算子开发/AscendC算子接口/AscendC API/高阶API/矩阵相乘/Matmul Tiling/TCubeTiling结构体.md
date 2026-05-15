# TCubeTiling结构体

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tcubetiling-structure

TCubeTiling结构体包含Matmul Tiling切分算法的相关参数，被传递给Matmul kernel侧，用于Matmul的切块、搬运和计算过程等。TCubeTiling结构体的参数说明见表1。

 **表1** TCubeTiling结构说明


| 参数名称 | 数据类型 | 说明 |
| --- | --- | --- |
| usedCoreNum | int | 使用的AI处理器核数，请根据实际情况设置。取值范围为：[1, AI处理器最大核数]。该参数与shape相关参数的关系为：usedCoreNum = (M / singleCoreM) * (N / singleCoreN)。 |
| M, N, Ka, Kb | int | A、B、C矩阵原始输入的shape大小，以元素为单位。M, Ka为A矩阵原始输入的Shape, Kb, N为B矩阵原始输入的Shape。 - 大小约束   - 若A矩阵为ND格式，不进行转置时，Ka取值范围为[1, 65535]，M无大小限制；进行转置时，M取值范围为[1, 65535]，Ka无大小限制。   - 若B矩阵为ND格式，不进行转置时，N取值范围为[1, 65535]，Kb无大小限制；进行转置时，Kb取值范围为[1, 65535]，N无大小限制。 - 对齐约束   - 若A矩阵以NZ格式输入，则M需要以16个元素对齐，K需要以C0_size对齐；若B矩阵以NZ格式输入，则K需要以C0_size对齐，N需要以16个元素对齐。   - 若A、B矩阵为ND格式，无对齐约束。 说明： NZ格式的输入，half/bfloat16_t数据类型的C0_size为16，float数据类型的C0_size为8，int8_t数据类型的C0_size为32，int4_t数据类型的C0_size为64。 |
| singleCoreM, singleCoreN, singleCoreK | int | A、B、C矩阵单核内shape大小，以元素为单位。 singleCoreK = K，多核处理时不对K进行切分；singleCoreM <= M；singleCoreN <= N。 若A矩阵以NZ格式输入，则singleCoreM需要以16个元素对齐，singleCoreK需要以C0_size * fractal_num对齐；若B矩阵以NZ格式输入，则singleCoreK需要以C0_size * fractal_num对齐，singleCoreN需要以16个元素对齐。 NZ格式的输入，half/bfloat16_t数据类型的C0_size为16，float数据类型的C0_size为8，int8_t数据类型的C0_size为32，int4_t数据类型的C0_size为64。 |
| baseM, baseN, baseK | int | A、B、C矩阵参与一次矩阵乘指令的shape大小，以元素为单位。 - baseM * baseN * sizeof(l0c_dtype) <= L0C_size，其中l0c_dtype为int32_t或者float数据类型 - baseM * baseK * sizeof(Input_dtype) <= L0A_size - baseK * baseN * sizeof(Input_dtype) <= L0B_size A、B、C矩阵参与一次矩阵乘的shape大小需要按分形对齐，其含义请参考Mmad中的数据格式说明。 |
| depthA1, depthB1 | int | A、B矩阵片全载A2/B2的份数，depthA1为baseM * baseK的整数倍，depthB1为baseN * baseK的整数倍。取值大于0。 |
| stepM， stepN，stepKa，stepKb | int | stepM为左矩阵在A1中缓存的bufferM方向上baseM的倍数。 stepN为右矩阵在B1中缓存的bufferN方向上baseN的倍数。 stepKa为左矩阵在A1中缓存的bufferKa方向上baseK的倍数。 stepKb为右矩阵在B1中缓存的bufferKb方向上baseK的倍数。 取值大于0。 |
| isBias | int | 是否使能Bias，0代表不使能Bias，1代表使能Bias。 |
| transLength | int | max(A1Length, B1Length, C1Length, BiasLength)。其中，A1Length, B1Length, C1Length, BiasLength分别表示A/B/C/Bias矩阵在计算过程中需要临时占用的UB空间大小。 |
| iterateOrder | int | 一次Iterate计算出[baseM, baseN]大小的C矩阵分片，Iterate完成后，Matmul会自动偏移下一次Iterate输出的C矩阵位置，iterateOrder表示自动偏移的顺序。参数取值如下。 - 0：先往M轴方向偏移再往N轴方向偏移 - 1：先往N轴方向偏移再往M轴方向偏移 |
| dbL0A, dbL0B, dbL0C | int | MTE1是否开启double buffer。 dbL0A：左矩阵MTE1是否开启double buffer。dbL0B：右矩阵MTE1是否开启double buffer；dbL0C：Mmad是否开启double buffer。参数取值如下。 - 1：不开启double buffer - 2：开启double buffer |
| shareMode | int | 该参数预留，开发者无需关注。 |
| shareL1Size | int | 该参数预留，开发者无需关注。 |
| shareL0CSize | int | 该参数预留，开发者无需关注。 |
| shareUbSize | int | 该参数预留，开发者无需关注。 |
| batchM | int | 该参数预留，开发者无需关注。 |
| batchN | int | 该参数预留，开发者无需关注。 |
| singleBatchM | int | 该参数预留，开发者无需关注。 |
| singleBatchN | int | 该参数预留，开发者无需关注。 |

开发者通过调用GetTiling接口获取TCubeTiling结构体，具体流程请参考[使用说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-matmul-tiling-usage-description)。若开发者需要修改调整Tiling，请参考如下TCubeTiling参数约束和性能调优推荐取值，进行参数的设置。


- base块推荐(baseM, baseN, baseK)：(128, 256, 64)
- dbL0A / dbL0B = 2
- depthA1 / (stepM * stepKa) = 2
- depthB1 / (stepN * stepKb) = 2
- 优先设置参数stepKa/stepKb，使得K方向全载，再考虑M方向或N方向全载。
