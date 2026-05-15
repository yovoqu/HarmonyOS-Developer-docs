# 使用eglSwapBuffers API，eglSwapBuffers执行报错错误码：EGL_BAD_ALLOC。

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-10

编码器通过 OH_VideoEncoder_GetSurface(encoder_, &NativeWindow) 获取 NativeWindow，使用该 NativeWindow 创建 Encoder 的 EGLSurface 来接收 OpenGL 的纹理数据。若未调用 OH_NativeWindow_NativeWindowHandleOpt(nativeWindow, SET_BUFFER_GEOMETRY, height, width) 设置 buffer 大小，在调用 eglSwapBuffers API 时会报错。
