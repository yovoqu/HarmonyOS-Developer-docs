# 如何解决Hypium测试用例转换为测试服务包时py_file字段获取为空的问题

更新时间：2026-06-30 12:21:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-regression-test-18

#### 问题现象

[DevEco Testing Hypium](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hypium-python-guidelines#section16890204264419)框架里测试套件生成测试服务包失败，提示“***.json文件py_file字段获取为空”，测试套件配置文件中该如何配置该字段？
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/Ky5jILDyT4aGXIji_hiXHw/zh-cn_image_0000002661534691.png?HW-CC-KV=V1&HW-CC-Date=20260701T041024Z&HW-CC-Expire=86400&HW-CC-Sign=51533D618356BE10FCFC05517DFB2CAD9305A7B83360EEB4D5EA025A3F75FAA7)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/9hsng-uSRAyL9FQwBO7Lrw/zh-cn_image_0000002631175564.png?HW-CC-KV=V1&HW-CC-Date=20260701T041024Z&HW-CC-Expire=86400&HW-CC-Sign=E0072D6F6CFF317CCB3CE2C705E01F688F0E315A5E373E25D8C32CFF71627998)

 
 

#### 背景知识

- [回归测试](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/other-test#section12324184817324)的测试对象为应用的核心功能，用户可将应用核心功能的测试用例构建成多个可执行测试包，每个测试包中仅包含单个测试用例，便于观察到核心功能的每个小功能点的质量。
- 测试执行前需先构建测试包，用户利用python的setuptools工具在工程根目录下构建setup-regression.py以及MANIFEST.in文件，setup-regression.py文件中声明用例，MANIFEST.in文件中声明脚本执行过程中需要用到的aw包、config文件夹下的配置文件及其他的资源文件。

 
 

#### 问题定位

由于回归测试生成的可执行测试包中仅支持单用例（即单个json文件和json中指定的用例文件），根据报错信息需要检查setup-regression.py配置的单条用例xx.json文件py_file字段是否存在或者是否为空。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/Sms9G70_RaeICcGPq_XXCg/zh-cn_image_0000002661414977.png?HW-CC-KV=V1&HW-CC-Date=20260701T041024Z&HW-CC-Expire=86400&HW-CC-Sign=6D956A13E7FFC1047FE9560E01075E2916AF93DBF835B66A6260182805978AD6)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/lqSgoCjISsmAQ-HGFyQulQ/zh-cn_image_0000002661414983.png?HW-CC-KV=V1&HW-CC-Date=20260701T041024Z&HW-CC-Expire=86400&HW-CC-Sign=59648CF2067962462AD8653FC1A9A849641E78BEF873D28CF9E8A7DC5A388EE8)

 
 

#### 分析结论

当用户在setup-regression.py文件中指定打包的json文件中未声明对应的用例py文件，会出现该提示。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/3y3KKyxPSiWD253NNnl9nw/zh-cn_image_0000002631175908.png?HW-CC-KV=V1&HW-CC-Date=20260701T041024Z&HW-CC-Expire=86400&HW-CC-Sign=FA98FB149385DBBD51E2B81AAFCCEB8F75CC54589BC442A9946D2C9BA323B353)

 
 

#### 修改建议

回归测试生成的可执行测试包相关配置需要配置正确，若用例是测试套件路径配置示例如下：
- 用例xx.json文件需要包含py_file字段；
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/4UW5zCL9TeWKZ7j_gh_VAg/zh-cn_image_0000002661415301.png?HW-CC-KV=V1&HW-CC-Date=20260701T041024Z&HW-CC-Expire=86400&HW-CC-Sign=D21359EDAEC1C97B749D7FCC989EE55E7BB783151BF5C48B6D6C8A66FC014FCA)


 
 
- setup-regression.py文件示例；
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/xX5DdDL-SSaDICs_nOlLpg/zh-cn_image_0000002631336454.png?HW-CC-KV=V1&HW-CC-Date=20260701T041024Z&HW-CC-Expire=86400&HW-CC-Sign=65AEA9DC9A5A79DE61686483DF2AD6F667A41A3B77C4E352C4371DDA6B439463)

- MANIFEST.in文件示例。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/29I7KlXTRn65y0_f23NpdQ/zh-cn_image_0000002631336616.png?HW-CC-KV=V1&HW-CC-Date=20260701T041024Z&HW-CC-Expire=86400&HW-CC-Sign=0F5CC70461F3F81744AD32E8C8A1E8F65B2EFBBB2AB4E515CCA79F94FF77B813)


 
 

#### 常见FAQ

Q：生成可执行测试包时报错提示“测试套生成失败，请检查setup-regression.py文件后重试”如何解决？
 
A：请检测setup-regression.py文件写法，使用python setup-regression.py sdist--formats=zip进行本地自验证，验证通过后再利用插件出包。
 
Q：setup-regression.py文件无问题，但Hypium插件构建测试套件不成功，提示“测试套生成失败，请检查setup-regression.py文件后重试”如何解决？
 
A：请更新setuptools版本，可以先python -m pip install --upgrade pip更新pip，再使用命令pip install --upgrade setuptools升级setuptools。
 
Q：生成可执行测试包时报错提示“xxx.py文件不存在，请检查json文件是否填写正确！”如何解决？
 
A：当指定待打包的json文件中指定的py用例文件不存在，会出现该报错，请检查json文件中指定的py文件是否存在。
