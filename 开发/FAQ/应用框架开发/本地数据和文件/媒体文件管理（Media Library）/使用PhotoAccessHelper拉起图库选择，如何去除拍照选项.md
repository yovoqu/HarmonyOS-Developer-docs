# 使用PhotoAccessHelper拉起图库选择，如何去除拍照选项

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-library-14

#### 问题现象

使用PhotoPicker拉起图库选择器，应该如何去除拍照选项只保留视频和图片的选择。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/QvkoM9VzRHKnUekJFv4oFg/zh-cn_image_0000002629059036.png?HW-CC-KV=V1&HW-CC-Date=20260701T041344Z&HW-CC-Expire=86400&HW-CC-Sign=ABF1889E8B383D504461F0A75DF15154F3C5BA8F77412A22F1DF193F27D85FC0)

 
 

#### 解决方案

开发者可以通过以下步骤实现去除拍照选项的效果：
 1. 使用[PhotoSelectOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-class#photoselectoptions)对象：在调用select方法时，使用PhotoSelectOptions对象来配置选择选项。该对象允许你指定媒体文件类型和其他相关参数。
2. 设置isPhotoTakingSupported参数：在PhotoSelectOptions对象中，设置isPhotoTakingSupported参数为false。当使用PhotoPicker时，拍照功能将不会被启用。
3. 调用select方法：使用配置好的PhotoSelectOptions对象调用select方法。该方法会拉起PhotoPicker界面，由于拍照功能被禁用，只能选择图片或视频，而无法进行拍照。
 
更多图库选项设置可参考[BaseSelectOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-class#baseselectoptions)。
