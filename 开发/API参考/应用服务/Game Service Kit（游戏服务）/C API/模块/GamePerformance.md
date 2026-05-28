# GamePerformance

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/gameservice-game-performance
**支持设备：** Phone | PC/2in1 | Tablet

##### 概述

为游戏场景感知模块提供C接口的定义。
 
**系统能力：** SystemCapability.GameService.GamePerformance
 
**起始版本：** 5.0.2(14)
 
  

##### 汇总

  

##### 文件
 
| 名称 | 描述 |
| --- | --- |
| game_performance.h | 声明游戏场景感知的基本概念。 |
 
 
  

##### 类型定义
 
| 名称 | 描述 |
| --- | --- |
| typedef struct GamePerformance_DeviceInfo GamePerformance_DeviceInfo | 定义设备性能信息。 |
| typedef struct GamePerformance_GpuInfo GamePerformance_GpuInfo | 定义GPU性能信息。 |
| typedef struct GamePerformance_CpuInfo GamePerformance_CpuInfo | 定义CPU性能信息。 |
| typedef struct GamePerformance_ThermalInfo GamePerformance_ThermalInfo | 定义温度信息。 |
| typedef struct GamePerformance_ThermalInfoQueryParameters GamePerformance_ThermalInfoQueryParameters | 定义温度信息的查询参数。 |
| typedef struct GamePerformance_InitParameters GamePerformance_InitParameters | 定义初始化参数。 |
| typedef struct GamePerformance_PackageInfo GamePerformance_PackageInfo | 定义游戏包信息。 |
| typedef struct GamePerformance_ConfigInfo GamePerformance_ConfigInfo | 定义游戏配置信息。 |
| typedef struct GamePerformance_SceneInfo GamePerformance_SceneInfo | 定义游戏场景信息。 |
| typedef struct GamePerformance_NetInfo GamePerformance_NetInfo | 定义游戏网络信息。 |
| typedef struct GamePerformance_PlayerInfo GamePerformance_PlayerInfo | 定义游戏玩家信息。 |
| typedef enum GamePerformance_EngineType GamePerformance_EngineType | 定义游戏引擎类型。 |
| typedef enum GamePerformance_GameType GamePerformance_GameType | 定义游戏类型。 |
| typedef enum GamePerformance_PictureQualityLevel GamePerformance_PictureQualityLevel | 定义画质等级。 |
| typedef enum GamePerformance_SceneImportanceLevel GamePerformance_SceneImportanceLevel | 定义游戏场景重要程度。 |
| typedef enum GamePerformance_CpuLevel GamePerformance_CpuLevel | 定义CPU等级。 |
| typedef enum GamePerformance_GpuLevel GamePerformance_GpuLevel | 定义GPU等级。 |
| typedef enum GamePerformance_DdrLevel GamePerformance_DdrLevel | 定义DDR等级。 |
| typedef enum GamePerformance_NetLoad GamePerformance_NetLoad | 定义网络负载等级。 |
| typedef enum GamePerformance_ErrorCode GamePerformance_ErrorCode | 定义错误码。 |
| typedef enum GamePerformance_DeviceInfoType GamePerformance_DeviceInfoType | 定义设备性能信息类型。 |
| typedef void(*GamePerformance_ThermalLevelChangedCallback) (GamePerformance_DeviceInfo *deviceInfo, void *userData) | HMS_GamePerformance_RegisterThermalLevelChangedCallback中使用的回调函数。当温度等级改变并且温度等级小于3档时，该函数将被调用一次。当温度等级大于或等于3档时，该函数将每10秒调用一次。 |
 
 
  

##### 枚举
 
| 名称 | 描述 |
| --- | --- |
| GamePerformance_EngineType { GAME_PERFORMANCE_ENGINE_TYPE_UNITY = 1, GAME_PERFORMANCE_ENGINE_TYPE_UNREAL = 2, GAME_PERFORMANCE_ENGINE_TYPE_MESSIAH = 3, GAME_PERFORMANCE_ENGINE_TYPE_COCOS = 4, GAME_PERFORMANCE_ENGINE_TYPE_OTHERS = 200 } | 此枚举描述引擎类型。 |
| GamePerformance_GameType { GAME_PERFORMANCE_GAME_TYPE_MOBA = 1, GAME_PERFORMANCE_GAME_TYPE_RPG = 2, GAME_PERFORMANCE_GAME_TYPE_FPS = 3, GAME_PERFORMANCE_GAME_TYPE_FTG = 4, GAME_PERFORMANCE_GAME_TYPE_RAC = 5, GAME_PERFORMANCE_GAME_TYPE_OTHERS = 200 } | 此枚举描述游戏类型。 |
| GamePerformance_PictureQualityLevel { GAME_PERFORMANCE_PQL_SMOOTH = 1, GAME_PERFORMANCE_PQL_BALANCED = 2, GAME_PERFORMANCE_PQL_HD = 3, GAME_PERFORMANCE_PQL_HDR = 4, GAME_PERFORMANCE_PQL_UHD = 5 } | 此枚举描述画质等级。 |
| GamePerformance_SceneImportanceLevel { GAME_PERFORMANCE_SIL_LEVEL1 = 1, GAME_PERFORMANCE_SIL_LEVEL2 = 2, GAME_PERFORMANCE_SIL_LEVEL3 = 3, GAME_PERFORMANCE_SIL_LEVEL4 = 4, GAME_PERFORMANCE_SIL_LEVEL5 = 5 } | 此枚举描述场景重要程度。 |
| GamePerformance_CpuLevel { GAME_PERFORMANCE_CPU_LEVEL_LOW = 1, GAME_PERFORMANCE_CPU_LEVEL_MIDDLE = 2, GAME_PERFORMANCE_CPU_LEVEL_HIGH = 3 } | 此枚举描述CPU等级。 |
| GamePerformance_GpuLevel { GAME_PERFORMANCE_GPU_LEVEL_LOW = 1, GAME_PERFORMANCE_GPU_LEVEL_MIDDLE = 2, GAME_PERFORMANCE_GPU_LEVEL_HIGH = 3 } | 此枚举描述GPU等级。 |
| GamePerformance_DdrLevel { GAME_PERFORMANCE_DDR_LEVEL_LOW = 1, GAME_PERFORMANCE_DDR_LEVEL_MIDDLE = 2, GAME_PERFORMANCE_DDR_LEVEL_HIGH = 3 } | 此枚举描述DDR等级。 |
| GamePerformance_NetLoad { GAME_PERFORMANCE_NET_LOAD_LIGHT = 1, GAME_PERFORMANCE_NET_LOAD_MODERATE = 2, GAME_PERFORMANCE_NET_LOAD_HEAVY = 3 } | 此枚举描述网络负载等级。 |
| GamePerformance_ErrorCode { GAME_PERFORMANCE_SUCCESS = 0, GAME_PERFORMANCE_PARAM_INVALID = 401, GAME_PERFORMANCE_INTERNAL_ERROR = 1010300001, GAME_PERFORMANCE_AUTH_FAILED = 1010300002, GAME_PERFORMANCE_INVALID_REQUEST = 1010300003, GAME_PERFORMANCE_PARAM_ERROR = 1010300004 } | 此枚举描述错误码。 GAME_PERFORMANCE_PARAM_ERROR 从6.0.2(22)开始支持。 |
| GamePerformance_DeviceInfoType { GAME_PERFORMANCE_DEVICEINFO_TYPE_THERMAL = 0, GAME_PERFORMANCE_DEVICEINFO_TYPE_GPU = 1, GAME_PERFORMANCE_DEVICEINFO_TYPE_CPU = 2 } | 此枚举描述设备性能信息类型。 GAME_PERFORMANCE_DEVICEINFO_TYPE_CPU 从6.0.2(22)开始支持。 |
 
 
  

##### 函数
 
