# Data Augmentation Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-dataaugmentationkit-6002

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：Retriever； API声明：retrieveRdb(query: string, condition: RetrievalCondition): Promise&lt;RdbRecords&gt;; 差异内容：NA | 类名：Retriever； API声明：retrieveRdb(query: string, condition: RetrievalCondition): Promise&lt;RdbRecords&gt;; 差异内容：1021200012 | api/@hms.data.retrieval.d.ts |
| 属性变更 | 类名：VectorQuery； API声明：value: Float32Array; 差异内容：value: Float32Array; | 类名：VectorQuery； API声明：value?: Float32Array; 差异内容：value?: Float32Array; | api/@hms.data.retrieval.d.ts |
| 新增API | NA | 类名：global； API声明：declare namespace knowledgeProcessor 差异内容：declare namespace knowledgeProcessor | api/@hms.data.knowledgeProcessor.d.ts |
| 新增API | NA | 类名：knowledgeProcessor； API声明：function getKnowledgeProcessor(context: common.BaseContext, config: KnowledgeProcessorConfig): Promise&lt;KnowledgeProcessor&gt;; 差异内容：function getKnowledgeProcessor(context: common.BaseContext, config: KnowledgeProcessorConfig): Promise&lt;KnowledgeProcessor&gt;; | api/@hms.data.knowledgeProcessor.d.ts |
| 新增API | NA | 类名：knowledgeProcessor； API声明：interface KnowledgeProcessorConfig 差异内容：interface KnowledgeProcessorConfig | api/@hms.data.knowledgeProcessor.d.ts |
| 新增API | NA | 类名：KnowledgeProcessorConfig； API声明：sourceConfig: KnowledgeSourceConfig; 差异内容：sourceConfig: KnowledgeSourceConfig; | api/@hms.data.knowledgeProcessor.d.ts |
| 新增API | NA | 类名：knowledgeProcessor； API声明：interface KnowledgeSourceConfig 差异内容：interface KnowledgeSourceConfig | api/@hms.data.knowledgeProcessor.d.ts |
| 新增API | NA | 类名：KnowledgeSourceConfig； API声明：rdbSource?: relationalStore.StoreConfig; 差异内容：rdbSource?: relationalStore.StoreConfig; | api/@hms.data.knowledgeProcessor.d.ts |
| 新增API | NA | 类名：knowledgeProcessor； API声明：enum ProcessorStatus 差异内容：enum ProcessorStatus | api/@hms.data.knowledgeProcessor.d.ts |
| 新增API | NA | 类名：ProcessorStatus； API声明：DATA_REMAINING_TO_PROCESS = 0 差异内容：DATA_REMAINING_TO_PROCESS = 0 | api/@hms.data.knowledgeProcessor.d.ts |
| 新增API | NA | 类名：ProcessorStatus； API声明：DATA_PROCESSING_IN_PROGRESS = 1 差异内容：DATA_PROCESSING_IN_PROGRESS = 1 | api/@hms.data.knowledgeProcessor.d.ts |
| 新增API | NA | 类名：ProcessorStatus； API声明：DATA_PROCESSING_COMPLETE = 2 差异内容：DATA_PROCESSING_COMPLETE = 2 | api/@hms.data.knowledgeProcessor.d.ts |
| 新增API | NA | 类名：knowledgeProcessor； API声明：interface KnowledgeProcessor 差异内容：interface KnowledgeProcessor | api/@hms.data.knowledgeProcessor.d.ts |
| 新增API | NA | 类名：KnowledgeProcessor； API声明：getStatus(): Promise&lt;ProcessorStatus&gt;; 差异内容：getStatus(): Promise&lt;ProcessorStatus&gt;; | api/@hms.data.knowledgeProcessor.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@hms.data.knowledgeProcessor.d.ts 差异内容：DataAugmentationKit | api/@hms.data.knowledgeProcessor.d.ts |
