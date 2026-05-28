# 代码检查工具（codelinter）

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-command-line-codelinter

codelinter同时支持使用命令行执行代码检查与修复，可将codelinter工具集成到门禁或持续集成环境中。
 
codelinter命令行格式为：
 
```text
codelinter [options] [dir]
```
 
options：可选配置，请参考[表1](#table25697717185)。
 
dir：待检查的工程根目录；为可选参数，如不指定，默认为当前上下文目录。
  
| 指令 | 说明 |
| --- | --- |
| --config/-c &lt;filepath&gt; | 指定执行codelinter检查的规则配置文件，&lt;filepath&gt;指定执行检查的规则配置文件位置。 |
| --fix | 设置codelinter检查同时执行QuickFix。 |
| --format/-f | 设置检查结果的输出格式。目前支持default/json/xml/html四种格式；不指定时，默认是default格式（文本格式）。 |
| --output/-o &lt;filepath&gt; | 指定检查结果保存位置，且命令行窗口不展示检查结果。&lt;filepath&gt;指定存放代码检查结果的文件路径，支持使用相对/绝对路径。不使用--output指令时，检查结果默认会显示在命令行窗口中。 |
| --version/-v | 查看codelinter版本。 |
| --product/-p &lt;productName&gt; | 指定当前生效的product。 &lt;productName&gt; 为生效的product名称。 |
| --incremental/-i | 对Git工程中的增量文件（包含新增/修改/重命名的文件）执行Code Linter检查。 |
| --help/-h | 查询codelinter命令行帮助。 |
| --exit-on/-e &lt;levels&gt; | 指定哪些告警级别需要返回非零退出码，告警级别包括：error、warn和suggestion。若需要指定多个告警级别，级别间需要用英文逗号分开。 退出码的计算方式为：用一个3位的二进制数从高到低分别表示error、warn、suggestion告警级别。若在命令行中配置告警级别，并且代码检查结果中也包含该告警级别，则该二进制值为1，否则均为0。将二进制数转换为十进制数，则是退出码。 例如： 命令配置为--exit-on error，代码检查结果包括error、warn、suggestion三类告警，则退出码的二进制数为100，十进制数为4。命令配置为--exit-on error，代码检查结果包括warn、suggestion两类告警，则退出码的二进制数为000，十进制数为0。 |
 
1. 进行codelinter代码检查与修复。若您的工程存在多个product，请使用--product/-p指令，指定生效的product和执行检查的工程根目录。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/7gwG2SLmRxyQSbaLsdLxEw/zh-cn_image_0000002571547260.png?HW-CC-KV=V1&HW-CC-Date=20260528T014959Z&HW-CC-Expire=86400&HW-CC-Sign=6E696686CCC7555D4CF427F7AD4DD421CC61DA112FD6F8FC648DC79163A19B30)

- 在工程根目录下使用命令行工具：
直接执行** codelinter **指令。此时根据默认codelinter检查规则，对该工程中的TS/ArkTS文件进行代码检查。默认的规则清单可在检查完成后，根据命令行提示，查看相应位置的code-linter.json5文件。
```text
codelinter // 进行codelinter检查
```
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/Z-LWjAqyS-S0HJcWBcUAOg/zh-cn_image_0000002571387626.png?HW-CC-KV=V1&HW-CC-Date=20260528T014959Z&HW-CC-Expire=86400&HW-CC-Sign=589A6396642E03C8ECBFA9BF8C5134898D72E0FE0FC5E6CAC2BF3B8111BDB4EB)


2. 执行如下命令，指定codelinter检查所使用的code-linter.json5规则配置文件，并进行代码检查。
```text
codelinter -c <em>filepath</em> // 指定执行检查的规则配置文件位置
```
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/oczaSju8ToiqzY5yDM6ROQ/zh-cn_image_0000002602186795.png?HW-CC-KV=V1&HW-CC-Date=20260528T014959Z&HW-CC-Expire=86400&HW-CC-Sign=A2807DAB53EACA39670669EC7C61C2EA3D32BC23F30C3D538A455F5CFFDA47FC)


3. 执行如下命令，对指定工程将根据指定的规则配置文件执行codelinter检查，并对部分支持修复的告警信息进行自动修复。
```text
<em>codelinter -c filepath</em> --fix // 对工程中的告警进行修复
```
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/kqFcY1CwTeiZ3ko5Tq_HVQ/zh-cn_image_0000002602186793.png?HW-CC-KV=V1&HW-CC-Date=20260528T014959Z&HW-CC-Expire=86400&HW-CC-Sign=A8A84E6FC15EBF16137867C9F831C9226D18A7C48E4F4E44A15B00FB15B6062C)

- 在非工程根目录下使用命令行工具：1. 执行如下命令，指定需要进行检查的工程目录或文件路径。此时根据默认codelinter检查规则，对该工程中的TS/ArkTS文件进行代码检查。默认的规则清单可在检查完成后，根据命令行提示，查看相应位置的code-linter.json5文件。
```text
codelinter dir [filepath] [dir1] // 指定执行检查的工程目录或文件路径。支持同时配置多个文件/文件夹路径。 filepath为待检查的文件所在位置，dir、dir1指定待检查的工程目录
```
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/_rPz_sEVT8WjbPzxJaiamw/zh-cn_image_0000002602066743.png?HW-CC-KV=V1&HW-CC-Date=20260528T014959Z&HW-CC-Expire=86400&HW-CC-Sign=A8AA83DF87A55FE1325CF0E2B36B6A92121159A16C6F4A76A880BCA69BE90DD3)


2. 在指定的工程目录下，根据指定的codelinter规则配置文件进行代码检查。
```text
codelinter -c <em>filepath</em> dir // filepath为指定的规则配置文件所在位置，dir指定执行检查的工程根目录
```


3. 执行如下命令，对指定工程重新执行codelinter检查，并对部分支持修复的告警进行自动修复。
```text
<em>codelinter -c filepath dir</em> --fix // 对指定工程中的告警进行修复。支持配置同时多个工程路径
```
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/wQ_EP99gRVWbJmR1MUrwTA/zh-cn_image_0000002571547262.png?HW-CC-KV=V1&HW-CC-Date=20260528T014959Z&HW-CC-Expire=86400&HW-CC-Sign=868D0E2FDBEFADD7853D1F4A05451CFEC936BCF2887A9D63894CDA29CF980118)


 
 

- 如需指定检查结果输出格式（以json格式为例），执行如下指令。检查结果将在命令行窗口展示。

  
```json
codelinter [dir] -f json  //[dir]为待检查的工程根目录
```
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/J1cki1yxSQ2N8vRmPEwOfg/zh-cn_image_0000002571387628.png?HW-CC-KV=V1&HW-CC-Date=20260528T014959Z&HW-CC-Expire=86400&HW-CC-Sign=73156E6856C619DCFA70208CA51131068F88D6E68018F48C9A40DD88178F6329)

- 执行如下指令，指定代码检查输出格式及结果保存位置。此时将不在命令行窗口中打印检查结果，可在指定的文件存放路径下查看。

  
```json
codelinter [dir] -f json -o <em>filepath</em>2     // [dir]为待检查的工程根目录，<em>filepath</em>2为指定存放代码检查结果的文件路径
```
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/RP60Va3aQV-ooKIhP70qtw/zh-cn_image_0000002602066745.png?HW-CC-KV=V1&HW-CC-Date=20260528T014959Z&HW-CC-Expire=86400&HW-CC-Sign=56B431ACD6449AFF5AD2E05DBFEDC4C4B0BD2FF8D878966041CC49B8E51D4037)
