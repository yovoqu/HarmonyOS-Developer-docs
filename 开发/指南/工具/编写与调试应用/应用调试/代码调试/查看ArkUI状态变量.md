# 查看ArkUI状态变量

更新时间：2026-04-20 06:32:02

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkui-state

从DevEco Studio 6.0.2 Beta1版本开始，支持在调试时查看ArkUI状态变量的实时变化情况。
 
在调试窗口中，点击**Layout Settings**
![](assets/查看ArkUI状态变量/file-20260514133008193-0.png)
，勾选**ArkUI State**，打开ArkUI状态变量面板。
 

![](assets/查看ArkUI状态变量/file-20260514133008193-1.png)

 
状态变量面板分为总览（Summary）和当前值（Current Value）两个子面板：
 
- 总览面板显示了当前应用运行时，状态变量更新的总体情况，包含了状态变量的名称、更新次数、装饰器类型、所属组件、所属类、当前值。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/IgDByT9DRzmWCxq_QT-Xpw/zh-cn_image_0000002571386868.png?HW-CC-KV=V1&HW-CC-Date=20260528T014923Z&HW-CC-Expire=86400&HW-CC-Sign=75E85ACB12264F359E342B696073B7A7EBC6E138542D477D512661AE89960DC2)

- 当前值面板记录了状态变量实时变化的数据，包含了状态变量的更新时间、名称、所属组件、所属类、装饰器类型、当前值、影响的组件数量。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/-6DqZ4AESYupRQvENzjAJw/zh-cn_image_0000002602186033.png?HW-CC-KV=V1&HW-CC-Date=20260528T014923Z&HW-CC-Expire=86400&HW-CC-Sign=FF6E009FDCE936613C77204DB1B829B557FCD54E2D7EC005C87305B7C5A44940)
当点击右侧的箭头时，新弹出的面板将显示当前选中状态变量影响的组件列表，包含影响组件的组件名、组件ID、是否为自定义组件。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/CiPMsbN2SjSjFP1fVcSQAA/zh-cn_image_0000002602065979.png?HW-CC-KV=V1&HW-CC-Date=20260528T014923Z&HW-CC-Expire=86400&HW-CC-Sign=C20FC25F0AC28F18E170C31D15A62827C4F5F4178BFA3358570D1B1698A102E2)


 
> [!NOTE]
> 打开状态变量面板后才会开始监听状态变量的更新，因此，无法查看面板打开前状态变量的更新情况。 同一次调试过程中，关闭状态变量面板不会清空之前的数据，当前值面板最多展示1000条数据，超过限制后，仅展示最新的1000条数据。
