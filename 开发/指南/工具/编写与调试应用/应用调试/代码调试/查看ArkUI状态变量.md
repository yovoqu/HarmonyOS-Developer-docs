# 查看ArkUI状态变量

更新时间：2026-06-12 06:54:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkui-state

从DevEco Studio 6.0.2 Beta1版本开始，支持在调试时查看ArkUI状态变量的实时变化情况。
 
在调试窗口中，点击**Layout Settings**
![](assets/查看ArkUI状态变量/file-20260514133008193-0.png)
，勾选**ArkUI State**，打开ArkUI状态变量面板。
 

![](assets/查看ArkUI状态变量/file-20260514133008193-1.png)

 
状态变量面板分为总览（Summary）和当前值（Current Value）两个子面板：
 
- 总览面板显示了当前应用运行时，状态变量更新的总体情况，包含了状态变量的名称、更新次数、装饰器类型、所属组件、所属类、当前值。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/AMTQJT_qT7uLFh7ebDL0WQ/zh-cn_image_0000002624993697.png?HW-CC-KV=V1&HW-CC-Date=20260624T020712Z&HW-CC-Expire=86400&HW-CC-Sign=A5B8A4EFEB5DC5827D4A2FE4AFE56010468B14A0871FCCC830BC1F5003748957)

- 当前值面板记录了状态变量实时变化的数据，包含了状态变量的更新时间、名称、所属组件、所属类、装饰器类型、当前值、影响的组件数量。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/UTSHlwruQaeUA1CngXV5_g/zh-cn_image_0000002625073837.png?HW-CC-KV=V1&HW-CC-Date=20260624T020712Z&HW-CC-Expire=86400&HW-CC-Sign=0D0FA07828A7344982D5AE9ED396D8D8A5A720D6A2FE57E17319FD86DFA087F0)
当点击右侧的箭头时，新弹出的面板将显示当前选中状态变量影响的组件列表，包含影响组件的组件名、组件ID、是否为自定义组件。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/6dQp-jNoSQ-avu7E_rimpg/zh-cn_image_0000002624993691.png?HW-CC-KV=V1&HW-CC-Date=20260624T020712Z&HW-CC-Expire=86400&HW-CC-Sign=4A35D0B724A7A8CC39BB72A2D05EDD66E59724297C53B64E4058BADB2272E5B4)


 
> [!NOTE]
> 打开状态变量面板后才会开始监听状态变量的更新，因此，无法查看面板打开前状态变量的更新情况。 同一次调试过程中，关闭状态变量面板不会清空之前的数据，当前值面板最多展示1000条数据，超过限制后，仅展示最新的1000条数据。
