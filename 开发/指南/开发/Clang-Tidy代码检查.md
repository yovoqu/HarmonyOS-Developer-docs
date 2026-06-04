# Clang-Tidy代码检查

更新时间：2026-06-02 08:37:00

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-clang-tidy

DevEco Studio支持通过内置的Clang-Tidy对C/C++代码进行静态检查，以及支持配置检查规则，帮助开发者快速发现C++编码的问题。
 

#### 检查规则配置

当前支持通过三种方式配置检查规则。
 
 

#### 方式一：在Clang-Tidy Checks中配置
1. 在菜单栏进入**File > Settings...**（macOS系统为**DevEco Studio > Preferences/Settings...**）> **Languages & Frameworks** > **C/C++**，勾选**Use clang-tidy via calngd to enable the following checks**选项。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/Z5zYD78EQNqIFEYfkN6rzg/zh-cn_image_0000002572181928.png?HW-CC-KV=V1&HW-CC-Date=20260604T013003Z&HW-CC-Expire=86400&HW-CC-Sign=D7065D282AB48B638B0D9E0AA187D61B52A68623C85A6B25F6FCA153E463C140)

2. 在选项下方添加检查规则，多条规则用英文逗号隔开，检查规则具体请参考[Clang-Tidy Checks网站](https://releases.llvm.org/19.1.0/tools/clang/tools/extra/docs/clang-tidy/checks/list.html)。

  添加检查规则时，可点击
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/TFYj-1NDRG6-2J013DEiCg/zh-cn_image_0000002602661389.png?HW-CC-KV=V1&HW-CC-Date=20260604T013003Z&HW-CC-Expire=86400&HW-CC-Sign=33AFB58BFB995D36C44118FD3B9BA3CED763A47968E09E15149882CF76E3E938)
按钮展开规则填写框，在不同行添加规则。添加完成后点击
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/d9vlr1RPTm-5S5Jb1SgzAg/zh-cn_image_0000002572022288.png?HW-CC-KV=V1&HW-CC-Date=20260604T013003Z&HW-CC-Expire=86400&HW-CC-Sign=C6F6CA2456C793AACFB8A5DE9F84341E64EBD498D380F83CE9DDCFCB07813D11)
按钮，多条规则会自动用英文逗号隔开。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/0TLmcVw8SC2KJAmjoCpBDA/zh-cn_image_0000002602781447.png?HW-CC-KV=V1&HW-CC-Date=20260604T013003Z&HW-CC-Expire=86400&HW-CC-Sign=95D8524990CF9406991D9E892435633EB8A7E4AD335AB039E791CC7364DF190A)

 
 

#### 方式二：在 .clang-tidy文件中配置
1. 在工程根目录中或在编辑器中搜索找到并打开 .clang-tidy文件。
2. 在**Checks**字段中添加检查规则，多条规则使用英文逗号隔开，检查规则具体请参考[Clang-Tidy Checks网站](https://releases.llvm.org/19.1.0/tools/clang/tools/extra/docs/clang-tidy/checks/list.html)。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/LaKUcJD_QC-Gwnxi10ifIA/zh-cn_image_0000002572181930.png?HW-CC-KV=V1&HW-CC-Date=20260604T013003Z&HW-CC-Expire=86400&HW-CC-Sign=C81F3A416C84AB288E06807FECC8631747A642F82D2B0C1E77F2C27DCBACEA2B)

 
 

#### 方式三：在Inspection-checks中配置
1. 通过如下两种方法进入Inspect Code。

  
在工程目录顶部或工程目录中任意文件，单击鼠标右键选择**Inspect Code**...。
2. 在菜单栏点击**Code >** **Inspect Code**...。
3. 点击**Configure...** **> CPP > clang-tidy**，在**checks**中添加检查规则，多条规则使用英文逗号隔开，检查规则具体请参考[Clang-Tidy Checks网站](https://releases.llvm.org/19.1.0/tools/clang/tools/extra/docs/clang-tidy/checks/list.html)。

  添加检查规则时，可点击
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/c3cAEVj7RTeEXPFCXC9I5Q/zh-cn_image_0000002572022290.png?HW-CC-KV=V1&HW-CC-Date=20260604T013003Z&HW-CC-Expire=86400&HW-CC-Sign=B784B87F676EE87BBD722B01E90205F801B3127C6FB42405D4E2217367D2667A)
按钮展开规则填写框，在不同行添加规则。添加完成后点击
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/0EAeQppHSGa88aK05T8EwQ/zh-cn_image_0000002602781449.png?HW-CC-KV=V1&HW-CC-Date=20260604T013003Z&HW-CC-Expire=86400&HW-CC-Sign=01A60C6B50D0AC5215F8448618DD09B656552F40DA92897D2294CC6AB66D1284)
按钮，多条规则会自动用英文逗号隔开。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/4d1D3mITTcqhfAdbgFHaUQ/zh-cn_image_0000002572181932.png?HW-CC-KV=V1&HW-CC-Date=20260604T013003Z&HW-CC-Expire=86400&HW-CC-Sign=959163138E46A73D56F709B209C4D85E74FF638AF7B4EF2B1AAA1CA3EED07168)

 
 

#### 代码检查

使用内置Clang-Tidy进行代码自动实时检查和手动检查。
 
 

#### 自动实时检查

**生效规则**
 
若勾选了**live update****（show in “Current File”）**，自动实时检查时，[Clang-Tidy Checks](#section386618116187)、[.clang-tidy文件](#section158716295189)和[Inspection-checks中](#section841663417181)配置的规则均生效；若不勾选**live update****（show in “Current File”）**，自动实时检查时，[Clang-Tidy Checks](#section386618116187)和 [.clang-tidy文件](#section158716295189)中配置的规则生效。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/KKIA82fGSAGLJ8wgMPeDHg/zh-cn_image_0000002602661393.png?HW-CC-KV=V1&HW-CC-Date=20260604T013003Z&HW-CC-Expire=86400&HW-CC-Sign=E1F9CA2B39B73738185EEEDB4E9EF274F894775E4ABB49FED19EF8725D37BE6C)

 
**操作步骤**
 
代码编辑时，工具自动提示语法错误等，将标放置在错误代码处会显示详细的错误信息。
 
 

#### 手动检查

**生效规则**
 
手动检查时，仅[Inspection-checks中配置的规则](#section841663417181)生效。
 
**操作步骤**
 1. 通过如下两种方法，进入手动检查入口。

  
在工程目录顶部或工程目录中任意文件，单击鼠标右键选择**Inspect Code**...。
2. 在菜单栏点击**Code >** **Inspect Code**...。
3. 指定检查范围，如整个工程、某个模块或者具体文件，单击**Analyze**按钮执行代码检查。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/rafB0gH4TtmIpkyAHi1PSg/zh-cn_image_0000002602781451.png?HW-CC-KV=V1&HW-CC-Date=20260604T013003Z&HW-CC-Expire=86400&HW-CC-Sign=4AE17B9B669DDC2557609316FE479BFDFA376D1AD09C9FE41393D922E442C480)

4. 检查完成后在界面左下方可查看告警文件和告警信息，点击告警信息可跳转至具体代码位置，开发者可在界面右下方代码区和上方代码区编辑修改。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/HW0T_BywS6S1Q5YqguhhDQ/zh-cn_image_0000002611471503.png?HW-CC-KV=V1&HW-CC-Date=20260604T013003Z&HW-CC-Expire=86400&HW-CC-Sign=3A3D21B21CB376E37B429E7B5B6A4AA9C1EEFCA8FA304292C640BE1384EE191C)
