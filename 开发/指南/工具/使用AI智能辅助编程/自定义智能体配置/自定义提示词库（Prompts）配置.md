# 自定义提示词库（Prompts）配置

更新时间：2026-05-14 10:06:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-prompts

#### 功能介绍

从DevEco Studio 6.1.0 Beta2开始，CodeGenie支持添加和管理提示词库。如果经常针对不同的文件或代码使用某个提示词向AI提问，可以将提示词添加到常用提示词库中，在需要时通过菜单栏快速触发，从而提高开发效率。
 
 

#### 操作步骤
1. 点击页面右侧菜单栏CodeGenie图标完成登录后，可以通过如下两种方式打开Prompts配置界面：

  
点击界面右上方**Settings**
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/Hkdr72kRRFyKe8n2863zdg/zh-cn_image_0000002602186231.png?HW-CC-KV=V1&HW-CC-Date=20260528T030637Z&HW-CC-Expire=86400&HW-CC-Sign=5B084644AC4A99739AA68B791570CE07DB0A1DE42AC5EB4742F18F67193CF8D8)
按钮，选择**Prompts**。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/IciraaBARYuMRxk4ZrVfcQ/zh-cn_image_0000002602186243.png?HW-CC-KV=V1&HW-CC-Date=20260528T030637Z&HW-CC-Expire=86400&HW-CC-Sign=E2F346803CCDF22E482F033BE80630C8D49DF7F1746B35D5533C0709D9C0B549)

2. 在代码编辑区右键唤醒菜单栏，点击**CodeGenie > Add New Prompts**。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/MSXwRyGpRHu13X-W3EQ6eg/zh-cn_image_0000002571387076.png?HW-CC-KV=V1&HW-CC-Date=20260528T030637Z&HW-CC-Expire=86400&HW-CC-Sign=70D8B0842894545E15AB0B86DF0BAAFC55509D48B958A61B5F4390C347935205)

3. 点击**Add Now**进入Prompts配置页面。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/t3IQnnjvRtSg4xDxLWs7Rg/zh-cn_image_0000002571387068.png?HW-CC-KV=V1&HW-CC-Date=20260528T030637Z&HW-CC-Expire=86400&HW-CC-Sign=A867A31EC65BC9AA7A8975298359A9DEA18FF9F3B71BCC6245561413E74E9A41)

4. 填写提示词名称、提示词内容等，点击**Save**进行保存。

  
**Title**：提示词名称，长度不超过20个字符。
5. **Prompt**：提示词的具体内容，长度不超过5000个字符。
6. **Auto-reference selected code for context**：是否自动引用所选代码作为上下文，勾选该选项后，会将选中代码和提示词一并发送给CodeGenie。
7. **Auto send prompts to AI**：是否自动发送给CodeGenie，不勾选该选项时需手动点击
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/QcomMZGZRhqY7GI_NyFTrw/zh-cn_image_0000002602186235.png?HW-CC-KV=V1&HW-CC-Date=20260528T030637Z&HW-CC-Expire=86400&HW-CC-Sign=4625123BF3E3454C980480086B0292CBE1977C6C4849EF11A6EB6F3D4E976053)
发送。
8. 选中代码片或在编辑区空白位置右键，点击CodeGenie下的提示词（如安全检查），发送提示词后等待AI解析回复。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/kuC5LpCaRrqArMvJDfeRBA/zh-cn_image_0000002571387050.png?HW-CC-KV=V1&HW-CC-Date=20260528T030637Z&HW-CC-Expire=86400&HW-CC-Sign=18C8475D24299490489FE4FD59512989B3C5E33F3EE986BF6A23F279198B1D47)
