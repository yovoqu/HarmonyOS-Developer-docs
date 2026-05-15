# Native侧如何通过char指针构造ArrayBuffer数组

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-59

可以通过napi_create_arraybuffer接口实现。

```cpp
#include "CharToArrBuffer.h"
napi_value CharToArrBuffer::TestCharBuf(napi_env env, napi_callback_info info) {
napi_value result = nullptr;
char *buf = nullptr;
// Create an Array buffer
napi_create_arraybuffer(env, 100, reinterpret_cast<void **>(&buf), &result);
// Assign an ArrayBuffer
for (int i = 0; i < 100; i++) {
buf[i] = i + 2;
}
return result;
}
```
