# 如何获取当前最前台UI界面的应用包名

更新时间：2026-07-22 12:10:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-37

#### 问题现象

如何获取当前最前台UI界面所属应用的信息（如包名）？通过hdc shell aa dump -l或hdc shell aa dump -a命令只能获取最近运行应用的包名，无法准确获取当前最前台UI界面的包名。
 
 

#### 背景知识

使用[hdc](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hdc)工具可以与设备进行交互调试。[uitest dumpLayout](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-uitest#dumplayout)命令可以导出当前页面的布局信息，其中包含当前最前台UI界面对应的应用信息。
 
 

#### 解决方案

通过uitest dumpLayout命令获取最前台UI界面应用信息。
 1. 执行以下hdc命令，在设备的/data/local/tmp目录下生成布局信息的JSON文件：
```bash
hdc shell uitest dumpLayout
```

2. 通过DevEco Device File Browser（DevEco Studio右侧边工具栏的设备文件浏览器）查看/data/local/tmp目录下的layout_xxx.json文件。
3. 在JSON文件中，type为root的节点的attributes属性展示了当前页面对应的应用信息，包括abilityName、bundleName以及当前页面对应的页面路径PagePath。
 
更多详细信息可参考[文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-52)。
