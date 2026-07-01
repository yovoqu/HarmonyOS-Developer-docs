# 如何通过USB线将手机相册里面图片传到电脑上

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-21

#### 问题现象

手机通过截图、拍照等生成保存在相册中的图片，如何通过USB线将图片传到电脑上？
 
 

#### 背景知识

[mediatool](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mediatool)是一个轻量级的命令行工具集合，开发者可通过此工具操作媒体库资源。媒体库为图库提供和管理数据，媒体库中的图片、视频会在图库界面呈现。
 
mediatool工具为系统自带工具，不需要安装，内置在/bin文件夹中，可以通过hdc shell直接调用。
 
 

#### 解决方案

方案一：通过[mediatool](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mediatool)工具来导出图片。
 1. [导出指定图片](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mediatool#导出特定媒体库资产)。
2. [导出所有媒体库资源](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mediatool#导出所有媒体库资产)。
 
方案二：通过DevEco Studio导出。
 1. 选择【图库】中的照片，点击分享-复制，然后打开【文件管理】后根据提示，粘贴到我的手机-Download路径下。
2. 打开DevEco Studio的Device File Browser，在/storage/media/100/local/files/Docs/Download路径下即可看到对应的图片，右键另存为保存到电脑上。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/JhIflkVhR_SoNtHNxO8qqw/zh-cn_image_0000002628569626.png?HW-CC-KV=V1&HW-CC-Date=20260701T041008Z&HW-CC-Expire=86400&HW-CC-Sign=E2F57817EBB4F0DBEBBE922337D088D3BFB79D4DFAA5BE1429C5B5DEDA070B7E)
