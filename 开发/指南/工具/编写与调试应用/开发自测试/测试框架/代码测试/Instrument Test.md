# Instrument Test

更新时间：2026-04-20 06:32:02

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-instrument-test

#### 创建ArkTS测试用例

 

#### 创建默认测试用例
1. 在工程目录下打开待测试模块（支持HAP、HAR、HSP模块）下的ets文件，将光标置于代码中任意位置，单击**右键 > Show Context Actions**** > Create Instrument Test**或快捷键**Alt+Enter**** （macOS为Option+Enter）> Create Instrument Test**创建测试类。

  
![](assets/Instrument%20Test/file-20260514133035505-0.png)

2. 在弹出的Create Instrument Test窗口，输入或选择如下参数。

  
- **Testing library**：测试类型，默认为DECC-ArkTSUnit，JS语言默认为DECC-JSUnit。

3. **ArkTS name**：创建的测试文件名称，测试文件中包含了测试用例。测试文件名称要求在工程目录范围内具有唯一性，仅支持字母、数字、下划线（_）和点（.）。

4. **Destination package**：测试文件存放的位置，建议存放在待测试模块的test目录下。

5. DevEco Studio在ohosTest/ets/test目录下自动生成对应的测试类。在测试类中，DevEco Studio会生成对应方法的用例模板，具体测试代码需要开发者根据业务逻辑进行开发，具体请参考[自动化测试框架使用指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkxtest-guidelines)。

  
> [!NOTE]
> 您也可以手动在ohosTest > ets > test文件夹下创建测试用例，手动创建后，需要在List.test.ets文件中添加创建的用例类。手动创建的工程或历史工程，ohosTest > ets > test文件夹下所有文件的文件名必须以.test.ets结尾，否则将在运行时弹窗提示“Error: Test files must end with '.test.ets'.”请点击 Fix 按钮，DevEco Studio将自动对ohosTest > ets > test目录下的文件名进行修改。 首次在HarmonyOS设备上运行UI测试框架需要使用命令“hdc -n shell param set persist.ace.testmode.enabled 1”使能UiTest测试能力。


  

  #### 自定义Ability和Resources

  从5.0.3.403版本开始，新创建的工程/模块的ohosTest目录下默认不创建testability、testrunner和resources目录，历史工程仍保留这些目录，如果新工程需要使用ability或resources能力，需要开发者自行创建。

  
> [!NOTE]
> 如果需要使用ability能力，需要同时创建testrunner目录及OpenHarmonyTestRunner.ets文件。


| 新版本 | 历史版本 |

|  |  |