| 名称 | 描述 |
| --- | --- |
| GamePerformance_ErrorCode HMS_GamePerformance_CreateInitParameters (GamePerformance_InitParameters **initParameters) | 创建GamePerformance_InitParameters实例，该实例在HMS_GamePerformance_Init方法中使用。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DestroyInitParameters (GamePerformance_InitParameters **initParameters) | 当GamePerformance_InitParameters实例不再使用，销毁该实例。 |
| GamePerformance_ErrorCode HMS_GamePerformance_InitParameters_SetBundleName (GamePerformance_InitParameters *initParameters, const char *bundleName) | 为GamePerformance_InitParameters实例设置包名。 |
| GamePerformance_ErrorCode HMS_GamePerformance_InitParameters_SetAppVersion (GamePerformance_InitParameters *initParameters, const char *appVersion) | 为GamePerformance_InitParameters实例设置版本号。 |
| GamePerformance_ErrorCode HMS_GamePerformance_Init (GamePerformance_InitParameters *initParameters) | 初始化游戏场景感知。 说明：调用HMS_GamePerformance_Init前，必须已设置bundleName，appVersion。 |
| GamePerformance_ErrorCode HMS_GamePerformance_CreatePackageInfo (GamePerformance_PackageInfo **packageInfo) | 创建GamePerformance_PackageInfo实例，该实例在HMS_GamePerformance_UpdatePackageInfo方法中使用。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DestroyPackageInfo (GamePerformance_PackageInfo **packageInfo) | 当GamePerformance_PackageInfo实例不再使用，销毁该实例。 |
| GamePerformance_ErrorCode HMS_GamePerformance_PackageInfo_SetBundleName (GamePerformance_PackageInfo *packageInfo, const char *bundleName) | 为GamePerformance_PackageInfo实例设置包名。 |
| GamePerformance_ErrorCode HMS_GamePerformance_PackageInfo_SetAppVersion (GamePerformance_PackageInfo *packageInfo, const char *appVersion) | 为GamePerformance_PackageInfo实例设置版本号。 |
| GamePerformance_ErrorCode HMS_GamePerformance_PackageInfo_SetEngineType (GamePerformance_PackageInfo *packageInfo, const GamePerformance_EngineType engineType) | 为GamePerformance_PackageInfo实例设置引擎类型。 |
| GamePerformance_ErrorCode HMS_GamePerformance_PackageInfo_SetEngineVersion (GamePerformance_PackageInfo *packageInfo, const char *engineVersion) | 为GamePerformance_PackageInfo实例设置引擎版本号。 |
| GamePerformance_ErrorCode HMS_GamePerformance_PackageInfo_SetGameType (GamePerformance_PackageInfo *packageInfo, const GamePerformance_GameType gameType) | 为GamePerformance_PackageInfo实例设置游戏类型。 |
| GamePerformance_ErrorCode HMS_GamePerformance_PackageInfo_SetVulkanSupported (GamePerformance_PackageInfo *packageInfo, const bool vulkanSupported) | 为GamePerformance_PackageInfo实例设置是否支持vulkan。 |
| GamePerformance_ErrorCode HMS_GamePerformance_UpdatePackageInfo (GamePerformance_PackageInfo *packageInfo) | 更新游戏包信息。 说明：调用HMS_GamePerformance_UpdatePackageInfo前，必须已设置bundleName，appVersion。 |
| GamePerformance_ErrorCode HMS_GamePerformance_CreateConfigInfo (GamePerformance_ConfigInfo **configInfo) | 创建GamePerformance_ConfigInfo实例，该实例在HMS_GamePerformance_UpdateConfigInfo方法中使用。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DestroyConfigInfo (GamePerformance_ConfigInfo **configInfo) | 当GamePerformance_ConfigInfo实例不再使用，销毁该实例。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetMaxPictureQualityLevel (GamePerformance_ConfigInfo *configInfo, const GamePerformance_PictureQualityLevel maxPictureQualityLevel) | 为GamePerformance_ConfigInfo实例设置最大画质等级。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetCurrentPictureQualityLevel (GamePerformance_ConfigInfo *configInfo, const GamePerformance_PictureQualityLevel currentPictureQualityLevel) | 为GamePerformance_ConfigInfo实例设置当前画质等级。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetMaxFrameRate (GamePerformance_ConfigInfo *configInfo, const int64_t maxFrameRate) | 为GamePerformance_ConfigInfo实例设置最大帧率。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetCurrentFrameRate (GamePerformance_ConfigInfo *configInfo, const int64_t currentFrameRate) | 为GamePerformance_ConfigInfo实例设置当前帧率。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetMaxResolution (GamePerformance_ConfigInfo *configInfo, const char *maxResolution) | 为GamePerformance_ConfigInfo实例设置最大分辨率。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetCurrentResolution (GamePerformance_ConfigInfo *configInfo, const char *currentResolution) | 为GamePerformance_ConfigInfo实例设置当前分辨率。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetAntiAliasingEnabled (GamePerformance_ConfigInfo *configInfo, const bool antiAliasingEnabled) | 为GamePerformance_ConfigInfo实例设置是否开启抗锯齿。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetShadowEnabled (GamePerformance_ConfigInfo *configInfo, const bool shadowEnabled) | 为GamePerformance_ConfigInfo实例设置是否开启阴影。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetMultithreadingEnabled (GamePerformance_ConfigInfo *configInfo, const bool multithreadingEnabled) | 为GamePerformance_ConfigInfo实例设置开启多线程。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetParticleEnabled (GamePerformance_ConfigInfo *configInfo, const bool particleEnabled) | 为GamePerformance_ConfigInfo实例设置粒子效果。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetHdModeEnabled (GamePerformance_ConfigInfo *configInfo, const bool hdModeEnabled) | 为GamePerformance_ConfigInfo实例设置开启高清模式。 |
| GamePerformance_ErrorCode HMS_GamePerformance_UpdateConfigInfo (GamePerformance_ConfigInfo *configInfo) | 更新游戏配置信息。 |
| GamePerformance_ErrorCode HMS_GamePerformance_CreateSceneInfo (GamePerformance_SceneInfo **sceneInfo) | 创建GamePerformance_SceneInfo实例，该实例在HMS_GamePerformance_UpdateSceneInfo方法中使用。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DestroySceneInfo (GamePerformance_SceneInfo **sceneInfo) | 当GamePerformance_SceneInfo实例不再使用，销毁该实例。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetSceneID (GamePerformance_SceneInfo *sceneInfo, const int64_t sceneID) | 为GamePerformance_SceneInfo实例设置场景ID。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetDescription (GamePerformance_SceneInfo *sceneInfo, const char *description) | 为GamePerformance_SceneInfo实例设置场景描述。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetSubSceneID (GamePerformance_SceneInfo *sceneInfo, const char *subSceneID) | 为GamePerformance_SceneInfo实例设置子场景ID。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetSubDescription (GamePerformance_SceneInfo *sceneInfo, const char *subDescription) | 为GamePerformance_SceneInfo实例设置子场景描述。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetImportanceLevel (GamePerformance_SceneInfo *sceneInfo, const GamePerformance_SceneImportanceLevel importanceLevel) | 为GamePerformance_SceneInfo实例设置场景重要程度。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetSceneFrequency (GamePerformance_SceneInfo *sceneInfo, const int64_t sceneFrequency) | 为GamePerformance_SceneInfo实例设置该场景在一局游戏中出现的次数。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetSceneTime (GamePerformance_SceneInfo *sceneInfo, const int64_t sceneTime) | 为GamePerformance_SceneInfo实例设置场景持续时间。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetRecommendedCpuLevel (GamePerformance_SceneInfo *sceneInfo, const GamePerformance_CpuLevel recommendedCpuLevel) | 为GamePerformance_SceneInfo实例设置推荐的CPU等级。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetRecommendedGpuLevel (GamePerformance_SceneInfo *sceneInfo, const GamePerformance_GpuLevel recommendedGpuLevel) | 为GamePerformance_SceneInfo实例设置推荐的GPU等级。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetRecommendedDdrLevel (GamePerformance_SceneInfo *sceneInfo, const GamePerformance_DdrLevel recommendedDdrLevel) | 为GamePerformance_SceneInfo实例设置推荐的DDR等级。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetMaxFrameRate (GamePerformance_SceneInfo *sceneInfo, const int64_t maxFrameRate) | 为GamePerformance_SceneInfo实例设置场景最大帧率。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetCurrentFrameRate (GamePerformance_SceneInfo *sceneInfo, const int64_t currentFrameRate) | 为GamePerformance_SceneInfo实例设置场景当前帧率。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetKeyThread (GamePerformance_SceneInfo *sceneInfo, const char *keyThread) | 为GamePerformance_SceneInfo实例设置关键线程。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetDrawCallCount (GamePerformance_SceneInfo *sceneInfo, const int64_t drawCallCount) | 为GamePerformance_SceneInfo实例设置每帧的平均Drawcall数。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetVertexCount (GamePerformance_SceneInfo *sceneInfo, const int64_t vertexCount) | 为GamePerformance_SceneInfo实例设置每帧的平均模型顶点数。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetTriangleCount (GamePerformance_SceneInfo *sceneInfo, const int64_t triangleCount) | 为GamePerformance_SceneInfo实例设置每帧的平均模型三角形数。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetShaderCount (GamePerformance_SceneInfo *sceneInfo, const int64_t shaderCount) | 为GamePerformance_SceneInfo实例设置每帧的平均shader数量。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetTextureCount (GamePerformance_SceneInfo *sceneInfo, const int64_t textureCount) | 为GamePerformance_SceneInfo实例设置每帧的平均纹理数量。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetMeshCount (GamePerformance_SceneInfo *sceneInfo, const int64_t meshCount) | 为GamePerformance_SceneInfo实例设置每帧的平均mesh数量。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetChannelCount (GamePerformance_SceneInfo *sceneInfo, const int64_t channelCount) | 为GamePerformance_SceneInfo实例设置每帧渲染的通道数。 |
| GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetParticipantCount (GamePerformance_SceneInfo *sceneInfo, const int64_t participantCount) | 为GamePerformance_SceneInfo实例设置场景下的同屏人数。 |
| GamePerformance_ErrorCode HMS_GamePerformance_UpdateSceneInfo (GamePerformance_SceneInfo *sceneInfo) | 更新游戏场景信息。 说明：调用HMS_GamePerformance_UpdateSceneInfo前，必须已设置sceneID，importanceLevel。 |
| GamePerformance_ErrorCode HMS_GamePerformance_CreateNetInfo (GamePerformance_NetInfo **netInfo) | 创建GamePerformance_NetInfo实例，该实例在HMS_GamePerformance_UpdateNetInfo方法中使用。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DestroyNetInfo (GamePerformance_NetInfo **netInfo) | 当GamePerformance_NetInfo实例不再使用，销毁该实例。 |
| GamePerformance_ErrorCode HMS_GamePerformance_NetInfo_SetTotalLatency (GamePerformance_NetInfo *netInfo, const int64_t total) | 为GamePerformance_NetInfo实例设置总网络时延。 |
| GamePerformance_ErrorCode HMS_GamePerformance_NetInfo_SetUplinkLatency (GamePerformance_NetInfo *netInfo, const int64_t up) | 为GamePerformance_NetInfo实例设置上行网络时延。 |
| GamePerformance_ErrorCode HMS_GamePerformance_NetInfo_SetDownlinkLatency (GamePerformance_NetInfo *netInfo, const int64_t down) | 为GamePerformance_NetInfo实例设置下行网络时延。 |
| GamePerformance_ErrorCode HMS_GamePerformance_NetInfo_SetServerLatency (GamePerformance_NetInfo *netInfo, const int64_t server) | 为GamePerformance_NetInfo实例设置服务器网络时延。 |
| GamePerformance_ErrorCode HMS_GamePerformance_NetInfo_SetNetLoad (GamePerformance_NetInfo *netInfo, const GamePerformance_NetLoad netLoad) | 为GamePerformance_NetInfo实例设置网络负载。 |
| GamePerformance_ErrorCode HMS_GamePerformance_UpdateNetInfo (GamePerformance_NetInfo *netInfo) | 更新游戏网络信息。 说明：调用HMS_GamePerformance_UpdateNetInfo前必须已设置totalLatency。 |
| GamePerformance_ErrorCode HMS_GamePerformance_CreatePlayerInfo (GamePerformance_PlayerInfo **playerInfo) | 创建GamePerformance_PlayerInfo实例，该实例在HMS_GamePerformance_UpdatePlayerInfo方法中使用。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DestroyPlayerInfo (GamePerformance_PlayerInfo **playerInfo) | 当GamePerformance_PlayerInfo实例不再使用，销毁该实例。 |
| GamePerformance_ErrorCode HMS_GamePerformance_PlayerInfo_SetGamePlayerId (GamePerformance_PlayerInfo *playerInfo, const char *gamePlayerId) | 为GamePerformance_PlayerInfo实例设置游戏玩家ID。 说明：gamePlayerId、teamPlayerId和thirdOpenId不能同时为空。 |
| GamePerformance_ErrorCode HMS_GamePerformance_PlayerInfo_SetTeamPlayerId (GamePerformance_PlayerInfo *playerInfo, const char *teamPlayerId) | 为GamePerformance_PlayerInfo实例设置团队玩家ID。 说明：gamePlayerId、teamPlayerId和thirdOpenId不能同时为空。 |
| GamePerformance_ErrorCode HMS_GamePerformance_PlayerInfo_SetThirdOpenId (GamePerformance_PlayerInfo *playerInfo, const char *thirdOpenId) | 为GamePerformance_PlayerInfo实例设置游戏官方账号。 说明：gamePlayerId、teamPlayerId和thirdOpenId不能同时为空。 |
| GamePerformance_ErrorCode HMS_GamePerformance_UpdatePlayerInfo (GamePerformance_PlayerInfo *playerInfo) | 更新游戏玩家信息。 |
| GamePerformance_ErrorCode HMS_GamePerformance_RegisterThermalLevelChangedCallback (GamePerformance_DeviceInfoType *types[], size_t size, GamePerformance_ThermalLevelChangedCallback callback, void *userData) | 订阅温度变化事件，注册温度变化回调，当达到触发点时，将调用回调函数。 |
| GamePerformance_ErrorCode HMS_GamePerformance_UnregisterThermalLevelChangedCallback (GamePerformance_ThermalLevelChangedCallback callback) | 取消注册指定温度变化回调。 |
| GamePerformance_ErrorCode HMS_GamePerformance_UnregisterAllThermalLevelChangedCallbacks (void) | 取消注册所有温度变化回调。 |
| GamePerformance_ErrorCode HMS_GamePerformance_CreateThermalInfoQueryParameters (GamePerformance_ThermalInfoQueryParameters **parameters) | 创建GamePerformance_ThermalInfoQueryParameters实例，该实例在HMS_GamePerformance_QueryThermalInfo方法中使用。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DestroyThermalInfoQueryParameters (GamePerformance_ThermalInfoQueryParameters **parameters) | 当GamePerformance_ThermalInfoQueryParameters实例不再使用，销毁该实例。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ThermalInfoQueryParameters_SetNeedsPrediction (GamePerformance_ThermalInfoQueryParameters *parameters, const bool needsPrediction) | 为GamePerformance_ThermalInfoQueryParameters实例设置是否需要预测温升趋势。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ThermalInfoQueryParameters_SetTargetThermalLevel (GamePerformance_ThermalInfoQueryParameters *parameters, const int32_t targetThermalLevel) | 为GamePerformance_ThermalInfoQueryParameters实例设置预测温升趋势的目标温度等级。 |
| GamePerformance_ErrorCode HMS_GamePerformance_QueryThermalInfo (GamePerformance_ThermalInfoQueryParameters *parameters, GamePerformance_ThermalInfo **thermalInfo) | 查询温度信息。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DestroyThermalInfo (GamePerformance_ThermalInfo **thermalInfo) | 当GamePerformance_ThermalInfo实例不再使用，销毁该实例。 |
| GamePerformance_ErrorCode HMS_GamePerformance_QueryGpuInfo (GamePerformance_GpuInfo **gpuInfo) | 查询GPU性能信息。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DestroyGpuInfo (GamePerformance_GpuInfo **gpuInfo) | 当GamePerformance_GpuInfo实例不再使用，销毁该实例。 |
| GamePerformance_ErrorCode HMS_GamePerformance_QueryCpuInfo (GamePerformance_CpuInfo **cpuInfo) | 查询CPU性能信息。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DestroyCpuInfo (GamePerformance_CpuInfo **cpuInfo) | 当GamePerformance_CpuInfo实例不再使用，销毁该实例。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DeviceInfo_GetThermalInfo (GamePerformance_DeviceInfo *deviceInfo, GamePerformance_ThermalInfo **thermalInfo) | 从设备性能信息GamePerformance_DeviceInfo中获取温度信息GamePerformance_ThermalInfo。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ThermalInfo_GetThermalMargin (GamePerformance_ThermalInfo *thermalInfo, int32_t *thermalMargin) | 从温度信息GamePerformance_ThermalInfo中获取温度时间裕量。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ThermalInfo_GetThermalTrend (GamePerformance_ThermalInfo *thermalInfo, int32_t *thermalTrend) | 从GamePerformance_ThermalInfo中获取温升趋势。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ThermalInfo_GetThermalLevel (GamePerformance_ThermalInfo *thermalInfo, int32_t *thermalLevel) | 从GamePerformance_ThermalInfo中获取温度等级。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ThermalInfo_GetRecommendNormalizedCurrent (GamePerformance_ThermalInfo *thermalInfo, int32_t *recommendCurrent) | 从GamePerformance_ThermalInfo中获取系统建议的工作电流。若当前的工作电流高于此值，温升趋势thermalTrend会大于0，设备有发烫风险。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ThermalInfo_GetNowNormalizedCurrent (GamePerformance_ThermalInfo *thermalInfo, int32_t *nowCurrent) | 从GamePerformance_ThermalInfo中获取当前的工作电流。 |
| GamePerformance_ErrorCode HMS_GamePerformance_ThermalInfo_GetRecommendMaxNormalizedCurrent (GamePerformance_ThermalInfo *thermalInfo, int32_t *recommendMaxCurrent) | 从GamePerformance_ThermalInfo中获取系统建议的最大工作电流。若当前的工作电流高于此值，设备会立即发烫。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DeviceInfo_GetGpuInfo (GamePerformance_DeviceInfo *deviceInfo, GamePerformance_GpuInfo **gpuInfo) | 从设备性能信息GamePerformance_DeviceInfo中获取GPU性能信息GamePerformance_GpuInfo。 |
| GamePerformance_ErrorCode HMS_GamePerformance_GpuInfo_GetGpuLoadLevel (GamePerformance_GpuInfo *gpuInfo, int32_t *gpuLoadLevel) | 从GamePerformance_GpuInfo中获取GPU负载信息。 |
| GamePerformance_ErrorCode HMS_GamePerformance_GpuInfo_GetVertexLoadLevel (GamePerformance_GpuInfo *gpuInfo, int32_t *vertexLoadLevel) | 从GamePerformance_GpuInfo中获取GPU顶点处理负载等级。 |
| GamePerformance_ErrorCode HMS_GamePerformance_GpuInfo_GetFragmentLoadLevel (GamePerformance_GpuInfo *gpuInfo, int32_t *fragmentLoadLevel) | 从GamePerformance_GpuInfo中获取GPU片元处理负载等级。 |
| GamePerformance_ErrorCode HMS_GamePerformance_GpuInfo_GetTextureLoadLevel (GamePerformance_GpuInfo *gpuInfo, int32_t *textureLoadLevel) | 从GamePerformance_GpuInfo中获取GPU纹理处理负载等级。 |
| GamePerformance_ErrorCode HMS_GamePerformance_GpuInfo_GetBandwidthLoadLevel (GamePerformance_GpuInfo *gpuInfo, int32_t *bandwidthLoadLevel) | 从GamePerformance_GpuInfo中获取GPU带宽负载等级。 |
| GamePerformance_ErrorCode HMS_GamePerformance_GpuInfo_GetCurrentFrequency (GamePerformance_GpuInfo *gpuInfo, int32_t *currentFrequency) | 从GamePerformance_GpuInfo中获取GPU频点信息。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DeviceInfo_GetCpuInfo (GamePerformance_DeviceInfo *deviceInfo, GamePerformance_CpuInfo **cpuInfo) | 从设备性能信息GamePerformance_DeviceInfo中获取CPU性能信息GamePerformance_CpuInfo。 |
| GamePerformance_ErrorCode HMS_GamePerformance_CpuInfo_GetCpuLoadLevel (GamePerformance_CpuInfo *cpuInfo, int32_t *cpuLoadLevel) | 从GamePerformance_CpuInfo中获取CPU负载整体等级。 |
| GamePerformance_ErrorCode HMS_GamePerformance_CpuInfo_GetSingleThreadLoadLevel (GamePerformance_CpuInfo *cpuInfo, int32_t *singleThreadLoadLevel) | 从GamePerformance_CpuInfo中获取游戏最重线程的负载整体等级。 |
| GamePerformance_ErrorCode HMS_GamePerformance_DestroyDeviceInfo (GamePerformance_DeviceInfo **deviceInfo) | 当GamePerformance_DeviceInfo实例不再使用，销毁该实例。 |
 
 
  

