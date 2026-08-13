# Clang-Tidy代码检查

更新时间：2026-08-05 02:47:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-clang-tidy

DevEco Studio支持通过内置的Clang-Tidy和自定义的Clang-Tidy对C/C++代码进行静态检查，以及支持配置检查规则，帮助开发者快速发现C++编码的问题。
 

#### 检查规则配置

当前支持通过三种方式配置检查规则。
 
 

#### 方式一：在Clang-Tidy Checks中配置
1. 在菜单栏进入**File > Settings...**（macOS系统为**DevEco Studio > Preferences/Settings...**）> **Languages & Frameworks** > **C/C++**，勾选**Use clang-tidy via clangd to enable the following checks**选项。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/1eNq7EKaTr2EwaEClgf0_g/zh-cn_image_0000002647917074.png?HW-CC-KV=V1&HW-CC-Date=20260813T095856Z&HW-CC-Expire=86400&HW-CC-Sign=62B1E0400395404DF1D8712944C8FFDC84A1EEE6445A5941BB485B4604CEBBB8)

2. 在选项下方添加检查规则，多条规则用英文逗号隔开，检查规则具体请参考[Clang-Tidy Checks网站](https://releases.llvm.org/19.1.0/tools/clang/tools/extra/docs/clang-tidy/checks/list.html)。

  添加检查规则时，可点击
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/rBuIl3sLSlyOZdCOi98J8A/zh-cn_image_0000002677996839.png?HW-CC-KV=V1&HW-CC-Date=20260813T095856Z&HW-CC-Expire=86400&HW-CC-Sign=E63690BA8F08256C48AB59CD85304B8E97B126514C4EF5ECD5F0DDDFA1127C43)
按钮展开规则填写框，在不同行添加规则。添加完成后点击
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/7sdBabqmRJq2OR7uet8o_g/zh-cn_image_0000002648076972.png?HW-CC-KV=V1&HW-CC-Date=20260813T095856Z&HW-CC-Expire=86400&HW-CC-Sign=7B095AF1CB4B53D4885062B22FF4B4F399D28969B7C7468E0287BEA73F0FA3C8)
按钮，多条规则会自动用英文逗号隔开。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/AeuFJRxOSpagaU6yLPGuPg/zh-cn_image_0000002648076978.png?HW-CC-KV=V1&HW-CC-Date=20260813T095856Z&HW-CC-Expire=86400&HW-CC-Sign=545FAB428FA51A2F6A3FE924A048089EC3D7622AC52709D74096BBF1DD83379C)

 
 

#### 方式二：在 .clang-tidy文件中配置
1. 在工程根目录中或在编辑器中搜索找到并打开 .clang-tidy文件。
2. 在**Checks**字段中添加检查规则，多条规则使用英文逗号隔开，检查规则具体请参考[Clang-Tidy Checks网站](https://releases.llvm.org/19.1.0/tools/clang/tools/extra/docs/clang-tidy/checks/list.html)。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/jUwNzhrXTd-oe8Hje0kMNQ/zh-cn_image_0000002648076980.png?HW-CC-KV=V1&HW-CC-Date=20260813T095856Z&HW-CC-Expire=86400&HW-CC-Sign=DCEF970D3379C85B21B40F62CDDD9E02C6962D55FEB577C32AD73EB603385D00)

 
 

#### 方式三：在Inspection-checks中配置
1. 通过如下两种方法进入Inspect Code。

  
在工程目录顶部或工程目录中任意文件，单击鼠标右键选择**Inspect Code**...。
2. 在菜单栏点击**Code >** **Inspect Code**...。
3. 点击**Configure...** **> CPP > clang-tidy**，在**checks**中添加检查规则，多条规则使用英文逗号隔开，检查规则具体请参考[Clang-Tidy Checks网站](https://releases.llvm.org/19.1.0/tools/clang/tools/extra/docs/clang-tidy/checks/list.html)。

  添加检查规则时，可点击
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/bKDT2mwoTbaVROgAnSkJTw/zh-cn_image_0000002648076970.png?HW-CC-KV=V1&HW-CC-Date=20260813T095856Z&HW-CC-Expire=86400&HW-CC-Sign=954A33B1F5AFFEB1140231884C3F2BFEA62BE2F3FFB72E35E52290BA59392BDB)
按钮展开规则填写框，在不同行添加规则。添加完成后点击
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/E40bnCH1TieoLByUQET0BA/zh-cn_image_0000002677996851.png?HW-CC-KV=V1&HW-CC-Date=20260813T095856Z&HW-CC-Expire=86400&HW-CC-Sign=B5C300511A7D40B976DA684D2CA801482387861D74603878A44C1AF6CF0F542B)
按钮，多条规则会自动用英文逗号隔开。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/JlOvOxEiQFa7GrhULT4JJQ/zh-cn_image_0000002647917078.png?HW-CC-KV=V1&HW-CC-Date=20260813T095856Z&HW-CC-Expire=86400&HW-CC-Sign=B0F910C688F0E493DCBED61BC0D98A0DF3DC85D0E633C72364BEF0C3328AA96A)

 
 

