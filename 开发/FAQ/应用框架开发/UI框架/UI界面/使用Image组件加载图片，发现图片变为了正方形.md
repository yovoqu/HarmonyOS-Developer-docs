# 使用Image组件加载图片，发现图片变为了正方形

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1149

## 使用Image组件加载图片，发现图片变为了正方形
 


##### 问题现象

使用Image加载图片，发现图片被压缩，且打印图片大小时发现，图片大小并非图片原本尺寸，而是高宽均为512像素尺寸。
 
错误现象展示如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/0Hiahax3RgiPX1pvHyszrA/zh-cn_image_0000002658928931.png?HW-CC-KV=V1&HW-CC-Date=20260701T025659Z&HW-CC-Expire=86400&HW-CC-Sign=240406F941598ED90CA43627BECF80DBAF63803161FF0F3FE178CF41F5736F0D)

 
正常现象展示如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/zYjHYlAGRpivEY9BwyX7oA/zh-cn_image_0000002658808975.png?HW-CC-KV=V1&HW-CC-Date=20260701T025659Z&HW-CC-Expire=86400&HW-CC-Sign=104027024B74D14CEA97263316905FB8B72314B2FE151BFF9DDBB7270A397676)

 
 

##### 背景知识

[module.json5配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)主要包含以下内容：
 
- module的基本配置信息，包含module名称、类型、描述、支持的设备类型等基本信息。
- 应用组件信息，包含UIAbility组件和ExtensionAbility组件的描述信息。
- 应用运行过程中所需的权限信息。

 
 

##### 问题定位

- 同一张图片，新建项目展示查看确认正常。
- 使用代码确认其尺寸，发现其尺寸被压缩到512像素尺寸。
- 全局搜索图片资源，发现该图片资源也被用于在module.json5中的icon属性引用。
- 修改module.json5的icon属性对该图片引用后，该图片应用内展示恢复正常。
- 重新设置icon属性复现之后，发现是编译打包后的HAP包内，该图片大小被压缩到512像素大小的正方形。

 
 

##### 分析结论

应该是因为该图片被设置为应用桌面图标后，IDE编译打包时将其压缩到512像素尺寸的正方形，而后续应用内使用也只能拿到压缩后的图片。
 
 

##### 修改建议

修改module.json5的icon属性，不要使用可能会在应用内使用的图片作为桌面应用图标。
