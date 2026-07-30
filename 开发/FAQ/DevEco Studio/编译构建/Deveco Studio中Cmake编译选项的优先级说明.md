# DevEco Studio中Cmake编译选项的优先级说明

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-196

1. 常见的Cmake编译选项如下：
Cmakelists.txt中通过CACHE FORCE设置的参数。
2. Cmakelists.txt中缓存的变量。
3. CmakeLists.txt中环境变量配置的缓存。
```text
#1、采用CACHE FORCE
set(CMAKE_BUILD_TYPE debug CACHE STRING "Build type" FORCE)
message(${CMAKE_BUILD_TYPE} "CMAKE_BUILD_TYPE_FORCE")

#2、缓存变量
set(CMAKE_BUILD_TYPE debug CACHE STRING "Build type")
message(${CMAKE_BUILD_TYPE} "CMAKE_BUILD_TYPE")

#3、缓存环境变量
set(CMAKE_BUILD_TYPE $ENV{CMAKE_BUILD_TYPE} CACHE STRING "Build type")
message($ENV{CMAKE_BUILD_TYPE} "ENV_CMAKE_BUILD_TYPE")
```

4. CmakePresets.json或CMakeUsersPersets.json中配置的参数。
```text
{
    "version":3,
    "configurePresets":[
        {
            "name":"debug",
            "displayName":"Build type",
            "description":"Build type debug preset",
            "cacheVariables":{
                "CMAKE_BUILD_TYPE":"Debug"
            }
        }
    ]
}
```

5. DevEco Studio自定义Cmake编译选项如下：
模块级build-profile.json5中"externalNativeOptions"->"arguments"显式配置的参数。
```text
"externalNativeOptions": {
      "path": "./src/main/cpp/CMakeLists.txt",
      "arguments": "-DCMAKE_BUILD_TYPE=debug",
      "cppFlags": "",
      "cFlags": "",
      "abiFilters": [
        "arm64-v8a",      
        "x86_64"
      ]
    }
```

6. hvigor默认配置的-DCMAKE_BUILD_TYPE参数。
```text
<em>//</em><em> "debuggable"缺省或为true，或者buildMode为debug</em>
-DCMAKE_BUILD_TYPE=debug
<em>// </em><em>"debuggable"为false，或者buildMode为release</em>
-DCMAKE_BUILD_TYPE=release
```

 
用户可根据实际需求动态配置CMake变量，使参数生效，DevEco Studio中Cmake缓存变量的优先级顺序如下所示（从高到低）：
 1. Cmakelists.txt中通过CACHE FORCE设置的参数。
2. 模块级build-profile.json5中"externalNativeOptions"->"arguments"显式配置的参数。
3. hvigor默认配置的-DCMAKE_BUILD_TYPE参数。
4. CmakePresets.json或CMakeUsersPersets.json中配置的参数。
5. Cmakelists.txt中缓存的变量及环境变量配置的缓存。
