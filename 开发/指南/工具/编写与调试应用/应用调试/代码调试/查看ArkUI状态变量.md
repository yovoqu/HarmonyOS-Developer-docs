# 查看ArkUI状态变量

更新时间：2026-06-10 12:49:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkui-state

从DevEco Studio 6.0.2 Beta1版本开始，支持在调试时查看ArkUI状态变量的实时变化情况。
 
在调试窗口中，点击**Layout Settings**
![](assets/查看ArkUI状态变量/file-20260514133008193-0.png)
，勾选**ArkUI State**，打开ArkUI状态变量面板。
 

![](assets/查看ArkUI状态变量/file-20260514133008193-1.png)

 
状态变量面板分为总览（Summary）和当前值（Current Value）两个子面板：
 
- 总览面板显示了当前应用运行时，状态变量更新的总体情况，包含了状态变量的名称、更新次数、装饰器类型、所属组件、所属类、当前值。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/0LxZbJnbRvW7Z4u6LloDSA/zh-cn_image_0000002571386868.png?HW-CC-KV=V1&HW-CC-Date=20260611T074913Z&HW-CC-Expire=86400&HW-CC-Sign=5AD15C74661B32EA2B219AB5D95469E18CB878C3DEF9924D95710351192FC8B1)

- 当前值面板记录了状态变量实时变化的数据，包含了状态变量的更新时间、名称、所属组件、所属类、装饰器类型、当前值、影响的组件数量。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/aIgL7grZR1SX9vW7PQAUhA/zh-cn_image_0000002602186033.png?HW-CC-KV=V1&HW-CC-Date=20260611T074913Z&HW-CC-Expire=86400&HW-CC-Sign=832801FA1109F2C848FE04D177322DB1FF44CFC80F36AA9A3E06381965FE2BAE)
当点击右侧的箭头时，新弹出的面板将显示当前选中状态变量影响的组件列表，包含影响组件的组件名、组件ID、是否为自定义组件。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/XNqgXSAWRaWyJ5auaUz5Ng/zh-cn_image_0000002602065979.png?HW-CC-KV=V1&HW-CC-Date=20260611T074913Z&HW-CC-Expire=86400&HW-CC-Sign=16283801C9C7D32F1182E77EF49A5A9AB323BA6F2CBA15EB790ED5945236C6BD)


 
> [!NOTE]
> 打开状态变量面板后才会开始监听状态变量的更新，因此，无法查看面板打开前状态变量的更新情况。 同一次调试过程中，关闭状态变量面板不会清空之前的数据，当前值面板最多展示1000条数据，超过限制后，仅展示最新的1000条数据。
