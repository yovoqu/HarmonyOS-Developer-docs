# 基于Dockerfile部署ohpm-repo私仓

更新时间：2026-03-09 07:00:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-dockerfile

Dockerfile是构建Docker镜像的文本文件，其中包含了构建镜像的命令和说明，可以实现如下功能：


- 指定基础镜像。
- 创建项目目录。
- 修改config.yaml配置。
- 设置环境变量。
- 创建用户，设置文件权限。
- 运行install命令，更新环境变量。
- 运行start命令，启动私仓服务。

 本文档介绍在Linux系统中如何使用Docker命令搭建ohpm-repo私仓。

 **环境准备**


1. 下载[Docker镜像](https://www.docker.com/)，并进行环境搭建。
2. 下载ohpm-repo工具包，将下载的工具包重命名为ohpm-repo.zip，[点击链接获取](https://developer.huawei.com/consumer/cn/download/ohpm-repo)。

 **搭建私仓服务**


1. 浏览器访问IP地址8088，使用私仓服务。