##### 类型定义说明

  

##### GamePerformance_ConfigInfo

```text
typedef struct GamePerformance_ConfigInfo GamePerformance_ConfigInfo
```
 
**描述**
 
定义游戏配置信息。
 
**起始版本：** 5.0.2(14)
 
  

##### GamePerformance_CpuInfo

```text
typedef struct GamePerformance_CpuInfo GamePerformance_CpuInfo
```
 
**描述**
 
定义CPU性能信息。
 
**起始版本：** 6.0.2(22)
 
  

##### GamePerformance_CpuLevel

```text
typedef enum GamePerformance_CpuLevel GamePerformance_CpuLevel
```
 
**描述**
 
定义CPU等级。
 
**起始版本：** 5.0.2(14)
 
  

##### GamePerformance_DdrLevel

```text
typedef enum GamePerformance_DdrLevel GamePerformance_DdrLevel
```
 
**描述**
 
定义DDR等级。
 
**起始版本：** 5.0.2(14)
 
  

##### GamePerformance_DeviceInfo

```text
typedef struct GamePerformance_DeviceInfo GamePerformance_DeviceInfo
```
 
**描述**
 
定义设备性能信息。
 
**起始版本：** 5.0.2(14)
 
  

##### GamePerformance_DeviceInfoType

```text
typedef enum GamePerformance_DeviceInfoType GamePerformance_DeviceInfoType
```
 
**描述**
 
定义设备性能信息类型。
 
**起始版本：** 5.0.2(14)
 
  

##### GamePerformance_EngineType

```text
typedef enum GamePerformance_EngineType GamePerformance_EngineType
```
 
**描述**
 
定义游戏引擎类型。
 
**起始版本：** 5.0.2(14)
 
  

##### GamePerformance_ErrorCode

```text
typedef enum GamePerformance_ErrorCode GamePerformance_ErrorCode
```
 
**描述**
 
定义错误码。
 
**起始版本：** 5.0.2(14)
 
  

##### GamePerformance_GameType

```text
typedef enum GamePerformance_GameType GamePerformance_GameType
```
 
**描述**
 
定义游戏类型。
 
**起始版本：** 5.0.2(14)
 
  

##### GamePerformance_GpuInfo

```text
typedef struct GamePerformance_GpuInfo GamePerformance_GpuInfo
```
 
**描述**
 
定义GPU性能信息。
 
**起始版本：** 5.0.2(14)
 
  

##### GamePerformance_GpuLevel

```text
typedef enum GamePerformance_GpuLevel GamePerformance_GpuLevel
```
 
**描述**
 
定义GPU等级。
 
**起始版本：** 5.0.2(14)
 
  

##### GamePerformance_InitParameters

```text
typedef struct GamePerformance_InitParameters GamePerformance_InitParameters
```
 
**描述**
 
定义初始化参数。
 
**起始版本：** 5.0.2(14)
 
  

##### GamePerformance_NetInfo

```text
typedef struct GamePerformance_NetInfo GamePerformance_NetInfo
```
 
**描述**
 
定义游戏网络信息。
 
**起始版本：** 5.0.2(14)
 
  

##### GamePerformance_NetLoad

```text
typedef enum GamePerformance_NetLoad GamePerformance_NetLoad
```
 
**描述**
 
定义网络负载等级。
 
**起始版本：** 5.0.2(14)
 
  

##### GamePerformance_PackageInfo

```text
typedef struct GamePerformance_PackageInfo GamePerformance_PackageInfo
```
 
**描述**
 
定义游戏包信息。
 
**起始版本：** 5.0.2(14)
 
  

##### GamePerformance_PictureQualityLevel

```text
typedef enum GamePerformance_PictureQualityLevel GamePerformance_PictureQualityLevel
```
 
**描述**
 
定义画质等级。
 
**起始版本：** 5.0.2(14)
 
  

##### GamePerformance_PlayerInfo

```text
typedef struct GamePerformance_PlayerInfo GamePerformance_PlayerInfo
```
 
**描述**
 
定义游戏玩家信息。
 
**起始版本：** 5.0.2(14)
 
  

##### GamePerformance_SceneImportanceLevel

```text
typedef enum GamePerformance_SceneImportanceLevel GamePerformance_SceneImportanceLevel
```
 
**描述**
 
定义场景重要程度。
 
**起始版本：** 5.0.2(14)
 
  

##### GamePerformance_SceneInfo

```text
typedef struct GamePerformance_SceneInfo GamePerformance_SceneInfo
```
 
**描述**
 
定义游戏场景信息。
 
**起始版本：** 5.0.2(14)
 
  

##### GamePerformance_ThermalInfo

```text
typedef struct GamePerformance_ThermalInfo GamePerformance_ThermalInfo
```
 
**描述**
 
定义温度信息。
 
**起始版本：** 5.0.2(14)
 
  

##### GamePerformance_ThermalInfoQueryParameters

```text
typedef struct GamePerformance_ThermalInfoQueryParameters GamePerformance_ThermalInfoQueryParameters
```
 
**描述**
 
定义温度信息的查询参数。
 
**起始版本：** 5.0.2(14)
 
  

##### GamePerformance_ThermalLevelChangedCallback

```text
typedef void(*GamePerformance_ThermalLevelChangedCallback) (GamePerformance_DeviceInfo *deviceInfo, void *userData)
```
 
**描述**
 
