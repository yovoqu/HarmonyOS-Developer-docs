# AGC页面菜单缺失或点击菜单报错问题排查指导

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-6

## AGC页面菜单缺失或点击菜单报错问题排查指导
 


##### 问题现象

登录AGC页面进行操作时，有些菜单看不到、按钮点击无响应，无法进行下一步操作。比如邀请测试无法找到对应的“测试用户”菜单、发布应用时没有“提交审核”按钮、点击某些菜单会未知错误、点击某些菜单无响应等。
 
- 缺少提交审核按钮：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/RKCz9XSbQD28HankdCKTOA/zh-cn_image_0000002628394576.png?HW-CC-KV=V1&HW-CC-Date=20260701T025857Z&HW-CC-Expire=86400&HW-CC-Sign=9D7E98A2DD79393545B63F0F0656A4C88C59954CA5A27D7259B9690DCA742606)

- 缺少“测试用户”菜单：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/benglG7OTKa3J3F9LuaiGA/zh-cn_image_0000002628554466.png?HW-CC-KV=V1&HW-CC-Date=20260701T025857Z&HW-CC-Expire=86400&HW-CC-Sign=97F332119C8345E8121DCBEFB7D8BE286E930A05E551A3A7A608D5561D4C3784)

- 点击菜单报未知错误：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/_3xNMoBeS7Wf08gRrD4bpA/zh-cn_image_0000002658913791.png?HW-CC-KV=V1&HW-CC-Date=20260701T025857Z&HW-CC-Expire=86400&HW-CC-Sign=421125E4269C368CB19D4200B2A6409C8C33AFACA444229452EFC52966B1F321)

- 点击“应用分类”设置按钮无响应：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/akVWPdcBQjuQh7mbWuV9MQ/zh-cn_image_0000002658793847.png?HW-CC-KV=V1&HW-CC-Date=20260701T025857Z&HW-CC-Expire=86400&HW-CC-Sign=9F49994FE698DD8FE5729CF4BD8EB09625D2C55E412A72A497A101B21C942DD0)


 
 

##### 背景知识

- AGC是上架分发的入口，包含应用、项目、证书、个人信息等多个菜单栏，缺少部分菜单会影响开发者的操作。
- AGC的菜单展示依赖于登录的账号角色和权限，为方便管理，AGC提供了团队账号的功能，主账号可以根据成员的职责配置不同的角色。最高权限角色为“系统管理员”，其次还有“APP管理员”、“运营”、“客服”、“法务”等角色。不同角色又对应不同的权限，如“APP管理员”可以进行应用上架分发和测试，“运营”角色负责应用运营数据查看，“法务”角色负责协议签署等，具体可以参见[角色与权限列表](https://developer.huawei.com/consumer/cn/doc/app/agc-help-rolepermission-0000001155345429)。
- 为了方便进行页面的自定义布局，AGC还提供了菜单自定义功能，可以选择部分菜单展示或隐藏。

 
 

##### 问题定位

- 排查是否团队账号权限问题。
可以登录AGC，进入“用户与访问-个人信息”可以查看当前是否是团队账号，是何种角色，拥有哪个项目和应用的权限。

 
- 登录的账号角色是“账号持有者”，即主账号，拥有最高权限。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/vE9cvWXcTZ6cKB0UYW0nDA/zh-cn_image_0000002628394578.png?HW-CC-KV=V1&HW-CC-Date=20260701T025857Z&HW-CC-Expire=86400&HW-CC-Sign=F6CF6E7BAD2E109AC9F22882469E3816DD276C474C6A03BD1E93C3716D4EDE96)

- 登录的账号角色是“运营”、“开发”和“客服”，只能进行数据查看，不能进行应用上架。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/q3wWsqs5Rf-IJc-s1Fi1wA/zh-cn_image_0000002628554468.png?HW-CC-KV=V1&HW-CC-Date=20260701T025857Z&HW-CC-Expire=86400&HW-CC-Sign=529D0518B1520C824216EF5F2AF78377935C537A4DF5212B2C84132AE319E40F)


 - 排查是否进行了自定义菜单权限。AGC左下角有自定义菜单功能，选中的菜单右边的图钉时会展示菜单，不选中不展示。如“测试用户”菜单未选中时，左侧菜单栏不展示。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/kNHQwtTwS-C7Jejg0U_B2w/zh-cn_image_0000002658913793.png?HW-CC-KV=V1&HW-CC-Date=20260701T025857Z&HW-CC-Expire=86400&HW-CC-Sign=53FAC0712232C1376BA6818990097F4AB80921B0AEC496AA1976BC7D8A34AE46)

- 出现未知错误时，可以通过浏览器日志来获取具体的报错原因，打开浏览器日志（一般是按F12）->进入Network->选中报错的接口->查看报错信息描述。

 
 

##### 分析结论

- 排查是否是团队账号登录的AGC，如果是主账号，继续排查是否是进行了自定义菜单导致。
- 如果不是团队账号，查看角色是否合理，建议一般至少“APP管理员”以上才可以进行应用上架测试。联系主账号，将角色提高至“APP管理员”或者“管理员”。

 
 

##### 修改建议

- 登录[AGC平台首页](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，通过右上角个人账号位置点击[个人信息](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/ups/9249519184595931321)，在“角色管理”页签查看当前是否为团队账号，是何种角色，拥有哪个项目和应用的权限。建议至少“APP管理员”以上才具备应用管理权限，拥有上架测试、应用分类设置等权限。
- 在AGC左下角自定义菜单功能，查看是否没选择对应的菜单，如“测试用户”，如没选中，选中即可。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/E4ETY5DiTo-99Pc_PaxnIw/zh-cn_image_0000002658793849.png?HW-CC-KV=V1&HW-CC-Date=20260701T025857Z&HW-CC-Expire=86400&HW-CC-Sign=2ADFD9128A5CAF8635C799D7C39BC56FE69CD0DCFCA176564C6DF8CDD5247C21)

- 若出现未知错误，也可以通过浏览器日志查看是否是当前登录用户没有权限导致，如果使用了团队账号登录，登录的角色可能是开发或者运营，建议联系账号持有者提高权限，一般至少需要提高至APP管理员角色。然后退出账号重新登录再试一下。
