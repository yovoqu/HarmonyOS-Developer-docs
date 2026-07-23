# ohpm私仓安装私有SDK失败

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-20

#### 问题现象

本地搭建了一个ohpm私仓，上传了一些私有的SDK。执行ohpm install后，会先在当前的源上下载没安装的SDK，导致install失败。
 
 

#### 背景知识

[ohpm私仓搭建](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo)：ohpm-repo是一个搭建轻量级的ohpm私仓服务的工具。它与ohpm包管理器兼容，并按需缓存所有依赖项，加速私有网络中的安装。
 
 

#### 解决方案

在ohpm中，可以通过配置文件.ohpmrc文件来配置多个私有仓库和公共仓库。
 1. 打开项目的ohpm配置文件，可以通过IDE的settings查找文件所在位置：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/qJfPT-lVTw2OKr7LWOOPHA/zh-cn_image_0000002628409724.png?HW-CC-KV=V1&HW-CC-Date=20260723T014011Z&HW-CC-Expire=86400&HW-CC-Sign=25E07B0881D065C1F4BF7BFB97F0D3C7B7514049619BF4B10B7501459A774E4B)

2. 添加仓库地址配置：通过@group:registry语法，为特定作用域的包指定专属registry。

  在配置文件.ohpmrc中增加如下配置：

  
```text
公共仓库：registry=https://ohpm.openharmony.cn/ohpm/
私有仓库1：@group1:registry=https://registry.group1.com/ohpm/
私有仓库2：@group2:registry=https://registry.group2.com/ohpm/
```

3. 在oh-package.json5中引入依赖时需要在包名增加前缀匹配"@group1/abc": "1.0.0"。
