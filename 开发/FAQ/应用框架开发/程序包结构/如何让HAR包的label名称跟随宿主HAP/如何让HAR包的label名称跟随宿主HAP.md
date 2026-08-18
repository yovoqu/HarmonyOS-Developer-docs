# 如何让HAR包的label名称跟随宿主HAP

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-79

#### 问题现象

HAP包集成HAR包，HAR包中的UIAbility进入后台任务列表界面时显示的label名称不跟随HAP包，如下图所示。如何让HAR包的label名称跟随HAP包的label名称呢？
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/5ZPnBM23TZ26WOT2mceuLg/zh-cn_image_0000002658987445.png?HW-CC-KV=V1&HW-CC-Date=20260811T005852Z&HW-CC-Expire=86400&HW-CC-Sign=66201D017C4F6AFFE6C2AD0CBC10805B3587D4EEB931D01B870B08C71B1014F4)

 
 

#### 效果预览

配置后可以看到HAR包的label名称跟随了HAP包：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/CKjDzxxPQya7gkBuM2C-QA/zh-cn_image_0000002628628224.png?HW-CC-KV=V1&HW-CC-Date=20260811T005852Z&HW-CC-Expire=86400&HW-CC-Sign=263C49C760F12E1351050D316A8E30AA744DEB8C19E112B7C4D429DC30E4F19C)

 
 

#### 背景知识

- label：标识当前UIAbility组件对用户显示的名称，取值为字符串资源的索引。详见[abilities标签](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#abilities标签)中的label字段。
- [HAR](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/har-package)（Harmony Archive）是静态共享包，可以包含代码、C++库、资源和配置文件。通过HAR可以实现多个模块或多个工程共享ArkUI组件、资源等相关代码。
- 在编译构建HAP时，DevEco Studio会从HAP模块及依赖的模块中收集资源文件，如果不同模块下的资源文件出现重名冲突时，DevEco Studio会按照以下优先级进行覆盖（优先级由高到低）：AppScope（仅Stage模型支持）->HAP包自身模块->依赖的HAR模块。详情参考[导出资源](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/har-package#导出资源)。

 
 

#### 解决方案

出现该情况主要是由于HAR包中的UIAbility使用的是HAR包中的label资源，没有使用宿主HAP包的资源导致，所以会展示为HAR包的label名称。
 
由背景知识中可知，可以在HAP中配置和HAR中重名的label字段，这样根据优先级覆盖原则：AppScope（仅Stage模型支持）->HAP包自身模块->依赖的HAR模块，HAR中使用的就是HAP中的所配置的label资源。
 
具体修改步骤如下：
 1. 在HAR模块的string.json中配置HAR包的label字段“Ability_label”，并在HAR模块的module.json5文件中abilities标签下的label字段中被引用。

  HAR string.json：
```json
{
  "string": [
    {
      "name": "page_show",
      "value": "page from package"
    },
    {
      "name": "HarAbility_desc",
      "value": "description"
    },
    {
      "name": "Ability_label",
      "value": "HAR"
    }
  ]
}
```


  HAR module.json5：

  
```json
"label": "$string:Ability_label",
```

2. 在HAP包的string.json中配置与HAR包中label相同字段名的“Ability_label”，并在HAP包的module.json5文件中abilities标签下的label字段中被引用。HAP string.json：

  
```json
{
  "string": [
    {
      "name": "module_desc",
      "value": "module description"
    },
    {
      "name": "EntryAbility_desc",
      "value": "description"
    },
    {
      "name": "Ability_label",
      "value": "APP"
    }
  ]
}
```
 HAP module.json5：

  
```json
"label": "$string:Ability_label",
```

 
 

#### 总结

可以利用资源优先级覆盖原则，在HAP中配置和HAR包同名label字段，使得HAR包的label名称跟随宿主HAP。
