# Mac安装Python不修改环境变量

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-11

1. 下载官方Python Mac系统安装包，推荐使用 3.11.7。

2. Mac版本自定义安装可以不修改环境变量，请查看文档：在 macOS 上使用 Python不勾选UNIX command-line tools和shell profile updater。


![](assets/Mac安装Python不修改环境变量/file-20260515130347706-0.png)


3.  关闭DevEco Studio修改other.xml配置 。

```bash
cd ~/Library/Application\ Support/Huawei/DevEcoStudio6.0/options
```


```bash
vi other.xml
```

输入： /python，定位到location.python.path这一行, 修改后面的python路径为/Library/Frameworks/Python.framework/Versions/3.11/bin


![](assets/Mac安装Python不修改环境变量/file-20260515130347706-1.png)
