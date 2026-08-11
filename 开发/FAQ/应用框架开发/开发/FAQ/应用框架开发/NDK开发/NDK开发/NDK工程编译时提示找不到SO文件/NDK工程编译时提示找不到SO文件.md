# NDK工程编译时提示找不到SO文件

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-development-13

#### 问题现象

Native工程导入库以及编译的时候，遇到找不到库文件或者引用的函数符号。
 
报错日志参考如下：
 
```text
<span style="color: rgb(181,106,1);">Cause</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Can</span>'t <span style="color: rgb(0,0,255);">find any </span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">so file </span>in <span style="color: rgb(0,0,255);">the xxx</span>
```
 
```text
<span style="color: rgb(0,0,255);">CMake Error at CMakeLists</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">txt</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(0,0,255);">XXX </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">find_package</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">:</span>
<span style="color: rgb(0,0,255);">find a package configuration file provided by XXX</span>
<span style="color: rgb(0,0,255);">but it set XX_FLAG to </span>false <span style="color: rgb(0,0,255);">so package is considered to be NOT FOUND</span>
```
 
 

#### 背景知识

HarmonyOS上[使用DevEco Studio模板构建NDK工程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/build-with-ndk-ide)，其核心编译过程如下：
 
根据[CMake配置脚本](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/build-with-ndk-ide#cmakeliststxt)以及[build-profile.json5](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-profile-app)中配置的[externalNativeOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/build-with-ndk-ide#externalnativeoptions)构建参数，与缓存中的配置比对后，生成CMake命令并执行CMake，按照makefile执行编译和链接，将生成的.so以及运行时依赖的.so同步到输出目录，完成构建过程。
 
 

#### 问题定位

当遇到编译找不到SO文件的时候，需要做以下几个方向的排查：
 1. 通过错误日志锁定问题SO的名字，并在CMakeLists.txt文件中找到对应的配置项。
2. 如果配置项语法没有问题，则检查是否存在工程对应的SO存放路径。
3. 查看是否有编译缓存文件。
4. 检查预编译SO的SONAME，文件拷贝是否正确。
5. 检查该预编译的SO中依赖的其他库是否都存在。
 
 

#### 分析结论
1. 可能是CMake配置里，对应的SO关联的选项未打开，或者未配置库的搜索路径。
2. 可能对应的SO文件未拷贝或者未生成到对应的路径下。
3. 可能之前的编译缓存影响，编译使用了缓存，未刷新成正确的配置。
4. 应用在引用动态库的时候是通过SONAME来查找的，开发者需要将SONAME对应的库文件拷贝到entry/libs/${OHOS_ARCH}/目录下。查询命令：llvm-readelf -d xxx.so。查询命令：llvm-readelf -d xxx.so。

  
```text
<span style="color: rgb(0,0,255);">$ llvm</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(0,0,255);">readelf </span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(0,0,255);">d xxx</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">so</span>

<span style="color: rgb(0,0,255);">Dynamic section at offset </span><span style="color: rgb(0,0,255);">0xad00a0 </span><span style="color: rgb(0,0,255);">contains </span><span style="color: rgb(255,0,0);">31 </span><span style="color: rgb(181,106,1);">entries</span><span style="color: rgb(181,106,1);">:</span>
  <span style="color: rgb(0,0,255);">Tag        Type                         Name</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">Value</span>
<span style="color: rgb(0,0,255);">0x000000000000001d (</span><span style="color: rgb(0,0,255);">RUNPATH</span><span style="color: rgb(0,0,255);">)            </span><span style="color: rgb(0,0,255);">Library </span><span style="color: rgb(181,106,1);">runpath</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">$ORIGIN</span><span style="color: rgb(181,106,1);">/..</span><span style="color: rgb(255,0,170);">/../</span><span style="color: rgb(181,106,1);">..</span><span style="color: rgb(255,0,170);">/mapi/s</span><span style="color: rgb(0,0,255);">hared</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(0,0,255);">glapi</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,170);">/xxx/</span><span style="color: rgb(0,0,255);">ohos</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(0,0,255);">sdk</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">thirdparty</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">libxxx</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,170);">/xxx/</span><span style="color: rgb(0,0,255);">ohos</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(0,0,255);">sdk</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">hiviewdfx</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(0,0,255);">hilog</span><span style="color: rgb(0,0,255);">]</span>
<span style="color: rgb(0,0,255);">0x0000000000000001 (</span><span style="color: rgb(0,0,255);">NEEDED</span><span style="color: rgb(0,0,255);">)             </span><span style="color: rgb(0,0,255);">Shared </span><span style="color: rgb(181,106,1);">library</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">libglapi</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">so</span><span style="color: rgb(255,0,0);">.0</span><span style="color: rgb(0,0,255);">]</span>
<span style="color: rgb(0,0,255);">0x0000000000000001 (</span><span style="color: rgb(0,0,255);">NEEDED</span><span style="color: rgb(0,0,255);">)             </span><span style="color: rgb(0,0,255);">Shared </span><span style="color: rgb(181,106,1);">library</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">libz</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">so</span><span style="color: rgb(0,0,255);">]</span>
<span style="color: rgb(0,0,255);">0x0000000000000001 (</span><span style="color: rgb(0,0,255);">NEEDED</span><span style="color: rgb(0,0,255);">)             </span><span style="color: rgb(0,0,255);">Shared </span><span style="color: rgb(181,106,1);">library</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">libhilog</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">so</span><span style="color: rgb(0,0,255);">]</span>
<span style="color: rgb(0,0,255);">0x0000000000000001 (</span><span style="color: rgb(0,0,255);">NEEDED</span><span style="color: rgb(0,0,255);">)             </span><span style="color: rgb(0,0,255);">Shared </span><span style="color: rgb(181,106,1);">library</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">libc</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(0,0,255);">_shared</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">so</span><span style="color: rgb(0,0,255);">]</span>
<span style="color: rgb(0,0,255);">0x0000000000000001 (</span><span style="color: rgb(0,0,255);">NEEDED</span><span style="color: rgb(0,0,255);">)             </span><span style="color: rgb(0,0,255);">Shared </span><span style="color: rgb(181,106,1);">library</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">libc</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">so</span><span style="color: rgb(0,0,255);">]</span>
<span style="color: rgb(0,0,255);">0x000000000000000e (</span><span style="color: rgb(0,0,255);">SONAME</span><span style="color: rgb(0,0,255);">)             </span><span style="color: rgb(0,0,255);">Library </span><span style="color: rgb(181,106,1);">soname</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">libaaa</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">so</span><span style="color: rgb(0,0,255);">]</span>
```

1. 使用上述命令查看依赖的SO（NEEDED）。需要把依赖的SO添加到工程中并在CMakeLists.txt链接。
 
 

#### 修改建议
1. 检查并更正对应的配置选项。
2. 拷贝SO到对应的路径下。
3. 删除缓存的.CXX文件夹，重新执行编译。
4. Native工程引入SO库时需要SONAME对应的库文件拷贝到entry/libs/${OHOS_ARCH}/目录下。
5. Native工程引入SO库时要将其依赖项同步链接到工程中。
 
 

#### 常见FAQ

Q：编译的第三方库SONAME必须是libxxx.so.x或者libxxx.so格式的么？
 
A：三方SO库并没有强制要求必须是libxxx.so.x或者libxxx.so格式。但出于规范性和安全性考虑，避免出现文件内SO信息和文件名一致性等问题，建议按照libxxx.so标准格式设计SONAME，也方便出错时可以快速定位。
