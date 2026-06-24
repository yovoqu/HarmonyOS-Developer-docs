# llm_engine.h

更新时间：2026-06-12 06:54:11

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit-llm-engine

#### 概述

定义用于LLM模型推理的API。
 
**引用文件：** <CANNKit/llm_engine.h>
 
**库：** 新增libcann_llm_engine.so
 
**系统能力：** SystemCapability.AI.CANN.LLMEngine
 
**起始版本：** 6.1.1(24)
 
**相关模块：** [CANN](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit)
 
  

#### 汇总

  

#### 类型定义
 
| 名称 | 描述 |
| --- | --- |
| typedef struct HMS_LLMEngine_Context HMS_LLMEngine_Context | 定义LLM引擎上下文的别名。 |
| typedef struct HMS_LLMEngine_Executor HMS_LLMEngine_Executor | LLM 引擎执行器。 |
| typedef struct HMS_LLMEngine_Prompt HMS_LLMEngine_Prompt | LLM引擎文本输入。 |
| typedef void(* callbackFunctionType) (const HMS_LLMEngine_Context *) | 生成回调函数。 |
 
 
  

#### 枚举
 
| 名称 | 描述 |
| --- | --- |
| HMS_LLMEngine_InferPerfMode { HMS_LLMENGINE_INFERPERF_UNSET = 0, HMS_LLMENGINE_INFERPERF_LOW, HMS_LLMENGINE_INFERPERF_MIDDLE, HMS_LLMENGINE_INFERPERF_HIGH, HMS_LLMENGINE_INFERPERF_EXTREME_HIGH } | 推断性能模式。 |
 
 
  

#### 函数
 
| 名称 | 描述 |
| --- | --- |
| HMS_LLMEngine_Context * HMS_LLMEngineExecutor_CreateFromExecutorJson (const char *jsonFile) | 通过JSON配置文件创建LLM引擎上下文句柄。 |
| void HMS_LLMEngine_Context_Destroy (HMS_LLMEngine_Context **ctx) | 销毁LLM引擎上下文。 |
| HMS_LLMEngine_Executor * HMS_LLMEngineContext_CreateFromContextJson (const char *jsonFile) | 通过JSON配置文件创建LLM引擎执行器句柄。 |
| void HMS_LLMEngineExecutor_Destroy (HMS_LLMEngine_Executor **executor) | 销毁一个LLM引擎执行器，该执行器内存释放。 |
| HMS_LLMEngine_Prompt * HMS_LLMEnginePrompt_Create (void) | 创建一个LLM引擎提示句柄。 |
| OH_NN_ReturnCode HMS_LLMEnginePrompt_SetText (HMS_LLMEngine_Prompt *prompt, const char *text) | 设置文本输入。 |
| OH_NN_ReturnCode HMS_LLMEnginePrompt_SetTokenId (HMS_LLMEngine_Prompt *prompt, int32_t *tokenIds, uint32_t tokenNum) | 设置输入的token ID。 |
| void HMS_LLMEnginePrompt_Destroy (HMS_LLMEngine_Prompt **prompt) | 销毁LLM引擎提示词句柄。 |
| OH_NN_ReturnCode HMS_LLMEngineContext_SetOnOneTokenGenerateDoneFunc (HMS_LLMEngine_Context *ctx, callbackFunctionType func) | 设置生成token时触发的回调函数。 |
| OH_NN_ReturnCode HMS_LLMEngineContext_SetOnAllTokensGenerateDoneFunc (HMS_LLMEngine_Context *ctx, callbackFunctionType func) | 设置所有token生成完毕时触发的回调函数。 |
| OH_NN_ReturnCode HMS_LLMEngineContext_SetOnGenerateAsyncFailed (HMS_LLMEngine_Context *ctx, callbackFunctionType func) | 设置生成失败时的回调函数。 |
| OH_NN_ReturnCode HMS_LLMEngineContext_GetOneGenerationLen (const HMS_LLMEngine_Context *ctx, uint32_t *len) | 获取生成文本片段的长度。 |
| OH_NN_ReturnCode HMS_LLMEngineContext_GetOneGeneration (const HMS_LLMEngine_Context *ctx, char *generation, uint32_t len) | 获取生成的文本片段。 |
| OH_NN_ReturnCode HMS_LLMEngineContext_GetAllGenerationLen (const HMS_LLMEngine_Context *ctx, uint32_t *len) | 获取所有生成文本的总长度。 |
| OH_NN_ReturnCode HMS_LLMEngineContext_GetAllGeneration (const HMS_LLMEngine_Context *ctx, char *generation, uint32_t len) | 获取所有生成的文本。 |
| OH_NN_ReturnCode HMS_LLMEngineContext_GetOneTokenGeneration (const HMS_LLMEngine_Context *ctx, int32_t *genToken) | 获取生成的tokenid。 |
| OH_NN_ReturnCode HMS_LLMEngineContext_GetAllTokenGenerationLen (const HMS_LLMEngine_Context *ctx, uint32_t *len) | 获取所有已生成tokenid的长度。 |
| OH_NN_ReturnCode HMS_LLMEngineContext_GetAllTokenGeneration (const HMS_LLMEngine_Context *ctx, int32_t *genToken, uint32_t len) | 获取所有已生成的tokenid。 |
| OH_NN_ReturnCode HMS_LLMEngineExecutor_Generate (HMS_LLMEngine_Executor *executor, HMS_LLMEngine_Context *ctx, const HMS_LLMEngine_Prompt *prompt) | 执行同步LLM推理。 |
| OH_NN_ReturnCode HMS_LLMEngineExecutor_GenerateAsync (HMS_LLMEngine_Executor *executor, HMS_LLMEngine_Context *ctx, const HMS_LLMEngine_Prompt *prompt) | 异步执行LLM推理。 |
| OH_NN_ReturnCode HMS_LLMEngineExecutor_SetInferencePerfMode (HMS_LLMEngine_Executor *executor, HMS_LLMEngine_InferPerfMode inferPerfMode) | 设置推理性能模式。 |
| OH_NN_ReturnCode HMS_LLMEngineContext_GetTotalTimeMs (const HMS_LLMEngine_Context *ctx, double *ms) | 生成总耗时（单位：ms）。 |
| OH_NN_ReturnCode HMS_LLMEngineContext_GetPrefillTimeMs (const HMS_LLMEngine_Context *ctx, double *ms) | 预填充时间（单位：ms）。 |
| OH_NN_ReturnCode HMS_LLMEngineContext_GetDecodeTimeMs (const HMS_LLMEngine_Context *ctx, double *ms) | 解码耗时（单位：ms）。 |
| OH_NN_ReturnCode HMS_LLMEngineContext_GetInputTokenCount (const HMS_LLMEngine_Context *ctx, uint64_t *count) | 输入token数量。 |
| OH_NN_ReturnCode HMS_LLMEngineContext_GetOutputTokenCount (const HMS_LLMEngine_Context *ctx, uint64_t *count) | 输出token数量。 |