1. 创建以下目录或文件，文件内容示例可在[运行Instrument Test测试用例](#section1574003717165)后，在对应模块的.test/{productName}/intermediates/src/ohosTest（DevEco Studio 6.1.0 Beta1及以上版本）或build/{productName}/intermediates/src/ohosTest（DevEco Studio 6.1.0 Beta1以下版本）下查看，其中productName是当前生效的product，可以通过点击DevEco Studio右上方
![](assets/Instrument%20Test/file-20260514133035505-14.png)
图标进行查看。

  
testability目录 > TestAbility.ets文件

2. testability目录 > pages目录 > Index.ets文件

3. testrunner目录 > OpenHarmonyTestRunner.ets文件

4. resources目录 > base目录 > element目录 > color.json文件

5. resources目录 > base目录 > element目录 > string.json文件

6. resources目录 > base目录 > profile目录 > test_pages.json文件

7. 在module.json5文件中补充ability配置字段mainElement、pages、abilities，关于字段的具体说明请参考[module.json5配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)。

  
```ArkTS
{
  <span style="color: rgb(135,16,148);">"module"</span>: {
    <span style="color: rgb(135,16,148);">"name"</span>: <span style="color: rgb(6,125,23);">"entry_test"</span>,
    <span style="color: rgb(135,16,148);">"type"</span>: <span style="color: rgb(6,125,23);">"feature"</span>,
<span style="color: rgb(135,16,148);">    "description"</span>: <span style="color: rgb(6,125,23);">"$string:module_test_desc"</span>,
    <span style="color: rgb(135,16,148);">"mainElement"</span>: <span style="color: rgb(6,125,23);">"TestAbility"</span>,                                   // 对应下方abilities中的ability name。
    <span style="color: rgb(135,16,148);">"deviceTypes"</span>: [
      <span style="color: rgb(6,125,23);">"phone"</span>,
      <span style="color: rgb(6,125,23);">"tablet"</span>,
      <span style="color: rgb(6,125,23);">"2in1"</span>
    ],
    <span style="color: rgb(135,16,148);">"deliveryWithInstall"</span>: <span style="color: rgb(0,51,179);">true</span>,
    <span style="color: rgb(135,16,148);">"installationFree"</span>: <span style="color: rgb(0,51,179);">false</span>,
    <span style="color: rgb(135,16,148);">"pages"</span>: <span style="color: rgb(6,125,23);">"$profile:test_pages"</span>,                                 // 对应resources目录 > base目录 > profile目录 > test_pages.json文件。
    <span style="color: rgb(135,16,148);">"abilities"</span>: [                                                  // 添加的ability的配置信息。
      {
        <span style="color: rgb(135,16,148);">"name"</span>: <span style="color: rgb(6,125,23);">"TestAbility"</span>,
        <span style="color: rgb(135,16,148);">"srcEntry"</span>: <span style="color: rgb(6,125,23);">"./ets/testability/TestAbility.ets"</span>,
        <span style="color: rgb(135,16,148);">"description"</span>: <span style="color: rgb(6,125,23);">"$string:TestAbility_desc"</span>,
        <span style="color: rgb(135,16,148);">"icon"</span>: <span style="color: rgb(6,125,23);">"$media:icon"</span>,    // 确保引用的资源都存在
        <span style="color: rgb(135,16,148);">"label"</span>: <span style="color: rgb(6,125,23);">"$string:TestAbility_label"</span>,
        <span style="color: rgb(135,16,148);">"exported"</span>: <span style="color: rgb(0,51,179);">true</span>,
        <span style="color: rgb(135,16,148);">"startWindowIcon"</span>: <span style="color: rgb(6,125,23);">"$media:icon"</span>,
        <span style="color: rgb(135,16,148);">"startWindowBackground"</span>: <span style="color: rgb(6,125,23);">"$color:start_window_background"</span>
      }
    ]
  }
}
```


  

  #### 运行测试用例

  

  #### 运行模式

  使用DevEco Studio运行测试用例前，需要将设备与电脑进行连接，将工程编译成带签名信息的HAP，再安装到真机设备或模拟器上运行，具体请参考[使用本地真机运行应用](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-device)或[使用模拟器运行应用](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-emulator)。

  可以采用运行工程目录（test）、测试文件（如Ability.test.ets）、测试套件（describe）、测试方法（it）的方式来运行测试用例：
在工程目录中，单击**右键 > Run'测试文件名称'**，执行测试。
![](assets/Instrument%20Test/file-20260514133035505-15.png)

- 打开测试文件，单击测试套件左侧按钮。
![](assets/Instrument%20Test/file-20260514133035505-16.png)

- 如果要根据自定义的配置执行Instrument Test，在[创建测试用例运行任务](#section65264166107)后，通过如下方式的其中之一，执行Instrument Test：
在工具栏主菜单单击**Run > Run'测试名称'**。
- 在DevEco Studio的右上角，选择测试任务，然后单击右侧的
![](assets/Instrument%20Test/file-20260514133035505-17.png)
按钮，执行Instrument Test。
![](assets/Instrument%20Test/file-20260514133035505-18.png)


 
 
 
执行完测试任务后，查看测试结果。
 

![](assets/Instrument%20Test/file-20260514133035505-19.png)

 
 

#### 调试模式

调试模式相比运行模式增加了断点管理功能。在断点命中时，可以选择单步执行、步入步出、进入下个断点等方式进行调试，另外可以使用线程堆栈可视化、变量和表达式可视化功能，快速定位问题。
 
以文件级别为例，在添加断点之后，在工程目录中，选中文件，单击**右键 > Debug'测试文件名称'**，以调试模式执行测试任务。
 

![](assets/Instrument%20Test/file-20260514133035505-2.png)

 
在断点命中时，下方将出现Debug窗口。开发者可在该窗口中进行断点管理与基础调试能力的可视化操作，在断点命中时可查看当前线程的变量和堆栈信息。
 

![](assets/Instrument%20Test/file-20260514133035505-20.png)

 
断点命中时，在代码编辑器窗口单击右键，在弹出的菜单中将出现调试模式特有功能，如计算表达式、添加变量监视等。
 

![](assets/Instrument%20Test/file-20260514133035505-21.png)

 
在跳出所有断点后，测试结束，与运行模式相同，在测试窗口查看测试结果。
 

![](assets/Instrument%20Test/file-20260514133035505-22.png)

 
> [!NOTE]
> DevEco Studio支持设置调试代码类型，具体请参考 设置调试代码类型 。

 
 

#### 覆盖率统计模式

在Instrument Test运行的基础上支持代码覆盖率统计。
 
开发者可以自定义需要参与覆盖率测试的文件，具体配置方法请参考[配置覆盖率过滤文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ui-test#section13756446154)。
 
可以采用运行工程目录（test）、测试文件（如Ability.test.ets）、测试套件（describe）、测试方法（it）的方式来启动代码覆盖率的统计。
 
以文件级别为例，有两种方式启动测试：
 
 
- 方式一：在工程目录中，选中文件，单击**右键 > Run '测试文件名称' with Coverage**，执行测试。
![](assets/Instrument%20Test/file-20260514133035505-24.png)

- 方式二：在DevEco Studio的右上角，选择测试任务，然后单击右侧的
![](assets/Instrument%20Test/file-20260514133035505-25.png)
按钮，执行测试。
![](assets/Instrument%20Test/file-20260514133035505-26.png)


 
启动测试后，进行编译构建，底部将出现Cover窗口，构建结束后自动拉起Cover窗口，测试任务结束后，窗口中会打印测试报告的路径。
 

![](assets/Instrument%20Test/file-20260514133035505-27.png)

 
点击链接可打开报告，查看ArkTS代码覆盖率详情，关于覆盖率的计算方式请参考[查看覆盖率报告](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ui-test#section10394362109)。
 

![](assets/Instrument%20Test/file-20260514133035505-28.png)

 
在Cover窗口中，单击rerun按钮可以按照之前的设置，重新执行覆盖率用例。
 

![](assets/Instrument%20Test/file-20260514133035505-29.png)

 

#### （可选）自定义测试用例运行任务

默认情况下，测试用例可直接运行，如果需要自定义测试用例运行任务，可通过如下方法进行设置。
 1. 在工具栏主菜单单击**Run** >** Edit Configurations**进入Run/Debug Configurations界面。
2. 在**Run/Debug Configurations**界面，单击+按钮，在弹出的下拉菜单中，单击Instrument Test。

  
![](assets/Instrument%20Test/file-20260514133035505-3.png)

3. 根据实际情况，配置Instrument Test的运行参数。然后单击**OK**，完成配置。

  
- 如果模块依赖共享包，请提前设置HAP安装方式，勾选“**Keep Application Data**”，则表示采用覆盖安装方式，保留应用/元服务缓存数据。

4. 如果工程中HAP/HSP模块直接依赖其他HSP模块（如entry模块依赖HSP模块）或间接依赖其他模块（如entry模块依赖HAR模块，HAR又依赖HSP模块）时，在测试阶段需要同时安装模块包及其所有依赖模块的包到设备中。此时，可以勾选“**Auto Dependencies**”，测试时会自动将所有依赖的模块都安装到设备上。该选项默认勾选。

5. 如果不涉及UI测试，勾选“**Only OhosTest Package**”，则只会推送OhosTest测试包到设备上，不会推送HAP/HSP包，可以缩短推包时间。

  

  #### 使用过滤条件筛选待运行的测试用例

1. 在用例编写时，通过配置it的第二个入参，为每个用例添加过滤参数。此参数用于为测试用例添加标注，不添加则参数默认为0表示未被标注。

  
![](assets/Instrument%20Test/file-20260514133035505-31.png)


2. 打开**Run/Debug Configurations**窗口，点击Test Args
![](assets/Instrument%20Test/file-20260514133035505-32.png)
，打开**Test Args**界面，添加命令行参数。

  
![](assets/Instrument%20Test/file-20260514133035505-33.png)


  例如将测试参数配置为level=1, size=medium

  
![](assets/Instrument%20Test/file-20260514133035505-4.png)


| Key | 含义说明 | Value取值范围 |

| --- | --- | --- |

| level | 用例级别 | "0","1","2","3","4", 例如：-s level 1 |

| size | 用例粒度 | "small","medium","large", 例如：-s size small |

| testType | 用例测试类型 | "function","performance","power","reliability","security","global","compatibility","user","standard","safety","resilience", 例如：-s testType function |

3. 完成以上配置后，在运行此项配置对应的测试任务时，只运行过滤后的测试用例。

  
![](assets/Instrument%20Test/file-20260514133035505-5.png)


  

  #### 设置调试代码类型

  点击**Run > Edit Configurations**，打开**Run/Debug Configurations**窗口，选择Instrument Test，点击**Debugger**页签，设置Debug type。

  
![](assets/Instrument%20Test/file-20260514133035505-6.png)


  调试类型Debug type默认为Detect Automatically，关于各调试类型的说明如下表所示：

| 调试类型 | 调试代码 |

| --- | --- |

| Detect Automatically | 自动检测。根据工程模块及其依赖的模块涉及的编程语言，自动启动对应的调试器。 如果检测到是Native模块，出现两个调试窗口（PandaDebugger、Native）；如果不是Native模块，只出现PandaDebugger调试窗口。 |

| ArkTS/JS | 只调试ArkTS/JS，只出现PandaDebugger调试窗口。 |

| Native | 单独调试C++，只出现Native调试窗口。 |

| Dual(ArkTS/JS + Native) | 支持ArkTS/JS和C++混合调试，出现两个调试窗口（PandaDebugger、Native）。 |

  
> [!NOTE]
> 调试C++代码时，当前模块及所有依赖的HSP模块的 Address Sanitizer配置 要保持一致，若不一致，可能无法进入C++代码的断点处。


  

  #### ASan检测

  Instrument Test针对C/C++方法提供ASan检测能力，关于ASan的介绍请参考[ASan检测](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-asan)，当前不支持JS语言。

1. 在运行/调试配置窗口，选择对应的Instrument Test，点击**Diagnostics**页签，勾选**Address Sanitizer**选项，勾选后，测试包和源码包均开启ASan能力。

  
![](assets/Instrument%20Test/file-20260514133035505-8.png)


2. 如果有引用本地library，需在library模块的build-profile.json5文件中，配置arguments字段值为“-DOHOS_ENABLE_ASAN=ON”，表示以ASan模式编译so文件。

  
![](assets/Instrument%20Test/file-20260514133035505-9.png)


3. 运行测试用例。

4. 当程序出现内存错误时，弹出ASan log信息，点击信息中的链接即可跳转至引起内存错误的代码处。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/X9YdoEzeTIqUlQFdo7dn_Q/zh-cn_image_0000002602066547.png?HW-CC-KV=V1&HW-CC-Date=20260528T030556Z&HW-CC-Expire=86400&HW-CC-Sign=DDE0AD23AB7389AC1BDDA8C8CD8CEAF01706A762B34B2F2064BC3D3DBA7D469B)


  

  #### 测试C++代码

  从DevEco Studio 6.0.0 Beta5版本开始，支持对C++代码进行测试，包括运行/调试C++测试代码、对C++代码进行覆盖率统计。

  由于C++的测试so无法直接在设备上运行，需要通过Node-API的方式拉起，即通过ArkTS/JS语言拉起C/C++测试用例。

  

  #### 运行C++测试代码

1. 创建cpp测试目录，鼠标右键单击ohosTest目录，选择**New > C/C++ File(Napi)**，在ohosTest下生成cpp测试目录，以entry模块为例，目录结构如下。
**src > ohosTest > cpp > types**：用于存放C++的API接口描述文件。

2. **src > ohosTest > cpp > types** **> libentry_test > index.d.ts**：描述C++ API接口行为，如接口名、入参、返回参数等。

3. **src > ohosTest > cpp > types** **> libentry_test > oh-package.json5**：配置.so三方包声明文件的入口及包名。

4. **src > ohosTest > cpp > CMakeLists.txt**：CMake配置文件，提供CMake构建脚本。

5. **src > ohosTest > cpp > napi_init.cpp：**定义C++ API接口的文件**。**

6. 通过ArkTS测试用例拉起C++测试，示例如下。
```ArkTS
// ArkTS测试文件Ability.test.ets
import entryTest from 'libentry_test.so';
export default function abilityTest() {
  describe('ActsAbilityTest', () => {
    ...
    it('testNative', 0, () => {
      hilog.info(0x0000, 'testTag', '%{public}s', 'testNative it begin');
      let result = entryTest.runNativeTest();
      hilog.info(0x0000, 'testTag', '%{public}s', result)
      expect(result).assertContain("ended");
    })
  })
}
```


7. 运行testNative测试用例，查看测试结果。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/kd0jJJHtRcOGM5RL7y8gkQ/zh-cn_image_0000002571387432.png?HW-CC-KV=V1&HW-CC-Date=20260528T030556Z&HW-CC-Expire=86400&HW-CC-Sign=43D53423CD899E9EFA3BDEDC52AB8BDA8521C5AC68CFDE4236DDA85C0DAB8D11)


  

  #### 收集代码覆盖率

  DevEco Studio默认不收集C++代码覆盖率，需要通过以下方式开启。

1. 在测试目录下的CMakeLists.txt中添加以下代码，开启覆盖率编译插桩能力。
```text
// DevEco Studio 6.0.2 Beta1之前版本
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fprofile-instr-generate -fcoverage-mapping")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fprofile-instr-generate -fcoverage-mapping")

// DevEco Studio 6.0.2 Beta1及以上版本，OHOS_TEST_COVERAGE在覆盖率模式下为true，在调试/运行模式下为false
if(OHOS_TEST_COVERAGE)
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fprofile-instr-generate -fcoverage-mapping")
  set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fprofile-instr-generate -fcoverage-mapping")
endif()
```


2. 在napi_init.cpp文件的RunNativeTest方法中，调用__llvm_profile_write_file方法，将覆盖率数据保存到设备的/data/storage/el2/base路径下的c++_coverage.profraw文件中，该路径和文件名不可修改，示例代码如下。

  
```text
<span style="color: rgb(0,0,255);">extern</span> <span style="color: rgb(255,0,0);">"C"</span> {
    <span style="color: rgb(0,0,255);">void</span> __llvm_profile_set_filename(<span style="color: rgb(0,0,255);">char</span> *);
    <span style="color: rgb(0,0,255);">int</span> __llvm_profile_write_file(<span style="color: rgb(0,0,255);">void</span>);
}

<span style="color: rgb(0,0,255);">static</span> napi_value RunNativeTest(napi_env env, napi_callback_info info)
{
    <span style="color: rgb(0,0,255);">char</span> filename[<span style="color: rgb(80,160,79);">256</span>];
    snprintf(filename, <span style="color: rgb(0,0,255);">sizeof</span>(filename), <span style="color: rgb(255,0,0);">"/data/storage/el2/base/c++_coverage.profraw"</span>); // 覆盖率报告文件路径和文件名，不可修改
    __llvm_profile_set_filename(filename);
    <span style="color: rgb(80,160,79);">// 开启测试</span>
    ...
    // 结束测试，保存数据
     __llvm_profile_write_file();
    ...
}
```


3. 运行覆盖率测试，选中ArkTS测试文件，单击**右键 >**** Run '测试文件名称' with Coverage**，执行测试。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/nvk_hzs0TeS7BOn5z9X-ow/zh-cn_image_0000002571547038.png?HW-CC-KV=V1&HW-CC-Date=20260528T030556Z&HW-CC-Expire=86400&HW-CC-Sign=3BDD4F614F3CDEC6FCDAABDEBA6EDF0DE771C8A4D067B9EEFBE11A188F327FF7)


  启动测试后，进行编译构建，底部将出现Cover窗口，构建结束后自动拉起Cover窗口，测试任务结束后，窗口中会打印测试报告的路径。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/4QcyvJjOQZS1kWh2FyPXGw/zh-cn_image_0000002571547036.png?HW-CC-KV=V1&HW-CC-Date=20260528T030556Z&HW-CC-Expire=86400&HW-CC-Sign=347CD3DB9AE0FEE5EF7E727F3758BE814C016BF2386288CDC2A31726692E8CC9)


  点击链接可打开报告，查看C++代码覆盖率详情。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/1VHeYVkeTy-ea0NZEmnQDg/zh-cn_image_0000002571547050.png?HW-CC-KV=V1&HW-CC-Date=20260528T030556Z&HW-CC-Expire=86400&HW-CC-Sign=0ED50AECA98E5DE2F07C93D440E3758FF53156DD0B776EAC40D10E180D6753E7)


  

  #### 使用命令行执行测试Instrument Test

  通过命令行方式执行Instrument Test，在工程根目录下执行命令：
