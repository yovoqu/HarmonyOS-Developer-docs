# Vulkan Surface开发指导

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vulkan-guidelines


## 场景介绍

在HarmonyOS中，扩展VK_OHOS_surface相关的API创建出来的VkSurfaceKHR会对接到本机窗口（OHNativeWindow）模块，实现本机缓冲区（OHNativeBuffer）的轮转，用于屏幕显示。

创建VkSurfaceKHR对象需要通过OHNativeWindow，而OHNativeWindow需要从XComponent中获取，所以此场景下需要配合XComponent模块和NativeWindow模块一起使用。XComponent模块的具体使用方法请参考[XComponent开发指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-xcomponent-guidelines)。


## 接口说明


| 接口名 | 描述 |
| --- | --- |
| vkCreateSurfaceOHOS (VkInstance instance, const VkSurfaceCreateInfoOHOS* pCreateInfo, const VkAllocationCallbacks* pAllocator, VkSurfaceKHR* pSurface) | 创建VkSurfaceKHR对象。 |


更多的接口说明请参考[Vulkan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vulkan)。


## 开发步骤

以下步骤说明了如何创建一个VkSurfaceKHR对象。

**HarmonyOS平台宏**

使用平台扩展的接口，需要定义一个宏VK_USE_PLATFORM_OHOS，我们在CMakeLists.txt定义这个宏。


```text
ADD_DEFINITIONS(-DVK_USE_PLATFORM_OHOS=1)
```

**添加动态链接库**

CMakeLists.txt中添加Vulkan的lib和周边模块的lib。


```text
libvulkan.so
libace_ndk.z.so
libnative_window.so
libnative_image.so
libnative_buffer.so
```


> [!NOTE]
> 在程序中通过dlopen函数链接libvulkan.so动态库时不需要在CMake中增加依赖，否则会导致符号冲突。

**头文件**


```text
#include <ace/xcomponent/native_interface_xcomponent.h>
#include <native_window/external_window.h>
#include <vulkan/vulkan.h>
```


1. **首先需要创建一个Vulkan实例**。       __PREBLOCK_3__
2. **获取OHNativeWindow**。       OHNativeWindow需要从XComponent组件中获取，下面提供一份从XComponent组件中获取OHNativeWindow的代码示例，XComponent模块的具体使用方法请参考[XComponent模块的介绍文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-xcomponent-guidelines)。                        ets/pages/Index.ets中增加一个XComponent组件。         __PREBLOCK_4__
3. 从XComponent组件中获取OHNativeWindow。         __PREBLOCK_5__

**创建VkSurfaceKHR对象**。


```text
VkSurfaceKHR surface = VK_NULL_HANDLE;
VkSurfaceCreateInfoOHOS surfaceCreateInfo = {};
surfaceCreateInfo.sType = VK_STRUCTURE_TYPE_SURFACE_CREATE_INFO_OHOS;
surfaceCreateInfo.window = nativeWindow; // 这里的nativeWindow就是从上一步骤OnSurfaceCreatedCB回调函数中拿到的
int err = vkCreateSurfaceOHOS(instance, &surfaceCreateInfo, NULL, &surface);
if (err != VK_SUCCESS) {
// Create Surface Failed.
}
```
