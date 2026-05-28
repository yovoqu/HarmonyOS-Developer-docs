# 如何在Native侧构建一个ArkTS对象

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-45

1. 调用接口napi_create_object创建对象。
```cpp
// Create object arg_order in the native layer
napi_value arg_object;
napi_create_object(env, &arg_object);
```

2. 调用接口napi_set_named_property给对象属性赋值。
```cpp
napi_value testNum, testString;
// Set the property testNum and assign a value of 123 to the arg_order object created above
napi_create_int32(env, 123, &testNum);
napi_set_named_property(env, arg_object, "testNum", testNum);
// Set the property testString and assign 'Pure' to the arg_order object created above
napi_create_string_utf8(env, "Pure", NAPI_AUTO_LENGTH, &testString);
napi_set_named_property(env, arg_object, "testString", testString);
```
