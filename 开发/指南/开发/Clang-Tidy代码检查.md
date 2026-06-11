# Clang-Tidy代码检查

更新时间：2026-06-09 08:54:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-clang-tidy

DevEco Studio支持通过内置的Clang-Tidy对C/C++代码进行静态检查，以及支持配置检查规则，帮助开发者快速发现C++编码的问题。
 

#### 检查规则配置

当前支持通过三种方式配置检查规则。
 
 

#### 方式一：在Clang-Tidy Checks中配置
1. 在菜单栏进入**File > Settings...**（macOS系统为**DevEco Studio > Preferences/Settings...**）> **Languages & Frameworks** > **C/C++**，勾选**Use clang-tidy via clangd to enable the following checks**选项。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/71fWbGGWQ3Sa-JcgALqyRA/zh-cn_image_0000002572181928.png?HW-CC-KV=V1&HW-CC-Date=20260611T074937Z&HW-CC-Expire=86400&HW-CC-Sign=11FB4C96655EED99C28BB8753EEB66DD9A023C3B00D58CACED0B7B6B986C8F6E)

2. 在选项下方添加检查规则，多条规则用英文逗号隔开，检查规则具体请参考[Clang-Tidy Checks网站](https://releases.llvm.org/19.1.0/tools/clang/tools/extra/docs/clang-tidy/checks/list.html)。

  添加检查规则时，可点击
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/F-poghnQQmuebR9j_l9A0w/zh-cn_image_0000002602661389.png?HW-CC-KV=V1&HW-CC-Date=20260611T074937Z&HW-CC-Expire=86400&HW-CC-Sign=F7D1E70AA1A6FD850CABFB06C9AB380836312503199952BDAE30FE927B33EF30)
按钮展开规则填写框，在不同行添加规则。添加完成后点击
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/4eq00gNUQy-oHi3xoTbVBQ/zh-cn_image_0000002572022288.png?HW-CC-KV=V1&HW-CC-Date=20260611T074937Z&HW-CC-Expire=86400&HW-CC-Sign=0809AF819F430F4122A51BF014747B13E8209248848C1CFB061CE7982C20826C)
按钮，多条规则会自动用英文逗号隔开。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/gAcsDL9cSRCUxla9EV8h9Q/zh-cn_image_0000002602781447.png?HW-CC-KV=V1&HW-CC-Date=20260611T074937Z&HW-CC-Expire=86400&HW-CC-Sign=3FDD27BF12D1D3DF1CF473ABC132646D91BEBD16840E5E1A70AC01DA6E85B39A)

 
 

#### 方式二：在 .clang-tidy文件中配置
1. 在工程根目录中或在编辑器中搜索找到并打开 .clang-tidy文件。
2. 在**Checks**字段中添加检查规则，多条规则使用英文逗号隔开，检查规则具体请参考[Clang-Tidy Checks网站](https://releases.llvm.org/19.1.0/tools/clang/tools/extra/docs/clang-tidy/checks/list.html)。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/RYDtv1-LRN26RJH6chG2iA/zh-cn_image_0000002572181930.png?HW-CC-KV=V1&HW-CC-Date=20260611T074937Z&HW-CC-Expire=86400&HW-CC-Sign=A207F83C2064BBFC09602BCE4264D1D3B92F7C57F1E1393C562EAF963864DAF6)

 
 

#### 方式三：在Inspection-checks中配置
1. 通过如下两种方法进入Inspect Code。

  
在工程目录顶部或工程目录中任意文件，单击鼠标右键选择**Inspect Code**...。
2. 在菜单栏点击**Code >** **Inspect Code**...。
3. 点击**Configure...** **> CPP > clang-tidy**，在**checks**中添加检查规则，多条规则使用英文逗号隔开，检查规则具体请参考[Clang-Tidy Checks网站](https://releases.llvm.org/19.1.0/tools/clang/tools/extra/docs/clang-tidy/checks/list.html)。

  添加检查规则时，可点击
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/L4G4tMWLT5inA6SC02vv3g/zh-cn_image_0000002572022290.png?HW-CC-KV=V1&HW-CC-Date=20260611T074937Z&HW-CC-Expire=86400&HW-CC-Sign=F9A8F74E20CA067444C4BAA6C88FCBD9935CD8E99DEF6C313FEC6CD4C4B7E9EF)
按钮展开规则填写框，在不同行添加规则。添加完成后点击
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/CXmYt56mTLSBNRCpGSXplQ/zh-cn_image_0000002602781449.png?HW-CC-KV=V1&HW-CC-Date=20260611T074937Z&HW-CC-Expire=86400&HW-CC-Sign=5C77D810F39B83664367AAFEF3B4B717B81D4382F59BF6465102D6619781054C)
按钮，多条规则会自动用英文逗号隔开。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/xBcxN_sGREWGUQN4ve5DTw/zh-cn_image_0000002572181932.png?HW-CC-KV=V1&HW-CC-Date=20260611T074937Z&HW-CC-Expire=86400&HW-CC-Sign=BA00FC3549E803032D44E17314CB18753166F9B7614AC4C27962BD58A1A303ED)

 
 

#### 代码检查

使用内置Clang-Tidy进行代码自动实时检查和手动检查。
 
 

#### 自动实时检查

**生效规则**
 
若勾选了**live update****（show in “Current File”）**，自动实时检查时，[Clang-Tidy Checks](#section386618116187)、[.clang-tidy文件](#section158716295189)和[Inspection-checks中](#section841663417181)配置的规则均生效；若不勾选**live update****（show in “Current File”）**，自动实时检查时，[Clang-Tidy Checks](#section386618116187)和 [.clang-tidy文件](#section158716295189)中配置的规则生效。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/bpdYs3LvRXWyFWrv6cnmZQ/zh-cn_image_0000002602661393.png?HW-CC-KV=V1&HW-CC-Date=20260611T074937Z&HW-CC-Expire=86400&HW-CC-Sign=B7F20F6557D6F81CC5C59D3D300EFDA991F03E651D79A26EB954256BBFC685E8)

 
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

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/lafhaVulQ6OlYwyXS4EHww/zh-cn_image_0000002602781451.png?HW-CC-KV=V1&HW-CC-Date=20260611T074937Z&HW-CC-Expire=86400&HW-CC-Sign=81D88F3460AD99D74A5718A334518D3E993DB6F95661F495C2E5B89AAD6A1357)

4. 检查完成后在界面左下方可查看告警文件和告警信息，点击告警信息可跳转至具体代码位置，开发者可在界面右下方代码区和上方代码区编辑修改。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/AP-DH_IPTJiy7hd6_HjZew/zh-cn_image_0000002611471503.png?HW-CC-KV=V1&HW-CC-Date=20260611T074937Z&HW-CC-Expire=86400&HW-CC-Sign=04AEE53D464402E155CA20D9096CA815E62FB69D9728B0091966035E1F8BB56E)
