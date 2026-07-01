# 链接系统网络库librcp_c.so报错unable to find library -lrcp_c

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-remote-communication-8

#### 问题现象

使用Remote Communication Kit能力时，在项目中集成librcp_c.so，在CMakeLists.txt配置系统库依赖：
 
```text
<span style="color: rgb(0,0,255);">target_link_libraries</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">mmm PRIVATE</span>
<span style="color: rgb(0,0,255);">ace_napi</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">z</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">so</span>
<span style="color: rgb(0,0,255);">libhilog_ndk</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">z</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">so</span>
<span style="color: rgb(0,0,255);">librcp_c</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">so</span>
<span style="color: rgb(0,0,255);">z</span>）
```
 
在生成共享库libopenai.so时，链接器（clang++ + lld）报错：
 
```cpp
<span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">hvigor </span><span style="color: rgb(181,106,1);">ERROR</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Failed </span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(181,106,1);">openai</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(0,0,255);">default</span><span style="color: rgb(181,106,1);">@</span><span style="color: rgb(0,0,255);">BuildNativeWithNinja</span><span style="color: rgb(181,106,1);">...</span>
<span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">hvigor </span><span style="color: rgb(181,106,1);">ERROR</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Exceptions happened </span>while <span style="color: rgb(0,0,255);">executing</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ninja</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Entering directory </span><span style="color: rgb(255,0,170);">`D:\Develop\Code\HarmonyOS\MyNextAI\openai\.cxx\default\default\debug\x86_64'</span>
<span style="color: rgb(255,0,170);">[1/1] Linking CXX shared library D:\Develop\Code\HarmonyOS\MyNextAI\openai\build\default\intermediates\cmake\default\obj\x86_64\libopenai.so</span>
<span style="color: rgb(255,0,170);">FAILED: D:/Develop/Code/HarmonyOS/MyNextAI/openai/build/default/intermediates/cmake/default/obj/x86_64/libopenai.so</span>
<span style="color: rgb(255,0,170);">C:\WINDOWS\system32\cmd.exe /C "cd . </span><span style="color: rgb(255,0,170);">&</span><span style="color: rgb(255,0,170);">&</span><span style="color: rgb(255,0,170);"> "D:\Develop\Tools\Huawei\DevEco Studio\sdk\default\openharmony\native\llvm\bin\clang++.exe" --target=x86_64-linux-ohos --gcc-toolchain="D:/Develop/Tools/Huawei/DevEco Studio/sdk/default/openharmony/native/llvm" --sysroot="D:/Develop/Tools/Huawei/DevEco Studio/sdk/default/openharmony/native/sysroot" -fPIC -fdata-sections -ffunction-sections -funwind-tables -fstack-protector-strong -no-canonical-prefixes -fno-addrsig -Wa,--noexecstack -Wformat -Werror=format-security --std=c++17 -D__MUSL__ -O0 -g -fno-limit-debug-info --rtlib=compiler-rt -fuse-ld=lld -Wl,--build-id=sha1 -Wl,--warn-shared-textrel -Wl,--fatal-warnings -lunwind -Wl,--no-undefined -Qunused-arguments -Wl,-z,noexecstack -shared -Wl,-soname,libopenai.so -o D:\Develop\Code\HarmonyOS\MyNextAI\openai\build\default\intermediates\cmake\default\obj\x86_64\libopenai.so CMakeFiles/openai.dir/napi_init.cpp.o CMakeFiles/openai.dir/liboai/components/audio.cpp.o CMakeFiles/openai.dir/liboai/components/azure.cpp.o CMakeFiles/openai.dir/liboai/components/chat.cpp.o CMakeFiles/openai.dir/liboai/components/completions.cpp.o CMakeFiles/openai.dir/liboai/components/edits.cpp.o CMakeFiles/openai.dir/liboai/components/embeddings.cpp.o CMakeFiles/openai.dir/liboai/components/files.cpp.o CMakeFiles/openai.dir/liboai/components/fine_tunes.cpp.o CMakeFiles/openai.dir/liboai/components/images.cpp.o CMakeFiles/openai.dir/liboai/components/models.cpp.o CMakeFiles/openai.dir/liboai/components/moderations.cpp.o CMakeFiles/openai.dir/liboai/core/authorization.cpp.o CMakeFiles/openai.dir/liboai/core/netimpl.cpp.o CMakeFiles/openai.dir/liboai/core/response.cpp.o CMakeFiles/openai.dir/openai/openai_native.cpp.o CMakeFiles/openai.dir/openai/openai_native_chat.cpp.o -lace_napi.z -lrcp_c -lm </span><span style="color: rgb(255,0,170);">&</span><span style="color: rgb(255,0,170);">&</span><span style="color: rgb(255,0,170);"> cd ."</span>
<span style="color: rgb(255,0,170);">ld.lld: error: unable to find library -lrcp_c</span>
<span style="color: rgb(255,0,170);">clang++: error: linker command failed with exit code 1 (use -v to see invocation)</span>
<span style="color: rgb(255,0,170);">ninja: build stopped: subcommand failed.</span>
```
 
 

#### 背景知识

Remote Communication Kit提供了网络数据请求功能，相较于Network Kit中HTTP请求能力，更具易用性，且拥有更多的功能。
 
Remote Communication Kit还提供了URPC（Unified Remote Procedure Call）高性能rpc通信库，拥有构筑远程函数调用能力，具有抗弱网传输、多径传输（5G和Wifi）等特征。应用可以通过URPC完成简单方便的远程过程调用。
 
 

#### 问题定位
1. 查看编译报错，报错根因在：error: unable to find library -lrcp_c。
2. 检查librcp_c.so文件是否存在，存放路径是否正确。
3. 检查工具链配置是否存在，C API使用时还需要在CMakeLists.txt中设置动态库路径及头文件路径，并进行链接。
 
 

#### 分析结论

查看编译报错可知，找不到lrcp_c库，librcp_c.so为系统库，无需复制进lib文件夹，此问题一般为缺少工具链配置导致，检查CmakeLists.txt文件发现HarmonyOS NDK的sysroot路径未配置。
 
 

#### 修改建议

在链接librcp_c.so前添加以下配置：
 
```text
<span style="color: rgb(0,0,255);">target_include_directories</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">entry PUBLIC $</span><span style="color: rgb(255,0,170);">{</span><span style="color: rgb(0,0,255);">HMOS_SDK_NATIVE</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">/sysroot/us</span>r<span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">include</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(0,0,255);">target_link_directories</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">entry PUBLIC $</span><span style="color: rgb(255,0,170);">{</span><span style="color: rgb(0,0,255);">HMOS_SDK_NATIVE</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">/sysroot/us</span>r<span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">lib</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">aarch64</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(0,0,255);">linux</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(0,0,255);">ohos</span><span style="color: rgb(0,0,255);">)</span>
```
