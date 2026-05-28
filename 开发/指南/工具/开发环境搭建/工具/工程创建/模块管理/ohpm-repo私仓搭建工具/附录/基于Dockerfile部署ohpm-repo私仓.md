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
3. 将Dockerfile文件和ohpm-repo.zip放在同一目录下。

  Dockerfile文件模板如下：
```text
<em># 使用官方 Node.js 18 镜像</em>
<span style="color: rgb(0,0,255);">FROM</span> node:18
<span style="color: rgb(0,0,255);">COPY</span> ./ohpm-repo.zip /tmp/ohpm-repo.zip
<span style="color: rgb(0,0,255);">RUN</span> mkdir -p /opt/ohpm-repo && \
    unzip /tmp/ohpm-repo.zip -d /opt/ohpm-repo && \
    rm -f /tmp/ohpm-repo.zip
<em># 修改conf/config.yaml的listen配置，不能用localhost和127.0.0.1，必须使用0.0.0.0</em>
<span style="color: rgb(0,0,255);">RUN</span> if [ -f /opt/ohpm-repo/conf/config.yaml ]; then \
      sed -i 's/listen: [^ ]*/listen: 0.0.0.0:8088/g' /opt/ohpm-repo/conf/config.yaml; \
    fi
<span style="color: rgb(0,0,255);">ENV</span> OHPM_REPO_BIN_DIR=<span style="color: rgb(80,160,79);">"/opt/ohpm-repo/bin"</span>
<span style="color: rgb(0,0,255);">ENV</span> PATH=<span style="color: rgb(80,160,79);">"${OHPM_REPO_BIN_DIR}:${PATH}"</span>
<em># 创建用户，不允许使用root用户来运行ohpm-repo install和ohpm-repo start命令</em>
<span style="color: rgb(0,0,255);">RUN</span> useradd -m myuser && \
    chown -R myuser:myuser /opt/ohpm-repo && \ 
    chmod -R 755 /opt/ohpm-repo
<span style="color: rgb(0,0,255);">USER</span> myuser
<span style="color: rgb(0,0,255);">RUN</span> ohpm-repo install
<span style="color: rgb(0,0,255);">ENV</span> OHPM_REPO_DEPLOY_ROOT=<span style="color: rgb(80,160,79);">"/home/myuser/ohpm-repo"</span>
<span style="color: rgb(0,0,255);">CMD</span> [<span style="color: rgb(80,160,79);">"ohpm-repo"</span>, <span style="color: rgb(80,160,79);">"start"</span>]
```

 
**搭建私仓服务**
 1. 在当前Dockerfile文件目录下，构建镜像。
```text
docker build -t ohpm-repo .
```

2. 启动服务，包括前台运行命令、后台运行命令两种形式。
```text
<em># </em>前台运行命令
docker run -it -p 8088:8088 ohpm-repo
<em># </em>后台运行命令
docker run -d --restart=unless-stopped --name ohpm-repo -p 8088:8088 ohpm-repo
```

3. 浏览器访问IP地址8088，使用私仓服务。
