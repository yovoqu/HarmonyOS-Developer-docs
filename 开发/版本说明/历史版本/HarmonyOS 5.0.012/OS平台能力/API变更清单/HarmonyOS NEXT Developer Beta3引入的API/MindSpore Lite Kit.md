# MindSpore Lite Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mindsporelitekit-b035

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API模型切换 | 类名：Context； API声明：target?: string[]; 差异内容：NA | 类名：Context； API声明：target?: string[]; 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：Context； API声明：cpu?: CpuDevice; 差异内容：NA | 类名：Context； API声明：cpu?: CpuDevice; 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：Context； API声明：nnrt?: NNRTDevice; 差异内容：NA | 类名：Context； API声明：nnrt?: NNRTDevice; 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：CpuDevice； API声明：threadNum?: number; 差异内容：NA | 类名：CpuDevice； API声明：threadNum?: number; 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：CpuDevice； API声明：threadAffinityMode?: ThreadAffinityMode; 差异内容：NA | 类名：CpuDevice； API声明：threadAffinityMode?: ThreadAffinityMode; 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：CpuDevice； API声明：threadAffinityCoreList?: number[]; 差异内容：NA | 类名：CpuDevice； API声明：threadAffinityCoreList?: number[]; 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：CpuDevice； API声明：precisionMode?: string; 差异内容：NA | 类名：CpuDevice； API声明：precisionMode?: string; 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：ThreadAffinityMode； API声明：NO_AFFINITIES = 0 差异内容：NA | 类名：ThreadAffinityMode； API声明：NO_AFFINITIES = 0 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：ThreadAffinityMode； API声明：BIG_CORES_FIRST = 1 差异内容：NA | 类名：ThreadAffinityMode； API声明：BIG_CORES_FIRST = 1 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：ThreadAffinityMode； API声明：LITTLE_CORES_FIRST = 2 差异内容：NA | 类名：ThreadAffinityMode； API声明：LITTLE_CORES_FIRST = 2 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：MSTensor； API声明：name: string; 差异内容：NA | 类名：MSTensor； API声明：name: string; 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：MSTensor； API声明：shape: number[]; 差异内容：NA | 类名：MSTensor； API声明：shape: number[]; 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：MSTensor； API声明：elementNum: number; 差异内容：NA | 类名：MSTensor； API声明：elementNum: number; 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：MSTensor； API声明：dataSize: number; 差异内容：NA | 类名：MSTensor； API声明：dataSize: number; 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：MSTensor； API声明：dtype: DataType; 差异内容：NA | 类名：MSTensor； API声明：dtype: DataType; 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：MSTensor； API声明：format: Format; 差异内容：NA | 类名：MSTensor； API声明：format: Format; 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：DataType； API声明：TYPE_UNKNOWN = 0 差异内容：NA | 类名：DataType； API声明：TYPE_UNKNOWN = 0 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：DataType； API声明：NUMBER_TYPE_INT8 = 32 差异内容：NA | 类名：DataType； API声明：NUMBER_TYPE_INT8 = 32 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：DataType； API声明：NUMBER_TYPE_INT16 = 33 差异内容：NA | 类名：DataType； API声明：NUMBER_TYPE_INT16 = 33 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：DataType； API声明：NUMBER_TYPE_INT32 = 34 差异内容：NA | 类名：DataType； API声明：NUMBER_TYPE_INT32 = 34 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：DataType； API声明：NUMBER_TYPE_INT64 = 35 差异内容：NA | 类名：DataType； API声明：NUMBER_TYPE_INT64 = 35 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：DataType； API声明：NUMBER_TYPE_UINT8 = 37 差异内容：NA | 类名：DataType； API声明：NUMBER_TYPE_UINT8 = 37 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：DataType； API声明：NUMBER_TYPE_UINT16 = 38 差异内容：NA | 类名：DataType； API声明：NUMBER_TYPE_UINT16 = 38 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：DataType； API声明：NUMBER_TYPE_UINT32 = 39 差异内容：NA | 类名：DataType； API声明：NUMBER_TYPE_UINT32 = 39 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：DataType； API声明：NUMBER_TYPE_UINT64 = 40 差异内容：NA | 类名：DataType； API声明：NUMBER_TYPE_UINT64 = 40 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：DataType； API声明：NUMBER_TYPE_FLOAT16 = 42 差异内容：NA | 类名：DataType； API声明：NUMBER_TYPE_FLOAT16 = 42 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：DataType； API声明：NUMBER_TYPE_FLOAT32 = 43 差异内容：NA | 类名：DataType； API声明：NUMBER_TYPE_FLOAT32 = 43 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：DataType； API声明：NUMBER_TYPE_FLOAT64 = 44 差异内容：NA | 类名：DataType； API声明：NUMBER_TYPE_FLOAT64 = 44 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：Format； API声明：DEFAULT_FORMAT = -1 差异内容：NA | 类名：Format； API声明：DEFAULT_FORMAT = -1 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：Format； API声明：NCHW = 0 差异内容：NA | 类名：Format； API声明：NCHW = 0 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：Format； API声明：NHWC = 1 差异内容：NA | 类名：Format； API声明：NHWC = 1 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：Format； API声明：NHWC4 = 2 差异内容：NA | 类名：Format； API声明：NHWC4 = 2 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：Format； API声明：HWKC = 3 差异内容：NA | 类名：Format； API声明：HWKC = 3 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：Format； API声明：HWCK = 4 差异内容：NA | 类名：Format； API声明：HWCK = 4 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
| API模型切换 | 类名：Format； API声明：KCHW = 5 差异内容：NA | 类名：Format； API声明：KCHW = 5 差异内容：stagemodelonly | api/@ohos.ai.mindSporeLite.d.ts |
