# OpenGTX_GameSceneInfo

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___game_scene_info
**支持设备：** Phone / Tablet / TV


## 概述
**支持设备：** Phone / Tablet / TV

此结构体描述游戏场景信息，游戏应用获取到场景后传递此参数。

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate)

**所在头文件：** [opengtx_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/opengtx__base_8h)


## 汇总
**支持设备：** Phone / Tablet / TV


### 成员变量
**支持设备：** Phone / Tablet / TV


| 名称 | 描述 |
| --- | --- |
| [OpenGTX_SceneID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#opengtx_sceneid-1) [sceneID](#sceneid) | 游戏场景类型。 |
| char* [description](#description) | 对游戏场景的描述，字节长度范围[0,256]。 |
| int32_t [recommendFPS](#recommendfps) | 当前场景的建议帧率。取值范围0、[30,[targetFPS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___config_description#targetfps)]，若设置0则该值不生效。 |
| int32_t [minFPS](#minfps) | 当前场景预期的最小帧率。取值范围0、[30,[targetFPS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___config_description#targetfps)]，若设置0则该值不生效。 |
| int32_t [maxFPS](#maxfps) | 当前场景预期的最大帧率。取值范围0、[30,[targetFPS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___config_description#targetfps)]，若设置0则该值不生效。 |
| [OpenGTX_ResolutionValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___resolution_value) [resolutionCurValue](#resolutioncurvalue) | 当前场景的分辨率，取值范围360p-8k。 |


## 结构体成员变量说明
**支持设备：** Phone / Tablet / TV


### description
**支持设备：** Phone / Tablet / TV


```text
char* OpenGTX_GameSceneInfo::description
```

**描述**

对游戏场景的描述，字节长度范围[0,256]。


### maxFPS
**支持设备：** Phone / Tablet / TV


```text
int32_t OpenGTX_GameSceneInfo::maxFPS
```

**描述**

当前场景预期的最大帧率。取值范围0、[30,[targetFPS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___config_description#targetfps)]，若设置0则该值不生效。


### minFPS
**支持设备：** Phone / Tablet / TV


```text
int32_t OpenGTX_GameSceneInfo::minFPS
```

**描述**

当前场景预期的最小帧率。取值范围0、[30,[targetFPS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___config_description#targetfps)]，若设置0则该值不生效。


### recommendFPS
**支持设备：** Phone / Tablet / TV


```text
int32_t OpenGTX_GameSceneInfo::recommendFPS
```

**描述**

当前场景的建议帧率。取值范围0、[30,[targetFPS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___config_description#targetfps)]，若设置0则该值不生效。


### resolutionCurValue
**支持设备：** Phone / Tablet / TV


```text
OpenGTX_ResolutionValue OpenGTX_GameSceneInfo::resolutionCurValue
```

**描述**

当前场景的分辨率，取值范围360p-8k。


### sceneID
**支持设备：** Phone / Tablet / TV


```text
OpenGTX_SceneID OpenGTX_GameSceneInfo::sceneID
```

**描述**

游戏场景类型。
