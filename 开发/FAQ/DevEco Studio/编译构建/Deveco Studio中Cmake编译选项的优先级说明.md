# DevEco Studio中Cmake编译选项的优先级说明

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-196

1. 常见的Cmake编译选项如下：
Cmakelists.txt中通过CACHE FORCE设置的参数。
2. Cmakelists.txt中缓存的变量。
3. CmakeLists.txt中环境变量配置的缓存。
```text
<span style="color: rgb(128,128,128);">#1</span><span style="color: rgb(128,128,128);">、采用</span><span style="color: rgb(128,128,128);">CACHE FORCE</span>
<span style="color: rgb(181,106,1);">set</span>(<span style="color: rgb(181,106,1);">CMAKE_BUILD_TYPE </span>debug <span style="color: rgb(181,106,1);">CACHE STRING </span><span style="color: rgb(80,160,79);">"Build type" </span>FORCE)
<span style="color: rgb(181,106,1);">message</span>(${<span style="color: rgb(181,106,1);">CMAKE_BUILD_TYPE</span>} <span style="color: rgb(80,160,79);">"CMAKE_BUILD_TYPE_FORCE"</span>)

<span style="color: rgb(128,128,128);">#2</span><span style="color: rgb(128,128,128);">、缓存变量</span>
<span style="color: rgb(181,106,1);">set</span>(<span style="color: rgb(181,106,1);">CMAKE_BUILD_TYPE </span>debug <span style="color: rgb(181,106,1);">CACHE STRING </span><span style="color: rgb(80,160,79);">"Build type"</span>)
<span style="color: rgb(181,106,1);">message</span>(${<span style="color: rgb(181,106,1);">CMAKE_BUILD_TYPE</span>} <span style="color: rgb(80,160,79);">"CMAKE_BUILD_TYPE"</span>)

<span style="color: rgb(128,128,128);">#3</span><span style="color: rgb(128,128,128);">、缓存环境变量</span>
<span style="color: rgb(181,106,1);">set</span>(<span style="color: rgb(181,106,1);">CMAKE_BUILD_TYPE </span>$ENV{<span style="color: rgb(181,106,1);">CMAKE_BUILD_TYPE</span>} <span style="color: rgb(181,106,1);">CACHE STRING </span><span style="color: rgb(80,160,79);">"Build type"</span>)
<span style="color: rgb(181,106,1);">message</span>($ENV{<span style="color: rgb(181,106,1);">CMAKE_BUILD_TYPE</span>} <span style="color: rgb(80,160,79);">"ENV_CMAKE_BUILD_TYPE"</span>)
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
<span style="color: rgb(132,63,161);">"externalNativeOptions"</span><span style="color: rgb(181,106,1);">: </span>{
      <span style="color: rgb(132,63,161);">"path"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"./src/main/cpp/CMakeLists.txt"</span><span style="color: rgb(181,106,1);">,</span>
<span style="color: rgb(128,128,128);">      "arguments": "-DCMAKE_BUILD_TYPE=debug",</span>
      <span style="color: rgb(132,63,161);">"cppFlags"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">""</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(132,63,161);">"cFlags"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">""</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(132,63,161);">"abiFilters"</span><span style="color: rgb(181,106,1);">: </span>[
        <span style="color: rgb(80,160,79);">"arm64-v8a"</span><span style="color: rgb(181,106,1);">,</span>      
<span style="color: rgb(80,160,79);">        "x86_64"</span>
      ]
    }
```

6. hvigor默认配置的-DCMAKE_BUILD_TYPE参数。
```text
<em>//</em><em><span style="color: rgb(132,63,161);"> "debuggable"</span>缺省或为true，或者buildMode为debug</em>
<span style="color: rgb(128,128,128);">-DCMAKE_BUILD_TYPE=debug</span>
<em>// </em><em><span style="color: rgb(132,63,161);">"debuggable"为false</span>，或者buildMode为release</em>
<span style="color: rgb(128,128,128);">-DCMAKE_BUILD_TYPE=release</span>
```

 
用户可根据实际需求动态配置CMake变量，使参数生效，DevEco Studio中Cmake缓存变量的优先级顺序如下所示（从高到低）：
 1. Cmakelists.txt中通过CACHE FORCE设置的参数。
2. 模块级build-profile.json5中"externalNativeOptions"->"arguments"显式配置的参数。
3. hvigor默认配置的-DCMAKE_BUILD_TYPE参数。
4. CmakePresets.json或CMakeUsersPersets.json中配置的参数。
5. Cmakelists.txt中缓存的变量及环境变量配置的缓存。
