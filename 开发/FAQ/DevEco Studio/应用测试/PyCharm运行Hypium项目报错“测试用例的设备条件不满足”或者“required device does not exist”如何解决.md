# PyCharm运行Hypium项目报错“测试用例的设备条件不满足”或者“required device does not exist”如何解决

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-24

## PyCharm运行Hypium项目报错“测试用例的设备条件不满足”或者“required device does not exist”如何解决
 


##### 问题现象

cmd命令行可以连接到设备，UiViewer也可以连接设备。但是执行用例出现如下报错信息：
 
- 提示“Test source required 1 devices, actually 0 devices were found [Suggestions]测试用例的设备条件不满足”。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/8WfeLszcQVi1aDkYmEg6iA/zh-cn_image_0000002628409554.png?HW-CC-KV=V1&HW-CC-Date=20260701T025922Z&HW-CC-Expire=86400&HW-CC-Sign=1965A24D0E93545BF6B7FACE44BAD94AFA5B211FF5A15D26B6C5F7EF99649AEF)

- 提示“required device does not exist”。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/JHnS85HIShSmXywYMqnqzg/zh-cn_image_0000002628569452.png?HW-CC-KV=V1&HW-CC-Date=20260701T025922Z&HW-CC-Expire=86400&HW-CC-Sign=8C62A10DE99CB23112E84186613514A1374B97BF28ECB474057E680F84BA3463)


 
 

##### 背景知识

[DevEco Testing Hypium](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hypium-python-guidelines#section16890204264419)以下简称（Hypium）是HarmonyOS平台的UI自动化测试框架，支持开发者使用python语言为应用编写UI自动化测试脚本。
 
 

##### 问题定位

- 检查本地设备实际是否存在、系统环境变量[OHOS_HDC_SERVER_PORT](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hdc#ohos_hdc_server_port)的hdc端口配置。
- 检查当前user_config.xml中是否设置了设备的sn，设备的sn是否实际存在。
- 检查用例的json文件请求的设备类型type字段是否正确。
- 检查json中请求的设备label类型是否正确。

 
 

##### 分析结论

如果“hdc list targets”命令查询到设备，但Hypium框架运行报错设备未连接，排查以下原因：
 
- 系统环境变量OHOS_HDC_SERVER_PORT配置的hdc端口非默认端口8710。
- 当前user_config.xml设置的设备sn不存在。
- 用例的json文件type字段与当前设备不匹配。
- 用例的json文件设备label字段与当前设备不匹配。

 
 

##### 修改建议

- 将OHOS_HDC_SERVER_PORT环境变量删除后重启PyCharm。
- user_config.xml文件sn不设置或者修改为当前设备sn，type类型和label类型按实际使用设备配置正确。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/KMLeCDzjRJKg9XZsffCY8A/zh-cn_image_0000002658928769.png?HW-CC-KV=V1&HW-CC-Date=20260701T025922Z&HW-CC-Expire=86400&HW-CC-Sign=E9DD3A10ABA0CA118B19EE967FAB1D9B749CBFCE4A896C13F1C193ADBBF4B702)

- 用例的json文件type类型配置正确。如下图所示，该用例请求了两个设备，一个为HarmonyOS设备，一个为其他平台设备。
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/Y_QNd9RjQJyGVT_LBOqzzQ/zh-cn_image_0000002658808823.png?HW-CC-KV=V1&HW-CC-Date=20260701T025922Z&HW-CC-Expire=86400&HW-CC-Sign=B1E432A436D5B194CB98CF635543DBCCAC242F73FCD84F1626AAF8F977BFC499)

- 用例的json文件设备label类型配置每个设备对应的设备类型。如果用例可以在任何设备上运行，label字段不需要填。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/JmFJpMU8RlOYs5mNHdqYwQ/zh-cn_image_0000002628409556.png?HW-CC-KV=V1&HW-CC-Date=20260701T025922Z&HW-CC-Expire=86400&HW-CC-Sign=4884480A5C67598B42FFF5144A86B3B89AEE068F97A060271D1EEC046017AB47)
 
| label类型 | 设备 |
| --- | --- |
| phone | 手机 |
| car | 车机 |
| tv | 电视 |
| watch | 手表 |
| tablet | 平板 |
| 2in1 | PC |

 
 

##### 常见FAQ

Q：如何获取对应的设备类型？
 
A：通过hdc命令
 
```text
hdc shell param get const.product.devicetype
```
