# DevEco Testing Hypium中的UiViewer使用中的常见问题和解决方案

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-31

#### 问题现象

使用[DevEco Testing Hypium](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hypium-python-guidelines#section16890204264419)插件展开UiViewer功能面板，提示“获取视频流失败，请重新选择设备进入”，如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/pFlVd5o7T-OzaFKGNehnsQ/zh-cn_image_0000002628409626.png?HW-CC-KV=V1&HW-CC-Date=20260701T041009Z&HW-CC-Expire=86400&HW-CC-Sign=53C1F9DA3A116EEFCE4EDE6CF9086149365C37CF7AEB2E7E87EC1C72A3691760)

 
 

#### 背景知识

PyCharm界面右侧栏的toolWindow区域可见UiViewer标签，点击后展开UiViewer面板。UiViewer功能目前分为4个界面：设备选择界面、单设备控件查看界面、单设备投屏界面、双设备投屏界面。详情请参考[安装向导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hypium-python-guidelines#section191615399595)的UiViewer功能模块。
 
 

#### 问题定位

- 查看插件版本是否为Hypium的新版本。打开PyCharm的settings->Plugins查看版本号。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/fP_1gORaRNaqhMzSH6tyNA/zh-cn_image_0000002658808885.png?HW-CC-KV=V1&HW-CC-Date=20260701T041009Z&HW-CC-Expire=86400&HW-CC-Sign=5FB3A98D61D32CD31A0BD4FE881A77A7C9712B844F589884D5C478F11CBE58EC)

- 查看设备视频流设置。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/qKI0Z9LJSaiVHLHw3UVN1w/zh-cn_image_0000002628569518.png?HW-CC-KV=V1&HW-CC-Date=20260701T041009Z&HW-CC-Expire=86400&HW-CC-Sign=EE15D0C444043BDDDDE91886797F2D54DC7521BD72510BFFA43AAA61C1F81B29)


 
 

#### 分析结论

- 插件版本未更新，导致投屏失败。
- 无法获取设备视频流。

 
 

#### 修改建议

- 更新当前插件版本为适配Hypium新版本。访问华为开发者联盟官网下载[DevEco Testing Hypium安装包](https://developer.huawei.com/consumer/cn/download/deveco-testing-hypium)，下载解压后找到其中的hypium-5.0.7.200.zip(请以实际版本号为准)。DevEco Testing Hypium离线安装包请参考[安装向导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hypium-python-guidelines#section191615399595)的安装包离线安装模块。
- 使用视频流投屏模式设置。将PyCharm的settings->DevEco Testing Hypium->UiViewer的是否使用视频流投屏模式设置为否，再重新使用插件进行手机投屏。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/rO4jkl21TNe9SCmSD7LVIg/zh-cn_image_0000002658928841.png?HW-CC-KV=V1&HW-CC-Date=20260701T041009Z&HW-CC-Expire=86400&HW-CC-Sign=54770ACA3E5C711EA369EE5CC8C3BF2F1F1359ED21DE43BD36D2EEABED02DE97)


 
 

#### 常见FAQ

Q：PyCharm专业版使用DevEco Testing Hypium时，UiViewer无法看到设备如何解决？
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/IQVwsDIzQSuHuI1pwgiUwA/zh-cn_image_0000002628409628.png?HW-CC-KV=V1&HW-CC-Date=20260701T041009Z&HW-CC-Expire=86400&HW-CC-Sign=A96A9E530F69D5AF2A8D2E0AA82CAEE9CE233C304ED8D3347263E1E380092F65)

 
A：检查系统环境变量[OHOS_HDC_SERVER_PORT](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hdc#ohos_hdc_server_port)：如果电脑的8710端口已经被使用或希望使用其他端口，可以通过添加环境变量OHOS_HDC_SERVER_PORT到系统环境变量中来修改服务器进程启动时监听的端口号，设置完之后重启PyCharm。
