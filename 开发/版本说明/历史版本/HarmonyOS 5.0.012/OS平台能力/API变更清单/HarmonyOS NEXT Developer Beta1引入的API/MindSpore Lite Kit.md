# MindSpore Lite Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mindsporelitekit-hdc

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明： declare namespace mindSporeLite 差异内容： declare namespace mindSporeLite | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：mindSporeLite； API声明：function loadModelFromFile(model: string, context?: Context): Promise&lt;Model&gt;; 差异内容：function loadModelFromFile(model: string, context?: Context): Promise&lt;Model&gt;; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：mindSporeLite； API声明：function loadModelFromFile(model: string, callback: Callback&lt;Model&gt;): void; 差异内容：function loadModelFromFile(model: string, callback: Callback&lt;Model&gt;): void; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：mindSporeLite； API声明：function loadModelFromFile(model: string, context: Context, callback: Callback&lt;Model&gt;): void; 差异内容：function loadModelFromFile(model: string, context: Context, callback: Callback&lt;Model&gt;): void; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：mindSporeLite； API声明：function loadModelFromBuffer(model: ArrayBuffer, context?: Context): Promise&lt;Model&gt;; 差异内容：function loadModelFromBuffer(model: ArrayBuffer, context?: Context): Promise&lt;Model&gt;; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：mindSporeLite； API声明：function loadModelFromBuffer(model: ArrayBuffer, callback: Callback&lt;Model&gt;): void; 差异内容：function loadModelFromBuffer(model: ArrayBuffer, callback: Callback&lt;Model&gt;): void; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：mindSporeLite； API声明：function loadModelFromBuffer(model: ArrayBuffer, context: Context, callback: Callback&lt;Model&gt;): void; 差异内容：function loadModelFromBuffer(model: ArrayBuffer, context: Context, callback: Callback&lt;Model&gt;): void; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：mindSporeLite； API声明：function loadModelFromFd(model: number, context?: Context): Promise&lt;Model&gt;; 差异内容：function loadModelFromFd(model: number, context?: Context): Promise&lt;Model&gt;; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：mindSporeLite； API声明：function loadModelFromFd(model: number, callback: Callback&lt;Model&gt;): void; 差异内容：function loadModelFromFd(model: number, callback: Callback&lt;Model&gt;): void; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：mindSporeLite； API声明：function loadModelFromFd(model: number, context: Context, callback: Callback&lt;Model&gt;): void; 差异内容：function loadModelFromFd(model: number, context: Context, callback: Callback&lt;Model&gt;): void; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：mindSporeLite； API声明：function loadTrainModelFromFile(model: string, trainCfg?: TrainCfg, context?: Context): Promise&lt;Model&gt;; 差异内容：function loadTrainModelFromFile(model: string, trainCfg?: TrainCfg, context?: Context): Promise&lt;Model&gt;; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：mindSporeLite； API声明：function loadTrainModelFromBuffer(model: ArrayBuffer, trainCfg?: TrainCfg, context?: Context): Promise&lt;Model&gt;; 差异内容：function loadTrainModelFromBuffer(model: ArrayBuffer, trainCfg?: TrainCfg, context?: Context): Promise&lt;Model&gt;; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：mindSporeLite； API声明：function loadTrainModelFromFd(model: number, trainCfg?: TrainCfg, context?: Context): Promise&lt;Model&gt;; 差异内容：function loadTrainModelFromFd(model: number, trainCfg?: TrainCfg, context?: Context): Promise&lt;Model&gt;; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：mindSporeLite； API声明： interface Model 差异内容： interface Model | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：Model； API声明：learningRate?: number; 差异内容：learningRate?: number; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：Model； API声明：trainMode?: boolean; 差异内容：trainMode?: boolean; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：Model； API声明：getInputs(): MSTensor[]; 差异内容：getInputs(): MSTensor[]; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：Model； API声明：predict(inputs: MSTensor[], callback: Callback<MSTensor[]>): void; 差异内容：predict(inputs: MSTensor[], callback: Callback<MSTensor[]>): void; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：Model； API声明：predict(inputs: MSTensor[]): Promise<MSTensor[]>; 差异内容：predict(inputs: MSTensor[]): Promise<MSTensor[]>; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：Model； API声明：resize(inputs: MSTensor[], dims: Array<Array&lt;number&gt;>): boolean; 差异内容：resize(inputs: MSTensor[], dims: Array<Array&lt;number&gt;>): boolean; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：Model； API声明：runStep(inputs: MSTensor[]): boolean; 差异内容：runStep(inputs: MSTensor[]): boolean; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：Model； API声明：getWeights(): MSTensor[]; 差异内容：getWeights(): MSTensor[]; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：Model； API声明：updateWeights(weights: MSTensor[]): boolean; 差异内容：updateWeights(weights: MSTensor[]): boolean; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：Model； API声明：setupVirtualBatch(virtualBatchMultiplier: number, lr: number, momentum: number): boolean; 差异内容：setupVirtualBatch(virtualBatchMultiplier: number, lr: number, momentum: number): boolean; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：Model； API声明：exportModel(modelFile: string, quantizationType?: QuantizationType, exportInferenceOnly?: boolean, outputTensorName?: string[]): boolean; 差异内容：exportModel(modelFile: string, quantizationType?: QuantizationType, exportInferenceOnly?: boolean, outputTensorName?: string[]): boolean; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：Model； API声明：exportWeightsCollaborateWithMicro(weightFile: string, isInference?: boolean, enableFp16?: boolean, changeableWeightsName?: string[]): boolean; 差异内容：exportWeightsCollaborateWithMicro(weightFile: string, isInference?: boolean, enableFp16?: boolean, changeableWeightsName?: string[]): boolean; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：mindSporeLite； API声明： export enum QuantizationType 差异内容： export enum QuantizationType | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：QuantizationType； API声明：NO_QUANT = 0 差异内容：NO_QUANT = 0 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：QuantizationType； API声明：WEIGHT_QUANT = 1 差异内容：WEIGHT_QUANT = 1 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：QuantizationType； API声明：FULL_QUANT = 2 差异内容：FULL_QUANT = 2 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：mindSporeLite； API声明： export enum OptimizationLevel 差异内容： export enum OptimizationLevel | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：OptimizationLevel； API声明：O0 = 0 差异内容：O0 = 0 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：OptimizationLevel； API声明：O2 = 2 差异内容：O2 = 2 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：OptimizationLevel； API声明：O3 = 3 差异内容：O3 = 3 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：OptimizationLevel； API声明：AUTO = 4 差异内容：AUTO = 4 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：mindSporeLite； API声明： interface TrainCfg 差异内容： interface TrainCfg | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：TrainCfg； API声明：lossName?: string[]; 差异内容：lossName?: string[]; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：TrainCfg； API声明：optimizationLevel?: OptimizationLevel; 差异内容：optimizationLevel?: OptimizationLevel; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：mindSporeLite； API声明： interface Context 差异内容： interface Context | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：Context； API声明：target?: string[]; 差异内容：target?: string[]; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：Context； API声明：cpu?: CpuDevice; 差异内容：cpu?: CpuDevice; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：Context； API声明：nnrt?: NNRTDevice; 差异内容：nnrt?: NNRTDevice; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：mindSporeLite； API声明： interface CpuDevice 差异内容： interface CpuDevice | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：CpuDevice； API声明：threadNum?: number; 差异内容：threadNum?: number; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：CpuDevice； API声明：threadAffinityMode?: ThreadAffinityMode; 差异内容：threadAffinityMode?: ThreadAffinityMode; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：CpuDevice； API声明：threadAffinityCoreList?: number[]; 差异内容：threadAffinityCoreList?: number[]; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：CpuDevice； API声明：precisionMode?: string; 差异内容：precisionMode?: string; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：mindSporeLite； API声明： export enum PerformanceMode 差异内容： export enum PerformanceMode | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：PerformanceMode； API声明：PERFORMANCE_NONE = 0 差异内容：PERFORMANCE_NONE = 0 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：PerformanceMode； API声明：PERFORMANCE_LOW = 1 差异内容：PERFORMANCE_LOW = 1 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：PerformanceMode； API声明：PERFORMANCE_MEDIUM = 2 差异内容：PERFORMANCE_MEDIUM = 2 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：PerformanceMode； API声明：PERFORMANCE_HIGH = 3 差异内容：PERFORMANCE_HIGH = 3 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：PerformanceMode； API声明：PERFORMANCE_EXTREME = 4 差异内容：PERFORMANCE_EXTREME = 4 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：mindSporeLite； API声明： export enum Priority 差异内容： export enum Priority | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：Priority； API声明：PRIORITY_NONE = 0 差异内容：PRIORITY_NONE = 0 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：Priority； API声明：PRIORITY_LOW = 1 差异内容：PRIORITY_LOW = 1 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：Priority； API声明：PRIORITY_MEDIUM = 2 差异内容：PRIORITY_MEDIUM = 2 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：Priority； API声明：PRIORITY_HIGH = 3 差异内容：PRIORITY_HIGH = 3 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：mindSporeLite； API声明： interface Extension 差异内容： interface Extension | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：Extension； API声明：name: string; 差异内容：name: string; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：Extension； API声明：value: ArrayBuffer; 差异内容：value: ArrayBuffer; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：mindSporeLite； API声明： export enum NNRTDeviceType 差异内容： export enum NNRTDeviceType | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：NNRTDeviceType； API声明：NNRTDEVICE_OTHERS = 0 差异内容：NNRTDEVICE_OTHERS = 0 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：NNRTDeviceType； API声明：NNRTDEVICE_CPU = 1 差异内容：NNRTDEVICE_CPU = 1 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：NNRTDeviceType； API声明：NNRTDEVICE_GPU = 2 差异内容：NNRTDEVICE_GPU = 2 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：NNRTDeviceType； API声明：NNRTDEVICE_ACCELERATOR = 3 差异内容：NNRTDEVICE_ACCELERATOR = 3 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：mindSporeLite； API声明： interface NNRTDeviceDescription 差异内容： interface NNRTDeviceDescription | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：NNRTDeviceDescription； API声明：deviceID(): bigint; 差异内容：deviceID(): bigint; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：NNRTDeviceDescription； API声明：deviceType(): NNRTDeviceType; 差异内容：deviceType(): NNRTDeviceType; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：NNRTDeviceDescription； API声明：deviceName(): string; 差异内容：deviceName(): string; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：mindSporeLite； API声明：function getAllNNRTDeviceDescriptions(): NNRTDeviceDescription[]; 差异内容：function getAllNNRTDeviceDescriptions(): NNRTDeviceDescription[]; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：mindSporeLite； API声明： interface NNRTDevice 差异内容： interface NNRTDevice | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：NNRTDevice； API声明：deviceID?: bigint; 差异内容：deviceID?: bigint; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：NNRTDevice； API声明：performanceMode?: PerformanceMode; 差异内容：performanceMode?: PerformanceMode; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：NNRTDevice； API声明：priority?: Priority; 差异内容：priority?: Priority; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：NNRTDevice； API声明：extensions?: Extension[]; 差异内容：extensions?: Extension[]; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：mindSporeLite； API声明： export enum ThreadAffinityMode 差异内容： export enum ThreadAffinityMode | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：ThreadAffinityMode； API声明：NO_AFFINITIES = 0 差异内容：NO_AFFINITIES = 0 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：ThreadAffinityMode； API声明：BIG_CORES_FIRST = 1 差异内容：BIG_CORES_FIRST = 1 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：ThreadAffinityMode； API声明：LITTLE_CORES_FIRST = 2 差异内容：LITTLE_CORES_FIRST = 2 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：mindSporeLite； API声明： interface MSTensor 差异内容： interface MSTensor | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：MSTensor； API声明：name: string; 差异内容：name: string; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：MSTensor； API声明：shape: number[]; 差异内容：shape: number[]; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：MSTensor； API声明：elementNum: number; 差异内容：elementNum: number; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：MSTensor； API声明：dataSize: number; 差异内容：dataSize: number; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：MSTensor； API声明：dtype: DataType; 差异内容：dtype: DataType; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：MSTensor； API声明：format: Format; 差异内容：format: Format; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：MSTensor； API声明：getData(): ArrayBuffer; 差异内容：getData(): ArrayBuffer; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：MSTensor； API声明：setData(inputArray: ArrayBuffer): void; 差异内容：setData(inputArray: ArrayBuffer): void; | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：mindSporeLite； API声明： export enum DataType 差异内容： export enum DataType | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：DataType； API声明：TYPE_UNKNOWN = 0 差异内容：TYPE_UNKNOWN = 0 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：DataType； API声明：NUMBER_TYPE_INT8 = 32 差异内容：NUMBER_TYPE_INT8 = 32 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：DataType； API声明：NUMBER_TYPE_INT16 = 33 差异内容：NUMBER_TYPE_INT16 = 33 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：DataType； API声明：NUMBER_TYPE_INT32 = 34 差异内容：NUMBER_TYPE_INT32 = 34 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：DataType； API声明：NUMBER_TYPE_INT64 = 35 差异内容：NUMBER_TYPE_INT64 = 35 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：DataType； API声明：NUMBER_TYPE_UINT8 = 37 差异内容：NUMBER_TYPE_UINT8 = 37 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：DataType； API声明：NUMBER_TYPE_UINT16 = 38 差异内容：NUMBER_TYPE_UINT16 = 38 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：DataType； API声明：NUMBER_TYPE_UINT32 = 39 差异内容：NUMBER_TYPE_UINT32 = 39 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：DataType； API声明：NUMBER_TYPE_UINT64 = 40 差异内容：NUMBER_TYPE_UINT64 = 40 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：DataType； API声明：NUMBER_TYPE_FLOAT16 = 42 差异内容：NUMBER_TYPE_FLOAT16 = 42 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：DataType； API声明：NUMBER_TYPE_FLOAT32 = 43 差异内容：NUMBER_TYPE_FLOAT32 = 43 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：DataType； API声明：NUMBER_TYPE_FLOAT64 = 44 差异内容：NUMBER_TYPE_FLOAT64 = 44 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：mindSporeLite； API声明： export enum Format 差异内容： export enum Format | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：Format； API声明：DEFAULT_FORMAT = -1 差异内容：DEFAULT_FORMAT = -1 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：Format； API声明：NCHW = 0 差异内容：NCHW = 0 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：Format； API声明：NHWC = 1 差异内容：NHWC = 1 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：Format； API声明：NHWC4 = 2 差异内容：NHWC4 = 2 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：Format； API声明：HWKC = 3 差异内容：HWKC = 3 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：Format； API声明：HWCK = 4 差异内容：HWCK = 4 | api/@ohos.ai.mindSporeLite.d.ts |
| 新增API | NA | 类名：Format； API声明：KCHW = 5 差异内容：KCHW = 5 | api/@ohos.ai.mindSporeLite.d.ts |
