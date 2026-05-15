# 运行时提示“Hdc server port XXXX has been used”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-19

问题现象

在设备中运行HAP时，提示“Hdc server port XXXX已被使用。请配置环境变量‘OHOS_HDC_SERVER_PORT’并重启DevEco Studio。”


![](assets/运行时提示“Hdc%20server%20port%20XXXX%20has%20been%20used”/file-20260515130310451-0.png)


解决措施

HDC的默认端口8710导致服务无法启动。解决方法如下：

方式一：结束掉占用该端口的应用。

1. 运行CMD命令行工具，输入“netstat -ano | findstr *端口号*”，查询占用端口号的进程PID。
![](assets/运行时提示“Hdc%20server%20port%20XXXX%20has%20been%20used”/file-20260515130310451-1.png)
2. 打开任务管理器，选择详细信息页，查看PID对应的应用。
![](assets/运行时提示“Hdc%20server%20port%20XXXX%20has%20been%20used”/file-20260515130310451-2.png)
3. 结束掉对应应用后，重启DevEco Studio。


方式二：为HDC端口号设置其他的环境变量。

- Windows环境变量设置方法：在**此电脑 > 属性 > 高级系统设置 > 高级 > 环境变量**中，添加变量名OHOS_HDC_SERVER_PORT，变量值设置为任意未占用的端口，例如7035。
![](assets/运行时提示“Hdc%20server%20port%20XXXX%20has%20been%20used”/file-20260515130310451-3.png)
环境变量配置完成后，关闭并重启DevEco Studio。
- macOS环境变量设置方法：打开终端，执行以下命令，根据输出结果执行不同命令。
```bash
echo $SHELL
```
 如果输出结果为/bin/bash，则执行以下命令以打开.bash_profile文件。
```bash
vi ~/.bash_profile
```
- 如果输出结果为/bin/zsh，则执行以下命令以打开.zshrc文件。
```bash
vi ~/.zshrc
```

 按字母“i”，进入Insert模式。输入以下内容，添加OHOS_HDC_SERVER_PORT端口信息。
```text
OHOS_HDC_SERVER_PORT=7035
launchctl setenv OHOS_HDC_SERVER_PORT $OHOS_HDC_SERVER_PORT
export OHOS_HDC_SERVER_PORT
```
 编辑完成后，单击Esc键退出编辑模式，然后输入“:wq”并单击Enter键保存。执行以下命令，使环境变量生效。
- 如果[步骤1](#zh-cn_topic_0000001166752005_li1264071053012)打开的是.bash_profile文件，请执行如下命令：
```bash
source ~/.bash_profile
```
- 如果[步骤1](#zh-cn_topic_0000001166752005_li1264071053012)打开的是.zshrc文件，请执行如下命令：
```bash
source ~/.zshrc
```

 环境变量配置完成后，关闭并重启DevEco Studio。
方式三：如果查询端口未被占用，检查端口是否被防火墙拦截。如果被拦截，放行端口，然后重启DevEco Studio重新尝试。