#### 通过内置Clang-Tidy检查代码

使用内置Clang-Tidy进行代码自动实时检查和手动检查。
 
 

#### 自动实时检查

**生效规则**
 
若勾选了**live update****（show in “Current File”）**，自动实时检查时，[Clang-Tidy Checks](#section386618116187)、[.clang-tidy文件](#section158716295189)和[Inspection-checks中](#section841663417181)配置的规则均生效；若不勾选**live update****（show in “Current File”）**，自动实时检查时，[Clang-Tidy Checks](#section386618116187)和 [.clang-tidy文件](#section158716295189)中配置的规则生效。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/76YRdwBSS8K8CtuvYLa95A/zh-cn_image_0000002678156691.png?HW-CC-KV=V1&HW-CC-Date=20260813T095856Z&HW-CC-Expire=86400&HW-CC-Sign=BE5670AB889332B12701A9D91EAA89F5E3652159F8C39665AC0F77E516460352)

 
**操作步骤**
 
代码编辑时，工具自动提示语法错误等，将鼠标放置在错误代码处会显示详细的错误信息。
 
 

#### 手动检查

**生效规则**
 
手动检查时，仅[Inspection-checks中配置的规则](#section841663417181)生效。
 
**操作步骤**
 1. 通过如下两种方法，进入手动检查入口。

  
在工程目录顶部或工程目录中任意文件，单击鼠标右键选择**Inspect Code**...。
2. 在菜单栏点击**Code >** **Inspect Code**...。
3. 指定检查范围，如整个工程、某个模块或者具体文件，单击**Analyze**按钮执行代码检查。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/QxFXlsoZR5GvjwelCVykWA/zh-cn_image_0000002678156689.png?HW-CC-KV=V1&HW-CC-Date=20260813T095856Z&HW-CC-Expire=86400&HW-CC-Sign=DC5098C74B5D6BACEBC16246A58B7AC7EDC0303B83E189F1FE3C8AAEF75085B7)

4. 检查完成后在界面左下方可查看告警文件和告警信息，点击告警信息可跳转至具体代码位置，开发者可在界面右下方代码区和上方代码区编辑修改。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/nLkI-snFTQOFvXoXbol-pQ/zh-cn_image_0000002647917076.png?HW-CC-KV=V1&HW-CC-Date=20260813T095856Z&HW-CC-Expire=86400&HW-CC-Sign=CACE3198C11C5051CB965AC28D52F51E6754F8D94057DB93F40776F74BCB5055)

 
 

#### 通过自定义Clang-Tidy检查代码

从26.0.0 Beta1版本开始，支持使用自定义Clang-Tidy进行代码自动实时检查和手动检查。
 
**生效规则**
 1. 勾选Prefer .clang-tidy files over IDE settings时，自动实时检查和手动检查时，[.clang-tidy文件中配置的规则](#section158716295189)生效。
2. 不勾选Prefer .clang-tidy files over IDE settings时，自动实时检查和手动检查时，[Inspection-checks中配置的规则](#section841663417181)生效。
 
**操作步骤**
 1. 在菜单栏进入**File > Settings...**（macOS系统为**DevEco Studio > Preferences/Settings...**）> **Languages & Frameworks** > **C/C++**，勾选**Use external Clang-Tidy instead of the built-in one**，添加clang-tidy.exe程序文件。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/lahOiPW3RRqg1t5ZALYomA/zh-cn_image_0000002647917072.png?HW-CC-KV=V1&HW-CC-Date=20260813T095856Z&HW-CC-Expire=86400&HW-CC-Sign=A152AC266AFFDC74B1A41C8C14106791D07456598D654FC408DE85CAF8C11356)


  
> [!NOTE]
> clang-tidy.exe可从DevEco Studio安装目录中获取。

2. 选择生效规则和开启实时检查。

  
进入clang-tidy界面，若勾选**Prefer .clang-tidy files over IDE settings**， [.clang-tidy文件中配置的规则](#section158716295189)生效；若不勾选**Prefer .clang-tidy files over IDE settings**，[Inspection-checks中配置的规则](#section841663417181)生效。
3. 若勾选**live update（show in “Current File”）**，会开启自动实时检查；若不勾选，需要手动检查，手动检查操作具体请参考[内置Clang-Tidy的手动检查](#section1395112325376)。
