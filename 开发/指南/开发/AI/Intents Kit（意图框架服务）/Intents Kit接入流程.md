# Intents Kit接入流程

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-access-flow

![](assets/Intents%20Kit接入流程/file-20260514132626656-0.png)

 
**阶段一：意向**
  
| 任务 | 任务描述 | 示例 | 指导文档 |
| --- | --- | --- | --- |
| 选择特性确定意图 | 开发者根据想达成的用户体验，确定好涉及的系统入口和特性类型，基于已发布的特性列表选择需实现的意图。如果已发布的特性列表中没能找到合适的意图，则只需要确定好系统入口和特性类型即可。 | 开发者想实现“歌曲续听推荐”的特性，根据智慧分发特性的场景描述，该特性属于小艺建议系统入口下的习惯推荐特性类型，需要实现“播放歌曲”意图。 | 歌曲续听推荐 |
| 能力申请 | 确定好特性后，开发者在AppGallery Connect平台上提交对应特性类型的能力申请。 | 见下文图示。 | / |
 
 
**能力申请步骤**
 1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，选择“开发与服务”，在项目列表选择项目。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/iMRtztANQhmuaVLrab5OTg/zh-cn_image_0000002581435410.png?HW-CC-KV=V1&HW-CC-Date=20260528T025922Z&HW-CC-Expire=86400&HW-CC-Sign=2EF3EEFF2E921FD4A3303AF45C24B5383CA311DCEB03BEFCEF2BF7E60AE87905)

2. 选择项目后，选择需要申请开通能力的应用。
3. 进入“项目设置 > 开放能力管理”页面，点击“意图框架”对应能力的“申请”。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/xPBTbqS_RpiZRhkFKCfwMQ/zh-cn_image_0000002611835239.png?HW-CC-KV=V1&HW-CC-Date=20260528T025922Z&HW-CC-Expire=86400&HW-CC-Sign=D7E940D1F4D8BB7779B684909077161154A8B5AC94B32B9324939AD75BC90570)

4. 参考“申请原因”中的模版，提供必要的申请信息，然后点击“提交”按钮。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/wMBZuI_UT3GJ8rhtmNe86g/zh-cn_image_0000002581275492.png?HW-CC-KV=V1&HW-CC-Date=20260528T025922Z&HW-CC-Expire=86400&HW-CC-Sign=6CA0A0E4A955E1DE1CA946437F8C184C01E14C64FD8F8FDDE8E164DE55A310A6)

5. 返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果。申请结果请留意互动中心的“服务开通申请”信息。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/SYcoZS0-Q42Wu6XVIttiEg/zh-cn_image_0000002611755349.png?HW-CC-KV=V1&HW-CC-Date=20260528T025922Z&HW-CC-Expire=86400&HW-CC-Sign=CE92422CBBA0104A38FEA6B7A9C0F2496C5A89AE0DDBB10D2D3669634905ACB5)

 
**阶段二：开发**
  
| 任务 | 任务描述 | 示例 | 指导文档 |
| --- | --- | --- | --- |
| 意图调试申请 | 申请能力通过后，开发者可根据审核成功的反馈提示，提供测试应用的信息，用于开通意图调试权限。 | 1. 应用名称：华为音乐。 2. 应用包名：com.xxxx。 3. 接入意图名称：“播放歌曲”。 4. 应用图标：jpg、png……。 5. APP ID：1234567。 6. Client ID：1234567。 7. 华为账号（UID）：1234567、7654321……。 | 见各特性类型 习惯推荐：开发者测试 事件推荐：开发者测试 技能调用：开发者测试 |
| 意图声明文件中注册意图 | 在DevEco Studio中开发时，注册对应的意图。 | 注册“播放歌曲”意图。 | 意图注册 |
| 开发实现意图共享 | 开发应用/元服务的意图共享接口，使其可以通过HarmonyOS接口完成意图数据共享。 | 开发“播放歌曲”意图中的意图共享接口。 | 端侧意图共享 |
| 开发实现意图调用 | 开发应用/元服务的意图调用接口，使其可以通过HarmonyOS接口被正确调用。 | 开发“播放歌曲”意图中的意图调用接口。 | 端侧意图调用 |
 
 
**阶段三：验证**
  
| 任务 | 任务描述 | 示例 | 指导文档 |
| --- | --- | --- | --- |
| 端到端验证特性 | 使用华为侧提供的测试能力完成目标特性的端到端联调测试，联调测试完成后，提交智慧分发配置至审核。 | 在设备上对应入口进行“华为音乐-歌曲续听推荐”的特性端到端测试，测试完成后点击提交智慧分发配置。 | / |
 
 
**阶段四：上架**
  
| 任务 | 任务描述 | 示例 | 指导文档 |
| --- | --- | --- | --- |
| 应用市场上架软件包（应用/元服务） | 开发完成并打包好软件包后，在应用市场上传软件包。 | 打包“华为音乐”软件包并通过应用市场上架。 | 应用市场上架流程 |
| 意图框架注册 | 在小艺开放平台进行意图注册配置并提交审核。由华为工程师审核，一般情况在3个工作日内完成。 | 注册“播放歌曲”意图。 | 意图标准协议上架指导 |
