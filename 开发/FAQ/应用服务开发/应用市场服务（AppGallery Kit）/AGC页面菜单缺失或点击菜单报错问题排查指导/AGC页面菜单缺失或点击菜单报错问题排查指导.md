# AGC页面菜单缺失或点击菜单报错问题排查指导

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-6

#### 问题现象

登录AGC页面进行操作时，有些菜单看不到、按钮点击无响应，无法进行下一步操作。比如邀请测试无法找到对应的“测试用户”菜单、发布应用时没有“提交审核”按钮、点击某些菜单会未知错误、点击某些菜单无响应等。
 
- 缺少提交审核按钮：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/nspVg3XiQ_GZC8Pt2-Mytg/zh-cn_image_0000002628394576.png?HW-CC-KV=V1&HW-CC-Date=20260811T005617Z&HW-CC-Expire=86400&HW-CC-Sign=745FE5BDCDD802594561A47ECCA13A80988EE28EC815386AD1D5015AE745B715)

- 缺少“测试用户”菜单：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/KTZrGALmS8mIYRzT7kM-QQ/zh-cn_image_0000002628554466.png?HW-CC-KV=V1&HW-CC-Date=20260811T005617Z&HW-CC-Expire=86400&HW-CC-Sign=A10CB42DB4A432A89492BC297EC53E61E31AFE06DAFA1A7368426BDFEE780A9B)

- 点击菜单报未知错误：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/B9SLu32ZQE2Xpa7xCtnRLA/zh-cn_image_0000002658913791.png?HW-CC-KV=V1&HW-CC-Date=20260811T005617Z&HW-CC-Expire=86400&HW-CC-Sign=45D629792FAB28F722E4F8BB3B01A81D108686E7EE54E214DBACD83F0BFB93E5)

- 点击“应用分类”设置按钮无响应：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/TPOzj1AtRuCDJnzrqcfx8A/zh-cn_image_0000002658793847.png?HW-CC-KV=V1&HW-CC-Date=20260811T005617Z&HW-CC-Expire=86400&HW-CC-Sign=AFA28647546609E07F76A5E14ACA3E50FED425C9DD37DD1172678C5CD1A92FC7)


 
 

#### 背景知识
1. AGC是上架分发的入口，包含应用、项目、证书、个人信息等多个菜单栏，缺少部分菜单会影响开发者的操作。
2. AGC的菜单展示依赖于登录的账号角色和权限，为方便管理，AGC提供了团队账号的功能，主账号可以根据成员的职责配置不同的角色。最高权限角色为“系统管理员”，其次还有“APP管理员”、“运营”、“客服”、“法务”等角色。不同角色又对应不同的权限，如“APP管理员”可以进行应用上架分发和测试，“运营”角色负责应用运营数据查看，“法务”角色负责协议签署等，具体可以参见[角色与权限列表](https://developer.huawei.com/consumer/cn/doc/app/agc-help-rolepermission-0000001155345429)。
3. 为了方便进行页面的自定义布局，AGC还提供了菜单自定义功能，可以选择部分菜单展示或隐藏。
 
 

#### 问题定位
1. 排查是否团队账号权限问题。
可以登录AGC，进入“用户与访问-个人信息”可以查看当前是否是团队账号，是何种角色，拥有哪个项目和应用的权限。
2. 登录的账号角色是“账号持有者”，即主账号，拥有最高权限。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/ZOoVITGQRCGbNdAmcmEA5Q/zh-cn_image_0000002628394578.png?HW-CC-KV=V1&HW-CC-Date=20260811T005617Z&HW-CC-Expire=86400&HW-CC-Sign=AE5229CC8AC6D59E9B2DC6408FEA9716DF57C2AF87250F4421AD23FB04049EB3)

3. 登录的账号角色是“运营”、“开发”和“客服”，只能进行数据查看，不能进行应用上架。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/wSyTJdj1ScSgSPu3QRATDQ/zh-cn_image_0000002628554468.png?HW-CC-KV=V1&HW-CC-Date=20260811T005617Z&HW-CC-Expire=86400&HW-CC-Sign=526146854866834EDEBBD8F5A61C0093A6270CAF836408DB73312E4136A565A0)

4. 排查是否进行了自定义菜单权限。AGC左下角有自定义菜单功能，选中的菜单右边的图钉时会展示菜单，不选中不展示。如“测试用户”菜单未选中时，左侧菜单栏不展示。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/ZIiChshIQxaixSV7b8OJlw/zh-cn_image_0000002658913793.png?HW-CC-KV=V1&HW-CC-Date=20260811T005617Z&HW-CC-Expire=86400&HW-CC-Sign=A6C7562540EFB6DEB22524908D14426F28F1C2F84AA6291ED888F04CA09E2548)

5. 出现未知错误时，可以通过浏览器日志来获取具体的报错原因，打开浏览器日志（一般是按F12）->进入Network->选中报错的接口->查看报错信息描述。
 
 

#### 分析结论
1. 排查是否是团队账号登录的AGC，如果是主账号，继续排查是否是进行了自定义菜单导致。
2. 如果不是团队账号，查看角色是否合理，建议一般至少“APP管理员”以上才可以进行应用上架测试。联系主账号，将角色提高至“APP管理员”或者“管理员”。
 
 

#### 修改建议
1. 登录[AGC平台首页](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，通过右上角个人账号位置点击[个人信息](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/ups/9249519184595931321)，在“角色管理”页签查看当前是否为团队账号，是何种角色，拥有哪个项目和应用的权限。建议至少“APP管理员”以上才具备应用管理权限，拥有上架测试、应用分类设置等权限。
2. 在AGC左下角自定义菜单功能，查看是否没选择对应的菜单，如“测试用户”，如没选中，选中即可。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/scQuI9yoSmGlC1Lu_CVIKA/zh-cn_image_0000002658793849.png?HW-CC-KV=V1&HW-CC-Date=20260811T005617Z&HW-CC-Expire=86400&HW-CC-Sign=A000D5F799D51E88DF8EA80E5962CC9D8BEBEBDE276110673890C6294E2DA550)

3. 若出现未知错误，也可以通过浏览器日志查看是否是当前登录用户没有权限导致，如果使用了团队账号登录，登录的角色可能是开发或者运营，建议联系账号持有者提高权限，一般至少需要提高至APP管理员角色。然后退出账号重新登录再试一下。
