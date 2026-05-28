# 自定义提示词库（Prompts）配置

更新时间：2026-05-14 10:06:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-prompts

##### 功能介绍

从DevEco Studio 6.1.0 Beta2开始，CodeGenie支持添加和管理提示词库。如果经常针对不同的文件或代码使用某个提示词向AI提问，可以将提示词添加到常用提示词库中，在需要时通过菜单栏快速触发，从而提高开发效率。
 
 

##### 操作步骤
1. 点击页面右侧菜单栏CodeGenie图标完成登录后，可以通过如下两种方式打开Prompts配置界面：

  
点击界面右上方**Settings**
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/lYxbJBwpTearL0Kb6TWyAQ/zh-cn_image_0000002602186231.png?HW-CC-KV=V1&HW-CC-Date=20260528T015007Z&HW-CC-Expire=86400&HW-CC-Sign=5FE239B2B453460DDE3F36807BA02E0C48AEE3F137757DE7F3A875D6AAD3B278)
按钮，选择**Prompts**。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/NlTIOpDHQDuHmD-W0p4uXg/zh-cn_image_0000002602186243.png?HW-CC-KV=V1&HW-CC-Date=20260528T015007Z&HW-CC-Expire=86400&HW-CC-Sign=DF57A001E5BC66934FC0CF356ECC523961FAE933D27FF017143610CD71C750BE)

2. 在代码编辑区右键唤醒菜单栏，点击**CodeGenie > Add New Prompts**。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/eRYg70dDRbeV9NZ0T4c83Q/zh-cn_image_0000002571387076.png?HW-CC-KV=V1&HW-CC-Date=20260528T015007Z&HW-CC-Expire=86400&HW-CC-Sign=534271D59E9458E1B1B270789BF6DF8FEF00FFEB89B49B45651550EC7D19B1A2)

3. 点击**Add Now**进入Prompts配置页面。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/-7sb5sDiRv6Np3kq-axnvQ/zh-cn_image_0000002571387068.png?HW-CC-KV=V1&HW-CC-Date=20260528T015007Z&HW-CC-Expire=86400&HW-CC-Sign=C7426E25EDEB486452D3CDEDF7D9466DA7C1E433BE15F449F8867D0B107C5FB4)

4. 填写提示词名称、提示词内容等，点击**Save**进行保存。

  
**Title**：提示词名称，长度不超过20个字符。
5. **Prompt**：提示词的具体内容，长度不超过5000个字符。
6. **Auto-reference selected code for context**：是否自动引用所选代码作为上下文，勾选该选项后，会将选中代码和提示词一并发送给CodeGenie。
7. **Auto send prompts to AI**：是否自动发送给CodeGenie，不勾选该选项时需手动点击
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/4-yFiom0Qfqpw2jt_Pr9jA/zh-cn_image_0000002602186235.png?HW-CC-KV=V1&HW-CC-Date=20260528T015007Z&HW-CC-Expire=86400&HW-CC-Sign=53EA9FBBA172FEE3E81DA8DE67B7C2F20F2EF3928532D36B1724242E8A30C16C)
发送。
8. 选中代码片或在编辑区空白位置右键，点击CodeGenie下的提示词（如安全检查），发送提示词后等待AI解析回复。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/wNHhhSwYTfCPbRGjM15ZdA/zh-cn_image_0000002571387050.png?HW-CC-KV=V1&HW-CC-Date=20260528T015007Z&HW-CC-Expire=86400&HW-CC-Sign=AF8F4C4A753C2DE99658FC076328BE3EEF6B3797DD07CB355327D33661286BF9)
