# ABR进行Buffer分辨率调整引起其他Pass渲染效果异常，该如何解决？

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-faq-4

**现象描述**

以团结引擎URP管线为例，ABR对DrawOpaqueObjects绑定的Buffer进行分辨率调整时会引起SSAO shadow效果异常。

![](assets/ABR进行Buffer分辨率调整引起其他Pass渲染效果异常，该如何解决？/file-20260514131710558-0.png)

**原因分析**

通过上述URP管线可以看到，SSAO在渲染管线中是一个“前处理”，SSAO输出的图像会作为DrawOpaqueObjects的输入。当ABR对DrawOpaqueObjects绑定的Buffer进行自适应分辨率调整时，SSAO输出的图像为原始分辨率，而DrawOpaqueObjects绑定的Buffer使用低分辨率，分辨率不一致导致SSAO shadow效果异常。

**处理步骤**


支持渲染线程、RHI线程的游戏引擎处理步骤

对于同时支持渲染线程、RHI线程的游戏引擎，而且RHI线程延迟于渲染线程的场景，渲染线程通过[HMS_ABR_GetScale](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#hms_abr_getscale)接口获取的ABR Buffer分辨率因子无法解决上述问题。

对于该场景，渲染线程在Buffer渲染后调用[HMS_ABR_GetNextScale](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#hms_abr_getnextscale)接口获取下一帧的ABR Buffer分辨率因子，并根据Buffer分辨率因子对相关渲染数据进行同步调整。


```text
// 在Buffer渲染后调用
float scale = 1.0f;
errorCode = HMS_ABR_GetNextScale(context_, &scale);
if (errorCode != ABR_SUCCESS) {
    GOLOGE("HMS_ABR_GetNextScale execution failed, error code: %d.", errorCode);
}

// 根据Buffer分辨率因子对渲染数据进行同步调整
void SetViewUniformParameters()
{
    ViewUniformParameters.BufferSize.X = (int)(ViewUniformParameters.BufferSize.X * scale);
    ViewUniformParameters.BufferSize.Y = (int)(ViewUniformParameters.BufferSize.Y * scale);
    ViewUniformParameters.BufferInvSize.X /= scale;
    ViewUniformParameters.BufferInvSize.Y /= scale;
}
```
