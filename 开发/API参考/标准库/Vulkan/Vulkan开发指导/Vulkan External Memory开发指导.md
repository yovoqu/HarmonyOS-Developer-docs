# Vulkan External Memory开发指导

更新时间：2026-04-24 08:10:21

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vulkan-oh-external-memory-guidelines


## 场景介绍

VK_OHOS_external_memory 扩展用于在GPU Vulkan环境下与HarmonyOS的本机缓冲区（OHNativeBuffer）之间做零拷贝的内存共享。

该扩展允许：把由HarmonyOS或其他组件（Camera、RenderService、视频解码器、OHNativeWindow等）创建的OHNativeBuffer导入为Vulkan内存（并绑定到VkImage/VkBuffer）。

这可以实现视频帧、相机输出、图像解码器等在生产端与Vulkan渲染/计算端的高效共享，避免额外拷贝或像素转换。

所以，本指导将介绍实现视频解码器与渲染器零拷贝：将解码器输出OHNativeBuffer，直接导入Vulkan。


## 接口说明


### 结构体


| 名称 | 描述 |
| --- | --- |
| [VkNativeBufferPropertiesOHOS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vknativebufferpropertiesohos) | 包含了NativeBuffer的属性。 |
| [VkNativeBufferFormatPropertiesOHOS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vknativebufferformatpropertiesohos) | 包含了NativeBuffer的一些格式属性。 |
| [VkImportNativeBufferInfoOHOS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vkimportnativebufferinfoohos) | 包含了OH_NativeBuffer结构体的指针。 |
| [VkMemoryGetNativeBufferInfoOHOS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vkmemorygetnativebufferinfoohos) | 用于从Vulkan内存中获取OH_NativeBuffer。 |
| [VkExternalFormatOHOS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vkexternalformatohos) | 表示外部定义的格式标识符。 |


### 函数


| 名称 | 描述 |
| --- | --- |
| VKAPI_ATTR VkResult VKAPI_CALL [vkGetNativeBufferPropertiesOHOS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-ohos-h#vkgetnativebufferpropertiesohos) (VkDevice device, const struct OH_NativeBuffer *buffer, [VkNativeBufferPropertiesOHOS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vknativebufferpropertiesohos) *pProperties) | 获取OH_NativeBuffer属性。 |


## 开发步骤

以下步骤说明了如何将视频解码器输出的本机缓冲区（OHNativeBuffer）导入为Vulkan内存，并绑定到VkImage/VkBuffer。


1. 启动渲染子线程，初始化Vulkan环境，动态加载libvulkan.so, 并加载Vulkan基础函数的指针。  __PREBLOCK_0__   动态加载libvulkan.so，并加载Vulkan基础函数的指针。  __PREBLOCK_1__
2. 创建NativeImage对象作为OHNativeBuffer的消费端，并根据NativeImage对象获取对应的NativeWindow对象，将NativeWindow句柄传给视频编解码，作为OHNativeBuffer的生产端，用于生产视频帧内容。  __PREBLOCK_2__
3. 获取XComponent的NativeWindow对象，根据NativeWindow对象创建出Vulkan环境的VkSurface，用于绘制显示内容。  __PREBLOCK_3__   同时更新初始化Vulkan的上下文，包括Vulkan的实列、选择物理设备、创建渲染管线等。  __PREBLOCK_4__   通过vkCreateSurfaceOHOS()创建VkSurface对象。  __PREBLOCK_5__
4. 初始化视频解码的环境，包括初始化解封装器、初始化解码器。  __PREBLOCK_6__
5. 启动解码器、解码输入子线程、解码输出子线程。  __PREBLOCK_7__
6. 在解码输入子线程中，通过解封装器读取视频数据，并交给解码器。  __PREBLOCK_8__
7. 在解码输出子线程中，将解码后的视频提交给输出Surface。  __PREBLOCK_9__
8. 在NativeImage有可用数据后，通过OH_NativeImage_AcquireNativeWindowBuffer()获取视频数据，并通过OH_NativeBuffer_FromNativeWindowBuffer()转化NativeBuffer的类型。  __PREBLOCK_10__
9. Vulkan根据NativeBuffer创建对应的ImageView用于渲染显示，同时创建对应格式的采样器，将YUV格式的图像采样成RGBA的图像，用于正确的渲染显示。  ![](assets/Vulkan%20External%20Memory开发指导/file-20260514165305315-0.png)   API version 23之前，基于标准库VkExternalMemoryImageCreateInfo结构体，系统支持扩展类型VK_EXTERNAL_MEMORY_HANDLE_TYPE_OHOS_NATIVE_BUFFER_BIT_OHOS。
10. 从API version 23开始，VK_EXTERNAL_MEMORY_HANDLE_TYPE_OHOS_NATIVE_BUFFER_BIT_OHOS已废弃，请改用VK_EXTERNAL_MEMORY_HANDLE_TYPE_OH_NATIVE_BUFFER_BIT_OHOS。
