# 通过命令行获取profile文件中的bundleName信息失败怎么办

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-198

#### 问题现象

搭建流水线时通过cat命令行查看获取profile文件中的信息为乱码，没办法校验bundleName（包名）。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/Kd5PbOgVTjaaJlcPoIaEvA/zh-cn_image_0000002658808545.png?HW-CC-KV=V1&HW-CC-Date=20260723T013917Z&HW-CC-Expire=86400&HW-CC-Sign=8F5D9A44FC5B581E6B74C5613771BAE47D54EDA48964C4E8460AE14F52DCB22E)

 
 

#### 知识背景
1. **为什么要校验profile中的包名**？签名可能会因为签名所需要的profile文件与工程中的包名不同、当前不在profile有效期内等原因导致签名失败，提前校验可以尽早发现问题，符合测试左移的工程原则。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/25_ODtnnRYONWZ3BDnsoZQ/zh-cn_image_0000002628569170.png?HW-CC-KV=V1&HW-CC-Date=20260723T013917Z&HW-CC-Expire=86400&HW-CC-Sign=5D22460C65CE8AE2F3FDA27E32CE2832902319241B6035D56B03B03E46E72A5A)


  此校验过程在搭建流水过程中下图的红框部分，构建后签名前的校验脚本中。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/mGnvwQzDRPiVLxCEV2xHkA/zh-cn_image_0000002658928495.png?HW-CC-KV=V1&HW-CC-Date=20260723T013917Z&HW-CC-Expire=86400&HW-CC-Sign=692E4C753DC24A5FF6C412FB28ABD264B008D0549E318F24B43D0E29DE653E54)

2. **签名的作用**。
应用身份识别：每个包文件都有一个唯一的签名，系统通过它来识别应用的身份。
3. 保证应用完整性：签名能够确保包文件在传输和安装过程中没有被篡改。如果文件被修改，签名就会失效，系统就不会安装这个应用。
4. 应用升级校验：当应用需要升级时，系统会检查新版本的签名是否与旧版本一致，从而确保升级是来自同一个开发者。
5. 权限授予：某些系统级权限的授予会基于签名，比如ACL权限和消息推送等。
6. **Profile文件**。Profile格式为.p7b，包含HarmonyOS应用/元服务的包名、数字证书信息、HarmonyOS应用/元服务允许申请的证书权限列表，以及允许应用/元服务调试的设备列表（如果应用/元服务类型为Release类型，则设备列表为空）等内容。Profile文件分为调试Profile和发布Profile两种。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/bPQwPGuVTQCIFZyZSeEN7w/zh-cn_image_0000002628409276.png?HW-CC-KV=V1&HW-CC-Date=20260723T013917Z&HW-CC-Expire=86400&HW-CC-Sign=125E8720175D72B9161DD6A20BCF6E15979C007F5AB1745AB5407379306ECF26)

7. **[搭建流水线](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-command-line-building-app)**。
 
 

#### 问题定位

cat命令为Linux查看文件内容的命令，但profile文件不是纯文本信息，使用cat查看会出现乱码。
 
 

#### 分析结论

无法直接通过查看profile文件获取bundleName。
 
 

#### 修改建议

通过命令行工具提供的hap-sign-tool.jar 获取profile中的信息保存至变量或者文件中。
 
```json
<span style="color: rgb(0,0,255);">json</span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(0,0,255);">$</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">java </span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(0,0,255);">jar hap</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(0,0,255);">sign</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(0,0,255);">tool</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">jar verify</span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(0,0,255);">profile </span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(0,0,255);">inFile testDebug</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">p7b</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(0,0,255);">key</span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(255,0,170);">'bundle-name'</span>
<span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(0,0,255);">$</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">echo $json </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">awk </span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(0,0,255);">v k</span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(255,0,170);">'$key' 'BEGIN{RS='</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(255,0,170);">'; FS='</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(255,0,170);">'} $1 ~ '</span>\<span style="color: rgb(255,0,170);">''</span>k<span style="color: rgb(255,0,170);">'</span>\'<span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">{</span><span style="color: rgb(0,0,255);">gsub</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">/[{}']/</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">,</span><span style="color: rgb(0,0,255);">$2</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">print $2</span><span style="color: rgb(255,0,170);">}</span>'<span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(0,0,255);">echo $value</span>
```
 
然后再通过cat或者awk解析出profile中的bundle-name的值，再与项目文件app.json中的bundleName比较即可。
 
 

#### 总结

签名能够确保文件在传输和安装过程中没有被篡改，在搭建流水线时，可以通过官网提供的命令行工具中的签名工具hap-sign-tool.jar校验包名和工程项目中的包名是否一致，提前发现问题。通过该方法，还可以获得type、developer-id、validity，开发者也可使用同样方法，对这些字段进行校验。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/tuhLPOSRS1ibGrWfCJ6EFQ/zh-cn_image_0000002658808547.png?HW-CC-KV=V1&HW-CC-Date=20260723T013917Z&HW-CC-Expire=86400&HW-CC-Sign=7D673C508101388F86786957170B149246F95DC4FE13F1FEBC8828443D210DC5)