```bash
hvigorw onDeviceTest -p module={moduleName} -p coverage={true|false} -p scope={suiteName}#{methodName} -p ohos-debug-asan={true|false}
```
 
module：执行测试的模块，缺省默认是执行所有模块的用例。
- coverage：是否生成覆盖率报告，缺省默认是true，在<module-path>/.test/default/outputs/ohosTest/reports路径下生成两份报告，一份是html格式（index.html），一份是json格式（coverageReport.json），具体参考[查看覆盖率报告](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ui-test#section10394362109)。如果开启了C++代码覆盖率测试，会生成C++代码的覆盖率报告，路径：<module-path>/.test/default/outputs/ohosTest/cpp_reports/index.html
- scope：格式为{suiteName}#{methodName}或{suiteName}，分别表示测试用例级别或测试套件级别的测试，缺省默认是执行当前模块的所有用例。
- ohos-debug-asan：是否启用ASan检测，缺省默认是false。从DevEco Studio 5.1.1 Beta1版本开始支持。ASan日志路径：<module-path>/.test/default/intermediates/ohosTest/coverage_data

 
 
> [!NOTE]
> 通过命令行执行测试时，不支持配置product，默认为default。 多个module和scope之间用逗号隔开。

 
测试结果文件：<module-path>/.test/default/intermediates/ohosTest/coverage_data/test_result.txt