[HMS_GamePerformance_RegisterThermalLevelChangedCallback](#hms_gameperformance_registerthermallevelchangedcallback)中使用的回调函数。当温度等级改变并且温度等级小于3档时，该函数将被调用一次。当温度等级大于或等于3档时，该函数将每10秒调用一次。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| deviceInfo | 设备详细信息GamePerformance_DeviceInfo。 |
| userData | 用户指定的数据。用户自定义传参。 |
 
 
  

##### 枚举类型说明

  

##### GamePerformance_CpuLevel

```text
enum GamePerformance_CpuLevel
```
 
**描述**
 
定义CPU等级。
 
**起始版本：** 5.0.2(14)
  
| 枚举值 | 描述 |
| --- | --- |
| GAME_PERFORMANCE_CPU_LEVEL_LOW | 低。 |
| GAME_PERFORMANCE_CPU_LEVEL_MIDDLE | 中。 |
| GAME_PERFORMANCE_CPU_LEVEL_HIGH | 高。 |
 
 
  

##### GamePerformance_DdrLevel

```text
enum GamePerformance_DdrLevel
```
 
**描述**
 
定义DDR等级。
 
**起始版本：** 5.0.2(14)
  
| 枚举值 | 描述 |
| --- | --- |
| GAME_PERFORMANCE_DDR_LEVEL_LOW | 低。 |
| GAME_PERFORMANCE_DDR_LEVEL_MIDDLE | 中。 |
| GAME_PERFORMANCE_DDR_LEVEL_HIGH | 高。 |
 
 
  

##### GamePerformance_DeviceInfoType

```text
enum GamePerformance_DeviceInfoType
```
 
**描述**
 
定义回调返回的设备性能信息类型。
 
**起始版本：** 5.0.2(14)
  
| 枚举值 | 描述 |
| --- | --- |
| GAME_PERFORMANCE_DEVICEINFO_TYPE_THERMAL | 温度信息。 |
| GAME_PERFORMANCE_DEVICEINFO_TYPE_GPU | GPU性能信息。 |
| GAME_PERFORMANCE_DEVICEINFO_TYPE_CPU | CPU性能信息。 起始版本： 6.0.2(22) |
 
 
  

##### GamePerformance_EngineType

```text
enum GamePerformance_EngineType
```
 
**描述**
 
定义游戏引擎类型。
 
**起始版本：** 5.0.2(14)
  
| 枚举值 | 描述 |
| --- | --- |
| GAME_PERFORMANCE_ENGINE_TYPE_UNITY | UNITY。 |
| GAME_PERFORMANCE_ENGINE_TYPE_UNREAL | UNREAL。 |
| GAME_PERFORMANCE_ENGINE_TYPE_MESSIAH | MESSIAH。 |
| GAME_PERFORMANCE_ENGINE_TYPE_COCOS | COCOS。 |
| GAME_PERFORMANCE_ENGINE_TYPE_OTHERS | 其他引擎类型。 |
 
 
  

##### GamePerformance_ErrorCode

```text
enum GamePerformance_ErrorCode
```
 
**描述**
 
定义错误码。
 
**起始版本：** 5.0.2(14)
  
| 枚举值 | 描述 |
| --- | --- |
| GAME_PERFORMANCE_SUCCESS | 成功。 |
| GAME_PERFORMANCE_PARAM_INVALID | 无效参数。 |
| GAME_PERFORMANCE_INTERNAL_ERROR | 系统内部错误。 |
| GAME_PERFORMANCE_AUTH_FAILED | 鉴权失败。 |
| GAME_PERFORMANCE_INVALID_REQUEST | 非法请求。 |
| GAME_PERFORMANCE_PARAM_ERROR | 参数错误。 起始版本：6.0.2(22) |
 
 
  

##### GamePerformance_GameType

```text
enum GamePerformance_GameType
```
 
**描述**
 
定义游戏类型。
 
**起始版本：** 5.0.2(14)
  
| 枚举值 | 描述 |
| --- | --- |
| GAME_PERFORMANCE_GAME_TYPE_MOBA | 多人在线战术竞技。 |
| GAME_PERFORMANCE_GAME_TYPE_RPG | 角色扮演。 |
| GAME_PERFORMANCE_GAME_TYPE_FPS | 第一人称射击类。 |
| GAME_PERFORMANCE_GAME_TYPE_FTG | 格斗游戏。 |
| GAME_PERFORMANCE_GAME_TYPE_RAC | 竞速游戏。 |
| GAME_PERFORMANCE_GAME_TYPE_OTHERS | 其他游戏类型。 |
 
 
  

##### GamePerformance_GpuLevel

```text
enum GamePerformance_GpuLevel
```
 
**描述**
 
定义GPU等级。
 
**起始版本：** 5.0.2(14)
  
| 枚举值 | 描述 |
| --- | --- |
| GAME_PERFORMANCE_GPU_LEVEL_LOW | 低。 |
| GAME_PERFORMANCE_GPU_LEVEL_MIDDLE | 中。 |
| GAME_PERFORMANCE_GPU_LEVEL_HIGH | 高。 |
 
 
  

##### GamePerformance_NetLoad

```text
enum GamePerformance_NetLoad
```
 
**描述**
 
定义网络负载等级。
 
**起始版本：** 5.0.2(14)
  
| 枚举值 | 描述 |
| --- | --- |
| GAME_PERFORMANCE_NET_LOAD_LIGHT | 轻度负载。 |
| GAME_PERFORMANCE_NET_LOAD_MODERATE | 中度负载。 |
| GAME_PERFORMANCE_NET_LOAD_HEAVY | 重度负载。 |
 
 
  

##### GamePerformance_PictureQualityLevel

```text
enum GamePerformance_PictureQualityLevel
```
 
**描述**
 
定义画质等级。
 
**起始版本：** 5.0.2(14)
  
| 枚举值 | 描述 |
| --- | --- |
| GAME_PERFORMANCE_PQL_SMOOTH | 流畅。 |
| GAME_PERFORMANCE_PQL_BALANCED | 均衡。 |
| GAME_PERFORMANCE_PQL_HD | 高清。 |
| GAME_PERFORMANCE_PQL_HDR | HDR高清。 |
| GAME_PERFORMANCE_PQL_UHD | 超高清。 |
 
 
  

##### GamePerformance_SceneImportanceLevel

```text
enum GamePerformance_SceneImportanceLevel
```
 
**描述**
 
定义游戏场景重要程度，5个等级，重要程度从1到5递增。
 
**起始版本：** 5.0.2(14)
  
| 枚举值 | 描述 |
| --- | --- |
| GAME_PERFORMANCE_SIL_LEVEL1 | 等级1。 |
| GAME_PERFORMANCE_SIL_LEVEL2 | 等级2。 |
| GAME_PERFORMANCE_SIL_LEVEL3 | 等级3。 |
| GAME_PERFORMANCE_SIL_LEVEL4 | 等级4。 |
| GAME_PERFORMANCE_SIL_LEVEL5 | 等级5。 |
 
 
  

##### 函数说明

  

##### HMS_GamePerformance_ConfigInfo_SetAntiAliasingEnabled()

```text
GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetAntiAliasingEnabled (GamePerformance_ConfigInfo *configInfo, const bool antiAliasingEnabled)
```
 
**描述**
 
为[GamePerformance_ConfigInfo](#gameperformance_configinfo)实例设置是否开启抗锯齿。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向GamePerformance_ConfigInfo实例。该值不可以为空，否则将返回错误码401。 |
| antiAliasingEnabled | 是否开启抗锯齿。 - true：开启 - false：不开启 默认为false。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_ConfigInfo_SetCurrentFrameRate()

```text
GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetCurrentFrameRate (GamePerformance_ConfigInfo *configInfo, const int64_t currentFrameRate)
```
 
**描述**
 
为[GamePerformance_ConfigInfo](#gameperformance_configinfo)实例设置当前帧率。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向GamePerformance_ConfigInfo实例。该值不可以为空，否则将返回错误码401。 |
| currentFrameRate | 当前帧率，单位：fps。取值范围为[1, 144]。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_ConfigInfo_SetCurrentPictureQualityLevel()

```text
GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetCurrentPictureQualityLevel (GamePerformance_ConfigInfo *configInfo, const GamePerformance_PictureQualityLevel currentPictureQualityLevel)
```
 
**描述**
 
为[GamePerformance_ConfigInfo](#gameperformance_configinfo)实例设置当前画质等级。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向GamePerformance_ConfigInfo实例。该值不可以为空，否则将返回错误码401。 |
| currentPictureQualityLevel | 当前画质等级GamePerformance_PictureQualityLevel。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_ConfigInfo_SetCurrentResolution()

```text
GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetCurrentResolution (GamePerformance_ConfigInfo *configInfo, const char *currentResolution)
```
 
**描述**
 
为[GamePerformance_ConfigInfo](#gameperformance_configinfo)实例设置当前分辨率。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向GamePerformance_ConfigInfo实例。该值不可以为空，否则将返回错误码401。 |
| currentResolution | 当前分辨率。格式AxB（如1260x1980），字符长度范围：[1, 32]。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_ConfigInfo_SetHdModeEnabled()

```text
GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetHdModeEnabled (GamePerformance_ConfigInfo *configInfo, const bool hdModeEnabled)
```
 
**描述**
 
为[GamePerformance_ConfigInfo](#gameperformance_configinfo)实例设置开启高清模式。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向GamePerformance_ConfigInfo实例。该值不可以为空，否则将返回错误码401。 |
| hdModeEnabled | 是否开启高清模式。 - true：开启 - false：不开启 默认为false。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_ConfigInfo_SetMaxFrameRate()

```text
GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetMaxFrameRate (GamePerformance_ConfigInfo *configInfo, const int64_t maxFrameRate)
```
 
**描述**
 
为[GamePerformance_ConfigInfo](#gameperformance_configinfo)实例设置最大帧率。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向GamePerformance_ConfigInfo实例。该值不可以为空，否则将返回错误码401。 |
| maxFrameRate | 最大帧率，单位：fps。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_ConfigInfo_SetMaxPictureQualityLevel()

```text
GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetMaxPictureQualityLevel (GamePerformance_ConfigInfo *configInfo, const GamePerformance_PictureQualityLevel maxPictureQualityLevel)
```
 
**描述**
 
为[GamePerformance_ConfigInfo](#gameperformance_configinfo)实例设置最大画质等级。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向GamePerformance_ConfigInfo实例。该值不可以为空，否则将返回错误码401。 |
| maxPictureQualityLevel | 支持的画质最高等级GamePerformance_PictureQualityLevel。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_ConfigInfo_SetMaxResolution()

```text
GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetMaxResolution (GamePerformance_ConfigInfo *configInfo, const char *maxResolution)
```
 
**描述**
 
为[GamePerformance_ConfigInfo](#gameperformance_configinfo)实例设置最大分辨率。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向GamePerformance_ConfigInfo实例。该值不可以为空，否则将返回错误码401。 |
| maxResolution | 最大分辨率。格式AxB（如1260x1980），字符长度范围：[1, 32]。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_ConfigInfo_SetMultithreadingEnabled()

```text
GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetMultithreadingEnabled (GamePerformance_ConfigInfo *configInfo, const bool multithreadingEnabled)
```
 
**描述**
 
为[GamePerformance_ConfigInfo](#gameperformance_configinfo)实例设置开启多线程。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向GamePerformance_ConfigInfo实例。该值不可以为空，否则将返回错误码401。 |
| multithreadingEnabled | 是否开启多线程。 - true：开启 - false：不开启 默认为false。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_ConfigInfo_SetParticleEnabled()

```text
GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetParticleEnabled (GamePerformance_ConfigInfo *configInfo, const bool particleEnabled)
```
 
**描述**
 
为[GamePerformance_ConfigInfo](#gameperformance_configinfo)实例设置粒子效果。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向GamePerformance_ConfigInfo实例。该值不可以为空，否则将返回错误码401。 |
| particleEnabled | 是否开启粒子效果。 - true：开启 - false：不开启 默认为false。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_ConfigInfo_SetShadowEnabled()

```text
GamePerformance_ErrorCode HMS_GamePerformance_ConfigInfo_SetShadowEnabled (GamePerformance_ConfigInfo *configInfo, const bool shadowEnabled)
```
 
**描述**
 
为[GamePerformance_ConfigInfo](#gameperformance_configinfo)实例设置是否开启阴影。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向GamePerformance_ConfigInfo实例。该值不可以为空，否则将返回错误码401。 |
| shadowEnabled | 是否开启阴影。 - true：开启 - false：不开启 默认为false。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_CpuInfo_GetCpuLoadLevel()

```text
GamePerformance_ErrorCode HMS_GamePerformance_CpuInfo_GetCpuLoadLevel (GamePerformance_CpuInfo *cpuInfo, int32_t *cpuLoadLevel)
```
 
**描述**
 
从[GamePerformance_CpuInfo](#gameperformance_cpuinfo)中获取CPU负载整体等级。
 
**起始版本：** 6.0.2(22)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| cpuInfo | 指向GamePerformance_CpuInfo实例的指针。该值不可以为空，否则将返回错误码1010300004。 |
| cpuLoadLevel | CPU负载整体等级，取值范围为[1, 10]区间的整数。值越大表示负载越高。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_ERROR：参数错误。参数不能为空指针。 |
 
 
  

##### HMS_GamePerformance_CpuInfo_GetSingleThreadLoadLevel()

```text
GamePerformance_ErrorCode HMS_GamePerformance_CpuInfo_GetSingleThreadLoadLevel (GamePerformance_CpuInfo *cpuInfo, int32_t *singleThreadLoadLevel)
```
 
**描述**
 
从[GamePerformance_CpuInfo](#gameperformance_cpuinfo)中获取游戏最重线程的负载整体等级。
 
**起始版本：** 6.0.2(22)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| cpuInfo | 指针指向GamePerformance_CpuInfo实例。该值不可以为空，否则将返回错误码1010300004。 |
| singleThreadLoadLevel | 游戏最重线程的负载整体等级，取值范围为[1, 10]区间的整数。值越大表示负载越高。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_ERROR：参数错误。参数不能为空指针。 |
 
 
  

##### HMS_GamePerformance_CreateConfigInfo()

```text
GamePerformance_ErrorCode HMS_GamePerformance_CreateConfigInfo (GamePerformance_ConfigInfo **configInfo)
```
 
**描述**
 
创建[GamePerformance_ConfigInfo](#gameperformance_configinfo)实例，该实例在[HMS_GamePerformance_UpdateConfigInfo](#hms_gameperformance_updateconfiginfo)方法中使用。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| configInfo | 二级指针指向GamePerformance_ConfigInfo实例。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 |
 
 
  

##### HMS_GamePerformance_CreateInitParameters()

```text
GamePerformance_ErrorCode HMS_GamePerformance_CreateInitParameters (GamePerformance_InitParameters **initParameters)
```
 
**描述**
 
创建[GamePerformance_InitParameters](#gameperformance_initparameters)实例，该实例在[HMS_GamePerformance_Init](#hms_gameperformance_init)方法中使用。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| initParameters | 二级指针指向GamePerformance_InitParameters初始化参数实例。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 |
 
 
  

##### HMS_GamePerformance_CreateNetInfo()

```text
GamePerformance_ErrorCode HMS_GamePerformance_CreateNetInfo (GamePerformance_NetInfo **netInfo)
```
 
**描述**
 
创建[GamePerformance_NetInfo](#gameperformance_netinfo)实例，该实例在[HMS_GamePerformance_UpdateNetInfo](#hms_gameperformance_updatenetinfo)方法中使用。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| netInfo | 二级指针指向GamePerformance_NetInfo实例。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 |
 
 
  

##### HMS_GamePerformance_CreatePackageInfo()

```text
GamePerformance_ErrorCode HMS_GamePerformance_CreatePackageInfo (GamePerformance_PackageInfo **packageInfo)
```
 
**描述**
 
创建[GamePerformance_PackageInfo](#gameperformance_packageinfo)实例，该实例在[HMS_GamePerformance_UpdatePackageInfo](#hms_gameperformance_updatepackageinfo)方法中使用。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| packageInfo | 二级指针指向GamePerformance_PackageInfo实例。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 |
 
 
  

##### HMS_GamePerformance_CreatePlayerInfo()

```text
GamePerformance_ErrorCode HMS_GamePerformance_CreatePlayerInfo (GamePerformance_PlayerInfo **playerInfo)
```
 
**描述**
 
创建[GamePerformance_PlayerInfo](#gameperformance_playerinfo)实例，该实例在[HMS_GamePerformance_UpdatePlayerInfo](#hms_gameperformance_updateplayerinfo)方法中使用。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| playerInfo | 二级指针指向GamePerformance_PlayerInfo实例。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 |
 
 
  

##### HMS_GamePerformance_CreateSceneInfo()

```text
GamePerformance_ErrorCode HMS_GamePerformance_CreateSceneInfo (GamePerformance_SceneInfo **sceneInfo)
```
 
**描述**
 
创建[GamePerformance_SceneInfo](#gameperformance_sceneinfo)实例，该实例在[HMS_GamePerformance_UpdateSceneInfo](#hms_gameperformance_updatesceneinfo)方法中使用。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| sceneInfo | 二级指针指向GamePerformance_SceneInfo实例。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 |
 
 
  

##### HMS_GamePerformance_CreateThermalInfoQueryParameters()

```text
GamePerformance_ErrorCode HMS_GamePerformance_CreateThermalInfoQueryParameters (GamePerformance_ThermalInfoQueryParameters **parameters)
```
 
**描述**
 
创建[GamePerformance_ThermalInfoQueryParameters](#gameperformance_thermalinfoqueryparameters)实例，该实例在[HMS_GamePerformance_QueryThermalInfo](#hms_gameperformance_querythermalinfo)方法中使用。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| parameters | 二级指针指向GamePerformance_ThermalInfoQueryParameters实例。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 |
 
 
  

##### HMS_GamePerformance_DestroyConfigInfo()

```text
GamePerformance_ErrorCode HMS_GamePerformance_DestroyConfigInfo (GamePerformance_ConfigInfo **configInfo)
```
 
**描述**
 
当[GamePerformance_ConfigInfo](#gameperformance_configinfo)实例不再使用，销毁该实例。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| configInfo | 二级指针指向GamePerformance_ConfigInfo实例。该值不可以为空，否则将返回错误码401。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_DestroyCpuInfo()

```text
GamePerformance_ErrorCode HMS_GamePerformance_DestroyCpuInfo (GamePerformance_CpuInfo **cpuInfo)
```
 
**描述**
 
当[GamePerformance_CpuInfo](#gameperformance_cpuinfo)实例不再使用，销毁该实例。
 
**起始版本：** 6.0.2(22)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| cpuInfo | 二级指针指向GamePerformance_CpuInfo实例。该值不可以为空，否则将返回错误码1010300004。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_ERROR：参数错误。参数不能为空指针。 |
 
 
  

##### HMS_GamePerformance_DestroyDeviceInfo()

```text
GamePerformance_ErrorCode HMS_GamePerformance_DestroyDeviceInfo (GamePerformance_DeviceInfo **deviceInfo)
```
 
**描述**
 
当[GamePerformance_DeviceInfo](#gameperformance_deviceinfo)实例不再使用，销毁该实例。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| deviceInfo | 二级指针指向GamePerformance_DeviceInfo实例。该值不可以为空，否则将返回错误码401。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_DestroyGpuInfo()

```text
GamePerformance_ErrorCode HMS_GamePerformance_DestroyGpuInfo (GamePerformance_GpuInfo **gpuInfo)
```
 
**描述**
 
当[GamePerformance_GpuInfo](#gameperformance_gpuinfo)实例不再使用，销毁该实例。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| gpuInfo | 二级指针指向GamePerformance_GpuInfo实例。该值不可以为空，否则将返回错误码401。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_DestroyInitParameters()

```text
GamePerformance_ErrorCode HMS_GamePerformance_DestroyInitParameters (GamePerformance_InitParameters **initParameters)
```
 
**描述**
 
当[GamePerformance_InitParameters](#gameperformance_initparameters)实例不再使用，销毁该实例。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| initParameters | 二级指针指向GamePerformance_InitParameters实例。该值不可以为空，否则将返回错误码401。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_DestroyNetInfo()

```text
GamePerformance_ErrorCode HMS_GamePerformance_DestroyNetInfo (GamePerformance_NetInfo **netInfo)
```
 
**描述**
 
当[GamePerformance_NetInfo](#gameperformance_netinfo)实例不再使用，销毁该实例。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| netInfo | 二级指针指向GamePerformance_NetInfo实例。该值不可以为空，否则将返回错误码401。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_DestroyPackageInfo()

```text
GamePerformance_ErrorCode HMS_GamePerformance_DestroyPackageInfo (GamePerformance_PackageInfo **packageInfo)
```
 
**描述**
 
当[GamePerformance_PackageInfo](#gameperformance_packageinfo)实例不再使用，销毁该实例。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| packageInfo | 二级指针指向GamePerformance_PackageInfo实例。该值不可以为空，否则将返回错误码401。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_DestroyPlayerInfo()

```text
GamePerformance_ErrorCode HMS_GamePerformance_DestroyPlayerInfo (GamePerformance_PlayerInfo **playerInfo)
```
 
**描述**
 
当[GamePerformance_PlayerInfo](#gameperformance_playerinfo)实例不再使用，销毁该实例。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| playerInfo | 二级指针指向GamePerformance_PlayerInfo实例。该值不可以为空，否则将返回错误码401。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_DestroySceneInfo()

```text
GamePerformance_ErrorCode HMS_GamePerformance_DestroySceneInfo (GamePerformance_SceneInfo **sceneInfo)
```
 
**描述**
 
当[GamePerformance_SceneInfo](#gameperformance_sceneinfo)实例不再使用，销毁该实例。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| sceneInfo | 二级指针指向GamePerformance_SceneInfo实例。该值不可以为空，否则将返回错误码401。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_DestroyThermalInfo()

```text
GamePerformance_ErrorCode HMS_GamePerformance_DestroyThermalInfo (GamePerformance_ThermalInfo **thermalInfo)
```
 
**描述**
 
当[GamePerformance_ThermalInfo](#gameperformance_thermalinfo)实例不再使用，销毁该实例。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| thermalInfo | 二级指针指向GamePerformance_ThermalInfo实例。该值不可以为空，否则将返回错误码401。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_DestroyThermalInfoQueryParameters()

```text
GamePerformance_ErrorCode HMS_GamePerformance_DestroyThermalInfoQueryParameters (GamePerformance_ThermalInfoQueryParameters **parameters)
```
 
**描述**
 
当[GamePerformance_ThermalInfoQueryParameters](#gameperformance_thermalinfoqueryparameters)实例不再使用，销毁该实例。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| parameters | 二级指针指向GamePerformance_ThermalInfoQueryParameters实例。该值不可以为空，否则将返回错误码401。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_DeviceInfo_GetCpuInfo()

```text
GamePerformance_ErrorCode HMS_GamePerformance_DeviceInfo_GetCpuInfo (GamePerformance_DeviceInfo *deviceInfo, GamePerformance_CpuInfo **cpuInfo)
```
 
**描述**
 
从设备性能信息[GamePerformance_DeviceInfo](#gameperformance_deviceinfo)中获取CPU性能信息[GamePerformance_CpuInfo](#gameperformance_cpuinfo)。当[GamePerformance_CpuInfo](#gameperformance_cpuinfo)实例不再使用，必须调用[HMS_GamePerformance_DestroyCpuInfo](#hms_gameperformance_destroycpuinfo)销毁该实例。
 
**起始版本：** 6.0.2(22)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| deviceInfo | 指针指向GamePerformance_DeviceInfo实例。该值不可以为空，否则将返回错误码1010300004。 |
| cpuInfo | 二级指针指向GamePerformance_CpuInfo实例。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_ERROR：参数错误。参数不能为空指针。 |
 
 
  

##### HMS_GamePerformance_DeviceInfo_GetGpuInfo()

```text
GamePerformance_ErrorCode HMS_GamePerformance_DeviceInfo_GetGpuInfo (GamePerformance_DeviceInfo *deviceInfo, GamePerformance_GpuInfo **gpuInfo)
```
 
**描述**
 
从设备性能信息[GamePerformance_DeviceInfo](#gameperformance_deviceinfo)中获取GPU性能信息[GamePerformance_GpuInfo](#gameperformance_gpuinfo)。当[GamePerformance_GpuInfo](#gameperformance_gpuinfo)实例不再使用，必须调用[HMS_GamePerformance_DestroyGpuInfo](#hms_gameperformance_destroygpuinfo)销毁该实例。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| deviceInfo | 指针指向GamePerformance_DeviceInfo实例。该值不可以为空，否则将返回错误码401。 |
| gpuInfo | 二级指针指向GamePerformance_GpuInfo实例。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_DeviceInfo_GetThermalInfo()

```text
GamePerformance_ErrorCode HMS_GamePerformance_DeviceInfo_GetThermalInfo (GamePerformance_DeviceInfo *deviceInfo, GamePerformance_ThermalInfo **thermalInfo)
```
 
**描述**
 
从设备性能信息[GamePerformance_DeviceInfo](#gameperformance_deviceinfo)中获取温度信息[GamePerformance_ThermalInfo](#gameperformance_thermalinfo)。当[GamePerformance_ThermalInfo](#gameperformance_thermalinfo)实例不再使用，必须调用[HMS_GamePerformance_DestroyThermalInfo](#hms_gameperformance_destroythermalinfo)销毁该实例。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| deviceInfo | 指针指向GamePerformance_DeviceInfo实例。该值不可以为空，否则将返回错误码401。 |
| thermalInfo | 二级指针指向GamePerformance_ThermalInfo实例。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_GpuInfo_GetBandwidthLoadLevel()

```text
GamePerformance_ErrorCode HMS_GamePerformance_GpuInfo_GetBandwidthLoadLevel (GamePerformance_GpuInfo *gpuInfo, int32_t *bandwidthLoadLevel)
```
 
**描述**
 
从[GamePerformance_GpuInfo](#gameperformance_gpuinfo)中获取GPU带宽负载等级。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| gpuInfo | 指针指向GamePerformance_GpuInfo实例。该值不可以为空，否则将返回错误码401。 |
| bandwidthLoadLevel | GPU带宽负载等级，取值范围为[1, 10]区间的整数。值越大表示负载越高。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_GpuInfo_GetCurrentFrequency()

```text
GamePerformance_ErrorCode HMS_GamePerformance_GpuInfo_GetCurrentFrequency (GamePerformance_GpuInfo *gpuInfo, int32_t *currentFrequency)
```
 
**描述**
 
从[GamePerformance_GpuInfo](#gameperformance_gpuinfo)中获取GPU频点信息。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| gpuInfo | 指针指向GamePerformance_GpuInfo实例。该值不可以为空，否则将返回错误码401。 |
| currentFrequency | GPU频点信息，单位：KHz。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_GpuInfo_GetFragmentLoadLevel()

```text
GamePerformance_ErrorCode HMS_GamePerformance_GpuInfo_GetFragmentLoadLevel (GamePerformance_GpuInfo *gpuInfo, int32_t *fragmentLoadLevel)
```
 
**描述**
 
从[GamePerformance_GpuInfo](#gameperformance_gpuinfo)中获取GPU片元处理负载等级。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| gpuInfo | 指针指向GamePerformance_GpuInfo实例。该值不可以为空，否则将返回错误码401。 |
| fragmentLoadLevel | GPU片元处理负载等级，取值范围为[1, 10]区间的整数。值越大表示负载越高。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_GpuInfo_GetGpuLoadLevel()

```text
GamePerformance_ErrorCode HMS_GamePerformance_GpuInfo_GetGpuLoadLevel (GamePerformance_GpuInfo *gpuInfo, int32_t *gpuLoadLevel)
```
 
**描述**
 
从[GamePerformance_GpuInfo](#gameperformance_gpuinfo)中获取GPU负载信息。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| gpuInfo | 指针指向GamePerformance_GpuInfo实例。该值不可以为空，否则将返回错误码401。 |
| gpuLoadLevel | GPU负载信息，取值范围为[1, 10]区间的整数。值越大表示负载越高。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_GpuInfo_GetTextureLoadLevel()

```text
GamePerformance_ErrorCode HMS_GamePerformance_GpuInfo_GetTextureLoadLevel (GamePerformance_GpuInfo *gpuInfo, int32_t *textureLoadLevel)
```
 
**描述**
 
从[GamePerformance_GpuInfo](#gameperformance_gpuinfo)中获取GPU纹理处理负载等级。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| gpuInfo | 指针指向GamePerformance_GpuInfo实例。该值不可以为空，否则将返回错误码401。 |
| textureLoadLevel | GPU纹理处理负载等级，取值范围为[1, 10]区间的整数。值越高表示负载越高。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_GpuInfo_GetVertexLoadLevel()

```text
GamePerformance_ErrorCode HMS_GamePerformance_GpuInfo_GetVertexLoadLevel (GamePerformance_GpuInfo *gpuInfo, int32_t *vertexLoadLevel)
```
 
**描述**
 
从[GamePerformance_GpuInfo](#gameperformance_gpuinfo)中获取GPU顶点处理负载等级。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| gpuInfo | 指针指向GamePerformance_GpuInfo实例。该值不可以为空，否则将返回错误码401。 |
| vertexLoadLevel | GPU顶点处理负载等级，取值范围为[1, 10]区间的整数。值越大表示负载越高。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_Init()

```text
GamePerformance_ErrorCode HMS_GamePerformance_Init (GamePerformance_InitParameters *initParameters)
```
 
**描述**
 
初始化游戏场景感知。
 
> [!NOTE]
> 调用HMS_GamePerformance_Init前，必须已调用 HMS_GamePerformance_InitParameters_SetBundleName 接口和 HMS_GamePerformance_InitParameters_SetAppVersion 接口，分别设置bundleName和appVersion。

 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| initParameters | 指针指向GamePerformance_InitParameters实例。该值不可以为空，否则将返回错误码401。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 GAME_PERFORMANCE_INTERNAL_ERROR：系统内部错误。 GAME_PERFORMANCE_AUTH_FAILED：认证失败。 |
 
 
  

##### HMS_GamePerformance_InitParameters_SetAppVersion()

```text
GamePerformance_ErrorCode HMS_GamePerformance_InitParameters_SetAppVersion (GamePerformance_InitParameters *initParameters,const char *appVersion)
```
 
**描述**
 
为[GamePerformance_InitParameters](#gameperformance_initparameters)实例设置版本号。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| initParameters | 指针指向GamePerformance_InitParameters实例。该值不可以为空，否则将返回错误码401。 |
| appVersion | 游戏版本号。字符长度范围：[1, 64]。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_InitParameters_SetBundleName()

```text
GamePerformance_ErrorCode HMS_GamePerformance_InitParameters_SetBundleName (GamePerformance_InitParameters *initParameters, const char *bundleName)
```
 
**描述**
 
为[GamePerformance_InitParameters](#gameperformance_initparameters)实例设置包名。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| initParameters | 指针指向GamePerformance_InitParameters实例。该值不可以为空，否则将返回错误码401。 |
| bundleName | 游戏包名。字符长度范围：[1, 128]。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_NetInfo_SetDownlinkLatency()

```text
GamePerformance_ErrorCode HMS_GamePerformance_NetInfo_SetDownlinkLatency (GamePerformance_NetInfo *netInfo, const int64_t down)
```
 
**描述**
 
为[GamePerformance_NetInfo](#gameperformance_netinfo)实例设置下行网络时延。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| netInfo | 指针指向GamePerformance_NetInfo实例。该值不可以为空，否则将返回错误码401。 |
| down | 下行网络时延，单位：毫秒（ms）。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_NetInfo_SetNetLoad()

```text
GamePerformance_ErrorCode HMS_GamePerformance_NetInfo_SetNetLoad (GamePerformance_NetInfo *netInfo, const GamePerformance_NetLoad netLoad)
```
 
**描述**
 
为[GamePerformance_NetInfo](#gameperformance_netinfo)实例设置网络负载。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| netInfo | 指针指向GamePerformance_NetInfo实例。该值不可以为空，否则将返回错误码401。 |
| netLoad | 网络负载GamePerformance_NetLoad。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_NetInfo_SetServerLatency()

```text
GamePerformance_ErrorCode HMS_GamePerformance_NetInfo_SetServerLatency (GamePerformance_NetInfo *netInfo, const int64_t server)
```
 
**描述**
 
为[GamePerformance_NetInfo](#gameperformance_netinfo)实例设置服务器网络时延。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| netInfo | 指针指向GamePerformance_NetInfo实例。该值不可以为空，否则将返回错误码401。 |
| server | 服务器网络时延，单位：毫秒（ms）。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_NetInfo_SetTotalLatency()

```text
GamePerformance_ErrorCode HMS_GamePerformance_NetInfo_SetTotalLatency (GamePerformance_NetInfo *netInfo, const int64_t total)
```
 
**描述**
 
为[GamePerformance_NetInfo](#gameperformance_netinfo)实例设置总网络时延。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| netInfo | 指针指向GamePerformance_NetInfo实例。该值不可以为空，否则将返回错误码401。 |
| total | 总网络时延，单位：毫秒（ms）。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_NetInfo_SetUplinkLatency()

```text
GamePerformance_ErrorCode HMS_GamePerformance_NetInfo_SetUplinkLatency (GamePerformance_NetInfo *netInfo, const int64_t up)
```
 
**描述**
 
为[GamePerformance_NetInfo](#gameperformance_netinfo)实例设置上行网络时延。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| netInfo | 指针指向GamePerformance_NetInfo实例。该值不可以为空，否则将返回错误码401。 |
| up | 上行网络时延，单位：毫秒（ms）。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_PackageInfo_SetAppVersion()

```text
GamePerformance_ErrorCode HMS_GamePerformance_PackageInfo_SetAppVersion (GamePerformance_PackageInfo *packageInfo, const char *appVersion)
```
 
**描述**
 
为[GamePerformance_PackageInfo](#gameperformance_packageinfo)实例设置游戏版本号。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| packageInfo | 指针指向GamePerformance_PackageInfo实例。该值不可以为空，否则将返回错误码401。 |
| appVersion | 游戏版本号。字符长度范围：[1, 64]。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_PackageInfo_SetBundleName()

```text
GamePerformance_ErrorCode HMS_GamePerformance_PackageInfo_SetBundleName (GamePerformance_PackageInfo *packageInfo, const char *bundleName)
```
 
**描述**
 
为[GamePerformance_PackageInfo](#gameperformance_packageinfo)实例设置包名。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| packageInfo | 指针指向GamePerformance_PackageInfo实例。该值不可以为空，否则将返回错误码401。 |
| bundleName | 游戏包名。字符长度范围：[1, 128]。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_PackageInfo_SetEngineType()

```text
GamePerformance_ErrorCode HMS_GamePerformance_PackageInfo_SetEngineType (GamePerformance_PackageInfo *packageInfo, const GamePerformance_EngineType engineType)
```
 
**描述**
 
为[GamePerformance_PackageInfo](#gameperformance_packageinfo)实例设置引擎类型。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| packageInfo | 指针指向GamePerformance_PackageInfo实例。该值不可以为空，否则将返回错误码401。 |
| engineType | 引擎类型GamePerformance_EngineType。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_PackageInfo_SetEngineVersion()

```text
GamePerformance_ErrorCode HMS_GamePerformance_PackageInfo_SetEngineVersion (GamePerformance_PackageInfo *packageInfo, const char *engineVersion)
```
 
**描述**
 
为[GamePerformance_PackageInfo](#gameperformance_packageinfo)实例设置引擎版本号。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| packageInfo | 指针指向GamePerformance_PackageInfo实例。该值不可以为空，否则将返回错误码401。 |
| engineVersion | 游戏引擎版本号。字符长度范围：[0, 64]。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_PackageInfo_SetGameType()

```text
GamePerformance_ErrorCode HMS_GamePerformance_PackageInfo_SetGameType (GamePerformance_PackageInfo *packageInfo, const GamePerformance_GameType gameType)
```
 
**描述**
 
为[GamePerformance_PackageInfo](#gameperformance_packageinfo)实例设置游戏类型。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| packageInfo | 指针指向GamePerformance_PackageInfo实例。该值不可以为空，否则将返回错误码401。 |
| gameType | 游戏类型GamePerformance_GameType。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_PackageInfo_SetVulkanSupported()

```text
GamePerformance_ErrorCode HMS_GamePerformance_PackageInfo_SetVulkanSupported (GamePerformance_PackageInfo *packageInfo, const bool vulkanSupported)
```
 
**描述**
 
为[GamePerformance_PackageInfo](#gameperformance_packageinfo)实例设置是否支持vulkan。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| packageInfo | 指针指向GamePerformance_PackageInfo实例。该值不可以为空，否则将返回错误码401。 |
| vulkanSupported | 是否支持vulkan。 - true：支持 - false：不支持 默认为false。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_PlayerInfo_SetGamePlayerId()

```text
GamePerformance_ErrorCode HMS_GamePerformance_PlayerInfo_SetGamePlayerId (GamePerformance_PlayerInfo *playerInfo, const char *gamePlayerId)
```
 
**描述**
 
为[GamePerformance_PlayerInfo](#gameperformance_playerinfo)实例设置游戏玩家ID。
 
> [!NOTE]
> 调用 HMS_GamePerformance_PlayerInfo_SetGamePlayerId 设置的gamePlayerId、 HMS_GamePerformance_PlayerInfo_SetTeamPlayerId 设置的teamPlayerId和 HMS_GamePerformance_PlayerInfo_SetThirdOpenId 设置的thirdOpenId不能同时为空。

 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| playerInfo | 指针指向GamePerformance_PlayerInfo实例。该值不可以为空，否则将返回错误码401。 |
| gamePlayerId | 游戏玩家ID。字符长度范围：[0, 256]。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_PlayerInfo_SetTeamPlayerId()

```text
GamePerformance_ErrorCode HMS_GamePerformance_PlayerInfo_SetTeamPlayerId (GamePerformance_PlayerInfo *playerInfo, const char *teamPlayerId)
```
 
**描述**
 
为[GamePerformance_PlayerInfo](#gameperformance_playerinfo)实例设置团队玩家ID。
 
> [!NOTE]
> 调用 HMS_GamePerformance_PlayerInfo_SetGamePlayerId 设置的gamePlayerId、 HMS_GamePerformance_PlayerInfo_SetTeamPlayerId 设置的teamPlayerId和 HMS_GamePerformance_PlayerInfo_SetThirdOpenId 设置的thirdOpenId不能同时为空。

 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| playerInfo | 指针指向GamePerformance_PlayerInfo实例。该值不可以为空，否则将返回错误码401。 |
| teamPlayerId | 团队玩家ID。字符长度范围：[0, 256]。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_PlayerInfo_SetThirdOpenId()

```text
GamePerformance_ErrorCode HMS_GamePerformance_PlayerInfo_SetThirdOpenId (GamePerformance_PlayerInfo *playerInfo, const char *thirdOpenId)
```
 
**描述**
 
为[GamePerformance_PlayerInfo](#gameperformance_playerinfo)实例设置游戏官方账号。
 
> [!NOTE]
> 调用 HMS_GamePerformance_PlayerInfo_SetGamePlayerId 设置的gamePlayerId、 HMS_GamePerformance_PlayerInfo_SetTeamPlayerId 设置的teamPlayerId和 HMS_GamePerformance_PlayerInfo_SetThirdOpenId 设置的thirdOpenId不能同时为空。

 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| playerInfo | 指针指向GamePerformance_PlayerInfo实例。该值不可以为空，否则将返回错误码401。 |
| thirdOpenId | 游戏官方账号。字符长度范围：[0, 128]。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_QueryCpuInfo()

```text
GamePerformance_ErrorCode HMS_GamePerformance_QueryCpuInfo (GamePerformance_CpuInfo **cpuInfo)
```
 
**描述**
 
查询CPU性能信息。当[GamePerformance_CpuInfo](#gameperformance_cpuinfo)实例不再使用，必须调用[HMS_GamePerformance_DestroyCpuInfo](#hms_gameperformance_destroycpuinfo)销毁该实例。
 
**起始版本：** 6.0.2(22)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| cpuInfo | 二级指针指向GamePerformance_CpuInfo实例。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_INTERNAL_ERROR：系统内部错误。请通过在线提单系统提交此问题。 GAME_PERFORMANCE_INVALID_REQUEST：无效请求。请先调用HMS_GamePerformance_Init接口。 GAME_PERFORMANCE_PARAM_ERROR：参数错误。参数不能为空指针。 |
 
 
  

##### HMS_GamePerformance_QueryGpuInfo()

```text
GamePerformance_ErrorCode HMS_GamePerformance_QueryGpuInfo (GamePerformance_GpuInfo **gpuInfo)
```
 
**描述**
 
查询GPU性能信息。当[GamePerformance_GpuInfo](#gameperformance_gpuinfo)实例不再使用，必须调用[HMS_GamePerformance_DestroyGpuInfo](#hms_gameperformance_destroygpuinfo)销毁该实例。
 
> [!NOTE]
> Mali系列GPU不支持采集GPU性能信息，无法获取设备GPU性能信息。

 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| gpuInfo | 二级指针指向GamePerformance_GpuInfo实例。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 GAME_PERFORMANCE_INTERNAL_ERROR：系统内部错误。 GAME_PERFORMANCE_INVALID_REQUEST：无效请求。 |
 
 
  

##### HMS_GamePerformance_QueryThermalInfo()

```text
GamePerformance_ErrorCode HMS_GamePerformance_QueryThermalInfo (GamePerformance_ThermalInfoQueryParameters *parameters, GamePerformance_ThermalInfo **thermalInfo)
```
 
**描述**
 
查询温度信息。当[GamePerformance_ThermalInfo](#gameperformance_thermalinfo)实例不再使用，必须调用[HMS_GamePerformance_DestroyThermalInfo](#hms_gameperformance_destroythermalinfo)销毁该实例。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| parameters | 指针指向GamePerformance_ThermalInfoQueryParameters实例。该值不可以为空，否则将返回错误码401。 |
| thermalInfo | 二级指针指向GamePerformance_ThermalInfo实例。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 GAME_PERFORMANCE_INTERNAL_ERROR：系统内部错误。 GAME_PERFORMANCE_INVALID_REQUEST：无效请求。 |
 
 
  

##### HMS_GamePerformance_RegisterThermalLevelChangedCallback()

```text
GamePerformance_ErrorCode HMS_GamePerformance_RegisterThermalLevelChangedCallback (GamePerformance_DeviceInfoType *types[], size_t size, GamePerformance_ThermalLevelChangedCallback callback, void *userData)
```
 
**描述**
 
订阅温度变化事件，注册温度变化回调，当达到触发点时，将调用回调函数。
 
当温度等级改变并且温度等级小于3档时，该函数将被调用一次。当温度等级大于或等于3档时，该函数将每10秒调用一次。
 
> [!NOTE]
> Mali系列GPU不支持采集GPU性能信息，无法获取设备GPU性能信息。

 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| types[] | 注册回调的设备性能信息类型GamePerformance_DeviceInfoType。 |
| size | types数组的长度。 |
| callback | 回调函数GamePerformance_ThermalLevelChangedCallback。 |
| userData | 用户指定数据。用户自定义任意类型，callback透传返回。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 GAME_PERFORMANCE_INTERNAL_ERROR：系统内部错误。 GAME_PERFORMANCE_INVALID_REQUEST：无效请求。 |
 
 
  

##### HMS_GamePerformance_SceneInfo_SetChannelCount()

```text
GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetChannelCount (GamePerformance_SceneInfo *sceneInfo, const int64_t channelCount)
```
 
**描述**
 
为[GamePerformance_SceneInfo](#gameperformance_sceneinfo)实例设置每帧渲染的通道数。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向GamePerformance_SceneInfo实例。该值不可以为空，否则将返回错误码401。 |
| channelCount | 每帧渲染的通道数。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_SceneInfo_SetCurrentFrameRate()

```text
GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetCurrentFrameRate (GamePerformance_SceneInfo *sceneInfo, const int64_t currentFrameRate)
```
 
**描述**
 
为[GamePerformance_SceneInfo](#gameperformance_sceneinfo)实例设置场景当前帧率。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向GamePerformance_SceneInfo实例。该值不可以为空，否则将返回错误码401。 |
| currentFrameRate | 场景当前帧率，单位：fps。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_SceneInfo_SetDescription()

```text
GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetDescription (GamePerformance_SceneInfo *sceneInfo, const char *description)
```
 
**描述**
 
为[GamePerformance_SceneInfo](#gameperformance_sceneinfo)实例设置场景描述。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向GamePerformance_SceneInfo实例。该值不可以为空，否则将返回错误码401。 |
| description | 游戏场景描述（自定义描述）。字符长度范围：[0, 128]。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_SceneInfo_SetDrawCallCount()

```text
GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetDrawCallCount (GamePerformance_SceneInfo *sceneInfo, const int64_t drawCallCount)
```
 
**描述**
 
为[GamePerformance_SceneInfo](#gameperformance_sceneinfo)实例设置每帧的平均Drawcall数。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向GamePerformance_SceneInfo实例。该值不可以为空，否则将返回错误码401。 |
| drawCallCount | 每帧的平均Drawcall数。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_SceneInfo_SetImportanceLevel()

```text
GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetImportanceLevel (GamePerformance_SceneInfo *sceneInfo, const GamePerformance_SceneImportanceLevel importanceLevel)
```
 
**描述**
 
为[GamePerformance_SceneInfo](#gameperformance_sceneinfo)实例设置场景重要程度。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向GamePerformance_SceneInfo实例。该值不可以为空，否则将返回错误码401。 |
| importanceLevel | 场景重要程度GamePerformance_SceneImportanceLevel。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_SceneInfo_SetKeyThread()

```text
GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetKeyThread (GamePerformance_SceneInfo *sceneInfo, const char *keyThread)
```
 
**描述**
 
为[GamePerformance_SceneInfo](#gameperformance_sceneinfo)实例设置关键线程。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向GamePerformance_SceneInfo实例。该值不可以为空，否则将返回错误码401。 |
| keyThread | 该场景下的关键线程。 - render：渲染线程 - logic：逻辑线程 - net：网络线程 按照 render\|xxx\|logic\|xxx 格式传入。字符长度范围：[0, 32]。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_SceneInfo_SetMaxFrameRate()

```text
GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetMaxFrameRate (GamePerformance_SceneInfo *sceneInfo, const int64_t maxFrameRate)
```
 
**描述**
 
为[GamePerformance_SceneInfo](#gameperformance_sceneinfo)实例设置场景最大帧率。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向GamePerformance_SceneInfo实例。该值不可以为空，否则将返回错误码401。 |
| maxFrameRate | 场景最大帧率，单位：fps。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_SceneInfo_SetMeshCount()

```text
GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetMeshCount (GamePerformance_SceneInfo *sceneInfo, const int64_t meshCount)
```
 
**描述**
 
为[GamePerformance_SceneInfo](#gameperformance_sceneinfo)实例设置每帧的平均mesh数量。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向GamePerformance_SceneInfo实例。该值不可以为空，否则将返回错误码401。 |
| meshCount | 每帧的平均mesh数量。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_SceneInfo_SetParticipantCount()

```text
GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetParticipantCount (GamePerformance_SceneInfo *sceneInfo, const int64_t participantCount)
```
 
**描述**
 
为[GamePerformance_SceneInfo](#gameperformance_sceneinfo)实例设置场景下的同屏人数。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向GamePerformance_SceneInfo实例。该值不可以为空，否则将返回错误码401。 |
| participantCount | 场景下的同屏人数。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_SceneInfo_SetRecommendedCpuLevel()

```text
GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetRecommendedCpuLevel (GamePerformance_SceneInfo *sceneInfo, const GamePerformance_CpuLevel recommendedCpuLevel)
```
 
**描述**
 
为[GamePerformance_SceneInfo](#gameperformance_sceneinfo)实例设置推荐的CPU等级。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向GamePerformance_SceneInfo实例。该值不可以为空，否则将返回错误码401。 |
| recommendedCpuLevel | 推荐的CPU等级GamePerformance_CpuLevel。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_SceneInfo_SetRecommendedDdrLevel()

```text
GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetRecommendedDdrLevel (GamePerformance_SceneInfo *sceneInfo, const GamePerformance_DdrLevel recommendedDdrLevel)
```
 
**描述**
 
为[GamePerformance_SceneInfo](#gameperformance_sceneinfo)实例设置推荐的DDR等级。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向GamePerformance_SceneInfo实例。该值不可以为空，否则将返回错误码401。 |
| recommendedDdrLevel | 推荐的DDR等级GamePerformance_DdrLevel。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_SceneInfo_SetRecommendedGpuLevel()

```text
GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetRecommendedGpuLevel (GamePerformance_SceneInfo *sceneInfo, const GamePerformance_GpuLevel recommendedGpuLevel)
```
 
**描述**
 
为[GamePerformance_SceneInfo](#gameperformance_sceneinfo)实例设置推荐的GPU等级。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向GamePerformance_SceneInfo实例。该值不可以为空，否则将返回错误码401。 |
| recommendedGpuLevel | 推荐的GPU等级GamePerformance_GpuLevel。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_SceneInfo_SetSceneFrequency()

```text
GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetSceneFrequency (GamePerformance_SceneInfo *sceneInfo, const int64_t sceneFrequency)
```
 
**描述**
 
为[GamePerformance_SceneInfo](#gameperformance_sceneinfo)实例设置该场景在一局游戏中出现的次数。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向GamePerformance_SceneInfo实例。该值不可以为空，否则将返回错误码401。 |
| sceneFrequency | 该场景在一局游戏中出现的次数。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_SceneInfo_SetSceneID()

```text
GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetSceneID (GamePerformance_SceneInfo *sceneInfo, const int64_t sceneID)
```
 
**描述**
 
为[GamePerformance_SceneInfo](#gameperformance_sceneinfo)实例设置场景ID。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向GamePerformance_SceneInfo实例。该值不可以为空，否则将返回错误码401。 |
| sceneID | 场景ID。 0：回切场景标识结束 1：游戏启动 2：游戏内更新 3：登录过程 4：主界面 5：加载一局游戏（自己加载） 6：加载一局游戏（自己加载完毕，等待其他玩家） 7：游戏中 8：观战模式 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_SceneInfo_SetSceneTime()

```text
GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetSceneTime (GamePerformance_SceneInfo *sceneInfo, const int64_t sceneTime)
```
 
**描述**
 
为[GamePerformance_SceneInfo](#gameperformance_sceneinfo)实例设置场景持续时间。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向GamePerformance_SceneInfo实例。该值不可以为空，否则将返回错误码401。 |
| sceneTime | 场景持续时间，单位：毫秒（ms）。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_SceneInfo_SetShaderCount()

```text
GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetShaderCount (GamePerformance_SceneInfo *sceneInfo, const int64_t shaderCount)
```
 
**描述**
 
为[GamePerformance_SceneInfo](#gameperformance_sceneinfo)实例设置每帧的平均shader数量。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向GamePerformance_SceneInfo实例。该值不可以为空，否则将返回错误码401。 |
| shaderCount | 每帧的平均shader数量。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_SceneInfo_SetSubDescription()

```text
GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetSubDescription (GamePerformance_SceneInfo *sceneInfo, const char *subDescription)
```
 
**描述**
 
为[GamePerformance_SceneInfo](#gameperformance_sceneinfo)实例设置子场景描述。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向GamePerformance_SceneInfo实例。该值不可以为空，否则将返回错误码401。 |
| subDescription | 游戏子场景描述（自定义描述）。字符长度范围：[0, 128]。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_SceneInfo_SetSubSceneID()

```text
GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetSubSceneID (GamePerformance_SceneInfo *sceneInfo, const char *subSceneID)
```
 
**描述**
 
为[GamePerformance_SceneInfo](#gameperformance_sceneinfo)实例设置子场景ID。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向GamePerformance_SceneInfo实例。该值不可以为空，否则将返回错误码401。 |
| subSceneID | 游戏子场景ID。字符长度范围：[0, 128]。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_SceneInfo_SetTextureCount()

```text
GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetTextureCount (GamePerformance_SceneInfo *sceneInfo, const int64_t textureCount)
```
 
**描述**
 
为[GamePerformance_SceneInfo](#gameperformance_sceneinfo)实例设置每帧的平均纹理数量。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向GamePerformance_SceneInfo实例。该值不可以为空，否则将返回错误码401。 |
| textureCount | 每帧的平均纹理数量。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_SceneInfo_SetTriangleCount()

```text
GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetTriangleCount (GamePerformance_SceneInfo *sceneInfo, const int64_t triangleCount)
```
 
**描述**
 
为[GamePerformance_SceneInfo](#gameperformance_sceneinfo)实例设置每帧的平均模型三角形数。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向GamePerformance_SceneInfo实例。该值不可以为空，否则将返回错误码401。 |
| triangleCount | 每帧的平均模型三角形数。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_SceneInfo_SetVertexCount()

```text
GamePerformance_ErrorCode HMS_GamePerformance_SceneInfo_SetVertexCount (GamePerformance_SceneInfo *sceneInfo, const int64_t vertexCount)
```
 
**描述**
 
为[GamePerformance_SceneInfo](#gameperformance_sceneinfo)实例设置每帧的平均模型顶点数。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向GamePerformance_SceneInfo实例。该值不可以为空，否则将返回错误码401。 |
| vertexCount | 每帧的平均模型顶点数。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_ThermalInfo_GetNowNormalizedCurrent()

```text
GamePerformance_ErrorCode HMS_GamePerformance_ThermalInfo_GetNowNormalizedCurrent (GamePerformance_ThermalInfo *thermalInfo, int32_t *nowCurrent)
```
 
**描述**
 
从[GamePerformance_ThermalInfo](#gameperformance_thermalinfo)中获取当前的工作电流。
 
**起始版本：** 6.0.2(22)
 
**设备行为差异：** 该接口在Phone中可正常调用，在其他设备类型中无返回值。
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| thermalInfo | 指针指向GamePerformance_ThermalInfo实例。该值不可以为空，否则将返回错误码1010300004。 |
| nowCurrent | 当前的工作电流，单位：mA。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_ERROR：参数错误。参数不能为空指针。 |
 
 
  

##### HMS_GamePerformance_ThermalInfo_GetRecommendMaxNormalizedCurrent()

```text
GamePerformance_ErrorCode HMS_GamePerformance_ThermalInfo_GetRecommendMaxNormalizedCurrent (GamePerformance_ThermalInfo *thermalInfo, int32_t *recommendMaxCurrent)
```
 
**描述**
 
从[GamePerformance_ThermalInfo](#gameperformance_thermalinfo)中获取系统建议的最大工作电流。
 
**起始版本：** 6.0.2(22)
 
**设备行为差异：** 该接口在Phone中可正常调用，在其他设备类型中无返回值。
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| thermalInfo | 指针指向GamePerformance_ThermalInfo实例。该值不可以为空，否则将返回错误码1010300004。 |
| recommendMaxCurrent | 系统建议的最大工作电流，单位：mA。 若当前的工作电流高于此值，设备会立即发烫。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_ERROR：参数错误。参数不能为空指针。 |
 
 
  

##### HMS_GamePerformance_ThermalInfo_GetRecommendNormalizedCurrent()

```text
GamePerformance_ErrorCode HMS_GamePerformance_ThermalInfo_GetRecommendNormalizedCurrent (GamePerformance_ThermalInfo *thermalInfo, int32_t *recommendCurrent)
```
 
**描述**
 
从[GamePerformance_ThermalInfo](#gameperformance_thermalinfo)中获取系统建议的工作电流。
 
**起始版本：** 6.0.2(22)
 
**设备行为差异：** 该接口在Phone中可正常调用，在其他设备类型中无返回值。
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| thermalInfo | 指针指向GamePerformance_ThermalInfo实例。该值不可以为空，否则将返回错误码1010300004。 |
| recommendCurrent | 系统建议的工作电流，单位：mA。 若当前的工作电流高于此值，温升趋势thermalTrend会大于0，设备有发烫风险。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_ERROR：参数错误。参数不能为空指针。 |
 
 
  

##### HMS_GamePerformance_ThermalInfo_GetThermalLevel()

```text
GamePerformance_ErrorCode HMS_GamePerformance_ThermalInfo_GetThermalLevel (GamePerformance_ThermalInfo *thermalInfo, int32_t *thermalLevel)
```
 
**描述**
 
从[GamePerformance_ThermalInfo](#gameperformance_thermalinfo)中获取温度等级。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| thermalInfo | 指针指向GamePerformance_ThermalInfo实例。该值不可以为空，否则将返回错误码401。 |
| thermalLevel | 温度等级，即温控档位，档位越高表示温度越高。不同档位及其建议如下： 1：无需处理。 2：建议降低无感知业务规格，例如后台更新降速或延迟运行。 3：建议暂停无感知业务，降低游戏非核心业务的规格，例如前台更新降速。 4：建议减少游戏特效，降低分辨率，画质。 5：建议降低全场景规格，进一步降低分辨率、画质等。 6：建议游戏降至最低规格。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_ThermalInfo_GetThermalMargin()

```text
GamePerformance_ErrorCode HMS_GamePerformance_ThermalInfo_GetThermalMargin (GamePerformance_ThermalInfo *thermalInfo, int32_t *thermalMargin)
```
 
**描述**
 
从温度信息[GamePerformance_ThermalInfo](#gameperformance_thermalinfo)中获取温度时间裕量。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| thermalInfo | 指针指向GamePerformance_ThermalInfo实例。该值不可以为空，否则将返回错误码401。 |
| thermalMargin | 时间裕量，温控到达指定档位的时间，负值表示系统无法预测。单位：秒（s）。 说明： - 该数值超过60时，可信度降低。 - 值为0：表示已达到查询的温控档位。 - 值为-1：表示不能到达。 - 值为-2：表示查询的档位低于当前档位。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_ThermalInfo_GetThermalTrend()

```text
GamePerformance_ErrorCode HMS_GamePerformance_ThermalInfo_GetThermalTrend (GamePerformance_ThermalInfo *thermalInfo, int32_t *thermalTrend)
```
 
**描述**
 
从温度信息[GamePerformance_ThermalInfo](#gameperformance_thermalinfo)中获取温升趋势。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| thermalInfo | 指针指向GamePerformance_ThermalInfo实例。该值不可以为空，否则将返回错误码401。 |
| thermalTrend | 温升趋势，取值范围为[-100, 100]，负号代表降温，数值越大说明当前温度变化越快。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_ThermalInfoQueryParameters_SetNeedsPrediction()

```text
GamePerformance_ErrorCode HMS_GamePerformance_ThermalInfoQueryParameters_SetNeedsPrediction (GamePerformance_ThermalInfoQueryParameters *parameters, const bool needsPrediction)
```
 
**描述**
 
为[GamePerformance_ThermalInfoQueryParameters](#gameperformance_thermalinfoqueryparameters)实例设置是否需要预测温升趋势。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| parameters | 指针指向GamePerformance_ThermalInfoQueryParameters实例。该值不可以为空，否则将返回错误码401。 |
| needsPrediction | 是否需要预测温升趋势。如果需要预测温升趋势，将返回温度时间裕量和温升趋势。 - true：需要 - false：不需要 默认为false。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_ThermalInfoQueryParameters_SetTargetThermalLevel()

```text
GamePerformance_ErrorCode HMS_GamePerformance_ThermalInfoQueryParameters_SetTargetThermalLevel (GamePerformance_ThermalInfoQueryParameters *parameters, const int32_t targetThermalLevel)
```
 
**描述**
 
为[GamePerformance_ThermalInfoQueryParameters](#gameperformance_thermalinfoqueryparameters)实例设置预测温升趋势的目标温度等级。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| parameters | 指针指向GamePerformance_ThermalInfoQueryParameters实例。该值不可以为空，否则将返回错误码401。 |
| targetThermalLevel | 预测温升趋势的目标温度等级。如果需要预测温升趋势，将根据该目标温度等级计算返回温度时间裕量和温度趋势。取值请参见温度等级。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 |
 
 
  

##### HMS_GamePerformance_UnregisterAllThermalLevelChangedCallbacks()

```text
GamePerformance_ErrorCode HMS_GamePerformance_UnregisterAllThermalLevelChangedCallbacks (void)
```
 
**描述**
 
取消注册所有温度变化回调。
 
**起始版本：** 5.0.2(14)
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_INTERNAL_ERROR：系统内部错误。 GAME_PERFORMANCE_INVALID_REQUEST：无效请求。 |
 
 
  

##### HMS_GamePerformance_UnregisterThermalLevelChangedCallback()

```text
GamePerformance_ErrorCode HMS_GamePerformance_UnregisterThermalLevelChangedCallback (GamePerformance_ThermalLevelChangedCallback callback)
```
 
**描述**
 
取消注册指定温度变化回调。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| callback | 回调函数GamePerformance_ThermalLevelChangedCallback。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 GAME_PERFORMANCE_INTERNAL_ERROR：系统内部错误。 GAME_PERFORMANCE_INVALID_REQUEST：无效请求。 |
 
 
  

##### HMS_GamePerformance_UpdateConfigInfo()

```text
GamePerformance_ErrorCode HMS_GamePerformance_UpdateConfigInfo (GamePerformance_ConfigInfo *configInfo)
```
 
**描述**
 
更新游戏配置信息。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| configInfo | 指针指向GamePerformance_ConfigInfo实例。该值不可以为空，否则将返回错误码401。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 GAME_PERFORMANCE_INTERNAL_ERROR：系统内部错误。 GAME_PERFORMANCE_INVALID_REQUEST：无效请求。 |
 
 
  

##### HMS_GamePerformance_UpdateNetInfo()

```text
GamePerformance_ErrorCode HMS_GamePerformance_UpdateNetInfo (GamePerformance_NetInfo *netInfo)
```
 
**描述**
 
更新游戏网络信息。
 
> [!NOTE]
> 调用HMS_GamePerformance_UpdateNetInfo前，必须已调用 HMS_GamePerformance_NetInfo_SetTotalLatency 设置totalLatency。

 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| netInfo | 指针指向GamePerformance_NetInfo实例。该值不可以为空，否则将返回错误码401。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 GAME_PERFORMANCE_INTERNAL_ERROR：系统内部错误。 GAME_PERFORMANCE_INVALID_REQUEST：无效请求。 |
 
 
  

##### HMS_GamePerformance_UpdatePackageInfo()

```text
GamePerformance_ErrorCode HMS_GamePerformance_UpdatePackageInfo (GamePerformance_PackageInfo *packageInfo)
```
 
**描述**
 
更新游戏包信息。
 
> [!NOTE]
> 调用HMS_GamePerformance_UpdatePackageInfo前，必须已调用 HMS_GamePerformance_InitParameters_SetBundleName 接口和 HMS_GamePerformance_InitParameters_SetAppVersion 接口，分别设置bundleName和appVersion。

 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| packageInfo | 指针指向GamePerformance_PackageInfo实例。该值不可以为空，否则将返回错误码401。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 GAME_PERFORMANCE_INTERNAL_ERROR：系统内部错误。 GAME_PERFORMANCE_INVALID_REQUEST：无效请求。 |
 
 
  

##### HMS_GamePerformance_UpdatePlayerInfo()

```text
GamePerformance_ErrorCode HMS_GamePerformance_UpdatePlayerInfo (GamePerformance_PlayerInfo *playerInfo)
```
 
**描述**
 
更新游戏玩家信息。
 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| playerInfo | 指针指向GamePerformance_PlayerInfo实例。该值不可以为空，否则将返回错误码401。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 GAME_PERFORMANCE_INTERNAL_ERROR：系统内部错误。 GAME_PERFORMANCE_INVALID_REQUEST：无效请求。 |
 
 
  

##### HMS_GamePerformance_UpdateSceneInfo()

```text
GamePerformance_ErrorCode HMS_GamePerformance_UpdateSceneInfo (GamePerformance_SceneInfo *sceneInfo)
```
 
**描述**
 
更新游戏场景信息。
 
> [!NOTE]
> 调用HMS_GamePerformance_UpdateSceneInfo前，必须已调用 HMS_GamePerformance_SceneInfo_SetSceneID 接口和 HMS_GamePerformance_SceneInfo_SetImportanceLevel 接口，分别设置sceneID和importanceLevel。

 
**起始版本：** 5.0.2(14)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| sceneInfo | 指针指向GamePerformance_SceneInfo实例。该值不可以为空，否则将返回错误码401。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| GamePerformance_ErrorCode | GAME_PERFORMANCE_SUCCESS：成功。 GAME_PERFORMANCE_PARAM_INVALID：无效参数。 GAME_PERFORMANCE_INTERNAL_ERROR：系统内部错误。 GAME_PERFORMANCE_INVALID_REQUEST：无效请求。 |
