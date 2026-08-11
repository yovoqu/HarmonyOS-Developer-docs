# 打包App报错：input module vendor is different

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-204

#### 问题现象

打包App时报错。
 
```text
<span style="color: rgb(255,255,255);">hvigor ERROR</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">Failed </span><span style="color: rgb(181,106,1);">::</span><span style="color: rgb(255,255,255);">PackageApp</span><span style="color: rgb(181,106,1);">...</span>
<span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,255,255);">hvigor ERROR</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">Tools execution failed</span><span style="color: rgb(181,106,1);">.</span>
<span style="color: rgb(80,160,79);">2024</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(80,160,79);">03</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(80,160,79);">03 11</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(80,160,79);">31</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(80,160,79);">45.825 </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,255,255);">Ohos BundleTool </span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(255,255,255);">Error</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">input </span>module vendor <span style="color: rgb(255,255,255);">is different</span><span style="color: rgb(181,106,1);">.</span>
<span style="color: rgb(80,160,79);">2024</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(80,160,79);">03</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(80,160,79);">03 11</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(80,160,79);">31</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(80,160,79);">45.827 </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,255,255);">Ohos BundleTool </span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(255,255,255);">Error</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">some app variable is different</span><span style="color: rgb(181,106,1);">.</span>
<span style="color: rgb(80,160,79);">2024</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(80,160,79);">03</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(80,160,79);">03 11</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(80,160,79);">31</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(80,160,79);">45.827 </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,255,255);">Ohos BundleTool </span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(255,255,255);">Error</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">Compressor</span><span style="color: rgb(181,106,1);">::</span><span style="color: rgb(255,255,255);">compressAppMode compress failed</span><span style="color: rgb(181,106,1);">.</span>
<span style="color: rgb(80,160,79);">2024</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(80,160,79);">03</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(80,160,79);">03 11</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(80,160,79);">31</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(80,160,79);">45.840 </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,255,255);">Ohos BundleTool </span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(255,255,255);">Error</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">Compressor</span><span style="color: rgb(181,106,1);">::</span><span style="color: rgb(255,255,255);">compressProcess Bundle exception</span><span style="color: rgb(181,106,1);">.</span>
<span style="color: rgb(80,160,79);">2024</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(80,160,79);">03</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(80,160,79);">03 11</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(80,160,79);">31</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(80,160,79);">45.840 </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,255,255);">Ohos BundleTool </span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(255,255,255);">Error</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">Compressor</span><span style="color: rgb(181,106,1);">::</span><span style="color: rgb(255,255,255);">compressProcess compress failed</span><span style="color: rgb(181,106,1);">.</span>
<span style="color: rgb(80,160,79);">2024</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(80,160,79);">03</span><span style="color: rgb(181,106,1);">/</span><span style="color: rgb(80,160,79);">03 11</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(80,160,79);">31</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(80,160,79);">45.841 </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,255,255);">Ohos BundleTool </span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(255,255,255);">Error</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">CompressEntrance</span><span style="color: rgb(181,106,1);">::</span><span style="color: rgb(255,255,255);">main exit</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">compress failed</span>
```
 
 

#### 背景知识

vendor标识对应用开发厂商的描述，取值为长度不超过255字节的字符串。该字段可用于展示开发厂商信息，如在应用的关于页面，取该字段展示开发厂商信息。
 
 

#### 问题定位

报错提示：input module vendor is different，打包模块的vendor不一致。检查各模块的vendor字段是否存在且一致。
 
 

#### 分析结论

- **场景一**： 打包模块的vendor不一致。
- **场景二**： app.json5文件缺失了vendor字段。

 
 

#### 修改建议

- **场景一**：打包时检查应用了哪些模块，使各模块的vendor配置保持一致。排查方法如下：1. File->Settings->Build, Execution, Deployment->Build Tools->Hvigor中将Use log level改成Debug。

2. 重新执行Build apps。

3. Build日志中搜索“app_packing_tool”，查看入参：--hap-path、--hsp-path的对应信息，可得构建app时所有依赖的hsp和hap。

4. hsp和hap的vendor要一致。
- **场景二**： 在app.json5中补全vendor字段信息。
```text
{
  <span style="color: rgb(132,63,161);">"app"</span><span style="color: rgb(181,106,1);">: </span>{
    <span style="color: rgb(132,63,161);">"vendor"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"example"</span><span style="color: rgb(181,106,1);">,</span>
    <em><span style="color: rgb(128,128,128);">// ...</span></em>
  }
}
```


 
 

#### 常见FAQ

Q：打包App时报错：input module minAPIVersion is different，该如何解决？
 
A：出现该报错原因是模块间minAPIVersion配置不一致或app.json5中未统一声明minAPIVersion。可手动检查并统一各模块的minAPIVersion字段，同时确保在app.json5中声明该字段，然后重新打包App即可。
 
 

#### 总结

vendor是标识应用供应商的核心字段，需在应用配置文件和模块配置文件中统一设置，且不同模块间的值必须完全一致以确保安装成功。
