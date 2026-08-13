# 混淆编译keep配置使用通配符*不生效

更新时间：2026-08-13 01:23:38

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-163

#### 问题现象

开启混淆编译后，使用如下混淆配置，生成release包发现混淆未生效。
 
```text
# 混淆选项
-enable-property-obfuscation
-enable-toplevel-obfuscation
-enable-filename-obfuscation
-remove-comments
# 保留选项
-keep-file-name
./src/main/ets/model/**
-keep
./src/main/ets/model/**
```
 
 

#### 背景知识

- [-keep-file-name](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/source-obfuscation-keep-options#section-keep-file-name)指定要保留的文件/文件夹的名称（不需要写文件后缀），支持使用名称类通配符。[-keep](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/source-obfuscation-keep-options#section-keep)保留指定相对路径filepath中的所有名称（例如变量名、类名、属性名等）不被混淆，./与../为相对于混淆配置文件所在目录，支持使用路径类通配符。
- [名称类通配符和路径类通配符](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/source-obfuscation-keep-options#保留选项支持的通配符)：

  
| 通配符 | 含义 | 名称类使用示例 | 路径类使用示例 |
| --- | --- | --- | --- |
| ? | 匹配任意单个字符，除了路径分隔符/ | "AB?"能匹配"ABC"等，但不能匹配"AB" | "../a?"能匹配"../ab"等，但不能匹配"../a/" |
| * | 匹配任意数量的任意字符，除了路径分隔符/ | "*AB*"能匹配"AB"、"aaABb"、"cAB"、"ABc"等 | "../a*/c"能匹配"../ab/c"，但不能匹配"../ab/d/s/c" |
| ** | 匹配任意数量的任意字符 | 不支持 | "../a**/c"能匹配"../ab/c"，也能匹配"../ab/d/s/c" |
| ! | 表示非，只能写在某个路径最前端，用来排除用户配置的白名单中已有的某种情况 | 不支持 | "!../a/b/c.ets"表示除"../a/b/c.ets"以外 |
 
 
 

#### 问题定位
1. [开启源码混淆](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/source-obfuscation-guide#开启源码混淆)后，分别不使用保留选项（-keep-file-name和-keep）和使用保留选项，使用release模式构建hap包后，[查看混淆效果](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/source-obfuscation-guide#查看混淆效果)得到以下结果：不使用保留选项：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/nbK7oczwQAuS1EQrXJWevg/zh-cn_image_0000002659138341.png?HW-CC-KV=V1&HW-CC-Date=20260813T095602Z&HW-CC-Expire=86400&HW-CC-Sign=00665846D7D9D34FC5070B17486443122551838006382FFA3899A629E78D84B5)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/5tvDzKq2QXStGqmCRUEZWA/zh-cn_image_0000002629058990.png?HW-CC-KV=V1&HW-CC-Date=20260813T095602Z&HW-CC-Expire=86400&HW-CC-Sign=01FD95E5CA74ED5C7D865181E50F85FE99297F7D360A57FEECAFF48DC02FFB6C)


  使用保留选项：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/90mAQEKhRUeIMetRdJr1Nw/zh-cn_image_0000002628899072.png?HW-CC-KV=V1&HW-CC-Date=20260813T095602Z&HW-CC-Expire=86400&HW-CC-Sign=FD1DC4F2BABCEC073A1C6CA56AA540C9A214B1D9EB0203DAA5B9C39A3EE8D359)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/ud9Uw_-CQUiGnwSBvmyS9A/zh-cn_image_0000002659258283.png?HW-CC-KV=V1&HW-CC-Date=20260813T095602Z&HW-CC-Expire=86400&HW-CC-Sign=D393FA2524433459180C6A6AB92223AEB75BBF413DDA5EF142F03AFB8AFE2A2E)


  对比两者，使用保留选项后，文件夹及文件名被混淆，而变量名、类名、属性名未被混淆，即-keep生效，而-keep-file-name未生效。
2. -keep-file-name指定要保留的文件/文件夹的名称，将-keep-file-name配置修改为名称配置而非路径配置，即将路径../src/main/ets/model/**修改为文件夹名称model和文件名称TestModel：
```text
-keep-file-name
model
TestModel
```

3. 考虑到当文件夹中文件较多时，依次列出所有文件易错且不易读，需要使用通配符。-keep-file-name支持名称类通配符，如使用*Model匹配TestModel等任意以Model结尾的文件：
```text
-keep-file-name
model
*Model
```

 
 

#### 分析结论

-keep-file-name指定要保留的文件/文件夹的名称，支持使用名称类通配符，不支持相对路径的写法，不支持使用路径类通配符。
 
 

#### 修改建议

根据问题现象中的混淆配置，保留选项的目的是保留src/main/ets/model文件夹中的所有名称，包括文件名、类名、变量名、属性名等不被混淆。
 
其中保留文件名不被混淆使用-keep-file-name，仅支持名称类写法，支持名称类通配符；保留类名、变量名、属性名等不被混淆使用-keep，仅支持相对路径写法，支持路径类通配符。修改为如下混淆配置：
 
```text
# 混淆选项
-enable-toplevel-obfuscation
-enable-property-obfuscation
-enable-filename-obfuscation
-remove-comments
# 保留选项
-keep-file-name
model
*Model
-keep
./src/main/ets/model/**
```
 
 

#### 总结

[保留选项](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/source-obfuscation-keep-options)写法总结：
  
| 保留选项 | 功能 | 写法 | 通配符 |
| --- | --- | --- | --- |
| -keep-property-name | 指定保留属性名称 | 属性名称 | 名称类通配符 |
| -keep-global-name | 指定保留顶层作用域或导入导出元素名称 | 导入导出元素名称 | 名称类通配符 |
| -keep-file-name | 指定保留文件/文件夹名称 | 文件/文件夹名称 | 名称类通配符 |
| -keep-comments | 指定保留注释 | 需要保留注释的class、function、namespace、enum、struct、interface、module、type及属性等的名称 | 名称类通配符 |
| -keep-dts | 指定保留声明文件中的所有名称 | 绝对路径 | 不支持 |
| -keep | 指定保留源码文件中的所有名称 | 相对路径 | 路径类通配符 |
